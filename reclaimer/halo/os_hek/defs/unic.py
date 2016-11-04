from ...common_descs import *
from supyr_struct.defs.tag_def import TagDef

string_reference = Struct("string reference",
    dependency("string id", valid_string_id_yelo),
    BSInt32("english offset"),
    BSInt32("unused offset 1"),
    BSInt32("unused offset 2"),
    BSInt32("unused offset 3"),
    BSInt32("unused offset 4"),
    BSInt32("unused offset 5"),
    BSInt32("unused offset 6"),
    BSInt32("unused offset 7"),
    BSInt32("unused offset 8"),
    SIZE=56
    )

unic_body = Struct("tagdata",
    reflexive("string references", string_reference),
    Pad(12),
    rawdata_ref("string data utf8", StrUtf8),

    SIZE=80
    )

def get():
    return unic_def

unic_def = TagDef("unic",
    blam_header_os('unic', 0),
    unic_body,

    ext=".multilingual_unicode_string_list", endian=">"
    )
