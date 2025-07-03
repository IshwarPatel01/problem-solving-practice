function  calculateAge(b,y) {  
  if (b - y === 1) return `You will be born in 1 year.`
  if(y-b === 1) return `You are 1 year old.`
  if(b > y) return `You will be born in ${b- y} years.`
  if(y > b) return `You are ${y-b} years old.`
  if(y === b) return `You were born this very year!`
}
​
​