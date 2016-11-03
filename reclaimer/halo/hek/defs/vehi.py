from .obje import *
from .unit import *

vehicle_attrs = Struct("vehicle attrs",
    BBool32("flags",
        "speed wakes physics",
        "turn wakes physics",
        "driver power wakes physics",
        "gunner power wakes physics",
        "control opposite sets brake",
        "slide wakes physics",
        "kills riders at terminal velocity",
        "causes collision damage",
        "ai weapon cannot rotate",
        "ai does not require driver",
        "ai unused",
        "ai driver enable",
        "ai driver flying",
        "ai driver can sidestep",
        "ai driver hovering",
        ),
    BSEnum16('type', *vehicle_types),

    Pad(2),
    BFloat("maximum forward speed"),
    BFloat("maximum reverse speed"),
    BFloat("speed acceleration"),
    BFloat("speed deceleration"),
    BFloat("maximum left turn"),
    BFloat("maximum right turn"),  # this should be negative
    BFloat("wheel circumference"),  # world units
    BFloat("turn rate"),
    BFloat("blur speed"),
    BSEnum16('A in', *vehicle_inputs),
    BSEnum16('B in', *vehicle_inputs),
    BSEnum16('C in', *vehicle_inputs),
    BSEnum16('D in', *vehicle_inputs),

    Pad(12),
    BFloat("maximum left slide"),
    BFloat("maximum right slide"),
    BFloat("slide acceleration"),
    BFloat("slide deceleration"),
    BFloat("minimum flipping angular velocity"),
    BFloat("maximum flipping angular velocity"),

    Pad(24),
    BFloat("fixed gun yaw"),  # degrees
    BFloat("fixed gun pitch"),  # degrees

    Pad(24),
    Struct("ai",
        BFloat("sidestep distance"),
        BFloat("destination radius"),
        BFloat("avoidance distance"),
        BFloat("pathfinding radius"),
        BFloat("charge repeat timeout"),
        BFloat("strafing abort range"),
        QStruct("oversteering bounds", INCLUDE=from_to),  # radians
        BFloat("steering maximum"),  # radians
        BFloat("throttle maximum"),
        BFloat("move-position time"),
        ),

    Pad(4),
    dependency('suspension sound', valid_sounds),
    dependency('crash sound', valid_sounds),
    dependency('material effect', valid_material_effects),
    dependency('effect', valid_effects),
    
    SIZE=256
    )

vehi_body = Struct("tagdata",
    object_attrs,
    unit_attrs,
    vehicle_attrs,
    SIZE=1008,
    )


def get():
    return vehi_def

vehi_def = TagDef("vehi",
    blam_header('vehi'),
    vehi_body,

    ext=".vehicle", endian=">"
    )