<template>
  <v-layout column>
    <v-flex class="rest_detail__top">
      <div class="rest_detail__top__section">
        <h1>{{ input.name }}</h1>
        <p class="rest_detail__subtitle rest_detail__subtitle--first">
          {{ input.cuisine }}
        </p>
        <p class="rest_detail__subtitle">
          {{ input.location }}
        </p>
        <p class="rest_detail__subtitle">
          {{ `Max Occupancy: ${input.occupancy}` }}
        </p>
      </div>
      <div class="rest_detail__top__section rest_detail__top__section--btn">
        <v-btn large color="primary" @click="modal = !modal">
          Request
        </v-btn>
      </div>
    </v-flex>
    <v-flex class="rest_detail__section">
      <p>
        {{ input.description }}
      </p>
    </v-flex>
    <v-flex class="rest_detail__section">
      <v-img src="https://picsum.photos/id/11/1000/300" />
    </v-flex>
    <v-flex class="rest_detail__section">
      <v-img src="https://picsum.photos/id/12/1000/300" />
    </v-flex>
    <v-flex class="rest_detail__section">
      <v-img src="https://picsum.photos/id/13/1000/300" />
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
            :items="input.time"
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
      input: {
        name: 'Restaurant Name',
        location: '140 East 14th Street, New York, NY, 10003',
        cuisine: 'Indian Food',
        occupancy: 10,
        image: '',
        description: `
          This is a description for the restaurant, This is a description for the restaurant,
          This is a description for the restaurant, This is a description for the restaurant,
          This is a description for the restaurant, This is a description for the restaurant,
          This is a description for the restaurant, This is a description for the restaurant,
          This is a description for the restaurant, This is a description for the restaurant,
        `,
        time: [
          '2019-10-5 14:00 ~ 16:00',
          '2019-10-6 14:00 ~ 16:00',
          '2019-10-7 14:00 ~ 16:00'
        ],
        position: {
          lat: 40.730610,
          lng: -73.935242
        }
      }
    }
  },
  computed: {
    restInfo () {
      const { id } = this.$route.params
      const restaurants = this.$store.state.restaurants
    }
  }
}
</script>

<style lang="scss">
.rest_detail__top {
  display: flex;
  margin-top: 32px;
}
.rest_detail__section {
  margin-top: 32px;
}
.rest_detail__top__section {
  flex: 1;
  width: 50%;
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
</style>
