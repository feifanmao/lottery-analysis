"""连号分析"""


def _find_consecutive(nums):
    """在排序后的号码中找连号组"""
    sorted_nums = sorted(nums)
    groups = []
    current = [sorted_nums[0]]
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] == sorted_nums[i - 1] + 1:
            current.append(sorted_nums[i])
        else:
            if len(current) >= 2:
                groups.append(current)
            current = [sorted_nums[i]]
    if len(current) >= 2:
        groups.append(current)
    return groups


def analyze_dlt_consecutive(draws):
    """大乐透连号分析"""
    has_consecutive = 0
    consecutive_count = {0: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    pair_freq = {}

    for d in draws:
        front = [d[f'front_{i}'] for i in range(1, 6)]
        groups = _find_consecutive(front)
        if groups:
            has_consecutive += 1
        consecutive_count[len(groups)] = consecutive_count.get(len(groups), 0) + 1
        for g in groups:
            for i in range(len(g) - 1):
                pair = f'{g[i]}-{g[i + 1]}'
                pair_freq[pair] = pair_freq.get(pair, 0) + 1

    total = len(draws)
    pair_list = sorted(pair_freq.items(), key=lambda x: -x[1])[:20]

    return {
        'consecutive_rate': round(has_consecutive / total * 100, 2) if total else 0,
        'group_count_dist': [{'groups': k, 'count': v} for k, v in sorted(consecutive_count.items())],
        'top_pairs': [{'pair': p, 'count': c} for p, c in pair_list],
        'total_draws': total,
    }


def analyze_ssq_consecutive(draws):
    """双色球连号分析"""
    has_consecutive = 0
    consecutive_count = {}
    pair_freq = {}

    for d in draws:
        red = [d[f'red_{i}'] for i in range(1, 7)]
        groups = _find_consecutive(red)
        if groups:
            has_consecutive += 1
        key = len(groups)
        consecutive_count[key] = consecutive_count.get(key, 0) + 1
        for g in groups:
            for i in range(len(g) - 1):
                pair = f'{g[i]}-{g[i + 1]}'
                pair_freq[pair] = pair_freq.get(pair, 0) + 1

    total = len(draws)
    pair_list = sorted(pair_freq.items(), key=lambda x: -x[1])[:20]

    return {
        'consecutive_rate': round(has_consecutive / total * 100, 2) if total else 0,
        'group_count_dist': [{'groups': k, 'count': v} for k, v in sorted(consecutive_count.items())],
        'top_pairs': [{'pair': p, 'count': c} for p, c in pair_list],
        'total_draws': total,
    }
