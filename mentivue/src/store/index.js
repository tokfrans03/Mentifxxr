import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    pin: undefined,
    idUrl: "https://www.menti.com/core/identifier",
    infoUrl: 'https://www.menti.com/core/vote-ids/',
    id: "",
    ids: [],
    info: {}
  },
  mutations: {
    Get_ID: (state, append) => {
      axios
        .post(state.idUrl)
        .catch(error => {
          console.log(error)
        })
        .then(response => {
          if (append) {
            state.ids.push(response.data.identifier);
          } else {
            state.id = response.data.identifier;
          }
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