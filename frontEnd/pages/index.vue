<template>
  <v-layout
    column
    justify-center
    flat
    class="main"
  >
    <v-flex class="main__container__top">
      <img src="../static/logo-vertical.svg">
    </v-flex>
    <v-layout>
      <p class="main__description">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras lacinia vulputate mi, cursus dapibus massa pretium id. Nulla nibh velit, finibus quis diam a, posuere pharetra tortor. Morbi vel elementum turpis. Morbi ultrices pharetra hendrerit. Vivamus a lectus ex. Phasellus viverra enim vitae lorem pharetra, imperdiet pretium eros euismod. Maecenas quis sem auctor, lobortis erat eu, fermentum purus. Quisque varius quis elit ut rutrum. Vivamus at ipsum in velit sagittis venenatis in a velit. Suspendisse potenti. Sed aliquam tristique quam, ut posuere risus bibendum in. Quisque eros tortor, ornare eget blandit maximus, iaculis et ex. Donec id volutpat felis, ac mollis ex. Nunc in purus tellus. Sed finibus laoreet enim a tincidunt. Duis porta, sem vitae consequat porta, massa nunc luctus orci, ut sagittis velit mauris vitae leo.
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
  mounted () {
    this.$store.dispatch('getAllRestaurants')
    console.log('Mounted')
  },
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
  background-image: linear-gradient(180deg, rgba(255,255,255,0) 0%, #A8A8A8 100%), url('../static/chef-main.jpg');
}
.image--two {
  background-image: linear-gradient(180deg, rgba(255,255,255,0) 0%, #A8A8A8 100%), url('../static/restaurant-main.jpg');
}
.image--three {
  background-image: linear-gradient(180deg, rgba(255,255,255,0) 0%, #A8A8A8 100%), url('../static/foodie-main.jpg');
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
  height: 50vh;
  background: linear-gradient(#BDE270, #6AAC63);
  display: flex;
  justify-content: center;
  align-items: flex-end;
  padding-bottom: 12px;
}
.main__logo {
  color: black;
  background: white;
  height: 100%;
}
.main__description {
  padding: 3vh 30vw;
  text-align: justify;
  margin-top: 5vh;
}
.main__tabs {
  width: 100%;
  height: 30%;
  padding: 0 5%;
  margin: 5% 0;
}
.main__divider {
  width: 100%;
  height: 10vh;
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
