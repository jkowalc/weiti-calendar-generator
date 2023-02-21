from ics import Calendar
from ics.grammar.parse import ContentLine

from bss.generate_events import generate_events_bss
from wmm.generate_events import generate_events_wmm


def main():
    cal = Calendar()
    bss_group = ''
    print('Możliwości: 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, brak')
    while bss_group not in ['101', '102', '103', '104', '105', '106', '107', '108', '109', '110', 'brak']:
        bss_group = input('Podaj grupę BSS: ')
    cal.events = cal.events.union(generate_events_bss(bss_group))
    wmm_group = ''
    print('Możliwości: 101, 102, 103, 104, 105, 106, 107, 108, brak')
    while wmm_group not in ['101', '102', '103', '104', '105', '106', '107', '108', 'brak']:
        wmm_group = input('Podaj grupę WMM: ')
    cal.events = cal.events.union(generate_events_wmm(wmm_group))
    with open('out.ics', 'w') as fp:
        fp.writelines(cal.serialize_iter())


if __name__ == '__main__':
    main()
