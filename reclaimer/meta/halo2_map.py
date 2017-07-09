import zlib
import os

from ..h2.common_descs import *
from supyr_struct.defs.tag_def import TagDef


def tag_name_table_name_pointer(parent=None, new_value=None, **kwargs):
    header = parent.parent.parent.parent
    if new_value is None:
        if parent.offset == -1:
            return header.tag_name_table_offset
        return header.tag_name_table_offset + parent.offset
    parent.offset = new_value - header.tag_name_table_offset


def string_id_table_name_pointer(parent=None, new_value=None, **kwargs):
    header = parent.parent.parent.parent
    if new_value is None:
        if parent.offset == -1:
            return header.string_id_table_offset
        return header.string_id_table_offset + parent.offset
    parent.offset = new_value - header.string_id_table_offset


tag_name_table_entry = Container("tag name table entry",
    SInt32("offset"),
    STEPTREE=CStrLatin1("tag name", POINTER=tag_name_table_name_pointer),
    )

string_id_table_entry = Container("string id table entry",
    SInt32("offset"),
    STEPTREE=CStrLatin1("string id", POINTER=string_id_table_name_pointer),
    )


tag_name_table = Array("tag name table",
    SIZE="..tag_name_count", SUB_STRUCT=tag_name_table_entry,
    POINTER="..tag_name_index_offset"
    )

string_id_table = Array("string id table",
    SIZE="..string_id_count", SUB_STRUCT=string_id_table_entry,
    POINTER="..string_id_index_offset"
    )


halo2_map_header = Struct("map header",
    UEnum32('head', ('head', 'head'), EDITABLE=False, DEFAULT='head'),
    UEnum32("version",
        ("halo1xbox",   5),
        ("halo1pcdemo", 6),
        ("halo1pc", 7),
        ("halo2", 8),
        ("halo3", 11),
        ("halo1ce", 609),
        ),
    UInt32("decomp len"),
    UInt32("unknown0"),
    UInt32("tag index header offset"),
    UInt32("tag data size"),
    UInt32("meta size"),
    UInt32("meta offset mask"),
    UInt32("unknown1"),
    UInt32("unknown2"),
    UInt32("unknown3"),
    Pad(256),

    ascii_str32("build date"),
    UEnum16("map type",
        "sp",
        "mp",
        "ui",
        "shared",
        "sharedsp",
        ),
    Pad(2),
    UInt32("crc32"),
    Pad(16),
    UInt32("crazy data offset"),
    UInt32("crazy data len"),
    UInt32("string id padded offset"),  # what is this?
    UInt32("string id count"),
    UInt32("string id table size"),
    UInt32("string id index offset"),
    UInt32("string id table offset"),
    Pad(36),
    ascii_str32("map name"),
    Pad(4),
    StrLatin1("scenario tag path", SIZE=260),
    UInt32("tag name count"),
    UInt32("tag name table offset"),
    UInt32("tag name table size"),
    UInt32("tag name index offset"),
    UInt32("checksum"),
    UInt32("unknown4"),
    UInt32("unknown5"),
    UInt32("unknown offset0"),
    UInt32("unknown offset1"),
    UInt32("unknown6"),
    Pad(1288),
    UEnum32('foot', ('foot', 'foot'), EDITABLE=False, DEFAULT='foot'),
    SIZE=2048,
    STEPTREE=Container("strings",
        string_id_table,
        tag_name_table,
        )
    )

halo2_tag_type = Struct("tag header",
    UEnum32("class 1", GUI_NAME="primary tag class",   INCLUDE=valid_h2_tags),
    UEnum32("class 2", GUI_NAME="secondary tag class", INCLUDE=valid_h2_tags),
    UEnum32("class 3", GUI_NAME="tertiary tag class",  INCLUDE=valid_h2_tags)
    )

halo2_tag_header = Struct("tag header",
    UEnum32("tag class", INCLUDE=valid_h2_tags),
    tag_id_struct,
    UInt32("offset"),
    UInt32("size"),
    SIZE=16
    )

halo2_tag_types_array = Array("tag types",
    SIZE=".tag_types_count", SUB_STRUCT=halo2_tag_type,
    )

halo2_tag_index_array = TagIndex("tag index",
    SIZE=".tag_count", SUB_STRUCT=halo2_tag_header,
    )

halo2_tag_index = Container("tag index",
    UInt32("tag types offset"),
    UInt32("tag types count"),
    UInt32("tag index offset"),

    QStruct("scenario tag id", INCLUDE=tag_id_struct),
    QStruct("globals tag id", INCLUDE=tag_id_struct),

    UInt32("crc32"),
    UInt32("tag count"),
    UInt32("tag sig", EDITABLE=False, DEFAULT='tags'),

    halo2_tag_types_array,
    halo2_tag_index_array
    )

halo2_map_header_def = BlockDef(halo2_map_header)
halo2_tag_index_def = BlockDef(halo2_tag_index)