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
Class2：Serial Debugging and Arithmetic Encoding
<!-- element style="background-color: black; font-size: 60px;align: left; text-align: middle;color: white"-->
</grid>

<grid drag="50 10" drop="40 70">
TA: 賴宏達\
eddlai.be10@nycu.edu.tw
<!-- element style="background-color: black;font-size: 40px;align: right; text-align: right;color: white"-->
</grid>

<!-- slide bg="[[MSP430 HD pic.png]]" -->

---
# Goal

debug $\rightarrow$ Human-Machine Interface (User Interface)  
Serial Communication $\rightarrow$ Transmit and Receive\

---

![[platformIO monitor.png]]

---

# Task

Display a number on screen + use UART to transmit a randomly changing complement-encoded string. You must write code to compute it and print the same result  
Depending on difficulty and solution status:

- Two's Complement (with helper functions) 1 pt    
- Two's Complement 1 pt
- One's Complement 2 pts
- IEEE-754 Float 3 pts
    

---

![[Class2 result.png]]

---

# Pinout
<split no-margin>
![[UART module.png|400]]
![[esp32 pinout.png|500]]
</split>

---

![[ESP32 C3 super mini pinout.jpeg]]

---

Explanation: What is GPIO  
Why only specific pins support specific functions?  
![[MSPG2553.png]]

---

![[nearsight of MSPG2553.png]]

---

![[Device manager.png]]

---

# Framework Design

(Ugly hand-drawn diagram, submit one function block per group)  
Homework: Polished diagram + Bug Log

---
- PC Serial Code
- UART TTL Module to PC
- ESP32 Serial Code
- ESP32 Arithmetic Code

---

![[Framework Design hand made.png]]

---

# Hint
- Refer to example code in the IDE
- Bit-width of complement
- RX, TX are inverted
- Baudrate must match
- Welcome to the UART Test Tool  
    Enter UART Port (e.g., COM3 / /dev/ttyUSB0): COM14 (note)
    

---

Initial starter code:

```C++
#include <Arduino.h>

#define BAUD_RATE 9600
#define RX_PIN P1_1
#define TX_PIN P1_2

String receivedString = "";

void setup() {
    Serial.begin(BAUD_RATE);
    Serial.println("MSP430 UART RX/TX Test Start (? baud)");
}

void loop() {
    while (Serial.available()) {
        char c = Serial.read();
        if (c == '\n' || c == '\r') {
            Serial.println(receivedString);
            receivedString = "";
        } else {
            receivedString += c;
        }
    }
}
```

---

11:30 connection diagram released  
![[pinout connection of TTLmodule.png|400]]

---

## complete code

```C++
#include <Arduino.h>

#define BAUD_RATE 115200
#define RX_PIN 20
#define TX_PIN 21

String receivedString = "";
int mode = 8;

int32_t parseTwosComplement(String binary);

void setup() {
    Serial.begin(BAUD_RATE);
    Serial1.begin(BAUD_RATE, SERIAL_8N1, RX_PIN, TX_PIN);

    Serial.println("🔹 ESP32-C3 UART Receiver");
    Serial.println("Select parsing mode:");
    Serial.println("  1. 8-bit Two's Complement");
    Serial.println("  2. 16-bit Two's Complement");
    Serial.println("  3. 32-bit Two's Complement");
    Serial.println("Enter option (1~3):");
}

void loop() {
    if (Serial.available()) {
        char inputChar = Serial.read();
        if (inputChar >= '1' && inputChar <= '3') {
            mode = (inputChar == '1') ? 8 : (inputChar == '2') ? 16 : 32;
            Serial.print("✅ Mode selected: ");
            Serial.print(mode);
            Serial.println("-bit Two's Complement");
        }
    }

    while (Serial1.available()) {
        char c = Serial1.read();
        if (c == '\n' || c == '\r') {
            if (receivedString.startsWith("TWO:")) {
                String binaryStr = receivedString.substring(4);
                int32_t result = parseTwosComplement(binaryStr);
                Serial.print("🟢 Result: ");
                Serial.println(result);
                Serial1.print("🟢 Result: ");
                Serial1.println(result);
            }
            receivedString = "";
        } else {
            receivedString += c;
        }
    }
}

int32_t parseTwosComplement(String binary) {
    int bits = binary.length();
    int32_t value = 0;
    for (int i = 0; i < bits; i++) {
        value = (value << 1) | (binary[i] - '0');
    }
    if (binary[0] == '1') {
        value -= (1 << bits);
    }
    return value;
}
```

---

# Grading Criteria:
Diagram drawing:
- 20%: Complete, 15~20 pts
- 20%: ...
- 10%: Submit = 7~10 pts
- 50%: Full/partial depending on check
    

---

```python
import serial
import random
import struct
import time

print("🔹 Welcome to the UART Test Tool")
uart_port = input("Please enter UART port (e.g., COM3 / /dev/ttyUSB0): ").strip()
baud_rate = 9600

print("\n🔹 Select the encoding type to test:")
print("  1. Two's Complement")
print("  2. One's Complement")
print("  3. IEEE-754 Floating Point")
print("  4. Send All")
mode = input("Please select (1~4): ").strip()

ser = None

try:
    ser = serial.Serial(uart_port, baud_rate, timeout=1)
    print(f"(O) Successfully connected to {uart_port}, starting data transmission...\n")
except Exception as e:
    print(f"(X) Unable to open UART port: {e}")
    print("(!) Data will be displayed only, not sent")

def twos_complement(value, bits):
    if value < 0:
        value = (1 << bits) + value
    return format(value, f"0{bits}b")

def ones_complement(value, bits):
    if value < 0:
        value = ~(-value)
    return format(value & ((1 << bits) - 1), f"0{bits}b")

def ieee_754_float(value):
    binary = struct.unpack('!I', struct.pack('!f', value))[0]
    return format(binary, "032b")

def send_uart(binary_str):
    if ser:
        ser.write(binary_str.encode() + b'\n')
    else:
        print(f"(X) Unable to send: {binary_str}")

while True:
    int_value = random.randint(-128, 127)
    float_value = round(random.uniform(-10, 10), 2)

    twos_str = twos_complement(int_value, 8)
    ones_str = ones_complement(int_value, 8)
    ieee_str = ieee_754_float(float_value)

    print(f"\n🔹 Random Data: {int_value} (int), {float_value} (float)")

    if mode == "1" or mode == "4":
        print(f"  - Two's Complement: {twos_str}")
        send_uart(f"TWO:{twos_str}")

    if mode == "2" or mode == "4":
        print(f"  - One's Complement: {ones_str}")
        send_uart(f"ONE:{ones_str}")

    if mode == "3" or mode == "4":
        print(f"  - IEEE-754 Float: {ieee_str}")
        send_uart(f"FLT:{ieee_str}")

    time.sleep(0.5)
```