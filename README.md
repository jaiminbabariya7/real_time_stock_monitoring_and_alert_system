[User Interface] <--> [Firestore (User Data)]
                              |
[Stock API] --> [Cloud Function (Fetch Prices)] --> [Pub/Sub Topic] --> [Cloud Function (Process and Store)]
                                                                     |
                                                                     v
                                                            [Firestore (Historical Data)]
                                                                     |
                                                           [Cloud Function (Alert Users)]
                                                                     |
                                                            [Notification Service]
