# Flask To-Do List Application

This is a simple Flask web application that allows users to add tasks with due dates and prioritize them based on how soon they are due. 

## Features

- Add tasks with due dates
- Automatically prioritize tasks based on the closest due date
- View the prioritized list of tasks
- Reset the task list

## Requirements

- Python 3.x
- Flask

## Setup and Installation

1. **Clone the repository:**
```
git clone https://github.com/Mohammed-Majid/Task-Manager.git
```
2. **Create a virtual environment:**
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. **Install the dependencies:**
```
pip install Flask
```
4. **Run the application:**
```
python app.py
```
5. **Open your browser and go to:**
```
http://127.0.0.1:5000
```
## Usage

1. Open the application in your browser.
   
2. Add tasks:
  - Enter the task name and due date (in dd/mm format) in the form and submit.
    
3. View the prioritized list of tasks:
  - The tasks will be displayed in the order of their due dates, from soonest to latest.
    
4. Reset the task list:
  - Click the "Reset" button to clear all tasks.
    
## Project Structure

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for rendering the task form and displaying the prioritized list.
- `static/css/styles.css`: The CSS file for styling the HTML template.



##Extra info

This project uses an adj list with a graph that initially has one node "A". 
Each time a task is added, a weighted edge connected to a neighbor is added.
weights represent the number of days left while nodes represent the tasks.
A min heap is used to sort through the weights of the graph to order them in a priority list.



<img width="1274" alt="Screen Shot 2023-06-10 at 11 39 02 AM" src="https://github.com/Mohammed-Majid/Task-Manager/assets/136110323/f46ffdd8-bc92-4edf-a912-ad90dd2cf90e">
