# Crawl Google Playstore Reviews
This is an open source cronjob, where you can crawl reviews from a specific app in Google Store. This is built in ``Django``.

### Requirements:
> ***
> - **Python** >= 3.7
> - **psycopg2-binary** >= 2.8
> - **celery** >= 5.0
> - **redis** >= 3.5
> - **google-play-scraper** >= 0.1

### Setup:
> - Pull this repository into your machine.
> - ``$ git clone https://github.com/marcmelchor/crawl-google-playsotre-reviews.git``
> - ``$ cd crawler``
> - Create a virtual environment.
> - ``$ virtualenv venv``
> - **MacOS or Linux** ``$ venv/bin/activate``
> - Install all the libraries.
> - ``$ pip install -r requirements.txt``
