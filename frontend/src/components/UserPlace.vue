<template>
  <v-container fluid grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex xs6>
        <v-card>
          <div class="headline">My marts</div>
          <v-list>
            <template v-for="place in places">
              <v-card>
                <v-card-title primary-title>
                  <div>{{ place.name }}</div>
                </v-card-title>
                <v-card-title>
                  <div>{{ place.description }}</div>
                </v-card-title>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn dark @click="">Редактировать</v-btn>
                  <v-btn dark @click="del_place(place.id)" color="red">Удалить</v-btn>
                  <v-spacer></v-spacer>
                  <v-btn dark @click="" :to="'/place/'+place.id">Просмотр</v-btn>
                </v-card-actions>
              </v-card>
              <v-divider></v-divider>
            </template>
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
                @click="add_place()"
              >
                <v-icon>add</v-icon>
              </v-btn>
            </v-fab-transition>
          </v-list>
        </v-card>
        <placedialog ref="placedialog" v-bind:show="dialog"></placedialog>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import auth from '../auth'
  import PlaceDialog from '@/components/PlaceDialog.vue'

  const API_URL = 'http://localhost:8000/api/'
  const PLACE = API_URL + 'places/'

  export default {
    components: {'placedialog': PlaceDialog},
    data () {
      return {
        hidden: false,
        places: [],
        dialog: false
      }
    },
    created () {
      this.get_place()
    },
    mounted () {
      this.$on('added', this.get_place)
    },
    watch: {
      '$route' (to, from) {
        // Call resizePreserveCenter() on all maps
      }
    },
    methods: {
      add_place: function () {
        this.$refs.placedialog.dialog = true
      },
      get_place: function () {
        auth.user_info(this)
        this.axios.get(API_URL + 'users/user/' + auth.user.pk + '/places')
          .then(response => {
            //  JSON responses are automatically parsed.
            this.places = response.data.results
          })
      },
      del_place: function (id) {
        this.axios.delete(PLACE + id)
        var self = this
        self.get_place()
      }
    }
  }
</script>
