from .mod2 import *

def get():
    return obje_def

attachment = Struct('attachment',
    dependency('type', valid_attachments),
    ascii_str32('marker'),
    BSEnum16('primary scale', *function_outputs),
    BSEnum16('secondary scale', *function_outputs),
    BSEnum16('change color', *function_names),

    SIZE=72
    )

widget = Struct('widget',
    dependency('reference', valid_widgets),
    SIZE=32
    )

function = Struct('function',
    BBool32('flags',
        'invert',
        'additive',
        'always active',
        ),
    BFloat('period'),
    BSEnum16('scale period by', *function_inputs_outputs),
    BSEnum16('function', *animation_functions),
    BSEnum16('scale function by', *function_inputs_outputs),
    BSEnum16('wobble function', *animation_functions),
    BFloat('wobble period'),  # seconds
    BFloat('wobble magnitude'),  # percent

    BFloat('square wave threshold'),
    BSInt16('step count'),
    BSEnum16('map to', *fade_functions),
    BSInt16('sawtooth count'),
    BSEnum16('add', *function_inputs_outputs),
    BSEnum16('scale result by', *function_inputs_outputs),
    BSEnum16('bounds mode',
        'clip',
        'clip and normalize',
        'scale to fit',
        ),
    QStruct('bounds', INCLUDE=from_to),

    Pad(6),
    BSInt16('turn off with',
        'A out',
        'B out',
        'C out',
        'D out',
        ('NONE', -1)
        ),
    BFloat('scale by'),

    Pad(268),
    ascii_str32('usage'),

    SIZE=360
    )

permutation = Struct('permutation',
    BFloat('weight'),
    QStruct('color lower bound', INCLUDE=rgb_float),
    QStruct('color upper bound', INCLUDE=rgb_float),

    SIZE=28
    )

change_color = Struct('change_color',
    BSEnum16('darken by', *function_inputs_outputs),
    BSEnum16('scale by', *function_inputs_outputs),
    BBool32('flags',
        'blend in hsv',
        'more colors',
        ),
    QStruct('color lower bound', INCLUDE=rgb_float),
    QStruct('color upper bound', INCLUDE=rgb_float),
    reflexive("permutations", permutation, 8),

    SIZE=44
    )

object_attrs = Struct('object attrs',
    FlSEnum16("object type",
        "bipd",
        "vehi",
        "weap",
        "eqip",
        "garb",
        "proj",
        "scen",
        "mach",
        "ctrl",
        "lifi",
        "plac",
        "ssce",
        ("obje", -1),
        EDITABLE=False,
        ),
    BBool16('flags',
        'does not cast shadow',
        'transparent self-occlusion',
        'brighter than it should be',
        'not a pathfinding obstacle',
        ('unknown0', 1<<8),
        ('unknown1', 1<<11),
        ),
    BFloat('bounding radius'),
    QStruct('bounding offset', INCLUDE=xyz_float),
    QStruct('origin offset', INCLUDE=xyz_float),
    BFloat('acceleration scale'),

    Pad(4),
    dependency('model', valid_models),
    dependency('animation graph', valid_model_animations),

    Pad(40),
    dependency('collision model', valid_model_collision_models),
    dependency('physics', valid_physics),
    dependency('modifier shader', valid_shaders),
    dependency('creation effect', valid_effects),
    Pad(84),
    BFloat('render bounding radius'),

    #Export to functions
    BSEnum16('A in', *object_export_to),
    BSEnum16('B in', *object_export_to),
    BSEnum16('C in', *object_export_to),
    BSEnum16('D in', *object_export_to),

    Pad(44),
    BSInt16('hud text message index'),
    BSInt16('forced shader permutation index'),
    reflexive("attachments", attachment, 8),
    reflexive("widgets", widget, 4),
    reflexive("functions", function, 4,
        'A out', 'B out', 'C out', 'D out'),
    reflexive("change colors", change_color, 4,
        'A', 'B', 'C', 'D'),
    reflexive("predicted resources", predicted_resource, 1024),

    SIZE=380
    )

obje_body = Struct('tagdata', object_attrs)

obje_def = TagDef("obje",
    blam_header('obje'),
    obje_body,

    ext=".object", endian=">"
    )