import joblib
import numpy as np

# Load the trained model
model = joblib.load("model/model.pkl")

def predict_parkinsons(age, heart_rate, emg, mems):
    input_data = np.array([[age, heart_rate, emg, mems]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        return "Parkinson's Disease Detected"
    else:
        return "No Parkinson's Disease Detected"

# Example
if __name__ == "__main__":
    result = predict_parkinsons(65, 95, 120, 80)
    print(result)
