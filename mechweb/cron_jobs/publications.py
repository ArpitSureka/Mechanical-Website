# This is cron job page to add research paper publiucations to professors Page

from scholarly import scholarly
from mechweb.models import FacultyPage
from urllib.parse import urlparse, parse_qs

def updateGoogleScholarPublications():
    all_faculty_data = FacultyPage.objects.all()
    for faculty_data in all_faculty_data:
        if faculty_data.google_scholar_profile_link :
            parsed_url = urlparse(faculty_data.google_scholar_profile_link)
            query_params = parse_qs(parsed_url.query)
            user_id = query_params.get('user', [''])[0]
            author = scholarly.search_author_id(user_id)
            scholarly.pprint(author)