"""
Loads all the fx !
Usage:
import __moviepy.video.fx.all as vfx
clip = vfx.resize(some_clip, width=400)
clip = vfx.mirror_x(some_clip)
"""

import pkgutil
import __moviepy.video.fx as fx

__all__ = [name for _, name, _ in pkgutil.iter_modules(
    fx.__path__) if name != "all"]

#for name in __all__:
   #exec("from ..%s import %s" % (name, name))

from __moviepy.video.fx.accel_decel import accel_decel
from __moviepy.video.fx.blackwhite import blackwhite
from __moviepy.video.fx.blink import blink
from __moviepy.video.fx.colorx import colorx
from __moviepy.video.fx.crop import crop
from __moviepy.video.fx.even_size import even_size
from __moviepy.video.fx.fadein import fadein
from __moviepy.video.fx.fadeout import fadeout
from __moviepy.video.fx.freeze import freeze
from __moviepy.video.fx.freeze_region import freeze_region
from __moviepy.video.fx.gamma_corr import gamma_corr
from __moviepy.video.fx.headblur import headblur
from __moviepy.video.fx.invert_colors import invert_colors
from __moviepy.video.fx.loop import loop
from __moviepy.video.fx.lum_contrast import lum_contrast
from __moviepy.video.fx.make_loopable import make_loopable
from __moviepy.video.fx.margin import margin
from __moviepy.video.fx.mask_and import mask_and
from __moviepy.video.fx.mask_color import mask_color
from __moviepy.video.fx.mask_or import mask_or
from __moviepy.video.fx.mirror_x import mirror_x
from __moviepy.video.fx.mirror_y import mirror_y
from __moviepy.video.fx.painting import painting
from __moviepy.video.fx.resize import resize
from __moviepy.video.fx.rotate import rotate
from __moviepy.video.fx.scroll import scroll
from __moviepy.video.fx.speedx import speedx
from __moviepy.video.fx.supersample import supersample
from __moviepy.video.fx.time_mirror import time_mirror
from __moviepy.video.fx.time_symmetrize import time_symmetrize