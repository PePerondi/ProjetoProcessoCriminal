class User {
    constructor(usuario, senha) {
        this.usuario = usuario;
        this.senha = senha;
    }
}

function criarUsuario() {
    // Obter os valores dos campos de entrada
    var email = document.getElementById("email").value;
    var senha = document.getElementById("senha").value;

    // Criar uma instância de User
    var novoUsuario = new User(email, senha);

    // Exemplo de uso da instância:
    console.log("Usuário criado:", novoUsuario.email);
}