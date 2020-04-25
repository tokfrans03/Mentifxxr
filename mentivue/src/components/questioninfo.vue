<template>
  <v-container grid-list-xs class="mx-auto">
    <v-row>
      <v-col
        cols="auto"
        primary-title
        :style="(Question.id == $store.state.info.pace.active)? 'color: green': 'color: red'"
      >
        <div>
          <h3 class="headline mb-0">{{Question.question}}</h3>
          <div>{{Question.type}}</div>
        </div>
      </v-col>
      <v-col>
        <v-card v-if="(Question.id == $store.state.info.pace.active)">
          <v-form v-if="Question.type == 'wordcloud'" class="pa-4">
            <v-text-field label="What to say" v-model="text"></v-text-field>
            <v-slider v-model="amount" :min="1" :max="10" step="1">
              <template v-slot:append>
                <v-text-field
                  v-model="amount"
                  class="mt-0 pt-0"
                  hide-details
                  single-line
                  type="number"
                  style="width: 60px"
                ></v-text-field>
              </template>
            </v-slider>
            <v-btn color="success" @click="send(Question.type, Question.id, text, amount)">send</v-btn>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";
import axios from "axios";

export default {
  name: "question",
  data() {
    return {
      text: "",
      amount: 1
    };
  },
  props: {
    Question: {
      type: Object,
      required: true
    }
  },
  computed: {
    ...mapGetters(["info", "voteUrl"])
  },
  methods: {
    ...mapMutations({
      // Get_ID: "Get_ID",
      Get_info: "Get_info"
    }),
        Get_ID(){
      return axios
        .post(this.$store.state.idUrl)
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
    send(type, id, text, times) {
      for (let i = 0; i < times; i++) {
        this.Get_ID().then(ID => {
          let headers = {
            "x-identifier": ID,
            // cookie: "identifier1=" + ID, // får inte för chrome :/
            // "origin": "https://www.menti.com", // får inte för chrome :/
            "Content-Type": "application/json"
          };
          console.log(headers);
          switch (type) {
            case "wordcloud": {
              let data = { question_type: type, vote: text };

              axios.post(this.$store.state.voteUrl + id, data, {
                headers: headers
              });
              break;
            }
            case "choices": {
              console.log("AAA");
              break;
            }
          }
        });
      }
    }
  }
};
</script>