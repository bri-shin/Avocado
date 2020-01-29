<template>
  <v-layout
    column
    justify-center
    flat
    class="main"
  >
    <v-flex class="main__container__top">
      <img class="main__container__top__logo" src="../static/logo-vertical.svg">
      <v-icon large>
        mdi-menu-down
      </v-icon>
    </v-flex>
    <v-layout style="display: flex;" class="main__description">
      <p style="color: #7B8898;">
        The web application has features that directly addresses the pain points of our target users. Aspiring chefs can sign up on the app and list out their cuisines of specialization. Restaurants can sign up and list any free time slots that they might have, as well as what cuisine they specialize in. Chefs can then apply to occupy a time slot at a particular restaurant, and it is up to the restaurant to decide whether or not they will allow the chef to occupy the space.To help them make this decision, each chef will have a composite rating score based on their past performances and customer ratings of them. In the event where the restaurant agrees to give the space to the chef, they may be compensated in two different ways : a) A flat "rent" cost at a nominal rate b) A portion of the chef's earnings for the day. Customers, or foodies, will be presented a list of restaurants that have such chefs cooking at them, and they have an option of RSVP'ing for a meal at a flat rate. In addition to this, the foodies are provided with recommendations of which chefs' cuisines they might enjoy next.
      </p>
    </v-layout>
    <div class="main__divider">
      <hr class="main__hr">
    </div>
    <v-layout class="main__tabs">
      <v-flex class="main__tabs__item" @click="navigateTo('chefs')">
        <p class="main__tabs__description">
          Chefs
        </p>
        <div class="main__tabs__img image--one" />
      </v-flex>
      <v-flex class="main__tabs__item" @click="navigateTo('restaurants')">
        <p class="main__tabs__description">
          Restaurants
        </p>
        <div class="main__tabs__img image--two" />
      </v-flex>
      <v-flex class="main__tabs__item">
        <p class="main__tabs__description">
          Foodies
        </p>
        <div class="main__tabs__img image--three" />
      </v-flex>
    </v-layout>
  </v-layout>
</template>

<script>
export default {
  name: 'LandingPage',
  layout: 'default',
  methods: {
    navigateTo (url, id) {
      this.$router.push(url)
    }
  }
}
</script>

<style lang="scss">
.main {
  height: auto;
  width: 100vw;
}
.main__tabs__img {
  width: 100%;
  height: 300px;
  border: none;
  background-position: center;
}
.image--one {
  background: linear-gradient(180deg, rgba(255,255,255,0) 0%, #A8A8A8 100%), url('../static/chef-main.jpg');
}
.image--two {
  background: linear-gradient(180deg, rgba(255,255,255,0) 0%, #A8A8A8 100%), url('../static/restaurant-main.jpg');
}
.image--three {
  background: linear-gradient(180deg, rgba(255,255,255,0) 0%, #A8A8A8 100%), url('../static/foodie-main.jpg');
}
.main__tabs__description {
  font-family: Helvetica;
  position: absolute;
  color: white;
  font-size: 32px;
  padding-right: 6px;
  font-weight: bold;
}
.main__container__logo {
  height: 70%;
  width: 15%;
  background: white;
}
.main__container__top {
  width: 100%;
  height: 120vh;
  background: linear-gradient(rgba(190, 226, 112, 0.94), #6AAC63), url('../static/landing-bg.png');
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  flex-direction: column;
  padding-bottom: 12px;
  &__logo {
    height: 45vh;
    text-align: center;
  }
}
.main__logo {
  color: black;
  background: white;
  height: 100%;
}
.main__description {
  padding: 3vh 10vw;
  text-align: justify;
  margin-top: 5vh;
}
.main__tabs {
  width: 100%;
  height: 30%;
  padding: 0 5%;
}
.main__divider {
  width: 100%;
  height: 10vh;
  margin: 10vh 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.main__hr {
  width: 30vw;
  height: 2px;
  background-color: #e0e0e0;
  border: none;
}
.main__tabs__item {
  display: flex;
  align-items: flex-end;
  justify-content: flex-end;
  font-family: helvetica;
  height: 250px;
  width: 20%;
  cursor: pointer;
}
.main__tabs__item  + .main__tabs__item {
  margin-left: 16px;
}
</style>
