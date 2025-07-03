function sumOfDifferences(arr) {
  let result = 0
  
  let sorted = arr.sort((a,b) => b - a)
  
  for (let i = 1; i <= sorted.length - 1; i++){
    result +=( sorted[i -1] - sorted[i])
  }
  return result
}