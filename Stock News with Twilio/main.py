import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_API_KEY = "XKVF3RRKJD1LOKAP"
NEWS_API_KEY = "6a94e5338935438d978b5b96ff596edc"
TWILIO_SID = "ACab739de85430d43382db5b7e6ecaa588"
TWILIO_AUTH = "b3ab0a2f8771d7e3541c931034720c59"
TWILIO_PHONE_NUMBER = "+12537854597"

url_alpha = "https://www.alphavantage.co/query"
url_news = "https://newsapi.org/v2/everything"

parameters_news = {
    "q": COMPANY_NAME,
    "from": "2022-08-14",
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


today = float(properties[0]["close"])
prev = float(properties[1]["close"])
diff = abs(today - prev)
if ((diff/today) * 100) >= 1:
        news_response = requests.get(url=url_news, params=parameters_news)
        news_response.raise_for_status()
        top_trending_articles = news_response.json()["articles"][:3]
        formatted_articles = [f"Headline: {article['title']}. \nBrief:{article['description']}" for article in top_trending_articles]
        client = Client(TWILIO_SID, TWILIO_AUTH)
        for article in formatted_articles:
            message = client.messages.create(
                body=article,
                from=TWILIO_PHONE_NUMBER,
                to="+254719629908")
        print(message.status)


