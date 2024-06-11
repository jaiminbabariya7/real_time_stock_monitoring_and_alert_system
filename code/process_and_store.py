import base64
import json
from google.cloud import firestore

def process_message(event, context):
    db = firestore.Client()
    
    # Decode the Pub/Sub message
    message_data = base64.b64decode(event['data']).decode('utf-8')
    stock_symbol, stock_price = message_data.split(':')
    stock_price = float(stock_price)
    
    # Store the stock price in Firestore
    stock_data = {
        'symbol': stock_symbol,
        'price': stock_price,
        'timestamp': firestore.SERVER_TIMESTAMP
    }
    db.collection('stocks').add(stock_data)
    
    # Check if any alerts are triggered
    alerts = db.collection('alerts').where('stock_symbol', '==', stock_symbol).get()
    
    for alert in alerts:
        alert_data = alert.to_dict()
        if stock_price >= alert_data['threshold']:
            send_alert(alert_data['user_email'], stock_symbol, stock_price)

def send_alert(email, stock_symbol, stock_price):
    # Logic to send an email alert
    print(f"Sending alert to {email}: {stock_symbol} has reached {stock_price}")
