# Crawl Google Playstore Reviews
This is an open source cronjob, where you can crawl reviews from a specific app in Google Store. This is built in ``Django``.

### Requirements:
> ***
> - **Python** >= 3.7
> - **psycopg2-binary** >= 2.8
> - **celery** >= 5.0
> - **redis** >= 3.5
> - **google-play-scraper** >= 0.1

### Setup Locally:
> - Pull this repository into your machine.
> - ``$ git clone https://github.com/marcmelchor/crawl-google-playsotre-reviews.git``
> - ``$ cd crawler``
> - Create a virtual environment.
> - ``$ virtualenv venv``
> - **MacOS or Linux** ``$ venv/bin/activate``
> - Install all the libraries.
> - ``$ pip install -r requirements.txt``

### Setup Docker:
> - Build the images ``$ docker-compose build -d``
> - Run migrations and migrate them
>> - ``$ docker exec -it django bash``
>> - ``$ python manage.py makemigrations``
>> - ``$ python manage.py migrate``
> - ``$ docker-compose up``. I suggest to not run it in background, in order to see
the job queues.
> - If you don't want to wait 1 hour for the next scheduled job. You can go to
``crawler/celery.py`` and in the line ``27``, you change ``hour='*/1'`` for ``minute='*/10'``
> - There are other methods like ``import_app_info`` or ``crawl_app_reviews`` which you can also test just by
uncomment the lines in the ``celery.py`` file.

### Important
> - At the moment to crawl the reviews, these are not deleted from the database but, map the
saved reviews (in case they are) with the reviews pulled and only save the new ones. It happens
the same with the app itself.
> - In the ``app/uml`` folder you can find the ``UML`` of the app