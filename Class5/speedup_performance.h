#include <stdint.h>  // 使用 int64_t 類型

int calc(int x, int a, int b) {
    return a * x + b;
}

int64_t loop_in_C(int n, int a, int b) {
    int64_t result = 0;  // 使用 int64_t 來避免溢出
    for (int i = 0; i < n; i++) {
        result += calc(i, a, b);
    }
    return result;  // 返回 int64_t 類型
}