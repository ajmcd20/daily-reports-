import os, requests, feedparser

TICKERS = ["VWRP","GCTS","RPIL"]
TOPIC = os.environ["NFTY_TOPIC"]

lines = []
for t in TICKERS:
  f = feedparser.parse(f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={t}&lang=en-US")
  lines.append(f"\n{t}")
  lines += [f"-{e.title}" for e in f.entries[:5]]

requests.post(
  f"https://nfty.sh/{TOPIC}",
  data="\n".join(lines).encode(),
  headers={"Title": "Equity headlines"},
)
