import os, requests, feedparser

TICKERS = ["VWRP.L","GCTS","CMPS","AAPL"]
TOPIC = os.environ["NTFY_TOPIC"]
if not TOPIC:
  raise SystemExit("NTFY_TOPIC is empty: Check the repoo secret name and tab")

lines = []
for t in TICKERS:
  f = feedparser.parse(f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={t}&lang=en-US")
  lines.append(f"\n{t}")
  lines += [f"-{e.title}" for e in f.entries[:5]]

r = requests.post(
  f"https://ntfy.sh/{TOPIC}",
  data="\n".join(lines).encode(),
  headers={"Title": "Equity headlines"},
)
print(len(lines), "lines;", r.status_code, r.text[:200])
r.raise_for_status()
