import boto3
from flask import Flask
from random import choice, randint
from string import ascii_letters

tiny_baseurl = 'https://tiny.domain.com/t'

c = boto3.Session(region_name='eu-west-1', profile_name='default')
sdb = c.client('sdb')

app = Flask(__name__)

def generate_tiny():
    tiny_key = ''.join(choice(ascii_letters) + str(randint(0,9)) for x in range(randint(8, 8)))
    return tiny_key

@app.route('/')
def main():
    return 'ok'

if __name__ == '__main__':
    app.run()
