"""打包为 exe 的入口文件"""
import sys
import os
import threading
import webbrowser
import time


def get_base_path():
    """获取资源根目录（兼容 PyInstaller 打包）"""
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def get_bundle_path():
    """获取打包内部资源路径"""
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


# 必须在 import app 之前设置路径
BASE_DIR = get_base_path()
BUNDLE_DIR = get_bundle_path()

# 覆写 config 中的路径
sys.path.insert(0, BUNDLE_DIR)
import config
config.BASE_DIR = BASE_DIR
config.DB_PATH = os.path.join(BASE_DIR, 'lottery.db')

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


def open_browser():
    time.sleep(3)
    webbrowser.open(f'http://localhost:{config.FLASK_PORT}')


if __name__ == '__main__':
    init_db()
    print(f'[INIT] 数据库: {config.DB_PATH}')

    t = threading.Thread(target=crawl_in_background, daemon=True)
    t.start()

    threading.Thread(target=open_browser, daemon=True).start()

    print(f'[SERVER] http://localhost:{config.FLASK_PORT}')
    from waitress import serve
    serve(app, host=config.FLASK_HOST, port=config.FLASK_PORT)
