# DailyWeeklyManagementBackend
日报周报管理系统后端-fastapi

## 框架
fastapi-framework from xiyusullos

## 启动方式
### 安装依赖
```python
pip install -r requirements.txt
```
### 启动
```python
uvicorn main:app --host 0.0.0.0 --port 5000 --env-file .env.dev
```

## 现有功能
1. 日报管理
2. 用户登录

## 数据库
mysql
redis

## 定时任务
Apscheduler

## 更多依赖见requirements.txt

## 后期
支持docker
