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

export default {

  // User object will let us check authentication status
  user: {
    authenticated: false
  },

  // Send a request to the login URL and save the returned JWT
  login (context, creds) {
    context.axios.post(LOGIN_URL, {
      email: creds.email,
      password: creds.password
    }).then((response) => {
      this.user.authenticated = true
      console.log(response.data)
      localStorage.setItem('token', response.data.key)
      axios.defaults.headers.common['Authorization'] = this.getAuthHeader()
      context.dialog_log = false
      this.user_info(context)
    }).catch(error => {
      console.log(creds.email)
      console.log(creds.password)
      console.log('Error login')
      console.log(error)
    })
  },

  user_info (context) {
    context.axios.get(USER_URL, {withCredentials: true}
    ).then((response) => {
      console.log(response.data)
      localStorage.setItem('user', response.data)
    }).catch(error => {
      console.log('Reg error')
      console.log(error)
    })
  },

  signup (context, creds) {
    context.axios.post(REG_URL, {
      email: creds.email,
      password1: creds.password1,
      password2: creds.password2,
      username: creds.username
    }).then((response) => {
      localStorage.setItem('token', response.data.key)
      axios.headers.common['Authorization'] = this.getAuthHeader()
      this.user.authenticated = true
      context.dialog_reg = false
      console.log(response.data)
    }).catch(error => {
      console.log('Reg error')
      console.log(error)
    })
  },

  // To log out, we just need to remove the token
  logout () {
    localStorage.removeItem('token')
    this.user.authenticated = false
    delete this.axios.defaults.headers.common['Authorization']
  },

  checkAuth () {
    var jwt = localStorage.getItem('token')
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
