"""
@ProjectName: celery_service
@FileName：celery_config.py
@IDE：PyCharm
@Author：Libre
@Time：2024/10/14 上午10:08
"""
from celery.schedules import crontab

backend = "redis://default:My$trongP@ssw0rd123!@172.16.11.167:6379/0"
broker = "redis://default:My$trongP@ssw0rd123!@172.16.11.167:6379/1"
beat_schedule = {
    'pis_dashboards_task': {
        'task': 'pis_dashboards_task',
        'schedule': crontab(hour='8', minute='30'),
    },
    'shipout_inventory': {
        'task': 'shipout_inventory',
        'schedule': crontab(hour='7', minute='00'),
    },
    'saiHu_keywords': {
        'task': 'saiHu_keywords',
        'schedule': crontab(hour='7', minute='00', day_of_week='monday')
    },
    # 'x_keywords': {
    #     'task': 'x_keywords',
    #     'schedule': crontab(hour='3', minute='00', day_of_week='monday')
    # },
    'ga4': {
        'task': 'ga4',
        'schedule': crontab(hour='5', minute='00', day_of_week='monday')
    },
    # 'test': {
    #     'task': 'test',
    #     'schedule': crontab(minute='*')
    # },
    'celebrity': {
        'task': 'celebrity',
        'schedule': crontab(day_of_month='15', hour='3', minute='00'),
    },
    'video': {
        'task': 'video',
        'schedule': crontab(minute='00', hour='0')
    },
    'logistics_9:00': {
        'task': 'logistics',
        'schedule': crontab(hour='9', minute='00')
    },
    'logistics_13_30': {
        'task': 'logistics',
        'schedule': crontab(hour='13', minute='30')
    },
    # 'tmallOrder_01_30': {
    #     'task': 'tmallOrder',
    #     'schedule': crontab(hour='01', minute='30')
    # }
    # },
    'weatherDaily': {
        'task': 'weatherDaily',
        'schedule': crontab(hour='9', minute='00')
    },
    'coupang_sales_info': {
        'task': 'coupang_sales_info',
        'schedule': crontab(hour='9', minute='00')
    }
}
