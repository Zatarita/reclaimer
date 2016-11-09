from ...common_descs import *
from supyr_struct.defs.tag_def import TagDef

build_info = Struct("build info",
    BSEnum32("build stage",
        "ship",
        "alpha",
        "beta",
        "delta",
        "epsilon",
        "release",
        ),
    BSInt32("revision"),
    SIZE=48
    )

scripted_ui_widget = Struct("scripted ui widget",
    ascii_str32("name"),
    dependency_os("definition", "DeLa"),
    SIZE=76
    )

parameter = Struct("parameter",
    BSEnum16("type", *script_object_types),
    SIZE=2
    )

new_function = Struct("new function",
    ascii_str32("name1"),
    ascii_str32("name2"),
    BSInt16("override index"),
    BSEnum16("return type", *script_object_types),
    reflexive("parameters", parameter),
    SIZE=80
    )

new_global = Struct("new global",
    ascii_str32("name1"),
    ascii_str32("name2"),
    BSInt16("override index"),
    BSEnum16("type", *script_object_types),
    SIZE=68
    )

yelo_scripting = Struct("yelo scripting",
    reflexive("new functions", new_function),
    reflexive("new globals", new_global),
    SIZE=24
    )

yelo_body = Struct("tagdata",
    BSInt16("version"),
    BBool16("flags",
        "dont fix ui game globals",
        "game updates ignore player pvs hack",
        ),
    dependency_os("yelo globals", "yelo"),
    dependency_os("globals override", "matg"),
    dependency_os("scenario explicit references", "tagc"),
    reflexive("build info", build_info, 1),

    Pad(40),
    reflexive("scripted ui widgets", scripted_ui_widget, 128),

    Pad(16),
    # Physics
    BFloat("gravity scale", MIN=0.0, MAX=2.0),
    BFloat("player speed scale", MIN=0.0, MAX=6.0),

    Pad(44),
    BBool32("gameplay model",
        "prohibit multi-team vehicles",
        ),

    Pad(20),
    reflexive("yelo scripting", yelo_scripting, 1),
    #reflexive("unknown", void_desc),

    SIZE=312
    )

def get():
    return yelo_def

yelo_def = TagDef("yelo",
    blam_header_os('yelo', 2),
    yelo_body,

    ext=".project_yellow", endian=">"
    )