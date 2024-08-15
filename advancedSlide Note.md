eveal.js
透過CSS註釋來建立物件
==註釋要放在文字後面==

---

<!-- .slide: style="text-align: left" -->

Slide content 

---

<!-- .slide: style="text-align: left" -->

Slide Content

---

::: block
 
#### Header
_and_
Paragraph content
*in same block*
 
:::
 
---
 
no color
 
::: block <!-- element style="background-color: red;" -->
 
everything inside this block has red background color
 
::: block <!-- element style="background-color: blue;" -->
 
blue
 
:::
 
red
 
:::
 
no color

Fade in <!-- element class="fragment" -->
 
Fade out <!-- element class="fragment fade-out" -->
 
Highlight red <!-- element class="fragment highlight-red" -->
 
Fade in, then out <!-- element class="fragment fade-in-then-out" -->
 
Slide up while fading in <!-- element class="fragment fade-up" -->
 
---
 
- Permanent item
- Appear Fourth <!-- element class="fragment" data-fragment-index="4" -->
- Appear Third <!-- element class="fragment" data-fragment-index="3" -->
- Appear Second <!-- element class="fragment" data-fragment-index="2" -->
- Appear First <!-- element class="fragment" data-fragment-index="1" -->
<style>
	.with-border{
		border: 1px solid red;
	}
</style>
 
styled text <!-- element class="with-border" -->

---
css: [css/layout.css,css/customFonts.css]

---
<!-- slide bg="aquamarine" -->
## Slide with text based background
---
 
<!-- slide bg="#ff0000" -->
## Slide with hex based background
 
---
 
<!-- slide bg="rgb(70, 70, 255)" -->
## Slide with rgb based background
 
---
 
<!-- slide bg="hsla(315, 100%, 50%, 1)" -->
## Slide with hsl based background
 
---
 
# Slide without background
 
---
 
<!-- slide bg="https://picsum.photos/seed/picsum/800/600" -->
## Slide with image background
 
---
 
<!-- slide bg="[[image.jpg]]" -->
## Slide with image background #2
 
---
 
<!-- slide bg="https://picsum.photos/seed/picsum/800/600" data-background-opacity="0.5" -->
## with opacity
 
0.5 ≙ 50% opacity
 
---
 
## More options:
 
See [reveal backgrounds](https://revealjs.com/backgrounds/)

---

bg: red
bg: '#ff0000'
bg: rgb(70, 70, 255)
bg: transparent  <!--设置背景为透明样式-->

---

# Unordered list
 
- First
- Second
- Third
 
---
 
# Fragmented unordered list
 
+ Permanent
+ First
+ Second
+ Third
 
---
 
# Ordered list
 
1. First
2. Second
3. Third
 
---
 
# Fragmented ordered list
 
1. Permanent
2) Second
3) Third
4) Fourth
---
#### Excalidraw support
 
![[Sample.excalidraw|100]]
 
![[Sample.excalidraw]] <!-- element style="width:300px; height:400px" -->

---
 
<!-- .slide: bg="white"-->
 
![](fab fa-font-awesome fa-4x)
 
## Icons
 
---
 
<!-- .slide: bg="white"-->
### Basic Syntax
 
![](fas fa-envelope fa-4x)<!-- .element: color="coral"-->
 
Short Syntax
 
	![](fas fa-envelope fa-4x)<!-- .element: color="coral"-->

HTML Synthax
 
 	<i color="coral" class="fas fa-envelope fa-4x"/>
 
ShortCode Synthax
 
	:fas_envelope:
 
---
 
# Sizing
 
<i class="fas fa-camera fa-xs"></i>
<i class="fas fa-camera fa-sm"></i>
<i class="fas fa-camera fa-lg"></i>
<i class="fas fa-camera fa-2x"></i>
<i class="fas fa-camera fa-3x"></i>
<i class="fas fa-camera fa-5x"></i>
<i class="fas fa-camera fa-7x"></i>
 
---
 
# Rotating Icons
 
<i class="fas fa-snowboarding"></i>
<i class="fas fa-snowboarding fa-rotate-90"></i>
<i class="fas fa-snowboarding fa-rotate-180"></i>
<i class="fas fa-snowboarding fa-rotate-270"></i>
<i class="fas fa-snowboarding fa-flip-horizontal"></i>
<i class="fas fa-snowboarding fa-flip-vertical"></i>
<i class="fas fa-snowboarding fa-flip-both"></i>
  
---
  
  # Animating Icons
  
<i class="fas fa-spinner fa-spin fa-3x"></i>
<i class="fas fa-circle-notch fa-spin fa-3x"></i>
<i class="fas fa-sync fa-spin fa-3x"></i>
<i class="fas fa-cog fa-spin fa-3x"></i>
<i class="fas fa-spinner fa-pulse fa-3x"></i>
<i class="fas fa-stroopwafel fa-spin fa-3x"></i>
  
  
---
 
#### Bordered + Pulled Icons
 
<i class="fas fa-quote-left fa-2x fa-pull-left"></i>
 
Gatsby believed in the green light, the orgastic future that year by year recedes before us.
It eluded us then, but that’s no matter — tomorrow we will run faster, stretch our arms further...
And one fine morning — So we beat on, boats against the current, borne back ceaselessly into the past.<!-- .element: style="font-size: 24px" align="justify" -->

---

<br>
 <!-- .slide: style="text-align: left;" -->
<i class="fas fa-arrow-right fa-2x fa-pull-right fa-border"></i>
 
Gatsby believed in the green light, the orgastic future that year by year recedes before us.
It eluded us then, but that’s no matter — tomorrow we will run faster, stretch our arms further...
And one fine morning — So we beat on.<!-- .element: style="font-size: 46px" align="justify" -->

[Find the Perfect Icon for Your Project in Font Awesome 5 | Font Awesome](https://fontawesome.com/v5/search)

---
:smile: => 😄

---
```chart
    type: bar
    labels: [Monday,Tuesday,Wednesday,Thursday,Friday, Saturday, Sunday, "next Week", "next Month"]
    series:
      - title: Title 1
        data: [1,2,3,4,5,6,7,8,9]
      - title: Title 2
        data: [5,4,3,2,1,0,-1,-2,-3]
```
---
<canvas data-chart="line" >
<!--
{
 "data": {
  "labels": ["January"," February"," March"," April"," May"," June"," July"],
  "datasets":[
   {
    "data":[65,59,80,81,56,55,40],
    "label":"My first dataset","backgroundColor":"rgba(20,220,220,.8)"
   },
   {
    "data":[28,48,40,19,86,27,90],
    "label":"My second dataset","backgroundColor":"rgba(220,120,120,.8)"
   }
  ]
 }
}
-->
</canvas>

---
 <!-- .slide: data-auto-animate -->
# Title
 
---
<!-- .slide: data-auto-animate -->
 
# Title
##### **Subtitle**
###### *Author - 2022* 

[Auto-Animate | reveal.js (revealjs.com)](https://revealjs.com/auto-animate/)

---
<split even>
 
![](https://picsum.photos/id/1005/250/250) 
![](https://picsum.photos/id/1010/250/250) 
![](https://picsum.photos/id/1025/250/250) 
 
</split>

---

<split even gap="3">
 
**Lorem Ipsum** is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s
 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap
 
into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem
</split>

---
<split left="2" right="1" gap="2">
 
**Lorem Ipsum** is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s
when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap
	
into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem
</split>
---
<split wrap="4">
 
![](https://picsum.photos/id/1010/250/250) 
 
![](https://picsum.photos/id/1011/250/250) 
 
![](https://picsum.photos/id/1012/250/250) 
 
![](https://picsum.photos/id/1013/250/250) 
 
![](https://picsum.photos/id/1014/250/250) 
 
![](https://picsum.photos/id/1015/250/250) 
</split>

---
<split no-margin>
 
![](https://picsum.photos/id/1001/250/250) 
![](https://picsum.photos/id/1002/250/250) 
![](https://picsum.photos/id/1003/250/250) 
![](https://picsum.photos/id/1004/250/250) 
![](https://picsum.photos/id/1005/250/250) 
![](https://picsum.photos/id/1006/250/250) 
![](https://picsum.photos/id/1009/250/250) 
![](https://picsum.photos/id/1008/250/250) 
</split>

---
<grid drag="60 55" drop="5 10" bg="red">
60 x 55
</grid>
 
<grid drag="25 55" drop="-5 10" bg="green">
25 x 55
</grid>
 
<grid drag="90 20" drop="5 -10" bg="gray">
90  x 20
</grid>
---
<grid drag="40 30" drop="topleft" bg="red">
Top Left
</grid>
 
<grid drop="right" bg="green">
Right with default size
</grid>
 
<grid drag="80 30" drop="bottom" bg="coral">
Bottom
</grid>

---
<grid  drag="40 100" drop="center" bg="coral" flow="col">
Heading
![[Image.jpg]]
**Lorem Ipsum** is simply dummy text
</grid>
---
<grid  drag="100 40" drop="center" bg="coral" flow="row">
Left
![[Image.jpg]]
**Lorem Ipsum** is simply dummy text
</grid>
---

<grid  drag="55 50" drop="topleft" bg="orange">
### Make
</grid>
 
### Noise
<!-- element drag="55 50" drop="bottomright" bg="rgb(0,0,0)"-->
 
<grid  drag="25 20" drop="center" bg="green" rotate="-15">
### some
</grid>

---
<grid  drag="30 25" drop="left" border="thick dotted blue">
thick dotted blue
</grid>
 
<grid  drag="30 25" drop="center" border="4px solid white">
20px solid white
</grid>
 
thick dotted blue <!-- element drag="30 25" drop="right" border="medium dashed red"-->

---
<grid  drag="width height" drop="x y" animate="type speed">
## test

---

<grid  drag="50 50" drop="-12 -25" bg="white" filter="grayscale()">
![[Image.jpg]]
</grid>
 
Text is too blurry <!-- element drag="30 25" drop="5 15" bg="#B565A7" filter="blur(10px)" -->

---
<grid  drag="30 25" drop="12 15" bg="#B565A7" rotate="-10">
Hello
</grid>
 
World! <!-- element drag="40 25" drop="-12 -25" bg="#D65076" rotate="40" -->
---
<grid  drag="50 50" drop="topleft" bg="orange" pad="0 50px">
###### Lorem Ipsum wasnt simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book here there
</grid>
 
<grid  drag="50 50" drop="bottomright" bg="orange" pad="20px">
![[Image.jpg|800]]
</grid>

---
<grid drag="35 20" drop="topleft" align="left">
This text is aligned to the left side of the box
</grid>
 
<grid drag="35 20" drop="topright" align="right">
This text is aligned to the right side of the box
</grid>
 
<grid drag="36 20" drop="center" align="justify">
Stretches the text so that each line has equal width (like in newspapers and magazines)
</grid>
 
<grid drag="100 45" drop="top" flow="row" align="stretch">
![[Title-Wide.png]]
![[Title-Wide.png]]
![[Title-Wide.png]]
</grid>
 
<grid drag="100 55" drop="bottom" flow="col" align="stretch">
![[Title-Wide.png]]
![[Title-Wide.png]]
</grid>

---
<grid drag="30 100" drop="left" justify-content="center" bg="red">
Item 1
	
Item 2
	
Item 3
	
Item 4
</grid>
 
<grid drag="30 100" drop="center" justify-content="space-between" bg="green">
Item 1
 
Item 2
	
Item 3
	
Item 4
</grid>
 
<grid drag="30 100" drop="right" justify-content="space-around" bg="coral">
Item 1
	
Item 2
	
Item 3
	
Item 4
</grid>

---
<grid drag="100 10" drop="top" bg="white" align="left" pad="0 20px">
 <% title %>
</grid>
 
<grid drag="28 75" drop="69 15" bg="white" style="border-radius:15px"/>
 
<grid drag="64 70" drop="3 15" align="topleft">
 
<% left %>
 
</grid>
 
<grid drag="26 71" drop="70 17" align="topleft">
 
<% right %>
 
</grid>
 
<% content %>
 
<style>
.horizontal_dotted_line{
  border-bottom: 2px dotted gray;
} 
} 
</style>
 
<grid drag="94 0" drop="3 -6" class="horizontal_dotted_line">
</grid>
 
<grid drag="100 30" drop="0 64" align="bottomleft" pad="0 30px" >
<%? source %>
</grid>
 
<grid drag="100 6" drop="bottom">
###### © 2022 Advanced Slides<!-- element style="font-weight:300" -->
</grid>

---
---
theme: consult
height: 540
margin: 0
maxScale: 4
---
<!-- slide template="[[tpl-con-2-1-box]]" -->
 
::: title
### _**This is the Title of this Slide**_
:::
 
::: left
![[Image.jpg|1500]]
:::
 
<style>
.small-indent > ul { 
   padding-left: 1em;
}
</style>
 
::: right
**Header #1**
- Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
- tium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequa
- augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit a
- Nam quam nunc
Umsetzungsschritte
**Header #2**
- Curabitur
- condimentum
- Maecenas
**Header #3**
- justo
- rhoncus
- semper
 
:::<!-- element align="left" style="font-size: 13px;" class="small-indent" -->
 
::: source
###### Source: Copied from Lorem ipsum dolor Generator
:::

---