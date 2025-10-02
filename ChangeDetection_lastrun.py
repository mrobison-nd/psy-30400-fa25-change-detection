#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.2),
    on July 30, 2025, at 13:20
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.2'
expName = 'ChangeDetection'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [2560, 1440]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='G:\\My Drive\\Teaching\\FA 25 PSY 30400\\Experiments\\Change detection\\ChangeDetection_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('key_resp_5') is None:
        # initialise key_resp_5
        key_resp_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_5',
        )
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "welcome" ---
    welcome_text = visual.TextStim(win=win, name='welcome_text',
        text='Welcome!\n\nThis task is a version of the Luck & Vogel (1997) "change-detection" task.\n\nPress the spacebar to proceed.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "instruction1" ---
    instruct1_text = visual.TextStim(win=win, name='instruct1_text',
        text="On each trial, you will see a pattern of colored squares. There will be anywhere from 2 to 8 squares in the display.\n\nThe display will appear only briefly, followed by a short delay. Then, the display will reappear, and one of the squares will be outlined by a black circle.\n\nYour task is to indicate whether this square is the same color or a different color than its initial presentation. Press the 'F' key for same, and the 'J' key for different.\n\nBelow are example trials. Press the right arrow key to continue.",
        font='Arial',
        pos=(0, .2), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    image = visual.ImageStim(
        win=win,
        name='image', 
        image='examples.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -.2), draggable=False, size=(0.6, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "start_practice" ---
    welcome_text_2 = visual.TextStim(win=win, name='welcome_text_2',
        text='We will start with some practice trials.\n\nRemember: press F for same, and J for different.\n\nPress the spacebar to proceed.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    
    # --- Initialize components for Routine "encoding" ---
    item1 = visual.Rect(
        win=win, name='item1',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    item2 = visual.Rect(
        win=win, name='item2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    item3 = visual.Rect(
        win=win, name='item3',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    item4 = visual.Rect(
        win=win, name='item4',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    item5 = visual.Rect(
        win=win, name='item5',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    item6 = visual.Rect(
        win=win, name='item6',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    item7 = visual.Rect(
        win=win, name='item7',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    item8 = visual.Rect(
        win=win, name='item8',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    fixation = visual.TextStim(win=win, name='fixation',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    
    # --- Initialize components for Routine "delay_interval" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "test" ---
    test_indicator = visual.ShapeStim(
        win=win, name='test_indicator',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=5.0,
        colorSpace='rgb', lineColor='black', fillColor='grey',
        opacity=None, depth=0.0, interpolate=True)
    item1_2 = visual.Rect(
        win=win, name='item1_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    item2_2 = visual.Rect(
        win=win, name='item2_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    item3_2 = visual.Rect(
        win=win, name='item3_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    item4_2 = visual.Rect(
        win=win, name='item4_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    item5_2 = visual.Rect(
        win=win, name='item5_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    item6_2 = visual.Rect(
        win=win, name='item6_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    item7_2 = visual.Rect(
        win=win, name='item7_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    item8_2 = visual.Rect(
        win=win, name='item8_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-8.0, interpolate=True)
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    
    # --- Initialize components for Routine "feedback" ---
    fb_text = visual.TextStim(win=win, name='fb_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "end_practice" ---
    instruct1_text_2 = visual.TextStim(win=win, name='instruct1_text_2',
        text='That is the end of the practice trials.\n\nWe will now start the real trials.\n\nPress the right arrow key to begin.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    
    # --- Initialize components for Routine "encoding" ---
    item1 = visual.Rect(
        win=win, name='item1',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    item2 = visual.Rect(
        win=win, name='item2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    item3 = visual.Rect(
        win=win, name='item3',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    item4 = visual.Rect(
        win=win, name='item4',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    item5 = visual.Rect(
        win=win, name='item5',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    item6 = visual.Rect(
        win=win, name='item6',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    item7 = visual.Rect(
        win=win, name='item7',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    item8 = visual.Rect(
        win=win, name='item8',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    fixation = visual.TextStim(win=win, name='fixation',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    
    # --- Initialize components for Routine "test" ---
    test_indicator = visual.ShapeStim(
        win=win, name='test_indicator',
        size=(0.1, 0.1), vertices='circle',
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=5.0,
        colorSpace='rgb', lineColor='black', fillColor='grey',
        opacity=None, depth=0.0, interpolate=True)
    item1_2 = visual.Rect(
        win=win, name='item1_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    item2_2 = visual.Rect(
        win=win, name='item2_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    item3_2 = visual.Rect(
        win=win, name='item3_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    item4_2 = visual.Rect(
        win=win, name='item4_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    item5_2 = visual.Rect(
        win=win, name='item5_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    item6_2 = visual.Rect(
        win=win, name='item6_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    item7_2 = visual.Rect(
        win=win, name='item7_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    item8_2 = visual.Rect(
        win=win, name='item8_2',
        width=(0.05, 0.05)[0], height=(0.05, 0.05)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-8.0, interpolate=True)
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    
    # --- Initialize components for Routine "end_exp" ---
    end_text = visual.TextStim(win=win, name='end_text',
        text='That is the end of the experiment.\n\nThank you for participating!\n\nThis window will close automatically.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "welcome" ---
    # create an object to store info about Routine welcome
    welcome = data.Routine(
        name='welcome',
        components=[welcome_text, key_resp],
    )
    welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # store start times for welcome
    welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome.tStart = globalClock.getTime(format='float')
    welcome.status = STARTED
    thisExp.addData('welcome.started', welcome.tStart)
    welcome.maxDuration = None
    # keep track of which components have finished
    welcomeComponents = welcome.components
    for thisComponent in welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome" ---
    welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_text* updates
        
        # if welcome_text is starting this frame...
        if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_text.frameNStart = frameN  # exact frame index
            welcome_text.tStart = t  # local t and not account for scr refresh
            welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_text.started')
            # update status
            welcome_text.status = STARTED
            welcome_text.setAutoDraw(True)
        
        # if welcome_text is active this frame...
        if welcome_text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome
    welcome.tStop = globalClock.getTime(format='float')
    welcome.tStopRefresh = tThisFlipGlobal
    thisExp.addData('welcome.stopped', welcome.tStop)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction1" ---
    # create an object to store info about Routine instruction1
    instruction1 = data.Routine(
        name='instruction1',
        components=[instruct1_text, key_resp_2, image],
    )
    instruction1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # store start times for instruction1
    instruction1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instruction1.tStart = globalClock.getTime(format='float')
    instruction1.status = STARTED
    thisExp.addData('instruction1.started', instruction1.tStart)
    instruction1.maxDuration = None
    # keep track of which components have finished
    instruction1Components = instruction1.components
    for thisComponent in instruction1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction1" ---
    instruction1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct1_text* updates
        
        # if instruct1_text is starting this frame...
        if instruct1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruct1_text.frameNStart = frameN  # exact frame index
            instruct1_text.tStart = t  # local t and not account for scr refresh
            instruct1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct1_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruct1_text.started')
            # update status
            instruct1_text.status = STARTED
            instruct1_text.setAutoDraw(True)
        
        # if instruct1_text is active this frame...
        if instruct1_text.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['right'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *image* updates
        
        # if image is starting this frame...
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            # update status
            image.status = STARTED
            image.setAutoDraw(True)
        
        # if image is active this frame...
        if image.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instruction1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction1" ---
    for thisComponent in instruction1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instruction1
    instruction1.tStop = globalClock.getTime(format='float')
    instruction1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instruction1.stopped', instruction1.tStop)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "start_practice" ---
    # create an object to store info about Routine start_practice
    start_practice = data.Routine(
        name='start_practice',
        components=[welcome_text_2, key_resp_5],
    )
    start_practice.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_5
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # store start times for start_practice
    start_practice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    start_practice.tStart = globalClock.getTime(format='float')
    start_practice.status = STARTED
    thisExp.addData('start_practice.started', start_practice.tStart)
    start_practice.maxDuration = None
    # keep track of which components have finished
    start_practiceComponents = start_practice.components
    for thisComponent in start_practice.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "start_practice" ---
    start_practice.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_text_2* updates
        
        # if welcome_text_2 is starting this frame...
        if welcome_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_text_2.frameNStart = frameN  # exact frame index
            welcome_text_2.tStart = t  # local t and not account for scr refresh
            welcome_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'welcome_text_2.started')
            # update status
            welcome_text_2.status = STARTED
            welcome_text_2.setAutoDraw(True)
        
        # if welcome_text_2 is active this frame...
        if welcome_text_2.status == STARTED:
            # update params
            pass
        
        # *key_resp_5* updates
        waitOnFlip = False
        
        # if key_resp_5 is starting this frame...
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_5.started')
            # update status
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            start_practice.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_practice.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start_practice" ---
    for thisComponent in start_practice.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for start_practice
    start_practice.tStop = globalClock.getTime(format='float')
    start_practice.tStopRefresh = tThisFlipGlobal
    thisExp.addData('start_practice.stopped', start_practice.tStop)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    thisExp.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        thisExp.addData('key_resp_5.rt', key_resp_5.rt)
        thisExp.addData('key_resp_5.duration', key_resp_5.duration)
    thisExp.nextEntry()
    # the Routine "start_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_trials = data.TrialHandler2(
        name='practice_trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('practice_trials.csv'), 
        seed=None, 
    )
    thisExp.addLoop(practice_trials)  # add the loop to the experiment
    thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            globals()[paramName] = thisPractice_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPractice_trial in practice_trials:
        currentLoop = practice_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
        if thisPractice_trial != None:
            for paramName in thisPractice_trial:
                globals()[paramName] = thisPractice_trial[paramName]
        
        # --- Prepare to start Routine "encoding" ---
        # create an object to store info about Routine encoding
        encoding = data.Routine(
            name='encoding',
            components=[item1, item2, item3, item4, item5, item6, item7, item8, fixation],
        )
        encoding.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        item1.setFillColor(color1)
        item1.setPos(loc1)
        item1.setLineColor(color1)
        item2.setFillColor(color2)
        item2.setPos(loc2)
        item2.setLineColor(color2)
        item3.setFillColor(color3)
        item3.setPos(loc3)
        item3.setLineColor(color3)
        item4.setFillColor(color4)
        item4.setPos(loc4)
        item4.setLineColor(color4)
        item5.setFillColor(color5)
        item5.setPos(loc5)
        item5.setLineColor(color5)
        item6.setFillColor(color6)
        item6.setPos(loc6)
        item6.setLineColor(color6)
        item7.setFillColor(color7)
        item7.setPos(loc7)
        item7.setLineColor(color7)
        item8.setFillColor(color8)
        item8.setPos(loc8)
        item8.setLineColor(color8)
        # store start times for encoding
        encoding.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        encoding.tStart = globalClock.getTime(format='float')
        encoding.status = STARTED
        thisExp.addData('encoding.started', encoding.tStart)
        encoding.maxDuration = None
        # keep track of which components have finished
        encodingComponents = encoding.components
        for thisComponent in encoding.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "encoding" ---
        # if trial has changed, end Routine now
        if isinstance(practice_trials, data.TrialHandler2) and thisPractice_trial.thisN != practice_trials.thisTrial.thisN:
            continueRoutine = False
        encoding.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.75:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *item1* updates
            
            # if item1 is starting this frame...
            if item1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item1.frameNStart = frameN  # exact frame index
                item1.tStart = t  # local t and not account for scr refresh
                item1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item1.started')
                # update status
                item1.status = STARTED
                item1.setAutoDraw(True)
            
            # if item1 is active this frame...
            if item1.status == STARTED:
                # update params
                pass
            
            # if item1 is stopping this frame...
            if item1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item1.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item1.tStop = t  # not accounting for scr refresh
                    item1.tStopRefresh = tThisFlipGlobal  # on global time
                    item1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item1.stopped')
                    # update status
                    item1.status = FINISHED
                    item1.setAutoDraw(False)
            
            # *item2* updates
            
            # if item2 is starting this frame...
            if item2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item2.frameNStart = frameN  # exact frame index
                item2.tStart = t  # local t and not account for scr refresh
                item2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item2.started')
                # update status
                item2.status = STARTED
                item2.setAutoDraw(True)
            
            # if item2 is active this frame...
            if item2.status == STARTED:
                # update params
                pass
            
            # if item2 is stopping this frame...
            if item2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item2.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item2.tStop = t  # not accounting for scr refresh
                    item2.tStopRefresh = tThisFlipGlobal  # on global time
                    item2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item2.stopped')
                    # update status
                    item2.status = FINISHED
                    item2.setAutoDraw(False)
            
            # *item3* updates
            
            # if item3 is starting this frame...
            if item3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item3.frameNStart = frameN  # exact frame index
                item3.tStart = t  # local t and not account for scr refresh
                item3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item3.started')
                # update status
                item3.status = STARTED
                item3.setAutoDraw(True)
            
            # if item3 is active this frame...
            if item3.status == STARTED:
                # update params
                pass
            
            # if item3 is stopping this frame...
            if item3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item3.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item3.tStop = t  # not accounting for scr refresh
                    item3.tStopRefresh = tThisFlipGlobal  # on global time
                    item3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item3.stopped')
                    # update status
                    item3.status = FINISHED
                    item3.setAutoDraw(False)
            
            # *item4* updates
            
            # if item4 is starting this frame...
            if item4.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item4.frameNStart = frameN  # exact frame index
                item4.tStart = t  # local t and not account for scr refresh
                item4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item4.started')
                # update status
                item4.status = STARTED
                item4.setAutoDraw(True)
            
            # if item4 is active this frame...
            if item4.status == STARTED:
                # update params
                pass
            
            # if item4 is stopping this frame...
            if item4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item4.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item4.tStop = t  # not accounting for scr refresh
                    item4.tStopRefresh = tThisFlipGlobal  # on global time
                    item4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item4.stopped')
                    # update status
                    item4.status = FINISHED
                    item4.setAutoDraw(False)
            
            # *item5* updates
            
            # if item5 is starting this frame...
            if item5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item5.frameNStart = frameN  # exact frame index
                item5.tStart = t  # local t and not account for scr refresh
                item5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item5.started')
                # update status
                item5.status = STARTED
                item5.setAutoDraw(True)
            
            # if item5 is active this frame...
            if item5.status == STARTED:
                # update params
                pass
            
            # if item5 is stopping this frame...
            if item5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item5.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item5.tStop = t  # not accounting for scr refresh
                    item5.tStopRefresh = tThisFlipGlobal  # on global time
                    item5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item5.stopped')
                    # update status
                    item5.status = FINISHED
                    item5.setAutoDraw(False)
            
            # *item6* updates
            
            # if item6 is starting this frame...
            if item6.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item6.frameNStart = frameN  # exact frame index
                item6.tStart = t  # local t and not account for scr refresh
                item6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item6.started')
                # update status
                item6.status = STARTED
                item6.setAutoDraw(True)
            
            # if item6 is active this frame...
            if item6.status == STARTED:
                # update params
                pass
            
            # if item6 is stopping this frame...
            if item6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item6.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item6.tStop = t  # not accounting for scr refresh
                    item6.tStopRefresh = tThisFlipGlobal  # on global time
                    item6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item6.stopped')
                    # update status
                    item6.status = FINISHED
                    item6.setAutoDraw(False)
            
            # *item7* updates
            
            # if item7 is starting this frame...
            if item7.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item7.frameNStart = frameN  # exact frame index
                item7.tStart = t  # local t and not account for scr refresh
                item7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item7.started')
                # update status
                item7.status = STARTED
                item7.setAutoDraw(True)
            
            # if item7 is active this frame...
            if item7.status == STARTED:
                # update params
                pass
            
            # if item7 is stopping this frame...
            if item7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item7.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item7.tStop = t  # not accounting for scr refresh
                    item7.tStopRefresh = tThisFlipGlobal  # on global time
                    item7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item7.stopped')
                    # update status
                    item7.status = FINISHED
                    item7.setAutoDraw(False)
            
            # *item8* updates
            
            # if item8 is starting this frame...
            if item8.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item8.frameNStart = frameN  # exact frame index
                item8.tStart = t  # local t and not account for scr refresh
                item8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item8.started')
                # update status
                item8.status = STARTED
                item8.setAutoDraw(True)
            
            # if item8 is active this frame...
            if item8.status == STARTED:
                # update params
                pass
            
            # if item8 is stopping this frame...
            if item8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item8.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item8.tStop = t  # not accounting for scr refresh
                    item8.tStopRefresh = tThisFlipGlobal  # on global time
                    item8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item8.stopped')
                    # update status
                    item8.status = FINISHED
                    item8.setAutoDraw(False)
            
            # *fixation* updates
            
            # if fixation is starting this frame...
            if fixation.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                # update status
                fixation.status = STARTED
                fixation.setAutoDraw(True)
            
            # if fixation is active this frame...
            if fixation.status == STARTED:
                # update params
                pass
            
            # if fixation is stopping this frame...
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    # update status
                    fixation.status = FINISHED
                    fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                encoding.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in encoding.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "encoding" ---
        for thisComponent in encoding.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for encoding
        encoding.tStop = globalClock.getTime(format='float')
        encoding.tStopRefresh = tThisFlipGlobal
        thisExp.addData('encoding.stopped', encoding.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if encoding.maxDurationReached:
            routineTimer.addTime(-encoding.maxDuration)
        elif encoding.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.750000)
        
        # --- Prepare to start Routine "delay_interval" ---
        # create an object to store info about Routine delay_interval
        delay_interval = data.Routine(
            name='delay_interval',
            components=[text],
        )
        delay_interval.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for delay_interval
        delay_interval.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        delay_interval.tStart = globalClock.getTime(format='float')
        delay_interval.status = STARTED
        thisExp.addData('delay_interval.started', delay_interval.tStart)
        delay_interval.maxDuration = None
        # keep track of which components have finished
        delay_intervalComponents = delay_interval.components
        for thisComponent in delay_interval.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "delay_interval" ---
        # if trial has changed, end Routine now
        if isinstance(practice_trials, data.TrialHandler2) and thisPractice_trial.thisN != practice_trials.thisTrial.thisN:
            continueRoutine = False
        delay_interval.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.9:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + .9-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                delay_interval.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in delay_interval.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "delay_interval" ---
        for thisComponent in delay_interval.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for delay_interval
        delay_interval.tStop = globalClock.getTime(format='float')
        delay_interval.tStopRefresh = tThisFlipGlobal
        thisExp.addData('delay_interval.stopped', delay_interval.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if delay_interval.maxDurationReached:
            routineTimer.addTime(-delay_interval.maxDuration)
        elif delay_interval.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.900000)
        
        # --- Prepare to start Routine "test" ---
        # create an object to store info about Routine test
        test = data.Routine(
            name='test',
            components=[test_indicator, item1_2, item2_2, item3_2, item4_2, item5_2, item6_2, item7_2, item8_2, key_resp_3],
        )
        test.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        test_indicator.setPos(loc1)
        item1_2.setFillColor(testcolor)
        item1_2.setPos(loc1)
        item1_2.setLineColor(testcolor)
        item2_2.setFillColor(color2)
        item2_2.setPos(loc2)
        item2_2.setLineColor(color2)
        item3_2.setFillColor(color3)
        item3_2.setPos(loc3)
        item3_2.setLineColor(color3)
        item4_2.setFillColor(color4)
        item4_2.setPos(loc4)
        item4_2.setLineColor(color4)
        item5_2.setFillColor(color5)
        item5_2.setPos(loc5)
        item5_2.setLineColor(color5)
        item6_2.setFillColor(color6)
        item6_2.setPos(loc6)
        item6_2.setLineColor(color6)
        item7_2.setFillColor(color7)
        item7_2.setPos(loc7)
        item7_2.setLineColor(color7)
        item8_2.setFillColor(color8)
        item8_2.setPos(loc8)
        item8_2.setLineColor(color8)
        # create starting attributes for key_resp_3
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # store start times for test
        test.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        test.tStart = globalClock.getTime(format='float')
        test.status = STARTED
        thisExp.addData('test.started', test.tStart)
        test.maxDuration = None
        # keep track of which components have finished
        testComponents = test.components
        for thisComponent in test.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test" ---
        # if trial has changed, end Routine now
        if isinstance(practice_trials, data.TrialHandler2) and thisPractice_trial.thisN != practice_trials.thisTrial.thisN:
            continueRoutine = False
        test.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *test_indicator* updates
            
            # if test_indicator is starting this frame...
            if test_indicator.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_indicator.frameNStart = frameN  # exact frame index
                test_indicator.tStart = t  # local t and not account for scr refresh
                test_indicator.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_indicator, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_indicator.started')
                # update status
                test_indicator.status = STARTED
                test_indicator.setAutoDraw(True)
            
            # if test_indicator is active this frame...
            if test_indicator.status == STARTED:
                # update params
                pass
            
            # *item1_2* updates
            
            # if item1_2 is starting this frame...
            if item1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item1_2.frameNStart = frameN  # exact frame index
                item1_2.tStart = t  # local t and not account for scr refresh
                item1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item1_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item1_2.started')
                # update status
                item1_2.status = STARTED
                item1_2.setAutoDraw(True)
            
            # if item1_2 is active this frame...
            if item1_2.status == STARTED:
                # update params
                pass
            
            # *item2_2* updates
            
            # if item2_2 is starting this frame...
            if item2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item2_2.frameNStart = frameN  # exact frame index
                item2_2.tStart = t  # local t and not account for scr refresh
                item2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item2_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item2_2.started')
                # update status
                item2_2.status = STARTED
                item2_2.setAutoDraw(True)
            
            # if item2_2 is active this frame...
            if item2_2.status == STARTED:
                # update params
                pass
            
            # *item3_2* updates
            
            # if item3_2 is starting this frame...
            if item3_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item3_2.frameNStart = frameN  # exact frame index
                item3_2.tStart = t  # local t and not account for scr refresh
                item3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item3_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item3_2.started')
                # update status
                item3_2.status = STARTED
                item3_2.setAutoDraw(True)
            
            # if item3_2 is active this frame...
            if item3_2.status == STARTED:
                # update params
                pass
            
            # *item4_2* updates
            
            # if item4_2 is starting this frame...
            if item4_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item4_2.frameNStart = frameN  # exact frame index
                item4_2.tStart = t  # local t and not account for scr refresh
                item4_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item4_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item4_2.started')
                # update status
                item4_2.status = STARTED
                item4_2.setAutoDraw(True)
            
            # if item4_2 is active this frame...
            if item4_2.status == STARTED:
                # update params
                pass
            
            # *item5_2* updates
            
            # if item5_2 is starting this frame...
            if item5_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item5_2.frameNStart = frameN  # exact frame index
                item5_2.tStart = t  # local t and not account for scr refresh
                item5_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item5_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item5_2.started')
                # update status
                item5_2.status = STARTED
                item5_2.setAutoDraw(True)
            
            # if item5_2 is active this frame...
            if item5_2.status == STARTED:
                # update params
                pass
            
            # *item6_2* updates
            
            # if item6_2 is starting this frame...
            if item6_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item6_2.frameNStart = frameN  # exact frame index
                item6_2.tStart = t  # local t and not account for scr refresh
                item6_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item6_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item6_2.started')
                # update status
                item6_2.status = STARTED
                item6_2.setAutoDraw(True)
            
            # if item6_2 is active this frame...
            if item6_2.status == STARTED:
                # update params
                pass
            
            # *item7_2* updates
            
            # if item7_2 is starting this frame...
            if item7_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item7_2.frameNStart = frameN  # exact frame index
                item7_2.tStart = t  # local t and not account for scr refresh
                item7_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item7_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item7_2.started')
                # update status
                item7_2.status = STARTED
                item7_2.setAutoDraw(True)
            
            # if item7_2 is active this frame...
            if item7_2.status == STARTED:
                # update params
                pass
            
            # *item8_2* updates
            
            # if item8_2 is starting this frame...
            if item8_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item8_2.frameNStart = frameN  # exact frame index
                item8_2.tStart = t  # local t and not account for scr refresh
                item8_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item8_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item8_2.started')
                # update status
                item8_2.status = STARTED
                item8_2.setAutoDraw(True)
            
            # if item8_2 is active this frame...
            if item8_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_3* updates
            waitOnFlip = False
            
            # if key_resp_3 is starting this frame...
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                # update status
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_3.keys == str(correct)) or (key_resp_3.keys == correct):
                        key_resp_3.corr = 1
                    else:
                        key_resp_3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                test.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test" ---
        for thisComponent in test.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for test
        test.tStop = globalClock.getTime(format='float')
        test.tStopRefresh = tThisFlipGlobal
        thisExp.addData('test.stopped', test.tStop)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               key_resp_3.corr = 1;  # correct non-response
            else:
               key_resp_3.corr = 0;  # failed to respond (incorrectly)
        # store data for practice_trials (TrialHandler)
        practice_trials.addData('key_resp_3.keys',key_resp_3.keys)
        practice_trials.addData('key_resp_3.corr', key_resp_3.corr)
        if key_resp_3.keys != None:  # we had a response
            practice_trials.addData('key_resp_3.rt', key_resp_3.rt)
            practice_trials.addData('key_resp_3.duration', key_resp_3.duration)
        # the Routine "test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        # create an object to store info about Routine feedback
        feedback = data.Routine(
            name='feedback',
            components=[fb_text],
        )
        feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        if key_resp_3.corr == 1:
            feedback_text = 'correct'
            feedback_color = 'cyan'
        if key_resp_3.corr == 0:
            feedback_text = 'incorrect'
            feedback_color = 'darkred'
        fb_text.setColor(feedback_color, colorSpace='rgb')
        fb_text.setText(feedback_text)
        # store start times for feedback
        feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        feedback.tStart = globalClock.getTime(format='float')
        feedback.status = STARTED
        thisExp.addData('feedback.started', feedback.tStart)
        feedback.maxDuration = None
        # keep track of which components have finished
        feedbackComponents = feedback.components
        for thisComponent in feedback.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback" ---
        # if trial has changed, end Routine now
        if isinstance(practice_trials, data.TrialHandler2) and thisPractice_trial.thisN != practice_trials.thisTrial.thisN:
            continueRoutine = False
        feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fb_text* updates
            
            # if fb_text is starting this frame...
            if fb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fb_text.frameNStart = frameN  # exact frame index
                fb_text.tStart = t  # local t and not account for scr refresh
                fb_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fb_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fb_text.started')
                # update status
                fb_text.status = STARTED
                fb_text.setAutoDraw(True)
            
            # if fb_text is active this frame...
            if fb_text.status == STARTED:
                # update params
                pass
            
            # if fb_text is stopping this frame...
            if fb_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fb_text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fb_text.tStop = t  # not accounting for scr refresh
                    fb_text.tStopRefresh = tThisFlipGlobal  # on global time
                    fb_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fb_text.stopped')
                    # update status
                    fb_text.status = FINISHED
                    fb_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for feedback
        feedback.tStop = globalClock.getTime(format='float')
        feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('feedback.stopped', feedback.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if feedback.maxDurationReached:
            routineTimer.addTime(-feedback.maxDuration)
        elif feedback.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practice_trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end_practice" ---
    # create an object to store info about Routine end_practice
    end_practice = data.Routine(
        name='end_practice',
        components=[instruct1_text_2, key_resp_4],
    )
    end_practice.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_4
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # store start times for end_practice
    end_practice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end_practice.tStart = globalClock.getTime(format='float')
    end_practice.status = STARTED
    thisExp.addData('end_practice.started', end_practice.tStart)
    end_practice.maxDuration = None
    # keep track of which components have finished
    end_practiceComponents = end_practice.components
    for thisComponent in end_practice.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_practice" ---
    end_practice.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct1_text_2* updates
        
        # if instruct1_text_2 is starting this frame...
        if instruct1_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruct1_text_2.frameNStart = frameN  # exact frame index
            instruct1_text_2.tStart = t  # local t and not account for scr refresh
            instruct1_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct1_text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruct1_text_2.started')
            # update status
            instruct1_text_2.status = STARTED
            instruct1_text_2.setAutoDraw(True)
        
        # if instruct1_text_2 is active this frame...
        if instruct1_text_2.status == STARTED:
            # update params
            pass
        
        # *key_resp_4* updates
        waitOnFlip = False
        
        # if key_resp_4 is starting this frame...
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            # update status
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['right'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end_practice.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_practice.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_practice" ---
    for thisComponent in end_practice.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end_practice
    end_practice.tStop = globalClock.getTime(format='float')
    end_practice.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end_practice.stopped', end_practice.tStop)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    thisExp.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        thisExp.addData('key_resp_4.rt', key_resp_4.rt)
        thisExp.addData('key_resp_4.duration', key_resp_4.duration)
    thisExp.nextEntry()
    # the Routine "end_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('trials.csv'), 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "encoding" ---
        # create an object to store info about Routine encoding
        encoding = data.Routine(
            name='encoding',
            components=[item1, item2, item3, item4, item5, item6, item7, item8, fixation],
        )
        encoding.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        item1.setFillColor(color1)
        item1.setPos(loc1)
        item1.setLineColor(color1)
        item2.setFillColor(color2)
        item2.setPos(loc2)
        item2.setLineColor(color2)
        item3.setFillColor(color3)
        item3.setPos(loc3)
        item3.setLineColor(color3)
        item4.setFillColor(color4)
        item4.setPos(loc4)
        item4.setLineColor(color4)
        item5.setFillColor(color5)
        item5.setPos(loc5)
        item5.setLineColor(color5)
        item6.setFillColor(color6)
        item6.setPos(loc6)
        item6.setLineColor(color6)
        item7.setFillColor(color7)
        item7.setPos(loc7)
        item7.setLineColor(color7)
        item8.setFillColor(color8)
        item8.setPos(loc8)
        item8.setLineColor(color8)
        # store start times for encoding
        encoding.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        encoding.tStart = globalClock.getTime(format='float')
        encoding.status = STARTED
        thisExp.addData('encoding.started', encoding.tStart)
        encoding.maxDuration = None
        # keep track of which components have finished
        encodingComponents = encoding.components
        for thisComponent in encoding.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "encoding" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        encoding.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.75:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *item1* updates
            
            # if item1 is starting this frame...
            if item1.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item1.frameNStart = frameN  # exact frame index
                item1.tStart = t  # local t and not account for scr refresh
                item1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item1.started')
                # update status
                item1.status = STARTED
                item1.setAutoDraw(True)
            
            # if item1 is active this frame...
            if item1.status == STARTED:
                # update params
                pass
            
            # if item1 is stopping this frame...
            if item1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item1.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item1.tStop = t  # not accounting for scr refresh
                    item1.tStopRefresh = tThisFlipGlobal  # on global time
                    item1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item1.stopped')
                    # update status
                    item1.status = FINISHED
                    item1.setAutoDraw(False)
            
            # *item2* updates
            
            # if item2 is starting this frame...
            if item2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item2.frameNStart = frameN  # exact frame index
                item2.tStart = t  # local t and not account for scr refresh
                item2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item2.started')
                # update status
                item2.status = STARTED
                item2.setAutoDraw(True)
            
            # if item2 is active this frame...
            if item2.status == STARTED:
                # update params
                pass
            
            # if item2 is stopping this frame...
            if item2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item2.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item2.tStop = t  # not accounting for scr refresh
                    item2.tStopRefresh = tThisFlipGlobal  # on global time
                    item2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item2.stopped')
                    # update status
                    item2.status = FINISHED
                    item2.setAutoDraw(False)
            
            # *item3* updates
            
            # if item3 is starting this frame...
            if item3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item3.frameNStart = frameN  # exact frame index
                item3.tStart = t  # local t and not account for scr refresh
                item3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item3.started')
                # update status
                item3.status = STARTED
                item3.setAutoDraw(True)
            
            # if item3 is active this frame...
            if item3.status == STARTED:
                # update params
                pass
            
            # if item3 is stopping this frame...
            if item3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item3.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item3.tStop = t  # not accounting for scr refresh
                    item3.tStopRefresh = tThisFlipGlobal  # on global time
                    item3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item3.stopped')
                    # update status
                    item3.status = FINISHED
                    item3.setAutoDraw(False)
            
            # *item4* updates
            
            # if item4 is starting this frame...
            if item4.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item4.frameNStart = frameN  # exact frame index
                item4.tStart = t  # local t and not account for scr refresh
                item4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item4.started')
                # update status
                item4.status = STARTED
                item4.setAutoDraw(True)
            
            # if item4 is active this frame...
            if item4.status == STARTED:
                # update params
                pass
            
            # if item4 is stopping this frame...
            if item4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item4.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item4.tStop = t  # not accounting for scr refresh
                    item4.tStopRefresh = tThisFlipGlobal  # on global time
                    item4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item4.stopped')
                    # update status
                    item4.status = FINISHED
                    item4.setAutoDraw(False)
            
            # *item5* updates
            
            # if item5 is starting this frame...
            if item5.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item5.frameNStart = frameN  # exact frame index
                item5.tStart = t  # local t and not account for scr refresh
                item5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item5.started')
                # update status
                item5.status = STARTED
                item5.setAutoDraw(True)
            
            # if item5 is active this frame...
            if item5.status == STARTED:
                # update params
                pass
            
            # if item5 is stopping this frame...
            if item5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item5.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item5.tStop = t  # not accounting for scr refresh
                    item5.tStopRefresh = tThisFlipGlobal  # on global time
                    item5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item5.stopped')
                    # update status
                    item5.status = FINISHED
                    item5.setAutoDraw(False)
            
            # *item6* updates
            
            # if item6 is starting this frame...
            if item6.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item6.frameNStart = frameN  # exact frame index
                item6.tStart = t  # local t and not account for scr refresh
                item6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item6.started')
                # update status
                item6.status = STARTED
                item6.setAutoDraw(True)
            
            # if item6 is active this frame...
            if item6.status == STARTED:
                # update params
                pass
            
            # if item6 is stopping this frame...
            if item6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item6.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item6.tStop = t  # not accounting for scr refresh
                    item6.tStopRefresh = tThisFlipGlobal  # on global time
                    item6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item6.stopped')
                    # update status
                    item6.status = FINISHED
                    item6.setAutoDraw(False)
            
            # *item7* updates
            
            # if item7 is starting this frame...
            if item7.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item7.frameNStart = frameN  # exact frame index
                item7.tStart = t  # local t and not account for scr refresh
                item7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item7.started')
                # update status
                item7.status = STARTED
                item7.setAutoDraw(True)
            
            # if item7 is active this frame...
            if item7.status == STARTED:
                # update params
                pass
            
            # if item7 is stopping this frame...
            if item7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item7.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item7.tStop = t  # not accounting for scr refresh
                    item7.tStopRefresh = tThisFlipGlobal  # on global time
                    item7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item7.stopped')
                    # update status
                    item7.status = FINISHED
                    item7.setAutoDraw(False)
            
            # *item8* updates
            
            # if item8 is starting this frame...
            if item8.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                item8.frameNStart = frameN  # exact frame index
                item8.tStart = t  # local t and not account for scr refresh
                item8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item8.started')
                # update status
                item8.status = STARTED
                item8.setAutoDraw(True)
            
            # if item8 is active this frame...
            if item8.status == STARTED:
                # update params
                pass
            
            # if item8 is stopping this frame...
            if item8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > item8.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    item8.tStop = t  # not accounting for scr refresh
                    item8.tStopRefresh = tThisFlipGlobal  # on global time
                    item8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'item8.stopped')
                    # update status
                    item8.status = FINISHED
                    item8.setAutoDraw(False)
            
            # *fixation* updates
            
            # if fixation is starting this frame...
            if fixation.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                # update status
                fixation.status = STARTED
                fixation.setAutoDraw(True)
            
            # if fixation is active this frame...
            if fixation.status == STARTED:
                # update params
                pass
            
            # if fixation is stopping this frame...
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    # update status
                    fixation.status = FINISHED
                    fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                encoding.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in encoding.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "encoding" ---
        for thisComponent in encoding.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for encoding
        encoding.tStop = globalClock.getTime(format='float')
        encoding.tStopRefresh = tThisFlipGlobal
        thisExp.addData('encoding.stopped', encoding.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if encoding.maxDurationReached:
            routineTimer.addTime(-encoding.maxDuration)
        elif encoding.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.750000)
        
        # --- Prepare to start Routine "test" ---
        # create an object to store info about Routine test
        test = data.Routine(
            name='test',
            components=[test_indicator, item1_2, item2_2, item3_2, item4_2, item5_2, item6_2, item7_2, item8_2, key_resp_3],
        )
        test.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        test_indicator.setPos(loc1)
        item1_2.setFillColor(testcolor)
        item1_2.setPos(loc1)
        item1_2.setLineColor(testcolor)
        item2_2.setFillColor(color2)
        item2_2.setPos(loc2)
        item2_2.setLineColor(color2)
        item3_2.setFillColor(color3)
        item3_2.setPos(loc3)
        item3_2.setLineColor(color3)
        item4_2.setFillColor(color4)
        item4_2.setPos(loc4)
        item4_2.setLineColor(color4)
        item5_2.setFillColor(color5)
        item5_2.setPos(loc5)
        item5_2.setLineColor(color5)
        item6_2.setFillColor(color6)
        item6_2.setPos(loc6)
        item6_2.setLineColor(color6)
        item7_2.setFillColor(color7)
        item7_2.setPos(loc7)
        item7_2.setLineColor(color7)
        item8_2.setFillColor(color8)
        item8_2.setPos(loc8)
        item8_2.setLineColor(color8)
        # create starting attributes for key_resp_3
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # store start times for test
        test.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        test.tStart = globalClock.getTime(format='float')
        test.status = STARTED
        thisExp.addData('test.started', test.tStart)
        test.maxDuration = None
        # keep track of which components have finished
        testComponents = test.components
        for thisComponent in test.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "test" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        test.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *test_indicator* updates
            
            # if test_indicator is starting this frame...
            if test_indicator.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_indicator.frameNStart = frameN  # exact frame index
                test_indicator.tStart = t  # local t and not account for scr refresh
                test_indicator.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_indicator, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_indicator.started')
                # update status
                test_indicator.status = STARTED
                test_indicator.setAutoDraw(True)
            
            # if test_indicator is active this frame...
            if test_indicator.status == STARTED:
                # update params
                pass
            
            # *item1_2* updates
            
            # if item1_2 is starting this frame...
            if item1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item1_2.frameNStart = frameN  # exact frame index
                item1_2.tStart = t  # local t and not account for scr refresh
                item1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item1_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item1_2.started')
                # update status
                item1_2.status = STARTED
                item1_2.setAutoDraw(True)
            
            # if item1_2 is active this frame...
            if item1_2.status == STARTED:
                # update params
                pass
            
            # *item2_2* updates
            
            # if item2_2 is starting this frame...
            if item2_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item2_2.frameNStart = frameN  # exact frame index
                item2_2.tStart = t  # local t and not account for scr refresh
                item2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item2_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item2_2.started')
                # update status
                item2_2.status = STARTED
                item2_2.setAutoDraw(True)
            
            # if item2_2 is active this frame...
            if item2_2.status == STARTED:
                # update params
                pass
            
            # *item3_2* updates
            
            # if item3_2 is starting this frame...
            if item3_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item3_2.frameNStart = frameN  # exact frame index
                item3_2.tStart = t  # local t and not account for scr refresh
                item3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item3_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item3_2.started')
                # update status
                item3_2.status = STARTED
                item3_2.setAutoDraw(True)
            
            # if item3_2 is active this frame...
            if item3_2.status == STARTED:
                # update params
                pass
            
            # *item4_2* updates
            
            # if item4_2 is starting this frame...
            if item4_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item4_2.frameNStart = frameN  # exact frame index
                item4_2.tStart = t  # local t and not account for scr refresh
                item4_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item4_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item4_2.started')
                # update status
                item4_2.status = STARTED
                item4_2.setAutoDraw(True)
            
            # if item4_2 is active this frame...
            if item4_2.status == STARTED:
                # update params
                pass
            
            # *item5_2* updates
            
            # if item5_2 is starting this frame...
            if item5_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item5_2.frameNStart = frameN  # exact frame index
                item5_2.tStart = t  # local t and not account for scr refresh
                item5_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item5_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item5_2.started')
                # update status
                item5_2.status = STARTED
                item5_2.setAutoDraw(True)
            
            # if item5_2 is active this frame...
            if item5_2.status == STARTED:
                # update params
                pass
            
            # *item6_2* updates
            
            # if item6_2 is starting this frame...
            if item6_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item6_2.frameNStart = frameN  # exact frame index
                item6_2.tStart = t  # local t and not account for scr refresh
                item6_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item6_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item6_2.started')
                # update status
                item6_2.status = STARTED
                item6_2.setAutoDraw(True)
            
            # if item6_2 is active this frame...
            if item6_2.status == STARTED:
                # update params
                pass
            
            # *item7_2* updates
            
            # if item7_2 is starting this frame...
            if item7_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item7_2.frameNStart = frameN  # exact frame index
                item7_2.tStart = t  # local t and not account for scr refresh
                item7_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item7_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item7_2.started')
                # update status
                item7_2.status = STARTED
                item7_2.setAutoDraw(True)
            
            # if item7_2 is active this frame...
            if item7_2.status == STARTED:
                # update params
                pass
            
            # *item8_2* updates
            
            # if item8_2 is starting this frame...
            if item8_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                item8_2.frameNStart = frameN  # exact frame index
                item8_2.tStart = t  # local t and not account for scr refresh
                item8_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item8_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item8_2.started')
                # update status
                item8_2.status = STARTED
                item8_2.setAutoDraw(True)
            
            # if item8_2 is active this frame...
            if item8_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_3* updates
            waitOnFlip = False
            
            # if key_resp_3 is starting this frame...
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                # update status
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['f', 'j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_3.keys == str(correct)) or (key_resp_3.keys == correct):
                        key_resp_3.corr = 1
                    else:
                        key_resp_3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                test.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test" ---
        for thisComponent in test.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for test
        test.tStop = globalClock.getTime(format='float')
        test.tStopRefresh = tThisFlipGlobal
        thisExp.addData('test.stopped', test.tStop)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               key_resp_3.corr = 1;  # correct non-response
            else:
               key_resp_3.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp_3.keys',key_resp_3.keys)
        trials.addData('key_resp_3.corr', key_resp_3.corr)
        if key_resp_3.keys != None:  # we had a response
            trials.addData('key_resp_3.rt', key_resp_3.rt)
            trials.addData('key_resp_3.duration', key_resp_3.duration)
        # the Routine "test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end_exp" ---
    # create an object to store info about Routine end_exp
    end_exp = data.Routine(
        name='end_exp',
        components=[end_text],
    )
    end_exp.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for end_exp
    end_exp.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end_exp.tStart = globalClock.getTime(format='float')
    end_exp.status = STARTED
    thisExp.addData('end_exp.started', end_exp.tStart)
    end_exp.maxDuration = None
    # keep track of which components have finished
    end_expComponents = end_exp.components
    for thisComponent in end_exp.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_exp" ---
    end_exp.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_text* updates
        
        # if end_text is starting this frame...
        if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_text.frameNStart = frameN  # exact frame index
            end_text.tStart = t  # local t and not account for scr refresh
            end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_text.started')
            # update status
            end_text.status = STARTED
            end_text.setAutoDraw(True)
        
        # if end_text is active this frame...
        if end_text.status == STARTED:
            # update params
            pass
        
        # if end_text is stopping this frame...
        if end_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                end_text.tStop = t  # not accounting for scr refresh
                end_text.tStopRefresh = tThisFlipGlobal  # on global time
                end_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'end_text.stopped')
                # update status
                end_text.status = FINISHED
                end_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end_exp.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_exp.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_exp" ---
    for thisComponent in end_exp.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end_exp
    end_exp.tStop = globalClock.getTime(format='float')
    end_exp.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end_exp.stopped', end_exp.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if end_exp.maxDurationReached:
        routineTimer.addTime(-end_exp.maxDuration)
    elif end_exp.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
