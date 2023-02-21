   let detalle="Definimos <b>variables</b>y vemos cosas relativas";// defino una variable con el mensaje 

   let detalle2="<ol> <li>Definimos variables</li>  <li>y vemos cosas relativas</li> </ol> ";
   
    console.log(typeof(detalle),detalle);// lo muestro para verificar 
   
  var elemento=document.getElementById ("aqui");  // obtengo un puntero al alemento html que quiero modificar 
   elemento.innerHTML=detalle2; // modifico el contenido 
   

 