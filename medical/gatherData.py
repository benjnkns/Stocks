import pandas as pd
import os
import quandl
import time

auth_tok = "L-pbw1X7QL9tTMZ9s2xr"
path = "./MedicalStocks"
def Stock_Prices():
	df = pd.DataFrame()
	statspath = path #+"/_KeyStats"
	#print (statspath)
	stock_list = [x[0] for x in os.walk(statspath)]
	#print(stock_list)
	for each_dir in stock_list[1:100]:
		try:
			ticker = each_dir.split("/")[-1]
			name = "WIKI/"+ticker.upper()
			print(name)
			data = quandl.get(name,
				trim_start = "2000-12-12",
				trim_end = "2014-12-30",
				authtoken=auth_tok)
			data[ticker.upper()] = data["Adj. Close"]
			#print (df)
			#print(data[ticker.upper()])
			df = pd.concat([df, data[ticker.upper()]], axis = 1)
		except Exception as e:
			print(str(e))
			time.sleep(10)
			try:
				ticker = each_dir.split("/")[-1]
				print(ticker)
				name = "WIKI/"+ticker.upper()
				data = quandl.get(name,
					trim_start = "2000-12-12",
					trim_end = "2014-12-30",
					authtoken=auth_tok)
				data[ticker.upper()] = data["Adj. Close"]
				df = pd.concat([df, data[ticker.upper()]], axis = 1)
			except Exception as e:
				print(str(e))
	df.to_csv("medical_stock_prices.csv")
                

if __name__ == "__main__":
	Stock_Prices()





#data = quandl.get("WIKI/KO", trim_start = "2000-12-12", trim_end = "2014-12-30", authtoken=auth_tok)

#print(data)
