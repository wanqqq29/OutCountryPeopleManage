<!--
 * @Author: wanqqq29
 * @Date: 2021-11-22 10:25:12
 * @LastEditTime: 2021-11-22 15:48:17
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \outpeoplecheckin\src\pages\login.vue
-->
<template>
  <q-form @submit="onSubmit" class="q-gutter-md" style="color: white">
    <q-input
      rounded
      outlined
      v-model="username"
      label="用户名"
      lazy-rules
      :rules="[(val) => (val && val.length > 0) || '请输入用户名']"
    />

    <q-input
      rounded
      outlined
      type="password"
      v-model="pas"
      label="密码"
      lazy-rules
      :rules="[(val) => (val !== null && val !== '') || '请输入密码']"
    />
    <div>
      <q-btn label="登录" type="submit" color="primary" />
    </div>
  </q-form>
</template>

<script>
import { useQuasar, Cookies } from "quasar";
import { ref, onMounted } from "vue";
import { api } from "boot/axios";

export default {
  name: "login",
  setup() {
    const $q = useQuasar();

    const username = ref(null);
    const pas = ref(null);

    onMounted(() => {
      if (Cookies.has("ijc")) {
        flag: false;
      } else {
        flag: true;
      }
    });
    return {
      username,
      pas,

      onSubmit() {
        api.get("/CsR").then((response) => {
          var csrtoken = response.data;
          api
            .post(
              "/login/",
              { tk: csrtoken.jsdlak,username: username.value,pas: pas.value },
              { headers: { "X-CSRFToken": csrtoken.csrf_token } }
            )
            .then((response) => {
              console.log(response);
              if (response.data == 1) {
                Cookies.set("ijc", "yybbwy", { expires: "30m" });
                window.location="/";
              } else if (response.data == "x") {
                Cookies.remove("ijc");
              }
            })
            .catch((error) => {
              console.log(error);
            });
        });
      },
    };
  },
};
</script>
