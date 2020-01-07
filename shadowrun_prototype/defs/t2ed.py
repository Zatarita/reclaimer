#
# This file is part of Reclaimer.
#
# For authors and copyright check AUTHORS.TXT
#
# Reclaimer is free software under the GNU General Public License v3.0.
# See LICENSE for more information.
#

from ..common_descs import *
from supyr_struct.defs.tag_def import TagDef

def get():
    return t2ed_def

t2ed_def = TagDef("t2ed",
    blam_header('t2ed'),
    Struct('tagdata',
        ),

    ext=".tech_2_effect_data", endian=">"
    )
