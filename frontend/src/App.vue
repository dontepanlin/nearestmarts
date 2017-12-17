<template>
  <v-app id="inspire">
    <v-navigation-drawer
      fixed
      clipped
      app
      v-model="drawer"
      class="blue accent-1"
    >
      <v-list>
        <v-subheader v-text="items.header"></v-subheader>
        <template v-for="cat in categories">
            <v-list-tile @click="">
              <v-list-tile-content>
                <v-list-tile-title>{{ cat.name }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-divider></v-divider>
          </template>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar
      color="blue darken-3"
      dark
      app
      clipped-left
      fixed
    >
      <v-toolbar-title :style="$vuetify.breakpoint.smAndUp ? 'width: 300px; min-width: 250px' : 'min-width: 72px'"
                       class="ml-0 pl-3">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <v-btn flat to="/"><span class="hidden-xs-only">Nearest Mart</span></v-btn>
      </v-toolbar-title>
      <v-text-field
        light
        solo
        v-model="query"
        prepend-icon="search"
        placeholder="Search"
        @keyup.enter="search"
        style="max-width: 500px; min-width: 128px"
      ></v-text-field>
      <div class="d-flex align-center" style="margin-left: auto">
        <v-btn icon>
          <v-icon>apps</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>notifications</v-icon>
        </v-btn>
        <v-menu offset-y>
      <v-btn icon large slot="activator">
          <v-avatar size="32px" tile>
            <img
              src="https://vuetifyjs.com/static/doc-images/logo.svg"
              alt="Vuetify"
            >
          </v-avatar>
        </v-btn>
      <v-list>
        <v-list-tile v-for="item in items1" :key="item.title" @click="menu_method(item)">
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-menu>
      </div>
    </v-toolbar>
    <v-content>
      <router-view :key="$route.fullPath">
      </router-view>
    </v-content>
    <login ref="login" v-bind:method="signup"></login>
    <registration ref="registration" v-bind:method="login"></registration>
  </v-app>
</template>

<script>
  import Login from './components/Login.vue'
  import Registration from './components/Registration.vue'
  import auth from './auth'
  const API_URL = 'http://localhost:8000/api/'
  const CATS = API_URL + 'categories/'

  export default {
    name: 'app',
    components: {
      'login': Login,
      'registration': Registration
    },

    created () {
      this.axios.get(CATS)
        .then(response => {
      // JSON responses are automatically parsed.
          this.categories = response.data
        })
    },
    methods: {
      menu_method: function (item) {
        if (item.title === 'Вход') {
          this.login()
        } else if (item.title === 'Регистрация') {
          this.signup()
        }
      },
      signup: function () {
        this.$refs.login.dialog_log = false
        this.$refs.registration.dialog_reg = true
      },
      login: function () {
        this.$refs.registration.dialog_reg = false
        this.$refs.login.dialog_log = true
      },
      search: function () {
        this.$router.push('/search')
      }
    },
    data: () => ({
      drawer: null,
      user: auth.user,
      query: '',
      categories: [],
      items1: [
        { title: 'Вход' },
        { title: 'Регистрация' }
      ],
      items: {header: 'Категории'}
    }),
    props: {
      source: String
    }
  }
</script>


<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
