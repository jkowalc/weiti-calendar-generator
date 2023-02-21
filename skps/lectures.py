lectures_topics = [
    'Wprowadzenie (Winiarski)',
    'Środowiska do zastosowań wbudowanych i sterowania (Zabołotny)',
    'Zaawansowane użycie BR, Wprowadzenie do OpenWRT (Zabołotny)',
    'Realizacja komunikacji między procesowej (Zabołotny)',
    'QEMU, Komunikacja z urządzeniami I/O (Zabołotny)',
    'Techniki przystowania Linuxa do czasu rzeczywistego (Zabołotny)',
    'Kolokwium nr 1',
    'SoC i MPSoC (Zabołotny)',
    'Sprzęt z naciskiem na sterowniki (Winiarski)',
    'Organizacja oprogramowania bez systemu operacyjnego (Winiarski)',
    'Przykładowy system z mikrokontrolerem (Winiarski)',
    'Szeregowanie zadań i aspekty bezpieczeństwa (Winiarski)',
    'Sieci przemysłowe (Winiarski)',
    'Kolokwium nr 2',
    'Kolokwium poprawkowe'
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
