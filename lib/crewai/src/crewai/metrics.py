# Instrumentação mínima de métricas para CrewAI

import time
import logging
from functools import wraps

def metric_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        logging.info(f"METRIC: {func.__name__} duration={duration:.3f}s")
        return result
    return wrapper

# Exemplo de uso:
# @metric_time
# def funcao_critica(...):
#     ...
