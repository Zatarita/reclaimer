############# Credits and version info #############
# Definition generated from Assembly XML tag def
#	 Date generated: 2018/11/30  01:44
#
# revision: 1		author: -DeToX-
# 	Mapped plugin structure a new.
# revision: 2		author: DeadCanadian
# 	named most
# revision: 3		author: Lord Zedd
# 	h22222
# revision: 4		author: Moses_of_Egypt
# 	Cleaned up and converted to SuPyr definition
#
####################################################
from ..common_descs import *
from supyr_struct.defs.tag_def import TagDef

foot_effect_old_material_sweetener_mode = (
    "sweetener_default",
    "sweetener_enabled",
    "sweetener_disabled",
    )


foot_effect_old_material = Struct("old_material", 
    h3_dependency("effect"),
    h3_dependency("sound"),
    h3_string_id("material_name"),
    SInt16("global_material_index"),
    SEnum8("sweetener_mode", *foot_effect_old_material_sweetener_mode),
    SInt8("unknown", VISIBLE=False),
    ENDIAN=">", SIZE=40
    )


foot_effect_sound = Struct("sound", 
    h3_dependency("tag"),
    h3_dependency("secondary_tag"),
    h3_string_id("material_name"),
    SInt16("global_material_index"),
    SEnum8("sweetener_mode", *foot_effect_old_material_sweetener_mode),
    SInt8("unknown", VISIBLE=False),
    ENDIAN=">", SIZE=40
    )


foot_effect_effect = Struct("effect", 
    h3_dependency("tag"),
    h3_dependency("secondary_tag"),
    h3_string_id("material_name"),
    SInt16("global_material_index"),
    SEnum8("sweetener_mode", *foot_effect_old_material_sweetener_mode),
    SInt8("unknown", VISIBLE=False),
    ENDIAN=">", SIZE=40
    )


foot_effect = Struct("effect", 
    h3_reflexive("old_materials", foot_effect_old_material),
    h3_reflexive("sounds", foot_effect_sound),
    h3_reflexive("effects", foot_effect_effect),
    ENDIAN=">", SIZE=36
    )


foot_meta_def = BlockDef("foot", 
    h3_reflexive("effects", foot_effect),
    TYPE=Struct, ENDIAN=">", SIZE=12
    )