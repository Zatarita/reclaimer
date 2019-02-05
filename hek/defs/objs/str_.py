from .tag import *

class Str_Tag(HekTag):

    def calc_internal_data(self):
        HekTag.calc_internal_data(self)
        strings = self.data.tagdata.strings.STEPTREE

        for i in range(len(strings)):
            # replace all instances of \r and \n with \r\n
            split_strings = []
            for s in strings[i].data.split("\r\n"):
                for sub_s in s.split('\r'):
                    split_strings.extend(sub_s.split('\n'))

            new_string = split_strings.pop(0)
            for s in split_strings:
                new_string += "\r\n" + s

            strings[i].data = new_string
