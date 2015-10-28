from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

todos = {}

#--------STEP 1--------#
class HelloWorld(Resource):
   def get(self):
       return {'hello': 'world'}

#--------STEP 2--------#
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(HelloWorld, '/', '/hello')
api.add_resource(TodoSimple, '/<string:todo_id>') #, endpoint='todo_ep' #? what does this doe?


#api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)