 
function mango(q, p){
  
  
  if(q >= 3){
    freeMango = Math.floor(q / 3)
    result = (q - freeMango) * p
    return result
  }else{
  return q * p
  }
}