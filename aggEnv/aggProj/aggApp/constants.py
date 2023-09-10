from .models import Student
from django.db import connection
import math

# Pagination and other constants

BASE_URL = "localhost/users/"
RECORD_PER_PAGE = 3
NUMBER_OF_PAGE_LINKS_PER_SLOT=5
URL_PREFIX = '/api'