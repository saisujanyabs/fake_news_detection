from flask import Flask, render_template, request
from model import predict_news

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news = request.form['news']
        prediction = predict_news(news)
        return render_template('result.html', news=news, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
