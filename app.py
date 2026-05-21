import sys
import os
import threading
from flask import Flask, render_template
import config
from models.database import init_db
from api.draw import draw_bp
from api.analysis import analysis_bp

if getattr(sys, 'frozen', False):
    template_dir = os.path.join(sys._MEIPASS, 'templates')
    static_dir = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
else:
    app = Flask(__name__)
app.register_blueprint(draw_bp)
app.register_blueprint(analysis_bp)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/trend')
def trend():
    return render_template('trend.html')


@app.route('/frequency')
def frequency():
    return render_template('frequency.html')


@app.route('/segment')
def segment():
    return render_template('segment.html')


@app.route('/advanced')
def advanced():
    return render_template('advanced.html')


def crawl_in_background():
    """后台爬取数据"""
    try:
        from crawler.dlt_crawler import crawl_dlt
        from crawler.ssq_crawler import crawl_ssq
        crawl_dlt(pages=10)
        crawl_ssq(pages=10)
    except Exception as e:
        print(f'[CRAWL] 爬取失败: {e}')


if __name__ == '__main__':
    init_db()
    print('[INIT] 数据库初始化完成')
    t = threading.Thread(target=crawl_in_background, daemon=True)
    t.start()
    print(f'[SERVER] 启动服务 http://localhost:{config.FLASK_PORT}')
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=config.FLASK_DEBUG)
