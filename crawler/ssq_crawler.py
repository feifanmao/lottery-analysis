import requests
import config
from models.database import insert_ssq_draw, get_latest_ssq_issue


def fetch_ssq_page(page_no=1, page_size=100):
    """从中彩网获取双色球开奖数据"""
    params = dict(config.SSQ_PARAMS)
    params['pageNo'] = str(page_no)
    params['pageSize'] = str(page_size)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://www.cwl.gov.cn/ygkj/wqkjgg/ssq/',
    }
    resp = requests.get(config.SSQ_API_URL, params=params, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data.get('result', [])


def parse_ssq_item(item):
    """解析单条双色球记录"""
    issue = item['code']
    draw_date = item['date']
    red = [int(n) for n in item['red'].split(',')]
    blue = int(item['blue'])
    return issue, draw_date, red, blue


def crawl_ssq(pages=5):
    """爬取双色球数据，支持增量更新"""
    latest_issue = get_latest_ssq_issue()
    total_new = 0
    for page in range(1, pages + 1):
        try:
            items = fetch_ssq_page(page_no=page)
        except Exception as e:
            print(f'[SSQ] 第{page}页获取失败: {e}')
            break
        if not items:
            break
        stop = False
        for item in items:
            issue = item['code']
            if latest_issue and issue <= latest_issue:
                stop = True
                break
            try:
                issue, draw_date, red, blue = parse_ssq_item(item)
                insert_ssq_draw(issue, draw_date, red, blue)
                total_new += 1
            except Exception as e:
                print(f'[SSQ] 解析期号{issue}失败: {e}')
        if stop:
            break
    print(f'[SSQ] 新增 {total_new} 条记录')
    return total_new
