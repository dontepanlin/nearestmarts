<template>
  <v-dialog v-model="dialog_log" width="600px">
    <v-btn color="primary" dark slot="activator">Open Dialog</v-btn>
    <v-card>
      <v-toolbar style="flex: 0 0 auto;" dark class="primary">
        <v-toolbar-title class="text-md-center">Вход</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon @click.native="dialog_log = false" dark>
          <v-icon>close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-spacer></v-spacer>
      <v-container grid-list-sm class="pa-4">
        <v-layout row wrap>
          <v-flex xs12 align-center justify-space-between>
            <v-form v-model="valid" ref="form">
              <v-text-field
                label="E-mail"
                v-model="email"
                :rules="emailRules"
                required
              ></v-text-field>
              <v-text-field
                label="Password"
                v-model="pass"
                min="8"
                hint="At least 8 characters"
                :rules="passlRules"
                :append-icon="e1 ? 'visibility' : 'visibility_off'"
                :append-icon-cb="() => (e1 = !e1)"
                :type="e1 ? 'password' : 'text'"
                required
              ></v-text-field>
            </v-form>
          </v-flex>
        </v-layout>
      </v-container>
      <v-card-actions>
        <v-btn color="blue darken-1" flat @click="method">Sign Up</v-btn>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" flat @click="submit">Log In</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
  import auth from '../auth'
  //  const API_URL = 'http://localhost:8000/api/'
  //  const LOGIN_URL = API_URL + 'users/login/'
  export default {
    name: 'login',
    props: ['method'],
    data () {
      return {
        dialog_log: false,
        e1: true,
        valid: true,
        tok: '',
        email: '',
        emailRules: [
          (v) => !!v || 'E-mail is required',
          (v) => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
        ],
        pass: '',
        passlRules: [
          (v) => !!v || 'Password is required',
          (v) => (v && v.length >= 8) || 'Password must be 8 characters min',
          (v) => /^(?=.*\d)(?=.*[a-z])[^\s]{8,}$/.test(v) || 'Pass must contain characters and digits'
        ]
      }
    },
    methods: {
      submit () {
        if (this.$refs.form.validate()) {
//           Native form submission is not yet supported
          console.log(this.email)
          console.log(this.pass)
          var credentials = {
            email: this.email,
            password: this.pass
          }

          auth.login(this, credentials)
//          this.axios.post(LOGIN_URL, {
//            email: this.email,
//            password: this.pass
//          }).then((response) => {
//            localStorage.setItem('token', response.data.token)
//            this.dialog = false
//          }).catch(error => {
//            console.log('Error login')
//            console.log(error)
//          })
        }
      }
    }
  }
</script>
