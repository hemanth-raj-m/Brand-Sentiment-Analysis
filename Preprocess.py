import nltk
from nltk.tokenize import word_tokenize
import re
from Words_Filters import tamil_stopwords, Additional_Aspects_Filter_tamil, kannada_stopwords, Additional_Aspects_Filter_kannada


# Tokenize sentences into words after basic NLP pre-processing
def preprocess_text_ta(text):
    text = re.sub(r'[^\u0B80-\u0BFF\s]', '', text.lower())  # Include Tamil Unicode range
    tokens = nltk.word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in tamil_stopwords]
    return filtered_tokens

def preprocess_text_kn(text):
    text = re.sub(r'[^\u0C80-\u0CFF\s]', '', text.lower())  # Include Kannada Unicode range
    tokens = nltk.word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in kannada_stopwords]
    return filtered_tokens

# Extract Aspects for Tamil
#def extract_aspects_ta(text):
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in tamil_stopwords]
    pos_tags = nltk.pos_tag(tokens)
    aspects = [token for token, pos in pos_tags if pos in ['NN', 'NNS'] and token not in Additional_Aspects_Filter_tamil]
    return aspects

# Extract Aspects for Kannada
#def extract_aspects_kn(text):
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in kannada_stopwords]
    pos_tags = nltk.pos_tag(tokens)
    aspects = [token for token, pos in pos_tags if pos in ['NN', 'NNS'] and token not in Additional_Aspects_Filter_kannada]
    return aspects

def extract_aspects_ta(text):
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in tamil_stopwords and token not in Additional_Aspects_Filter_tamil]
    return tokens  # Skip POS tagging

def extract_aspects_kn(text):
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in kannada_stopwords and token not in Additional_Aspects_Filter_kannada]
    return tokens  # Skip POS tagging
