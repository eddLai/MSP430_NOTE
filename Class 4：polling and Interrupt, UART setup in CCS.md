---
bg: "[[NTKLab_white bg.png]]"
---
<style>
    .reveal {
        font-family: 'Times New Roman', '標楷體';
        font-size: 30px;
        text-align: left;
        color: black;
        background-size: cover;
        background-position: center;
    }
	.reveal h1,
	.reveal h2,
	.reveal h3,
	.reveal h4,
	.reveal h5,
	.reveal h6 {
	  font-family: 'Times New Roman', '標楷體';
	  color: black;
	  %%text-transform: lowercase%%;
	  text-transform: capitalize;
	}
	.with-border{
		border: 1px solid red;
	}
</style>
<grid drag="100 10" drop="0 40">
polling and Interrupt, UART setup in CCS
<!-- element style="background-color: black; font-size: 60px;align: left; text-align: middle;color: white"-->
</grid>

<grid drag="50 10" drop="40 70">
TA: 賴宏達\
eddlai.be10@nycu.edu.tw
<!-- element style="background-color: black;font-size: 40px;align: right; text-align: right;color: white"-->
</grid>

<!-- slide bg="[[MSP430 HD pic.png]]" -->

---
# Idea
- polling（輪詢）
- Interrupt

舉例：多個if的問題，(阻塞)

`switch`, `if, else` \
哪個更加接近於人? Event-driven programming

---
![[polling example1.png]]![[interrupt example1.png]]
[PIC Interrupts vs. Polling - Interrupt Theory | PyroElectro - News, Projects & Tutorials](http://www.pyroelectro.com/tutorials/pic_interrupts_vs_polling/theory.html)

---
Interrupt觸發條件：
- Change value of internal variable (count)
- Read a data value (sensor, receive)
- Write a data value (actuator, send)

maskable還需要等待GIE（General Interrupt Enable）通過

---
向量表的入口是固定在處理的向量表\
(最後之類的，視處理器而定)，\
但是後續的==ISR(Interrupt Service Routine)==則是可以在flash記憶體中的任何位置\
![[ISR location.png]]

---
# Task
`#define BUTTON BIT3`\
`#define LED1 BIT0 綠燈`\
`#define LED2 BIT6 紅燈`
- 寫一下按鈕會閃3秒綠燈
- 如果按超過1秒會開始閃爍紅燈

---
# Polling Code Example
```C++
#include <msp430.h>

#define BUTTON BIT3     // P1.3 = S2 按鈕
#define LED1   BIT0     // 綠燈（P1.0）
#define LED2   BIT6     // 紅燈（P1.6）
int i;

void main(void)
{
    WDTCTL = WDTPW | WDTHOLD;       // 停用 watchdog timer

    // 設定 LED 為輸出
    P1DIR |= LED1 | LED2;
    P1OUT &= ~(LED1 | LED2);        // 初始熄滅

    // 設定按鈕為輸入，並啟用上拉電阻
    P1DIR &= ~BUTTON;
    P1REN |= BUTTON;
    P1OUT |= BUTTON;

    while (1)
    {
        if ((P1IN & BUTTON) == 0)   // 偵測按鈕按下
        {
            unsigned int held = 0;

            // 按鈕持續按下時持續累加時間（每次約 100ms）
            while ((P1IN & BUTTON) == 0)
            {
                __delay_cycles(100000);  // 100ms 延遲（假設 8MHz）
                held++;

                // 若按超過 20 次 * 100ms = 2 秒，就不再累加
                if (held >= 20)
                    break;
            }

            // 判斷短按或長按
            if (held >= 20)  // 長按：紅燈
            {
                for (i = 0; i < 10; i++) {
                    P1OUT ^= LED2;
                    __delay_cycles(500000);  // 0.5 秒
                }
                P1OUT &= ~LED2;
            }
            else             // 短按：綠燈
            {
                for (i = 0; i < 10; i++) {
                    P1OUT ^= LED1;
                    __delay_cycles(500000);
                }
                P1OUT &= ~LED1;
            }

            // 等待放開再繼續
            while ((P1IN & BUTTON) == 0);
            __delay_cycles(50000); // debounce
        }
    }
}

```

---
# Interrupt Code hint
```C++
#include <msp430.h>

#define BUTTON    BIT3      // P1.3 = 按鈕
#define LED_GREEN BIT0     // P1.0 = 綠燈
#define LED_RED   BIT6     // P1.6 = 紅燈

volatile unsigned int tick_green = 0;  // 記錄綠燈閃爍時間
volatile unsigned int tick_red = 0;    // 記錄紅燈閃爍時間
volatile unsigned char pressed = 0;    // 按鈕是否被按下

int i;

void flash_led(unsigned char led)
{
    for (i = 0; i < 10; i++) {       // 6 次閃爍，每次 0.5 秒
        P1OUT ^= led;                // 切換 LED 狀態
        __delay_cycles(500000);      // 延遲 0.5 秒
    }
    P1OUT &= ~led;                   // 確保燈熄掉
}

void main(void)
{
    WDTCTL = WDTPW | WDTHOLD;      // 停用 watchdog timer
    BCSCTL1 = CALBC1_1MHZ;         // DCO 1MHz
    DCOCTL = CALDCO_1MHZ;

    P1DIR |= LED_GREEN | LED_RED;  // 設定 LED 為輸出
    P1OUT &= ~(LED_GREEN | LED_RED);  // 初始熄燈

    P1DIR &= ~BUTTON;               // 設定按鈕為輸入
    P1REN |= BUTTON;                // 啟用內建拉電阻
    P1OUT |= BUTTON;                // 啟用上拉（按鈕未按下時為高電位）
    P1IE  |= BUTTON;                // 啟用 P1.3 中斷
    P1IES |= BUTTON;                // 設定中斷為 falling edge（按鈕按下）

    P1IFG &= ~BUTTON;               // 清除中斷旗標

    __enable_interrupt();           // 啟用全域中斷
    __bis_SR_register(LPM0_bits + GIE); // 進入低功耗模式，等待中斷
}

// 按鈕中斷處理（falling edge）
#pragma vector=PORT1_VECTOR
__interrupt void PORT1_ISR(void)
{
    P1IFG &= ~BUTTON;  // 清除中斷旗標

    if ((P1IN & BUTTON) == 0 && !pressed)  // 按鈕被按下
    {
        pressed = 1;
        tick_green = 0;  // 重置綠燈計時器
        tick_red = 0;    // 重置紅燈計時器

        WDTCTL = WDT_MDLY_32;  // 設定 watchdog timer 每 32 毫秒觸發一次中斷
        IFG1 &= ~WDTIFG;       // 清除 WDT 中斷旗標
        IE1 |= WDTIE;          // 啟用 WDT 中斷
    }
}

// Watchdog timer 中斷，每 32ms 觸發一次
#pragma vector=WDT_VECTOR
__interrupt void WDT_ISR(void)
{
    if (!pressed) return;  // 若按鈕未被按下則不處理

    tick_green++;  // 增加綠燈計時器
    tick_red++;    // 增加紅燈計時器

    if (tick_green == 12)  // 約 0.4 秒
    {
        flash_led(LED_GREEN);    // 閃綠燈
    }
    else if (tick_red == 24)  // 約 0.8 秒
    {
        flash_led(LED_RED);      // 閃紅燈
    }
    else if (tick_green == 24)  // 約 0.8 秒
    {
        flash_led(LED_GREEN);    // 再閃一次綠燈
    }
    else if (tick_red == 31)  // 約 1 秒
    {
        flash_led(LED_RED);      // 再閃一次紅燈
    }

    // 完成後重置狀態
    if (tick_red >= 31 && tick_green >= 24)  // 1 秒後，重置狀態
    {
        pressed = 0;    // 重置按鈕狀態
        tick_green = 0; // 重置綠燈計時器
        tick_red = 0;   // 重置紅燈計時器
        IE1 &= ~WDTIE;  // 停用 WDT 中斷
        WDTCTL = WDTPW | WDTHOLD;  // 停用 Watchdog Timer
    }
}
```

---
# Homework
- [[MSP430F2xx, MSP430G2xx Family.pdf]] 解釋第32頁，Fig. 2-3
- 用Interrupt的想法，解說任務二中的程式碼做註解

---
```
// Configure UART
UCA0CTLW0|= UCSWRST;
UCA0CTLW0|= UCSSEL__SMCLK;

// Baud Rate calculation
// 8000000/(16*9600) = 52.083
// Fractional portion = 0.083
// User's Guide Table 14-4: UCBRSx = 0x49
// UCBRFx = int ( (52.083-52)*16) = 1
UCA0BR0 = 52;                             // 8000000/16/9600
UCA0BR1 = 0x00;
UCA0MCTLW = 0x4900 | UCOS16 | UCBRF_1;

UCA0CTLW0 &= ~UCSWRST;                    // Initialize eUSCI
UCA0IE|= UCRXIE;                         // Enable USCI_A0 RX interrupt

  switch(__even_in_range(UCA0IV,USCI_UART_UCTXCPTIFG))
  {
case USCI_NONE: break;
case USCI_UART_UCRXIFG:
  while(!(UCA0IFG&UCTXIFG));
  UCA0TXBUF = UCA0RXBUF;
  __no_operation();
  break;
case USCI_UART_UCTXIFG: break;
case USCI_UART_UCSTTIFG: break;
case USCI_UART_UCTXCPTIFG: break;
default: break;
  }
```

---
# Flow
燒錄就好
1. 軟體重置可配置狀態`UCA0CTLW0 |= UCSWRST;`
2. 關閉UCSWRST，啟動 UART `UCA0CTL1 &= ~UCSWRST;`
3. `IE2 |= UCA0RXIE;`
4. `__bis_SR_register(LPM0_bits + GIE);`
進入 低功耗模式 LPM0，並開啟全域中斷允許

---
# Register Table
[msp430g2xx3_uscia0_uart_01_9600.c](https://dev.ti.com/tirex/explore/nod\e?node=A__AL4DP41WSJ9ZDY-aLKgPKg__msp430ware__IOGqZri__LATEST)\
[UART 简介实验室 — MSP430 Academy 教程](https://dev.ti.com/tirex4-desktop/content/msp430_academy_%E6%95%99%E7%A8%8B_2_01_00_00/_build_msp430_academy_%E6%95%99%E7%A8%8B_2_01_00_00/source/msp430/msp430_uart_training/msp430_uart_chinese.html)\
[MSP430 USCI/EUSCI UART Baudrate Calculator](https://software-dl.ti.com/msp430/msp430_public_sw/mcu/msp430/MSP430BaudRateConverter/index.html)
[[MSP430F2xx, MSP430G2xx Family.pdf]]


---
# button module
[Arduino 4x4薄膜鍵盤模組實驗（一）：按鍵掃描程式原理說明 - 超圖解系列圖書](https://swf.com.tw/?p=917)\
引入一個我手寫的`.h`檔案\
寫一個計算機

---
[MSP430 Serial Monitor](https://www.youtube.com/watch?v=Fzf8q6fgxfQ)\
[[MSP430G2553 LaunchPad™ Development Kit.pdf]]


[courses.cs.washington.edu/courses/cse466/11au/calendar/04-Interrupts-posted.pdf](https://courses.cs.washington.edu/courses/cse466/11au/calendar/04-Interrupts-posted.pdf)