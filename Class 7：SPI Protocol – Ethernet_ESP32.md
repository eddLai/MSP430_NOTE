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
https://mischianti.org/esp32-ethernet-w5500-with-plain-http-and-ssl-https/

---
https://magicjackting.pixnet.net/blog/post/164725144

---
```C
#include <SPI.h>
#include "EthernetLarge.h"

#define W5500_CS 5  // Chip Select
#define MYIPADDR 192,168,1,28
#define MYIPMASK 255,255,255,0
#define MYDNS 192,168,1,1
#define MYGW 192,168,1,1

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("=== Begin Ethernet Test ===");

  // 初始化 CS 腳位
  Ethernet.init(W5500_CS);

  // 嘗試使用 DHCP
  if (Ethernet.begin(mac)) {
    Serial.println("✅ DHCP OK!");
    Serial.print("Local IP    : ");
    Serial.println(Ethernet.localIP());
    Serial.print("Subnet Mask : ");
    Serial.println(Ethernet.subnetMask());
    Serial.print("Gateway IP  : ");
    Serial.println(Ethernet.gatewayIP());
    Serial.print("DNS Server  : ");
    Serial.println(Ethernet.dnsServerIP());
  } else {
    Serial.println("⚠️ DHCP failed, switching to static IP...");

    // 檢查硬體與網路線
    if (Ethernet.hardwareStatus() == EthernetNoHardware) {
      Serial.println("❌ Ethernet hardware not found.");
      while (true) delay(1);
    }
    if (Ethernet.linkStatus() == LinkOFF) {
      Serial.println("⚠️ Ethernet cable not connected.");
    }

    // 設定靜態 IP
    IPAddress ip(MYIPADDR), dns(MYDNS), gw(MYGW), sn(MYIPMASK);
    Ethernet.begin(mac, ip, dns, gw, sn);

    Serial.println("✅ Static IP assigned.");
    Serial.print("Local IP    : ");
    Serial.println(Ethernet.localIP());
    Serial.print("Subnet Mask : ");
    Serial.println(Ethernet.subnetMask());
    Serial.print("Gateway IP  : ");
    Serial.println(Ethernet.gatewayIP());
    Serial.print("DNS Server  : ");
    Serial.println(Ethernet.dnsServerIP());
  }
}

void loop() {
  // 可擴充為 ping, HTTP request, TCP server 等功能
}
```

---
>小技巧：務必選好一篇文章就想辦法仔細的復刻，想辦法
1. 說明兩個Ethernet and EthernetLarge的差別
2. 