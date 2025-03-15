%module speedup_performance

%{
#include "speedup_performance.h"
#include <stdint.h>
%}

%include "stdint.i"

/* List declarations */
extern int calc(int x, int a, int b);
extern int64_t loop_in_C(int n, int a, int b);  // Modified declaration