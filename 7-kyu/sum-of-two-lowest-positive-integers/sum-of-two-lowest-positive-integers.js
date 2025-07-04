function sumTwoSmallestNumbers(numbers) {  
  let sorted =  numbers.sort((a,b) => a - b)
  let result = sorted[0] + sorted[1]
  return result
  
  }