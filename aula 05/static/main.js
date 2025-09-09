

function login(){

    let conteiner = document.querySelector(".ver")
    let login = document.querySelector(".login")
    let registro = document.querySelector(".Registro")
    login.style.display = "flex"
    registro.style.display = "none"
    conteiner.style.display = "none"

}
function registro(){

    let conteiner = document.querySelector(".ver")
    let login = document.querySelector(".login")
    let registro = document.querySelector(".Registro")
    login.style.display = "none"
    registro.style.display = "flex"
    conteiner.style.display = "none"

}

if (document.querySelector("#mostrar").innerHTML == "true"){

    let conteiner = document.querySelector(".ver")
    let login = document.querySelector(".login")
    let registro = document.querySelector(".Registro")
    login.style.display = "none"
    registro.style.display = "none"
    conteiner.style.display = "block"


}