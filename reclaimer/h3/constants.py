from ..constants import *


# maps tag class four character codes(fccs) in
# their string encoding to their int encoding.
h3_tag_class_fcc_to_be_int = {}
h3_tag_class_fcc_to_le_int = {}
# maps tag class four character codes(fccs) in
# their int encoding to their string encoding.
h3_tag_class_be_int_to_fcc = {}
h3_tag_class_le_int_to_fcc = {}

# maps tag class four character codes to the tags file extension
# 177 tag classes
h3_tag_class_fcc_to_ext = {
    "$#!+": "cache_file_sound",
    "*cen": "scenario_scenery_resource",
    "*eap": "scenario_weapons_resource",
    "*ehi": "scenario_vehicles_resource",
    "*fsc": "UNKNOWN0",
    "*igh": "scenario_lights_resource",
    "*ipd": "scenario_bipeds_resource",
    "*qip": "scenario_equipment_resource",
    "*rea": "scenario_creature_resource",
    "*sce": "scenario_sound_scenery_resource",
    "/**/": "scenario_comments_resource",
    "<fx>": "sound_effect_template",
    "BooM": "stereo_system",
    "adlg": "ai_dialogue_globals",
    "ai**": "scenario_ai_resource",
    "ant!": "antenna",
    "beam": "UNKNOWN1",
    "bink": "UNKNOWN2",
    "bipd": "biped",
    "bitm": "bitmap",
    "bkey": "UNKNOWN3",
    "bloc": "crate",
    "bmp3": "UNKNOWN4",
    "bsdt": "breakable_surface",
    "cddf": "UNKNOWN5",
    "cfxs": "UNKNOWN6",
    "chad": "UNKNOWN7",
    "char": "character",
    "chdt": "UNKNOWN8",
    "chgd": "UNKNOWN9",
    "chmt": "UNKNOWN10",
    "cin*": "scenario_cinematics_resource",
    "cine": "UNKNOWN11",
    "cisc": "UNKNOWN12",
    "clu*": "scenario_cluster_data_resource",
    "clwd": "cloth",
    "cntl": "UNKNOWN13",
    "coll": "collision_model",
    "colo": "color_table",
    "crea": "creature",
    "crte": "UNKNOWN14",
    "ctrl": "device_control",
    "cub*": "UNKNOWN15",
    "dc*s": "scenario_decorators_resource",
    "dctr": "UNKNOWN16",
    "dec*": "scenario_decals_resource",
    "decs": "UNKNOWN17",
    "devi": "device",
    "devo": "cellular_automata",
    "dgr*": "scenario_devices_resource",
    "dobc": "detail_object_collection",
    "draw": "UNKNOWN18",
    "drdf": "UNKNOWN19",
    "dsrc": "UNKNOWN20",
    "effe": "effect",
    "effg": "UNKNOWN21",
    "efsc": "UNKNOWN22",
    "egor": "screen_effect",
    "eqip": "equipment",
    "flck": "UNKNOWN23",
    "fldy": "UNKNOWN24",
    "fog ": "planar_fog",
    "foot": "material_effects",
    "fpch": "patchy_fog",
    "frag": "UNKNOWN25",
    "gint": "UNKNOWN26",
    "glps": "UNKNOWN27",
    "glvs": "UNKNOWN28",
    "goof": "multiplayer_variant_settings_interface_definition",
    "grup": "UNKNOWN29",
    "hlmt": "model",
    "hlsl": "UNKNOWN30",
    "hsc*": "scenario_hs_source_file",
    "item": "item",
    "itmc": "item_collection",
    "jmad": "model_animation_graph",
    "jmrq": "UNKNOWN31",
    "jpt!": "damage_effect",
    "lens": "lens_flare",
    "ligh": "light",
    "lsnd": "sound_looping",
    "lst3": "UNKNOWN32",
    "lswd": "UNKNOWN33",
    "ltvl": "UNKNOWN34",
    "mach": "device_machine",
    "matg": "globals",
    "mdl3": "UNKNOWN35",
    "mdlg": "ai_mission_dialogue",
    "metr": "meter",
    "mffn": "UNKNOWN36",
    "mode": "render_model",
    "mply": "multiplayer_scenario_description",
    "mulg": "multiplayer_globals",
    "nclt": "UNKNOWN37",
    "obje": "object",
    "perf": "UNKNOWN38",
    "phmo": "physics_model",
    "pixl": "pixel_shader",
    "play": "UNKNOWN39",
    "pmdf": "UNKNOWN40",
    "pmov": "particle_physics",
    "pphy": "point_physics",
    "proj": "projectile",
    "prt3": "particle",
    "rasg": "UNKNOWN41",
    "rm  ": "UNKNOWN42",
    "rmb ": "UNKNOWN43",
    "rmcs": "UNKNOWN44",
    "rmct": "UNKNOWN45",
    "rmd ": "UNKNOWN46",
    "rmdf": "UNKNOWN47",
    "rmfl": "UNKNOWN48",
    "rmhg": "UNKNOWN49",
    "rmlv": "UNKNOWN50",
    "rmop": "UNKNOWN51",
    "rmsh": "UNKNOWN52",
    "rmsk": "UNKNOWN53",
    "rmt2": "UNKNOWN54",
    "rmtr": "UNKNOWN55",
    "rmw ": "UNKNOWN56",
    "rwrd": "UNKNOWN57",
    "sFdT": "UNKNOWN58",
    "sLdT": "UNKNOWN59",
    "sbsp": "scenario_structure_bsp",
    "scen": "scenery",
    "scn3": "UNKNOWN60",
    "scnr": "scenario",
    "sddt": "UNKNOWN61",
    "sefc": "UNKNOWN62",
    "sfx+": "sound_effect_collection",
    "sgp!": "UNKNOWN63",
    "shit": "UNKNOWN64",
    "sily": "text_value_pair_definition",
    "skn3": "UNKNOWN65",
    "sky*": "UNKNOWN66",
    "skya": "UNKNOWN67",
    "smap": "UNKNOWN68",
    "sncl": "sound_classes",
    "snd!": "sound",
    "snde": "sound_environment",
    "snmx": "sound_mix",
    "spk!": "sound_dialogue_constants",
    "ssce": "sound_scenery",
    "sslt": "scenario_structure_lighting_resource",
    "stli": "UNKNOWN69",
    "stse": "UNKNOWN70",
    "styl": "style",
    "term": "UNKNOWN71",
    "trak": "camera_track",
    "trg*": "scenario_trigger_volumes_resource",
    "txt3": "UNKNOWN72",
    "udlg": "dialogue",
    "ugh!": "sound_cache_file_gestalt",
    "uise": "UNKNOWN73",
    "unic": "multilingual_unicode_string_list",
    "unit": "unit",
    "vehc": "vehicle_collection",
    "vehi": "vehicle",
    "vtsh": "UNKNOWN74",
    "wacd": "UNKNOWN75",
    "wclr": "UNKNOWN76",
    "weap": "weapon",
    "wezr": "UNKNOWN77",
    "wfon": "UNKNOWN78",
    "wgan": "UNKNOWN79",
    "wgtz": "user_interface_globals_definition",
    "whip": "cellular_automata2d",
    "wigl": "user_interface_shared_globals_definition",
    "wind": "wind",
    "wpos": "UNKNOWN80",
    "wrot": "UNKNOWN81",
    "wscl": "UNKNOWN82",
    "wspr": "UNKNOWN83",
    "wtuv": "UNKNOWN84",
    "zone": "UNKNOWN85",
    b"\x00rmc".decode(encoding="latin-1"): "UNKNOWN86",
    b"\x00rmp".decode(encoding="latin-1"): "UNKNOWN87"
    }

for tag_cls in h3_tag_class_fcc_to_ext:
    h3_tag_class_fcc_to_be_int[tag_cls] = fcc(tag_cls)
    h3_tag_class_be_int_to_fcc[fcc(tag_cls)] = tag_cls
    h3_tag_class_fcc_to_le_int[tag_cls] = fcc(tag_cls)
    h3_tag_class_le_int_to_fcc[fcc(tag_cls)] = tag_cls
