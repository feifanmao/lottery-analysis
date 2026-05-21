import requests
import config
from models.database import insert_dlt_draw, get_latest_dlt_issue


def fetch_dlt_page(page_no=1, page_size=100):
    """从体彩网获取大乐透开奖数据"""
    params = dict(config.DLT_PARAMS)
    params['pageNo'] = str(page_no)
    params['pageSize'] = str(page_size)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://www.lottery.gov.cn/',
    }
    resp = requests.get(config.DLT_API_URL, params=params, headers=headers, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data.get('value', {}).get('list', [])


def parse_dlt_item(item):
    """解析单条大乐透记录"""
    issue = item['lotteryDrawNum']
    draw_date = item['lotteryDrawTime']
    nums = item['lotteryDrawResult'].split()
    front = [int(n) for n in nums[:5]]
    back = [int(n) for n in nums[5:7]]
    return issue, draw_date, front, back


def crawl_dlt(pages=5):
    """爬取大乐透数据，支持增量更新"""
    latest_issue = get_latest_dlt_issue()
    total_new = 0
    for page in range(1, pages + 1):
        try:
            items = fetch_dlt_page(page_no=page)
        except Exception as e:
            print(f'[DLT] 第{page}页获取失败: {e}')
            break
        if not items:
            break
        stop = False
        for item in items:
            issue = item['lotteryDrawNum']
            if latest_issue and issue <= latest_issue:
                stop = True
                break
            try:
                issue, draw_date, front, back = parse_dlt_item(item)
                insert_dlt_draw(issue, draw_date, front, back)
                total_new += 1
            except Exception as e:
                print(f'[DLT] 解析期号{issue}失败: {e}')
        if stop:
            break
    print(f'[DLT] 新增 {total_new} 条记录')
    return total_new
