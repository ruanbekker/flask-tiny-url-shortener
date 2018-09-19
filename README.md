# flask-tiny-url-shortener
URL Shortener using Python Flask backed by SimpleDB

## Pre-Requirements

Install dependencies:

```
$ pip install -r requirements.txt
```

Create SimpleDB Domain:

```
$ python
>>> import boto3
>>> c = boto3.Session(region_name='eu-west-1', profile_name='dev')
>>> sdb = c.client('sdb')
>>> sdb.create_domain(DomainName='tiny-url')
```

Run Server:

```
$ python app.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Screenshots

Enter your URL to be shortened:

![](https://user-images.githubusercontent.com/567298/45783856-49c37600-bc67-11e8-93ba-22ba37484027.png)

Generated Tiny URL, with the copy button to copy to the clipboard

![](https://user-images.githubusercontent.com/567298/45783925-7d060500-bc67-11e8-878a-76810e525aa1.png)
