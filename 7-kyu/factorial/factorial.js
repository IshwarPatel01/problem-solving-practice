 
function factorial(n)
{
  if (n < 0 || n > 12) {
    throw new RangeError("The argument must be between 1 and 12.")
  }
  
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n-1);
  }
}