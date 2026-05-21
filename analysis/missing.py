"""遗漏值分析"""


def analyze_dlt_missing(draws):
    """分析大乐透遗漏值
    draws: 按期号降序排列的记录列表
    """
    front_missing = {n: 0 for n in range(1, 36)}
    back_missing = {n: 0 for n in range(1, 13)}
    front_max_missing = {n: 0 for n in range(1, 36)}
    back_max_missing = {n: 0 for n in range(1, 13)}
    front_appear_count = {n: 0 for n in range(1, 36)}
    back_appear_count = {n: 0 for n in range(1, 13)}

    front_streak = {n: 0 for n in range(1, 36)}
    back_streak = {n: 0 for n in range(1, 13)}

    for idx, d in enumerate(draws):
        front_set = {d[f'front_{i}'] for i in range(1, 6)}
        back_set = {d[f'back_{i}'] for i in range(1, 3)}
        for n in range(1, 36):
            if n in front_set:
                if front_streak[n] > front_max_missing[n]:
                    front_max_missing[n] = front_streak[n]
                front_streak[n] = 0
                front_appear_count[n] += 1
            else:
                front_streak[n] += 1
        for n in range(1, 13):
            if n in back_set:
                if back_streak[n] > back_max_missing[n]:
                    back_max_missing[n] = back_streak[n]
                back_streak[n] = 0
                back_appear_count[n] += 1
            else:
                back_streak[n] += 1

    total = len(draws)
    front_result = []
    for n in range(1, 36):
        cur_miss = front_streak[n]
        avg_miss = round(total / front_appear_count[n], 2) if front_appear_count[n] else 0
        front_result.append({
            'number': n,
            'current_missing': cur_miss,
            'max_missing': max(front_max_missing[n], cur_miss),
            'avg_missing': avg_miss,
            'appear_count': front_appear_count[n],
        })

    back_result = []
    for n in range(1, 13):
        cur_miss = back_streak[n]
        avg_miss = round(total / back_appear_count[n], 2) if back_appear_count[n] else 0
        back_result.append({
            'number': n,
            'current_missing': cur_miss,
            'max_missing': max(back_max_missing[n], cur_miss),
            'avg_missing': avg_miss,
            'appear_count': back_appear_count[n],
        })

    return {'front': front_result, 'back': back_result, 'total_draws': total}


def analyze_ssq_missing(draws):
    """分析双色球遗漏值"""
    red_missing = {n: 0 for n in range(1, 34)}
    blue_missing = {n: 0 for n in range(1, 17)}
    red_max_missing = {n: 0 for n in range(1, 34)}
    blue_max_missing = {n: 0 for n in range(1, 17)}
    red_appear_count = {n: 0 for n in range(1, 34)}
    blue_appear_count = {n: 0 for n in range(1, 17)}
    red_streak = {n: 0 for n in range(1, 34)}
    blue_streak = {n: 0 for n in range(1, 17)}

    for d in draws:
        red_set = {d[f'red_{i}'] for i in range(1, 7)}
        blue_val = d['blue']
        for n in range(1, 34):
            if n in red_set:
                if red_streak[n] > red_max_missing[n]:
                    red_max_missing[n] = red_streak[n]
                red_streak[n] = 0
                red_appear_count[n] += 1
            else:
                red_streak[n] += 1
        for n in range(1, 17):
            if n == blue_val:
                if blue_streak[n] > blue_max_missing[n]:
                    blue_max_missing[n] = blue_streak[n]
                blue_streak[n] = 0
                blue_appear_count[n] += 1
            else:
                blue_streak[n] += 1

    total = len(draws)
    red_result = []
    for n in range(1, 34):
        cur_miss = red_streak[n]
        avg_miss = round(total / red_appear_count[n], 2) if red_appear_count[n] else 0
        red_result.append({
            'number': n,
            'current_missing': cur_miss,
            'max_missing': max(red_max_missing[n], cur_miss),
            'avg_missing': avg_miss,
            'appear_count': red_appear_count[n],
        })

    blue_result = []
    for n in range(1, 17):
        cur_miss = blue_streak[n]
        avg_miss = round(total / blue_appear_count[n], 2) if blue_appear_count[n] else 0
        blue_result.append({
            'number': n,
            'current_missing': cur_miss,
            'max_missing': max(blue_max_missing[n], cur_miss),
            'avg_missing': avg_miss,
            'appear_count': blue_appear_count[n],
        })

    return {'red': red_result, 'blue': blue_result, 'total_draws': total}
