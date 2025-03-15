import sys
import os

# 確保當前目錄在 sys.path 中
sys.path.append(os.getcwd())

import speedup_performance
print(f"speedup_performance module loaded: {speedup_performance}")
print(speedup_performance.calc(3, a=2, b=4))
result_value = speedup_performance.loop_in_C(100000000, 2, 3)
print(result_value)
