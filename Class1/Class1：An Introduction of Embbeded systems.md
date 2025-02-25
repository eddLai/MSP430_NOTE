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

一桌4~5人，
wifi: Asus2.4G\
密碼nycu87557573

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
# Why MSP430?
%% 適合醫材 %%
真正的工業級應用(舉例：其ADC vs ESP32)
- 超低功耗
- 降低EMI的影響%% 電磁干擾 %%
- 延長電池壽命
- 永久安全容絲%% 免受電器故障影響 %%
- 引導程序的256位密碼保護
- 內建RTC用於時間追蹤以及睡眠喚醒

<grid drag="80 20" drop="bottom" bg="gray">
「MSP430 在 3V 系统中以 1MIPS 工作状态下只消耗电流约 250μA，而且它可以从 0.8μA 的 待机状态下在 1μs（F2xx 系列）内唤醒进入全速运行模式。」
[利用超低功耗单片机 MSP430 作为系统伴随芯片 (ti.com)](https://www.ti.com/cn/lit/an/zhca117/zhca117.pdf?ts=1710052319647&ref_url=https%253A%252F%252Fwww.google.com%252F)
<!-- element style="font-size: 25px;align: left; text-align: left;"-->
</grid>

---
<split wrap="2">
![[記憶體規格.png|300]]![[時脈對電供圖.jpg|600]]
</split>

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
<!-- element style="font-size: 25px;text-align: left;"-->
- [【MSP430教學-第十一課】UART串列通訊(六) – TX Interrupt + RX Interrupt 練習 – MSP430系列分享與教學 (wordpress.com)](https://msp430teaching.wordpress.com/2018/08/31/%E3%80%90msp430%E6%95%99%E5%AD%B8-%E7%AC%AC%E5%8D%81%E4%B8%80%E8%AA%B2%E3%80%91uart%E4%B8%B2%E5%88%97%E9%80%9A%E8%A8%8A%E5%85%AD-tx-interrupt-rx-interrupt-%E7%B7%B4%E7%BF%92/)
- [MSP430 Fundamentals Workshop (ti.com)](https://software-dl.ti.com/ccs/esd/training/workshop/ccsv9/ccs_msp430_fundamentals_workshop.html#requirements)
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
```
[env:lpmsp430g2231]
platform = timsp430
board = lpmsp430g2231
framework = arduino
```
- src: source code，存放main.cpp
- .pio：系統產生文件，存放編譯和上傳過程中生成的臨時文件
- .lib：儲存第三方庫，其中有README

操作：Build、Upload、Monitor、Clean

---
# 本日任務

1. 設定platformIO
2. 完成Arduino framework的[[LED blinkin]]
3. 下載CSS開發環境
4. 完成[[LED blinking.c]]
5. 提供debug log：遇到的問題+解決方法圖(做完的可以先走，但是要報告一下這個)

(下課前沒寫出來就扣分)\
多使用chatgpt，但是嵌入式的code需要自己找出特化的定義
\
<i class="fas fa-circle-notch fa-spin fa-2x"></i>
交大電機DSP課就在機械碼，我們難度30%就好\
不然過四年就是從頭輸到尾\
建議各位以後的課程要先預習否則會做不完\
覺得太簡單的可以私下找我，可以提高大家的難度

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

---
Attachments 2:
LED blinking in CSS
```C
#include <msp430.h>				

void main(void)
{
	WDTCTL = ;		// stop watchdog timer，
	//watchdog用於確認系統響應正常，密碼or控制位
	P1DIR = ;		// configure P1.0 as output

	;		// 分配一個變量，記得volatile to prevent optimization

	while(1)
	{
			// toggle P1.0
			// delay 使用迴圈
	}
}
```