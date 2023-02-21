from ics import Calendar

from bd2.generate_events import generate_events_bd2
from bss.generate_events import generate_events_bss
from skps.generate_events import generate_events_skps
from swo.generate_events import generate_events_swo
from wmm.generate_events import generate_events_wmm
from wsyz.generate_events import generate_events_wsyz


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
    cal.events = cal.events.union(generate_events_wsyz())
    cal.events = cal.events.union(generate_events_swo())
    cal.events = cal.events.union(generate_events_skps())
    cal.events = cal.events.union(generate_events_bd2())
    with open('out.ics', 'w') as fp:
        fp.writelines(cal.serialize_iter())


if __name__ == '__main__':
    main()
