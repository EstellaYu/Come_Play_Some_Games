from shuffel_cards import *
from deal_initial_hand import *

cards = cards(1)
[initial_hand, card, draw_ind] = deal_initial_hand(2, cards, 0)
print("Dealer's hand: [{}] {}".format(print_pt(pt_calculator(initial_hand[-1])),
									  initial_hand[-1]))
print("Your card: [{}] {}".format(print_pt(pt_calculator(initial_hand[0])),
								initial_hand[0]))
print("")


"""--------------------------------------------------------------------
	Player choosing hit/stay
--------------------------------------------------------------------"""
hit_stay = input("take another card? [y/n] ")

while (hit_stay == 'y' and min(pt_calculator(initial_hand[0]) <= 21)):
	[new_card, cards, draw_ind] = hit_one_card(cards, draw_ind)
	initial_hand[0].append(new_card)

	print("Your card: [{}] {}".format(print_pt(pt_calculator(initial_hand[0])),
									  initial_hand[0]))

	if pt_calculator(initial_hand[0]) <= 21:
		hit_stay = input("take another card? [y/n] ")

"""--------------------------------------------------------------------
	Dealer's turn
--------------------------------------------------------------------"""

while (max(pt_calculator(initial_hand[-1])) < 16):
	[new_card, cards, draw_ind] = hit_one_card(cards, draw_ind)
	initial_hand[-1].append(new_card)

	
if min(pt_calculator(initial_hand[0])) > 21:
	print("\nYou busted!")

print("Dealer's hand: [{}] {}".format(print_pt(pt_calculator(initial_hand[-1])),
									  initial_hand[-1]))
print("Your card: [{}] {}".format(print_pt(pt_calculator(initial_hand[0])),
								initial_hand[0]))
print("")

