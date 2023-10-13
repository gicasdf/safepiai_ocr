import os
from keras.models import load_model

#AI 모델 로드를 돕는 모듈
def load_ai_model():
    model_path = os.path.join(os.path.dirname(__file__), 'models', 'ocr_three.py')
    model = load_model(model_path)
    return model

def predict_with_model(model, input_data):
    result = model.predict(input_data)
    return result