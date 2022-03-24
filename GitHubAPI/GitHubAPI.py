from Users.Users import Users
import requests
import os


class GitHubAPI:
    GITHUB_AUTH_TOKEN = os.environ.get('GITHUB_TOKEN')
    GITHUB_MAIN_URL = 'https://api.github.com/users/'
    user = {}

    @classmethod
    def authenticate_user(cls, username):
        url = cls.GITHUB_MAIN_URL + username
        headers = {'Authorization': 'token' + cls.GITHUB_AUTH_TOKEN}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            raw_data = response.json()
            user_data = Users(raw_data)
            cls.user = user_data.get_user_data()
            return cls.user
        else:
            print('Error: Invalid GutHub username!')
            return False

    # I use it in module TestAPIs to check get request for GitHub
    @classmethod
    def get_res(cls, username):
        url = cls.GITHUB_MAIN_URL + username
        headers = {'Authorization': 'token' + cls.GITHUB_AUTH_TOKEN}
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            return 'Bad request!'
