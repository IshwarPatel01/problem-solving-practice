 
function findAverage(nums) {
  return nums.reduce((acc,curr) => acc + curr,0) / nums.length
   
  }
​
// var findAverage = function(nums){
//   return nums.reduce((a, b) => a + b, 0) / nums.length;
// }