
'use strict';
var colorfuente = "white";
// maneras de declarar arrays 
// defino un array con colores , tipo contaste 
const colores = [];
colores[0] = "green";
colores[1] = "red";
colores[2] = "blue";
colores[3] = "white";
colores[4] = "magenta";

const colores2 = ["green", "red", "blue", "white", "magenta"];

const colores3 = new Array("green", "red", "blue", "white", "magenta");

const colores4 = new Array(3);
colores[0] = "green";
colores[1] = "red";
colores[2] = "blue";
colores[3] = "white";
colores[4] = "magenta";


// funcion que sirve para mostrar un mensaje en un elemto
function saludar(identificador) {
    let elem = document.getElementById(identificador)
    elem.style.color = colorfuente;
    elem.innerHTML = "Hi there";
    colorfuente = getComputedStyle(elem).backgroundColor;
}

function pintar() {

   /*  // sirva pra pintar los cuadros de distintos colores */

    for (let x = 1; x <= colores.length; x++) {
        let ident ="c"+x;
        let cf =colores[x-1];
        rellenar(ident,cf);


    }
    
}
function rellenar(identificador, colorfondo) {
        let elem = document.getElementById(identificador)
        elem.style.backgroundcolor = colorfondo;


    }

    pintar();