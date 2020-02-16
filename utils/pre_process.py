"""

This module performs the preprocessing of raw tweets preparing
them for sentimental analysis with with CNN + Embedding model

"""
import re
import stopwords
from constants import VectorInt, VectorString, TOKEN_TO_INDEX, MAX_LENGTH_TWEET, \
                    MAX_LENGTH_DICTIONARY
from nltk_tokenize import TweetTokenizer

class Preprocess:
    """
    The Preprocess object
    :param max_length_tweet_arg: defaults to MAX_LENGTH_TWEET defined in constants
    :param max_length_dictionary: defaults to MAX_LENGTH_DICTIONARY defined in constants
    """

    def __init__(self, max_length_tweet_arg=MAX_LENGTH_TWEET,
                 max_length_dictionary_arg=MAX_LENGTH_DICTIONARY):
        """
        Intializes a Preprocess object
        """
        self.__max_length_dictionary = max_length_dictionary_arg
        self.__token_to_index = self.token_to_index_helper()
        self.__max_length_tweet = max_length_tweet_arg
        self.tokenizer = TweetTokenizer()
        self.cleaning_regex = r'([RT])|(@[\w]+:?)|(\w+:\/\/\S+)'

    @property
    def token_to_index(self):
        """
        getter method for token_to_index
        """
        return self.__token_to_index

    @token_to_index.setter
    def token_to_index(self, token_dictionary):
        """
        setter method for token_to_index
        """
        self.__token_to_index = token_dictionary

    @property
    def max_length_tweet(self):
        """
        getter method for max_length_tweet
        """
        return self.__max_length_tweet

    @max_length_tweet.setter
    def max_length_tweet(self, max_length_tweet_arg):
        """
        setter method for max_length_tweet
        """
        self.__max_length_tweet = max_length_tweet_arg

    @property
    def max_length_dictionary(self):
        """
        getter method for max_length_tweet
        """
        return self.__max_length_dictionary

    @max_length_dictionary.setter
    def max_length_dictionary(self, max_length_dictionary_arg):
        """
        setter method for max_length_tweet
        """
        self.__max_length_dictionary = max_length_dictionary_arg

    def token_to_index_helper(self):
        """
        helper function to initialize token_to_index dict
        """
        # replace numpy with python in-built functions
        return_dict = dict()
        with open(TOKEN_TO_INDEX, 'r') as file:
            count = 0
            for line in file:
                return_dict[line.strip()] = count
                count += 1
                if count >= self.max_length_dictionary:
                    break
        return return_dict

    def clean_text(self, tweet: str) -> str:
        """
        Args:
            tweet
                raw tweet with url and @

        Returns:
            cleaned_tweet
                removes the RT, handle and url

       """
        tweet = re.sub(re.compile(self.cleaning_regex), ' ', tweet)
        return ' '.join(tweet.split()).strip()


    def tokenize_text(self, cleaned_tweet: str) -> VectorInt:

        """
        Args:
            cleaned_tweet
                cleaned tweet not containing the url and the @ twitter handler

        Returns:
           An array of tokens

        """
        token = self.tokenizer.tokenize(cleaned_tweet)
        return [i for i in token if i not in stopwords.words()]


    def replace_token_with_index(self, tokens: VectorString) -> VectorInt:

        """
        Args:
            tokens
                An array of tokens
        Returns:
            List of indices
        """

        # intitialize result list
        result = []
        # load token to index array
        for token in tokens:
            if token.isnumeric():
                result.append(self.token_to_index.get('<number>', -1) + 1)
            elif token.isupper():
                result.append(self.token_to_index.get('<allcaps>', -1) + 1)
            else:
                result.append(self.token_to_index.get(token, -1) + 1)

        return result


    def pad_sequence(self, indices: VectorInt) -> VectorInt:

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

        if len(indices) > self.max_length_tweet:
            padded_seq = indices[:self.max_length_tweet]
        else:
            zeros = [0] * (self.max_length_tweet-len(indices))
            padded_seq = indices + zeros
        return padded_seq

    def one_for_all(self, tweet) -> list:
        """Do all conversion at once"""
        return self.pad_sequence(self.replace_token_with_index(self.tokenize_text(
            self.clean_text(tweet))))
