############# Credits and version info #############
# Definition generated from Assembly XML tag def
#	 Date generated: 2018/11/30  01:44
#
# revision: 1		author: Assembly
# 	Generated plugin from scratch.
# revision: 2		author: Lord Zedd
# 	Oh the xex has names.
# revision: 3		author: Moses_of_Egypt
# 	Cleaned up and converted to SuPyr definition
#
####################################################
from ..common_descs import *
from supyr_struct.defs.tag_def import TagDef


perf_performance = Struct("performance", 
    Bool32("flags", 
        ("disable_self_shadowing", 1 << 1),
        "disable_player_shadows",
        ),
    Float("water"),
    Float("decorators"),
    Float("effects"),
    Float("instanced_geometry"),
    Float("object_fade"),
    Float("object_lod"),
    Float("decals"),
    SInt32("cpu_light_count"),
    Float("cpu_light_quality"),
    SInt32("gpu_light_count"),
    Float("gpu_light_quality"),
    SInt32("shadow_count"),
    Float("shadow_quality"),
    ENDIAN=">", SIZE=56
    )


perf_meta_def = BlockDef("perf", 
    h3_reflexive("performance", perf_performance),
    TYPE=Struct, ENDIAN=">", SIZE=12
    )