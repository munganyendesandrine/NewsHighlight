from app import app
import urllib.request,json
from .models import news
from .models import articles
Articlesd =articles.Articlesd


# Getting api key
api_key = app.config['NEWS_API_KEY']

News = news.News

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
base_url2 = app.config["ARTICLES_API_BASE_URL"]
print(base_url2)

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
           
            


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if url:
            news_object = News(id,name,description,url,category,language,country)
            news_results.append(news_object)
            
    return news_results    

def get_articles(id):
    
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url2.format(id,api_key)
    

    with urllib.request.urlopen(get_articles_url) as url:
       
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
   
      

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            
            articles_results = process_results(articles_results_list)
            


    return articles_results  

def process_results(articles_list):
    '''
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain articles details

    Returns :
        articles_results: A list of articles objects
    '''
    articles_results = []
    for articles_item in articles_list:
        id = articles_item.get('id')
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')

        if url:
            articles_object = Articlesd(id,author,title,description,url,urlToImage,publishedAt,content)
            articles_results.append(articles_object)

    return articles_results      

