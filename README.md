#Mark 43 Text APE
####Leila Hofer

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
###### NOTE: the terminal I test on reads requires unicode chars instead of escaped special characters (i.e. apostrophe should be represented as \u0027 instead of \')

###Usage
1. $ . venv/bin/activate
2. $ python api.py

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
