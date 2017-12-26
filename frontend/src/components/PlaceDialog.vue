<template>
  <v-dialog v-model="dialog" width="600px">
    <v-card>
      <v-toolbar style="flex: 0 0 auto;" dark class="primary">
        <v-toolbar-title class="text-md-center">Добавление</v-toolbar-title>
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
              <gmap-place-input
                @place_changed="setPlace"
                placeholder="Введите адрес"
                :default-place="place"
                className="input-group input-group--error input-group--required input-group--text-field">
              </gmap-place-input>
              <v-select
                label="Категории"
                v-bind:items="cats"
                v-model="e7"
                item-text="name"
                item-value="id"
                multiple
                chips
                hint="Категории товаров в магазине"
                persistent-hint
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
  import auth from '../auth'
  //  const API_URL = 'http://localhost:8000/api/'
  //  const LOGIN_URL = API_URL + 'users/login/'
  const API_URL = 'http://localhost:8000/api/'
  const PLACE = API_URL + 'places/'
  const CATS = API_URL + 'categories/'

  export default {
    name: 'placedialog',
    props: ['show'],
    data () {
      return {
        latLng: {},
        place: '',
        cats: [],
        e7: [],
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
          this.axios.post(PLACE, {
            withCredentials: true,
            user: auth.user.pk,
            name: this.name,
            description: this.description,
            lat: this.latLng.lat,
            lon: this.latLng.lng,
            cats_id: this.e7
          }).then((response) => {
            console.log(response.data)
            this.dialog = false
            this.$parent.$emit('added', this.name)
          }).catch(error => {
            console.log('Error add')
            console.log(error)
          })
        }
      },
      setPlace (place) {
        this.latLng = {
          lat: place.geometry.location.lat(),
          lng: place.geometry.location.lng()
        }
        console.log(this.latLng)
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
