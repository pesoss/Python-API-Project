import json
import unittest
from unittest.mock import patch
from GitHubAPI.GitHubAPI import GitHubAPI
from FreshdeskAPI.FreshdeskAPI import FreshdeskAPI


class TestAPIs(unittest.TestCase):

    # Testing GitHub get request
    def test_github_response_get(self):
        with patch('GitHubAPI.GitHubAPI.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.text = 'Success'

            schedule = GitHubAPI.get_res('pesoss')
            mocked_get.assert_called_with('https://api.github.com/users/pesoss')
            self.assertEqual(schedule, 'Success')

    # Testing Freshdesk get request
    def test_freshdesk_response_get(self):
        with patch('FreshdeskAPI.FreshdeskAPI.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.text = 'Success'

            schedule = FreshdeskAPI.get_res('quickbase-help')
            url = 'https://quickbase-help.freshdesk.com/api/v2/contacts/'
            headers = {'Content-Type': 'application/json'}
            mocked_get.assert_called_with(url, auth=('j9mfm8FXVWknZDsqe5Wm', 'test'), headers=headers)
            self.assertEqual(schedule, 'Success')

    # Testing Freshdesk post request
    def test_freshdesk_response_post(self):
        with patch('FreshdeskAPI.FreshdeskAPI.requests.post') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.status_code = 201
            mocked_get.return_value.text = 'Success'

            user_data = {'name': 'Peter Petrov', 'twitter_id': 'test_twitter', 'unique_external_id': '102258071'}
            schedule = FreshdeskAPI.get_post(user_data, 'quickbase-help')
            url = 'https://quickbase-help.freshdesk.com/api/v2/contacts/'
            headers = {'Content-Type': 'application/json'}
            mocked_get.assert_called_with(url, auth=('j9mfm8FXVWknZDsqe5Wm', 'test'),
                                          data=json.dumps(user_data), headers=headers)
            self.assertEqual(schedule, 'Success')

    # Testing Freshdesk put request
    def test_freshdesk_response_put(self):
        with patch('FreshdeskAPI.FreshdeskAPI.requests.put') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.text = 'Success'

            user_data = {'name': 'Peter Petrov', 'twitter_id': 'test_twitter', 'unique_external_id': '102258071'}
            schedule = FreshdeskAPI.get_put(user_data, 'quickbase-help')
            url = 'https://quickbase-help.freshdesk.com/api/v2/contacts/'
            headers = {'Content-Type': 'application/json'}
            mocked_get.assert_called_with(url + '102258071', auth=('j9mfm8FXVWknZDsqe5Wm', 'test'),
                                          data=json.dumps(user_data), headers=headers)
            self.assertEqual(schedule, 'Success')


if __name__ == '__main__':
    unittest.main()
