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

`switch`, `if, else` 讓LED燈閃10下，每0.5秒

---
# Task
`#define BUTTON BIT3`\
`#define LED1 BIT0 綠燈`\
`#define LED2 BIT6 紅燈`
- 寫一下按鈕會閃10秒
- 如果按超過

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

---
# Homework
- [[MSP430F2xx, MSP430G2xx Family.pdf]] 解釋第32頁，Fig. 2-3

---
## Polling Answer
```C
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
                for (i = 0; i < 6; i++) {
                    P1OUT ^= LED2;
                    __delay_cycles(500000);  // 0.5 秒
                }
                P1OUT &= ~LED2;
            }
            else             // 短按：綠燈
            {
                for (i = 0; i < 6; i++) {
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