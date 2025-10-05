# 🏎️ Live Pit Stop Strategy Simulator  

**Live Pit Stop Strategy Simulator** is an interactive **Streamlit app** that simulates Formula 1 pit stop strategies in real-time.  
It uses a **Random Forest model** trained on a sample dataset of tracks, weather, laps, and tire wear to predict the **optimal pit stop strategy** as the race unfolds.  

---

## 🚦 Features  

- **Live Race Simulation**  
  - Updates lap-by-lap with increasing tire wear.  
  - Shows current lap and predicted strategy in real-time.  

- **Machine Learning Strategy Predictor**  
  - Trained on synthetic F1 strategy dataset (tracks, weather, tire wear).  
  - Predicts strategies like:  
    - `1-stop (Soft→Hard)`  
    - `2-stop (Soft→Medium→Hard)`  

- **Interactive Dashboard**  
  - Choose track, weather, total laps, and initial tire wear.  
  - Watch the simulation update dynamically every 0.5 seconds.  

---

## 🧠 How It Works  

1. **Sample Dataset**  
   - A small dataset is defined with tracks (Suzuka, Monaco, Monza, etc.),  
     weather conditions, average tire wear, laps, and optimal strategies.  

2. **Model Training**  
   - Features are encoded using `pd.get_dummies`.  
   - A `RandomForestClassifier` is trained to classify optimal strategy.  

3. **Live Simulation**  
   - Each lap, tire wear increases randomly (`+0.01` to `+0.05`).  
   - The trained model predicts the best strategy based on updated wear.  
   - Results are shown with Streamlit’s **metric cards**.  

---

## 🛠️ Tech Stack  

- **Frontend/UI**: Streamlit  
- **Backend/ML**: Scikit-learn (Random Forest Classifier)  
- **Data Simulation**: Python (Numpy, Pandas)  
- **Live Updates**: Python `time.sleep` + Streamlit placeholders  

---

## 📌 Notes  

- ⚠️ The dataset is **very small and synthetic** → for demonstration purposes only.  
- 📊 With a larger dataset (historical F1 telemetry/strategies), this can be made more realistic.  
- 🎯 Great example of combining **real-time simulation + ML + interactive dashboards**.  
 

