<template>
  <div class="home">
    <v-card class="mx-auto" max-width="500">
      <v-card-title primary-title>Pin</v-card-title>
      <v-form class="pa-4">
        <v-text-field label="pin" v-model="$store.state.pin" :rules="numrules" :counter="6"></v-text-field>
      </v-form>
      <v-card-actions>
        <v-btn color="success" @click="Get_info($store.state.pin)">Get info</v-btn>
      </v-card-actions>
      <v-card >
        <v-card-title primary-title>
          {{$store.state.info.given_name}}
        </v-card-title>
        <question v-for="(question, index) in $store.state.info.questions" :key="index" :Question="question"/>
      </v-card>
    </v-card>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters, mapMutations } from "vuex";
import question from "@/components/questioninfo";

export default {
  name: "Home",
  components: {
    question
  },
  data() {
    return {
      numrules: [
        v => !!v || "A Pin is required",
        v => (v && v.length == 6) || "A Pin must be 6 numbers",
        v => (v && !isNaN(v)) || "A Pin must be a number"
      ],
    };
  },
  computed: {
    // ...mapGetters(["pin", "id", "ids"])
  },
  methods: {
    ...mapMutations({
      Get_ID: "Get_ID",
      Get_info: "Get_info"
    })
  }
};
</script>
