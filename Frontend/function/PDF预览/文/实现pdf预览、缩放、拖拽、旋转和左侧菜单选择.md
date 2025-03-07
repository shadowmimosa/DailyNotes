---
created: 2024-09-24T16:27:20 (UTC +08:00)
tags: [Vue]
source: https://www.cnblogs.com/wx980416/p/17374192.html
author: 
---

# vue-pdf-embed 实现pdf预览、缩放、拖拽、旋转和左侧菜单选择

---
## 实际效果

![Alt text](2002005-20230505150056133-1046184315.gif)

## 安装插件

```bash
pnpm install vue-pdf-embed
pnpm install vue3-pdfjs
```

## 左侧pdf菜单组件

```html
<template>
  <div class="pdf-view-list">
    <div class="item active-item" v-for="(item, index) in pageTotalNum" @click="itemClcik(index)">
      <div class="pdf-box">
        <vue-pdf-embed :source="testpdf1" class="vue-pdf-embed" :page="index + 1" />
      </div>
      <div class="page">{{ index + 1 }}</div>
      <div class="mask" :class="{ active: activePage === index + 1 }"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import VuePdfEmbed from 'vue-pdf-embed';
import { createLoadingTask } from 'vue3-pdfjs/esm'; // 获得总页数
import testpdf1 from '@/assets/zhjx-xrkg/testpdf1.pdf';

const props = defineProps<{
  activePage: number; // 当前页
}>();
const emits = defineEmits<{
  (event: 'update:activePage', index: number): void;
}>();
const pageTotalNum = ref(0); // 总页数

onMounted(() => {
  // 获得总页数
  createLoadingTask(testpdf1).promise.then((pdf) => {
    pageTotalNum.value = pdf.numPages;
  });
});

// 更新当前页
const itemClcik = (index: number) => {
  emits('update:activePage', index + 1);
};
</script>

<style scoped lang="scss">
.pdf-view-list {
  width: 183px;
  height: 100%;
  background-color: #333333;
  overflow-y: scroll;
  // 隐藏滚动条
  &::-webkit-scrollbar {
    display: none;
  }
  .item {
    width: 100%;
    height: 257px;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 20px 20px 0 20px;
    cursor: pointer;
    .pdf-box {
      width: 140px;
      height: 203px;
      background: #ffffff;
      border-radius: 4px;
      z-index: 1;
      .vue-pdf-embed {
        width: 100%;
        height: 100%;
      }
    }
    .page {
      font-weight: 600;
      font-size: 12px;
      color: #ffffff;
      line-height: 34px;
      z-index: 1;
    }
    .mask {
      width: 100%;
      height: 100%;
      background-color: transparent;
      position: absolute;
      left: 0;
      top: 0;
      z-index: 0;
    }
    .active {
      background-color: #ffaa46;
      opacity: 0.2;
    }
  }
}
</style
```

## 右侧预览组件

```html
<template>
  <div class="zhjxMain">
    <div class="content">
      <!-- 展示容器 -->
      <div class="left-box" :ref="refs.wrapper" @wheel.prevent="scaleWheel($event)">
        <div class="box" :ref="refs.box" @mousedown="dragstart($event)">
          <vue-pdf-embed :source="testpdf1" :style="scaleFun" class="vue-pdf-embed" :page="activePage" />
        </div>
        <div class="zoomin-wrapper">
          <img src="@/assets/XRKG/btn-enlarge.svg" @click="rollBtn('enlarge')" alt="" />
          <img src="@/assets/XRKG/btn-zoomin.svg" @click="rollBtn('zoomin')" alt="" />
          <img src="@/assets/zhjx-xrkg/btn-flip.svg" alt="" @click="rolate" />
        </div>
      </div>
      <div class="right-box">
        <div class="item" v-for="(value, key) in parseObj">
          <div class="label">{{ key }}</div>
          <div class="text">
            {{ value }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, reactive, watch } from 'vue';
import VuePdfEmbed from 'vue-pdf-embed';
import testpdf1 from '@/assets/zhjx-xrkg/testpdf1.pdf';

const props = defineProps<{
  activePage: number;
}>();

const parseObj = ref({
  设备名称: '1RPEOOIBA冷却剂疏水泵',
  功能位置: 'ND-4-01-RGL-010AR',
  缺陷原因: `取工作票，现场确认设备位号及安措正确
拆卸联轴器螺栓，对中复查同轴度 0.08mm平行度0.03mm不合格
拆卸泵盖螺栓，将泵憋体脱出运至检修场地，临时开口设备做好封堵拆卸叶轮及机械密封组件，解体轴承箱，消洗检查各零部件，测量泵轴最大0.0...大0.02mm，轴与轴承配合间隙最大0.01mm，轴与叶轮配合间隙0.02mm，体口环与叶回装新轴承及机械密封组件，安装泵叶轮，将泵整体运往现场回装，至工作油位，调整对中同轴度 0.03mm平行度 0.025mm，合格
回装联轴器及保护單，清理现场
归还工作票及辐射票完工，修后试验在工单01447934-02中执行`,
  处理措施: `1RPB002P0 解体检查工作完成`,
  处理结果: `取工作票，现场确认设备位号及安措正确
拆卸联轴器螺栓，对中复查同轴度 0.08mm平行度0.03mm不合格
拆卸泵盖螺栓，将泵憋体脱出运至检修场地，临时开口设备做好封堵拆卸叶轮及机械密封组件，解体轴承箱，消洗检查各零部件，测量泵轴最大0.0...大0.02mm，轴与轴承配合间隙最大0.01mm，轴与叶轮配合间隙0.02mm，体口环与叶回装新轴承及机械密封组件，安装泵叶轮，将泵整体运往现场回装，至工作油位，调整对中同轴度 0.03mm平行度 0.025mm，合格
回装联轴器及保护單，清理现场
归还工作票及辐射票完工，修后试验在工单01447934-02中执行`,
  其他字段1: `取工作票，现场确认设备位号及安措正确
拆卸联轴器螺栓，对中复查同轴度 0.08mm平行度0.03mm不合格
拆卸泵盖螺栓，将泵憋体脱出运至检修场地，临时开口设备做好封堵拆卸叶轮及机械密封组件，解体轴承箱，消洗检查各零部件，测量泵轴最大0.0...大0.02mm，轴与轴承配合间隙最大0.01mm，轴与叶轮配合间隙0.02mm，体口环与叶回装新轴承及机械密封组件，安装泵叶轮，将泵整体运往现场回装，至工作油位，调整对中同轴度 0.03mm平行度 0.025mm，合格
回装联轴器及保护單，清理现场
归还工作票及辐射票完工，修后试验在工单01447934-02中执行`,
  我是很长的字段名称: `取工作票，现场确认设备位号及安措正确
拆卸联轴器螺栓，对`,
  其他字段2: `取工作票，现场确认设备位号及安措正确
拆卸联轴器螺栓，对中复查同轴度 0.08mm平行度0.03mm不合格
拆卸泵盖螺栓，将泵憋体脱出运至检修场地，临时开口设备做好封堵拆卸叶轮及机械密封组件，解体轴承箱，消洗检查各零部件，测量泵轴最大0.0...大0.02mm，轴与轴承配合间隙最大0.01mm，轴与叶轮配合间隙0.02mm，体口环与叶回装新轴承及机械密封组件，安装泵叶轮，将泵整体运往现场回装，至工作油位，调整对中同轴度 0.03mm平行度 0.025mm，合格
回装联轴器及保护單，清理现场
归还工作票及辐射票完工，修后试验在工单01447934-02中执行`,
  其他字段3: `取工作票，现场确认设备位号及安措正确
拆卸联轴器螺栓，对中复查同轴度 0.08mm平行度0.03mm不合格
拆卸泵盖螺栓，将泵憋体脱出运至检修场地，临时开口设备做好封堵拆卸叶轮及机械密封组件，解体轴承箱，消洗检查各零部件，测量泵轴最大0.0...大0.02mm，轴与轴承配合间隙最大0.01mm，轴与叶轮配合间隙0.02mm，体口环与叶回装新轴承及机械密封组件，安装泵叶轮，将泵整体运往现场回装，至工作油位，调整对中同轴度 0.03mm平行度 0.025mm，合格
回装联轴器及保护單，清理现场
归还工作票及辐射票完工，修后试验在工单01447934-02中执行`,
});

// 实现pdf缩放
const scaleFun = computed(() => {
  return `transform:scale(${scaleData.scale});transition: all 0.3s;`;
});
const refs = {
  wrapper: ref<HTMLElement | null>(null), // pdf外层容器
  box: ref<HTMLElement | null>(null), // pdf容器，用于拖拽
};
const dragData = reactive({
  x: 0, // 拖拽初始化时的x坐标
  y: 0, // 拖拽初始化时的y坐标
  left: 0, // 拖拽结束时的x偏移量
  top: 0, // 拖拽结束时的y偏移量
  firstX: 0, // 初始x坐标
  firstY: 0, // 初始y坐标
});
const scaleData = reactive({
  scale: 1, // 缩放比例
  scaleNum: 0.1, // 滚轮缩放比例
  scaleMax: 100, // 最大缩放比例
  scaleMin: 0.1, // 最小缩放比例
  scaleBtn: 0.4, // 缩放按钮缩放比例
  rotate: 0, // 旋转角度
});

watch(
  () => props.activePage,
  (v) => {
    // 重置pdf大小和位置
    scaleData.scale = 1;
    scaleData.rotate = 0;
    refs.box.value.style.left = '50%';
    refs.box.value.style.top = '50%';
    boxTransform();
  },
);

// box 容器也要跟着变化
const boxTransform = () => {
  refs.box.value.style.transform = `translate(-50%, -50%) rotate(${scaleData.rotate}deg) scale(${scaleData.scale})`;
};

// 旋转
const rolate = () => {
  scaleData.rotate += 90;
  boxTransform();
};

// 鼠标滚轮缩放
function scaleWheel(e: any) {
  let dy = -e.deltaY || e.wheelDeltaY;
  if (dy < 0) {
    scaleData.scale -= scaleData.scaleNum;
  } else {
    // console.log('放大');
    scaleData.scale += scaleData.scaleNum;
  }
  // 边界判断
  if (scaleData.scale >= scaleData.scaleMax) {
    scaleData.scale = scaleData.scaleMax;
    return;
  }
  if (scaleData.scale <= scaleData.scaleMin) {
    scaleData.scale = scaleData.scaleMin;
    return;
  }
  boxTransform();
  return false;
}

// 点击放大缩小
const rollBtn = (action: 'enlarge' | 'zoomin') => {
  if (action === 'enlarge') {
    scaleData.scale += scaleData.scaleBtn;
  } else {
    scaleData.scale -= scaleData.scaleBtn;
  }
  // 边界判断
  if (scaleData.scale >= scaleData.scaleMax) {
    scaleData.scale = scaleData.scaleMax;
    return;
  }
  if (scaleData.scale <= scaleData.scaleMin) {
    scaleData.scale = scaleData.scaleMin;
    return;
  }
  boxTransform();
};

// 拖拽（box容器拖拽）
function dragstart(e: MouseEvent) {
  refs.box.value.style.transition = 'none';
  e.preventDefault(); // 阻止默认事件
  const box = refs.box.value as HTMLElement;
  const wrapper = refs.wrapper.value as HTMLElement;
  dragData.x = e.pageX - box.offsetLeft;
  dragData.y = e.pageY - box.offsetTop;

  // 添加鼠标移动事件
  document.addEventListener('mousemove', move);
  function move(event: any) {
    // 计算元素的位置
    dragData.left = event.pageX - dragData.x;
    dragData.top = event.pageY - dragData.y;
    // 边界判断可以在这里添加 ↓

    // 设置元素的位置
    box.style.left = dragData.left + 'px';
    box.style.top = dragData.top + 'px';
  }
  // 添加鼠标抬起事件，鼠标抬起，将事件移除
  document.addEventListener('mouseup', function () {
    document.removeEventListener('mousemove', move);
  });
  // 鼠标离开父级元素，把事件移除
  document.addEventListener('mouseout', function () {
    document.removeEventListener('mousemove', move);
  });
}
</script>

<style scoped lang="scss">
.zhjxMain {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  background-color: #000000;
  overflow: hidden;
  .content {
    width: 100%;
    height: 100%;
    margin: 0 auto;
    background-color: #000000;
    display: flex;
    overflow: hidden;

    .left-box {
      width: 50%;
      height: 100%;
      background-color: #262626;
      margin-right: 10px;
      position: relative;
      overflow: hidden;
      .box {
        width: 80%;
        height: 100%;
        object-fit: contain;
        user-select: none; /* 不可选中,为了拖拽时不让文字高亮 */
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: flex;
        align-items: center;
        justify-content: center;
        .vue-pdf-embed {
          width: 100%;
        }
      }
      .zoomin-wrapper {
        position: absolute;
        top: 50%;
        right: 20px;
        transform: translateY(-50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        img {
          width: 34px;
          height: 34px;
          cursor: pointer;
          margin: 5px 0;
        }
      }
      .center {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
      }
      .bottom-left {
        position: absolute;
        bottom: 20px;
        left: 20px;
      }
    }
    .right-box {
      width: 50%;
      height: 100%;
      background-color: #000000;
      margin-left: 10px;
      padding: 10px 0;
      overflow-y: scroll;
      //   修改滚动条
      &::-webkit-scrollbar {
        width: 10px;
      }
      &::-webkit-scrollbar-thumb {
        background: #333333;
        border-radius: 10px;
      }
      .item {
        min-height: 48px;
        display: flex;
        padding-right: 50px;
        & + .item {
          margin-top: 10px;
        }
        .label {
          width: 100px;
          min-height: 48px;
          display: flex;
          align-items: center;
          justify-content: center;
          color: #ffffff;
          font-size: 14px;
          font-weight: 600;
          padding: 0 5px;
        }
        .text {
          flex: 1;
          color: #ffffff;
          background-color: #262626;
          border-radius: 10px;
          font-size: 14px;
          font-weight: 600;
          line-height: 24px;
          padding: 10px 20px;
        }
      }
    }
  }
}
</style>
```

## 具体请参考链接

[Vue3 实现 PDF 文件在线预览功能](https://juejin.cn/post/7105933034771185701 "Vue3 实现 PDF 文件在线预览功能")
