---
bg: "[[NTKLab_white bg.png]]"
---
---

# Why Embedded System?

- [Laser Scanning Microscope from Blu-ray Player](https://www.youtube.com/watch?v=xfuWbnMYOos)
    

- [RL Robot dog](https://www.youtube.com/watch?v=bnKOeMoibLg)
    
- [Drone Camera](https://youtu.be/0ql20JKrscQ?si=gVeQsk3uIRJ7cHQK)
    
- [Remote Control](https://youtube.com/shorts/XpFgRPBc53Y?si=R1Bd89zEwpVDFSdN)+[Remote Control Car](https://youtube.com/shorts/NbVywWpCxbY?si=TxnPLvtMHPK0F273)
    
- [FPV Camera](https://youtube.com/shorts/Ls8sYQf2LmA?si=BQWC_4mvnUI6BOg4)
    

%% + Slide Rail Surgical Robot

- Robotic Arm
    
- Autonomous Vehicle
    
- Zipline %%  
    (Many projects are open source, explain what open source means)
    

---

# What's Embedded C

Standard C language is designed for high-performance computing platforms, meaning computers with operating systems such as Mac, Windows, and Linux.  
But when used on microcontrollers, various optimizations are needed.  
Some special syntax examples include:

- `volatile` declaration: prevents variable optimization
    
- [[ISR code]]: `__interrupted`
    

---

## Register Operations

```yaml
To set pin registers as output mode, the lowest bit must be set to 1
Any result of |= with 0x01 will make the lowest bit 1
P1DIR    = 0000 0010
0x01     = 0000 0001
-------------------
OR result = 0000 0011

Then ^= with 0x01 will toggle the lowest bit
```

Advanced libraries like DriverLib offer: `GPIO_setOutputHighOnPin()`

---

## Interrupt Service Routine (ISR)

Besides event notification, ISR is also used for system optimization (multitasking, priority handling)

Example: Using ISR to transmit UART without placing it in the main loop  
Send and receive logic is encapsulated within ISR. This is part of the driver layer, but it is hardware-interrupt-driven, not main-loop-driven.  
[https://docs.arduino.cc/language-reference/en/functions/external-interrupts/attachInterrupt/](https://docs.arduino.cc/language-reference/en/functions/external-interrupts/attachInterrupt/)

```cpp
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

---

## Arduino Framework

Adds an abstraction layer over Embedded C to make it easier to use.  
Development Environment: VSCode + PlatformIO as the editor, based on the Energia framework developed in collaboration with TI

1. Search for "PlatformIO" in Extensions  
    ![[PlatformIO setup1.png|300]]
    
2. After downloading, create a new project
    

---

# Project File Structure

- `.ini` file: PlatformIO project configuration file, defines IDE build behavior
    

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

- `src`: source code folder, contains `main.cpp`
    
- `.pio`: system-generated folder, contains temporary build/upload files
    
- `.lib`: third-party libraries, may contain README
    

Operations: Build, Upload, Monitor, Clean

---

# Today's Tasks

1. Set up Energia
    
2. Complete Arduino framework [[LED blinking]]
    
3. Download Code Composer Studio development environment
    
4. Complete [[LED blinking.c]]
    
5. Submit debug log: problem encountered + solution with screenshots
    

> wifi: Asus2.4G  
> password: nycu87557573  
> Use ChatGPT extensively, but for embedded code, you must research specific definitions yourself.  
>   
>   
> It is recommended to preview future lessons or you won’t finish on time  
> If you feel the current tasks are too simple, contact me privately for harder challenges

If your network is slow, come to the front and plug into Ethernet

---

Attachments:

- A firmware update is required for the MSP430 Debug Interface (MSP-FET430UIF / MSP-FET / eZ-FET)
    
- [MSP-EXP430G2ET Quick Start Guide](https://www.ti.com/lit/pdf/swmu005)
    
- [MSP430G2553 LaunchPad™ Development Kit (MSP-EXP430G2ET) User's Guide (Rev. A)](https://www.ti.com/lit/pdf/slau772)
    
- [MSP430g2553 datasheet](https://www.ti.com/lit/ds/symlink/msp430g2553.pdf?ts=1740213125627)
    
- [MSP430G2553 User Guide](https://www.ti.com/lit/ug/slau144k/slau144k.pdf?ts=1740236247753&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FMSP430G2553)
    

---

Attachments1:  
LED blinking in Arduino

```Arduino
#include <Arduino.h>

#define LED

// find pins_energia.h for more LED definitions
  
// initialization and it runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode();     
}

// the loop routine runs over and over again forever:
void loop() {
  // turn the LED on and off depending on voltage level
  // Bonus: wait for 1, 2, ... ~10 seconds, accumulate longer delays
}
```