from django.shortcuts import render, redirect

import json
import joblib
import contractions
import pandas
from nltk.corpus import stopwords
from nltk import word_tokenize, sent_tokenize
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_df=1200, min_df=2, max_features=10000, ngram_range=(1,2))
model = joblib.load('model/modelo_random_forest.joblib')

def process_text(text):

    text.replace('[^a-zA-Z ]', '')
    text.lower()

    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stop words
    stop_words = stopwords.words('english')
    tokens = [token for token in tokens if token not in stop_words]

    # Stemming
    stemmer = LancasterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Join tokens
    text = ' '.join(tokens)

    return text

def vectorize_text(text):
    tokens = {}

    # For each unique word in the text, create a dict with the word as key and the word count as value
    for word in text.split():
        if word in tokens:
            tokens[word] += 1
        else:
            tokens[word] = 1

    # Create dataframe with the tokens dict
    df = pandas.DataFrame([tokens])
    return df

def home(request):
    return render(request, 'home.html')

def predict(request):

    if request.method == 'POST':
        probabilidad = 0
        prediccion = 0

        # Obtener los datos del formulario
        text = request.POST['mensaje_para_prediccion']
        text = process_text(text)

        try:

            # Vectorizar el texto
            text_vectorized = vectorize_text(text)

            prediccion = model.predict(text_vectorized)
            probabilidad = model.predict_proba(text_vectorized)
            return redirect('showPrediction', prediccion, probabilidad)
        except Exception as e:
            return redirect('error', e)

    return render(request, 'predict.html')

def error(request, error):
    return render(request, 'error.html', {'error': error})

def showPrediction(request, prediction, probability):

    with open('model\model_metrics.json', 'r') as f:
        model_metrics = json.load(f)

    accuracy = float(model_metrics['accuracy']) * 100
    precision = float(model_metrics['precision']) * 100
    recall = float(model_metrics['recall']) * 100
    f1_score = float(model_metrics['f1']) * 100

    context = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1_score,
        'prediction': prediction,
        'probability': probability
    }
    return render(request, 'show_prediction.html', context)
