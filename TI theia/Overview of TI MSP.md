MSP430 vs MSPM0(較新)
使用Sysconfig系統可以有效的，建構該晶片specific的底層庫
- GPIO
- Timer: 本質上就是脈衝counter，所以要計算脈衝$f$轉$T$，
	- Bits+脈衝頻率的產生，決定最大最小值+精度，TIMAdvanced, TIMGeneral, TIMX\
![[Timer and Operation.png]]
- ADC, DAC配置