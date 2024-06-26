import sys
import time

import pytest
import requests


def test_normal_behavior():
    retries = 3
    success = False
    while not success:
        try:
            endpoint = "/security-events/123_abc"
            response = requests.get(endpoint)

            assert response.status_code == 200
            assert "customer_email" in response.text, "customer_email is missing"
            assert "number_of_events" in response.text, "number_of_events is missing"
            # Not sure about events because its list
            assert "events" in response.text, "events is missing"
            assert "ip" in response.text, "ip is missing"
            assert "time" in response.text, "time is missing"
            # Not sure about event_type because it should be displayed in specific scenarios
            assert "event_type" in response.text, "event_type is missing"

            success = True

        except Exception as e:
            wait = retries * 30
            print('Error! Waiting %s secs and re-trying...' % wait)
            sys.stdout.flush()
            time.sleep(wait)
            retries += 1


def test_invalid_id():
    retries = 3
    success = False
    while not success:
        try:
            user_id = "321_abc"
            endpoint = "/security-events/" + user_id
            response = requests.get(endpoint)

            assert response.status_code == 400, 'status = ' + response.text
            assert response.text == 'User ID {} is invalid'.format(user_id)

            success = True

        except Exception as e:
            wait = retries * 30
            print('Error! Waiting %s secs and re-trying...' % wait)
            sys.stdout.flush()
            time.sleep(wait)
            retries += 1
