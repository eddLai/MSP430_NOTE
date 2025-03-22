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
Class3.5：functionization and API, write your own library to control button module
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

[Arduino 4x4薄膜鍵盤模組實驗（一）：按鍵掃描程式原理說明 - 超圖解系列圖書](https://swf.com.tw/?p=917)\
引入一個我手寫的`.h`檔案\
寫一個計算機

---
[MSP430 Serial Monitor](https://www.youtube.com/watch?v=Fzf8q6fgxfQ)\
[[MSP430G2553 LaunchPad™ Development Kit.pdf]]

---
# Functionization
Why is C++ not python or JAVA?\
X-ray用python寫嗎(自由度太高，資料結構太亂)，用python寫你敢照嗎\
開發不能出錯的應用需要用嚴謹的語言\
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
C編譯器

---
1. 下載python[Welcome to Python.org](https://www.python.org/)，或者用colab[歡迎使用 Colaboratory - Colab](https://colab.research.google.com/)
2. 從官網中找到自己系統的下載版本[Simplified Wrapper and Interface Generator](https://www.swig.org/), [SWIG 安装教程 - OpenBox 文档](https://open-box.readthedocs.io/zh-cn/latest/installation/install_swig.html), 其中Mac可以用`brew install swig`
3. 解壓縮到系統儲存程式的位置(可能是C槽之類的) 
4. 設定為環境變數(什麼是環境變數，讓terminal可以呼叫這個程式)
5. `swig --version` 確認安裝完成
6. 確定C編譯器也被設定為環境變數
7. 打包C++ function，編譯並輸出
8. 參考.h檔案內容寫一個main.cpp以及python
9. 測試迭代速度差異
	1. windows用
		1. `Measure-Command {python my_script.p}` 
		2. `Measure-Command { .\my_program.exe }`
	2. Unix例如：macOS用`time`
		1. `time python3 my_script.py`
		2. `time ./my_program`

---
## swig命令
1. 使用terminal移動到檔案的所在位置
2. 確定存在`swig設定.i`, `函式定義.h`, `setup.py`
3. `swig -python -c++ speedup_performance.i`
4. `python setup.py build_ext --inplace`

---
## count in python
```
(base) PS D:\C code\python-c-mixing\python-call-c\swig> python main.py
Python result: 10000000200000000
(base) PS D:\C code\python-c-mixing\python-call-c\swig> Measure-Command {python .\main.py}


Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 13
Milliseconds      : 163
Ticks             : 131634775
TotalDays         : 0.000152355063657407
TotalHours        : 0.00365652152777778
TotalMinutes      : 0.219391291666667
TotalSeconds      : 13.1634775
TotalMilliseconds : 13163.4775
```

---
## count in C++
```
(base) PS D:\C code\python-c-mixing\python-call-c\swig> .\main.exe
Result: 10000000200000000
(base) PS D:\C code\python-c-mixing\python-call-c\swig> Measure-Command {.\main.exe}


Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 296
Ticks             : 2965770
TotalDays         : 3.43260416666667E-06
TotalHours        : 8.23825E-05
TotalMinutes      : 0.00494295
TotalSeconds      : 0.296577
TotalMilliseconds : 296.577
```

---
## Count in Swig
```
(base) PS D:\C code\python-c-mixing\python-call-c\swig> python swig_main.py
speedup_performance module loaded: <module 'speedup_performance' from 'D:\\C code\\python-c-mixing\\python-call-c\\swig\\speedup_performance.py'>
10
10000000200000000
(base) PS D:\C code\python-c-mixing\python-call-c\swig> Measure-Command {python .\swig_main.py}


Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 117
Ticks             : 1176634
TotalDays         : 1.36184490740741E-06
TotalHours        : 3.26842777777778E-05
TotalMinutes      : 0.00196105666666667
TotalSeconds      : 0.1176634
TotalMilliseconds : 117.6634
```

---
# Hint
完成全部步驟應該包含這些檔案
```
build
main.cpp
main.exe
main.py
setup.py
speedup_performance.h
speedup_performance.i
speedup_performance.py
speedup_performance_wrap.cxx
swig_main.py
_speedup_performance.cp311-win_amd64.pyd
```


---
# Tasks
- MSP430
	- 完成薄膜按鈕輸入輸出判定
- API
	- 下載SWIG
	- 把函式封裝成python API
	- 實測C++ vs python迴圈速度差異並記錄結果

---
# Homework
- 把swig工具所調用的檔案畫成block diagram
- 實測迴圈速度的差異
- 討論為什麼C++還比SWIG慢，是因為?(修改code，以及關閉.h調用試試看)
- 嘗試把`%include "stdint.i"`刪除並看看會發生什麼

(之後幾堂課會整合在一起)

---
# Ref.
- [pyliaorachel/python-c-mixing: Examples of mixing Python and C](https://github.com/pyliaorachel/python-c-mixing)
- [swig/python detected a memory leak of type 'int64_t *', no destructor found. · Issue #15 · aphysci/gravity](https://github.com/aphysci/gravity/issues/15)