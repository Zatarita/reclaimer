############# Credits and version info #############
# Definition autogenerated from Assembly XML tag def
#
# revision: 1		author: -DeToX-
# 	Created layout of plugin
# revision: 2		author: DeadCanadian
# 	naming tags
# revision: 3		author: Moses_of_Egypt
# 	Cleaned up and converted to SuPyr definition
#
####################################################
from reclaimer.common_descs import *
from supyr_struct.defs.tag_def import TagDef


bsdt_unknown0 = Struct("unknown0", 
    BytesRaw("unknown_0", SIZE=8, VISIBLE=False),
    rawdata_ref("unknown_1", VISIBLE=False),
    BytesRaw("unknown_2", SIZE=8, VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=36
    )


bsdt_unknown1 = Struct("unknown1", 
    BytesRaw("unknown_0", SIZE=8, VISIBLE=False),
    rawdata_ref("unknown_1", VISIBLE=False),
    BytesRaw("unknown_2", SIZE=8, VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=36
    )


bsdt_meta_def = BlockDef("bsdt", 
    Float("maximum_vitality"),
    dependency("effect"),
    dependency("sound"),
    BytesRaw("unknown_0", SIZE=16, VISIBLE=False),
    dependency("crack_bitmap"),
    dependency("hole_bitmap"),
    BytesRaw("unknown_1", SIZE=36, VISIBLE=False),
    reflexive("unknown0", bsdt_unknown0),
    BytesRaw("unknown_2", SIZE=12, VISIBLE=False),
    reflexive("unknown1", bsdt_unknown1),
    BytesRaw("unknown_3", SIZE=4, VISIBLE=False),
    TYPE=Struct, ENDIAN=">", SIZE=160
    )