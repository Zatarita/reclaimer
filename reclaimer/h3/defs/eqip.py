############# Credits and version info #############
# Definition autogenerated from Assembly XML tag def
#
# revision: 1		author: Assembly
# 	Generated plugin from scratch.
# revision: 2		author: DarkShallFall
# 	Values, Attachments. Effects, Projectile, jpt!, Impact sound, Pickup Sound, Activation Sound, HUD, and other small things
# revision: 3		author: DeadCanadian
# 	fixed the death properties
# revision: 4		author: Lord Zedd
# 	Portin'
# revision: 5		author: Moses_of_Egypt
# 	Cleaned up and converted to SuPyr definition
#
####################################################
from reclaimer.common_descs import *
from supyr_struct.defs.tag_def import TagDef

eqip_ai_propertie_leap_jump_speed = (
    "none",
    "down",
    "step",
    "crouch",
    "stand",
    "storey",
    "tower",
    "infinite",
    )

eqip_ai_propertie_size = (
    "default",
    "tiny",
    "small",
    "medium",
    "large",
    "huge",
    "immobile",
    )

eqip_attachment_change_color = (
    "none",
    "primary",
    "secondary",
    "tertiary",
    "quaternary",
    )

eqip_lightmap_shadow_mode_size = (
    "default",
    "never",
    "always",
    "unknown",
    )

eqip_multiplayer_object_propertie_object_type = (
    "ordinary",
    "weapon",
    "grenade",
    "projectile",
    "powerup",
    "equipment",
    "light_land_vehicle",
    "heavy_land_vehicle",
    "flying_vehicle",
    "teleporter_2way",
    "teleporter_sender",
    "teleporter_receiver",
    "player_spawn_location",
    "player_respawn_zone",
    "hold_spawn_objective",
    "capture_spawn_objective",
    "hold_destination_objective",
    "capture_destination_objective",
    "hill_objective",
    "infection_haven_objective",
    "territory_objective",
    "vip_boundary_objective",
    "vip_destination_objective",
    "juggernaut_destination_objective",
    )

eqip_multiplayer_object_propertie_shape = (
    "none",
    "sphere",
    "cylinder",
    "box",
    )

eqip_multiplayer_object_propertie_spawn_timer_mode = (
    "on_death",
    "on_disturbance",
    )

eqip_object_type = (
    "biped",
    "vehicle",
    "weapon",
    "equipment",
    "terminal",
    "projectile",
    "scenery",
    "machine",
    "control",
    "sound_scenery",
    "crate",
    "creature",
    "giant",
    "effect_scenery",
    )

eqip_powerup_powerup_trait_set = (
    "red",
    "blue",
    "yellow",
    )

eqip_sweetener_size = (
    "small",
    "medium",
    "large",
    )

eqip_water_density = (
    "default",
    "least",
    "some",
    "equal",
    "more",
    "more_still",
    "lots_more",
    )

unknown_flags_16 = tuple("bit_%s" % i for i in range(16))


eqip_early_mover_propertie = Struct("early_mover_propertie", 
    string_id_meta("name"),
    Pad(36),
    ENDIAN=">", SIZE=40
    )


eqip_ai_propertie = Struct("ai_propertie", 
    Bool32("flags", 
        "destroyable_cover",
        "pathfinding_ignore_when_dead",
        "dynamic_cover",
        ),
    string_id_meta("ai_type_name"),
    BytesRaw("unknown", SIZE=4, VISIBLE=False),
    SEnum16("size", *eqip_ai_propertie_size),
    SEnum16("leap_jump_speed", *eqip_ai_propertie_leap_jump_speed),
    ENDIAN=">", SIZE=16
    )


eqip_function = Struct("function", 
    Bool32("flags", 
        "invert",
        "mapping_does_not_controls_active",
        "always_active",
        "random_time_offset",
        ),
    string_id_meta("import_name"),
    string_id_meta("export_name"),
    string_id_meta("turn_off_with"),
    Float("minimum_value"),
    rawdata_ref("default_function"),
    string_id_meta("scale_by"),
    ENDIAN=">", SIZE=44
    )


eqip_attachment = Struct("attachment", 
    dependency("attachment"),
    string_id_meta("marker"),
    SEnum16("change_color", *eqip_attachment_change_color),
    SInt16("unknown", VISIBLE=False),
    string_id_meta("primary_scale"),
    string_id_meta("secondary_scale"),
    ENDIAN=">", SIZE=32
    )


eqip_widget = Struct("widget", 
    dependency("type"),
    ENDIAN=">", SIZE=16
    )


eqip_change_color_initial_permutation = Struct("initial_permutation", 
    Pad(4),
    color_rgb_float("color_lower_bound"),
    color_rgb_float("color_upper_bound"),
    string_id_meta("variant_name"),
    ENDIAN=">", SIZE=32
    )


eqip_change_color_function = Struct("function", 
    Bool32("scale_flags", 
        "blend_in_hsv",
        "more_colors",
        ),
    color_rgb_float("color_lower_bound"),
    color_rgb_float("color_upper_bound"),
    string_id_meta("darken_by"),
    string_id_meta("scale_by"),
    ENDIAN=">", SIZE=32
    )


eqip_change_color = Struct("change_color", 
    reflexive("initial_permutations", eqip_change_color_initial_permutation),
    reflexive("functions", eqip_change_color_function),
    ENDIAN=">", SIZE=24
    )


eqip_predicted_resource = Struct("predicted_resource", 
    SInt16("type"),
    SInt16("resource_index"),
    UInt32("tag_index"),
    VISIBLE=False,
    ENDIAN=">", SIZE=8
    )


eqip_multiplayer_object_propertie = Struct("multiplayer_object_propertie", 
    Bool16("engine_flags", 
        "capture_the_flag",
        "slayer",
        "oddball",
        "king_of_the_hill",
        "juggernaut",
        "territories",
        "assault",
        "vip",
        "infection",
        ),
    SEnum8("object_type", *eqip_multiplayer_object_propertie_object_type),
    Bool8("teleporter_flags", 
        "disallows_players",
        "allows_land_vehicles",
        "allows_heavy_vehicles",
        "allows_flying_vehicles",
        "allows_projectiles",
        ),
    Bool16("flags", 
        "editor_only",
        ),
    SEnum8("shape", *eqip_multiplayer_object_propertie_shape),
    SEnum8("spawn_timer_mode", *eqip_multiplayer_object_propertie_spawn_timer_mode),
    SInt16("spawn_time"),
    SInt16("abandon_time"),
    Float("radius_width"),
    Float("length"),
    Float("top"),
    Float("bottom"),
    Float("unknown_0", VISIBLE=False),
    Float("unknown_1", VISIBLE=False),
    Float("unknown_2", VISIBLE=False),
    SInt32("unknown_3", VISIBLE=False),
    SInt32("unknown_4", VISIBLE=False),
    dependency("child_object"),
    SInt32("unknown_5"),
    dependency("shape_shader"),
    dependency("unknown_shader"),
    dependency("unknown_6"),
    dependency("unknown_7"),
    dependency("unknown_8"),
    dependency("unknown_9"),
    dependency("unknown_10"),
    dependency("unknown_11"),
    ENDIAN=">", SIZE=196
    )


eqip_predicted_bitmap = Struct("predicted_bitmap", 
    dependency("bitmap", VISIBLE=False),
    VISIBLE=False,
    ENDIAN=">", SIZE=16
    )


eqip_health_pack = Struct("health_pack", 
    Float("unknown_0", VISIBLE=False),
    Float("unknown_1", VISIBLE=False),
    Float("shields_given"),
    dependency("unknown_2"),
    dependency("unknown_3"),
    dependency("unknown_4"),
    ENDIAN=">", SIZE=60
    )


eqip_powerup = Struct("powerup", 
    SEnum32("powerup_trait_set", *eqip_powerup_powerup_trait_set),
    ENDIAN=">", SIZE=4
    )


eqip_object_creation = Struct("object_creation", 
    dependency("object"),
    dependency("unknown_0"),
    Float("unknown_1", VISIBLE=False),
    Float("unknown_2", VISIBLE=False),
    Float("unknown_3", VISIBLE=False),
    Float("object_force"),
    Float("unknown_4", VISIBLE=False),
    ENDIAN=">", SIZE=52
    )


eqip_destruction = Struct("destruction", 
    dependency("destroy_effect"),
    dependency("destroy_damage_effect"),
    Float("unknown_0", VISIBLE=False),
    Float("self_destruction_time"),
    Float("unknown_1", VISIBLE=False),
    Float("unknown_2", VISIBLE=False),
    ENDIAN=">", SIZE=48
    )


eqip_radar_manipulation = Struct("radar_manipulation", 
    Float("unknown_0", VISIBLE=False),
    Float("fake_blip_radius"),
    SInt32("fake_blip_count"),
    Float("unknown_1", VISIBLE=False),
    ENDIAN=">", SIZE=16
    )


eqip_invisibility = Struct("invisibility", 
    Float("unknown_0"),
    Float("unknown_1"),
    ENDIAN=">", SIZE=8
    )


eqip_invincibility = Struct("invincibility", 
    string_id_meta("material_name"),
    SInt16("global_material_index"),
    SInt16("unknown_0", VISIBLE=False),
    BytesRaw("unknown_1", SIZE=4, VISIBLE=False),
    dependency("activation_effect"),
    dependency("active_effect"),
    dependency("deactivation_effect"),
    ENDIAN=">", SIZE=60
    )


eqip_regenerator = Struct("regenerator", 
    Float("unknown"),
    ENDIAN=">", SIZE=4
    )


eqip_meta_def = BlockDef("eqip", 
    SEnum16("object_type", *eqip_object_type),
    Bool16("flags_0", 
        "does_not_cast_shadow",
        "search_cardinal_direction_lightmaps",
        ("not_a_pathfinding_obstacle", 1 << 3),
        "extension_of_parent",
        "does_not_cause_collision_damage",
        "early_mover",
        "early_mover_localized_physics",
        "use_static_massive_lightmap_sample",
        "object_scales_attachments",
        "inherits_player_s_appearance",
        "dead_bipeds_can_t_localize",
        "attach_to_clusters_by_dynamic_sphere",
        "effects_created_by_this_object_do_not_spawn_objects_in_multiplayer",
        ),
    Float("bounding_radius"),
    QStruct("bounding_offset", INCLUDE=xyz_float),
    Float("acceleration_scale"),
    SEnum16("lightmap_shadow_mode_size", *eqip_lightmap_shadow_mode_size),
    SEnum8("sweetener_size", *eqip_sweetener_size),
    SEnum8("water_density", *eqip_water_density),
    SInt32("unknown_0", VISIBLE=False),
    Float("dynamic_light_sphere_radius"),
    QStruct("dynamic_light_sphere_offset", INCLUDE=xyz_float),
    string_id_meta("default_model_variant"),
    dependency("model"),
    dependency("crate_object"),
    dependency("collision_damage"),
    reflexive("early_mover_properties", eqip_early_mover_propertie),
    dependency("creation_effect"),
    dependency("material_effects"),
    dependency("melee_impact"),
    reflexive("ai_properties", eqip_ai_propertie),
    reflexive("functions", eqip_function),
    SInt16("hud_text_message_index"),
    SInt16("unknown_1", VISIBLE=False),
    reflexive("attachments", eqip_attachment),
    reflexive("widgets", eqip_widget),
    reflexive("change_colors", eqip_change_color),
    reflexive("predicted_resources", eqip_predicted_resource),
    reflexive("multiplayer_object_properties", eqip_multiplayer_object_propertie),
    Bool32("flags_1", 
        "always_maintains_z_up",
        "destroyed_by_explosions",
        "unaffected_by_gravity",
        ),
    SInt16("old_message_index"),
    SInt16("sort_order"),
    Float("old_multiplayer_on_ground_scale"),
    Float("old_campaign_on_ground_scale"),
    string_id_meta("pickup_message"),
    string_id_meta("swap_message"),
    string_id_meta("pickup_or_dual_wield_message"),
    string_id_meta("swap_or_dual_wield_message"),
    string_id_meta("picked_up_message"),
    string_id_meta("switch_to_message"),
    string_id_meta("switch_to_from_ai_message"),
    string_id_meta("all_weapons_empty_message"),
    dependency("collision_sound"),
    reflexive("predicted_bitmaps", eqip_predicted_bitmap),
    dependency("detonation_damage_effect"),
    QStruct("detonation_delay", INCLUDE=from_to),
    dependency("detonating_effect"),
    dependency("detonation_effect"),
    Float("campaign_ground_scale"),
    Float("multiplayer_ground_scale"),
    Float("small_hold_scale"),
    Float("small_holster_scale"),
    Float("medium_hold_scale"),
    Float("medium_holster_scale"),
    Float("large_hold_scale"),
    Float("large_holster_scale"),
    Float("huge_hold_scale"),
    Float("huge_holster_scale"),
    Float("grounded_friction_length"),
    Float("grounded_friction_unknown"),
    Float("use_duration"),
    Float("unknown_2", VISIBLE=False),
    SInt16("number_of_uses"),
    Bool16("flags_2", *unknown_flags_16),
    Float("unknown_3", VISIBLE=False),
    Float("unknown_4", VISIBLE=False),
    Float("unknown_5", VISIBLE=False),
    reflexive("health_pack", eqip_health_pack),
    reflexive("powerup", eqip_powerup),
    reflexive("object_creation", eqip_object_creation),
    reflexive("destruction", eqip_destruction),
    reflexive("radar_manipulation", eqip_radar_manipulation),
    BytesRaw("null", SIZE=12, VISIBLE=False),
    reflexive("invisibility", eqip_invisibility),
    reflexive("invincibility", eqip_invincibility),
    reflexive("regenerator", eqip_regenerator),
    dependency("hud_interface"),
    dependency("pickup_sound"),
    dependency("activation_effect"),
    dependency("active_effect"),
    dependency("deactivation_effect"),
    TYPE=Struct, ENDIAN=">", SIZE=640
    )