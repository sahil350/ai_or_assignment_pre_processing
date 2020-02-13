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

def pad_sequence(indices: VectorInt, max_length: int = None) -> VectorInt:

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

    pass
