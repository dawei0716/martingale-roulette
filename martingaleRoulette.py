import numpy as np
import matplotlib.pyplot as plt

def martingale(bankroll, baseWager, p, roundLimit, plot = False):
	wager = baseWager
	progress = []
	results = np.random.choice(['Red', 'Black'], p = [p, 1-p], size = roundLimit)
	for result in results:
		if bankroll < wager:
			break
		if result == 'Black':
			bankroll -= wager
			wager *= 1/p
		else:
			bankroll += wager
			wager = baseWager
		progress.append(bankroll)
	if plot == True:
		plt.plot(progress)
		plt.title('Bankroll Over n Number of Rounds Using Martingale Betting Strategy')
		plt.ylabel('Bankroll')
		plt.xlabel('n-th round')
		plt.show()
	return progress

martingale(100,1,.5,100,True)


def simulateMultipleTrial(bankroll, baseWager, p, roundLimit, goal, numTrial):
	numSuccess = 0
	for _ in range(numTrial):
		progress = martingale(bankroll, baseWager, p, roundLimit)
		if max(progress) > goal:
			numSuccess += 1
	successRate = numSuccess/numTrial
	print(f'Simulated martingale system starting with ${bankroll} and base wager of ${baseWager} with {p} chance of winning.\n' +
		f'Out of {numTrial} simulations, {numSuccess} simulations surpassed ${goal} for a successRate of {successRate}')

#Starting with $100, base wager $1, probability of winning: 50%, max 9999 rounds per simulation, test if it reaches $150, simulate 100 times.   
simulateMultipleTrial(100, 1, .5, 9999, 150, 100)









