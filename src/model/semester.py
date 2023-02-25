from dataclasses import dataclass


@dataclass
class Semester:
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
