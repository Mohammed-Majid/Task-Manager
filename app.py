from flask import Flask, render_template, request
import heapq
from datetime import datetime

app = Flask(__name__) # creating the flask app

graph = {
    'A': []  #adjacency list containing graph cuz its easier so why not
    }

def add_task(graph, task_name, due_date):  #function to append nodes to the dictionary up there
    graph['A'].append((task_name, (due_date - datetime.now()).days)) 

def print_priority_list(graph):
    priority_list = [] #empty list to store tasks (depending on weight)

    for task, weight in graph['A']:
        heapq.heappush(priority_list, (weight, task))

    results = []
    while priority_list:
        weight, task = heapq.heappop(priority_list)
        results.append({'task': task, 'weight': weight})

    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_name = request.form['task_name']
        due_date = request.form['due_date']

        day, month = map(int, due_date.split('/'))
        year = datetime.now().year
        due_date = datetime(year, month, day)
        add_task(graph, task_name, due_date)

    priority_list = print_priority_list(graph)

    return render_template('index.html', priority_list=priority_list)

if __name__ == '__main__':
    app.run()
