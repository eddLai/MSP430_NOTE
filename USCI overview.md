一個字母代表一種Module
- The USCI_Ax modules support:
	- UART mode
	- Pulse shaping for IrDA communications
	- Automatic baud rate detection for LIN communications
	- SPI mode
- The USCI_Bx modules support:
	- I2C mode
	- SPI mode

---
## UART mode
asynchronous mode
USCI_Ax modules connect the MSP430 to an external system via two external pins
UCAxRXD and UCAxTXD. UART mode is selected when the UCSYNC bit is cleared.