<template>
  <div id="app">

<form @submit.prevent="submitForm">
<div class="form-group row">
<input type="text" class="form-control col-3 mx-2" placeholder ="nome"
v-model="produto.nome">
    <input type="text" class="form-control col-3 mx-2" placeholder ="preco"
v-model="produto.preco">

<button class ="btn btn-sucess"> Enviar </button>
</div>
</form>

  <table class="table">
    <thead>
      <th>nome</th>
        <th>categoria</th>
        <th>preco</th>
    </thead>
    <tbody>
        <tr v-for="produto in produtos" :key="produto.id" @dblclick="$data.produto = produto">
            <td>{{produto.nome}}</td>
            <td>{{produto.categoria}}</td>
            <td>{{produto.preco}}</td>


                        <td>
                <button class="btn btn outline-danget btn-sm mx-1"
                        @click="editProduto(produto)">o</button>
            </td>
                <button class="btn btn outline-danget btn-sm mx-1"
                        @click="deleteProduto(produto)">x</button>


        </tr>
    </tbody>
  </table>
  </div>
</template>

<script>
export default {
  name: 'App',
    data () {
        return {
        active: false,
        show: false,
        selectedUser: null,
        produto: {},
        produtos:[]
        }
    },
    async created(){
       await this.getProdutos();
    },


    methods: {
        onConfirm() {
        this.$emit("confirm");
		},
    submitForm(){
        if (this.produto.id === undefined)
        {
        this.createProduto();
        }
        else {
        this.editProduto();
        }

    },
    async getProdutos(){
        var response = await fetch('http://127.0.0.1:8000/api/produtos/');
        this.produtos = await response.json();
    },


    async createProduto(){

        await this.getProdutos();

        await fetch ('http://127.0.0.1:8000/api/produtos/',
        {method: 'post',
        headers: { 'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.produto)
        });
        await this.getProdutos();
    },
    async editProduto()
    {
         await this.getProdutos();

        await fetch (`http://127.0.0.1:8000/api/produtos/${this.produto.id}/`,
        {
        method: 'put',
        headers: { 'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.produto)
        });
        await this.getProdutos();

    },


    async deleteProduto(produto)
    {

        await fetch (`http://127.0.0.1:8000/api/produtos/${produto.id}/`,
        {
        method: 'delete',
        headers: { 'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.produto)
        });
        await this.getProdutos();


    },
    confirmDelete(produto){
     this.selectedUser = produto;
     this.confirmModal = true;
    },
    toggleModal() {

      const body = document.querySelector("body");
      this.active = !this.active;
      this.active
        ? body.classList.add("modal-open")
        : body.classList.remove("modal-open");
      setTimeout(() => (this.show = !this.show), 10);

    }
  }
};

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
