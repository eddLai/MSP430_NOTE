```C
#include <msp430.h>				

void main(void)
{
	WDTCTL = ;		// stop watchdog timer，用於確認系統響應正常，密碼or控制位
	P1DIR = ;		// configure P1.0 as output

	;		// 分配一個變量，記得volatile to prevent optimization

	while(1)
	{
			// toggle P1.0
			// delay 使用迴圈
	}
}
```

%%
```
#include <msp430.h>				

void main(void)
{
	WDTCTL = WDTPW | WDTHOLD;		// stop watchdog timer，用於確認系統響應正常
	P1DIR |= 0x01;					// configure P1.0 as output

	volatile unsigned int i;		// volatile to prevent optimization

	while(1)
	{
		P1OUT ^= 0x01;				// toggle P1.0
		for(i=10000; i>0; i--);     // delay
	}
}
```
 %%