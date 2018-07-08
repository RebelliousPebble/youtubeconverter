"""
Loads all the fx !
Usage:
import moviepy.audio.fx.all as afx
audio_clip = afx.volume_x(some_clip, .5)
"""

import pkgutil
import moviepy.audio.fx as fx

__all__ = [name for _, name, _ in pkgutil.iter_modules(
    fx.__path__) if name != "all"]

#for name in __all__:
    #exec("from ..%s import %s" % (name, name))

import moviepy.audio.fx.audio_fadein as audio_fadein
import moviepy.audio.fx.audio_fadeout as audio_fadeout
import moviepy.audio.fx.audio_left_right as audio_left_right
import moviepy.audio.fx.audio_loop as audio_loop
import moviepy.audio.fx.audio_normalize as audio_normalize
import moviepy.audio.fx.volumex as volumex