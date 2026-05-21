import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'lottery.db')

# 大乐透数据源
DLT_API_URL = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry'
DLT_PARAMS = {
    'gameNo': '85',
    'provinceId': '0',
    'pageSize': '100',
    'isVerify': '1',
    'pageNo': '1',
}

# 双色球数据源
SSQ_API_URL = 'https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice'
SSQ_PARAMS = {
    'name': 'ssq',
    'issueCount': '100',
    'issueStart': '',
    'issueEnd': '',
    'dayStart': '',
    'dayEnd': '',
    'pageNo': '1',
    'pageSize': '100',
    'systemType': 'PC',
}

FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
FLASK_DEBUG = True
