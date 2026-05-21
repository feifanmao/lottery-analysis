"""和值分析"""


def analyze_dlt_sum(draws):
    """大乐透和值分析"""
    front_sums = []
    back_sums = []
    for d in draws:
        front = [d[f'front_{i}'] for i in range(1, 6)]
        back = [d[f'back_{i}'] for i in range(1, 3)]
        front_sums.append(sum(front))
        back_sums.append(sum(back))

    total = len(draws)
    if not total:
        return {'front_sum': {}, 'back_sum': {}, 'total_draws': 0}

    front_min, front_max = min(front_sums), max(front_sums)
    back_min, back_max = min(back_sums), max(back_sums)
    front_avg = round(sum(front_sums) / total, 2)
    back_avg = round(sum(back_sums) / total, 2)

    # 和值区间分布
    front_dist = {}
    for s in front_sums:
        bucket = (s // 20) * 20
        key = f'{bucket}-{bucket + 19}'
        front_dist[key] = front_dist.get(key, 0) + 1

    back_dist = {}
    for s in back_sums:
        bucket = (s // 5) * 5
        key = f'{bucket}-{bucket + 4}'
        back_dist[key] = back_dist.get(key, 0) + 1

    return {
        'front_sum': {
            'values': front_sums[:50],
            'min': front_min, 'max': front_max, 'avg': front_avg,
            'distribution': front_dist,
        },
        'back_sum': {
            'values': back_sums[:50],
            'min': back_min, 'max': back_max, 'avg': back_avg,
            'distribution': back_dist,
        },
        'total_draws': total,
    }


def analyze_ssq_sum(draws):
    """双色球和值分析"""
    red_sums = []
    for d in draws:
        red = [d[f'red_{i}'] for i in range(1, 7)]
        red_sums.append(sum(red))

    total = len(draws)
    if not total:
        return {'red_sum': {}, 'total_draws': 0}

    red_min, red_max = min(red_sums), max(red_sums)
    red_avg = round(sum(red_sums) / total, 2)

    red_dist = {}
    for s in red_sums:
        bucket = (s // 20) * 20
        key = f'{bucket}-{bucket + 19}'
        red_dist[key] = red_dist.get(key, 0) + 1

    return {
        'red_sum': {
            'values': red_sums[:50],
            'min': red_min, 'max': red_max, 'avg': red_avg,
            'distribution': red_dist,
        },
        'total_draws': total,
    }
