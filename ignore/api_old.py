from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
#nltk.download()

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')
parser.add_argument('text', required=True, help="text field cannot be blank!")


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    # curl http://localhost:5000/todos/todo3
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    # curl http://localhost:5000/todos/todo2 -X DELETE -v
    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    # curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v
    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    # curl http://localhost:5000/todos
    def get(self):
        return TODOS

    # curl http://localhost:5000/todos -d "task=something new" -X POST -v
    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

class Json(Resource):
    # curl http://localhost:5000/json -d '{"text":"something new"}' -X POST -H "Content-type: application/json"
    # curl http://localhost:5000/json -d '{"text":"something new. It doesn\'t have feathers"}' -X POST -H "Content-type: application/json"

    def post(self):
        args = parser.parse_args()
        text = {'text': args['text']}
        print text
        print sent_tokenize(text['text'])
        print word_tokenize(text['text'])
        return text['text']

class Json(Resource):
    def post(self):
        args = parser.parse_args()
        text = {'text': args['text']}
        return text['text']
    

        # dictionary = defaultdict(int)
        # repeats = []
        # #for word in filtered.iteritems():
        # #    if dictionary[word] != 0:
        # #        print  dictionary[word]
        # #        print word
        # #        repeats << word
        # #    dictionary[word] = len(word)
        # median = statistics.median(dictionary.values())
        # median_words = []
        # for key, value in dictionary.iteritems():  
        #     if value == median:
        #         median_words.push(key)
        # if len(median_words) > 0:
        #     return median_words




        
num_chars = len(gutenberg.raw(fileid))
##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(Json, '/json')
api.add_resource(Json, 'avg_len')


if __name__ == '__main__':
    app.run(debug=True)