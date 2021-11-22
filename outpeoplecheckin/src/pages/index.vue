<!--
 * @Author: wanqqq29
 * @Date: 2021-10-10 18:23:44
 * @LastEditTime: 2021-11-22 14:57:16
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \outpeoplecheckin\src\pages\index.vue
-->
<template>
  <div class="bg-blue text-white text-center q-pa-lg " style="height: 50rem;">
    <div v-if="flag">
      <div style="font-size: 10vh">
        出国人员登记系统导出
      </div>

      <div class="text-h2" style="opacity:.4;font-size: 5 vh">
        点击上方标签选择身份进行导出
      </div>
    </div>
    <div v-if="!flag" style="width:20%;margin:100px auto;">
      <login/>
    </div>
  </div>
</template>
<script>
import login from './login.vue'
import { useQuasar,Cookies  } from "quasar";
import { ref,onMounted } from "vue";
import { api } from "boot/axios";

export default {
   components: {
     login:login,
   },
  setup(){
    const flag = ref(false);


  onMounted(()=>{
        if (Cookies.has('ijc')){
            flag.value=true
        }
        else{
            flag.value=false
        }
    });
    return{
      flag
    }
  }
}
</script>

