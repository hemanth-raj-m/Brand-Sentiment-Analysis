# Import necessary libraries
import gradio as gr
import tensorflow as tf
import nltk
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from Preprocess import preprocess_text_kn,preprocess_text_ta, extract_aspects_kn, extract_aspects_ta
#from Words_Filters import tamil_stopwords, Additional_Aspects_Filter_tamil, kannada_stopwords, Additional_Aspects_Filter_kannada
from Load_Models import tokenizer_ta,tokenizer_kn, ml_vectorizer, ml_model_RanFo,ml_model_Xgb, ml_model_SVC, ml_model_Mnb
from Load_Models import dl_model_CNN_ta, dl_model_BGRU_ta, dl_model_RNN_ta, dl_model_Blstm_ta, dl_model_CNN_kn, dl_model_BGRU_kn, dl_model_RNN_kn, dl_model_Blstm_kn
# Download necessary NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
#nltk.download('averaged_perceptron_tagger_eng')

# Define function to predict sentiment using DL model for Tamil
def predict_dl_sentiment_ta(text, model_name):
    tam_pre = preprocess_text_ta(text)
    padded_text = pad_sequences(tokenizer_ta.texts_to_sequences([tam_pre]), maxlen=100)
    if model_name == 'CNN':
        prediction = dl_model_CNN_ta.predict(padded_text)
    elif model_name == 'BGRU':
        prediction = dl_model_BGRU_ta.predict(padded_text)
    elif model_name == 'RNN':
        prediction = dl_model_RNN_ta.predict(padded_text)
    elif model_name == 'BLSTM':
        prediction = dl_model_Blstm_ta.predict(padded_text)
    sentiment_label = np.argmax(prediction)
    return sentiment_label

# Define function to predict sentiment using DL model for Kannada
def predict_dl_sentiment_kn(text, model_name):
    kan_pre = preprocess_text_kn(text)
    padded_text = pad_sequences(tokenizer_kn.texts_to_sequences([kan_pre]), maxlen=100)
    if model_name == 'CNN_kn':
        prediction = dl_model_CNN_kn.predict(padded_text)
    elif model_name == 'BGRU_kn':
        prediction = dl_model_BGRU_kn.predict(padded_text)
    elif model_name == 'RNN_kn':
        prediction = dl_model_RNN_kn.predict(padded_text)
    elif model_name == 'BLSTM_kn':
        prediction = dl_model_Blstm_kn.predict(padded_text)
    sentiment_label = np.argmax(prediction)
    return sentiment_label

# Define function to predict sentiment using ML model
def predict_ml_sentiment(text, model_name):
    review_tfidf = ml_vectorizer.transform([text])
    if model_name == 'Random Forest':
        sentiment_pred = ml_model_RanFo.predict(review_tfidf.toarray())
    elif model_name == 'XGBoost':
        sentiment_pred = ml_model_Xgb.predict(review_tfidf.toarray())
    elif model_name == 'SVC':
        sentiment_pred = ml_model_SVC.predict(review_tfidf.toarray())
    elif model_name == 'MNB':
        sentiment_pred = ml_model_Mnb.fit(review_tfidf, ml_model_Mnb_y).predict(review_tfidf)
    return sentiment_pred[0]

# Define function to convert sentiment label to string
def label_to_sentiment(sentiment_label):
    if sentiment_label == 0:
        return "negative"
    elif sentiment_label == 1:
        return "neutral"
    elif sentiment_label == 2:
        return "positive"
    else:
        return "unknown"

# Create Gradio interface
def predict_sentiment(input_sentence, model_type, model_name):
    if 'kn' in model_name:
        if model_type == 'DL':
            sentiment_label = predict_dl_sentiment_kn(input_sentence, model_name)
        elif model_type == 'ML':
            sentiment_label = predict_ml_sentiment(input_sentence, model_name)
    else:
        if model_type == 'DL':
            sentiment_label = predict_dl_sentiment_ta(input_sentence, model_name)
        elif model_type == 'ML':
            sentiment_label = predict_ml_sentiment(input_sentence, model_name)
    sentiment = label_to_sentiment(sentiment_label)
    return sentiment

def extract_aspects(input_sentence, model_name):
    if 'kn' in model_name:
        aspects = extract_aspects_kn(input_sentence)
    else:
        aspects = extract_aspects_ta(input_sentence)
    print("Extracted Aspects:", aspects)
    return ', '.join(aspects)


def combined_predict(input_sentence, model_type, model_name):
    aspects = extract_aspects(input_sentence, model_name)
    sentiment = predict_sentiment(input_sentence, model_type, model_name)
    return sentiment, aspects

iface = gr.Interface(
    fn=combined_predict,
    inputs=[
        "text",
        gr.Dropdown(choices=['DL', 'ML'], label="Model Type"),
        gr.Dropdown(choices=['CNN', 'BGRU', 'RNN', 'BLSTM', 'Random Forest', 'XGBoost', 'SVC',# 'MNB',
                             'CNN_kn', 'BGRU_kn', 'RNN_kn', 'BLSTM_kn'], label="Model")
    ],
    outputs=[
        "text",#sentiment output
        "text"# aspects output
    ],
    title="Sentiment Prediction with Aspects",
    description="Enter a sentence in Tamil or Kannada and get the predicted sentiment (negative, neutral, or positive) along with aspects extracted."
)

iface.launch()

