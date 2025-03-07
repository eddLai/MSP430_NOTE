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
Class3：7 segment display pin wiring practice, difference of coding in Energia and CCS
<!-- element style="background-color: black; font-size: 60px;align: left; text-align: middle;color: white"-->
</grid>

<grid drag="50 10" drop="40 70">
TA: 賴宏達\
eddlai.be10@nycu.edu.tw
<!-- element style="background-color: black;font-size: 40px;align: right; text-align: right;color: white"-->
</grid>

<!-- slide bg="[[MSP430 HD pic.png]]" -->

---
# pinout Table
接5V線確定腳位位置\
填入連接的pin腳

|     | dis |     |               |     | MSP |     |
| --- | --- | --- | ------------- | --- | --- | --- |
| --- | A   | --- |               | --- |     | --- |
| F   |     | B   |               |     |     |     |
| --- | G   | --- | $\rightarrow$ | --- |     | --- |
| E   |     | C   |               |     |     |     |
| --- | D   | --- |               | --- |     | --- |

---
填入A+B等

| number | count |     |
| ------ | ----- | --- |
| 0      |       |     |
| 1      |       |     |
| 2      |       |     |
| 3      |       |     |
| 4      |       |     |
| 5      |       |     |
| 6      |       |     |
| 7      |       |     |
| 8      |       |     |
| 9      |       |     |

---

填入1代表ON, 0代表OFF

| number | P1_1 | P1_2 | P1_3 | P1_4 | P1_5 | P1_6 | P1_7 |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0      |      |      |      |      |      |      |      |
| 1      |      |      |      |      |      |      |      |
| 2      |      |      |      |      |      |      |      |
| 3      |      |      |      |      |      |      |      |
| 4      |      |      |      |      |      |      |      |
| 5      |      |      |      |      |      |      |      |
| 6      |      |      |      |      |      |      |      |
| 7      |      |      |      |      |      |      |      |
| 8      |      |      |      |      |      |      |      |
| 9      |      |      |      |      |      |      |      |

---
![[7 segments display pinout.png]]
共陰極是為了減少電流消耗(每個腳位是有電流上限的)

---
# Code Hint
## Energia
```C++
byte num[10][7] = ??
byte pinMapping[7] = {P1_1, P1_2, P1_3, P1_4, P1_5, P1_6, P1_7};
digitalWrite(pinMapping[i], HIGH);
digitalWrite(pinMapping[i], LOW);
```

---
## CCS
[MSP430F2xx, MSP430G2xx Family](https://www.ti.com/lit/ug/slau144k/slau144k.pdf?ts=1741352433148#page=49.09)
```C++
#include <msp430.h>

#define a BIT1
#define b BIT2
#define c BIT3
#define d BIT4
#define e BIT5
#define f BIT6
#define g BIT7
 
void main()
{
    WDTCTL = WDTPW + WDTHOLD;
    P1DIR = a+b+c+d+e+f+g;
 
    while(1)
    {
        P1OUT = b+c;
        __delay_cycles(500000);
        P1OUT = a+b+g+e+d;
        __delay_cycles(500000);
        P1OUT = a+b+g+c+d;
        __delay_cycles(500000);
    }
}
```

---
## Register
![[PxIN Register.png]]

---
![[PxOUT Register.png]]

---
![[PxDIR Register.png]]

---
# Task
注意沒有加電阻會導致顯示器被破壞，==一人只有一個==
1. 用Energia: 完成0~9的計時，並用碼表檢查其準確性
2. 用CCS:完成一樣的任務%%加分題：按下按鈕倒數計時%%

---
```
byte pin;
byte num[10][7] = {
  {1, 1, 1, 1, 1, 1, 0}, // 0
  {0, 1, 1, 0, 0, 0, 0}, // 1
  {1, 1, 0, 1, 1, 0, 1}, // 2
  {1, 1, 1, 1, 0, 0, 1}, // 3
  {0, 1, 1, 0, 0, 1, 1}, // 4 
  {1, 0, 1, 1, 0, 1, 1}, // 5
  {0, 0, 1, 1, 1, 1, 1}, // 6
  {1, 1, 1, 0, 0, 0, 0}, // 7
  {1, 1, 1, 1, 1, 1, 1}, // 8
  {1, 1, 1, 0, 0, 1, 1}  // 9
};

// MSP430 P1.x 腳位對應
byte pinMapping[7] = {P1_1, P1_2, P1_3, P1_4, P1_5, P1_6, P1_7};

void setup() {
  for (int i = 0; i < 7; i++) {         
    pinMode(pinMapping[i], OUTPUT);  // 設定 P1_x 為輸出
    digitalWrite(pinMapping[i], HIGH); // 測試 LED
    delay(200);
    digitalWrite(pinMapping[i], LOW);
    delay(200);
  }
  digitalWrite(pinMapping[0], HIGH);
}

void loop() {
  for (int i = 0; i < 10; i++) {  // 顯示 0~9
    for (int j = 0; j < 7; j++) {
      digitalWrite(pinMapping[j], num[i][j]); // 更新顯示
    }
    delay(1000);  // 1秒更新數字
  }
}
```

---
```
#include <msp430.h>

#define a BIT1
#define b BIT2
#define c BIT3
#define d BIT4
#define e BIT5
#define f BIT6
#define g BIT7
 
void main()
{
    WDTCTL = WDTPW + WDTHOLD;
    P1DIR = a+b+c+d+e+f+g;
 
    while(1)
    {
        P1OUT = b+c;
        __delay_cycles(500000);
        P1OUT = a+b+g+e+d;
        __delay_cycles(500000);
        P1OUT = a+b+g+c+d;
        __delay_cycles(500000);
    }
}
```

---
# Answer

|     | dis |     |               |      | MSP  |      |
| --- | --- | --- | ------------- | ---- | ---- | ---- |
| --- | A   | --- |               | ---  | P1_1 | ---  |
| F   |     | B   |               | P1_6 |      | P1_2 |
| --- | G   | --- | $\rightarrow$ | ---  | P1_7 | ---  |
| E   |     | C   |               | P1_5 |      | P1_3 |
| --- | D   | --- |               | ---  | P1_4 | ---  

| number | count       |     |
| ------ | ----------- | --- |
| 0      | A+B+C+D+E+F |     |
| 1      | B+C         |     |
| 2      | A+B+G+E+D   |     |
| 3      | A+B+C+D+G   |     |
| 4      | B+C+F+G     |     |
| 5      | A+F+G+C+D   |     |
| 6      | F+G+C+D+E   |     |
| 7      | A+B+C       |     |
| 8      | A+B+C+D+E+F |     |
| 9      | A+B+C+G+F   |     |

---

| number | P1_1 | P1_2 | P1_3 | P1_4 | P1_5 | P1_6 | P1_7 |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0      | 1    | 1    | 1    | 1    | 1    | 1    | 0    |
| 1      | 0    | 1    | 1    | 0    | 0    | 0    | 0    |
| 2      | 1    | 1    | 0    | 1    | 1    | 0    | 1    |
| 3      | 1    | 1    | 1    | 1    | 0    | 0    | 1    |
| 4      | 0    | 1    | 1    | 0    | 0    | 1    | 1    |
| 5      | 1    | 0    | 1    | 1    | 0    | 1    | 1    |
| 6      | 0    | 0    | 1    | 1    | 1    | 1    | 1    |
| 7      | 1    | 1    | 1    | 0    | 0    | 0    | 0    |
| 8      | 1    | 1    | 1    | 1    | 1    | 1    | 1    |
| 9      | 1    | 1    | 1    | 0    | 0    | 1    | 1    |

---
![[7 segment pinout with Arduino.png|500]]

---
# button module
[Arduino 4x4薄膜鍵盤模組實驗（一）：按鍵掃描程式原理說明 - 超圖解系列圖書](https://swf.com.tw/?p=917)
[Arduino筆記 07. 七段顯示器(7-Segment Display) - HackMD](https://hackmd.io/@hschen41/%E4%B8%83%E6%AE%B5%E9%A1%AF%E7%A4%BA%E5%99%A8)
[（十）msp430：7段显示器与MSP-EXP430G2 TI Launchpad连接 – 趣讨教](https://www.qutaojiao.com/18851.html)
[energia.nu/guide/tutorials/other/sidekick/sidekick_sevensegmentdisplay/](https://energia.nu/guide/tutorials/other/sidekick/sidekick_sevensegmentdisplay/)

接線30分鐘
[MSP430 Serial Monitor](https://www.youtube.com/watch?v=Fzf8q6fgxfQ)
[[MSP430G2553 LaunchPad™ Development Kit.pdf]]