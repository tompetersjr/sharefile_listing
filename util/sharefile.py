import requests


class ShareFile:
    def __init__(self, hostname, client_id, client_secret, username, password):
        self.hostname = hostname
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password
        self.token = None

        self.authenticate()

    def authenticate(self):
        uri_path = '/oauth/token'

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = {
            'grant_type': 'password',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'username': self.username,
            'password': self.password
        }

        url = "https://{}{}".format(self.hostname, uri_path)
        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            self.token = response.json()

        return self.token

    def get_authorization_header(self):
        return {'Authorization': 'Bearer {}'.format(self.token['access_token'])}

    def get_hostname(self):
        return '{}.sf-api.com'.format(self.token['subdomain'])

    def get_folder_templates(self):
        uri_path = '/sf/v3/FolderTemplates'

        headers = self.get_authorization_header()

        url = "https://{}{}".format(self.get_hostname(), uri_path)
        response = requests.get(url, headers=headers)

        templates = None
        if response.status_code == 200:
            templates = response.json()

        return templates

    def get_folder_templates_folders(self, folder_id):
        uri_path = '/sf/v3/FolderTemplates'

        headers = self.get_authorization_header()

        url = "https://{}{}({})".format(self.get_hostname(), uri_path, folder_id)
        response = requests.get(url, headers=headers)

        templates = None
        if response.status_code == 200:
            templates = response.json()

        return templates
