from ...common_descs import *
from supyr_struct.defs.tag_def import TagDef

string_data_struct = rawtext_ref("string", FlStrUTF16, max_size=32768)

ustr_body = Struct("tagdata",
    reflexive("strings", string_data_struct, 32767),
    SIZE=12,
    )


def get():
    return ustr_def

ustr_def = TagDef("ustr",
    blam_header('ustr'),
    ustr_body,

    ext=".unicode_string_list", endian=">"
    )
