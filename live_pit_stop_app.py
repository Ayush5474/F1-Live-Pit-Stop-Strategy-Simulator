# live_pit_stop_app.py

import streamlit as st
import pandas as pd
import numpy as np
import time
from sklearn.ensemble import RandomForestClassifier

# -------------------
# 1. Sample dataset
# -------------------
data = pd.DataFrame({
    'Track': ['Suzuka', 'Suzuka', 'Bahrain', 'Monaco', 'Monza'],
    'Weather': ['Sunny', 'Cloudy', 'Sunny', 'Sunny', 'Sunny'],
    'Laps': [58, 71, 72, 52, 74],
    'Avg_Tire_Wear': [1.56, 1.94, 2.10, 1.90, 1.23],
    'Optimal_Strategy': [
        '1-stop (Soft→Hard)',
        '2-stop (Soft→Medium→Hard)',
        '2-stop (Soft→Medium→Hard)',
        '1-stop (Soft→Hard)',
        '2-stop (Soft→Medium→Hard)'
    ]
})

# Preprocessing
X = pd.get_dummies(data[['Track', 'Weather', 'Laps', 'Avg_Tire_Wear']])
y = data['Optimal_Strategy']

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# -------------------
# 2. Streamlit UI
# -------------------
st.title("🚦 Live Pit Stop Strategy Simulator")

track_input = st.selectbox("Track", data['Track'].unique())
weather_input = st.selectbox("Weather", data['Weather'].unique())
laps_input = st.number_input("Total Laps", min_value=1, value=50)
avg_wear_input = st.number_input("Starting Avg Tire Wear", min_value=0.1, value=1.5, step=0.1)

st.write("Simulating live tire wear updates...")

# Placeholder for live output
strategy_placeholder = st.empty()
lap_placeholder = st.empty()

# -------------------
# 3. Live Simulation Loop
# -------------------
current_wear = avg_wear_input
for lap in range(1, laps_input + 1):
    time.sleep(0.5)  # simulate real-time update every 0.5 seconds
    
    # Simulate tire wear increase
    current_wear += np.random.uniform(0.01, 0.05)
    
    # Prepare input for model
    input_df = pd.DataFrame({
        'Laps': [laps_input],
        'Avg_Tire_Wear': [current_wear],
        'Track_' + track_input: [1],
        'Weather_' + weather_input: [1]
    })
    # Fill missing columns
    for col in X.columns:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[X.columns]
    
    # Predict strategy
    prediction = model.predict(input_df)
    
    # Update Streamlit live
    lap_placeholder.metric(label="Current Lap", value=lap)
    strategy_placeholder.metric(label="Predicted Strategy", value=prediction[0])
