"""号段分布分析"""


def _segment_dist(nums_list, ranges):
    """通用号段分布统计"""
    dist = {f'{s}-{e}': 0 for s, e in ranges}
    for n in nums_list:
        for s, e in ranges:
            if s <= n <= e:
                dist[f'{s}-{e}'] += 1
                break
    return dist


def analyze_dlt_segment(draws):
    """大乐透号段分布（前区分5段，后区分3段）"""
    front_ranges = [(1, 7), (8, 14), (15, 21), (22, 28), (29, 35)]
    back_ranges = [(1, 4), (5, 8), (9, 12)]

    front_segments = {f'{s}-{e}': [] for s, e in front_ranges}
    back_segments = {f'{s}-{e}': [] for s, e in back_ranges}

    for d in draws:
        front_nums = [d[f'front_{i}'] for i in range(1, 6)]
        back_nums = [d[f'back_{i}'] for i in range(1, 3)]
        fd = _segment_dist(front_nums, front_ranges)
        bd = _segment_dist(back_nums, back_ranges)
        for k, v in fd.items():
            front_segments[k].append(v)
        for k, v in bd.items():
            back_segments[k].append(v)

    total = len(draws)
    front_summary = []
    for label, counts in front_segments.items():
        avg = round(sum(counts) / total, 2) if total else 0
        front_summary.append({'segment': label, 'total': sum(counts), 'avg_per_draw': avg})

    back_summary = []
    for label, counts in back_segments.items():
        avg = round(sum(counts) / total, 2) if total else 0
        back_summary.append({'segment': label, 'total': sum(counts), 'avg_per_draw': avg})

    return {'front': front_summary, 'back': back_summary, 'total_draws': total}


def analyze_ssq_segment(draws):
    """双色球号段分布（红球分5段，蓝球分4段）"""
    red_ranges = [(1, 7), (8, 14), (15, 21), (22, 28), (29, 33)]
    blue_ranges = [(1, 4), (5, 8), (9, 12), (13, 16)]

    red_segments = {f'{s}-{e}': [] for s, e in red_ranges}
    blue_segments = {f'{s}-{e}': [] for s, e in blue_ranges}

    for d in draws:
        red_nums = [d[f'red_{i}'] for i in range(1, 7)]
        blue_num = d['blue']
        rd = _segment_dist(red_nums, red_ranges)
        for k, v in rd.items():
            red_segments[k].append(v)
        for s, e in blue_ranges:
            key = f'{s}-{e}'
            blue_segments[key].append(1 if s <= blue_num <= e else 0)

    total = len(draws)
    red_summary = []
    for label, counts in red_segments.items():
        avg = round(sum(counts) / total, 2) if total else 0
        red_summary.append({'segment': label, 'total': sum(counts), 'avg_per_draw': avg})

    blue_summary = []
    for label, counts in blue_segments.items():
        avg = round(sum(counts) / total, 2) if total else 0
        blue_summary.append({'segment': label, 'total': sum(counts), 'avg_per_draw': avg})

    return {'red': red_summary, 'blue': blue_summary, 'total_draws': total}
