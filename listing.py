import argparse
import os
import requests
import sys
import traceback

from util.sharefile import ShareFile


def main():
    try:
        parser = argparse.ArgumentParser(description='Export ShareFile '
                                         'Template Folder Listings')
        parser.add_argument('-c',
                            metavar='CLIENTID',
                            required=False,
                            dest='clientid',
                            help='ShareFile ClientId. (Required'
                            'if not exported as SHAREFILE_CLIENTID)')
        parser.add_argument('-n',
                            metavar='HOSTNAME',
                            required=False,
                            dest='hostname',
                            help='ShareFile Host Name. (Required'
                            'if not exported as SHAREFILE_HOSTNAME)')
        parser.add_argument('-p',
                            metavar='PASSWORD',
                            required=False,
                            dest='password',
                            help='ShareFile Password. (Required'
                            'if not exported as SHAREFILE_PASSWORD)')
        parser.add_argument('-s',
                            metavar='SECRET',
                            required=False,
                            dest='secret',
                            help='ShareFile Secret Key. (Required'
                            'if not exported as SHAREFILE_SECRET)')
        parser.add_argument('-u',
                            metavar='USERNAME',
                            required=False,
                            dest='username',
                            help='ShareFile User Name. (Required '
                            'if not exported as SHAREFILE_USERNAME)')

        args = None
        try:
            args = parser.parse_args()
        except:
            pass

        if args:
            hostname = args.hostname
            clientid = args.clientid
            secret = args.secret
            username = args.username
            password = args.password
            error = False

            if hostname is None:
                hostname = os.getenv('SHAREFILE_HOSTNAME')
                if hostname is None:
                    error = True
                    print('\nYou must specify a hostname as a parameter or export it.'
                          '\n\nExample:'
                          '\n\nParameter: -n HOSTNAME  ShareFile Host Name.'
                          '\nExport:    export SHAREFILE_HOSTNAME="hostname"\n')

            if clientid is None:
                clientid = os.getenv('SHAREFILE_CLIENTID')
                if clientid is None:
                    error = True
                    print('\nYou must specify a client id as a parameter or export it.'
                          '\n\nExample:'
                          '\n\nParameter: -c CLIENTID  ShareFile Client ID.'
                          '\nExport:    export SHAREFILE_CLIENTID="clientid"\n')

            if secret is None:
                secret = os.getenv('SHAREFILE_SECRET')
                if secret is None:
                    error = True
                    print('\nYou must specify a secret as a parameter or export it.'
                          '\n\nExample:'
                          '\n\nParameter: -s SECRET  ShareFile Secret.'
                          '\nExport:    export SHAREFILE_SECRET="secret"\n')

            if username is None:
                username = os.getenv('SHAREFILE_USERNAME')
                if username is None:
                    error = True
                    print('\nYou must specify a username as a parameter or export it.'
                          '\n\nExample:'
                          '\n\nParameter: -u USERNAME  ShareFile Username.'
                          '\nExport:    export SHAREFILE_USERNAME="username"\n')

            if password is None:
                password = os.getenv('SHAREFILE_PASSWORD')
                if password is None:
                    error = True
                    print('\nYou must specify a password as a parameter or export it.'
                          '\n\nExample:'
                          '\n\nParameter: -p PASSWORD  ShareFile Password.'
                          '\nExport:    export SHAREFILE_PASSWORD="password"\n')

            if error:
                return

            sharefile = ShareFile(hostname=hostname,
                                  client_id=clientid,
                                  client_secret=secret,
                                  username=username,
                                  password=password)

            templates = sharefile.get_folder_templates()

            for template in templates['value']:
                print('Template: {} - {}'.format(template['Name'], template['Description']))
                folders = sharefile.get_folder_templates_folders(template['Id'])
                print(folders)

    except:
        print('\n--- E R R O R ---\n')
        traceback.print_exc(file=sys.stdout)
        print('\n')
        return

if __name__ == "__main__":
    sys.exit(main())
