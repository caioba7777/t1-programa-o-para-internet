function confirmarExclusao() {
    return confirm("Tem certeza que deseja excluir este registro?");
}

function verificarForcaSenha() {
    let senha = document.getElementById("senha");
    let texto = document.getElementById("forcaSenha");

    if (!senha || !texto) {
        return;
    }

    let valor = senha.value;

    if (valor.length === 0) {
        texto.innerHTML = "";
    } else if (valor.length < 4) {
        texto.innerHTML = "Força da senha: fraca";
        texto.style.color = "red";
    } else if (valor.length < 8) {
        texto.innerHTML = "Força da senha: média";
        texto.style.color = "orange";
    } else {
        texto.innerHTML = "Força da senha: forte";
        texto.style.color = "green";
    }
}