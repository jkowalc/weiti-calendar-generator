import datetime
from dataclasses import dataclass


@dataclass
class CalendarSemester:
    code: str

    def get_full_name(self):
        full_name = 'rok akademicki '
        code_year = 2000 + int(self.code[:2])
        if self.code[2] == 'Z':
            begin_year = code_year
        else:
            begin_year = code_year - 1
        year_str = str(begin_year) + '/' + str(begin_year + 1)
        full_name += year_str
        if self.code[2] == 'Z':
            full_name += ' - sem. zimowy'
        else:
            full_name += ' - sem. letni'
        return full_name

    @staticmethod
    def get_current():
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        if month < 2 or (month == 2 and day < 18):
            return CalendarSemester(str(year - 2000 - 1) + 'Z')
        else:
            return CalendarSemester(str(year - 2000) + 'L')
