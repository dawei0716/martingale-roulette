import numpy as np
import matplotlib.pyplot as plt


class Martingale:
	def __init__(self, bankroll, BaseWager, prob):
		self.bankroll = bankroll
		self.prob = prob
		self.BaseWager = BaseWager
		self.progress = [bankroll]

	def simulateGame(self):
		wager = self.BaseWager
		while self.bankroll > wager:
			result = np.random.choice(['Red', 'Black'], p = [self.prob, 1- self.prob])
			#Assumes that the house does not have an edge (returns exactly 2x on 50% win).
			if(result == 'Black'):
				self.bankroll -= wager
				wager *= 1/(self.prob)
			else: 
				self.bankroll += wager
				wager = self.BaseWager
			self.progress.append(self.bankroll)

	def linePlot(self):
		plt.plot(self.progress)
		plt.title('Bankroll Over n Number of Rounds Using Martingale Betting Strategy')
		plt.ylabel('Bankroll')
		plt.xlabel('n-th round')
		plt.show()


gambler = Martingale(100, 1, .5) #starting with $100, waging $1 as base. 50% win rate.  
gambler.simulateGame()
print(gambler.progress)
gambler.linePlot()

















