"""生产级服务器入口（waitress）"""
from app import app
from models.database import init_db
from crawler.dlt_crawler import crawl_dlt
from crawler.ssq_crawler import crawl_ssq
import threading
import config


def crawl_in_background():
    try:
        crawl_dlt(pages=10)
        crawl_ssq(pages=10)
        print('[CRAWL] 数据更新完成')
    except Exception as e:
        print(f'[CRAWL] 爬取失败: {e}')


if __name__ == '__main__':
    init_db()
    print('[INIT] 数据库初始化完成')
    t = threading.Thread(target=crawl_in_background, daemon=True)
    t.start()
    print(f'[SERVER] 启动服务 http://localhost:{config.FLASK_PORT}')

    from waitress import serve
    serve(app, host=config.FLASK_HOST, port=config.FLASK_PORT)
