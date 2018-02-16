<template>
  <v-app id="inspire">
    <v-toolbar
      color="primary"
      dark
      app
      clipped-left
      fixed
      extended
    >
      <v-toolbar-title :style="$vuetify.breakpoint.smAndUp ? 'width: 300px; min-width: 250px' : 'min-width: 72px'"
                       class="ml-0 pl-3">
        <v-toolbar-side-icon @click.stop="drawer = !drawer" class="hidden-lg-and-up"></v-toolbar-side-icon>
        <router-link to="/" class="white--text">FindMarts</router-link>
      </v-toolbar-title>
      <v-container fluid>
        <v-layout row wrap mt-3>
      <v-text-field
              light
              solo
              v-model="query"
              placeholder="Search"
              @keyup.enter="search"
              style="min-width: 128px"
            ></v-text-field>
          <v-btn icon>
            <v-icon>search</v-icon>
          </v-btn>
        </v-layout>
        </v-container>
      <v-container fluid class="px-3" slot="extension">
        <v-layout row wrap>
          <v-flex xs3>
          <v-menu offset-y>
            <v-btn slot="activator" flat>
              <v-icon>list</v-icon>
              Категории
            </v-btn>
            <v-list>
              <template v-for="cat in categories">
                <v-list-tile @click="">
                  <v-list-tile-content>
                    <v-list-tile-title>{{ cat.name }}</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-divider></v-divider>
              </template>
            </v-list>
          </v-menu>
          </v-flex>
          <v-flex xs6>

          </v-flex>

        </v-layout>
      </v-container>
      <div class="d-flex align-center" style="margin-left: auto">
        <v-btn light flat class="white--text" v-if="user.authenticated" to="/mymarts">
          My marts

        </v-btn>
        <v-btn icon>
          <v-icon>star</v-icon>
        </v-btn>
        <v-menu offset-y left>
          <v-btn icon slot="activator">
            <v-icon>notifications</v-icon>
          </v-btn>
          <v-list>
            <v-list-tile v-for="item in items" :key="item.title" @click="">
              <v-list-tile-title>У вас нет уведомлений</v-list-tile-title>
            </v-list-tile>
          </v-list>
        </v-menu>
        <v-menu offset-y :nudge-width="200">
          <v-btn icon large slot="activator">
            <v-avatar size="32px" tile>
              <img
                src="https://vuetifyjs.com/static/doc-images/logo.svg"
                alt="Vuetify"
              >
            </v-avatar>
          </v-btn>
          <v-list v-if="!user.authenticated">
            <v-list-tile v-for="item in items1" :key="item.title" @click="menu_method(item)">
              <v-list-tile-title>{{ item.title }}</v-list-tile-title>
            </v-list-tile>
          </v-list>
          <v-card v-if="user.authenticated">
            <v-list>
              <v-list-tile>
                <v-list-tile-content>
                  <v-list-tile-title>Пользователь</v-list-tile-title>
                  <v-divider></v-divider>
                  <v-list-tile-sub-title>{{ user.name }}</v-list-tile-sub-title>
                </v-list-tile-content>
              </v-list-tile>
            </v-list>
            <v-card-actions>
              <v-btn color="primary" flat>Profile</v-btn>
              <v-spacer></v-spacer>
              <v-btn color="error" flat @click="logout()">Logout</v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </div>
    </v-toolbar>
    <v-content>
      <router-view :key="$route.fullPath">
      </router-view>
    </v-content>
    <login ref="login" v-bind:method="signup"></login>
    <registration ref="registration" v-bind:method="login"></registration>
    <v-footer class="pa-3" color="secondary">
      <v-spacer></v-spacer>
      <div>© {{ new Date().getFullYear() }}</div>
    </v-footer>
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
      if (auth.user.authenticated) {
        auth.user_info(this)
        auth.checkAuth()
        console.log(this.user)
      }
      this.axios.get(CATS)
        .then(response => {
          // JSON responses are automatically parsed.
          this.categories = response.data.results
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
      },
      logout: function () {
        auth.logout(this)
      }
    },
    data: () => ({
      drawer: null,
      user: auth.user,
      query: '',
      categories: [],
      items1: [
        {title: 'Вход'},
        {title: 'Регистрация'}
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

  A {
    text-decoration: none; /* Убирает подчеркивание для ссылок */
  }
</style>
