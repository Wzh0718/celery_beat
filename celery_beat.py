"""
@ProjectName: python
@FileName：celery_task.py
@IDE：PyCharm
@Author：Libre
@Time：2024/7/11 下午2:22
"""
import celery

from celery_config import broker, backend, beat_schedule

cel = celery.Celery('work_beat', broker=broker, backend=backend, include=["tasks"])
# 其他 Celery 配置
cel.conf.update(
    broker_connection_retry_on_startup=True,
    timezone='Asia/Shanghai',
    enable_utc=False,
    worker_log_color=True,
    worker_task_log_format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s",
    worker_log_format="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s",
    worker_task_log_datefmt="%Y-%m-%d %H:%M:%S",
    worker_log_datefmt="%Y-%m-%d %H:%M:%S",
    # 定时任务
    beat_schedule=beat_schedule
)
