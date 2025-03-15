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
Class3.5：Button module and functionization, write your own library
<!-- element style="background-color: black; font-size: 60px;align: left; text-align: middle;color: white"-->
</grid>

<grid drag="50 10" drop="40 70">
TA: 賴宏達\
eddlai.be10@nycu.edu.tw
<!-- element style="background-color: black;font-size: 40px;align: right; text-align: right;color: white"-->
</grid>

<!-- slide bg="[[MSP430 HD pic.png]]" -->

---
# button module

[Arduino 4x4薄膜鍵盤模組實驗（一）：按鍵掃描程式原理說明 - 超圖解系列圖書](https://swf.com.tw/?p=917)
寫一個計算機

---
接線30分鐘
[MSP430 Serial Monitor](https://www.youtube.com/watch?v=Fzf8q6fgxfQ)
[[MSP430G2553 LaunchPad™ Development Kit.pdf]]

---
# Functionization
Why is C++ not python or JAVA?\
Uber Eats 或 Foodpanda送出訂單，這一個函式
```C++
food food_order(food_category, deliver_platform) {
	if (deliver_platform == "UberEats") {
		result = UberEats(food_category); // 呼叫 UberEats API
	} else if (deliver_platform == "Foodpanda") {
		result = Foodpanda(food_category); // 呼叫 Foodpanda API
	} else { //防呆
		result = "Unknown delivery platform";
	}
	return result
}
```
application program interface，API\
金融API，馬達控制API，高階語法`digitalWrite(gpio, LEVEL)`

---
API的背後，**後端**，可能是某種複雜的函式
```C++
food UberEats(string food_category) {
    vector<string> process_steps = {"製作食物", "包裝食物", "配送中"};

    for (string step : process_steps) {
        cout << "[UberEats] " << step << "中：" << food_category << endl;
    }
```

---
1. 下載python[Welcome to Python.org](https://www.python.org/)，或者用colab[歡迎使用 Colaboratory - Colab](https://colab.research.google.com/)
2. 從官網中找到自己系統的下載版本[Simplified Wrapper and Interface Generator](https://www.swig.org/), [SWIG 安装教程 - OpenBox 文档](https://open-box.readthedocs.io/zh-cn/latest/installation/install_swig.html)
3. 解壓縮到系統儲存程式的位置(可能是C槽之類的) 
4. 設定為環境變數(什麼是環境變數，讓terminal可以呼叫這個程式)
5. `swig --version` 確認安裝完成
6. 打包C++ function，編譯並輸出
7. 測試迭代速度差異
	1. windows用
		1. `Measure-Command {python my_script.p}` 
		2. `Measure-Command { .\my_program.exe }`
	2. Unix例如：macOS用`time`
		1. `time python3 my_script.py`
		2. `time ./my_program`

---
# Tasks
- MSP430
	- 完成薄膜按鈕輸入輸出判定
- API
	- 下載SWIG
	- 把函式封裝成python API
	- 實測C++ vs python迴圈速度差異

(之後幾堂課會整合在一起)