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
          <v-progress-linear :value="(sent/tosend)*100" height="15" color="primary"></v-progress-linear>
          <p>{{Math.round((sent/tosend) * 100)}}%</p>
          <!-- Wordcloud -->
          <v-form v-if="Question.type == 'wordcloud'" class="pa-4">
            <v-checkbox label="Random 1024 chars" v-model="random"></v-checkbox>
            <v-text-field label="What to say" :disabled="random" v-model="text"></v-text-field>
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
            <p>{{ids.length}}</p>
            <v-btn
              :color="gather? 'color: green': 'color: red'"
              class="mr-4"
              @click="send_ultra(Question.type, Question.id, text, amount)"
            >ultra spammm stage {{gather? "1": "2"}}</v-btn>
            <v-switch label="Stage" v-model="gather"></v-switch>

            <v-btn
              color="success"
              v-if="!random"
              @click="send(Question.type, Question.id, text, amount)"
            >send</v-btn>
            <v-btn
              color="success"
              v-else
              @click="send(Question.type, Question.id, random1024(), amount)"
            >send 1024</v-btn>
          </v-form>
          <!-- choises -->
          <v-form
            v-if="Question.type == ('choices' || 'choices_images' || 'winner' || 'ranking')"
            class="pa-4"
          >
            <!-- <p>{{ selected_choise }}</p> -->
            <v-radio-group v-model="selected_choise">
              <v-radio
                v-for="(choise, index) in Question.choices"
                :key="index"
                :label="choise.label"
                :value="choise.id"
              ></v-radio>
            </v-radio-group>
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
            <v-btn
              color="success"
              @click="send(Question.type, Question.id, selected_choise, amount)"
            >send</v-btn>
          </v-form>
          <!-- qfa -->
          <v-form v-if="Question.type == 'qfa'" class="pa-4">
            <v-checkbox label="Random 1024 chars" v-model="random"></v-checkbox>
            <v-text-field label="What to say" :disabled="random" v-model="text"></v-text-field>
            <!-- <v-slider v-model="amount" :min="1" :max="10" step="1">
              <template v-slot:prepend>
                <p>Likes</p>
              </template>
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
            </v-slider>-->
            <v-btn
              color="success"
              v-if="!random"
              @click="send(Question.type, Question.id, text, amount)"
            >send</v-btn>
            <v-btn
              color="success"
              v-else
              @click="send(Question.type, Question.id, random1024(), amount)"
            >send 1024</v-btn>
          </v-form>
          <v-form v-if="Question.type == 'qfa'" class="pa-4">
            <v-btn color="success" @click="Get_qfa($store.state.info.id)">Get questions</v-btn>
            <v-container v-if="Object.keys($store.state.qfa).length" class="ma-n4">
              <p style="color: red" v-if="!$store.state.qfa.data.length">No questions yet</p>
              <v-radio-group v-model="question" v-if="Object.keys($store.state.qfa.data).length">
                <v-radio
                  v-for="(qfa_question, index) in $store.state.qfa.data"
                  :key="index"
                  :label="qfa_question.question"
                  :value="qfa_question.id"
                ></v-radio>
              </v-radio-group>
              <v-slider
                v-model="amount"
                :min="1"
                :max="10"
                step="1"
                v-if="Object.keys($store.state.qfa.data).length"
              >
                <template v-slot:prepend>
                  <p>Likes</p>
                </template>
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
              <v-btn
                color="success"
                @click="send('like', Question.id, question, amount)"
                :disabled="!Boolean(question)"
                v-if="Object.keys($store.state.qfa.data).length"
              >send</v-btn>
            </v-container>
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
      amount: 1,
      random: false,
      selected_choise: "",
      question: "",
      tosend: 0,
      sent: 0,
      gather: true,
      ids: [],
      id_wanted: 0
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
      Get_info: "Get_info",
      Get_qfa: "Get_qfa"
    }),
    Get_ID() {
      return (
        axios
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
          })
      );
    },
    send_ultra(type, id, text, times) {
      if (this.gather) {
        this.id_wanted = times;
        this.tosend += times;
        for (let i = 0; i < times; i++) {
          this.Get_ID().then(ID => {
            this.sent++;
            this.ids.push(ID);
            // console.log(i);
          });
        }
      } else {
        this.tosend = this.ids.length
        this.send = 0
        for (let ID of this.ids) {
          let headers = {
            "x-identifier": ID,
            // cookie: "identifier1=" + ID, // får inte för chrome :/
            // "origin": "https://www.menti.com", // får inte för chrome :/
            "Content-Type": "application/json",
            "x-requested-with": "localhost"
          };
          let data = { question_type: type, vote: text };
          axios
            .post(
              this.$store.state.cors_server + this.$store.state.voteUrl + id,
              data,
              {
                headers: headers
              }
            )
            .then(() => {
              this.sent++;
            });
        }
      }
    },
    send(type, id, text, times) {
      for (let i = 0; i < times; i++) {
        this.tosend++;
        this.Get_ID().then(ID => {
          let headers = {
            "x-identifier": ID,
            // cookie: "identifier1=" + ID, // får inte för chrome :/
            // "origin": "https://www.menti.com", // får inte för chrome :/
            "Content-Type": "application/json",
            "x-requested-with": "localhost"
          };

          switch (type) {
            case "wordcloud":
            case "choices":
            case "choices_images":
            case "winner":
            case "ranking": {
              // console.log("che");
              let data = { question_type: type, vote: text };

              axios
                .post(
                  this.$store.state.cors_server +
                    this.$store.state.voteUrl +
                    id,
                  data,
                  {
                    headers: headers
                  }
                )
                .then(() => {
                  this.sent++;
                });
              break;
            }
            case "qfa": {
              let seriesid = this.$store.state.info.id;
              let data = { vote_key: seriesid, question: text };

              axios
                .post(
                  this.$store.state.cors_server + this.$store.state.qfaUrl,
                  data,
                  {
                    headers: headers
                  }
                )
                .then(() => {
                  this.sent++;
                });

              break;
            }
            case "like": {
              axios
                .post(
                  this.$store.state.cors_server +
                    this.$store.state.qfaUrl +
                    "/" +
                    text +
                    "/upvote",
                  {},
                  {
                    headers: headers
                  }
                )
                .then(() => {
                  this.sent++;
                });

              break;
            }
          }
        });
      }
    },
    random1024() {
      let result = "";
      let characters =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
      let charactersLength = characters.length;
      for (var i = 0; i < 1024; i++) {
        result += characters.charAt(
          Math.floor(Math.random() * charactersLength)
        );
      }
      return result;
    }
  }
};
</script>