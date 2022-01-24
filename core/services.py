import typing as tp

import redis
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from core.configs import db as DB

engine = create_engine(DB.SQLALCHEMY_DATABASE_URL)
MySQLSession = sessionmaker(autocommit=True, autoflush=False, bind=engine)

redis_client = redis.Redis(DB.REDIS_HOST, DB.REDIS_PORT, DB.REDIS_DB, DB.REDIS_PASSWORD)

redis_job_store = {
    'redis': RedisJobStore(db=DB.REDIS_DB, host=DB.REDIS_HOST, port=DB.REDIS_PORT, password=DB.REDIS_PASSWORD)
}

redis_executors = {
    'default': ThreadPoolExecutor(10),  # 默认线程数
    'processpool': ProcessPoolExecutor(3)  # 默认进程
}


# Generator[yield_type, send_type, return_type]
def get_db() -> tp.Generator[Session, None, None]:
    db: tp.Optional[Session] = None
    try:
        db = MySQLSession()
        yield db
    finally:
        if db is not None:
            db.close()
