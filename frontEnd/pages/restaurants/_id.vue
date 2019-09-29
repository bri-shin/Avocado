<template>
  <v-layout column class="rest_detail">
    <v-flex class="rest_detail__section">
      <v-img :src="restInfo.image" />
    </v-flex>
    <v-flex class="rest_detail__top">
      <div class="rest_detail__top__section">
        <h1>{{ restInfo.Name }}</h1>
        <p class="rest_detail__subtitle rest_detail__subtitle--first">
          {{ `${restInfo.Cuisine.join(', ')} Food` || `${restInfo.Cuisine[0]} Food` }}
        </p>
        <p class="rest_detail__subtitle">
          <v-icon small>mdi-star</v-icon>
          4.1/5.0
        </p>
        <p class="rest_detail__subtitle">
          {{ restInfo.address }}
        </p>
        <p class="rest_detail__subtitle">
          {{ `Max Occupancy: ${restInfo.occupancy_limit}` }}
        </p>
      </div>
      <div class="rest_detail__top__section rest_detail__top__section--btn">
        <v-btn large color="primary" @click="modal = !modal">
          Request
        </v-btn>
      </div>
    </v-flex>
    <v-flex class="rest_detail__section rest_detail__section--description">
      <p>
        {{ restInfo.Description }}
      </p>
      <v-divider />
    </v-flex>
    <v-flex class="rest_detail__section">
      <p class="rest_detail__subtitle rest_detail__extendmb">
        Past Collaborated Chefs
      </p>
      <span class="rest_detail__chefFaces">
        <v-avatar
          size="50"
          round
        >
          <img src="../../static/chef-face-four.jpg">
        </v-avatar>
        <v-avatar
          size="50"
          round
        >
          <img src="../../static/chef-face-five.jpg">
        </v-avatar>
      </span>
    </v-flex>
    <v-flex class="rest_detail__section">
      <gmap-map
        :center="{ lat: parseFloat(restInfo.position.lat), lng: parseFloat(restInfo.position.lng) }"
        :map-type-id="mapTypeId"
        :zoom="16"
        :options="options"
        class="id__googleMaps"
      >
        <gmap-marker
          :position="{ lat: parseFloat(restInfo.position.lat), lng: parseFloat(restInfo.position.lng) }"
        />
      </gmap-map>
    </v-flex>
    <v-dialog v-model="modal" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <h3 style="margin-bottom: 16px;">
            Request Form for Chefs
          </h3>
        </v-card-title>
        <v-card-text>
          <v-text-field
            v-model="request.name"
            label="Cuisine Name"
          />
          <v-text-field
            v-model="request.description"
            label="Description"
          />
          <v-combobox
            v-model="request.ingredients"
            label="Ingredients"
            multiple
            chips
          />
          <v-select
            v-model="request.time"
            :items="Object.keys(restInfo.open_schedule)"
            label="Available Time"
          />
        </v-card-text>
        <v-card-actions>
          <div class="flex-grow-1" />
          <v-btn color="blue darken-1" text @click="modal = false">
            Close
          </v-btn>
          <v-btn color="blue darken-1" text @click="modal = false">
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
export default {
  name: 'RestaurantDetail',
  layout: 'details',
  data () {
    return {
      modal: false,
      request: {
        name: '',
        ingredients: [],
        description: '',
        time: ''
      },
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
    restInfo () {
      const { id } = this.$route.params
      const restaurants = this.$store.state.restaurants
      return restaurants.filter(item => item.RestID === id)[0]
    }
  },
  async fetch ({ store, params }) {
    await store.dispatch('getAllRestaurants')
  }
}
</script>

<style lang="scss">
.rest_detail {
  margin: 0 20vw;
}
.rest_detail__top {
  display: flex;
  margin-top: 32px;
}
.rest_detail__section {
  margin-top: 32px;
}
.rest_detail__top__section {
  flex: 1;
  &--btn {
    display: flex;
    justify-content: flex-end;
  }
}
.rest_detail__subtitle {
  font-size: 14px;
  color: grey;
  margin-bottom: 0 !important;
  &--first {
    margin-bottom: 16px !important;
  }
}
.rest_detail__section--description {
  // width: 50%;
  text-align: justify;
}
.rest_detail__extendmb {
  margin-bottom: 16px !important;
}
.id__googleMaps {
  height: 300px !important;
  width: 100%;
}
</style>
