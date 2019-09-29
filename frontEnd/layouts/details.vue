<template>
  <v-app>
    <toolbar />
    <v-content fill-height>
      <v-container>
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
</style>
