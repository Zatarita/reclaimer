############# Credits and version info #############
# Definition generated from Assembly XML tag def
#	 Date generated: 2018/11/30  01:44
#
# revision: 1		author: Assembly
# 	Generated plugin from scratch.
# revision: 2		author: Veegie
# 	Fixed some shit
# revision: 3		author: Lord Zedd
# 	Standardizing
# revision: 4		author: Moses_of_Egypt
# 	Cleaned up and converted to SuPyr definition
#
####################################################
from ..common_descs import *
from supyr_struct.defs.tag_def import TagDef


sefc_screen_effect = Struct("screen_effect", 
    h3_string_id("name"),
    SInt16("unknown_0", VISIBLE=False),
    SInt16("unknown_1", VISIBLE=False),
    Float("unknown_2", VISIBLE=False),
    h3_rawdata_ref("function_0", VISIBLE=False),
    Float("duration"),
    h3_rawdata_ref("function_1", VISIBLE=False),
    h3_rawdata_ref("function_2", VISIBLE=False),
    Float("light_intensity"),
    Pad(8),
    Float("saturation"),
    Float("color_muting"),
    Float("brightness"),
    Float("darkness"),
    Float("shadow_brightness"),
    color_rgb_float("tint"),
    color_rgb_float("tone"),
    ENDIAN=">", SIZE=132
    )


sefc_meta_def = BlockDef("sefc", 
    h3_reflexive("screen_effect", sefc_screen_effect),
    TYPE=Struct, ENDIAN=">", SIZE=12
    )