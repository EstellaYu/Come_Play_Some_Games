"""--------------------------------------------------------------------
# function returns "num_deck" decks of card
--------------------------------------------------------------------"""
def cards(num_deck):
	cards = range(51)
	# spade, heart, club, diamond
	suit = ["\u2660", "\u2665","\u2663", "\u2666"]
	card_order = ["A", "2", "3", "4", "5", "6", "7", 
				  "8", "9", "10", "J", "Q", "K"]

	cards = []
	for deck in range(num_deck):
		for suit_ind in range(4):
			for order_ind in range(13):
				cards.append(suit[suit_ind] + card_order[order_ind])
	return cards



import random
"""--------------------------------------------------------------------
# function returning shuffeled hands
  draw_ind: start drawing from this location 
			(convenient for drawing multiple hands in the same deck)
--------------------------------------------------------------------"""
def hand_of_card(num_cards, deck_of_card, draw_ind):
	hand_of_card = []

	for i in range(draw_ind, draw_ind + num_cards):
		num = random.randrange(i,len(deck_of_card))
		
		hand_of_card.append(deck_of_card[num])

		# switch the chosen card
		temp = deck_of_card[i]
		deck_of_card[i] = deck_of_card[num]
		deck_of_card[num] = temp

	return [hand_of_card , deck_of_card, draw_ind + num_cards]

"""--------------------------------------------------------------------
# function draw one card for a player
  draw_ind: start drawing from this location 
			(convenient for drawing multiple hands in the same deck)
--------------------------------------------------------------------"""
def hit_one_card(deck_of_card, draw_ind):
	num = random.randrange(draw_ind,len(deck_of_card))

	# switch the chosen card
	temp = deck_of_card[draw_ind]
	deck_of_card[draw_ind] = deck_of_card[num]
	deck_of_card[num] = temp

	return [deck_of_card[draw_ind], deck_of_card, draw_ind + 1]






