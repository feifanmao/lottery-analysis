"""AC值分析
AC值 = 不同差值的个数 - (号码个数 - 1)
AC值越大，号码越分散
"""


def _calc_ac(nums):
    """计算一组号码的AC值"""
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    diffs = set()
    for i in range(n):
        for j in range(i + 1, n):
            diffs.add(sorted_nums[j] - sorted_nums[i])
    return len(diffs) - (n - 1)


def analyze_dlt_ac(draws):
    """大乐透AC值分析"""
    ac_values = []
    for d in draws:
        front = [d[f'front_{i}'] for i in range(1, 6)]
        ac_values.append(_calc_ac(front))

    total = len(ac_values)
    if not total:
        return {'ac_values': [], 'distribution': [], 'avg': 0, 'total_draws': 0}

    avg_ac = round(sum(ac_values) / total, 2)
    dist = {}
    for v in ac_values:
        dist[v] = dist.get(v, 0) + 1

    return {
        'ac_values': ac_values[:50],
        'distribution': [{'ac': k, 'count': v, 'rate': round(v / total * 100, 2)} for k, v in sorted(dist.items())],
        'avg': avg_ac,
        'min': min(ac_values),
        'max': max(ac_values),
        'total_draws': total,
    }


def analyze_ssq_ac(draws):
    """双色球AC值分析"""
    ac_values = []
    for d in draws:
        red = [d[f'red_{i}'] for i in range(1, 7)]
        ac_values.append(_calc_ac(red))

    total = len(ac_values)
    if not total:
        return {'ac_values': [], 'distribution': [], 'avg': 0, 'total_draws': 0}

    avg_ac = round(sum(ac_values) / total, 2)
    dist = {}
    for v in ac_values:
        dist[v] = dist.get(v, 0) + 1

    return {
        'ac_values': ac_values[:50],
        'distribution': [{'ac': k, 'count': v, 'rate': round(v / total * 100, 2)} for k, v in sorted(dist.items())],
        'avg': avg_ac,
        'min': min(ac_values),
        'max': max(ac_values),
        'total_draws': total,
    }
