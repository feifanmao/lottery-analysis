"""奇偶比、大小比分析"""


def analyze_dlt_parity(draws):
    """大乐透奇偶比和大小比
    前区: 1-17小, 18-35大
    """
    odd_even_list = []
    big_small_list = []

    for d in draws:
        front = [d[f'front_{i}'] for i in range(1, 6)]
        odd = sum(1 for n in front if n % 2 == 1)
        even = 5 - odd
        big = sum(1 for n in front if n >= 18)
        small = 5 - big
        odd_even_list.append(f'{odd}:{even}')
        big_small_list.append(f'{big}:{small}')

    total = len(draws)
    oe_dist = {}
    for ratio in odd_even_list:
        oe_dist[ratio] = oe_dist.get(ratio, 0) + 1
    oe_result = [{'ratio': k, 'count': v, 'rate': round(v / total * 100, 2)} for k, v in sorted(oe_dist.items(), key=lambda x: -x[1])]

    bs_dist = {}
    for ratio in big_small_list:
        bs_dist[ratio] = bs_dist.get(ratio, 0) + 1
    bs_result = [{'ratio': k, 'count': v, 'rate': round(v / total * 100, 2)} for k, v in sorted(bs_dist.items(), key=lambda x: -x[1])]

    return {'odd_even': oe_result, 'big_small': bs_result, 'total_draws': total}


def analyze_ssq_parity(draws):
    """双色球奇偶比和大小比
    红球: 1-16小, 17-33大
    """
    odd_even_list = []
    big_small_list = []

    for d in draws:
        red = [d[f'red_{i}'] for i in range(1, 7)]
        odd = sum(1 for n in red if n % 2 == 1)
        even = 6 - odd
        big = sum(1 for n in red if n >= 17)
        small = 6 - big
        odd_even_list.append(f'{odd}:{even}')
        big_small_list.append(f'{big}:{small}')

    total = len(draws)
    oe_dist = {}
    for ratio in odd_even_list:
        oe_dist[ratio] = oe_dist.get(ratio, 0) + 1
    oe_result = [{'ratio': k, 'count': v, 'rate': round(v / total * 100, 2)} for k, v in sorted(oe_dist.items(), key=lambda x: -x[1])]

    bs_dist = {}
    for ratio in big_small_list:
        bs_dist[ratio] = bs_dist.get(ratio, 0) + 1
    bs_result = [{'ratio': k, 'count': v, 'rate': round(v / total * 100, 2)} for k, v in sorted(bs_dist.items(), key=lambda x: -x[1])]

    return {'odd_even': oe_result, 'big_small': bs_result, 'total_draws': total}
