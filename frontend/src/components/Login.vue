<template>
   <v-dialog v-model="dialog" width="600px">
     <v-btn color="primary" dark slot="activator">Open Dialog</v-btn>
      <v-card>
        <v-toolbar style="flex: 0 0 auto;" dark class="primary">
          <v-toolbar-title class="text-md-center">Вход</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn icon @click.native="dialog = false" dark>
            <v-icon>close</v-icon>
          </v-btn>
        </v-toolbar>
        <v-spacer></v-spacer>
        <v-container grid-list-sm class="pa-4">
          <v-layout row wrap>
            <v-flex xs12 align-center justify-space-between>
              <v-form v-model="valid" ref="form">
            <v-text-field
              label="Login"
              v-model="name"
              :rules="nameRules"
              :counter="50"
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
          <v-btn color="blue darken-1" flat @click.native="dialog = false">Sign Up</v-btn>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat @click.native="dialog = false">Log In</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
  export default {
    data: () => ({
      dialog: false,
      e1: false,
      valid: true,
      name: '',
      nameRules: [
        (v) => !!v || 'Login is required',
        (v) => (v && v.length <= 50) || 'Login must be less than 50 characters'
      ],
      pass: '',
      passlRules: [
        (v) => !!v || 'Password is required',
        (v) => (v && v.length >= 8) || 'Password must be 8 characters min',
        (v) => /^[\w\d]+$/.test(v) || 'Pass must contain characters and digits'
      ]
    }),
    methods: {
      submit () {
        if (this.$refs.form.validate()) {
//           Native form submission is not yet supported
          axios.post('/api/submit', {
            name: this.name,
            password: this.pass,
          }).then((response) => {
              response.data
          })
        }
      }
    }
  }
</script>
