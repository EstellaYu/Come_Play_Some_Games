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

"""-----------------------------------------------------------------------
# a point calculator for a player's hand 
	function 1. inputs the hand of the player, 
 			 2. identify what card is it
 			 3. calculate points
-----------------------------------------------------------------------"""
def pt_calculator(hand):
	pt = []
	ace = False

	for i in range(len(hand)):
		pt_temp = hand[i][1:] # order of the 1st card
	
		if pt_temp in ['J','Q','K']:
			pt_temp = 10
		elif pt_temp == 'A':
			pt_temp = 1
			ace = True
		else: 
			pt_temp = int(pt_temp)

		pt.append(pt_temp)

	if ace and (sum(pt) + 10 <= 21):
		return [sum(pt), sum(pt) + 10]
	else: 
		return [sum(pt)]

"""-----------------------------------------------------------------------
# prints the result from the pt_calculator
-----------------------------------------------------------------------"""
def print_pt(pt):
	if len(pt) == 2:
		return str(pt[0]) + " or " + str(pt[1])
	else:
		return str(pt[0])
