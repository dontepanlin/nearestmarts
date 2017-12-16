<template>
  <v-layout row>
    <v-flex xs12 sm6 offset-sm3>
      <v-card>
        <v-list>
          <v-list-tile v-for="item in items" v-bind:key="item.name" @click="">
            <v-list-tile-content>
              <v-list-tile-title v-text="item.name"></v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
  import api from '../api'

  const API_URL = 'http://localhost:8000/api/'
  const PLACES = API_URL + 'places/'

  export default {
    methods: {
      list: function () {
        var json = api.place_list(this)
        console.log(json)
        return JSON.parse(json)
      }},
    data: () => ({
      dialog: false,
      items: {}
    }),

    created () {
      this.axios.get(PLACES)
        .then(response => {
      // JSON responses are automatically parsed.
          this.items = response.data
        })
    },

    props: {
      source: String
    }
  }
</script>
