#####################################################################
# -*- coding: iso-8859-1 -*-                                        #
#                                                                   #
# Rock Band 2 Theme by KiD                                          #
#                                                                   #
# See credits for more information                                  #
#                                                                   #
#####################################################################

from Theme import _
from Theme import *

class CustomTheme(Theme):
  def __init__(self, path, name, iniFile = False):
    Theme.__init__(self, path, name, iniFile)
    
    self.menuRB = True
    self.menuX = .426
    self.menuY = .55
    self.main_menu_scaleVar = .505
    self.main_menu_vspacingVar = 0.037
    self.use_solo_submenu = True
    self.opt_text_xPos = .25
    self.opt_text_yPos = .19
    self.opt_text_colorVar = (1,1,1)
    self.opt_selected_colorVar = (1,.75,0)
    
    
    self.opt_bkg_size = [.5,.5,1.0,1.0]
    
    #Fret and Note Colors
    self.noteColors = [(.133,1,.133),(1,.133,.133),(1,1,.133),(.2,.2,1),(1,.6,.3),(.8,.133,.8)]
    self.spNoteColor = (1,1,1)
    self.killNoteColor = (0,0,0)
    self.use_fret_colors = False
      
    #Point of View
    self.povTargetX = 0.0
    self.povTargetY = 0.0
    self.povTargetZ = 3.7
    self.povOriginX = 0.0
    self.povOriginY = 2.9
    self.povOriginZ = -2.9
      
    #Loading phrases
    self.loadingPhrase = ["Check out the Tutorials to learn the basics and improve your technique.","Energy Phrases continue to appear once you go into Overdrive. Hit them to earn while you burn, and stay in Overdrive longer.",\
                          "If you see a series of glowing white notes, hit it perfectly to gain Energy.","Looking for a real challenge? Try singing and playing an instrument at the same time by using a mic stand!",\
                          "Play flawlessly to get a score multiplier going. The longer you hold a streak, the higher your multiplier will get.","Some musicians who would have to select \"Lefty Mode\" from the pause menu: Kurt Cobain, Jimi Hendrix, Paul McCartney, and Tony Iommi.",\
                          "Some TV and home theater setups can create a delay between what you see and what you hear. If the gameplay seems out of sync, you can adjust the A/V Delay in the settings to fix the lag.","Stuck on a song? Try it in Practice Mode.","The louder the better!",\
                          "Visit the Tutorials to learn how going into Overdrive can score you tons of points, slay the crowd, and even save your life.","Go into Overdrive to get a band-wide score multiplier going! Do it all at the same time for a really huge score bonus!",\
                          "If your bandmate fails out in the middle of a song, go into Overdrive to save them!","On a Fender Stratocaster Guitar Controller you can \"finger tap\" through solos on the high frets near the guitar body - no strumming required!",\
                          "You can buy a real guitar for pretty cheap - maybe it's time to invest.","You can hold down the fret buttons in anticipation of upcoming notes."]
    self.resultsPhrase = ["None"]
      
    #Miscellany (aka Garbage no one cares about)
    self.displayAllGreyStars = False
    self.smallMult = False
    self.oBarHScale = .97
    self.oBar3dFill = True
    self.power_up_name = "Overdrive"
      
    #Continuous star fillup!
    self.starFillupCenterX = 139
    self.starFillupCenterY = 151
    self.starFillupInRadius = 105
    self.starFillupOutRadius = 139
    self.starFillupColor = (1,.9490,.3686)
      
    #Neck choose
    self.neck_prompt_x = .1
    self.neck_prompt_y = .55
      
    #Setlist
    self.songListDisplay = 3
    self.songSelectSubmenuOffsetLines = 2
    self.songSelectSubmenuOffsetSpaces = 21
    self.songSelectSubmenuX = .195
    self.songSelectSubmenuY = .085
    self.song_listcd_cd_Xpos = .78
    self.song_listcd_cd_Ypos = .615
    self.song_listcd_score_Xpos = .6
    self.song_listcd_score_Ypos = .515
    self.song_listcd_list_Xpos = .1
    
    self.songlistcd_score_colorVar = (0,0,0)
    self.career_title_colorVar = (1,1,1)
    self.song_name_text_colorVar = (.9804,.9804,.9804)
    self.song_name_selected_colorVar = (0,0,0)
    self.artist_text_colorVar = (.6471,.6471,.6471)
    self.artist_selected_colorVar = (.25,.50,1)
    self.library_text_colorVar = (1,1,1)
    self.library_selected_colorVar = (0,0,0)
    self.pause_text_colorVar = (1,1,1)
    self.pause_selected_colorVar = (1,.75,0)
    self.fail_completed_colorVar = (1,1,1)
    self.fail_text_colorVar = (1,1,1)
    self.fail_selected_colorVar = (1,.75,0)
    self.song_rb2_diff_colorVar = (0,0,0)
    
    #pause menu and fail menu
    self.pause_text_xPos = .37
    self.pause_text_yPos = .275
    self.fail_text_xPos = .53
    self.fail_text_yPos = .45
    self.fail_songname_xPos = .5
    self.fail_songname_yPos = .365
    
    self.loadingX = .5
    self.loadingY = .35
    self.loadingColor = (1,1,1)
    self.loadingFScale = .0015
    self.loadingRMargin = 1.0
    self.loadingLSpacing = 1.0
    self.sub_menu_xVar = .25
    self.sub_menu_yVar = .19
    self.menuTipTextY = .7
    self.menuTipTextFont = "loadingFont"
    self.menuTipTextScale = .002
    self.menuTipTextColor = (1,1,1)
    self.menuTipTextScrollSpace = .25
    self.menuTipTextScrollMode = 0
    self.menuTipTextDisplay = True
    
    #Lobby
    self.controlActivateX = .645
    self.controlActivateSelectX = .5
    self.controlActivatePartX = .41
    self.controlActivateY = .18
    self.controlActivateScale = .0018
    self.controlActivateSpace = .045
    self.controlActivatePartSize = 22.000
    self.controlActivateFont = "loadingFont"
    self.controlDescriptionX = .5
    self.controlDescriptionY = .617
    self.controlDescriptionScale = .002
    self.controlDescriptionFont = "font"
    self.controlCheckX = .16
    self.controlCheckY = .26
    self.controlCheckTextY = .61
    self.controlCheckPartMult = 2.8
    self.controlCheckScale = .0018
    self.controlCheckSpace = .23
    self.controlCheckFont  = "loadingFont"
    self.lobbyPreviewX = .7
    self.lobbyPreviewY = 0.0
    self.lobbyPreviewSpacing = .04
    self.lobbyTitleX = .4
    self.lobbyTitleY = .06
    self.lobbyTitleCharacterX = .26
    self.lobbyTitleCharacterY = .24
    self.lobbyTitleScale = .0024
    self.lobbyTitleFont = "font"
    self.lobbySelectX = .4
    self.lobbySelectY = .32
    self.lobbySelectImageX = .255
    self.lobbySelectImageY = .335
    self.lobbySelectScale = .0018
    self.lobbySelectSpace = .04
    self.lobbySelectFont = "loadingFont"
    self.lobbySelectLength = 5
    self.lobbyTitleColor = (1,1,1)
    self.lobbyInfoColor = (1,1,1)
    self.lobbyFontColor = (1,1,1)
    self.lobbyPlayerColor = (1,1,1)
    self.lobbySelectColor = (1,.75,0)
    self.lobbyDisableColor = (.4,.4,.4)
    self.characterCreateX = .25
    self.characterCreateY = .15
    self.characterCreateOptionX = .75
    self.characterCreateFontColor = (1,1,1)
    self.characterCreateSelectColor = (1,.75,0)
    self.characterCreateHelpColor = (1,1,1)
    self.characterCreateHelpX = .5
    self.characterCreateHelpY = .5
    self.characterCreateHelpScale = .5
    self.characterCreateOptionFont = "font"
    self.characterCreateHelpFont = "loadingFont"
    self.characterCreateScale = .0018
    self.characterCreateSpace = .045
    self.avatarSelectTextX = .44
    self.avatarSelectTextY = .16
    self.avatarSelectTextScale = .0027
    self.avatarSelectFont = "font"
    self.avatarSelectAvX = .75
    self.avatarSelectAvY = .35
    self.avatarSelectWheelY = 0.0
    
    #3D Note/Fret rendering system
    self.twoDnote = True
    self.twoDkeys = True
    self.threeDspin = False
    self.fret_press = False
    self.noterot = [-6, -3, 0, 3, 6]
    self.keyrot  = [6, 3, 0, -3, -6]
    self.drumnoterot = [5, -5, -2, 2, 0]
    self.drumkeyrot = [6, 2, -2, -6, 0]
    self.notepos = [-.05, -.01, 0, -.01, -.05]
    self.keypos  = [.05, .01, 0, .01, .05]
    self.drumnotepos = [-.05, -.05, 0, 0, 0]
    self.drumkeypos = [.05, 0, 0, .05, 0]
    
    #Game results scene
    self.result_score = [.425,.144,.00085,None,None]
    self.result_star = [.71,.755,.075,1.0]
    self.result_song = [.5,.045,.0047,None,None]
    self.result_song_form = 3
    self.result_song_text = "%s"
    self.result_stats_part = [.455,.47,0.3,None,None]
    self.result_stats_part_text = "$icon$"
    self.result_stats_name = [.5,.3,0.002,None,None]
    self.result_stats_diff = [.565,.352,.002,None,None]
    self.result_stats_diff_text = "%s"
    self.result_stats_accuracy = [.565,.416,.002,(.7725,.7765,.0235),None]
    self.result_stats_accuracy_text = "%.1f%%"
    self.result_stats_streak = [.5,.448,.002,(.7725,.7765,.0235),None]
    self.result_stats_streak_text = "%d NOTE STREAK"
    self.result_stats_notes = [.565,.352,.002,None,None]
    self.result_stats_notes_text = "%s"
    self.result_cheats_info = [.5,.57,.002]
    self.result_cheats_numbers = [.44,.61,.002]
    self.result_cheats_percent = [.5,.65,.002]
    self.result_cheats_score   = [.43,.7,.002]
    self.result_cheats_color   = (1,1,1)
    self.result_cheats_font    = "font"
    self.result_high_score_font = "font"
    self.result_menu_x         = .1
    self.result_menu_y         = .565
    self.result_star_type      = 0
    
    #Submenus
    self.submenuX = {}
    self.submenuX['solotext2'] = .517
    self.submenuX['multiplayertext6'] = .415
    self.submenuX['settingstext9'] = .493
    self.submenuX['advsettingstext10'] = .493
    self.submenuX['failtext3'] = .65
    self.submenuX['careerfailtext4'] = .65
    self.submenuY = {}
    self.submenuY['solotext2'] = .53
    self.submenuY['multiplayertext6'] = .54
    self.submenuY['settingstext9'] = .75
    self.submenuY['advsettingstext10'] = .75
    self.submenuY['failtext3'] = .45
    self.submenuY['careerfailtext4'] = .45
    self.submenuScale = {}
    self.submenuScale['solotext2'] = .6
    self.submenuScale['multiplayertext6'] = .85
    self.submenuScale['settingstext9'] = .5
    self.submenuScale['advsettingstext10'] = .5
    self.submenuScale['failtext3'] = .45
    self.submenuScale['careerfailtext4'] = .45
    self.submenuVSpace = {}
    self.submenuVSpace['solotext2'] = .079
    self.submenuVSpace['multiplayertext6'] = .045
    self.submenuVSpace['settingstext9'] = .07
    self.submenuVSpace['advsettingstext10'] = .07
    self.submenuVSpace['failtext3'] = .065
    self.submenuVSpace['careerfailtext4'] = .065
    self.setlist = self.loadThemeModule("CustomSetlist")
