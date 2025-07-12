 
function adjacentElementsProduct(arr) {
  let total =  arr[0] * arr[1];
  
  for(let i = 1; i < arr.length; i++){
    let product = arr[i - 1] * arr[i]
    if(total < product){
      total = product
    }
  }
  return total
  
}