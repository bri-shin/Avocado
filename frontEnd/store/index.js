export const state = () => ({
  restaurants: null,
  chefs: null,
  matches: null
})

export const mutations = {
  SET_RESTAURANTS (state, payload) {
    state.restaurants = payload
  },
  SET_CHEFS (state, payload) {
    state.chefs = payload
  },
  SET_MATCHES (state, payload) {
    state.matches = payload
  }
}

const API_URL = 'https://avocadohackny.appspot.com'

export const actions = {
  async getAllRestaurants ({ commit }) {
    const data = await this.$axios.$get(`${API_URL}/get-all-restaurants`)
    const arr = Object.values(data)
    commit('SET_RESTAURANTS', arr)
  },
  async getAllChefs ({ commit }) {
    const data = await this.$axios.$get(`${API_URL}/get-all-chefs`)
    const arr = Object.values(data)
    commit('SET_CHEFS', arr)
  },
  async getMatchByRestId ({ commit }) {
    const data = await this.$axios.$get(`${API_URL}/get-match-by-restid`)
    commit('SET_MATCHES', data)
  },
  async getMatchByChefId ({ commit }) {
    const data = await this.$axios.$get(`${API_URL}/get-match-by-chefid`)
    commit('SET_MATCHES', data)
  }
}
