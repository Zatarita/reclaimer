############# Credits and version info #############
# Definition autogenerated from Assembly XML tag def
#
# revision: 1		author: Assembly
# 	Generated plugin from scratch.
# revision: 2		author: -DeToX-
# 	Named Some Values...
# revision: 3		author: Lord Zedd
# 	Standardizing.
# revision: 4		author: Moses_of_Egypt
# 	Cleaned up and converted to SuPyr definition
#
####################################################
from reclaimer.common_descs import *
from supyr_struct.defs.tag_def import TagDef

beam_beam_system_output_kind_0 = (
    "none",
    "plus",
    "times",
    )

unknown_flags_8 = tuple("bit_%s" % i for i in range(8))


beam_beam_system_unknown_0 = Struct("unknown_0", 
    SInt16("unknown", VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=2
    )


beam_beam_system_import_data_function = Struct("function", 
    SInt32("unknown_0", VISIBLE=False),
    string_id_meta("name"),
    BytesRaw("unknown_1", SIZE=8, VISIBLE=False),
    rawdata_ref("function"),
    ENDIAN=">", SIZE=36
    )


beam_beam_system_import_data = Struct("import_data", 
    string_id_meta("material_type"),
    SInt32("unknown_0", VISIBLE=False),
    dependency("bitmap"),
    BytesRaw("unknown_1", SIZE=4, VISIBLE=False),
    SInt32("unknown_2", VISIBLE=False),
    Array("unknown_array", SUB_STRUCT=SInt16("unknown"), SIZE=6, VISIBLE=False),
    BytesRaw("unknown_3", SIZE=4, VISIBLE=False),
    reflexive("functions", beam_beam_system_import_data_function),
    ENDIAN=">", SIZE=60
    )


beam_beam_system_shader_propertie_shader_map = Struct("shader_map", 
    dependency("bitmap"),
    SInt8("unknown_0", VISIBLE=False),
    SInt8("bitmap_index"),
    SInt8("unknown_1", VISIBLE=False),
    Bool8("bitmap_flags", *unknown_flags_8),
    SInt8("unknown_bitmap_index_enable"),
    SInt8("uv_argument_index"),
    SInt8("unknown_2", VISIBLE=False),
    SInt8("unknown_3", VISIBLE=False),
    ENDIAN=">", SIZE=24
    )


beam_beam_system_shader_propertie_argument = Struct("argument", 
    Array("arg_array", SUB_STRUCT=Float("arg"), SIZE=4),
    ENDIAN=">", SIZE=16
    )


beam_beam_system_shader_propertie_unknown_0 = Struct("unknown_0", 
    BytesRaw("unknown", SIZE=4, VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=4
    )


beam_beam_system_shader_propertie_unknown_2 = Struct("unknown_2", 
    SInt16("unknown", VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=2
    )


beam_beam_system_shader_propertie_unknown_3 = Struct("unknown_3", 
    BytesRaw("unknown_0", SIZE=4, VISIBLE=False),
    SInt8("unknown_1", VISIBLE=False),
    SInt8("unknown_2", VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=6
    )


beam_beam_system_shader_propertie_unknown_4 = Struct("unknown_4", 
    SInt16("unknown_0", VISIBLE=False),
    SInt16("unknown_1", VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=4
    )


beam_beam_system_shader_propertie_function = Struct("function", 
    SInt32("unknown_0", VISIBLE=False),
    string_id_meta("name"),
    BytesRaw("unknown_1", SIZE=8, VISIBLE=False),
    rawdata_ref("function"),
    ENDIAN=">", SIZE=36
    )


beam_beam_system_shader_propertie = Struct("shader_propertie", 
    dependency("template"),
    reflexive("shader_maps", beam_beam_system_shader_propertie_shader_map),
    reflexive("arguments", beam_beam_system_shader_propertie_argument),
    reflexive("unknown_0", beam_beam_system_shader_propertie_unknown_0),
    BytesRaw("unknown_1", SIZE=4, VISIBLE=False),
    reflexive("unknown_2", beam_beam_system_shader_propertie_unknown_2),
    reflexive("unknown_3", beam_beam_system_shader_propertie_unknown_3),
    reflexive("unknown_4", beam_beam_system_shader_propertie_unknown_4),
    reflexive("functions", beam_beam_system_shader_propertie_function),
    SInt32("unknown_5", VISIBLE=False),
    SInt32("unknown_6", VISIBLE=False),
    BytesRaw("unknown_7", SIZE=4, VISIBLE=False),
    Array("unknown_array", SUB_STRUCT=SInt16("unknown"), SIZE=8, VISIBLE=False),
    ENDIAN=">", SIZE=132
    )


beam_beam_system_unknown_26 = Struct("unknown_26", 
    BytesRaw("unknown", SIZE=16, VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=16
    )


beam_beam_system_compiled_function = Struct("compiled_function", 
    BytesRaw("unknown", SIZE=64, VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=64
    )


beam_beam_system_compiled_color_function = Struct("compiled_color_function", 
    color_rgb_float("color"),
    Float("magnitude"),
    ENDIAN=">", SIZE=16
    )


beam_beam_system = Struct("beam_system", 
    string_id_meta("name"),
    dependency("base_render_method"),
    reflexive("unknown_0", beam_beam_system_unknown_0),
    reflexive("import_data", beam_beam_system_import_data),
    reflexive("shader_properties", beam_beam_system_shader_propertie),
    Array("unknown_array", SUB_STRUCT=SInt8("unknown"), SIZE=4, VISIBLE=False),
    BytesRaw("unknown_1", SIZE=4, VISIBLE=False),
    SInt32("unknown_2", VISIBLE=False),
    BytesRaw("unknown_3", SIZE=36, VISIBLE=False),
    SInt8("input_0"),
    SInt8("input_range_0"),
    SEnum8("output_kind_0", *beam_beam_system_output_kind_0),
    SInt8("output_0"),
    rawdata_ref("unknown_4"),
    BytesRaw("unknown_5", SIZE=8, VISIBLE=False),
    SInt8("input_1"),
    SInt8("input_range_1"),
    SEnum8("output_kind_1", *beam_beam_system_output_kind_0),
    SInt8("output_1"),
    rawdata_ref("unknown_6"),
    BytesRaw("unknown_7", SIZE=8, VISIBLE=False),
    SInt8("input_2"),
    SInt8("input_range_2"),
    SEnum8("output_kind_2", *beam_beam_system_output_kind_0),
    SInt8("output_2"),
    rawdata_ref("unknown_8"),
    BytesRaw("unknown_9", SIZE=8, VISIBLE=False),
    SInt8("input_3"),
    SInt8("input_range_3"),
    SEnum8("output_kind_3", *beam_beam_system_output_kind_0),
    SInt8("output_3"),
    rawdata_ref("unknown_10"),
    BytesRaw("unknown_11", SIZE=24, VISIBLE=False),
    SInt8("input_4"),
    SInt8("input_range_4"),
    SEnum8("output_kind_4", *beam_beam_system_output_kind_0),
    SInt8("output_4"),
    rawdata_ref("unknown_12"),
    BytesRaw("unknown_13", SIZE=8, VISIBLE=False),
    SInt8("input_5"),
    SInt8("input_range_5"),
    SEnum8("output_kind_5", *beam_beam_system_output_kind_0),
    SInt8("output_5"),
    rawdata_ref("unknown_14"),
    BytesRaw("unknown_15", SIZE=8, VISIBLE=False),
    SInt8("input_6"),
    SInt8("input_range_6"),
    SEnum8("output_kind_6", *beam_beam_system_output_kind_0),
    SInt8("output_6"),
    rawdata_ref("unknown_16"),
    BytesRaw("unknown_17", SIZE=8, VISIBLE=False),
    SInt8("input_7"),
    SInt8("input_range_7"),
    SEnum8("output_kind_7", *beam_beam_system_output_kind_0),
    SInt8("output_7"),
    rawdata_ref("unknown_18"),
    BytesRaw("unknown_19", SIZE=8, VISIBLE=False),
    SInt8("input_8"),
    SInt8("input_range_8"),
    SEnum8("output_kind_8", *beam_beam_system_output_kind_0),
    SInt8("output_8"),
    rawdata_ref("unknown_20"),
    BytesRaw("unknown_21", SIZE=8, VISIBLE=False),
    SInt8("input_9"),
    SInt8("input_range_9"),
    SEnum8("output_kind_9", *beam_beam_system_output_kind_0),
    SInt8("output_9"),
    rawdata_ref("unknown_22"),
    BytesRaw("unknown_23", SIZE=8, VISIBLE=False),
    SInt8("input_10"),
    SInt8("input_range_10"),
    SEnum8("output_kind_10", *beam_beam_system_output_kind_0),
    SInt8("output_10"),
    rawdata_ref("unknown_24"),
    BytesRaw("unknown_25", SIZE=20, VISIBLE=False),
    reflexive("unknown_26", beam_beam_system_unknown_26),
    reflexive("compiled_functions", beam_beam_system_compiled_function),
    reflexive("compiled_color_functions", beam_beam_system_compiled_color_function),
    ENDIAN=">", SIZE=520
    )


beam_meta_def = BlockDef("beam", 
    reflexive("beam_system", beam_beam_system),
    TYPE=Struct, ENDIAN=">", SIZE=12
    )