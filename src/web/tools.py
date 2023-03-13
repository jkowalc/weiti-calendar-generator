import grequests
import requests


def map_single_url(url, func, *args, **kwargs):
    response = requests.get(url)
    text = response.text
    if text is None:
        raise Exception('Given url returns empty website!')
    return func(text, *args, **kwargs)


def map_multiple_urls(urls, func, *args, **kwargs):
    if isinstance(urls, list):
        rs = (grequests.get(u) for u in urls)
        responses = grequests.map(rs)
        return [func(r.text, *args, **kwargs) for r in responses]
    elif isinstance(urls, dict):
        rs = (grequests.get(u) for u in urls.values())
        responses = grequests.map(rs)
        return {k: func(r.text, *args, **kwargs) for k, r in zip(urls.keys(), responses)}
    else:
        raise TypeError('urls must be list or dict')

