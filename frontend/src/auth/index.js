/**
 * Created by Владислав on 11.12.2017.
 */
// src/auth/index.js
// URL and endpoint constants
import axios from 'axios'
const API_URL = 'http://localhost:8000/api/'
const LOGIN_URL = API_URL + 'users/login/'
const REG_URL = API_URL + 'users/registration/'
const USER_URL = API_URL + 'users/user/'
const LOGOUT = API_URL + 'users/logout/'

export default {

  // User object will let us check authentication status
  user: {
    authenticated: false,
    location: {
      lat: 61.93,
      lng: 73.65
    },
    name: '',
    first_name: '',
    last_name: '',
    pk: 0
  },

  // Send a request to the login URL and save the returned JWT
  login (context, creds) {
    var ret = false
    context.axios.post(LOGIN_URL, {
      withCredentials: true,
      email: creds.email,
      password: creds.password
    }).then((response) => {
      this.user.authenticated = true
      console.log(response.data)
      console.log(response)
      localStorage.setItem('token', response.data.key)
      axios.defaults.headers.common['Authorization'] = this.getAuthHeader().Authorization
      context.dialog_log = false
      this.user_info(context)
      this.ret = true
    }).catch(error => {
      console.log('Error login')
      console.log(error)
    })
    return ret
  },

  user_info (context) {
    context.axios.get(USER_URL
    ).then((response) => {
      console.log(response.data)
      localStorage.setItem('user', response.data)
      this.user.pk = response.data.pk
      this.user.name = response.data.email
      this.user.first_name = response.data.first_name
      this.user.last_name = response.data.last_name
      console.log(this.user.name)
    }).catch(error => {
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        console.log(error.response.data)
        console.log(error.response.status)
        console.log(error.response.headers)
      } else if (error.request) {
        // The request was made but no response was received
        // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
        // http.ClientRequest in node.js
        console.log(error.request)
      } else {
        // Something happened in setting up the request that triggered an Error
        console.log('Error', error.message)
      }
      console.log(error.config)
    })
  },

  signup (context, creds) {
    context.axios.post(REG_URL, {
      withCredentials: true,
      email: creds.email,
      password1: creds.password1,
      password2: creds.password2,
      username: creds.username
    }).then((response) => {
      localStorage.setItem('token', response.data.key)
      axios.headers.common['Authorization'] = this.getAuthHeader().Authorization
      this.user.authenticated = true
      context.dialog_reg = false
      this.user_info(context)
      console.log(response.data)
    }).catch(error => {
      console.log('Reg error')
      console.log(error)
    })
  },

  // To log out, we just need to remove the token
  logout (context) {
    context.axios.post(LOGOUT, {
      withCredentials: true
    })
    localStorage.removeItem('token')
    this.user.authenticated = false
    delete axios.defaults.headers.common['Authorization']
  },

  checkAuth () {
    var jwt = localStorage.getItem('token')
    var us = localStorage.getItem('user')
    console.log(us)
    if (us) {
      this.user.name = us.email
      this.user.pk = us.pk
      this.user.first_name = us.first_name
      this.user.last_name = us.last_name
    }
    if (!jwt) {
      this.user.authenticated = false
    } else {
      this.user.authenticated = true
    }
  },

  // The object to be passed as a header for authenticated requests
  getAuthHeader () {
    return {
      'Authorization': 'Token ' + localStorage.getItem('token')
    }
  }
}
