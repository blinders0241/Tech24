import pandas as pd
from bsedata.bse import BSE

b = BSE()
print(dir(b))
print(help(b.getQuote))
url = 'https://www.bseindia.com/stock-share-price/zee-entertainment-enterprises-ltd/zeel/505537/shareholding-pattern/'
html = b.get(url)
print(html)
dfs = pd.read_html(html)

shareholding_pattern_df = dfs[0]

print(shareholding_pattern_df)
