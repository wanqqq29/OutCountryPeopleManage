<!--
 * @Author: wanqqq29
 * @Date: 2021-10-06 22:01:39
 * @LastEditTime: 2021-10-10 18:21:33
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \outpeoplecheckin\src\layouts\MainLayout.vue
-->
<template>
  <q-layout view="hHh lpr lFr">

    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar>
          Title
        </q-toolbar-title>
      </q-toolbar>

      <q-tabs align="left">
        <q-route-tab to="/Tinfo" label="教师资料导出" />
        <q-route-tab to="/Sinfo" label="学生资料导出" />
      </q-tabs>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>