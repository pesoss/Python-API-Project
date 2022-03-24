import argparse
from GitHubAPI.GitHubAPI import GitHubAPI
from FreshdeskAPI.FreshdeskAPI import FreshdeskAPI


def read_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument('username', type=str, help='GitHub username')
    parser.add_argument('subdomain', type=str, help='Freshdesk subdomain')
    return vars(parser.parse_args())


def main():
    args = read_command_line()
    username = args['username']
    subdomain = args['subdomain']

    user = GitHubAPI.authenticate_user(username)
    FreshdeskAPI.create_or_update_contact(user, subdomain)


if __name__ == "__main__":
    main()
