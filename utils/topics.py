# pip install gensim nltk pandas matplotlib

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim import corpora
from gensim.models import LdaModel
import matplotlib.pyplot as plt
from read import read_pdf

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

data = read_pdf("/Users/vasudevan/Downloads/Digital_Fluency_Module3_asd.pdf")

# Preprocessing function
def preprocess_text(text):
    # Tokenization
    tokens = nltk.word_tokenize(text.lower())
    # Stopword removal
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return tokens

# Preprocess the dataset
processed_docs = [preprocess_text(doc) for doc in data]

# Create a dictionary and corpus
dictionary = corpora.Dictionary(processed_docs)
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

# Build LDA Model
num_topics = 1  # Number of topics to extract
lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)

# Display topics
for idx, topic in lda_model.print_topics(-1):
    print(f"Topic {idx + 1}: {topic}")

# Visualize word distributions in topics
for idx, topic in lda_model.show_topics(formatted=False):
    words, weights = zip(*topic)
    plt.barh(words, weights)
    plt.title(f"Topic {idx + 1}")
    plt.show()
