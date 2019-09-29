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
            v-for="item in matched"
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
                  <v-list-item-title>
                    Chef One
                  </v-list-item-title>
                  <v-divider />
                  <v-list-item-subtitle>
                    This is the description for this guy
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    About the dish
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    Ingredients List
                  </v-list-item-subtitle>
                  <v-divider />
                  <v-list-item-subtitle>
                    Date
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    Time
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
            v-for="item in requested"
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
                  <v-list-item-title>
                    Chef One
                  </v-list-item-title>
                  <v-divider />
                  <v-list-item-subtitle>
                    This is the description for this guy
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    About the dish
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    Ingredients List
                  </v-list-item-subtitle>
                  <v-divider />
                  <v-list-item-subtitle>
                    Date
                  </v-list-item-subtitle>
                  <v-list-item-subtitle>
                    Time
                  </v-list-item-subtitle>
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
</style>
