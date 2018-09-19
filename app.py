import boto3
from flask import Flask
from random import choice, randint
from string import ascii_letters

c = boto3.Session(region_name='eu-west-1', profile_name='default')
sdb = c.client('sdb')

sdb_domain = 'tiny-url'
tiny_baseurl = 'https://tiny.domain.com/t'

app = Flask(__name__)

def generate_tiny():
    tiny_key = ''.join(choice(ascii_letters) + str(randint(0,9)) for x in range(randint(8, 8)))
    return tiny_key

def put_url(destination_url):
    tiny_id = generate_tiny()
    tiny_url = '{}/{}'.format(tiny_baseurl, tiny_id)
    response = sdb.put_attributes(
        DomainName=sdb_domain, 
        ItemName=tiny_id, 
        Attributes=[{
            'Name': tiny_url, 
            'Value': destination_url
        }]
    )
    return tiny_url

@app.route('/')
def main():
    return 'ok'

if __name__ == '__main__':
    app.run()
