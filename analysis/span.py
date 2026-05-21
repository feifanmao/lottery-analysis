"""跨度分析
跨度 = 最大号码 - 最小号码
"""


def analyze_dlt_span(draws):
    """大乐透跨度分析"""
    front_spans = []
    back_spans = []
    for d in draws:
        front = [d[f'front_{i}'] for i in range(1, 6)]
        back = [d[f'back_{i}'] for i in range(1, 3)]
        front_spans.append(max(front) - min(front))
        back_spans.append(max(back) - min(back))

    total = len(front_spans)
    if not total:
        return {'front': {}, 'back': {}, 'total_draws': 0}

    front_dist = {}
    for s in front_spans:
        front_dist[s] = front_dist.get(s, 0) + 1

    back_dist = {}
    for s in back_spans:
        back_dist[s] = back_dist.get(s, 0) + 1

    return {
        'front': {
            'values': front_spans[:50],
            'avg': round(sum(front_spans) / total, 2),
            'min': min(front_spans),
            'max': max(front_spans),
            'distribution': [{'span': k, 'count': v, 'rate': round(v / total * 100, 2)} for k, v in sorted(front_dist.items())],
        },
        'back': {
            'values': back_spans[:50],
            'avg': round(sum(back_spans) / total, 2),
            'min': min(back_spans),
            'max': max(back_spans),
            'distribution': [{'span': k, 'count': v, 'rate': round(v / total * 100, 2)} for k, v in sorted(back_dist.items())],
        },
        'total_draws': total,
    }


def analyze_ssq_span(draws):
    """双色球跨度分析"""
    red_spans = []
    for d in draws:
        red = [d[f'red_{i}'] for i in range(1, 7)]
        red_spans.append(max(red) - min(red))

    total = len(red_spans)
    if not total:
        return {'red': {}, 'total_draws': 0}

    red_dist = {}
    for s in red_spans:
        red_dist[s] = red_dist.get(s, 0) + 1

    return {
        'red': {
            'values': red_spans[:50],
            'avg': round(sum(red_spans) / total, 2),
            'min': min(red_spans),
            'max': max(red_spans),
            'distribution': [{'span': k, 'count': v, 'rate': round(v / total * 100, 2)} for k, v in sorted(red_dist.items())],
        },
        'total_draws': total,
    }
