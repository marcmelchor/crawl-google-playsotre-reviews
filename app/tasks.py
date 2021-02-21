from __future__ import absolute_import, unicode_literals
from celery import shared_task
from google_play_scraper import app, Sort, reviews, reviews_all
from .models import App, Review
from django.core.exceptions import ObjectDoesNotExist


@shared_task
def import_app_info(app_id, **kwargs):
    response = app(
        app_id,
        lang=fix_attribute(kwargs.get('lang'), 'en'),
        country=fix_attribute(kwargs.get('country'), 'us'),
    )

    save_app(response['appId'])


@shared_task
def crawl_app_reviews(app_id, **kwargs):
    result, continuation_token = reviews(
        app_id,
        lang=fix_attribute(kwargs.get('lang'), 'en'),
        country=fix_attribute(kwargs.get('country'), 'us'),
        sort=Sort.MOST_RELEVANT,
        count=fix_attribute(kwargs.get('count'), 10),
        filter_score_with=fix_attribute(kwargs.get('score'), 5),
    )

    app_reviews, _ = reviews(
        app_id,
        continuation_token=continuation_token,
    )

    app_object = save_app(app_id)
    app_reviews = get_new_reviews(app_reviews)
    save_app_reviews(app_reviews, app_object)


@shared_task
def crawl_all_app_reviews(app_id, **kwargs):
    app_reviews = reviews_all(
        app_id,
        sleep_milliseconds=0,
        lang=fix_attribute(kwargs.get('lang'), 'en'),
        country=fix_attribute(kwargs.get('country'), 'us'),
        sort=Sort.MOST_RELEVANT,
        filter_score_with=fix_attribute(kwargs.get('score'), 5),
    )

    app_object = save_app(app_id)
    app_reviews = get_new_reviews(app_reviews)
    save_app_reviews(app_reviews, app_object)


def fix_attribute(attribute, default):
    if attribute is not None:
        return attribute

    return default


def save_app(android_app_id):
    try:
        app_object = App.objects.get(app_id=android_app_id)
        print(f'The application { android_app_id } already exists.')

        return app_object
    except ObjectDoesNotExist:
        android_app = App(app_id=android_app_id)
        app_object = android_app.save()
        print(f'The application { android_app_id } has been saved.')

        return app_object


def get_new_reviews(app_reviews):
    app_id_reviews = [android_reviews['reviewId'] for android_reviews in app_reviews]
    saved_reviews = list(Review.objects.filter(review_id__in=app_id_reviews).values_list('review_id', flat=True))
    app_id_reviews = list(set(app_id_reviews) - set(saved_reviews))

    return [app_review for app_review in app_reviews if (app_review['reviewId'] in app_id_reviews)]


def save_app_reviews(app_reviews, app_object):
    for review in app_reviews:
        review_id = review['reviewId']
        app_review = Review(
            app_id=app_object,
            review_id=review_id,
            user_name=review['userName'],
            user_image=review['userImage'],
            content=review['content'],
            score=review['score'],
            thumbs_up_count=review['thumbsUpCount'],
            review_created_version=review['reviewCreatedVersion'],
            at=review['at'],
        )

        app_review.save()

    print(f'{ len(app_reviews) } have been successfully saved.')
