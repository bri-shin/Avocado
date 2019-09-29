<template>
  <v-layout fill-height class="chef">
    <v-flex class="chef__panel">
      <v-list style="padding: 0;">
        <v-subheader>
          For Chefs
        </v-subheader>
        <v-list-item-group v-model="selectedPanel">
          <v-list-item
            v-for="(item, i) in panelList"
            :key="i"
          >
            <v-list-item-content>
              <v-list-item-title>
                {{ item }}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-flex>
    <v-flex v-if="panelList[selectedPanel] == 'Restaurants'" scrollable class="chef__section">
      <v-subheader style="background: white;">
        Available Restaurants
      </v-subheader>
      <v-divider />
      <v-list three-line max-height="93%" class="overflow-y-auto chef__list">
        <v-list-item-group v-model="selected">
          <v-list-item
            v-for="(item, i) in restList"
            :key="i"
            class="chef__restaurant__item"
            @click="navigateTo(item.RestID)"
          >
            <v-list-item-icon>
              <v-avatar color="primary">
                <v-icon>mdi-account</v-icon>
              </v-avatar>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="item.Name" />
              <v-list-item-subtitle v-text="item.address" />
              <v-list-item-subtitle v-text="`${item.Cuisine.join(', ')} Cuisine`" />
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-flex>
    <v-flex v-if="panelList[selectedPanel] == 'Restaurants'">
      <gmap-map :center="center" :map-type-id="mapTypeId" :zoom="14" :options="options">
        <gmap-marker
          v-for="(item, index) in restList"
          :key="index"
          :position="item.position"
          @click="center = item.position"
        />
      </gmap-map>
    </v-flex>
    <v-flex v-if="panelList[selectedPanel] == 'Status'">
      <StatusPanel :confirmed="confirmedMatches" :pending="pendingMatches" />
    </v-flex>
  </v-layout>
</template>

<script>
import StatusPanel from '@/components/StatusPanel'
export default {
  layout: 'landing',
  components: {
    StatusPanel
  },
  data () {
    return {
      panelList: ['Restaurants', 'Status'],
      selectedPanel: 0,
      selected: '',
      center: { lat: 40.729772, lng: -73.99941111 },
      mapTypeId: 'terrain',
      options: {
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: false,
        rotateControl: false,
        fullscreenControl: false
      }
    }
  },
  computed: {
    restList () {
      return this.$store.state.restaurants
    },
    confirmedMatches () {
      return this.$store.state.matches.filter(match => match.Status === 1)
    },
    pendingMatches () {
      return this.$store.state.matches.filter(match => match.Status === 0)
    }
  },
  async fetch ({ store, params }) {
    await store.dispatch('getAllRestaurants')
    await store.dispatch('getMatchByChefId', 'Chef001')
    console.log('Fetched')
  },
  methods: {
    navigateTo (id) {
      this.$router.push(`restaurants/${id}`)
    }
  }
}
</script>

<style lang="scss">
.chef__section {
  height: 91.5vh;
}
.chef__panel {
  min-width: 200px;
  max-width: 200px;
  background: white;
  border-right: 1px solid #e0e0e0;
  height: 91.5vh;
}
.chef__restaurant__item + .chef__restaurant__item {
  border-top: 1px solid #E0E0E0;
}
.vue-map-container {
  height: 100%;
  width: 100%;
}
</style>
