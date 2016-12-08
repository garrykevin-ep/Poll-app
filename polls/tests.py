from django.test import TestCase
import datetime
from django.utils import timezone
from django.test import testcases

from .models import Question
# Create your tests here.

class QuestionMethodTests(TestCase):
    def test_was_publish_recently_with_future_questions(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(),False)
