import boto3
from flask import Flask, render_template, url_for, redirect, request
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

def get_url(tiny_url):
    tiny_id = tiny_url.split('/')[-1]
    item = sdb.get_attributes(
        DomainName=sdb_domain, 
        ItemName=tiny_id
    )
    response = item.get('Attributes')[0].get('Value')
    return response

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    url = request.form["input"]
    if 'http' in url.split('.')[0]:
        tiny_url = put_url(url)
        return render_template('result.html', tiny_url=tiny_url)
    else:
        message = 'URL needs to include http or https'
        return render_template('result.html', tiny_url=message)
    
@app.route('/t/<tinyid>')
def redirect_it(tinyid):
    full_url = get_url(tinyid)
    return redirect(full_url)

if __name__ == '__main__':
    app.run()
