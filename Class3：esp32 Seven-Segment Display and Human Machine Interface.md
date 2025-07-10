---
bg: "[[NTKLab_white bg.png]]"
---
---

# pinout Table

Connect the 5V wire to confirm the pin positions  
Fill in the connected pin numbers

||dis||||MSP||
|---|---|---|---|---|---|---|
|---|A|---||---||---|
|F||B|||||
|---|G|---|$→$|---||---|
|E||C|||||
|---|D|---||---||---|

---

Fill in A+B, etc.

|number|count||
|---|---|---|
|0|||
|1|||
|2|||
|3|||
|4|||
|5|||
|6|||
|7|||
|8|||
|9|||

---

Fill in 1 for ON, 0 for OFF

|number|P1_1|P1_2|P1_3|P1_4|P1_5|P1_6|P1_7|
|---|---|---|---|---|---|---|---|
|0||||||||
|1||||||||
|2||||||||
|3||||||||
|4||||||||
|5||||||||
|6||||||||
|7||||||||
|8||||||||
|9||||||||

---

![[7 segments display pinout.png]]  
Common cathode is used to reduce current consumption (each pin has a current limit)

---

# Arduino

## Hint

```C++
byte num[10][7] = ??
byte pinMapping[7] = {P1_1, P1_2, P1_3, P1_4, P1_5, P1_6, P1_7};
digitalWrite(pinMapping[i], HIGH);
digitalWrite(pinMapping[i], LOW);
```

---


| Register |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- |
| BIT1     | 1   | 0   | 0   | 0   | 0   |     |


|BIT1|1|0|0|0|0|0|0|
|BIT5|0|0|0|0|1|0|0|
|+||||||||
|BIT1+BIT5|1|0|0|0|1|0|0|

---

## Register

![[PxIN Register.png]]

---

The seventh pin is HIGH, so BIT7 must be specified  
![[PxOUT Register.png]]

---

Input/output direction  
![[PxDIR Register.png]]

---

# Task

Note: Not adding a resistor may damage the display. ==Only one per person==
1. Use Arduino: Complete counting from 0 to 9, and check the accuracy with a stopwatch
    
2. ![[7 segment display with resistor.png|300]]
    

---

# Related
- [Arduino Notes 07. 7-Segment Display - HackMD](https://hackmd.io/@hschen41/%E4%B8%83%E6%AE%B5%E9%A1%AF%E7%A4%BA%E5%99%A8)    
- [MSP430 and 7-Segment Display with MSP-EXP430G2 TI Launchpad – Qutaojiao](https://www.qutaojiao.com/18851.html)
- [energia.nu/guide/tutorials/other/sidekick/sidekick_sevensegmentdisplay/](https://energia.nu/guide/tutorials/other/sidekick/sidekick_sevensegmentdisplay/)