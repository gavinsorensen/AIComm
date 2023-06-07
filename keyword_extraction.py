import nltk # natural language toolkit
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer

def extract_keywords(text):
    """
    Uses natural language processing techniques to extract the key topics or keywords from customer inquiries or communications.
    """
    # tokenize the text into sentences and then words
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]

    # remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    words = [[word.lower() for word in sentence if word.lower() not in stop_words and word.isalnum()] for sentence in words]

    # lemmatize words
    lemmatizer = WordNetLemmatizer()
    words = [[lemmatizer.lemmatize(word) for word in sentence] for sentence in words]

    # calculate word frequency and extract top keywords
    all_words = [word for sentence in words for word in sentence]
    freq_dist = FreqDist(all_words)
    n_top_keywords = 10
    top_keywords = [word for word, frequency in freq_dist.most_common(n_top_keywords)]

    return top_keywords
