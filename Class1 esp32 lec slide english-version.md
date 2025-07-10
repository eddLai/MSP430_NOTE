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
Class1：An Introduction of Embbeded systems
<!-- element style="background-color: black; font-size: 60px;align: left; text-align: middle;color: white"-->
</grid>

<grid drag="50 10" drop="40 70">
TA: 賴宏達\
eddlai.be10@nycu.edu.tw
<!-- element style="background-color: black;font-size: 40px;align: right; text-align: right;color: white"-->
</grid>
<!-- slide bg="[[MSP430 HD pic.png]]" -->


---
# Why Embedded system ?
<div style="font-family:標楷體; text-align: left;">
嵌入式平台可以做什麼?<br>
舉例：(==記得準備期末專題==)<br>
</div>

- [Laser Scanning Microscope from Blu-ray Player](https://www.youtube.com/watch?v=xfuWbnMYOos)
+ [RL Robot dog](https://www.youtube.com/watch?v=bnKOeMoibLg)
+ [Drone攝影機](https://youtu.be/0ql20JKrscQ?si=gVeQsk3uIRJ7cHQK)
+ [遙控器](https://youtube.com/shorts/XpFgRPBc53Y?si=R1Bd89zEwpVDFSdN)+[遙控車](https://youtube.com/shorts/NbVywWpCxbY?si=TxnPLvtMHPK0F273)
+ [FPV Camera](https://youtube.com/shorts/Ls8sYQf2LmA?si=BQWC_4mvnUI6BOg4)

%% + 滑台手術機
+ 機器手臂
+ 自走車
+ 溜索 %%
(很多專案都是開源的，解釋opensource)
<!-- element class="with-border" -->


---
## 開發環境：Ti CCS
參考：[[下載及安裝TI MSP 430 CCS程式的步驟.pdf]]
![[CSS IDE.png]]
CSS環境編譯器會幫忙確保最低功耗，好處之一。

---
# Whtat's Embedded C
標準C語言是寫給高運算能力的電腦用的，也就是說有操作系統，例如：Mac, Window, Linux
但如果要在單晶片上使用就需要各種優化。
一些特殊的語法，例如：

- volatile宣告：避免變量被優化
- [[ISR code]]：`__interrupted`

---
## 寄存器運算
```yaml
設定腳位寄存器為輸出狀態，需要使最低位為1
任何|=與0x01的結果都是最低位1
P1DIR    = 0000 0010
0x01     = 0000 0001
-------------------
OR運算后 = 0000 0011

則^=與0x01計算輸出結果是反向的
```
高級庫語法如DriverLib提供：`GPIO_setOutputHighOnPin()`

---
## 中斷服務例程（ISR）
除了事件通知，也是用作系統運作的優化(多工、優先級處理)

例如: 使用ISR讓UART發送不需要放在主循環中
將發送和接收邏輯被封裝在ISR中，這是驅動程序的一部分，但它是由硬件中斷驅動的，不是由主循環驅動的。
https://docs.arduino.cc/language-reference/en/functions/external-interrupts/attachInterrupt/
<!-- element style="font-size: 25px;text-align: left;"-->
```
const byte ledPin = 13;
const byte interruptPin = 2;  // input pin that the interruption will be attached to
volatile byte state = LOW;  // variable that will be updated in the ISR

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(interruptPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(interruptPin), blink, CHANGE);
}

void loop() {
  digitalWrite(ledPin, state);
}

void blink() {
  state = !state;
}
```
<!-- element style="text-align: left;"-->

---
## Arduino Framework
在Embbed C上加入一個抽象層使得容易上手。
開發環境：vscode platformIO作為編輯器，源自與Ti合作發展的energia開發架構
<!-- element style="text-align: left;"-->
1. 找到Extension輸入platformIO
![[PlatformIO setup1.png|300]]
2. 下載完成後，建立專案

---
# 檔案架構
- .ini檔案：PlatformIO項目配置檔案，提供IDE編譯方式

```C
[env:esp32-c3-devkitm-1]
platform_packages = 
	toolchain-riscv32-esp @ 8.4.0+2021r2-patch5
platform = espressif32
board = esp32-c3-devkitm-1
framework = arduino
monitor_speed = 9600
build_flags = 
	-D PIO_FRAMEWORK_ARDUINO_ENABLE_CDC
	-D USBCON
	-DARDUINO_USB_CDC_ON_BOOT=1
	-DARDUINO_USB_MODE=1

[env:esp32doit-devkit-v1]
platform = espressif32
board = esp32doit-devkit-v1
monitor_speed = 115200
framework = arduino
```
- src: source code，存放main.cpp
- .pio：系統產生文件，存放編譯和上傳過程中生成的臨時文件
- .lib：儲存第三方庫，其中有README

操作：Build、Upload、Monitor、Clean

---
# 本日任務

1. 設定Energia
2. 完成Arduino framework的[[LED blinkin]]
3. 下載Code Composer Studio開發環境
4. 完成[[LED blinking.c]]
5. 提供debug log：遇到的問題+解決方法圖(做完的可以先走，但是要報告一下這個)
>wifi: Asus2.4G\
passward: nycu87557573\
多使用chatgpt，但是嵌入式的code需要自己找出特化的定義
\
<i class="fas fa-circle-notch fa-spin fa-2x"></i>
建議各位以後的課程要先預習否則會做不完\
覺得太簡單的可以私下找我，可以提高大家的難度

網速不夠快的來前面插乙太

---
附件：
- A firmware update is required for the MSP430 Debug Interface (MSP-FET430UIF / MSP-FET / eZ-FET)
- [MSP-EXP430G2ET Quick Start Guide](https://www.ti.com/lit/pdf/swmu005)
- [MSP430G2553 LaunchPad™ Development Kit (MSP-EXP430G2ET) User's Guide (Rev. A)](https://www.ti.com/lit/pdf/slau772)
- [MSP430g2553 datasheet](https://www.ti.com/lit/ds/symlink/msp430g2553.pdf?ts=1740213125627)
- [MSP430G2553 User Guide](https://www.ti.com/lit/ug/slau144k/slau144k.pdf?ts=1740236247753&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FMSP430G2553)

---
Attachments1:
LED blinking in Arduino
```Arduino C
#include <Arduino.h>

#define LED 

//find pins_energia.h for more LED definitions
  
//  initialization and it runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode();     
}

// the loop routine runs over and over again forever:
void loop() {
  // turn the LED on and off depends on voltage level
  // 加分題：每次等1, 2, ... ~10秒，累積時間越來越長
}
```