# This is cron job page to add research paper publiucations to professors Page

from scholarly import scholarly
from mechweb.models import FacultyPage
from urllib.parse import urlparse, parse_qs
from django.core.cache import cache
from celery import shared_task
import requests

@shared_task
def updateGoogleScholarPublications():
    try: 
        all_faculty_data = FacultyPage.objects.all()
        for faculty_data in all_faculty_data:
            if faculty_data.google_scholar_profile_link :
                parsed_url = urlparse(faculty_data.google_scholar_profile_link)
                query_params = parse_qs(parsed_url.query)
                user_id = query_params.get('user', [''])[0]
                author = scholarly.search_author_id(user_id)
                scholarly.pprint(author)
    except Exception as e:
        # Handle other exceptions
        print(f"Error: {e}")


def fetch_and_store_temperature():
    try:
        response = requests.get('https://raw.githubusercontent.com/strativ-dev/technical-screening-test/main/bd-districts.json')
        response.raise_for_status()

        districts_data = response.json().get('districts', [])

        all_temperatures = []

        for district in districts_data:
            latitude = district.get('lat')
            longitude = district.get('long')

            if latitude is not None and longitude is not None:
                api_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&timezone=GMT&forecast_days=7'

                weather_response = requests.get(api_url)
                weather_response.raise_for_status()

                weather_data = weather_response.json()
                hourly_data = weather_data.get('hourly', {})
                temperature_at_2pm = hourly_data.get('temperature_2m', [])

                # Cache key for each district without specifying a travel date
                cache_key = f'temperature_at_2pm_{district["name"]}'
                cache.set(cache_key, temperature_at_2pm)

                # print("checking", cache.get(cache_key))

                all_temperatures.extend(temperature_at_2pm)

        # Store all temperatures in a single cache key
        cache.set('temperature_data', all_temperatures)

    except requests.exceptions.RequestException as e:
        # Handle API request exceptions
        print(f"Error fetching weather data: {e}")
    except Exception as e:
        # Handle other exceptions
        print(f"Error: {e}")
