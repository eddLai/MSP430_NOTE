---
bg: "[[NTKLab_white bg.png]]"
---
<style>
    .reveal {
        font-family: 'Times New Roman', 'Standard Kai', serif;
        font-size: 40px;
        text-align: left; /* Correction applied */
    }
    .with-border {
        border: 1px solid red;
    }
</style>
---
<!-- element class="fragment fade-up" -->
::: block <!-- element style="background-color: black; font-family: Time New Roman; font-size: 80px;" -->
Class 1: An Introduction to Embedded Systems
:::
<!-- slide bg="[[MSP430 HD pic.png]]" -->

---
## Why Embedded Systems?
%% 21:03 賴宏達 上課是啟發興趣而不是教你所有細節
21:03 賴宏達 所以答案你們要自己找網路
21:04 賴宏達 我也只比你們大一兩屆
21:04 賴宏達 20歲
21:04 賴宏達 所以你們可以輕而易舉的超越我 %%
%% 等下很刺激，如果順利應該一下就解決，但是很常遇到硬體問題，跟電腦不相容 %%
<div style="font-family: 'Standard Kai'; text-align: left;">
What can embedded platforms do?<br>
Examples: (==Remember to prepare the final project==)<br>
</div>

- [Laser Scanning Microscope from a Blu-ray Player](https://www.youtube.com/watch?v=xfuWbnMYOos)
+ [RL Robot Dog](https://www.youtube.com/watch?v=bnKOeMoibLg)
+ [Drone Camera](https://youtu.be/0ql20JKrscQ?si=gVeQsk3uIRJ7cHQK)
+ [Remote Control](https://youtube.com/shorts/XpFgRPBc53Y?si=R1Bd89zEwpVDFSdN) + [Remote-Control Car](https://youtube.com/shorts/NbVywWpCxbY?si=TxnPLvtMHPK0F273)
+ [FPV Camera](https://youtube.com/shorts/Ls8sYQf2LmA?si=BQWC_4mvnUI6BOg4)

%% + Surgical Slide Table
+ Robotic Arm
+ Autonomous Vehicle
+ Zip Line %%
(Many projects above are open source) %% Explanation of open source %%
<!-- element class="with-border" -->

---
### Why MSP430?
%% Suitable for medical devices %%
- Ultra-low power consumption
- Reducing the impact of EMI %% Electromagnetic interference %%
- Extending battery life
- Permanent safety fuse %% Protection from electrical faults %%
- Bootloader with 256-bit password protection
- Built-in RTC for time tracking and sleep wake-up
<!-- element style="font-family: 'Standard Kai'; font-size: 40px;"-->

<grid drag="80 20" drop="bottom" bg="gray">
「MSP430 在 3V 系统中以 1MIPS 工作状态下只消耗电流约 250μA，而且它可以从 0.8μA 的 待机状态下在 1μs（F2xx 系列）内唤醒进入全速运行模式。」
[利用超低功耗单片机 MSP430 作为系统伴随芯片 (ti.com)](https://www.ti.com/cn/lit/an/zhca117/zhca117.pdf?ts=1710052319647&ref_url=https%253A%252F%252Fwww.google.com%252F)
<!-- element style="font-family: 標楷體; font-size: 25px; align: left; text-align: left;" -->
</grid>

---
<split wrap="2">
![[記憶體規格.png|300]]![[時脈對電供圖.jpg|600]]
</split>

---
## Development Environment: Ti Code Composer Studio (CCS)
Refer to：==**[[下載及安裝TI MSP 430 CCS程式的步驟.pdf|Link]]**==
![[CSS IDE.png]]
The CSS environment compiler helps ensure minimal power consumption, one of its benefits.

---
## What's Embedded C?
Standard C language is designed for computers with high computational power, meaning those with operating systems, such as Mac, Windows, Linux. However, using it on a microcontroller requires various optimizations.
Special syntax includes:

- Declaration of `volatile`: to prevent optimization of variables
- [[ISR code]] (#InternalLinks): `__interrupt`

---
## Register Operations
```C[1-2|3|4|5-6|8]
To set the pin register to output state, the least significant bit needs to be 1.
Any operation |= with 0x01 results in the least significant bit being 1.
P1DIR    = 0000 0010
0x01     = 0000 0001
-------------------
Result of OR operation = 0000 0011

Conversely, ^= with 0x01 calculates an output result that is inverted.
```
Advanced library syntax like DriverLib provides: `GPIO_setOutputHighOnPin()`

---
## Interrupt Service Routines (ISR)
Besides event notification, ISRs are used for system operation optimization (multitasking, priority handling).
<!-- element style="font-size: 40px; text-align: left;" -->
For example, using ISR allows UART transmission without needing to be placed in the main loop. The logic for sending and receiving is encapsulated within
<!-- element style="font-size: 25px;text-align: left;"-->
- [【MSP430教學-第十一課】UART串列通訊(六) – TX Interrupt + RX Interrupt 練習 – MSP430系列分享與教學 (wordpress.com)](https://msp430teaching.wordpress.com/2018/08/31/%E3%80%90msp430%E6%95%99%E5%AD%B8-%E7%AC%AC%E5%8D%81%E4%B8%80%E8%AA%B2%E3%80%91uart%E4%B8%B2%E5%88%97%E9%80%9A%E8%A8%8A%E5%85%AD-tx-interrupt-rx-interrupt-%E7%B7%B4%E7%BF%92/)
- [MSP430 Fundamentals Workshop (ti.com)](https://software-dl.ti.com/ccs/esd/training/workshop/ccsv9/ccs_msp430_fundamentals_workshop.html#requirements)
<!-- element style="text-align: left;"-->
---
## Arduino Framework
Adds an abstraction layer on top of Embedded C to facilitate ease of use. The development environment utilizes Visual Studio Code with PlatformIO as the editor, stemming from the collaboration with TI to develop the Energia framework.
<!-- element style="font-size: 30px;text-align: left;"-->
1. Find the extension by entering "PlatformIO".
![[PlatformIO setup1.png|300]]
2. After downloading, create a new project.

---
Origin [ENERGIA IDE, configuration, compiler or debugger | TI.com](https://www.ti.com/tool/ENERGIA?utm_source=google&utm_medium=cpc&utm_campaign=epd-null-null-44700045336317950_prodfolderdynamic-cpc-pf-google-tw_int&utm_content=prodfolddynamic&ds_k=DYNAMIC+SEARCH+ADS&DCM=yes&gad_source=1&gclid=Cj0KCQjwwYSwBhDcARIsAOyL0fi1f9KjQZuTs-9nKmrvwt_T5PpAgz3sXepCp46o8rye02Rng1G5fYkaAj8XEALw_wcB&gclsrc=aw.ds#downloads)

you can also download .zip and click the 

executable file inside
<!-- element class="with-border" -->

---
### File Structure
<!-- element style="font-size: 70px;text-align: left;"-->

- `.ini` file: A PlatformIO project configuration file, specifying the IDE compilation method.
```
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
lib_deps = 
	SPI

[env:esp32doit-devkit-v1]
platform = espressif32
board = esp32doit-devkit-v1
monitor_speed = 115200
framework = arduino
lib_deps = 
```
- `src`: Contains the source code, such as `main.cpp`.
- `.pio`: System-generated files, storing temporary files created during compilation and upload processes.
- `.lib`: Stores third-party libraries, including a README file.

Operations: Build, Upload, Monitor, Clean.

---
### Today's Tasks
blink the led

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