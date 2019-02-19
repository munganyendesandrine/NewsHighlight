from flask import render_template
from app import app
from .request import get_news,get_news

   

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting general news
    general_news = get_news('general')
    technology_news = get_news('technology')
    business_news = get_news('business')
    sports_news=get_news('sports')
    entertainment_news=get_news('entertainment')
    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html', title = title, general = general_news, technology = technology_news, business = business_news,sports = sports_news,entertainment = entertainment_news)


@app.route('/news/<int:id>')
def get_newsd(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_newsd(id)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = news)

    