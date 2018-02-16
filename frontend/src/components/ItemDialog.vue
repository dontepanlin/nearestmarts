<template>
  <v-dialog v-model="dialog" width="600px">
    <v-card>
      <v-toolbar style="flex: 0 0 auto;" dark class="primary">
        <v-toolbar-title class="text-md-center">Добавление товара</v-toolbar-title>
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
                label="Название"
                v-model="name"
                :rules="req"
                required
              ></v-text-field>
              <v-text-field
                label="Описание"
                v-model="description"
                counter
                max="120"
                full-width
                multi-line
              ></v-text-field>
              <v-select
              v-bind:items="cats"
              v-model="e7"
              label="Категория товара"
              single-line
              bottom
              item-text="name"
              item-value="id"
            ></v-select>
            </v-form>
          </v-flex>
        </v-layout>
      </v-container>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" flat @click="submit">Добавить</v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
  //  const API_URL = 'http://localhost:8000/api/'
  //  const LOGIN_URL = API_URL + 'users/login/'
  const API_URL = 'http://localhost:8000/api/'
  const ITEM = API_URL + 'items/'
  const CATS = API_URL + 'categories/'

  export default {
    name: 'placedialog',
    props: ['id'],
    data () {
      return {
        latLng: {},
        place: '',
        cats: [],
        e7: 0,
        dialog: false,
        e1: true,
        valid: true,
        tok: '',
        name: '',
        req: [
          (v) => !!v || 'Field is required'
        ],
        description: ''
      }
    },
    methods: {
      submit () {
        if (this.$refs.form.validate()) {
        //           Native form submission is not yet supported
          this.axios.post(ITEM, {
            withCredentials: true,
            category: this.e7,
            place: this.id,
            description: this.description,
            name: this.name
          }).then((response) => {
            console.log(response.data)
            this.dialog = false
            this.$parent.$emit('added', this.name)
          }).catch(error => {
            console.log('Error add')
            console.log(error)
          })
        }
      }
    },
    created () {
      this.axios.get(CATS)
        .then(response => {
          // JSON responses are automatically parsed.
          this.cats = response.data.results
          this.dialog = false
        })
    }
  }
</script>
