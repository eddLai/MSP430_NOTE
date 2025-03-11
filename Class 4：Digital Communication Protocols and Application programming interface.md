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
Digital Communication Protocols and Application programming interface
<!-- element style="background-color: black; font-size: 60px;align: left; text-align: middle;color: white"-->
</grid>

<grid drag="50 10" drop="40 70">
TA: 賴宏達\
eddlai.be10@nycu.edu.tw
<!-- element style="background-color: black;font-size: 40px;align: right; text-align: right;color: white"-->
</grid>

<!-- slide bg="[[MSP430 HD pic.png]]" -->

---
# Flow
1. 軟體重置可配置狀態`UCA0CTLW0 |= UCSWRST;`
2. 關閉UCSWRST，啟動 UART `UCA0CTL1 &= ~UCSWRST;`

---
# Register Table
[msp430g2xx3_uscia0_uart_01_9600.c](https://dev.ti.com/tirex/explore/nod\e?node=A__AL4DP41WSJ9ZDY-aLKgPKg__msp430ware__IOGqZri__LATEST)\
[UART 简介实验室 — MSP430 Academy 教程](https://dev.ti.com/tirex4-desktop/content/msp430_academy_%E6%95%99%E7%A8%8B_2_01_00_00/_build_msp430_academy_%E6%95%99%E7%A8%8B_2_01_00_00/source/msp430/msp430_uart_training/msp430_uart_chinese.html)

