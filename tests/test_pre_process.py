"""
This module performs unit tests on pre_process.py module
"""

import unittest
from utils.pre_process import Preprocess

class TestPreprocessModule(unittest.TestCase):

    """
    Unit test Test class to test the Preprocess Module
    """

    __pre_process = Preprocess()
    __pre_process_2 = Preprocess(25, 500) # non default arguments

    def setUp(self): # run before test runs
        return # do nothing

    def test_clean_text(self):
        """
        To test the clean_text method in the Preprocess class
        """
        tweet = "RT @dullalena @taurusismagic @motshabi_P ❤❤ \
        I'm happy you had a beautiful day! 😘 https://t.co/T6uxfX6DpC"
        result = self.__pre_process.clean_text(tweet)
        expected_result = "❤❤ I'm happy you had a beautiful day! 😘"
        self.assertEqual(result, expected_result)

    def test_tokenize_text(self):
        """
        To test the tokenize_text method in the Preprocess class
        """
        cleaned_text = "❤❤ I'm happy you had a beautiful day! 😘"

        result = self.__pre_process.tokenize_text(cleaned_text)
        expected_result = ['❤', '❤', "I'm", "happy", "beautiful", "day", "!", '😘']
        self.assertEqual(result, expected_result)

    def test_replace_token_with_index(self):
        """
        To test the replace_token_with_index method in the Preprocess class
        """
        tokens = ['❤', '❤', "I'm", "happy", "beautiful", "day", "!"]
        result = self.__pre_process.replace_token_with_index(tokens)
        expected_result = [189, 189, 0, 178, 532, 126, 10]
        self.assertEqual(result, expected_result)
        result = self.__pre_process_2.replace_token_with_index(tokens)
        expected_result = [189, 189, 0, 178, 0, 126, 10]
        self.assertEqual(result, expected_result)


    def test_pad_sequence(self):
        """
        To test the pad_sequence method in the Preprocess class
        """
        index_list = [0, 0, 0, 0]

        result = self.__pre_process.pad_sequence(index_list)
        expected_result = [0] * 20
        self.assertEqual(result, expected_result)

        result = self.__pre_process_2.pad_sequence(index_list)
        expected_result = [0] * 25
        self.assertEqual(result, expected_result)
        