#so its stone paper and scissor


# inp=input("choose rock, paper or scissor")
# rock="a"
# paper="b"
# scissor="c"

# def game():







    
import random

c=random.choice([1,0,-1])
youstr=input("enter rock, paper, scissor ")
youdict={"r":1, "p" :-1, "s":0}
reversedict = {1:"rock", 0:"scissor", -1:"paper"}

y=youdict[youstr]

print(f"you chose {reversedict[y]}\ncomputer choose {reversedict[c]}")
if c==1 and y==1:
    print("tie")

if c==1 and y==0:
    print("you lose")

if c==1 and y==(-1):
    print("you win")

if c==(-1) and y==1:
    print("you lose")

if c==(-1) and y==0:
    print("you lose")

if c==(-1) and y==(-1):
    print("tie")

if c==0 and y==1:
    print("you win")

if c==0 and y==0:
    print("tie")

if c==0 and y==(-1):
    print("you lose")



