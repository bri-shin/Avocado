<template>
  <v-layout fill-height>
    <v-flex class="chef__panel">
      <v-list style="padding: 0;">
        <v-subheader>
          For Restaurants
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
    <v-flex v-if="selectedPanel == 0">
      <v-container>
        <v-row>
          <v-col
            v-for="item in matchList"
            :key="item.index"
            class="d-flex child-flex"
            cols="4"
          >
            <v-card>
              <v-list-item>
                <v-list-item-avatar
                  size="75"
                  round
                >
                  <img src="../../static/chef-face.jpeg">
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title style="font-weight: bold;">
                    Chef Gorden Ramsay
                  </v-list-item-title>
                  <v-list-item-subtitle>
                    Local Chef interested in Korean Food
                  </v-list-item-subtitle>
                  <div class="divider__container">
                    <v-divider />
                  </div>
                  <v-list-item-subtitle style="font-weight: bold;" class="panel__spacer">
                    {{ item.Description }}
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    {{ item.Ingredients[0] }}
                  </v-list-item-subtitle>
                  <v-list-item-subtitle style="margin-top: 6px;">
                    2019-10-04
                  </v-list-item-subtitle>
                  <v-list-item-subtitle style="margin-bottom: 12px;">
                    {{ `${Object.keys(item.Schedule)[0]}, ${Object.values(item.Schedule)[0]}` }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-flex>
    <v-flex v-if="selectedPanel == 1">
      <v-container>
        <v-row>
          <v-col
            class="d-flex child-flex"
            cols="4"
          >
            <v-card>
              <v-list-item>
                <v-list-item-avatar
                  size="75"
                  round
                >
                  <img src="../../static/chef-face.jpeg">
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title>
                    <h4>Chef Gibden Rimsay</h4>
                  </v-list-item-title>
                  <v-divider />
                  <v-list-item-subtitle>
                    <p>
                      Local Chef interested in Korean Cuisine
                    </p>
                  </v-list-item-subtitle>
                  <v-list-item-subtitle style="font-weight: bold;">
                    Bibimbap
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    Rice, Vegetables
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    2019-10-03
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    Sat, 8-9pm
                  </v-list-item-subtitle>
                  <div style="margin-top: 22px; text-align: left;">
                    <v-btn style="margin-right: 6px;" color="primary" small>
                      Confirm
                    </v-btn>
                    <v-btn color="error" small>
                      Reject
                    </v-btn>
                  </div>
                </v-list-item-content>
              </v-list-item>
            </v-card>
          </v-col>
          <v-col
            class="d-flex child-flex"
            cols="4"
          >
            <v-card>
              <v-list-item>
                <v-list-item-avatar
                  size="75"
                  round
                >
                  <img src="../../static/chef-face-two.jpg">
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title>
                    <h4>Chef Gordon Ramsay</h4>
                  </v-list-item-title>
                  <v-divider />
                  <v-list-item-subtitle>
                    <p>
                      Local Chef interested in Chinese Cuisine
                    </p>
                  </v-list-item-subtitle>
                  <v-list-item-subtitle style="font-weight: bold;">
                    Black Bean Noodle
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    Black Bean, Noodle
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    2019-10-07
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    Mon, 3-4pm
                  </v-list-item-subtitle>
                  <div style="margin-top: 22px; text-align: left;">
                    <v-btn style="margin-right: 6px;" color="primary" small>
                      Confirm
                    </v-btn>
                    <v-btn color="error" small>
                      Reject
                    </v-btn>
                  </div>
                </v-list-item-content>
              </v-list-item>
            </v-card>
          </v-col>
          <v-col
            class="d-flex child-flex"
            cols="4"
          >
            <v-card>
              <v-list-item>
                <v-list-item-avatar
                  size="75"
                  round
                >
                  <img src="../../static/chef-face-three.jpg">
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-title>
                    <h4>Chef Gidon Hamsay</h4>
                  </v-list-item-title>
                  <v-divider />
                  <v-list-item-subtitle>
                    <p>
                      Local Chef interested in Korean Cuisine
                    </p>
                  </v-list-item-subtitle>
                  <v-list-item-subtitle style="font-weight: bold;">
                    JapChae
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    Vegetables, Beef
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    2019-10-07
                  </v-list-item-subtitle>
                  <v-list-item-subtitle style="margin-bottom: 6px">
                    Mon, 8-9pm
                  </v-list-item-subtitle>
                  <div style="margin-top: 22px; text-align: left;">
                    <v-btn style="margin-right: 6px;" color="primary" small>
                      Confirm
                    </v-btn>
                    <v-btn color="error" small>
                      Reject
                    </v-btn>
                  </div>
                </v-list-item-content>
              </v-list-item>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-flex>
    <v-flex v-if="selectedPanel == 2">
      <v-container class="commission__container">
        <h1>Look for a New Chef</h1>
        <p>Post an Invitation for Chefs to Come</p>
        <v-date-picker v-model="commission.date" :show-current="true" class="commission__date" />
        <v-text-field
          v-model="commission.time"
          label="Time"
          class="commission__time"
        />
        <v-btn
          class="commission__btn"
          color="primary"
          @click="navigateTo('restaurants')"
        >
          Submit
        </v-btn>
      </v-container>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: 'RestaurantsIndex',
  layout: 'landing',
  data () {
    return {
      expand_one: false,
      expand_two: false,
      expand_three: false,
      commission: {
        time: '',
        date: '2019-09-29'
      },
      panelList: ['Accepted', 'Request', 'Commission'],
      selectedPanel: 0,
      selected: '',
      matched: [
        {
          restaurant_name: 'Restaurant',
          cuisine_name: 'FOOD',
          description: 'FOOD DESCRIPTION',
          ingredients: ['1', '2', '3'],
          status: 0
        },
        {
          restaurant_name: 'Restaurant',
          cuisine_name: 'FOOD',
          description: 'FOOD DESCRIPTION',
          ingredients: ['1', '2', '3'],
          status: 0
        },
        {
          restaurant_name: 'Restaurant',
          cuisine_name: 'FOOD',
          description: 'FOOD DESCRIPTION',
          ingredients: ['1', '2', '3'],
          status: 0
        },
        {
          restaurant_name: 'Restaurant',
          cuisine_name: 'FOOD',
          description: 'FOOD DESCRIPTION',
          ingredients: ['1', '2', '3'],
          status: 0
        }
      ],
      requested: [
        {
          restaurant_name: 'Restaurant',
          cuisine_name: 'FOOD',
          description: 'FOOD DESCRIPTION',
          ingredients: ['1', '2', '3'],
          status: 0
        }
      ]
    }
  },
  computed: {
    matchList () {
      return this.$store.state.matches
    }
  },
  async fetch ({ store, params }) {
    await store.dispatch('getMatchByRestId', 'Rest001')
    console.log('Mounted')
  },
  methods: {
    navigateTo (url) {
      if (url === 'restaurants') {
        this.$router.go()
      }
    }
  }
}
</script>

<style lang="scss">
.chef__panel {
  min-width: 200px;
  max-width: 200px;
  background: white;
  border-right: 1px solid #e0e0e0;
  height: 91.5vh;
}
.commission__container {
  margin-top: 20px;
  text-align: center;
  display: flex;
  align-items: center;
  flex-direction: column;
}
.commission__date {
  margin-top: 12px;
}
.commission__time {
  margin-top: 16px;
  width: 23%;
}
.commission__btn {
  margin-top: 16px;
  width: 23%;
}
.divider__container {
  margin: 12px 12px 12px 0;
}
.panel__spacer {
  margin-top: 12px;
}
</style>
