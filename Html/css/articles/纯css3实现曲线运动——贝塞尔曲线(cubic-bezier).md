---
title: 纯css3实现曲线运动——贝塞尔曲线(cubic-bezier)
date: 2022-07-05 14:41:02
copyright: false
author: 会会会会
home: https://www.jianshu.com/u/1b4fb0ed8acb
origin: jianshu
url: https://www.jianshu.com/p/fced4640d77c
tag: 
categories: 
description: 目标——就是纯css实现下面的曲线运动      image.png  这里是我最后实现的效果动画：...
---

#### 目标——就是纯css实现下面的曲线运动

![](./纯css3实现曲线运动——贝塞尔曲线(cubic-bezier)/37697cb5cef8f2fc484cfc26154b8e89)

image.png

#### 这里是我最后实现的效果动画：[在线视频实现效果](https://www.iesdouyin.com/share/video/6620215382764424455/?region=CN&mid=6620215394722401027&u_code=i6g6edgf&titleType=title&timestamp=1541389026&utm_campaign=client_share&app=aweme&utm_medium=ios&tt_from=copy&utm_source=copy&iid=48122756630)

直接看所有的代码；

##### html代码

```
  <div class="ball run_top_right"></div>
```

##### css代码

```
html{
 background: #ad4e24;
}
//定义球的初始值，位置是绝对定位；
.ball{
  height: 100px;
  width: 100px;
  border-radius: 50%;
  position: absolute;
  bottom: 40px;
  z-index: 10;
  left: 40px;
  background: greenyellow;
}

//定义动画的流程
.run_top_right {
  display: block;
  animation: run-right-right 3s 0.4s 1 linear, run-right-top 3s 0.4s 1 cubic-bezier(.66,.1,1,.41);
  // animation: run-right-right 3s 0.4s 1 linear, run-right-top 3s 0.4s 1 ease-out;
  animation-fill-mode: forwards;
}

//向上走的动画初始及结尾值
@keyframes run-right-top {
  0% {
    bottom: 40px;
  }

  100% {
    bottom: 800px;
  }
}
//向上右的动画初始及结尾值
@keyframes run-right-right {
  0% {
    left: 40px;
    transform: scale(0.7);
  }

  100% {
    left: 600px;
    transform: scale(0.45);
  }
}
```

---

这里简单解释下：

##### 第一、分解运动

上图的曲线运动进行分解  
向右：匀速运动；  
向上：加速运动；（因为向上的线越来越陡，意味着速度越来越快，所以在做加速运动）

##### 第二、实现代码解释

有了对该运动的本质认识，那么实现起来就很易如反掌了；

```css
@keyframes run-right-right {
  0% {
    left: 40px;
    transform: scale(0.7);
  }

  100% {
    left: 600px;
    transform: scale(0.45);
  }
}

```

——@keyframes 是css3的一个规则，用来定义一个运动的每个桢的位置，大小颜色等；

然后run-right-right就是这个动画特性的名字，很好理解；然后0%就是开始的时候的left值；transform: scale(0.7);变小0.7；时间到100%时 left值变大到600px的位置，然后变小到0.45；（*这里的位置，大小都是相对于初始设置的ball类里面的值*）

```css
animation: run-right-right 3s 0.4s 1 linear, run-right-top 3s 0.4s 1 cubic-bezier(.66,.1,1,.41);
```

——这段代码的意思是动画animation用run-right-right动画和 run-right-top动画，注意我们是同时引用的两个动画；  
就是@keyframes 所定义的，然后我们又设置了一些参数，逐一解释：

* 一.第一个参数就是引用的动画名字；
* 二，动画持续时间3s；
* 三、0.4s是延迟时间为0.4s，以run\_top\_right加到ball上面的时间为准，延后0.4s;
* 四、1是动画的执行次数是1次；
* 五、cubic-bezier(.66,.1,1,.41) 就是重要的**贝塞尔曲线(cubic-bezier)**；

实际上是设置animation-timing-function的属性；就是设置运动速度的特性属性；

* 1. linear，就是线性运动，也就是匀速运动；
* 2 ease，默认。动画以低速开始，然后加快，在结束前变慢。
* 3.ease-in，ease-out,ease-in-out,就很好记，ease就是慢的意思，ease-in就是慢速开始，就是做加速运动，ease-out就是减速运动，ease-in-out就是先加速后减速；当然我们也可以设置成cubic-bezier()值；

[贝塞尔曲线在线取值](http://cubic-bezier.com/)

打开网站就看到如下的界面；你可以自己调解运动曲线；我自己选了个向上做加速的曲线；然后复制cubic-bezier()值就是可以了。

![](./纯css3实现曲线运动——贝塞尔曲线(cubic-bezier)/7c4949c23e084a8fa50128989a4d15ff)

image.png

因为这里我只需要向上的运动做变速运动所以run-right-right 我设置的是linear，匀速运动，然后 run-right-top设置的是cubic-bezier(.66,.1,1,.41)，这样的加速运动，这样得到的运动路径就是一条曲线！！曲线的轨迹又run-right-top的cubic-bezier值决定！

```
  animation-fill-mode: forwards;
```

animation-fill-mode设置动画完成后的状态；  
forwards：当动画完成后，保持最后一个属性值（在最后一个关键帧中定义）。简单说就是定格在最后100%的样子；  
backwards：在 animation-delay 所指定的一段时间内，在动画显示之前，应用开始属性值（在第一个关键帧中定义）。就是定格在0%时候的样子

---

## 完成

> 当前文档由 [markdown文档下载插件](https://github.com/kscript/markdown-download) 下载, 原文链接: [纯css3实现曲线运动——贝塞尔曲线(cubic-bezier)](https://www.jianshu.com/p/fced4640d77c)  