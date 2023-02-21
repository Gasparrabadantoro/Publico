   let detalle="Definimos <b>variables</b>y vemos cosas relativas";// defino una variable con el mensaje 

   let detalle2="<ol> <li>Definimos variables</li>  <li>y vemos cosas relativas</li> </ol> ";
   
    console.log(typeof(detalle),detalle);// 
   
  var parrafos=document.getElementsByTagName ("p");  // obtengo un puntero al alemento html que quiero modificar 
  parrafos[3].innerHTML=detalle; // modifico el contenido 
// solo al parrafo 3 
  parrafos[3].style.backgroundColor="yellow";
  // modifico el color de fondo de todos los parrafos 

  for (let i=0;i<5;i++){
    parrafos[i].style.backgroundColor="yellow";
  }

 