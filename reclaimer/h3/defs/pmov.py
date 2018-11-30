############# Credits and version info #############
# Definition generated from Assembly XML tag def
#	 Date generated: 2018/11/30  01:44
#
# revision: 1		author: Assembly
# 	Generated plugin from scratch.
# revision: 2		author: Lord Zedd
# 	Copypasta H2.
# revision: 3		author: Moses_of_Egypt
# 	Cleaned up and converted to SuPyr definition
#
####################################################
from ..common_descs import *
from supyr_struct.defs.tag_def import TagDef

pmov_movement_type = (
    "physics",
    "collider",
    "swarm",
    "wind",
    )


pmov_movement_parameter = Struct("parameter", 
    SInt32("parameter_id"),
    SInt16("unknown_0", VISIBLE=False),
    SInt16("unknown_1", VISIBLE=False),
    h3_rawdata_ref("function"),
    Float("unknown_2", VISIBLE=False),
    UInt8("unknown_3", VISIBLE=False),
    SInt8("unknown_4", VISIBLE=False),
    SInt8("unknown_5", VISIBLE=False),
    SInt8("unknown_6", VISIBLE=False),
    ENDIAN=">", SIZE=36
    )


pmov_movement = Struct("movement", 
    SEnum16("type", *pmov_movement_type),
    SInt16("unknown_0", VISIBLE=False),
    h3_reflexive("parameters", pmov_movement_parameter),
    SInt16("unknown_1", VISIBLE=False),
    SInt16("unknown_2", VISIBLE=False),
    SInt32("unknown_3", VISIBLE=False),
    ENDIAN=">", SIZE=24
    )


pmov_meta_def = BlockDef("pmov", 
    h3_dependency("template"),
    Bool32("flags", 
        "physics",
        "collide_with_structure",
        "collide_with_media",
        "collide_with_scenery",
        "collide_with_vehicles",
        "collide_with_bipeds",
        "swarm",
        "wind",
        ),
    h3_reflexive("movements", pmov_movement),
    TYPE=Struct, ENDIAN=">", SIZE=32
    )