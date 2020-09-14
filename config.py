import os

class Config:

   	NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey=168f9da938494bd8b2751aa3eace387d'
   	ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey=168f9da938494bd8b2751aa3eace387d'
   	NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
   	@staticmethod
   	def init_app(app):
   		pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
