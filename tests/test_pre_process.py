"""
This module performs unit tests on pre_process.py module
"""

from utils.pre_process import *

def test_clean_text():
    """
    Test clean_text method: the method should remove twitter handle
    and url
    """

    tweet = "@my_handler here is my tweet http://..."
    cleaned_tweet = clean_text(tweet)

    expected_output = "here is my tweet"

    assert cleaned_tweet == expected_output


def test_tokenize_text():
    pass

def test_replace_token_with_index():
    pass

def test_pad_sequence():
    pass
