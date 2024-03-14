import requests
from twilio.rest import Client

CRYPTO_NAME = "bitcoin"
CRYPTO_ENDPOINT = f"https://api.coingecko.com/api/v3/coins/{CRYPTO_NAME}"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "Enter_Your_Own"
TWILIO_SID = "Enter_Your_Own"
TWILIO_AUTH_TOKEN = "Enter_Your_Own"
TWILIO_PHONE_NUMBER = "Enter_Your_Own"
RECIPIENT_PHONE_NUMBER = "Enter_Your_Own"

# STEP 1: Retrieve Bitcoin prices and 24-hour change
response = requests.get(CRYPTO_ENDPOINT)
response.raise_for_status()
bitcoin_data = response.json()
bitcoin_price = bitcoin_data["market_data"]["current_price"]["usd"]
price_change_percentage = bitcoin_data["market_data"]["price_change_percentage_24h"]

# Check if price change is greater than 2%
if abs(price_change_percentage) > 2:
    # STEP 2: Retrieve Bitcoin-related news
    parameters = {
        "q": CRYPTO_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]

    # STEP 3: Send news via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # Create a new list of the first 3 articles' headline and URL using list comprehension
    articles = [(article["title"], article["url"]) for article in news_data[:3]]

    # Send each article as a separate message via Twilio
    for article in articles:
        if price_change_percentage > 0.0:
            emoji = "🔼"
            color = "green"
        else:
            emoji = "🔽"
            color = "red"
        message = (
            f"{CRYPTO_NAME.capitalize()}: {'🔼' if price_change_percentage > 0 else '🔽'} {abs(price_change_percentage):.2f}%\n"
            f"Headline: {article[0]}\n"
            f"URL: {article[1]}")
        client.messages.create(
            body=message,
            from_=f"whatsapp:{TWILIO_PHONE_NUMBER}",
            to=f"whatsapp:{RECIPIENT_PHONE_NUMBER}")
