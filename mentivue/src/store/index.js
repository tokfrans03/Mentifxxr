import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    pin: 852698,
    // cors_server: "https://cors-anywhere.herokuapp.com/",
    cors_server: "http://192.168.0.54:8090/",
    idUrl: "https://www.menti.com/core/identifier",
    infoUrl: 'https://www.menti.com/core/vote-ids/',
    info2Url: 'https://www.menti.com/core/vote-keys/',
    voteUrl: "https://www.menti.com/core/votes/",
    qfaUrl: "https://www.menti.com/core/qfa",
    ids: [],
    info: {},
    qfa: {},
  },
  mutations: {
    Get_ID: (state, append) => {
      return axios
        .post(state.idUrl)
        // .catch(error => {
        //   console.log(error)
        // })
        .then(response => {
          // if (append) {sh(response.data.identifier);
          // } else {
          //   state.ids.pu
          return response.data.identifier;
          // }
        });
    },
    Get_info: (state, pin) => {
      axios
        .get(state.infoUrl + pin + "/series")
        .catch(error => {
          console.log(error)
        })
        .then(response => {
          // console.log(response.data)
          state.info = response.data
        });
    },
    Get_qfa: (state, id) => {
      axios.get(state.info2Url + id + '/qfa').then(response => {
        state.qfa = response.data
      })
    }
  },
  actions: {},
  modules: {}
})