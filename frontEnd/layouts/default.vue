<template>
  <v-app class="default__app">
    <v-content>
      <v-container fluid fill-height class="default__container">
        <nuxt />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {}
</script>

<style>
.default__app {
  background: white;
}
.default__container {
  padding: 0 !important;
}
</style>
