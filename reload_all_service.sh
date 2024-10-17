# 重启服务以应用最新配置
echo "重启 Celery Worker 服务..."
sudo systemctl restart celery_worker
echo "重启 Celery Beat 服务..."
sudo systemctl restart celery_beat
echo "重启 Celery Flower 服务..."
sudo systemctl restart celery_flower
echo "所有服务已重启。"
