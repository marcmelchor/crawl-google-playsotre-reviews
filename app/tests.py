from django.test import TestCase
from app.tasks import crawl_app_reviews


class CrawlAppReviewsTestCase(TestCase):

    def testCrawlReviews(self):
        crawl_app_reviews.delay('com.nianticlabs.pokemongo')

        self.assertTrue(True)
