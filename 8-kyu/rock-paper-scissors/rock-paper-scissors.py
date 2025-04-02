def rps(p1, p2):
    if p2 == "rock" and p1 == "paper" or p1 == "scissors" and p2 == "paper" or p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "scissors" or p1 == "rock" and p2 == "paper" or p2 == "rock" and p1 == "scissors":
        return "Player 2 won!"
    elif p1 == "paper" and p2 =="paper" or p1 == "scissors" and p2 == "scissors" or p1 == "rock" and p2 =="rock":
        return "Draw!"
    #your code here