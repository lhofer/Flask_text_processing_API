#Text Processing API
####Leila Hofer Mark 43 Application

##About
Use curl requests and return processed text

###Endpoints
1. /words/avg_len : average word lenght in text
2. /words/most_com : most common word in text
3. /words/median : words used the median number of times
4. /sentences/avg_len : average sentence length

###Example Calls
1. average word length: curl http://localhost:5000/words/avg_len -d '{"text":"something new"}' -X POST -H "Content-type: application/json" 
2. most common word: curl http://localhost:5000/words/most_com -d '{"text":"something new. and now a new sentence. That is pretty and awesome!"}' -X POST -H "Content-type: application/json"
3. median words: curl http://localhost:5000/words/median -d '{"text":"something new. and now a new sentence. That is pretty and awesome!"}' -X POST -H "Content-type: application/json"
4. sentence length: curl http://localhost:5000/sentences/avg_len -d '{"text":"something new. and now a new sentence. That is pretty and awesome!"}' -X POST -H "Content-type: application/json"

#####NOTE: the terminal I test on reads requires unicode chars instead of escaped special characters (i.e. apostrophe should be represented as \u0027 instead of \')

###Usage
1. Start Server in api_mark43 directory
  * $ . venv/bin/activate
  * $ python api.py
2. in another terminal window
  * $ curl request

###Setup
####IMPORTANT: If this setup doesn't work please let me know and I can host it on a server elsewhere
1. Clone Repo
  * clone repo from https://github.com/lhofer/api_mark43.git
2. Install virtual environment
  * (mac) $ sudo easy_install virtualenv  
  * (windows) $ sudo apt-get install python-virtualenv
3. Enter directory and set up virtual environment
  1. $ cd api_mark43
  2. $ virtualenv venv
4. enter virtual environment 
  * (mac) $ . venv/bin/activate
  * (windows) $ venv\scripts\activate
5. install dependencies
6. $ pip install Flask
7. $ pip install flask-restful
8. $ pip install nltk
9. $ pip install lazysorted
10. $ pip install Counter

###Design
#####Performance
Given the initial overhead of parsing, tokenizing, and filtering the text, where possible I tried to optimize my code for larger values of n, thinking that the time saved on large lists would be much more than the time lost on small lists. Additionally, the decision to implement a hash table with the words as a keys in the frequency functions was to allow O(1) access time to any word-frequency pair. 

##### Most Common Word
An alternative I considered was to sort the hash table by frequency and then iterate through only the most frequent words. However, this would take O(n logn) to sort plus the time to iterate through the most frequent words, on top of the O(n) time to hash. The current implementation will run in O(2n) time (O(n) time to hash and O(n) to iterate through each value to check for the max) whereas the previous implementation would take at a minimum of n + (n logn) which would be slower than the current implementation as n increases. 

##### Median Frequency Words
Again, an alternative would be to sort the hash (n logn) and then iterate through to find the median values, stopping once you pass the last median value in the sorted list. This would take at a minimum O(n logn plus) the O(n) time to hash which would again be slower as n increases than the current implementation. The current implementation takes O(n) time to generate the hash table, uses a linear median function (so O(n) agian) and then iterates through every value in the list (O(n)). 3n is still less than n logn + n for larger lists.

#####Definitions
As this program is a text processer not a spell checker, and I wanted to make sure someone could process Dr. Suss texts, I decided not to crosscheck all words against an english language dictionary. However, I did decide to use only words comprised of only alphabetic characters, hyphons, and apostrophes (so no numbers or other punctuation could be counted as a word). Beyond this, for the most part I left the definitions of words and sentences up to the NLTK library.
