#!/usr/bin/python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    from pygame.locals import *

from libs.toolbar import *
from libs.toolreq import *
from libs.gadget import *
from libs.tiptext import *

config = None

class AnimToolAction(Action):
    def get_tip(self):
        if self.gadget.id in tiptext:
            return tiptext[self.gadget.id]
        else:
            return [self.gadget.id]

class DoFirst(AnimToolAction):
    """
    First animation frame
    """
    def selected(self, attrs):
        config.anim.first_frame()

class DoPrev(AnimToolAction):
    """
    Previous animation frame
    """
    def selected(self, attrs):
        config.anim.prev_frame()

class DoPlay(AnimToolAction):
    """
    Play animation
    """
    def selected(self, attrs):
        config.anim.play()

class DoNext(AnimToolAction):
    """
    Next animation frame
    """
    def selected(self, attrs):
        config.anim.next_frame()

class DoLast(AnimToolAction):
    """
    Last animation frame
    """
    def selected(self, attrs):
        config.anim.last_frame()

class DoAnimBlank(AnimToolAction):
    """
    Do nothing
    """
    def selected(self, attrs):
        pass

class DoAddFrame(AnimToolAction):
    """
    Add animation frame
    """
    def selected(self, attrs):
        config.anim.add_frame()

class DoAddFrame(AnimToolAction):
    """
    Add animation frame
    """
    def selected(self, attrs):
        config.anim.add_frame()

class DoDeleteFrame(AnimToolAction):
    """
    Delete animation frame
    """
    def selected(self, attrs):
        config.anim.delete_frame()

def init_animtoolbar(config_in):
    global config
    config = config_in

    scaleX = config.fontx // 8
    scaleY = config.fonty // 12
    scaledown = 4 // min(scaleX,scaleY)
    minitools_image = imgload('animtools.png', scaleX=scaleX, scaleY=scaleY, scaledown=scaledown)
    numtools=8
    numsubtools=3
    h = minitools_image.get_height()//numsubtools
    w = minitools_image.get_width()
    mt_width = config.screen_width-25*scaleX
    minitoolbar_canvas = pygame.Surface((mt_width,h),0)

    minitoolbar = Toolbar(minitoolbar_canvas, config.cursor, (0,0,mt_width,h), minitools_image, height=numsubtools, tip_event=config.TOOLTIPEVENT)
    minitoolbar.add_grid((0,0,w,10*scaleY), numtools, 1, attr_list=[
        ["first",       ToolGadget.TT_SINGLE, "", DoFirst],
        ["prev",        ToolGadget.TT_SINGLE, "", DoPrev],
        ["play",        ToolGadget.TT_SINGLE, "", DoPlay],
        ["next",        ToolGadget.TT_SINGLE, "", DoNext],
        ["last",        ToolGadget.TT_SINGLE, "", DoLast],
        ["animblank",   ToolGadget.TT_SINGLE, "", DoAnimBlank],
        ["addframe",    ToolGadget.TT_SINGLE, "", DoAddFrame],
        ["deleteframe", ToolGadget.TT_SINGLE, "", DoDeleteFrame]
    ])

    minitoolbar.tool_id("first").has_subtool = False
    minitoolbar.tool_id("prev").has_subtool = False
    minitoolbar.tool_id("play").has_subtool = False
    minitoolbar.tool_id("next").has_subtool = False
    minitoolbar.tool_id("last").has_subtool = False
    minitoolbar.tool_id("addframe").has_subtool = False
    minitoolbar.tool_id("deleteframe").has_subtool = False

    #Add frame count text to toolbar
    gx,gy,gw,gh = minitoolbar.tools[-1].rect
    gx += gw + scaleX*4
    gw = scaleX*8*9  #make text label 9 chars wide
    textg = Gadget(Gadget.TYPE_LABEL, "         ", (gx,gy,gw,gh), id="framecount")
    minitoolbar.tools.append(textg)
    minitoolbar.add_coords(textg)

    #Add frame slider to toolbar
    gx,gy,gw,gh = minitoolbar.tools[-1].rect
    gx += gw + scaleX*4
    gw = mt_width - gx - scaleX*4
    gh = scaleX * 11
    sliderg = Gadget(Gadget.TYPE_PROP, "-", (gx,gy,gw,gh), maxvalue=100, id="frameslider")
    minitoolbar.tools.append(sliderg)
    minitoolbar.add_coords(sliderg)

    return minitoolbar


