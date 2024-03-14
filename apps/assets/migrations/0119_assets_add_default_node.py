# Generated by Django 3.2.19 on 2023-06-05 06:28

from django.db import migrations


# 历史问题一些资产没有关联到节点，这里将这些资产关联到默认节点
def migrate_asset_add_default_node(apps, *args):
    node_model = apps.get_model('assets', 'Node')
    asset_model = apps.get_model('assets', 'Asset')
    m2m_model = asset_model.nodes.through
    assets = asset_model.objects.filter(nodes__isnull=True).only('id', 'org_id')
    org_assets_map = {}
    for asset in assets:
        org_assets_map.setdefault(str(asset.org_id), []).append(str(asset.id))

    if not org_assets_map:
        return

    m2m_objs = []
    for org_id, asset_ids in org_assets_map.items():
        default_node = node_model.objects.filter(parent_key='', org_id=org_id).first()
        if not default_node:
            continue
        m2m_objs.extend(
            [
                m2m_model(node=default_node, asset_id=asset_id)
                for asset_id in asset_ids
            ]
        )
    if not m2m_objs:
        return

    m2m_model.objects.bulk_create(m2m_objs)


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0118_auto_20230524_1647'),
    ]

    operations = [
        migrations.RunPython(migrate_asset_add_default_node),
    ]
