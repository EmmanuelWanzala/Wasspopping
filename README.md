## WASSPOPPING

This is a news application that allows users to view news from various news sources around the world

## USER STORIES

The user should be able to:

-See various news sources

-Select the ones they prefer

-See the top news articles from that news source

-See the image, description and time the news article was created

-Click on an article and read it fully from the news source

## LIVE LINK TO THE PROJECT



## SET UP INSTRUCTIONS

-Click on the green button written Clone

-On your terminal:

-git clone ` `

-cd Wasspopping



## HOW  TO RUN THE APPLICATION

Creating the virtual environment

  $ python3.8 -m venv --without-pip virtual
  $ source virtual/bin/env
  $ curl https://bootstrap.pypa.io/get-pip.py | python 
Installing Flask and other Modules

  $ python3.8 -m pip install Flask
  $ python3.8 -m pip install Flask-Bootstrap
  $ python3.8 -m pip install Flask-Script
Setting up the API Key

  To be able to gather article info from the News API you will need an API Key.
  
  * Visit https://newsapi.org/ and register for an API key.
  * In the root directory of the project folder create a file: start.sh
  * Insert the following info into it: 
  
          export NEWS_API_KEY='<Your-Api-Key>'
          python3.8 manage.py server
          
  * Insert the API Key you received from News Api where <Your-Api-Key> is.
To run the application, in your terminal:

  $ chmod +x start.sh
  $ ./start.sh




## CONTACTS

wanzalaemmanuel28@gmail.com