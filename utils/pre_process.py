"""

This module performs the preprocessing of raw tweets preparing
them for sentimental analysis with with CNN + Embedding model

"""
from constants import VectorInt

def clean_text(tweet:str) -> str:
    """

    Args:
        tweet
            raw tweet with url and @

    Returns:
        cleaned_tweet
            removes the url and @ token

    """ 

    pass


def tokenize_text(cleaned_tweet:str) -> VectorInt:

    """

    Args:
        cleaned_tweet
            cleaned tweet not containing the url and the @ token

    Returns:
        An array of tokens 

    """

    pass


def replace_token_with_index(tokens_array: VectorInt) -> VectorInt:

    """

    Args:
        tokens_array
            An array of tokens

    Returns:
        List of indices
    """

    pass

def pad_sequence(indices: VectorInt, max_length: int) -> VectorInt:

    """
    Args:
        indices
            A list of indices
        max_length
            0s will padded to ensure that the list if of length 
            max_length
    Returns:
        A list of indices padded with 0s to ensure length equals
        max length
    """

    pass


