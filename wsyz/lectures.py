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

lectures_topics = [
    'Organizacja, systemy informacyjne',
    'Architektury systemów i inne aspekty 1',
    'Architektury systemów i inne aspekty 2',
    'Modelowanie procesów biznesowych',
    'Przegląd modeli analitycznych',
    'Wybrane modele optymalizacyjne 1',
    'Wybrane modele optymalizacyjne 2',
    'Kolokwium nr 1',
    'Harmonogramowanie i szeregowanie zadań 1',
    'Harmonogramowanie i szeregowanie zadań 2',
    'Planowanie produkcji i usług',
    'Metody zarządzania dystrybucją i lokalizacją',
    'Systemy ERP z przykładami',
    'Systemy Business Intelligence i Big Data',
    'Kolokwium nr 2'
]

if __name__ == '__main__':
    assert len(lectures_schedule) == len(lectures_topics)
