 
function evenNumbers(array, number) {
  let result = [] 
  
  for(let i = array.length - 1; i >= 0; i--){
    let num = array[i]  
    if(num % 2 === 0){
      
        result.push(num)
      }
    if(result.length === number) break
      
  }
    
  
  
  return result.reverse()
}