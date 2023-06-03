<template>
  <section class="profile-section" id="profile">
    <div class="profile-container">
      <div class="left-area">
         <!-- 简介 -->
        <div class="bg-area">
          <!-- <img src="~@/assets/img/bk.png" alt="" class="img-cur" /> -->
          <h3>作品简介</h3>
          <p>同济大学2023编译原理课程项目(完整前后端)<br />
            Author : lkj
          </p>
          <br />
          <a href="https://github.com/qbdl/TJ-Compiler-Full-Version" target="_blank" class="btn-a">
            <i class="fa fa-github"></i> Github链接
          </a>
        </div>
      </div>

      <div class="right-area">
        <div class="bg-area">
          <h2>TJ Compiler</h2>
          <div class="button-area">
            <button class="btn-action" @click="uploadFile">上传文件</button>
            <button class="btn-action" @click="compileCode">编译代码</button>
            <button class="btn-action" @click="targetCode">目标代码查看</button>
            <input type="file" @change="fileChanged" style="display:none;" ref="fileInput">
          </div>
          <textarea v-model="code" placeholder="输入你的代码"></textarea>
          <textarea readonly v-model="output" placeholder="编译结果"></textarea>
          <!-- <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p> -->
          <div class="spacer"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      code: '',
      output: '',
      file: null,
      errorMessage: ''
    };
  },
  methods: {
    compileCode() {
      axios.post('http://localhost:5000/compile', {
        code: this.code
      })
        .then(response => {
          if (response.data.error) {
            this.output = response.data.error;
            this.errorMessage = response.data.error;
          } else if (response.data.output) {
            this.output = response.data.output;
            this.errorMessage = '';
          }
        })
        .catch(error => {
          if (error.response && error.response.data.error) {
            this.output = error.response.data.error;
            this.errorMessage = error.response.data.error;
          } else {
            this.output = '请求错误';
            this.errorMessage = '请求错误';
          }
          console.log(error);
        });
    },
    targetCode() {
      axios.get('http://localhost:5000/getTargetCode') // send request to the new backend endpoint
        .then(response => {
          if (response.data.error) {
            this.output = response.data.error;
            this.errorMessage = response.data.error;
          } else if (response.data.output) {
            this.output = response.data.output;
          }
        })
        .catch(error => {
          this.output = '请求错误';
          this.errorMessage = '请求错误';
          console.log(error);
        });
    },
    uploadFile() {
      this.$refs.fileInput.click();
    },
    fileChanged(event) {
      this.file = event.target.files[0];
      const reader = new FileReader();
      reader.onload = e => {
        this.code = e.target.result;
      };
      reader.onerror = e => {
        this.errorMessage = '文件读取错误';
      };
      reader.readAsText(this.file);
    }
  }
};
</script>

<style scoped>
.profile-section {
  padding: 50px 15px 50px;
  margin: 20px auto;
}

.profile-container {
  width: 1170px;
  padding-left: 15px;
  padding-right: 15px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 120px;
}

.left-area{
  display: inline-block;
  position: relative;
}
.right-area {
  display: inline-block;
  text-align: center;
  width: 50%;
  position: relative;
  /* margin: 0px 20px; */
}

.img-cur {
  border-radius: 50%;
  width: 350px;
  height: 350px;
  margin-top: -120px;
  border: 10px solid rgb(215, 215, 215);
}

.img-cur:hover {
  border: 10px solid rgb(140, 140, 140);
}

.left-area p,
.right-area p {
  width: 90%;
  line-height: 25px;
  font-size: 15px;
  font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
  padding: 0px 20px;
  margin: 0px 10px !important;
}

.bg-area {
  background-color: rgb(253, 253, 253,0.6);
  margin: 0px 20px;
  box-shadow: 0px 56px 36px -60px #121d12;
}

.btn-a {
  text-decoration: none;
  background-color: #d3d3d3;
  padding: 10px 20px;
  display: inline-block;
  border-radius: 40px;
  color: white;
  margin: 10px auto 30px;
}

.btn-a:hover {
  background-color: #bef5ec;
}

.fa {
  color: #777;
  font-size: 20px;
  margin: 5px 0px;
  padding: 5px;
}

.fa:hover {
  color: rgb(230, 22, 45);
  border-radius: 50%;
  /* border: 1px solid rgb(217,0,19); */
  padding: 5px;
}

textarea {
  display: block;
  margin: 10px auto;
  width: 80%;
  height: 200px;
}

button {
  display: block;
}

.button-area {
  display: flex;
  justify-content: space-around;
  margin-bottom: 10px;
  margin-top: 20px;
}

.btn-action {
  background-color: #bbb;
    color: #fff;
  border: none;
  padding: 10px 20px;
  margin-left: 10px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-action:hover {
  background-color: #bef5ec;
}

.spacer {
  height: 30px; /* 根据需要添加更多或更少的空白 */
}
</style>
