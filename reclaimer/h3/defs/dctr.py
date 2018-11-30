############# Credits and version info #############
# Definition generated from Assembly XML tag def
#	 Date generated: 2018/11/30  01:44
#
# revision: 1		author: -DeToX-
# 	Created layout of plugin
# revision: 2		author: Moses_of_Egypt
# 	Cleaned up and converted to SuPyr definition
#
####################################################
from ..common_descs import *
from supyr_struct.defs.tag_def import TagDef


dctr_meta_def = BlockDef("dctr", 
    h3_dependency("model"),
    BytesRaw("unknown_0", SIZE=12, VISIBLE=False),
    SInt32("unknown_1", VISIBLE=False),
    h3_dependency("texture"),
    SInt16("affects_visibility"),
    SInt16("unknown_2"),
    color_rgb_float("color"),
    BytesRaw("unknown_3", SIZE=20, VISIBLE=False),
    Float("brightness_base"),
    Float("brightness_shadow"),
    BytesRaw("unknown_4", SIZE=36, VISIBLE=False),
    TYPE=Struct, ENDIAN=">", SIZE=128
    )