############# Credits and version info #############
# Definition generated from Assembly XML tag def
#	 Date generated: 2018/11/30  01:44
#
# revision: 1		author: Assembly
# 	Generated plugin from scratch.
# revision: 2		author: DeadCanadian
# 	naming
# revision: 3		author: Lord Zedd
# 	Updated and copypasted.
# revision: 4		author: Moses_of_Egypt
# 	Cleaned up and converted to SuPyr definition
#
####################################################
from ..common_descs import *
from supyr_struct.defs.tag_def import TagDef


bmp3_meta_def = BlockDef("bmp3", 
    Bool32("flags", 
        ("scale_to_bounds", 1 << 3),
        "replace_with_blur",
        ("replace_with_white", 1 << 10),
        "replace_with_black",
        ),
    h3_string_id("name"),
    SInt16("unknown_0", VISIBLE=False),
    SInt16("layer"),
    SInt16("widescreen_y_bounds_min"),
    SInt16("widescreen_x_bounds_min"),
    SInt16("widescreen_y_bounds_max"),
    SInt16("widescreen_x_bounds_max"),
    SInt16("standard_y_bounds_min"),
    SInt16("standard_x_bounds_min"),
    SInt16("standard_y_bounds_max"),
    SInt16("standard_x_bounds_max"),
    h3_dependency("animation"),
    h3_dependency("bitmap"),
    h3_dependency("unknown_1"),
    SEnum16("blend_method", *bmp3_blend_method),
    SInt16("unknown_2", VISIBLE=False),
    SInt16("sprite_index"),
    SInt16("unknown_3", VISIBLE=False),
    h3_string_id("data_source_name"),
    h3_string_id("sprite_data_source_name"),
    TYPE=Struct, ENDIAN=">", SIZE=92
    )