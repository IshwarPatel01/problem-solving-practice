function bump(x){
  
  let total = 0
  for(let i = 0; i < x.length;i++){
    if(x[i] === "n"){
      total += 1
    }
  }
    if (total > 15){
      return "Car Dead"
    }else{
    return "Woohoo!"
      }
    
    
  
}