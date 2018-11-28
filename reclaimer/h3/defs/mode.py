############# Credits and version info #############
# Definition autogenerated from Assembly XML tag def
#
# revision: 1		author: Assembly
# 	Generated plugin from scratch.
# revision: 2		author: bfixer117
# 	Named some more nodes.
# revision: 3		author: Lord Zedd
# 	Standardized model data and updated
# revision: 4		author: Moses_of_Egypt
# 	Cleaned up and converted to SuPyr definition
#
####################################################
from reclaimer.common_descs import *
from supyr_struct.defs.tag_def import TagDef

mode_meshe_index_buffer_type = (
    "point_list",
    "line_list",
    "line_strip",
    "triange_list",
    "triange_fan",
    "triange_strip",
    )

mode_meshe_prt_type = (
    "none",
    "ambient",
    "linear",
    "quadratic",
    )

mode_meshe_vertex_type = (
    "world",
    "rigid",
    "skinned",
    "particle_model",
    "flat_world",
    "flat_rigid",
    "flat_skinned",
    "screen",
    "debug",
    "transparent",
    "particle",
    "contrail",
    "light_volume",
    "chud_simple",
    "chud_fancy",
    "decorator",
    "tiny_position",
    "patchy_fog",
    "water",
    "ripple",
    "implicit",
    "beam",
    )


mode_region_permutation = Struct("permutation", 
    string_id_meta("name"),
    SInt16("mesh_index"),
    SInt16("mesh_count"),
    SInt32("unknown_0", VISIBLE=False),
    SInt32("unknown_1", VISIBLE=False),
    ENDIAN=">", SIZE=16
    )


mode_region = Struct("region", 
    string_id_meta("name"),
    reflexive("permutations", mode_region_permutation),
    ENDIAN=">", SIZE=16
    )


mode_instance = Struct("instance", 
    string_id_meta("name"),
    SInt32("node_index"),
    Float("default_scale"),
    QStruct("inverse_forward", INCLUDE=ijk_float),
    QStruct("inverse_left", INCLUDE=ijk_float),
    QStruct("inverse_up", INCLUDE=ijk_float),
    QStruct("inverse_position", INCLUDE=xyz_float),
    ENDIAN=">", SIZE=60
    )


mode_node = Struct("node", 
    string_id_meta("name"),
    SInt16("parent_node"),
    SInt16("first_child_node"),
    SInt16("next_sibling_node"),
    SInt16("import_node_index", VISIBLE=False),
    QStruct("default_translation", INCLUDE=xyz_float),
    QStruct("default_rotation", INCLUDE=ijkw_float),
    Float("default_scale"),
    QStruct("inverse_forward", INCLUDE=ijk_float),
    QStruct("inverse_left", INCLUDE=ijk_float),
    QStruct("inverse_up", INCLUDE=ijk_float),
    QStruct("inverse_position", INCLUDE=xyz_float),
    Float("distance_from_parent"),
    ENDIAN=">", SIZE=96
    )


mode_marker_group_marker = Struct("marker", 
    SInt8("region_index"),
    SInt8("permutation_index"),
    SInt8("node_index"),
    SInt8("unknown", VISIBLE=False),
    QStruct("translation", INCLUDE=xyz_float),
    QStruct("rotation", INCLUDE=ijkw_float),
    Float("scale"),
    ENDIAN=">", SIZE=36
    )


mode_marker_group = Struct("marker_group", 
    string_id_meta("name"),
    reflexive("markers", mode_marker_group_marker),
    ENDIAN=">", SIZE=16
    )


mode_material_propertie = Struct("propertie", 
    SInt16("type"),
    SInt16("int_value"),
    Array("unknown_array", SUB_STRUCT=SInt8("unknown"), SIZE=4, VISIBLE=False),
    Float("real_value"),
    ENDIAN=">", SIZE=12
    )


mode_material = Struct("material", 
    dependency("shader"),
    reflexive("properties", mode_material_propertie),
    SInt32("unknown_0", VISIBLE=False),
    SInt8("breakable_surface_index"),
    SInt8("unknown_1", VISIBLE=False),
    SInt8("unknown_2", VISIBLE=False),
    SInt8("unknown_3", VISIBLE=False),
    ENDIAN=">", SIZE=36
    )


mode_meshe_part = Struct("part", 
    SInt16("material_index"),
    SInt16("unknown_nodey_index", VISIBLE=False),
    SInt16("index_buffer_start"),
    SInt16("index_buffer_count"),
    SInt16("subpart_index"),
    SInt16("subpart_count"),
    SInt8("unknown_enum", VISIBLE=False),
    Bool8("flags", 
        ("water", 1 << 3),
        ),
    SInt16("vertex_count"),
    ENDIAN=">", SIZE=16
    )


mode_meshe_subpart = Struct("subpart", 
    SInt16("index_buffer_start"),
    SInt16("index_buffer_count"),
    SInt16("part_index"),
    SInt16("vertex_count"),
    ENDIAN=">", SIZE=8
    )


mode_meshe_instanced_geometry_indice_instanced_geometry_mesh_content = Struct("instanced_geometry_mesh_content", 
    SInt16("instanced_geometry_index"),
    ENDIAN=">", SIZE=2
    )


mode_meshe_instanced_geometry_indice = Struct("instanced_geometry_indice", 
    SInt16("instanced_geometry_mesh_index_1"),
    SInt16("instanced_geometry_mesh_index_2"),
    reflexive("instanced_geometry_mesh_contents", mode_meshe_instanced_geometry_indice_instanced_geometry_mesh_content),
    ENDIAN=">", SIZE=16
    )


mode_meshe_unknown_water = Struct("unknown_water", 
    SInt16("unknown"),
    VISIBLE=False,
    ENDIAN=">", SIZE=2
    )


mode_meshe = Struct("meshe", 
    reflexive("parts", mode_meshe_part),
    reflexive("subparts", mode_meshe_subpart),
    Array("vertex_buffer_index_array", SUB_STRUCT=SInt16("vertex_buffer_index"), SIZE=8),
    SInt16("index_buffer_index_1"),
    SInt16("index_buffer_index_2"),
    Bool8("flags", 
        "has_vertex_colors",
        ),
    SInt8("rigid_node"),
    SEnum8("vertex_type", *mode_meshe_vertex_type),
    SEnum8("prt_type", *mode_meshe_prt_type),
    SEnum8("index_buffer_type", *mode_meshe_index_buffer_type),
    SInt8("unknown_0", VISIBLE=False),
    SInt8("unknown_1", VISIBLE=False),
    SInt8("unknown_2", VISIBLE=False),
    reflexive("instanced_geometry_indices", mode_meshe_instanced_geometry_indice),
    reflexive("unknown_water", mode_meshe_unknown_water),
    ENDIAN=">", SIZE=76
    )


mode_compression_info = Struct("compression_info", 
    SInt16("unknown_0", VISIBLE=False),
    SInt16("unknown_1", VISIBLE=False),
    QStruct("position_bounds_x", INCLUDE=from_to),
    QStruct("position_bounds_y", INCLUDE=from_to),
    QStruct("position_bounds_z", INCLUDE=from_to),
    QStruct("texcoord_bounds_x", INCLUDE=from_to),
    QStruct("texcoord_bounds_y", INCLUDE=from_to),
    ENDIAN=">", SIZE=44
    )


mode_unknown_nodey = Struct("unknown_nodey", 
    Array("unknown_array", SUB_STRUCT=Float("unknown"), SIZE=8, VISIBLE=False),
    Array("node_index_array", SUB_STRUCT=SInt8("node_index"), SIZE=4, VISIBLE=False),
    Float("unknown_0", VISIBLE=False),
    Float("unknown_1", VISIBLE=False),
    Float("unknown_2", VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=48
    )


mode_unknown_5 = Struct("unknown_5", 
    SInt16("unknown_0", VISIBLE=False),
    SInt16("unknown_1", VISIBLE=False),
    rawdata_ref("unknown_2", VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=24
    )


mode_unknown_meshe_unknown_1 = Struct("unknown_1", 
    SInt16("unknown", VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=2
    )


mode_unknown_meshe = Struct("unknown_meshe", 
    rawdata_ref("unknown_0", VISIBLE=False),
    reflexive("unknown_1", mode_unknown_meshe_unknown_1),
    VISIBLE=False,
    ENDIAN=">", SIZE=32
    )


mode_node_map_unknown = Struct("unknown", 
    UInt8("node_index"),
    ENDIAN=">", SIZE=1
    )


mode_node_map = Struct("node_map", 
    reflexive("unknown", mode_node_map_unknown),
    ENDIAN=">", SIZE=12
    )


mode_unknown_7_unknown = Struct("unknown", 
    BytesRaw("unknown", SIZE=48, VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=48
    )


mode_unknown_7 = Struct("unknown_7", 
    reflexive("unknown", mode_unknown_7_unknown),
    VISIBLE=False,
    ENDIAN=">", SIZE=12
    )


mode_unknown_yo = Struct("unknown_yo", 
    BytesRaw("unknown_0", SIZE=12, VISIBLE=False),
    SInt16("unknown_index"),
    SInt16("unknown_1", VISIBLE=False),
    ENDIAN=">", SIZE=16
    )


mode_unknown_9 = Struct("unknown_9", 
    Array("unknown_array", SUB_STRUCT=Float("unknown"), SIZE=7, VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=28
    )


mode_unknown_10 = Struct("unknown_10", 
    BytesRaw("unknown", SIZE=336, VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=336
    )


mode_runtime_node = Struct("runtime_node", 
    QStruct("default_rotation", INCLUDE=ijkw_float),
    QStruct("default_translation", INCLUDE=xyz_float),
    Float("default_scale"),
    ENDIAN=">", SIZE=32
    )


mode_meta_def = BlockDef("mode", 
    string_id_meta("name"),
    Bool16("flags", 
        ("force_node_maps", 1 << 2),
        ),
    SInt16("unknown_0", VISIBLE=False),
    SInt32("model_checksum"),
    reflexive("regions", mode_region),
    BytesRaw("unknown_1", SIZE=4, VISIBLE=False),
    SInt32("instance_starting_mesh_index"),
    reflexive("instances", mode_instance),
    BytesRaw("unknown_2", SIZE=4, VISIBLE=False),
    reflexive("nodes", mode_node),
    reflexive("marker_groups", mode_marker_group),
    reflexive("materials", mode_material),
    BytesRaw("unknown_3", SIZE=16, VISIBLE=False),
    SInt32("unknown_4", VISIBLE=False),
    reflexive("meshes", mode_meshe),
    reflexive("compression_info", mode_compression_info),
    reflexive("unknown_nodey", mode_unknown_nodey),
    reflexive("unknown_5", mode_unknown_5),
    BytesRaw("unknown_6", SIZE=12, VISIBLE=False),
    reflexive("unknown_meshes", mode_unknown_meshe),
    reflexive("node_maps", mode_node_map),
    reflexive("unknown_7", mode_unknown_7),
    BytesRaw("unknown_8", SIZE=12, VISIBLE=False),
    reflexive("unknown_yo", mode_unknown_yo),
    UInt16("zone_asset_salt"),
    UInt16("zone_asset_index"),
    SInt32("useless_padding", VISIBLE=False),
    reflexive("unknown_9", mode_unknown_9),
    BytesRaw("unknown_a", SIZE=192, VISIBLE=False),
    reflexive("unknown_10", mode_unknown_10),
    reflexive("runtime_nodes", mode_runtime_node),
    TYPE=Struct, ENDIAN=">", SIZE=460
    )