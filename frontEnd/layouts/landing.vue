<template>
  <v-app class="landing">
    <toolbar />
    <v-content fluid>
      <v-container fluid class="general__container">
        <nuxt />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import toolbar from '@/components/ToolBar.vue'
export default {
  components: {
    toolbar
  }
}
</script>

<style>
.landing {
  background: white !important;
}
.general__container {
  padding: 0 !important;
  margin: 0 !important;
  /* height: 91%; */
}
</style>
