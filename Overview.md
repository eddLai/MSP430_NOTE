[CCS Note Content | CCS 教學系列目錄. 入門系列文章 | by Hsueh-Ju Wu 吳學儒 | TI Code Composer Studio | Medium](https://medium.com/ti-tms320f2837xd/ccs-note-content-ccs-%E6%95%99%E5%AD%B8%E7%B3%BB%E5%88%97%E7%9B%AE%E9%8C%84-590100673feb)
## 大綱
進度表格：https://docs.google.com/spreadsheets/d/1Q5lRjRBiwN_YJWAx8VdnXJqRml5ew77iE20tfGScxh0/edit?usp=sharing

- debug tree
- Class 1介紹：閃燈 (Embbed C+Arduino)
	- [[Class1：An Introduction of Embbeded systems]]
	- [[Class1 lec slide english-version]]
	- [[CCS]]
- Class 2加減：控制特定的寄存器，bitbang，自傳UART
- Class 3迴圈：七段顯示器 (Embbed C+Arduino)、UART Arduino應用+Array leetcode題目
- Class 4函式化：打出PWM
- Class 5函式化：UART (Embbed C+Ti API介紹)
- Class 6抽象化：使用API，DSP庫
- Class 7抽象化：做自己的API C wrapper for python API
- Class 8資料結構：leetcode
- Class 8物件導向：

- MSP430
	- 嵌入式系統、環境建置+Arduino C LED閃爍
	- Arduino C, 555Timer
	- Embbeded C, 555Timer
	- 通訊協定：RS232+UART，寫入USB
- Github
	- 專案管理，版本控制+多人協作
- AWS
	- 雲端運算、機器學習
	- C wrapper for python API

---

程式語言可以教
- MSP430
	- 嵌入式系統、環境建置+Arduino C LED閃爍
	- Arduino C, 555Timer
	- Embbeded C, 555Timer
	- 通訊協定：RS232+UART，寫入USB
- Github
	- 專案管理，版本控制+多人協作
- AWS
	- 雲端運算、機器學習
	- C wrapper for python API

---

1.
為什麼需要C，對於處在應用端的醫工產業，電腦中的程式C這些底層的東西都已經寫好了，資料處理用python，網頁前端用JavaScript
- [[Modules]]：腳位、功耗，直接設計
- 怎麼買
- 現場設定開發環境[[開發環境詳細介紹]]
- 七段顯示器

2.

 
3.
Embbeded C，手寫UART driver
- 燈泡、開關、馬達程式、引入第三方庫，學會看官方document

4.
- 各種專案
	- 使用模組(期中專題)
	- 軟韌體(期末專題)
	[ePanorama.net - Links](https://www.epanorama.net/links/serialbus.html)
		- UART：直接PC，putty
		- SPI：用LORA模組去測試
		- $I^2C$：用OLED顯示測試
		- PWM：用呼吸燈去做測試
- FPGA概念，，[超大型積體電路設計導論VLSI - 交大修課心得. 單純記錄一下自己的肝都用在哪裡 | by Mirkat | MIRKAT X BLOG | Medium](https://medium.com/mirkat-x-blog/%E8%B6%85%E5%A4%A7%E5%9E%8B%E7%A9%8D%E9%AB%94%E9%9B%BB%E8%B7%AF%E8%A8%AD%E8%A8%88%E5%B0%8E%E8%AB%96vlsi-%E4%BA%A4%E5%A4%A7%E4%BF%AE%E8%AA%B2%E5%BF%83%E5%BE%97-8f7349c5e903)需要的去修交大這堂，會Verilog

---
## Note
應該有分成最底層的寫法，跟比較高階使用各種庫的寫法
講多久的課?調整內容?
從程式語言的課下手應該這樣比較好入門
- [[Class1：An Introduction of Embbeded systems]]：下載環境、確認板子可用、使用現有UART Lib
- [[Class2 UART driver]]：玩玩UART轉TTL模組
- [[pinout]]
- [[Embbeded sys.]]

---
## 參考
- [【LaunchPad互動裝置】 - 數位輸入 + 加入按鈕 (google.com)](https://sites.google.com/site/msp430launchpaddiy/%E6%93%8D%E4%BD%9Claunchpad%E7%9A%84%E5%88%9D%E6%AD%A5/%E6%95%B8%E4%BD%8D%E8%BC%B8%E5%85%A5-%E5%8A%A0%E5%85%A5%E6%8C%89%E9%88%95)
- [MSP430G2 launchPad getting started tutorial (microcontrollerslab.com)](https://microcontrollerslab.com/msp430g2-launchpad-getting-started-tutorial/)
- [MSP430 主要應用及生態系統 | TI.com](https://www.ti.com/zh-tw/video/series/msp430-key-applications.html)
- [【第一部分.硬件结构】第一讲 概述_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV12V411z7g4/?p=1)
- [【MSP430教學-第一課】開發環境CCS以及第一支程式 – MSP430系列分享與教學 (wordpress.com)](https://msp430teaching.wordpress.com/2018/05/28/%e3%80%90msp430%e6%95%99%e5%ad%b8%e3%80%91%e9%96%8b%e7%99%bc%e7%92%b0%e5%a2%83ccs%e4%bb%a5%e5%8f%8a%e7%ac%ac%e4%b8%80%e6%94%af%e7%a8%8b%e5%bc%8f/)
- [（十）msp430：7段显示器与MSP-EXP430G2 TI Launchpad连接 – 趣讨教 (qutaojiao.com)](https://www.qutaojiao.com/18851.html)
- [[嵌入式 C 编程语言入门与深入.pdf (嵌入式 C 编程语言入门与深入.pdf) (Z-Library).pdf]]
- [[Embedded Systems – A Hardware-Software Co-Design Approach Unleash the Power of Arduino (Bashir I. Morshed) (Z-Library).pdf]]

---
From YY：
- https://msp430teaching.wordpress.com/category/msp430-%E6%95%99%E5%AD%B8/page/2/
- [【第一部分.硬件结构】第一讲 概述_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV12V411z7g4/?p=1&vd_source=d140198c00ff44556fe1cba20a0424c2)
- [MSP430 主要應用及生態系統 | TI.com](https://www.ti.com/zh-tw/video/series/msp430-key-applications.html)
- [MSP430G2 launchPad getting started tutorial (microcontrollerslab.com)](https://microcontrollerslab.com/msp430g2-launchpad-getting-started-tutorial/)
- [MSP430G2553 LaunchPad™ Development Kit (MSP-EXP430G2ET) User's Guide (Rev. A) (ti.com)](https://www.ti.com/lit/ug/slau772a/slau772a.pdf?ts=1615152602107)
- [【微控】含稅附發票、新版 MSP-EXP430G2ET LaunchPad、MSP430G2、MSP-EXP430G2 | 露天市集 | 全台最大的網路購物市集 (ruten.com.tw)](https://www.ruten.com.tw/item/show?21406221499189)
- [Lesson 9: UART – Simply Embedded](http://www.simplyembedded.org/tutorials/msp430-uart/)
- [MSP430 Fundamentals Workshop (ti.com)](https://software-dl.ti.com/ccs/esd/training/workshop/ccsv9/ccs_msp430_fundamentals_workshop.html#requirements)
- [（十）msp430：7段显示器与MSP-EXP430G2 TI Launchpad连接 – 趣讨教 (qutaojiao.com)](https://www.qutaojiao.com/18851.html)

---
Subject: Reminder: Bring Your Laptop for Next Tuesday’s Programming Class

Dear Students,

Next Tuesday, our Programming Language class will involve live coding. The class will be held at the Circuit Laboratory next to the General Physics Laboratory (located between the Biomedical Engineering Building 1F and the Experimental Building B1).

Please make sure to bring your laptop for the session. It is better to use a personal computer since using an computer you are not familiar with may significantly slow down the setup process Additionally, reviewing the slides in advance may help you complete the exercises before the class ends.

Best regards,
賴宏達
Teaching Assistant