import Vue from 'vue'
import Router from 'vue-router'
import Search from '@/components/Search'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Registration from '@/components/Registration'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/search',
      name: 'Search',
      component: Search,
      props: this.user
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/registration',
      name: 'Registration',
      component: Registration
    },
    {
      path: '/',
      name: 'Home',
      component: Home
    }
  ]
})
