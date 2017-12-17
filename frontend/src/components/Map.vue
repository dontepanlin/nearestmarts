<template>
  <gmap-map
    :center="cntr"
    :zoom="15"
    style="width: 500px; height: 300px"
  >
    <gmap-info-window :options="infoOptions" :position="infoWindowPos" :opened="infoWinOpen"
                      @closeclick="infoWinOpen=false">
      {{infoContent}}
    </gmap-info-window>
    <gmap-marker
      :position="center"
      :clickable="true"
      :draggable="true"
      @click="toggleInfoWindow(center,-1)"
    ></gmap-marker>
    <gmap-marker
      :key="index"
      v-for="(m, index) in place"
      :position="get_item(m)"
      :clickable="true"
      :draggable="true"
      @click="toggleInfoWindow(m,index)"
    ></gmap-marker>
  </gmap-map>
</template>

<script>
  //  import auth from '../auth'
  export default {
    props: ['place', 'cntr'],
    data () {
      return {
        center: {lat: 10.0, lng: 10.0},
        markers: this.place,
        infotext: ['Вы'],
        infoContent: '',
        infoWindowPos: {
          lat: 0,
          lng: 0
        },
        infoWinOpen: false,
        currentMidx: null,
        //  optional: offset infowindow so it visually sits nicely on top of our marker
        infoOptions: {
          pixelOffset: {
            width: 0,
            height: -35
          }
        }
      }
    },
    created () {
      this.center = {
        lat: this.cntr.lat,
        lng: this.cntr.lng
      }
    },
    watch: {
      '$route' (to, from) {
        // Call resizePreserveCenter() on all maps
        this.$gmapDefaultResizeBus.$emit('resize')
      }
    },
    methods: {
      toggleInfoWindow: function (marker, idx) {
        if (idx === -1) {
          this.infoContent = this.infotext[0]
          this.infoWindowPos = marker
        } else {
          this.infoContent = marker.name
          this.infoWindowPos = this.get_item(marker)
        }

        //  check if its the same marker that was selected if yes toggle
        if (this.currentMidx === idx) {
          this.infoWinOpen = !this.infoWinOpen
        } else {
          this.infoWinOpen = true
          this.currentMidx = idx
        }
      },
      get_item: function (item) {
        return {lat: item.lat, lng: item.lon}
      }
    }
  }
</script>
