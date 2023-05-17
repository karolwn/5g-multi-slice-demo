import numpy as np
from scipy import stats
from typing import List, Any, Tuple


def calc_avg(data_in: List[List[float]]) -> List:
    return np.nanmean(data_in, axis=0).tolist()


def calc_intervals(data_in: Any, percent: float) -> Tuple[List[float], List[float]]:
    data_array = np.array(data_in)
    A = data_array.transpose()
    lower_lvl = []
    upper_lvl = []
    for row in A:
        result = stats.t.interval(alpha=percent,
                                  loc=calc_avg(row),
                                  df=len(row)-1,
                                  scale=stats.sem(row, nan_policy="omit"))
        lower_lvl.append(result[0] if not np.isnan(result[0]) else calc_avg(row))
        upper_lvl.append(result[1] if not np.isnan(result[1]) else calc_avg(row))
    return lower_lvl, upper_lvl


def find_max_list(data_in: List[List[float]]) -> int:
    list_len = [len(i) for i in data_in]
    return max(list_len)


def add_nans(data_in: List[List[float]]) -> List[List[float]]:
    max_len = find_max_list(data_in)
    for row in data_in:
        while len(row) < max_len:
            row.append(np.nan)
    return data_in
