register & control bit ：返回!0表示被設置
register |= control bit：設置該位為1，但其他維持一樣
register &=  ~control bit：上面的相反
## UCAxCTL0
contains the configuration for the protocol.
![[Pasted image 20240303154812.png]]

| Bit Field | Description                                            | 0                   | 1                                                 |
| --------- | ------------------------------------------------------ | ------------------- | ------------------------------------------------- |
| UCPEN     | Parity enable                                          | Parity disabled     | Parity enabled                                    |
| UCPAR     | Parity mode selection                                  | Odd parity          | Even parity                                       |
| UCMSB     | MSB (most significant bit) first selection             | LSB first           | MSB first                                         |
| UC7BIT    | Data length                                            | 8-bit data          | 7-bit data                                        |
| UCSPB     | Number of stop bits                                    | One stop bit        | Two stop bits                                     |
| UCMODEx   | USCI mode asynchronous mode (only valid when UCSYNC=0) | UART mode           | Idle-line multiprocessor mode (01)                |
|           |                                                        |                     | Address-bit multiprocessor mode (10)              |
|           |                                                        |                     | UART mode with automatic baud rate detection (11) |
| UCSYNC    | Synchronous/Asynchronous mode                          | Asynchronous (UART) | Synchronous (SPI)                                 |

---
## UCAxCTL1
configures the USCI module in terms of clocking, enable, interrupts etc.
![[Pasted image 20240303154821.png]]

| Bit Field | Description                                           | 00                           | 01                                 | 10                               | 11                               |
|-----------|-------------------------------------------------------|------------------------------|------------------------------------|----------------------------------|----------------------------------|
| UCSSELx   | USCI clock source select                              | UCLK external clock source   | ACLK                               | SMCLK                            | SMCLK                            |
| UCRXEIE   | Erroneous character received interrupt enable         | Characters received with errors are dropped and no interrupt raised | Characters received with errors are retained and UCAxRXIFG is set |                                  |                                  |
| UCBRKIE   | Break character received interrupt enable             | Receiving a break character does not raise an interrupt | Receiving a break character raises UCAxRXIFG |                                  |                                  |
| UCDORM    | Set USCI module to sleep mode (dormant)               | Not in sleep mode            | Sleep mode – certain characters can still raise an interrupt on UCAxRXIFG |                                  |                                  |
| UCTXADDR  | Transmit address marker – only valid for address-bit multiprocessor mode | Next frame is data           | Next frame is marked as an address |                                  |                                  |
| UCTXBRK   | Transmit break – all symbols in the transmission are low | Next frame is not a break    | Next frame transmitted is a break   |                                  |                                  |
| UCSWRST   | Module software reset – USCI is held in reset by default on power on or device reset and must be cleared by software to enable the module | USCI operational – not in reset | Reset USCI module                 |                                  |                                  |

---
## UCAxSTAT
 the status of the module
![[Pasted image 20240303154827.png]]

| Bit Field | Description                                                                                             | 0                                        | 1                                                      |
|-----------|---------------------------------------------------------------------------------------------------------|------------------------------------------|--------------------------------------------------------|
| UCLISTEN  | Loopback (listen) enable. When enabled TX is fed into the RX                                            | Loopback disabled                        | Loopback enabled                                       |
| UCFE      | Framing error detect                                                                                    | No framing error detected                | A frame with a low stop bit detected                   |
| UCOE      | Overrun error – a character was received and stored in UCAxRXBUF before it was read by software        | No overrun error detected                | Overrun error detected                                 |
| UCPE      | Parity error detect                                                                                     | No parity error detected                 | Parity error detected                                  |
| UCBRK     | Break frame detect                                                                                      | No break frame detected                  | Break frame detected                                   |
| UCRXERR   | Character received with an error. This bit is cleared by reading UCAxRXBUF                              | Character received does not contain an error | Character received contains error                   |
| UCADDR    | Address received – only in address-bit multiprocessor mode                                              | Data received                            | Address received (address bit set)                     |
| UCIDLE    | Idle line detected – only in idle-line multiprocessor mode                                              | Idle line not detected                   | Idle line detected                                     |
| UCBUSY    | USCI module busy – either transmit or receive operation in progress                                     | USCI not busy                            | USCI operation in progress                             |


---
## SFR
interrupt enable bits, may be used by other modules depending on the specific device
![[Pasted image 20240303171614.png]]
- UCA0TXIE: USCI_A0 transmit interrupt enable
    - 0 Transmit interrupt disabled
    - 1 Transmit interrupt enabled
- UCA0RXIE: USCI_A0 receive interrupt enable
    - 0 Receive interrupt disabled
    - 1 Receive interrupt enabled

---
## SFR IFG2
nterrupt enable bits
![[Pasted image 20240303171612.png]]
- UCA1TXIFG: USCI_A0 transmit complete interrupt flag
    - 0 No interrupt pending
    - 1 Interrupt pending
- UCA1RXIFG: USCI_A0 receive interrupt flag
    - 0 No interrupt pending
    - 1 Interrupt pending