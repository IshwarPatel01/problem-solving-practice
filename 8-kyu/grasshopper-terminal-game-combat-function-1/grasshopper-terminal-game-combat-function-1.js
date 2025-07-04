function combat(health, damage) {
  if(health < damage) return 0
  let result = health - damage
  return result
}