核心處理器：based on ARM microcontroller
超低功耗、模擬電路
![[pinout.png]]![[MSP430G2ET pinout.png]]

---
pin mapping：pin numbers of header vs 實體pin腳
使用前者，因為後者的會隨著硬體不同

| Pin Number on Header | Pin of MSP430G2553 |
|----------------------|--------------------|
| 1                    | 3.3 Volt           |
| 2                    | P1.0               |
| 3                    | P1.1               |
| 4                    | P1.2               |
| 5                    | P1.3               |
| 6                    | P1.4               |
| 7                    | P1.5               |
| 8                    | P2.0               |
| 9                    | P2.1               |
| 10                   | P2.2               |
| 11                   | P2.3               |
| 12                   | P2.4               |
| 13                   | P2.5               |
| 14                   | P1.6               |
| 15                   | P1.7               |
| 16                   | Rest pin           |
| 17                   | Test               |
| 18                   | P2.6               |
| 19                   | P2.7               |
| 20                   | Ground             |

---
上電時序控制
震盪器用於計時，計時對於系統是很重要的
擴充板稱為BoosterPack
Serial baud要用4800