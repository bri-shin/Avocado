<template>
  <div>
    <v-tabs
      v-model="tab"
      centered
      light
    >
      <v-tabs-slider />

      <v-tab href="#tab-1">
        Confirmed
      </v-tab>

      <v-tab href="#tab-2">
        Requested
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab" style="max-height: 85vh;" class="overflow-y-auto">
      <v-tab-item value="tab-1">
        <v-container>
          <v-row>
            <v-col
              v-for="item in confirmed"
              :key="item.index"
              class="d-flex child-flex"
              cols="3"
            >
              <v-card>
                <v-img :src="getRestImage(item.RestID)" />
                <v-card-title>
                  {{ getRestName(item.RestID) }}
                </v-card-title>
                <v-card-text>
                  <v-divider />
                  <p class="status__subtitle__header">
                    Proposed Cusine
                  </p>
                  <p class="status__subtitle status__subtitle__first">
                    {{ `${item.Cuisine[0]} Cuisine` }}
                  </p>
                  <p class="status__subtitle status__subtitle__title">
                    {{ item.Description }}
                  </p>
                  <p class="status__subtitle">
                    {{ item.Ingredients.join(', ') }}
                  </p>
                  <p>{{ item.time || 'Monday, 6-8pm' }}</p>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-tab-item>
      <v-tab-item row value="tab-2">
        <v-container>
          <v-row>
            <v-col
              v-for="n in 9"
              :key="n"
              class="d-flex child-flex"
              cols="3"
            >
              <v-card>
                <v-img src="https://cdn.vuetifyjs.com/images/cards/docks.jpg" />
                <v-card-title>Card Title</v-card-title>
                <v-card-text>Card Text</v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: 'StatusPanelComponent',
  props: ['confirmed', 'pending'],
  data () {
    return {
      tab: 'tab-1',
      matched: [
        {
          restaurant_name: 'Restaurant',
          cuisine_name: 'FOOD',
          description: 'FOOD DESCRIPTION',
          ingredients: ['1', '2', '3'],
          status: true
        },
        {
          restaurant_name: 'Restaurant',
          cuisine_name: 'FOOD',
          description: 'FOOD DESCRIPTION',
          ingredients: ['1', '2', '3'],
          status: true
        },
        {
          restaurant_name: 'Restaurant',
          cuisine_name: 'FOOD',
          description: 'FOOD DESCRIPTION',
          ingredients: ['1', '2', '3'],
          status: true
        },
        {
          restaurant_name: 'Restaurant',
          cuisine_name: 'FOOD',
          description: 'FOOD DESCRIPTION',
          ingredients: ['1', '2', '3'],
          status: true
        }
      ]
    }
  },
  methods: {
    getRestName (id) {
      const restList = this.$store.state.restaurants
      return restList.filter(rest => rest.RestID === id)[0].Name
    },
    getRestImage (id) {
      const restList = this.$store.state.restaurants
      return restList.filter(rest => rest.RestID === id)[0].image
    }
  }
}
</script>

<style lang="scss">
.panel__tab {
  height: 100%;
}
.status__subtitle {
  margin-bottom: 0 !important;
}
.status_divider {
  margin-top: 12px !important;
}
.status__subtitle__title {
  font-weight: bold;
}
.status__subtitle__first {
  margin-top: 12px;
}
</style>
