<template>
  <v-container fluid grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex xs6>
        <v-card>
          <v-card-title primary-title>
            <div class="headline">{{ place.name }}</div>
          </v-card-title>
          <v-card-title>
            <div>{{ place.description }}</div>
          </v-card-title>
          <v-card-title>
            <v-chip v-for="cat in place.categories" :key="cat.name" text-color="white" color="secondary">
              {{ cat.name }}


            </v-chip>
          </v-card-title>
          <v-card-title>
            <div class="title">Список товаров:</div>
          </v-card-title>
          <v-list>
            <v-template v-for="item in items" :key="item.id">
              <v-card-text>
                <div class="subheading">{{ item.name }}</div>
              </v-card-text>
              <v-card-text>
                <div>{{ item.description }}</div>
              </v-card-text>
              <v-divider></v-divider>
            </v-template>
            <v-fab-transition>
              <v-btn
                color="pink"
                fab
                dark
                small
                absolute
                bottom
                left
                v-show="!hidden"
                @click="add_item()"
              >
                <v-icon>add</v-icon>
              </v-btn>
            </v-fab-transition>
          </v-list>
        </v-card>
      </v-flex>
      <itemdialog ref="itemdialog" v-bind:id="$route.params.id"></itemdialog>
    </v-layout>
  </v-container>
</template>

<script>
  import ItemDialog from '@/components/ItemDialog.vue'
  //  import auth from '../auth'
  const API_URL = 'http://localhost:8000/api/'
  const ITEM = API_URL + 'places/'
  export default {
    components: {'itemdialog': ItemDialog},
    data () {
      return {
        items: [],
        place: {},
        center: {lat: 10.0, lng: 10.0},
        markers: this.place
      }
    },
    created () {
      var url1 = ITEM + this.$route.params.id
      console.log(url1)
      this.axios.get(url1).then(response => {
        // JSON responses are automatically parsed.
        this.place = response.data
      })
      this.get_items()
    },
    methods: {
      get_items: function () {
        this.axios.get(ITEM + this.$route.params.id + '/items')
          .then(response => {
            //  JSON responses are automatically parsed.
            this.items = response.data.results
          })
      },
      add_item: function () {
        this.$refs.itemdialog.dialog = true
      }
    },
    mounted () {
      this.$on('added', this.get_items)
    }
  }
</script>
