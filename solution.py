import pandas as pd
import numpy as np
from scipy.stats import t

chat_id = 1633714108 # Ваш chat ID, не меняйте название переменной

def solution(data: np.ndarray, threshold: float = 300, alpha: float = 0.1) -> bool:
# data - массив с историческими данными
# threshold - установленный порог затрат
# alpha - уровень значимости критерия
    n = len(data) # размер выборки
    mean = np.mean(data) # выборочное среднее
    std = np.std(data, ddof=1) # выборочное стандартное отклонение

# рассчитываем t-статистику
    t_stat = (mean - threshold) / (std / np.sqrt(n))

# рассчитываем критическое значение t-статистики
    t_crit = t.ppf(1 - alpha, n - 1)

# сравниваем t-статистику с критическим значением и возвращаем ответ
    return t_stat < t_crit
