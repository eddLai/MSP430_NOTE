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
Class2：Serial Debug and Arithmetic Encoding
<!-- element style="background-color: black; font-size: 60px;align: left; text-align: middle;color: white"-->
</grid>

<grid drag="50 10" drop="40 70">
TA: 賴宏達\
eddlai.be10@nycu.edu.tw
<!-- element style="background-color: black;font-size: 40px;align: right; text-align: right;color: white"-->
</grid>

<!-- slide bg="[[MSP430 HD pic.png]]" -->

---
# Goad
debug需要人機互動介面(User interface)\
Serial通訊\
Transmit and Receive\
Mac的Energia替代(如果想要vscode的也可以學):
[platform-timsp430/examples/arduino-blink at master · platformio/platform-timsp430](https://github.com/platformio/platform-timsp430/tree/master/examples/arduino-blink)
`pio run -e lpmsp430g2553 --target upload`

---
![[platformIO setup.png]]

---
![[platformIO monitor.png]]

---
# Task
螢幕上顯示一組數字+透過UART送出隨機變化的一組補碼字串，要寫code進行計算，然後print出一樣的結果\
依據難度，看大家的解題狀況：
- Two's components(可以用現有函式) 1分
- Two's components 1分
- One's Complement 2分
- IEEE-754 float 3分

---
![[Class2 result.png]]

---
# Pinout
![[UART module.png]]
![[pinout MSP430G2ET.png]]

---
解釋：什麼是GPIO\
什麼只有特定的腳位可以接特定的功能?
![[MSPG2553.png]]

---
![[nearsight of MSPG2553.png]]

---
![[Device manager.png]]

---
# Framework Design
(手繪很醜的架構圖, 一組提一個function block)\
Homework: 漂亮的圖+Bug Log

---
- PC Serial code
- UART TTL module連接電腦
- MSP430 Serial code
- MSP430 Arithmetic code

---
# Hint
- 參考IDE提供的範例程式(開一次)
- 補數的bit數量
- RX, TX相反
- baudrate一定要對
-  歡迎使用 UART 測試工具
請輸入 UART 端口 (如 COM3 / /dev/ttyUSB0): COM14(注意)

---
# USB
- MSP Application UART1: 用來燒錄
- MSP Debug interface
![[Debug interface.png|500]]

[ti.com/lit/ug/slau772a/slau772a.pdf?ts=1740642273939](https://www.ti.com/lit/ug/slau772a/slau772a.pdf?ts=1740642273939)

---
一開始就給
```C++
#include <Arduino.h>

#define BAUD_RATE 4800  // UART 波特率
#define RX_PIN P1_1  // 硬體 UART RX
#define TX_PIN P1_2  // 硬體 UART TX

String receivedString = "";  // 存儲接收的 UART 數據

void setup() {
    Serial.begin(BAUD_RATE);
    Serial.println("MSP430 UART RX/TX 測試開始 (4800 baud)");
}

void loop() {
    while (Serial.available()) {  // 如果有 UART 數據
        char c = Serial.read();  // 讀取單個字元

        if (c == '\n' || c == '\r') {  // 偵測換行符
            Serial.println(receivedString);
            receivedString = "";  // 清空字串，準備接收新的數據
        } else {
            receivedString += c;  // 累積字元
        }
    }
}

```


---
11:30\
接線圖
![[pinout connection of TTLmodule.png|500]]


---
## complete code
```C++
#include <Arduino.h>

#define BAUD_RATE 115200  // UART 波特率
#define RX_PIN 20  // 設定 UART RX (ESP32-C3)
#define TX_PIN 21  // 設定 UART TX (ESP32-C3)
// 使用 ESP32 UART2 (Serial1)

// 全域變數
String receivedString = "";  // 儲存接收到的字串
int mode = 8;  // 預設 8-bit 解析模式

int32_t parseTwosComplement(String binary);  // 函數前置宣告

void setup() {
    Serial.begin(BAUD_RATE);  // USB-UART，用於除錯
    Serial1.begin(BAUD_RATE, SERIAL_8N1, RX_PIN, TX_PIN);  // UART2

    Serial.println("🔹 ESP32-C3 UART Receiver");
    Serial.println("請選擇解析模式:");
    Serial.println("  1. 8-bit 二補數");
    Serial.println("  2. 16-bit 二補數");
    Serial.println("  3. 32-bit 二補數");
    Serial.println("請輸入選項 (1~3):");
}

void loop() {
    // 檢查是否有用戶透過 USB 輸入解析模式
    if (Serial.available()) {
        char inputChar = Serial.read();
        if (inputChar >= '1' && inputChar <= '3') {
            mode = (inputChar == '1') ? 8 : (inputChar == '2') ? 16 : 32;
            Serial.print("✅ 已選擇 ");
            Serial.print(mode);
            Serial.println("-bit 二補數解析模式");
        }
    }

    // 檢查是否從 **UART2** (Serial1) 接收到數據
    while (Serial1.available()) {
        char c = Serial1.read();

        if (c == '\n' || c == '\r') {  // 偵測到換行，表示一組數據結束
            if (receivedString.startsWith("TWO:")) {
                String binaryStr = receivedString.substring(4);
                int32_t result = parseTwosComplement(binaryStr);

                // 顯示結果
                Serial.print("🟢 解析結果: ");
                Serial.println(result);
                Serial1.print("🟢 解析結果: ");  // 也回傳結果到 UART2
                Serial1.println(result);
            }
            receivedString = "";  // 清空字串，準備接收下一組數據
        } else {
            receivedString += c;  // 累積接收的字元
        }
    }
}

// 解析二補數
int32_t parseTwosComplement(String binary) {
    int bits = binary.length();  
    int32_t value = 0;

    // 轉換二進制字串為整數
    for (int i = 0; i < bits; i++) {
        value = (value << 1) | (binary[i] - '0');
    }

    // 處理負數 (如果最高位是 1)
    if (binary[0] == '1') {  
        value -= (1 << bits);  
    }

    return value;
}

```