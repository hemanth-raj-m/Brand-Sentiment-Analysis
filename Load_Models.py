from tensorflow.keras.models import load_model
import pickle


# Load tokenizers
with open("tokenizer_Tamil.pkl", "rb") as f:
    tokenizer_ta = pickle.load(f)

with open("./DL_Model_Kannada/tokenizer_Kannada.pkl", "rb") as f:
    tokenizer_kn = pickle.load(f)

# Load TF-IDF vectorizer for ML models
with open('./ML_Model_Tamil/ML_tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    ml_vectorizer = pickle.load(vectorizer_file)

# Load ML models
# Random Forest
with open('./ML_Model_Tamil/ML_RanFo_classifier.pkl', 'rb') as model_file:
    ml_model_RanFo = pickle.load(model_file)


# XGBoost
with open('./ML_Model_Tamil/ML_XGB_Tamil.pkl', 'rb') as model_file:
    ml_model_Xgb = pickle.load(model_file)

# SVC
with open('./ML_Model_Tamil/ML_SVC_Tamil.pkl', 'rb') as model_file:
    ml_model_SVC = pickle.load(model_file)

# Multinomial Bayes
with open('./ML_Model_Tamil/ML_Mnb_Tamil.pkl', 'rb') as model_file:
    ml_model_Mnb = pickle.load(model_file)


# Load DL models Tamil
dl_model_CNN_ta = load_model("./DL_Model_Tamil/DL_CNN_Tamil.h5")
dl_model_BGRU_ta = load_model("./DL_Model_Tamil/DL_BGRU_Tamil.h5")
dl_model_RNN_ta = load_model("./DL_Model_Tamil/DL_RNN_Tamil.h5")
dl_model_Blstm_ta = load_model("./DL_Model_Tamil/DL_BLstm_Tamil.h5")

# Load DL models Kannada
dl_model_CNN_kn = load_model("./DL_Model_Kannada/DL_BGRU_Kannada.h5")
dl_model_BGRU_kn = load_model("./DL_Model_Kannada/DL_BGRU_Kannada.h5")
dl_model_RNN_kn = load_model("./DL_Model_Kannada/DL_RNN_Kannada.h5")
dl_model_Blstm_kn = load_model("./DL_Model_Kannada/DL_BiLSTM_Kannada.h5")
