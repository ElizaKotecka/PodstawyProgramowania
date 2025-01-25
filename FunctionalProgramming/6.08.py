input_data = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]


def min_pts(limit):
    return lambda pts: pts >= limit

def filter_results(filter_function):
    return list(filter(filter_function, input_data))


results = filter_results(min_pts(70))
print(f"Min 70 pts: {results}")

results = filter_results(min_pts(40))
print(f"Min 70 pts: {results}")

results = filter_results(min_pts(30))
print(f"Min 70 pts: {results}")
