"""-----------------------------------------------------------------------
# a function 1. inputs num_players, 
 			 2. deals the initial hand for dealer and all players
 			 3. (2 cards for each player (including dealer))
 			 4. (dealer's cards are dealed the last)
-----------------------------------------------------------------------"""
from shuffel_cards import *

def deal_initial_hand(num_players, deck_of_card, draw_ind):
	initial_hand = []
	for player in range(num_players + 1):
		[hand, 
		 deck_of_card, 
		 draw_ind] = hand_of_card(2, deck_of_card, draw_ind)
		initial_hand.append(hand)
	return [initial_hand, deck_of_card, draw_ind]

def initial_pt(initial_hand):
	pt = []
	for i in range(len(initial_hand)):
		pt1 = initial_hand[i][0][1:] # order of the 1st card
		pt2 = initial_hand[i][1][1:] # order of the 2nd card

		if pt1 in ['J','Q','K']:
			pt1 = 10
		else: 
			pt1 = int(pt1)

		if pt2 in ['J','Q','K']:
			pt2 = 10
		else: 
			pt2 = int(pt2)

		pt.append((pt1+pt2))
	return pt
