"""

This module performs the preprocessing of raw tweets preparing
them for sentimental analysis with with CNN + Embedding model

"""
import re
from constants import VectorInt

import stopwords
from nltk_tokenize import TweetTokenizer

def clean_text(tweet: str) -> str:
    """

    Args:
        tweet
            raw tweet with url and @

    Returns:
        cleaned_tweet
            removes the RT, handle and url

   """
    # text = re.sub(r'^https?:\/\/.*[\r\n]*', '', tweet, flags=re.MULTILINE)
    # cleaned_tweet = ' '.join(re.sub(r"(@[A-Za-z0-9_]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", \
    #     text).split())

    tweet = re.sub(re.compile(r'([RT])|(@[\w]+:?)|(\w+:\/\/\S+)'), ' ', tweet)
    return ' '.join(tweet.split()).strip()


def tokenize_text(cleaned_tweet: str) -> VectorInt:

    """

    Args:
        cleaned_tweet
            cleaned tweet not containing the url and the @ twitter handler

    Returns:
       An array of tokens

    """

    tknzr = TweetTokenizer()
    token = tknzr.tokenize(cleaned_tweet)
    return [i for i in token if i not in stopwords.words()]


def replace_token_with_index(tokens: VectorInt, max_length_dictionary: int = None) -> VectorInt:

    """

    Args:
        tokens
            An array of tokens
        max_length_dictionary (Optional)
            load the GloVe embedding dictionary until max_length_dictionary

    Returns:
        List of indices
    """

    pass

def pad_sequence(indices: VectorInt, max_length_tweet: int = None) -> VectorInt:

    """
    Args:
        indices
            A list of indices
        max_length (Optional)
            0s will padded to ensure that the list if of length
            max_length
    Returns:
        A list of indices padded with 0s to ensure length equals
        max length
    """

    if len(indices) > max_length_tweet:
        padded_seq = indices[:max_length_tweet]
    else:
        zeros = [0] * (max_length_tweet-len(indices))
        padded_seq = indices + zeros
    return padded_seq

def one_for_all(tweet, max_length_dictionary=500, max_length_tweet=20) -> list:
    """Do all conversion at once"""
    return pad_sequence(replace_token_with_index(tokenize_text(
        clean_text(tweet)), max_length_dictionary), max_length_tweet)
