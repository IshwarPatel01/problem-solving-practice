 
function abbrevName(name){
  let split = name.split(" ")
  
  let first = split[0].charAt(0).toUpperCase()
  let second = split[1].charAt(0).toUpperCase()
  
  return `${first}.${second}`
  
} 