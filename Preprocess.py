import glob
import pickle
import os

def read_preprocess_files():
    dir = os.path.dirname(__file__)
    tweets = []
    lens = []

    if 'lens.pickle' not in os.listdir(dir):
        for file in glob.glob(dir + '/Health-Tweets/**'):
            with open(file, 'r') as f:
                print(file)
                lines = f.readlines()
                for line in lines:
                    tweet = ''.join(line.split('|')[2:]).strip().lower().split(' ')
                    tweets.append(tweet)
                    lens.append(len(tweet))
        with open(dir + '/tweets.pickle', 'wb') as handle:
            pickle.dump(tweets, handle)
        with open(dir + '/lens.pickle', 'wb') as handle:
            pickle.dump(lens, handle)

    else:
        with open(dir + '/tweets.pickle', 'rb') as handle:
            tweets = pickle.load(handle)
        with open(dir + '/lens.pickle', 'rb') as handle:
            lens = pickle.load(handle)

    return tweets, lens

