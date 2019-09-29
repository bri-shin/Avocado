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
  async getMatchByRestId ({ commit }, payload) {
    const data = await this.$axios.$post(`${API_URL}/get-match-by-restid`, { RestID: payload })
    const arr = Object.values(data)
    commit('SET_MATCHES', arr)
  },
  async getMatchByChefId ({ commit }, payload) {
    const data = await this.$axios.$post(`${API_URL}/get-match-by-chefid`, { ChefID: payload })
    const arr = Object.values(data)
    commit('SET_MATCHES', arr)
  }
}
