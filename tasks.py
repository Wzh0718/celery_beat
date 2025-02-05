"""
@ProjectName: celery_service
@FileName：tasks.py
@IDE：PyCharm
@Author：Libre
@Time：2024/10/14 上午11:12
"""
import requests

from celery_beat import cel

base_url = "http://172.16.11.245"
dataAnalysis_port = "5001"
Influencer_Data_Management_System_port = "5000"


@cel.task(name='pis_dashboards_task')
def pis_dashboards_task():
    _url = f"{base_url}:{dataAnalysis_port}/pis_dashboards_task"
    return requests.get(_url).json()


@cel.task(name='shipout_inventory')
def shipout_inventory():
    _url = f"{base_url}:{dataAnalysis_port}/shipout_inventory"
    return requests.get(_url).json()


@cel.task(name='saiHu_keywords')
def saihu_keywords():
    _url = f"{base_url}:{dataAnalysis_port}/saiHu_keywords"
    return requests.get(_url).json()


@cel.task(name='x_keywords')
def x_keywords():
    _url = f"{base_url}:{dataAnalysis_port}/x_keywords"
    return requests.get(_url).json()


@cel.task(name='ga4')
def ga4():
    _url = f"{base_url}:{dataAnalysis_port}/ga4"
    return requests.get(_url).json()


@cel.task(name='test')
def test():
    _url = f"{base_url}:{dataAnalysis_port}/pis_dashboards_task"
    return requests.get(_url).json()


@cel.task(name='video')
def video():
    _url = f"{base_url}:{Influencer_Data_Management_System_port}/scheduler/video"
    return requests.get(_url).json()


@cel.task(name='celebrity')
def celebrity():
    _url = f"{base_url}:{Influencer_Data_Management_System_port}/scheduler/celebrity"
    return requests.get(_url).json()


@cel.task(name='logistics')
def logistics():
    _url = f"{base_url}:{Influencer_Data_Management_System_port}/scheduler/logistics"
    return requests.get(_url).json()


@cel.task(name='tmallOrder')
def tmallOrder():
    _url = f"{base_url}:{dataAnalysis_port}/tmallOrder"
    return requests.get(_url).json()


@cel.task(name='weatherDaily')
def celebrity():
    _url = f"{base_url}:{dataAnalysis_port}/weatherDaily"
    return requests.get(_url).json()