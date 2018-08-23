import quandl
import pandas
import matplotlib.pyplot as plt

auth_tok = "L-pbw1X7QL9tTMZ9s2xr"
data = quandl.get("BNC3/GWA_BTC", authtoken=auth_tok)

data["GWA_BTC"] = data["Close"]

df = pandas.DataFrame()
df = pandas.concat([df, data])

df.to_csv("bitcoin.csv")
#print(data)

plt.plot(data["Close"])
plt.show()