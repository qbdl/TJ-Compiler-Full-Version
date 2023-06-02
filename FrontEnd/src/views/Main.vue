<template>
  <div id="div-main-wrap">
    <!-- header -->
    <div class="h-title">
      <div class="div-title">
        <a href="#">
          <h1>TJ Compiler</h1>
        </a>
        <div class="music-control" @click="musicCtrol">
          <!-- 音乐开启时的图片和文本 -->
          <template v-if="musicState">
                <span>停止音乐~ &nbsp; </span>
                <img src="~@/assets/img/musicon.png" alt="" />
            </template>

            <!-- 音乐关闭时的图片和文本 -->
            <template v-else>
                <span>听听音乐~ &nbsp; </span>
                <img src="~@/assets/img/musicoff.png" alt="" />
            </template>
        </div>
        <audio ref="audio" controls autoplay="autoplay" hidden>
          <source src="../../public/music/always_with_me.mp3" type="audio/mpeg" />
        </audio>
        <!-- <iframe
          ref="audio"
          allow="autoplay"
          style="display: none"
          src="../../public/music/always_with_me.mp3"
        ></iframe> -->
      </div>
      <ul class="navv">
        <li><a href="#">主页</a></li>
        <li><a href="#time">时间</a></li>
      </ul>
    </div>
    <!-- 主体 -->
    <div class="main-area">
      <!-- 简介 -->
      <profile></profile>
      <!-- 计时器 -->
      <section class="timer" id="time">
        <div class="timer-wrap">
          <div class="time-header">
            <h2>当前时间</h2>
            <hr class="line" />
            <span class="intro">Current&nbsp;Time</span>
          </div>
          <div class="time-area">
            <div>{{ hour }}</div>
            <div>{{ minute }}</div>
            <div>{{ second }}</div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import Profile from "@/components/content/Profile.vue";

export default {
  setup() {
    const audio = ref(null);
    const musicState = ref(false);
    // const clickA = () => {
    //   audio.value.play();
    // };
    const musicCtrol = () => {
      if (!musicState.value) {
        audio.value.play();
        musicState.value = true;
      } else {
        audio.value.pause();
        musicState.value = false;
      }
    };
    // onMounted(() => {
    //   // 监听全局点击事件
    //   window.addEventListener("click", clickA);
    //   // audio.value.play();
    //   console.log(audio.value);
    // });
    // 时间
    const hour = ref(0);
    const minute = ref(0);
    const second = ref(0);
    onMounted(() => {
      setInterval(() => {
        let date = new Date();
        hour.value = date.getHours();
        minute.value = date.getMinutes();
        second.value = date.getSeconds();
      }, 1000);
    });
    return {
      audio,
      musicState,
      hour,
      minute,
      second,

      musicCtrol,
    };
  },
  components: {
    Profile,
  },
};
</script>

<style >
/* 去掉了scoped 其样式可以被其子组件使用 */
h2 {
  font-weight: 600;
  color: #333;
  letter-spacing: 1px;
  font-family: "Ek Mukta";
  font-size: 36px;
  margin: 0;
}
a {
  text-decoration: none;
}
ul {
  /* 去除默认样式 */
  padding: 0;
  /*去除项目符号 (小点)*/
  list-style: none;
}
#div-main-wrap {
  width: 100%;
  padding-top: 450px; /* 上方位置调整 */
  background-image: url("~@/assets/img/whole_bk.png");
  background-size: cover;
  background-position: center;
}

.h-title {
  position: sticky;
  top: 0px;
  z-index: 9999;
  /* background-color: white; */
  background-color:rgba(247, 247, 247, 0.8);
  /* border-bottom: 1px #777 solid; */
  box-shadow: 0 1px 7px rgb(0 0 0 / 10%);
}
.music-control {
  position: absolute;
  top: 30px;
  right: 40px;
}
.music-control img {
  height: 30px;
  width: 30px;
  opacity: 0.8;
}
.div-title h1 {
  color: #777;
  text-align: center;
  margin: 0px 0px 15px 0px;
  padding-top: 15px;
}
.navv {
  margin: 15px auto 8px;
  display: flex;
  justify-content: center;
  width: 900px;
  padding: 10px 0px;
  border-top: 1px #ddd solid;
}
.navv a {
  font-size: 18px;
  padding: 0px 20px;
  font-weight: bold;
  color: #777;
}
.main-area {
  width: 100vw;
  /* background-color: rgb(247, 247, 247); */
  background-color: rgba(247, 247, 247, 0.8);  /* 添加透明度 */
}
/* time */
.time-area {
  padding: 10px 200px;
  width: 610px;
  display: flex;
  justify-content: space-between;
  margin: 0px auto;
}
.time-area div {
  height: 100px;
  width: 200px;
  background-color: rgba(51, 51, 51, 0.8);  /* 添加透明度 */
  color: white;
  font-size: 33px;
  line-height: 100px;
  opacity: 0.8;/*添加这一行，取值在0-1之间，值越小透明度越高*/
}
</style>
