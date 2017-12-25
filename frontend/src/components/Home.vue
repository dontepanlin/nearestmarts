<template>
  <v-container>
    <v-layout row wrap>
      <v-carousel style="width: 100%; height: 300px; background-clip: content-box; background-size: contain;" hide-delimiters>
        <v-carousel-item v-for="(item,i) in piars" v-bind:src="item.poster" :key="i"></v-carousel-item>
      </v-carousel>
    </v-layout>
  </v-container>
</template>

<script>
  const API_URL = 'http://localhost:8000/api/'
  const PIARS = API_URL + 'piars/'
  export default {
    created () {
      this.axios.get(PIARS)
        .then(response => {
          // JSON responses are automatically parsed.
          this.piars = response.data
        })
    },
    data () {
      return {
        piars: []
      }
    }
  }
</script>
