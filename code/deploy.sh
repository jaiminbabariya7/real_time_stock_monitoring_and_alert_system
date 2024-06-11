gcloud functions deploy fetch_prices --runtime python39 --trigger-topic <your-topic> --set-env-vars STOCK_API_KEY=<your-api-key>,GCP_PROJECT_ID=<your-project-id>,PUBSUB_TOPIC_ID=<your-topic-id>

gcloud functions deploy process_and_store --runtime python39 --trigger-topic <your-topic> --set-env-vars GCP_PROJECT_ID=<your-project-id>
