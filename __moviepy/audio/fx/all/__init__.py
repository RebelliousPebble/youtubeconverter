"""
Loads all the fx !
Usage:
import __moviepy.audio.fx.all as afx
audio_clip = afx.volume_x(some_clip, .5)
"""

import pkgutil
import __moviepy.audio.fx as fx

__all__ = [name for _, name, _ in pkgutil.iter_modules(
    fx.__path__) if name != "all"]

#for name in __all__:
    #exec("from ..%s import %s" % (name, name))

import __moviepy.audio.fx.audio_fadein as audio_fadein
import __moviepy.audio.fx.audio_fadeout as audio_fadeout
import __moviepy.audio.fx.audio_left_right as audio_left_right
import __moviepy.audio.fx.audio_loop as audio_loop
import __moviepy.audio.fx.audio_normalize as audio_normalize
import __moviepy.audio.fx.volumex as volumex