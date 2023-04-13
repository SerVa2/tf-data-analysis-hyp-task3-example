import pandas as pd
import numpy as np
from scipy.stats import t

chat_id = 1633714108 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    alpha = 0.1
    n = len(x)
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    t_stat = t.ppf(1 - alpha, n - 1)
    left = mean - t_stat * std / np.sqrt(n)
    right = mean + t_stat * std / np.sqrt(n)
    return right <= 300
