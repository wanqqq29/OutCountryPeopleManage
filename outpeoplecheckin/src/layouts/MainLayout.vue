<!--
 * @Author: wanqqq29
 * @Date: 2021-10-06 22:01:39
 * @LastEditTime: 2021-11-22 10:27:05
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
          出国人员信息管理系统
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