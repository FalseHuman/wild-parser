import Vue from 'vue'
import Vuex from 'vuex'
import parsing from './modules/parsing'

Vue.use(Vuex)

const store = new Vuex.Store({
    modules: {
        parsing
    },
})

export default store