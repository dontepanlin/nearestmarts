<template>
  <v-dialog v-model="dialog_reg" width="600px">
    <v-card>
      <v-toolbar style="flex: 0 0 auto;" dark class="primary">
        <v-toolbar-title class="text-md-center">Регистрация</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon @click.native="dialog_reg = false" dark>
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
                ref="email"
                :rules="[rules.required, rules.email]"
              ></v-text-field>
              <v-text-field
                label="Password"
                v-model="password"
                ref="password"
                min="8"
                hint="At least 8 characters"
                :rules="[rules.required, rules.pass]"
                :append-icon="e1 ? 'visibility' : 'visibility_off'"
                :append-icon-cb="() => (e1 = !e1)"
                :type="e1 ? 'password' : 'text'"
              ></v-text-field>
              <v-text-field
                label="Confirm"
                v-model="confirm"
                ref="confirm"
                :rules="[rules.required, rules.conf]"
                :append-icon="e2 ? 'visibility' : 'visibility_off'"
                :append-icon-cb="() => (e2 = !e2)"
                :type="e2 ? 'password' : 'text'"
              ></v-text-field>
            </v-form>
          </v-flex>
        </v-layout>
      </v-container>
      <v-card-actions>
        <v-btn color="blue darken-1" flat @click="method">Login</v-btn>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" flat @click="submit">Sign Up</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
  import auth from '../auth'
//  const API_URL = 'http://localhost:8000/api/'
//  const REG_URL = API_URL + 'users/registration/'
  export default {
    name: 'registration',
    props: ['method'],
    data () {
      return {
        dialog_reg: false,
        e1: true,
        e2: true,
        valid: false,
        tok: '',
        email: '',
        password: '',
        confirm: '',
        rules: {
          required: (value) => !!value || 'Required.',
          email: (value) => {
            const pattern = /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/
            return pattern.test(value) || 'Invalid e-mail.'
          },
          pass: (value) => {
            const pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[^\s]{8,}$/
            if (value.length < 8) {
              return (value && value.length >= 8) || 'Password must be 8 characters min'
            }
            return pattern.test(value) || 'pass must contain ch and nums.'
          },
          conf: (value) => {
              // eslint-disable-next-line
            console.log(this.password)
            return value === this.password || 'НЕе совпадают'
          }
        }
      }
    },
    methods: {
      submit () {
        if (this.$refs.form.validate()) {
//           Native form submission is not yet supported
          var credentials = {
            email: this.email,
            password1: this.password,
            password2: this.confirm,
            username: this.email
          }

          auth.signup(this, credentials)
//          this.axios.post(REG_URL, {
//            email: this.email,
//            password1: this.password,
//            password2: this.confirm,
//            username: this.email
//          }).then((response) => {
//            console.log(response.data)
//          })
        }
      }
    }
  }
</script>
