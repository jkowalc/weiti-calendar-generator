import grequests


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


def get_model_plan_url(course):
    return 'https://google.pl'
