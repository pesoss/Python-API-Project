import requests
import os
import json


class FreshdeskAPI:
    AUTH_TOKEN = os.environ.get('FRESHDESK_TOKEN')
    URL_EXTENSION = ".freshdesk.com/api/v2/contacts/"
    HEADERS = {"Content-Type": "application/json"}

    # With this function I check if there is an existing contact
    @classmethod
    def check_contact_exist(cls, user_data={}, subdomain={}):
        unique_external_id = user_data['unique_external_id']
        url = "https://" + str(subdomain) + cls.URL_EXTENSION
        response_id = requests.get(url, auth=(cls.AUTH_TOKEN, 'test'), headers=cls.HEADERS)
        if response_id.status_code == 200:
            for contact in response_id.json():
                if contact['unique_external_id'] == unique_external_id:
                    return True
            print('CHECK_CONTACT: Username not found!')
            return False
        print("Error: Broken request!")
        return False

    # With this function I get contact ID, created from Freshdesk
    @classmethod
    def get_id(cls, json_data, unique_external_id):
        for contact in json_data:
            if contact['unique_external_id'] == unique_external_id:
                return contact['id']
        print('GET_ID: Username not found!')
        return False

    # Function to create or update contact
    # First I check if there is an existing contact, if there is, the function updates the contact
    # If not, the function creates one
    @classmethod
    def create_or_update_contact(cls, user_data={}, subdomain={}):
        url = "https://" + str(subdomain) + cls.URL_EXTENSION
        main_response = requests.get(url, auth=(cls.AUTH_TOKEN, 'test'), headers=cls.HEADERS)
        contact_id = cls.get_id(main_response.json(), user_data["unique_external_id"])

        if cls.check_contact_exist(user_data, subdomain):
            if main_response.status_code == 200:
                url + str(contact_id)
                response = requests.put(url + str(contact_id), auth=(cls.AUTH_TOKEN, 'test'),
                                        data=json.dumps(user_data), headers=cls.HEADERS)
                print('response_put: ', response.status_code)
                if response.status_code == 200:
                    print('Contact updated!')
                else:
                    print('Contact was not updated!')
            else:
                print('Error: Broken request!')
        else:
            response_create = requests.post(url, auth=(cls.AUTH_TOKEN, 'test'),
                                            data=json.dumps(user_data), headers=cls.HEADERS)
            print('response_create: ', response_create.status_code)
            if response_create.status_code == 201:
                print("Successfully created contact!")
            else:
                print("Error: Unsuccessfully created contact!")

    # I create this function for delete contact for myself
    # I didn't use it in code
    @classmethod
    def delete_contact(cls, user_data={}, subdomain={}):
        url = "https://" + str(subdomain) + cls.URL_EXTENSION
        response_to_get_id = requests.get(url, auth=(cls.AUTH_TOKEN, 'test'), headers=cls.HEADERS)

        print('Delete response_to_get_id: ', response_to_get_id.status_code)
        check_id = cls.get_id(response_to_get_id.json(), user_data['unique_external_id'])

        print(url + str(check_id) + '/hard_delete?force=true')
        response = requests.delete(url + str(check_id) + '/hard_delete?force=true',
                                   auth=(cls.AUTH_TOKEN, 'test'), headers=cls.HEADERS)
        print('Delete response: ', response.status_code)

    # I use it in module TestAPIs to check get request for Freshdesk
    @classmethod
    def get_res(cls, subdomain):
        url = "https://" + str(subdomain) + cls.URL_EXTENSION
        response = requests.get(url, auth=(cls.AUTH_TOKEN, 'test'), headers=cls.HEADERS)
        if response.ok:
            return response.text
        else:
            return 'Bad request!'

    # I use it in module TestAPIs to check post request for Freshdesk
    @classmethod
    def get_post(cls, user_data, subdomain):
        url = "https://" + str(subdomain) + cls.URL_EXTENSION
        response = requests.post(url, auth=(cls.AUTH_TOKEN, 'test'),
                                 data=json.dumps(user_data), headers=cls.HEADERS)
        if response.ok:
            return response.text
        else:
            return 'Bad request!'

    # I use it in module TestAPIs to check put request for Freshdesk
    @classmethod
    def get_put(cls, user_data, subdomain):
        url = "https://" + str(subdomain) + cls.URL_EXTENSION
        response = requests.put(url + str(user_data['unique_external_id']), auth=(cls.AUTH_TOKEN, 'test'),
                                data=json.dumps(user_data), headers=cls.HEADERS)
        if response.ok:
            return response.text
        else:
            return 'Bad request!'
