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
    commit('SET_RESTAURANTS', data)
  },
  async getAllChefs ({ commit }) {
    const data = await this.$axios.$get(`${API_URL}/get-all-chefs`)
    commit('SET_CHEFS', data)
  },
  async getMatchByRestId ({ commit }) {
    const data = await this.$axios.$get(`${API_URL}/get-match-by-restid`)
    commit('SET_MATCHES', data)
  },
  async getMatchByCustId ({ commit }) {
    const data = await this.$axios.$get(`${API_URL}/get-match-by-custid`)
    commit('SET_MATCHES', data)
  }
}
