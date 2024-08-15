用於變數宣告__interrupted
```C++
#include <msp430.h>

// 假设已经在其他地方配置了定时器

// Timer0_A0中断服务例程
#pragma vector=TIMER0_A0_VECTOR
__interrupt void Timer_A (void) {
   // 这里是中断服务程序的代码
   P1OUT ^= 0x01; // 切换P1.0引脚的状态，如果LED连接到这个引脚，它会闪烁

   // 可以在这里添加其他处理代码
   // ...

   // 通常无需手动重置中断标志，因为MSP430硬件在退出中断服务程序时会自动处理
}

```
