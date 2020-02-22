from utils.pre_process import Preprocess

if __name__ == "__main__":

    test = Preprocess(max_length_tweet_arg=25, 
                    max_length_dictionary_arg=1000)

    print (test.path_to_dictionary)