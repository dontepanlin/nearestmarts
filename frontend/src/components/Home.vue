<template>
  <v-container fluid="fluid" class="text-xs-center">
    <v-layout row wrap>
      <v-flex xs12 sm6><span>Raised Dark Theme</span>
        <v-card height="185px" flat color="secondary">
          <v-card-text>
            <div>
              <v-btn color="primary" dark to="/login">Login</v-btn>
            </div>
            <div>
              <v-btn color="primary" dark to="/registration">Reg</v-btn>
            </div>
            <div>
              <v-btn color="primary" dark disabled>Disabled</v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    data: () => ({
      dialog: false
    }),
    props: {
      source: String
    }
  }
</script>
