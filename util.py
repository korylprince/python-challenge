import io

import bs4
import requests
from PIL import Image


def print_url(code, prefix="def"):
    print("http://www.pythonchallenge.com/pc/{0}/{1}.html".format(prefix, code))


def get_url(url, auth=None):
    return requests.get(url, auth=auth).text


def get_url_file(url, auth=None):
    return io.BytesIO(requests.get(url, auth=auth).content)


def get_url_image(url, auth=None):
    return Image.open(get_url_file(url, auth))


def get_url_soup(url, auth=None):
    return bs4.BeautifulSoup(get_url(url, auth), "html.parser")


def get_url_comments(url, auth=None):
    soup = get_url_soup(url, auth)
    return soup.findAll(string=lambda text: isinstance(text, bs4.Comment))
