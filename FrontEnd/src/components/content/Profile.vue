<template>
  <section class="profile-section" id="profile">
    <div class="profile-container">
      <div class="left-area">
         <!-- 简介 -->
        <div class="bg-area">
          <img src="~@/assets/img/bk.png" alt="" class="img-cur c-img-left" />
          <h3>作品简介</h3>
          <p>asd</p>
          <br />
          <a href="https://github.com/qbdl/TJ-Compiler-Full-Version" target="_blank" class="btn-a">
            <i class="fa fa-github"></i> Github链接
          </a>
        </div>
      </div>

      <div class="right-area">
        <div class="bg-area">
          <h3>具体作品</h3>
          <p>TJ Compiler以及操作界面</p>
          <div class="button-area">
            <button class="btn-action" @click="uploadFile">上传文件</button>
            <button class="btn-action" @click="compileCode">编译代码</button>
            <input type="file" @change="fileChanged" style="display:none;" ref="fileInput">
          </div>
          <textarea v-model="code" placeholder="输入你的代码"></textarea>
          <textarea readonly v-model="output" placeholder="编译结果"></textarea>
          <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
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
          this.output = response.data.output || response.data.error;
          this.errorMessage = '';
        })
        .catch(error => {
          this.errorMessage = '编译错误';
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

.left-area,
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
  background-color: rgb(253, 253, 253);
  margin: 0px 20px;
  box-shadow: 0px 56px 36px -60px #121d12;
}

.btn-a {
  text-decoration: none;
  background-color: #d3d3d3;
  padding: 10px 20px;
  display: inline-block;
  border-radius: 3px;
  color: white;
  margin: 10px auto 30px;
}

.btn-a:hover {
  background-color: rgb(0, 181, 229);
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
  margin: 10px auto;
}

.button-area {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 10px;
}

.btn-action {
  background-color: #d3d3d3;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin-left: 10px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-action:hover {
  background-color: #bbb;
}
</style>
