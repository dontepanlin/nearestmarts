<template>
  <v-layout row>
    <v-flex xs12 sm6>
      <v-list>
        <template v-for="item in items" @click="">
          <v-card color="cyan darken-2" class="white--text">
            <v-container fluid grid-list-lg>
              <v-layout row>
                <v-flex xs7>
                  <v-card-title primary-title>
                    <div class="headline">{{ item.name }}</div>
                  </v-card-title>
                  <v-card-title>
                    <div>{{ item.description }}</div>
                  </v-card-title>
                </v-flex>
                <v-flex xs5>
                  <v-card-text>
                    <div>{{ item.lat }}</div>
                    <div>{{ item.lon }}</div>
                  </v-card-text>
                  <v-card-actions>
                    <v-btn flat dark @click="show_place(item)">Показать на карте</v-btn>
                  </v-card-actions>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card>
          <v-divider></v-divider>
        </template>
      </v-list>
    </v-flex>
    <v-flex xs12 sm6>
      <vmap v-bind:place="items" v-bind:cntr="centr"></vmap>
    </v-flex>
  </v-layout>
</template>

<script>
  import api from '../api'
  import Map from './Map.vue'
  import auth from '../auth'

  const API_URL = 'http://localhost:8000/api/'
  const PLACES = API_URL + 'places/'

  export default {
    props: ['user'],
    components: {
      'vmap': Map
    },
    methods: {
      list: function () {
        var json = api.place_list(this)
        console.log(json)
        return JSON.parse(json)
      },
      show_place: function (item) {
        this.centr = {
          lat: item.lat,
          lng: item.lon
        }
      }
    },
    data: () => ({
      dialog: false,
      geo_coords: [],
      items: [],
      centr: {
        lat: auth.user.location.lat,
        lng: auth.user.location.lng
      }
    }),

    created () {
      this.axios.get(PLACES)
        .then(response => {
          // JSON responses are automatically parsed.
          this.items = response.data
        })
    },
    watch: {
      '$route' (to, from) {
        // Call resizePreserveCenter() on all maps
        this.$gmapDefaultResizeBus.$emit('resize')
      }
    }
  }
</script>
