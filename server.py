import random

class Cards(object):
	def __init__(self, suit = None, value = None):
		# suit = ["diamonds", "spades", "hearts", "clubs"]
		# value = ["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]
		self.suit = suit
		self.value = value
		
	def show(self):
		print self.suit, self.value
		



class Deck(object):
	def __init__(self):
		self.deck = []
		self.build()

	def build(self):
		suit = ["diamonds", "spades", "hearts", "clubs"]
		value = ["ace","2","3","4","5","6","7","8","9","10","jack","queen","king"]
		for i in suit:
			for k in value:
				card1 = Cards(i, k)
				self.deck.append(card1)
			
	def shuffle(self):
		random.shuffle(self.deck)
		return self

	def show(self):
		 for card in self.deck:
		 	card.show()

	def deal(self):
		return self.deck.pop()

	# def takeback(self, ):
	# 	self.deck.instert(0, )



class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []

	def currentHand(self):
		for card in self.hand:
			card.show()

	def draw(self, deck, number = 1):
		for i in range(0,number):
			self.hand.append(deck.deal())


	# def discard():
	# 	return self.hand.pop()
	# def discard():



	# def show():		

deck1 = Deck()
deck1.shuffle()
player1 = Player("bob")
player1.draw(deck1, 2)
player1.currentHand()









