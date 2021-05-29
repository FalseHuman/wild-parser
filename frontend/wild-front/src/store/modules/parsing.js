export default {
    actions: {
        async fetchProduct(ctx){
            const res = await fetch(
                'http://127.0.0.1:8001/api/product/'
            )
            const parsing =  await res.json()

            ctx.commit('updateProduct', parsing)
        }
    },
    mutations: {
        updateProduct( state, parsing){
            state.parsing = parsing
        }
    },
    state: {
        parsing: [],
    },
    getters: {
        allProduct(state){
            return state.parsing
        }
    },
}