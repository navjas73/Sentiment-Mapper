from django.db import models
from twython import Twython
import urllib
import json

class Tweet(models.Model):
    
