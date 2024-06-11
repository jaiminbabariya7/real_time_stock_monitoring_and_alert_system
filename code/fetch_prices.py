import requests
import os
from google.cloud import pubsub_v1

# Fetch stock prices from a third-party API
def fetch_stock_prices():
    api_key = os.getenv('STOCK_API_KEY')
    stock_symbols = ['AAPL', 'GOOGL', 'MSFT']
    prices = {}
    
    for symbol in stock_symbols:
        response = requests.get(f'https://api.example.com/quote?symbol={symbol}&apikey={api_key}')
        data = response.json()
        prices[symbol] = data['price']
    
    return prices

# Publish stock prices to Pub/Sub
def publish_prices_to_pubsub(prices):
    project_id = os.getenv('GCP_PROJECT_ID')
    topic_id = os.getenv('PUBSUB_TOPIC_ID')
    
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    
    for symbol, price in prices.items():
        message = f"{symbol}:{price}"
        publisher.publish(topic_path, message.encode('utf-8'))

def main(event, context):
    prices = fetch_stock_prices()
    publish_prices_to_pubsub(prices)
