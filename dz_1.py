def apply_all_func(int_list, *functions):
    results = {}
    count = 0
    len_list = len(int_list)
    for j in range(len_list):
        if isinstance(j, (int, float)):
            count += 1
    if count == len_list:
        for i in functions:
            res = i(int_list)
            results[i.__name__] = res
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))