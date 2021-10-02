from flask import Flask, abort, jsonify, request, render_template,session
import joblib
from feature import get_all_query,remove_punctuation_stopwords_lemma

pipeline = joblib.load('./pipeline.sav')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def predict():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def get_delay():

    result=request.form
    query_title = result['title']
    query_author = result['author']
    query_text = result['maintext']
    print(query_text)
    query = get_all_query(query_title, query_author, query_text)
    pred = pipeline.predict(query)
    return render_template('index.html', msg="success", op=pred)


if __name__ == '__main__':
    app.secret_key = "hai"
    app.run(port=8080, debug=True)
