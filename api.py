from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter, defaultdict
from lazysorted import LazySorted
from string import ascii_letters
import nltk

#nltk.download()

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('text', required=True, help="text field cannot be blank!")

#----------HELPERS-----------# 
## Filter words that contain only ascii_letters or '-' or ascii(44) which is an apostrophe 
def wordOnly(tokens):
    filtered = [word for word in tokens if all(char in ascii_letters+'-'+chr(44) for char in word)]
    return filtered

## Tokenize text and filter things that are words
def parseArgs():
    args = parser.parse_args()
    text = args['text']
    tokens = word_tokenize(text)
    filtered = wordOnly(tokens)
    return filtered

#An expected linear time median function using the LazySorted library
def calcMedian(xs):
    ls = LazySorted(xs)
    n = len(ls)
    if n == 0:
        raise ValueError("Need a non-empty iterable")
    elif n % 2 == 1:
        return ls[n//2]
    else:
        return sum(ls[(n/2-1):(n/2+1)]) / 2.0

#----------CONTROLLERS-----------# 
## Find average word length
#  1) Add the length of each word and divide by total number of words
class avgLen(Resource):
    def post(self):
        filtered = parseArgs()
        avg_len = float(sum(map(len, filtered))) / len(filtered)
        return avg_len

## Find words that occur the most frequently:
#  1) Hash by word and sum the count: O(n)
#  2) Look through hash for most frequent word, break ties with alphabetical order: O(n)
class mostCommonWord(Resource):
    def post(self):
        filtered = parseArgs()
        counts = Counter(filtered)
        most_common = {'word':None,'count':None}
        for word, count in counts.iteritems():
            if (most_common['word'] == None) or (most_common['count'] < count):
                most_common['word'] = word
                most_common['count'] = count
            if (most_common['count'] == count):
                most_common['word'] =  min(most_common['word'],word)     
        return most_common['word']

## Find words that occur the median amount
#  1) Hash by word and sum the count: O(n)
#  2) Calc median: expected run time is linear thansk to LazySorted
#  3) Iterate over words and add to array if count matches median: O(n)
class medianWordLen(Resource):
    def post(self):
        filtered = parseArgs()
        counts = Counter(filtered)
        median = calcMedian(counts.values())
        median_words = [word for word, count in counts.iteritems() if count == median]
        return median_words

## Find words that occur the median amount
#  1) Use NLTK's sentence tokenization
#  2) Calc avg: O(n)
class sentLength(Resource):
    def post(self):
        args = parser.parse_args()
        text = args['text']
        sentences = sent_tokenize(text)
        sum_lengths = 0
        for sentence in sentences:
            sum_lengths += len(wordOnly(word_tokenize(sentence)))
        return sum_lengths / len(sentences)

#----------ROUTES-----------# 
api.add_resource(avgLen, '/words/avg_len')
api.add_resource(mostCommonWord, '/words/most_com')
api.add_resource(medianWordLen, '/words/median')
api.add_resource(sentLength, '/sentences/avg_len')

if __name__ == '__main__':
    app.run(debug=True)
