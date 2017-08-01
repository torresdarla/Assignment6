#Programmed by Darla Torres
#August 1, 2017

#This program creates a deck of cards, shuffles them "perfectly," and then deals out the first five
import Short
import random

ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

#This function builds the deck of 52 cards
def buildDeck(rank, suit):
    deck = [rank + " of "+ suit for suit in suits for rank in ranks]
    return deck
 
#This function divides the deck into two halves, shuffles the two halves, and then weaves them in together one from each half at a time in order to ensure a "perfect" shuffle   
def shuffle(deck):
    leftHalf = deck [:26]
    rightHalf = deck [26:]
    for i in range (0,51):
        if i%2 == 0:
            deck[i] = leftHalf[i/2]
        else:
            deck[i] = rightHalf[i/2]
    return deck
    

#This function deals the first five cards of the deck
def deal(deck):
    print deck [0:5]
    

#This is the main function that performs all previous functions + asks the user how many times they would like the deck to be shuffled
    
def main():
    deck = buildDeck(ranks,suits)
    num = Short.userInt("How many times do you want me to shuffle?")
    while num > 0:
        deck = shuffle(deck)
        num = num - 1
    deal(deck)
    
    

main()

    
    