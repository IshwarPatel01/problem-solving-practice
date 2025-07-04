 
function include(arr, item){
  let result = false
  for (value of arr){
    if(value === item) {
    result = true
    }
  }
  return result
}