import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    pin: 542669,
    idUrl: "https://www.menti.com/core/identifier",
    infoUrl: 'https://www.menti.com/core/vote-ids/',
    voteUrl: "https://www.menti.com/core/votes/",
    ids: [],
    info: {}
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
          .get(state.infoUrl+pin+"/series")
          .catch(error => {
            console.log(error)
          })
          .then(response => {
            console.log(response.data)
            state.info = response.data
          });
    }
  },
  actions: {},
  modules: {}
})