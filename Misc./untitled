import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
import csv

def csv_read(filename):
	with open(filename, 'r') as f:
		reader = csv.reader(f)
		matrix = list(reader)
	return matrix

def column(matrix, columnNumber):
	justTheOneColumn = []
	for linePresumably in matrix:
		if not linePresumably[columnNumber] == "ACE" and not linePresumably[columnNumber] == "ABC":
			justTheOneColumn.append(int(float(linePresumably[columnNumber])))
	return justTheOneColumn


def iKnowYoureNotInLoveWithHimBreakUpWithHim(opens, pricesPast10, pricesNextDay):
	# I'm thinking using the last 10 opens to predict the next day's close
	# pricesPast10 = []
	# pricesNextDay = []
	#Make a list of lists (the last 10 opens)
	for i in range(0,len(opens)-11):
		pricesPast10.append(opens[i:i+10])
		pricesNextDay.append(opens[i+11])
	return [pricesPast10, pricesNextDay]


if __name__ == "__main__":
	bitcoinMatrix = csv_read("./test/stock_prices.csv")
	pricesColumn = column(bitcoinMatrix, 2)
	#closesColumn = column(bitcoinMatrix, 4)
	thisArrayProbablyWontWork = iKnowYoureNotInLoveWithHimBreakUpWithHim(pricesColumn, [], [])
	pricesColumn = column(bitcoinMatrix, 3)
	thisArrayProbablyWontWork = iKnowYoureNotInLoveWithHimBreakUpWithHim(pricesColumn, thisArrayProbablyWontWork[0], thisArrayProbablyWontWork[1])

	pricesPast10 = thisArrayProbablyWontWork[0]
	pricesNextDay = thisArrayProbablyWontWork[1]


	#############For testing purposes###############
	# pricesPast10.append([26.11,25.97,24.9,24.02,24.41,24.25,24.07,24.07,24.03,24.77])
	# pricesNextDay.append([26.19])

	clf = svm.SVC(gamma = 0.00001, C=100)

	clf.fit(pricesPast10[:-2], pricesNextDay[:-2])

	#print(closes10)
	print("Opens: ")
	print(pricesPast10[-1])

	print("Actual Close: ")
	print(pricesNextDay[-1])

	print("Predicted Close:")
	print(clf.predict([pricesPast10[-1]]))




