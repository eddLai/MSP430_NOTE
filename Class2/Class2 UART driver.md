## 用手機控制燈光閃爍? 使用UART


ref.
[MSP430F5529 DriverLib 库函数学习笔记（四）UART通信_串口clock pre-CSDN博客](https://blog.csdn.net/weixin_44457994/article/details/119062618)
[Usci_a_uart_api (ti.com)](https://software-dl.ti.com/msp430/msp430_public_sw/mcu/msp430/MSP430ware/1_60_02_09/exports/msp430ware_1_60_02_09/driverlib/doc/MSP430F5xx_6xx/html/group__usci__a__uart__api.html)
[msp430-sensor-sample/driverlib/MSP430F5xx_6xx/usci_a_uart.c at master · dbalatero/msp430-sensor-sample (github.com)](https://github.com/dbalatero/msp430-sensor-sample/blob/master/driverlib/MSP430F5xx_6xx/usci_a_uart.c)

---
## basic concept of data transmission
- Bard rate: how many times the lines can change state (high or low), 115200 or 9600 are commonly used.
- Data bits: ASCII碼是7bits，8bits則是擴充版的ASCII
- Stop bitts: 停止用，與處理時間相關
- Parity: 奇偶校驗，用於確保資訊傳遞中的遺失

---
## what's UART
**Universal asynchronous receiver/transmitter (UART)**
一條發送線（TX）和一條接收線（RX），以及可選的控制線。
>舉例：
>9600 7E1 – 9600 baud, 7 bits data, even parity and 1 stop bit  
>9600 8N1 – 9600 baud , 8 bits data, no parity and 1 stop bit  
>115200 8N1 – 115200 baud, 8 bits data, no parity  and 1 stop bit

![[UART Protocols.jpg|400]]

---
![[USB2TTL module.jpg|200]]
USB to TTL模組上有TX, RX腳位?
TTL描述的是電壓水平，UART則是通信標準
USB運作在非常低的電壓，將USB信號(包含協定以及電壓水平)轉換為UART信號。然後，UART信號會被進一步轉換為TTL電壓水平

---
## From hardware to Software
提供USCI module實現上述的協定。
寄存器：硬體和軟體之間的橋樑，顯示運行狀態，以下彼此獨立(時鐘就不會獨立)
舉例：UCAxSTAT。用於反映USART模組的當前狀態。各個位的意義需要查表
在寄存器名稱中，“UC”代表USART控制模組，“A”可能是指特定的USART模組（如USCI_A），“x”是指模組編號，例如USCI_A0或USCI_A1。
![[Pasted image 20240303133254.png]]

---
## Table
![[Pasted image 20240303132545.png]]
- **UCBUSY (位0)** - 可讀位，當USART模組正忙於處理一個串行傳輸時，此位為1。
- **UCIDLE (位1)** - 可讀位，指示USART是否處於閒置狀態。如果線路空閒，此位為1。
- **UCADDR (位2)** - 可讀位，用於多點通信，指示接收到的幀是否包含地址資訊。
- **UCRXERR (位3)** - 可讀位，顯示接收過程中是否有錯誤發生。
- **UCBRK (位4)** - 可讀位，表示是否檢測到一個斷開信號（break）。
- **UCPE (位5)** - 可讀位，表示是否檢測到同位檢測錯誤（parity error）。
- **UCOE (位6)** - 可讀位，表示是否有過載錯誤（overrun error），即數據丟失因為接收器來不及處理。
- **UCFE (位7)** - 可讀位，表示是否檢測到幀錯誤（framing error），如上文所述。

每個位通常都有特定的讀寫屬性
- 可讀（r）
- 可寫（w）
- 且有特定的初始值（0），表示無錯誤或閒置狀態。

---
## Workflow
- **數據接收和發送**：分別有兩個8位的寄存器，UCAxRXBUF用於接收數據，UCAxTXBUF用於發送數據。
- **7位模式**：當USCI配置為7位數據模式時，UCAxRXBUF和UCAxTXBUF的最高位（MSB）不會被使用。
- **發送數據**：將數據複製到UCAxTXBUF來開始傳輸，這個操作同時會清除UCAxTXIFG（傳輸完成中斷標誌）。
- **傳輸完成**：一旦傳輸完成，UCAxTXIFG標誌將被設置。
- **接收數據**：當線路上接收到數據時，它會被存儲在UCAxRXBUF中，並且設置UCAxRXIFG（接收中斷標誌）。
- **數據保留**：接收到的數據會保留在UCAxRXBUF寄存器中，直到軟件讀取它，或者接收到另一幀數據時被覆蓋，這時UCAxSTAT[UCOE]（過載錯誤）會被設置。
- **讀取操作**：軟件讀取UCAxRXBUF時，UCAxRXIFG標誌會被清除。

- **其他寄存器**：UCAxIRTCTL和UCAxIRRCTL寄存器用於紅外裝置，UCAxABCTL寄存器用於帶自動波特率檢測的UART。這些寄存器對於標準UART模式不是必需的，因此在本課程中不進行介紹。

---
## Program
標準C函式庫，例如：stdio中的printf調用太多資訊（為了標準化跨平臺使用）
How about let it accesses the UART directly?
src是source code的意思

附件：[[Table of  control bits]]

ref. 
[Lesson 9: UART – Simply Embedded](http://www.simplyembedded.org/tutorials/msp430-uart/)
[Parity bit - Wikipedia](https://en.wikipedia.org/wiki/Parity_bit)
