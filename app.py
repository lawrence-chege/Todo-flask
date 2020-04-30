import  random
from flask import Flask
from  flask_restful import  Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
random.seed(123)
Tasks = [ {"id": 0, "task_item": { "name":"Code", "date":"12-10-07","importance": 4}}]

class TodoList(Resource):
    def get(self):
        return {'Tasks': Tasks}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name',type=str,required=True,
                help="Name field is required")
        parser.add_argument('importance',type=int,required=True,
                help="Importance field is required")
        parser.add_argument('date',type=str,required=True,
                help="Date field is required")

        args = parser.parse_args()
        task = {}
        task_item = {}

        task["id"] = random.randint(1,100)

        task_item["name"] = args["name"]
        task_item["date"] = args["date"]
        task_item["importance"] = args["importance"]

        task["task_item"] = task_item

        Tasks.append(task)

        return {'Task': task}

class Todo(Resource):

    def get(self, task_id):
        task = [task for task in Tasks if int(task["id"] == int(task_id))]
        return task

    def put(self,task_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name',type=str,
                help="Name field should be a string")
        parser.add_argument('importance',type=int,
                help="Importance field should be an integer")
        parser.add_argument('date',type=str,
                help="Date field is should be a string")

        args = parser.parse_args()
        task = {}
        task_item = {}
        
        task = [task for task in Tasks if int(task["id"] == int(task_id))]
        if task:
            task_item["name"] = args["name"]
            task_item["date"] = args["date"]
            task_item["importance"] = args["importance"]

            task[0]["task_item"] = task_item
            return {'Task': task}

        return {"error": "task not found"}


api.add_resource(TodoList, '/')
api.add_resource(Todo, '/<task_id>/')

if __name__ == '__main__':
    app.run(debug=True)
