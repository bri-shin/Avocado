<template>
  <v-app-bar app flat color="#6AAC63" class="toolbar">
    <v-toolbar-title class="toolbar__title">
      <img src="../static/logo.svg" class="toolbar__logo" @click="navigateToHome">
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
export default {
  name: 'ToolBar',
  methods: {
    navigateToHome () {
      this.$router.push('/')
    }
  }
}
</script>

<style>
.toolbar__title {
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.toolbar__logo {
  margin-left: 20px;
  height: 40px;
}
.toolbar__btn {
  color: white !important;
  font-size: 10px;
}
</style>
