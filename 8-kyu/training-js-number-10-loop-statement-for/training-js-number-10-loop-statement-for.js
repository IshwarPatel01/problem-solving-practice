 
function pickIt(arr){
  let odd = [], even = [];
  //coding here
  for(item of arr){
    if(item % 2 === 0){
    even.push(item)
    }else{
    odd.push(item)
    }
  }
  
  
  return [odd,even];
}