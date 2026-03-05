import requests

query=input("What type of news are u interested today?")
api="9f3490a1215b429e8f7e0e32304f9693"
url=f"https://newsapi.org/v2/everything?q={query}&from=2026-03-01&to=2026-03-01&sortBy=popularity&apiKey={api}"
print(url)

r=requests.get(url)

data = r.json()
articles=data["articles"]
for index,article in enumerate(articles):
    print(index + 1, article["title"],article["url"])
    print("\n*************************\n")