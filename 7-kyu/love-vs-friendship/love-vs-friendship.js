 
function wordsToMarks(string){
  //your code here
  let total = 0
  
  for(let i = 0; i < string.length; i++){
    total += (string[i].charCodeAt() - 96)
  
  }
  return total
}