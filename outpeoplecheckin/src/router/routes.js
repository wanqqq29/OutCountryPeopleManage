/*
 * @Author: wanqqq29
 * @Date: 2021-10-06 22:01:39
 * @LastEditTime: 2021-11-22 10:56:39
 * @LastEditors: wanqqq29
 * @Description: blog.wanqqq29.cn
 * @FilePath: \outpeoplecheckin\src\router\routes.js
 */

const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('src/pages/index.vue') },
      { path: '/Tinfo',meta:{requireAuth:true,}, component: () => import('src/pages/Tinfo.vue') },
      { path: '/Sinfo',meta:{requireAuth:true,}, component: () => import('src/pages/Sinfo.vue') }

    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
