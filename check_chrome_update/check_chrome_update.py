import logging
from datetime import datetime
import requests

logging.basicConfig(format='%(asctime)s:%(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CustomException(Exception):
    pass


URL_TAG = 'https://quay.io/api/v1/repository/browser/google-chrome-stable/tag/'


def check_chrome_update():
    # https://quay.io/repository/browser/google-chrome-stable?tab=tags - ui
    tags = get_tags()
    latest_tag = [tag for tag in tags if tag['name'] == 'latest'][0]
    latest_v = [
        tag for tag in tags if tag['manifest_digest'] == latest_tag['manifest_digest'] and tag['name'] != 'latest'
    ][0]['name']
    upd_days = count_days(latest_tag['last_modified'])
    minor_v_tags = [tag for tag in tags if latest_v in tag['name']]
    minor_v_exist = True if len(minor_v_tags) > 2 else False
    if upd_days < 2 and not minor_v_exist:
        raise CustomException(f'Chrome version has been updated {upd_days} day(s) ago to {latest_v} version.')
    logger.info(f'Version is not updated. Current version is {latest_v} has been updated {upd_days} day(s) ago.')


def get_tags():
    response = requests.get(URL_TAG, params={'limit': 100, 'page': 1, 'onlyActiveTags': True})
    response.raise_for_status()
    format_response = response.json()
    return format_response['tags']


def count_days(start_date, end_date=None):
    end_date = datetime.strptime(end_date, '%a, %d %b %Y %H:%M:%S -%f') if end_date else datetime.now()
    start_date = datetime.strptime(start_date, '%a, %d %b %Y %H:%M:%S -%f')
    return (end_date - start_date).days


if __name__ == '__main__':
    check_chrome_update()
