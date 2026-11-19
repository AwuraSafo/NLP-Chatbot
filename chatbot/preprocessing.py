import re
from nltk.stem import PorterStemmer

# Initialize the Porter Stemmer
stemmer = PorterStemmer()


def preprocess_text(text):
    """
    Clean and prepare user input for NLP processing.
    """

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Convert text to lowercase
    text = text.lower()

    # Extract individual words
    tokens = re.findall(r"\b[a-zA-Z]+\b", text)

    # Reduce words to their root forms
    processed_tokens = [stemmer.stem(word) for word in tokens]

    return processed_tokens
