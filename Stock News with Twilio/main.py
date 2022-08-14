import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = "XKVF3RRKJD1LOKAP"
NEWS_API_KEY = "6a94e5338935438d978b5b96ff596edc"

url_alpha = "https://www.alphavantage.co/query"
url_news = "https://newsapi.org/v2/everything"

parameters_news = {
    "q": COMPANY_NAME,
    "from": "2022-08-14",
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}
parameters_alpha = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY
}

response = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=XKVF3RRKJD1LOKAP")
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

properties = [{"day": day, "open": report["1. open"], "close": report["4. close"]} for (day, report) in data.items()]

need_checkings = 0
for i in range(99):
    today = float(properties[i]["close"])
    prev = float(properties[i + 1]["close"])
    diff = today - prev
    if ((diff/today) * 100) >= 10 or ((diff/today) * 100) <= -10:
        need_checkings += 1
        # parameters_news["from"] = properties[i]["day"]
        news_response = requests.get(url=url_news, params=parameters_news)
        news_response.raise_for_status()
        top_trending_news = news_response.json()["articles"][:3]
        print(top_trending_news)

print(f"{need_checkings} Days need to be checked")

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

