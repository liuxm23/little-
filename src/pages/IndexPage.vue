<template>
  <q-page class="flex flex-center">
    <div>
      <q-btn :label="buttonLabel" @click="fetchRandomPerson" :loading="loading" />
      <q-dialog v-model="dialogVisible">
        <q-card>
          <q-card-section>
            <div v-if="loading">
              <p>加载中...</p>
            </div>
            <div v-else-if="person">
              <p>姓名: {{ person.name }}</p>
              <p>学号: {{ person.student_id }}</p>
              <p>班级: {{ person.class }}</p>
              <p>口头禅: {{ person.catchphrase }}</p>
            </div>
            <div v-else>
              <p>未能获取数据，请重试。</p>
            </div>
          </q-card-section>
          <q-card-actions align="right">
            <q-btn flat label="关闭" v-close-popup />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </div>
  </q-page>
</template>

<script>
import axios from 'axios';

export default {
  name: 'IndexPage',
  data() {
    return {
      buttonLabel: '脱单模拟器',
      loading: false,
      person: null,
      dialogVisible: false
    };
  },
  methods: {
    fetchRandomPerson() {
      this.loading = true;
      this.buttonLabel = '加载中...';
      this.dialogVisible = true; // 显示对话框
      setTimeout(() => {
        axios.get('http://127.0.0.1:8000/api/random-person/')
          .then(response => {
            console.log('成功获取数据:', response.data); // 调试信息
            this.person = response.data;
            this.loading = false;
            this.buttonLabel = '脱单模拟器';
          })
          .catch(error => {
            console.error('获取数据时出错:', error); // 调试信息
            this.loading = false;
            this.buttonLabel = '脱单模拟器';
          });
      }, 5000); // 模拟 5 秒延迟
    }
  }
}
</script>

<style>
/* 你可以在这里添加自定义样式 */
</style>