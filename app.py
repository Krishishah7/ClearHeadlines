from flask import Flask, render_template, request
import pickle

# Load model and vectorizer
vectorizer = pickle.load(open('model/vector.pkl', 'rb'))
model = pickle.load(open('model/pac.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def clean_text(text):
    return text.lower()

@app.route('/predict', methods=['POST'])
def predict():
    news_title = request.form.get('news_title', '').strip()

    if not news_title:
        return render_template('index.html', prediction="EMPTY", input_text='')
    
    cleaned_title = clean_text(news_title)
    transformed = vectorizer.transform([cleaned_title])
    prediction = model.predict(transformed)

    result = "FAKE" if prediction[0] == 1 else "REAL"
    return render_template('index.html', prediction=result, input_text=news_title)

# About Project
@app.route("/aboutProject")
def aboutProject():
    return render_template("aboutProject.html")

# Contact Us
@app.route("/contactUs")
def contactUs():
    return render_template("contactUs.html")

if __name__ == '__main__':
    app.run(debug=True)