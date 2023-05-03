
let turn =true
const botonlista=document.querySelectorAll('button')
const moverArray =new Array(9).fill(null)

function ganador(i,j,k){
    if (moverArray[i]==moverArray[j]&& moverArray[k]==moverArray[j]&& moverArray[i]
!=null)
return true

return false
}

botonlista.forEach((btn,index)=>{
    btn.addEventListener('click',event =>{
        event.target.textContent =turn ? 'X' :'O'

        moverArray[index]= turn
        if(ganador(0,1,2)||
        ganador(0,1,2)||
        ganador(3,4,5)||
        ganador(6,7,8)||
        ganador(0,3,6)||
        ganador(1,4,7)||
        ganador(2,5,8)||
        ganador(0,4,8)||
        ganador(2,4,6))

        document.querySelector('#winner')
        .textContent = `Ganó "${turn?'X':'O'}"`
        
        turn =!turn
    })

})
/*const botonPulsado=  (b)=>{
    const boton=b.target ;
 
    boton.style.backgroundColor='salmon';
 }
 
 document.querySelectorAll('button').forEach(obj => obj.addEventListener('click',botonPulsado));

document.getElementById("boton1").addEventListener("mouseover", function() {
   
});



document.getElementById("boton2").addEventListener("mouseover", function() {
   
});



document.getElementById("boton3").addEventListener("mouseover", function() {
   
});



document.getElementById("boton4").addEventListener("mouseover", function() {
  
});



document.getElementById("boton5").addEventListener("mouseover", function() {
   
});



document.getElementById("boton6").addEventListener("mouseover", function() {
   
});



document.getElementById("boton7").addEventListener("mouseover", function() {
   
});



document.getElementById("boton8").addEventListener("mouseover", function() {
    
});



document.getElementById("boton9").addEventListener("mouseover", function() {
    
});*/



