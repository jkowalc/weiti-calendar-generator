import grequests
import requests

COURSES = {
    'Informatyka': 'https://www.elka.pw.edu.pl/Studenci/Zalaczniki-i-formularze/Zalaczniki/Plany-modelowe-12/Informatyka-od-roku-2019-2020-1',
    'Automatyka i robotyka': 'https://www.elka.pw.edu.pl/Studenci/Zalaczniki-i-formularze/Zalaczniki/Plany-modelowe-12/Automatyka-i-robotyka-1',
    'Cyberbezpieczeństwo': 'https://www.elka.pw.edu.pl/Studenci/Zalaczniki-i-formularze/Zalaczniki/Plany-modelowe-12/Cyberbezpieczenstwo-1',
    'Elektronika': 'https://www.elka.pw.edu.pl/Studenci/Zalaczniki-i-formularze/Zalaczniki/Plany-modelowe-12/Elektronika-do-roku-2019-2020-1',
    'Telekomunikacja': 'https://www.elka.pw.edu.pl/Studenci/Zalaczniki-i-formularze/Zalaczniki/Plany-modelowe-12/Telekomunikacja-od-roku-2019-2020-1',
    'Inżynieria internetu rzeczy': 'https://www.elka.pw.edu.pl/Studenci/Zalaczniki-i-formularze/Zalaczniki/Plany-modelowe-12/Inzynieria-internetu-rzeczy-1',
}


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


def get_model_plan_url(course):
    return COURSES[course]
