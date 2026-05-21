"""频率统计与冷热号分析"""


def analyze_dlt_frequency(draws):
    """分析大乐透号码频率
    draws: list of dicts with front_1..front_5, back_1..back_2
    """
    front_freq = {}
    back_freq = {}
    for d in draws:
        for i in range(1, 6):
            n = d[f'front_{i}']
            front_freq[n] = front_freq.get(n, 0) + 1
        for i in range(1, 3):
            n = d[f'back_{i}']
            back_freq[n] = back_freq.get(n, 0) + 1

    total = len(draws)
    front_result = []
    for n in range(1, 36):
        cnt = front_freq.get(n, 0)
        front_result.append({'number': n, 'count': cnt, 'rate': round(cnt / total * 100, 2) if total else 0})

    back_result = []
    for n in range(1, 13):
        cnt = back_freq.get(n, 0)
        back_result.append({'number': n, 'count': cnt, 'rate': round(cnt / total * 100, 2) if total else 0})

    front_result.sort(key=lambda x: x['count'], reverse=True)
    back_result.sort(key=lambda x: x['count'], reverse=True)

    return {
        'front': front_result,
        'back': back_result,
        'hot_front': [x['number'] for x in front_result[:10]],
        'cold_front': [x['number'] for x in front_result[-10:]],
        'hot_back': [x['number'] for x in back_result[:5]],
        'cold_back': [x['number'] for x in back_result[-5:]],
        'total_draws': total,
    }


def analyze_ssq_frequency(draws):
    """分析双色球号码频率
    draws: list of dicts with red_1..red_6, blue
    """
    red_freq = {}
    blue_freq = {}
    for d in draws:
        for i in range(1, 7):
            n = d[f'red_{i}']
            red_freq[n] = red_freq.get(n, 0) + 1
        b = d['blue']
        blue_freq[b] = blue_freq.get(b, 0) + 1

    total = len(draws)
    red_result = []
    for n in range(1, 34):
        cnt = red_freq.get(n, 0)
        red_result.append({'number': n, 'count': cnt, 'rate': round(cnt / total * 100, 2) if total else 0})

    blue_result = []
    for n in range(1, 17):
        cnt = blue_freq.get(n, 0)
        blue_result.append({'number': n, 'count': cnt, 'rate': round(cnt / total * 100, 2) if total else 0})

    red_result.sort(key=lambda x: x['count'], reverse=True)
    blue_result.sort(key=lambda x: x['count'], reverse=True)

    return {
        'red': red_result,
        'blue': blue_result,
        'hot_red': [x['number'] for x in red_result[:10]],
        'cold_red': [x['number'] for x in red_result[-10:]],
        'hot_blue': [x['number'] for x in blue_result[:5]],
        'cold_blue': [x['number'] for x in blue_result[-5:]],
        'total_draws': total,
    }
