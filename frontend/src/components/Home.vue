<template>
  <v-layout row>
    <v-flex xs12 sm6 offset-sm3>
      <v-card>
        <v-list>
          <v-list-tile v-for="item in get_list()" v-bind:key="item.name" @click="">
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

  export default {
    data: () => ({
      dialog: false,
      items: {}
    }),

    props: {
      source: String
    }
  }
</script>
