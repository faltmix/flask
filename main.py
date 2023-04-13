from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_fibonacci_numbers(n):
   numbers = [1, 1]
   for i in range(2, n):
       numbers.append(numbers[i - 1] + numbers[i - 2])
   return numbers

@app.route('/')
def index():
    return render_template("index.html", title = 'новостной сайт', text = 'Скоро будут новости')
@app.route('/home')
def home():
    return 'Главная страница'
@app.route('/news')
def news():
    return "Страница с новостями"
@app.route('/about')
def about():
    return "Сайт с новостями"
@app.route('/fibonacci')
def fibonacci():
    result = get_fibonacci_numbers(100)
    return ''.join(map(str, result))


if __name__ == '__main__':
    app.run(debug=True)