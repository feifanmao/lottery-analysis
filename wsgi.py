"""WSGI 入口，用于生产环境部署（Render / Gunicorn / uWSGI）"""
import os
import sys
import threading

# 将项目目录加入 path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
from models.database import init_db


def crawl_in_background():
    try:
        from crawler.dlt_crawler import crawl_dlt
        from crawler.ssq_crawler import crawl_ssq
        crawl_dlt(pages=10)
        crawl_ssq(pages=10)
        print('[CRAWL] 数据更新完成')
    except Exception as e:
        print(f'[CRAWL] 爬取失败: {e}')


# Gunicorn 会 import 此模块，init 在首次请求前完成
init_db()
print('[INIT] 数据库初始化完成')

t = threading.Thread(target=crawl_in_background, daemon=True)
t.start()

if __name__ == '__main__':
    app.run()
