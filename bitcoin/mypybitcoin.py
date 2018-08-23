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
		if not linePresumably[columnNumber] == "Open" and not linePresumably[columnNumber] == "Close":
			justTheOneColumn.append(int(float(linePresumably[columnNumber])))
	return justTheOneColumn


def iKnowYoureNotInLoveWithHimBreakUpWithHim(opens):
	# I'm thinking using the last 10 opens to predict the next day's close
	opens10 = []
	#Make a list of lists (the last 10 opens)
	for i in range(0,len(opens)-20):
		opens10.append(opens[i:i+20])
	return opens10
	
def closeUpShop(closes):
	closes10 = []
	for i in range(19, len(closes)-1):
		closes10.append(closes[i])
	return closes10



if __name__ == "__main__":
	bitcoinMatrix = csv_read("bitcoin.csv")
	opensColumn = column(bitcoinMatrix, 1)
	closesColumn = column(bitcoinMatrix, 4)

	opens10 = iKnowYoureNotInLoveWithHimBreakUpWithHim(opensColumn)
	closes10 = closeUpShop(closesColumn)

	#print(opens10[444])
	#print(closes10[444])

	#print (len(opens10))
	#print(len(closes10))

	clf = svm.SVC(gamma = 0.000001, C=10)

	clf.fit(opens10[:-2], closes10[:-2])

	#print(closes10)
	print("Opens: ")
	print(opens10[-1])

	print("Actual Close: ")
	print(closes10[-1])

	print("Predicted Close:")
	print(clf.predict([opens10[-1]]))







# digits = datasets.load_digits()

# #print(digits.data)

# #print(digits.target)

# clf = svm.SVC(gamma=0.001, C=100)
# X,y = digits.data[:-10], digits.target[:-10]


# print(X[1757])
# print(y[1757])

# #print(len(X))

# #plt.imshow(digits.images[1757], cmap=plt.cm.gray_r, interpolation='nearest')
# #plt.show()

# clf.fit(X,y)

# print(clf.predict([digits.data[-5]]))
# plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation='nearest')
# plt.show()