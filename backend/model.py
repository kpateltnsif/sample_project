import torch
import numpy as np
import os
import joblib

# Paths
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, '../model/multi_linear_model.pkl')

# Load everything from the single .pkl file
data = joblib.load(MODEL_PATH)

INPUT_DIM = data['input_dim']
scaler_X = data['scaler_X']
scaler_y = data['scaler_y']
state_dict = data['model_state_dict']

# Define the same PyTorch model
class MultiLinearRegression(torch.nn.Module):
    def __init__(self, input_dim, output_dim=1):
        super(MultiLinearRegression, self).__init__()
        self.linear = torch.nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.linear(x)

# Load model
model = MultiLinearRegression(INPUT_DIM)
model.load_state_dict(state_dict)
model.eval()

# Prediction function
def predict(features: list):
    """
    Predict Performance Index
    :param features: list of 5 numeric values
    :return: predicted Performance Index (float)
    """
    X = np.array(features).reshape(1, -1)
    X_scaled = scaler_X.transform(X)
    X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
    
    with torch.no_grad():
        y_scaled = model(X_tensor).numpy()
    
    y_pred = scaler_y.inverse_transform(y_scaled)
    return float(y_pred[0][0])
