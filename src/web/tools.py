from time import sleep

import grequests
import requests

from src.scrapers.exceptions import USOSError
from src.web.exceptions import NetworkError


def check_ok(responses):
    for r in responses:
        if r.text is None:
            raise NetworkError()


def map_single_url(url, func, *args, **kwargs):
    response = requests.get(url)
    text = response.text
    if text is None:
        raise NetworkError()
    return func(text, *args, **kwargs)


def map_multiple_urls(urls, func, *args, **kwargs):
    if isinstance(urls, list):
        rs = (grequests.get(u) for u in urls)
        responses = grequests.map(rs)
        check_ok(responses)
        return [func(r.text, *args, **kwargs) for r in responses]
    elif isinstance(urls, dict):
        rs = (grequests.get(u) for u in urls.values())
        responses = grequests.map(rs)
        check_ok(responses)
        return {k: func(r.text, *args) for k, r in zip(urls.keys(), responses)}
    else:
        raise TypeError('urls must be list or dict')


def retry_if_network_error(func, *args, **kwargs):
    while True:
        try:
            return func(*args, **kwargs)
        except NetworkError:
            print("Bład z połączeniem, ponawiam próbę...")
            sleep(0.1)
        except USOSError:
            print("Bład USOS, ponawiam próbę...")
            sleep(0.1)
