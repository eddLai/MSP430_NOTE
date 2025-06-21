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

0900\~0930: Review and demonstrate the last question from the previous homework.
Bring TTL module to the front.

---

# Pinout Table

Connect the 5V line and identify pin positions.
Fill in the connected pin mapping:

|     | dis |     |   |     | MSP |     |
| --- | --- | --- | - | --- | --- | --- |
| --- | A   | --- |   | --- |     | --- |
| F   |     | B   |   |     |     |     |
| --- | G   | --- | → | --- |     | --- |
| E   |     | C   |   |     |     |     |
| --- | D   | --- |   | --- |     | --- |

---

Fill in A+B, etc.

| Number | Segment Combination |   |
| ------ | ------------------- | - |
| 0      |                     |   |
| 1      |                     |   |
| 2      |                     |   |
| 3      |                     |   |
| 4      |                     |   |
| 5      |                     |   |
| 6      |                     |   |
| 7      |                     |   |
| 8      |                     |   |
| 9      |                     |   |

---

Fill in 1 for ON, 0 for OFF:

| Number | P1\_1 | P1\_2 | P1\_3 | P1\_4 | P1\_5 | P1\_6 | P1\_7 |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0      |       |       |       |       |       |       |       |
| 1      |       |       |       |       |       |       |       |
| 2      |       |       |       |       |       |       |       |
| 3      |       |       |       |       |       |       |       |
| 4      |       |       |       |       |       |       |       |
| 5      |       |       |       |       |       |       |       |
| 6      |       |       |       |       |       |       |       |
| 7      |       |       |       |       |       |       |       |
| 8      |       |       |       |       |       |       |       |
| 9      |       |       |       |       |       |       |       |

---

![[7 segments display pinout.png]]
Common cathode design reduces current consumption due to per-pin current limits.

---

# Energia

## Hint

```C++
byte num[10][7] = ??
byte pinMapping[7] = {P1_1, P1_2, P1_3, P1_4, P1_5, P1_6, P1_7};
digitalWrite(pinMapping[i], HIGH);
digitalWrite(pinMapping[i], LOW);
```

---

# CCS

[MSP430F2xx, MSP430G2xx Family Reference](https://www.ti.com/lit/ug/slau144k/slau144k.pdf?ts=1741352433148#page=49.09)

```C++
#include <msp430.h>
#define a BIT1
#define b BIT2
#define c BIT3
#define d BIT4
#define e BIT5
#define f BIT6
#define g BIT7
```

| Register    | Bits          |
| ----------- | ------------- |
| BIT1        | 1 0 0 0 0 0 0 |
| BIT5        | 0 0 0 0 1 0 0 |
| BIT1 + BIT5 | 1 0 0 0 1 0 0 |

---

## Register Details

![[PxIN Register.png]]

---

Pin 7 is HIGH: set BIT7
![[PxOUT Register.png]]

---

Input/Output Direction Control
![[PxDIR Register.png]]

---

## Hint

P1DIR configures P1.1\~P1.7

```C++
void main()
{
    WDTCTL = WDTPW + WDTHOLD;
    P1DIR = ??;

    while(1)
    {
        P1OUT = ??;
        __delay_cycles(500000);
        P1OUT = ??;
        __delay_cycles(500000);
    }
}
```

# Related
- [Arduino筆記 07. 七段顯示器(7-Segment Display) - HackMD](https://hackmd.io/@hschen41/%E4%B8%83%E6%AE%B5%E9%A1%AF%E7%A4%BA%E5%99%A8)
- [（十）msp430：7段显示器与MSP-EXP430G2 TI Launchpad连接 – 趣讨教](https://www.qutaojiao.com/18851.html)
- [energia.nu/guide/tutorials/other/sidekick/sidekick_sevensegmentdisplay/](https://energia.nu/guide/tutorials/other/sidekick/sidekick_sevensegmentdisplay/)

---
# Task

**Important:** Without a resistor, the display can be damaged. Each person gets **one display only.**

1. Use Energia: Count from 0 to 9 and verify accuracy with a stopwatch.
2. Use CCS: Perform the same task.
3. **Bonus:** Add countdown using a button.

![[7 segment display with resistor.png|300]] 
---

```C++
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

byte pinMapping[7] = {P1_1, P1_2, P1_3, P1_4, P1_5, P1_6, P1_7};

void setup() {
  for (int i = 0; i < 7; i++) {         
    pinMode(pinMapping[i], OUTPUT);
    digitalWrite(pinMapping[i], HIGH);
    delay(200);
    digitalWrite(pinMapping[i], LOW);
    delay(200);
  }
  digitalWrite(pinMapping[0], HIGH);
}

void loop() {
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 7; j++) {
      digitalWrite(pinMapping[j], num[i][j]);
    }
    delay(1000);
  }
}
```

---

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

# Answer

|     | dis |     |   |       | MSP   |       |
| --- | --- | --- | - | ----- | ----- | ----- |
| --- | A   | --- |   | ---   | P1\_1 | ---   |
| F   |     | B   |   | P1\_6 |       | P1\_2 |
| --- | G   | --- | → | ---   | P1\_7 | ---   |
| E   |     | C   |   | P1\_5 |       | P1\_3 |
| --- | D   | --- |   | ---   | P1\_4 | ---   |

| Number | Segment Combo |   |
| ------ | ------------- | - |
| 0      | A+B+C+D+E+F   |   |
| 1      | B+C           |   |
| 2      | A+B+G+E+D     |   |
| 3      | A+B+C+D+G     |   |
| 4      | B+C+F+G       |   |
| 5      | A+F+G+C+D     |   |
| 6      | F+G+C+D+E     | ✓ |
| 7      | A+B+C         |   |
| 8      | A+B+C+D+E+F+G |   |
| 9      | A+B+C+G+F     | ✓ |

---

Affected by ABC definitions:

| Number | P1\_1 | P1\_2 | P1\_3 | P1\_4 | P1\_5 | P1\_6 | P1\_7 |
| ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0      | 1     | 1     | 1     | 1     | 1     | 1     | 0     |
| 1      | 0     | 1     | 1     | 0     | 0     | 0     | 0     |
| 2      | 1     | 1     | 0     | 1     | 1     | 0     | 1     |
| 3      | 1     | 1     | 1     | 1     | 0     | 0     | 1     |
| 4      | 0     | 1     | 1     | 0     | 0     | 1     | 1     |
| 5      | 1     | 0     | 1     | 1     | 0     | 1     | 1     |
| 6      | 0     | 0     | 1     | 1     | 1     | 1     | 1     |
| 7      | 1     | 1     | 1     | 0     | 0     | 0     | 0     |
| 8      | 1     | 1     | 1     | 1     | 1     | 1     | 1     |
| 9      | 1     | 1     | 1     | 0     | 0     | 1     | 1     |
