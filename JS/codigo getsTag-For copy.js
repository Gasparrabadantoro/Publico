// creo el contenido del segundo div

let piramid="";

   
  var divs=document.getElementsByTagName ("div");  // obtengo un puntero al alemento html que quiero modificar 

  // modifico el color de fondo de todos los parrafos 

  for (let vert=1;i<6;vert++){
    for(let horizontal =1;horizontal <=vert;horizontal++){
       piramid=piramid+vert;
    piramid=piramid+"<br/>";
    }
   
  }

  divs[1].innerHTML=piramid;

 