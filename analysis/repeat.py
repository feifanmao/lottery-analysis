"""重复号分析"""


def analyze_dlt_repeat(draws):
    """大乐透重复号分析：与上一期重复的号码"""
    repeat_counts = []
    repeat_num_freq = {}

    for i in range(len(draws) - 1):
        cur = {draws[i][f'front_{j}'] for j in range(1, 6)}
        prev = {draws[i + 1][f'front_{j}'] for j in range(1, 6)}
        common = cur & prev
        repeat_counts.append(len(common))
        for n in common:
            repeat_num_freq[n] = repeat_num_freq.get(n, 0) + 1

    total = len(repeat_counts)
    dist = {}
    for c in repeat_counts:
        dist[c] = dist.get(c, 0) + 1

    avg_repeat = round(sum(repeat_counts) / total, 2) if total else 0
    top_nums = sorted(repeat_num_freq.items(), key=lambda x: -x[1])[:10]

    return {
        'avg_repeat': avg_repeat,
        'distribution': [{'count': k, 'times': v} for k, v in sorted(dist.items())],
        'top_repeat_nums': [{'number': n, 'count': c} for n, c in top_nums],
        'total_draws': total,
    }


def analyze_ssq_repeat(draws):
    """双色球重复号分析"""
    repeat_counts = []
    repeat_num_freq = {}

    for i in range(len(draws) - 1):
        cur = {draws[i][f'red_{j}'] for j in range(1, 7)}
        prev = {draws[i + 1][f'red_{j}'] for j in range(1, 7)}
        common = cur & prev
        repeat_counts.append(len(common))
        for n in common:
            repeat_num_freq[n] = repeat_num_freq.get(n, 0) + 1

    total = len(repeat_counts)
    dist = {}
    for c in repeat_counts:
        dist[c] = dist.get(c, 0) + 1

    avg_repeat = round(sum(repeat_counts) / total, 2) if total else 0
    top_nums = sorted(repeat_num_freq.items(), key=lambda x: -x[1])[:10]

    return {
        'avg_repeat': avg_repeat,
        'distribution': [{'count': k, 'times': v} for k, v in sorted(dist.items())],
        'top_repeat_nums': [{'number': n, 'count': c} for n, c in top_nums],
        'total_draws': total,
    }
