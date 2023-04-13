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

news = [{'title': 'Удивительное событие в школе',
         'text': 'Вчера в местной школе произошло удивительное событие - все '
                 'ученики одновременно зевнули на уроке математики. '
                 'Преподаватель был так поражен этим коллективным зевком, '
                 'что решил отменить контрольную работу.'},
        {'title': 'Случай в зоопарке',
         'text': 'В зоопарке города произошел необычный случай - ленивец '
                 'решил не лениться и взобрался на самое высокое дерево в '
                 'своем вольере. Посетители зоопарка были поражены такой '
                 'активностью и начали снимать ленивца на видео. В итоге он '
                 'получил свой собственный канал на YouTube, где он размещает '
                 'свои приключения.'},
        {'title': 'Самый красивый пёс',
         'text': 'Сегодня в парке прошел необычный конкурс - "Самый красивый '
                 'пёс". Участники конкурса были так красивы, что судьи не '
                 'могли выбрать победителя. В итоге, конкурс был объявлен '
                 'ничейным, а участники получили награды за участие, '
                 'в том числе - пакетики конфет и игрушки в виде косточек. '
                 'Конкурс вызвал большой интерес у посетителей парка, '
                 'и его решили повторить в более масштабном формате.'}]
@app.route('/news_detail/<int:id>')
def news_detail(id):
    title = news[id]['title']
    text = news[id]['text']
    return render_template("news_detail.html", title = title, text = text)
@app.route('/about')
def about():
    return "Сайт с новостями"
@app.route('/fibonacci')
def fibonacci():
    result = get_fibonacci_numbers(100)
    return ''.join(map(str, result))


if __name__ == '__main__':
    app.run(debug=True)