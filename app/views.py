from flask import render_template
from app import app
from .request import get_news,get_news
from .request import get_articles,get_articles
   

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

@app.route('/articles/<id>')
def get_articlesd(id):

    '''
    View articles page function that returns the articles details page and its data
    '''
    
    articles=get_articles(id)
   
    title=f'{id}'
   
    return render_template('articlesd.html',title=title,articles =articles  )    
