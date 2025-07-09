import MASH.api as mapi
import maya.cmds as cmds
import mash_repro_utils as repro
import mash_repro_aetemplate as AErepro
import random

def random_repro_reorder(repro):
    """
    Choose a random object to be the 0 index in repro

    :param mash_repro_node: MASH Repro node
    :return: None
    """
new_order = maya.cmds.getAttr("%s.instancedGroup" % repro, mi=True) or []
items_count = len(new_order)
ranItem = random.randint(0,items_count)

new_order.pop(0)
new_order.insert(ranItem, 0)
repro.reorder_mesh_group_node(repro, new_order)
# print(new_order)

# ===========================================================================
# Copyright 2021 GlenJohnsonArt, Inc. All rights reserved.
# ===========================================================================
"""

import mash_repro_utils as repro
import mash_repro_aetemplate as AErepro
import random

new_order = maya.cmds.getAttr("%s.instancedGroup" % 'MASH2_Repro', mi=True) or []
items_count = len(new_order)
ranItem = random.randint(0,items_count)

new_order.pop(0)
new_order.insert(ranItem, 0)
repro.reorder_mesh_group_node('MASH2_Repro', new_order)

"""


