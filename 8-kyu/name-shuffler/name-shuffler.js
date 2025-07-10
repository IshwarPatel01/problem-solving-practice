function nameShuffler(str){
  let split = str.split(" ")
  let result = ""
  result += split[1] +" " + split[0]
  
  return result
}