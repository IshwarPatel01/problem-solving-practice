function noOdds( values ){
  // Return all non-odd values
  let arr = []
  for (item of values){
    if(item % 2 === 0){
      arr.push(item)
      
    }
  
  }
  
  return arr
}