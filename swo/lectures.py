lectures_topics = [
    'Organizacja, podstawy (Nowak)',
    'Styl kodowania (Grochowski)',
    'Wzorce projektowe 1 (Nowak)',
    'Wzorce projektowe 2 (Nowak), Git (Wysota)',
    'UML (Grochowski)',
    'Cykl wytwarzania oprogramowania 1 (Grochowski)',
    'Cykl wytwarzania oprogramowania 2 (Grochowski)',
    'Ocena jakości kodu i testów (Grochowski)',
    'Kolokwium nr 1, Wzorce projektowe 3 (Nowak)',
    'Monitorowanie i analiza aplikacji (Grochowski)',
    'Refaktoring i praca z kodem zastanym (Grochowski)',
    'Współbieżne wzorce projektowe 1 (Nowak)',
    'Współbieżne wzorce projektowe 2 (Nowak)',
    'Kolokwium nr 2',
    'Zasowy internetowe i standardy (Nowak)'
]

lectures_schedule = [
    (20, 2),
    (27, 2),
    (6, 3),
    (13, 3),
    (20, 3),
    (27, 3),
    (3, 4),
    (17, 4),
    (24, 4),
    (8, 5),
    (15, 5),
    (22, 5),
    (29, 5),
    (5, 6),
    (12, 6)
]

if __name__ == '__main__':
    assert len(lectures_schedule) == len(lectures_topics)
