
import requests

def get_crop_ai_response(**kwargs):
    """
    Sends a POST request to an external crop prediction service using the data 
    from the frontend. Returns the predicted crop as a string.
    """

    N = kwargs.get('nitrogen', 0)
    P = kwargs.get('phosphorus', 0)
    K = kwargs.get('potassium', 0)
    temperature = kwargs.get('temperature', 0)
    humidity = kwargs.get('humidity', 0)
    pH = kwargs.get('ph', 0)
    rainfall = kwargs.get('rainfall', 0)


    user_id = kwargs.get('user_id', None)


    payload = {
        "data": [N, P, K, temperature, humidity, pH, rainfall]
    }
    print(payload)

    PREDICTION_URL = "https://8519-35-197-98-239.ngrok-free.app/predict"

    try:
        response = requests.post(PREDICTION_URL, json=payload)
        response.raise_for_status()  
        
        result = response.json()
        predicted_crop = result.get("prediction", "Unknown Crop")

        return predicted_crop

    except requests.exceptions.RequestException as e:
        return f"Error in crop prediction request: {e}"


def get_fertilizer_response(**kwargs):
    """
    Sends a POST request to an external fertilizer prediction service using the data 
    from the frontend. Returns the predicted fertilizer recommendation as a string.
    """
    nitrogen = kwargs.get('nitrogen', 0)
    phosphorus = kwargs.get('phosphorus', 0)
    potassium = kwargs.get('potassium', 0)
    temperature = kwargs.get('temperature', 0)
    humidity = kwargs.get('humidity', 0)
    moisture = kwargs.get('moisture', 0)
    crop_type = kwargs.get('crop_type', 0)
    soil_type = kwargs.get('soil_type', 0)

    payload = {
        "data": [nitrogen, phosphorus, potassium, temperature, humidity, moisture, crop_type, soil_type]
    }
    print(f"Payload for fertilizer API: {payload}")

    PREDICTION_URL = "https://633e-34-16-107-213.ngrok-free.app/predict"

    try:
        response = requests.post(PREDICTION_URL, json=payload)
        response.raise_for_status()

        result = response.json()
        predicted_fertilizer = result.get("prediction", "Unknown Recommendation")

        return predicted_fertilizer

    except requests.exceptions.RequestException as e:
        return f"Error in fertilizer prediction request: {e}"
