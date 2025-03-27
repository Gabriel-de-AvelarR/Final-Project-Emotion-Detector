"""
Flask server for emotion detection application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Configuração do Flask
APP = Flask(
    "Emotion Detector",
    template_folder='./templates',
    static_folder='./static')

@APP.route('/')
def render_home_page():
    """
    Renderiza a página inicial.
    """
    return render_template("index.html")

@APP.route('/emotionDetector')
def sent_detector():
    """
    Processa a análise de emoção do texto fornecido.
    """
    text_to_detect = request.args.get('textToAnalyze', '')

    if not text_to_detect:
        return "Invalid text! Please provide a valid input."

    response = emotion_detector(text_to_detect)

    if not response or response.get('dominant_emotion') is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
