+-----------------------+      +-----------------------+       +------------------------+
|                       |      |                       |       |                        |
|   User Interface      |      |   Google Cloud        |       |   Notification Service |
|   (Web Application)   |      |   Functions           |       |                        |
|                       |      |                       |       |                        |
+-----------------------+      +-----------------------+       +------------------------+
         |                             |                              |
         |                             |                              |
         +-----------------------------|------------------------------+
                                       |
                                       |
                                       v
                            +-----------------------+
                            |                       |
                            |   Google Cloud        |
                            |   Firestore           |
                            |                       |
                            +-----------------------+



**Workflow Explanation:**

1. **User Interaction**: Users interact with the User Interface (UI) through the web application.
2. **UI Actions**: Users perform actions such as selecting stocks, setting alert thresholds, and viewing stock data.
3. **Google Cloud Functions**:
   - **Fetch Prices Function**: Fetches real-time stock prices and publishes them to Pub/Sub.
   - **Process and Store Function**: Receives stock data from Pub/Sub, processes it, stores it in Firestore, and checks against alert thresholds.
   - **Alert Users Function**: Sends notifications to users based on predefined thresholds.
4. **Data Storage**: Stock data and user preferences are stored in Google Cloud Firestore.
5. **Notification Service**: Sends alerts to users via email, SMS, or push notifications based on the triggers from the Process and Store Function.

This Markdown code provides an explanation of the workflow depicted in the diagram, detailing the steps involved in the stock monitoring system's operation, from user interaction to data processing and notification delivery.
