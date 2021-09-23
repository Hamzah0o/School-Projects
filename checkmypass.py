
import requests , hashlib , sys

def request_api_data(query_char):
    url= 'http://api.pwnedpasswords.com/range/' + query_char

    response_url = requests.get(url)
    return response_url

def pwned_api_check (password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5d , tail = sha1password[:5] , sha1password[5:]
    response_server = request_api_data(first5d)
    return get_password_count(response_server , tail)

def read_response(response):
    print(response.text)


def get_password_count( hashes , hash_to_check):
    hashes = (line.split(':') for line in hashes.text)
    for h , count in hashes:
        if h == hash_to_check:
            return  count
    return 0


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f{f'was found {count}')
            







