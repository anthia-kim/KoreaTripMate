# recommender/recommend_model.py
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# 숙소 추천
def get_hotel_recommendations(user_id: int):
    df = pd.read_csv("data/Dataset_Predict_Rating_hotel.csv")
    features = df[['User ID', 'Hotel ID', 'Satisfaction', 'Staff', 'Facilities',
                   'Cleanliness', 'Comfort', 'Value for money', 'Location', 'Free Wifi']]
    labels = df['Ratings']

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(features, labels)

    user_data = df[df['User ID'] == user_id]
    if user_data.empty:
        return []

    user_features = user_data[features.columns]
    predictions = model.predict(user_features)

    top_indices = predictions.argsort()[::-1][:3]
    top_hotels = user_data.iloc[top_indices]['Hotel ID'].tolist()

    return [f"호텔 {hid}" for hid in top_hotels]

# 음식점 추천
def get_restaurant_recommendations(user_id: int):
    df = pd.read_csv("data/Dataset_Predict_Rating_restaurant.csv")
    features = df[['User ID', 'Restaurant Name', 'Food', 'Service', 'Value for money', 'Atmosphere']]
    labels = df['Ratings']

    df['Restaurant Name'] = df['Restaurant Name'].astype('category')
    df['Restaurant Name Code'] = df['Restaurant Name'].cat.codes
    features = features.copy()
    features['Restaurant Name'] = df['Restaurant Name Code']

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(features, labels)

    user_data = df[df['User ID'] == user_id]
    if user_data.empty:
        return []

    user_features = user_data[features.columns]
    predictions = model.predict(user_features)

    top_indices = predictions.argsort()[::-1][:3]
    top_restaurants = user_data.iloc[top_indices]['Restaurant Name'].tolist()

    return top_restaurants  
