from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    emotional_score = emotion_detector(text_to_analyze)
    return f"For the given statement, the system response is 'anger': {emotional_score["anger"]}, \
            'disgust': {emotional_score["disgust"]}, 'fear': {emotional_score["fear"]}, \
            'joy': {emotional_score["joy"]} and 'sadness': {emotional_score["sadness"]}. \
            The dominant emotion is {emotional_score["dominant_emotion"]}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)    