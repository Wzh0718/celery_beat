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
    'x_keywords': {
        'task': 'x_keywords',
        'schedule': crontab(hour='3', minute='00', day_of_week='monday')
    },
    'ga4': {
        'task': 'ga4',
        'schedule': crontab(hour='5', minute='00', day_of_week='monday')
    },
    'test': {
        'task': 'test',
        'schedule': crontab(minute='*')
    },
    'celebrity': {
        'task': 'video',
        'schedule': crontab(day_of_month='15', hour='3', minute='00'),
    },
    'video': {
        'task': 'video',
        'schedule': crontab(day_of_week='0,1,3,5', hour='0', minute='30')
    }
}
