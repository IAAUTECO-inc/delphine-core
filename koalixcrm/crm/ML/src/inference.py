import numpy as np

class DummyModel:
    def predict(self, data):
        """
        A dummy model that returns a random prediction.
        """
        return np.random.rand(len(data))

def load_model(model_path):
    """
    Loads a model from the given path.
    In a real-world scenario, this function would load a trained model from a file.
    For this example, we will just return a dummy model.
    """
    print(f"Loading model from {model_path}")
    return DummyModel()

def make_prediction(model, data):
    """
    Makes a prediction using the given model and data.
    """
    # Input validation
    if not isinstance(data, np.ndarray):
        raise ValueError("Input data must be a numpy array")

    prediction = model.predict(data)
    return prediction

if __name__ == '__main__':
    # Example usage
    model = load_model("models/dummy_model.pkl")
    data = np.array([[1, 2, 3], [4, 5, 6]])
    prediction = make_prediction(model, data)
    print(f"Prediction: {prediction}")
