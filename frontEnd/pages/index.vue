<template>
  <v-layout
    column
    justify-center
    flat
    class="main"
  >
    <v-flex class="main__container__top">
      <div class="main__container__logo">
        Tofu
      </div>
    </v-flex>
    <v-layout class="main__tabs">
      <v-flex class="main__tabs__item">
        For Restaurants
      </v-flex>
      <v-flex class="main__tabs__item">
        For Chefs
      </v-flex>
      <v-flex class="main__tabs__item">
        For Foodies
      </v-flex>
    </v-layout>
  </v-layout>
</template>

<script>
export default {
  name: 'LandingPage'
}
</script>

<style lang="scss">
.main {
  height: 100%;
  width: 100vw;
}
.main__container__logo {
  height: 70%;
  width: 15%;
  background: white;
}
.main__container__top {
  width: 100%;
  height: 15vh;
  background: green;
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
.main__container__top__text {
}
.main__tabs {
  width: 100%;
  height: 30%;
  padding: 0 5%;
}
.main__tabs__item {
  font-family: helvetica;
  height: 250px;
  width: 20%;
  background: blue;
}
.main__tabs__item  + .main__tabs__item {
  margin-left: 16px;
}
</style>
