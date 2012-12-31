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

class CustomSetlist(Setlist):
  def __init__(self, theme):
    self.theme = theme
    self.setlist_type = 3
    self.setlistStyle = 0
    self.headerSkip = 0
    self.footerSkip = 0
    self.labelType = 0
    self.labelDistance = 1
    self.showMoreLabels = False
    self.texturedLabels = False
    self.itemsPerPage = 12
    self.showLockedSongs = True
    self.showSortTiers = True
    self.selectTiers = False
    self.itemSize = (0,.07)

    self.career_title_color = self.theme.career_title_colorVar
    self.song_name_text_color = self.theme.song_name_text_colorVar
    self.song_name_selected_color = self.theme.song_name_selected_colorVar
    self.song_rb2_diff_color = self.theme.song_rb2_diff_colorVar
    self.artist_text_color = self.theme.artist_text_colorVar
    self.artist_selected_color = self.theme.artist_selected_colorVar
    self.library_text_color = self.theme.library_text_colorVar
    self.library_selected_color = self.theme.library_selected_colorVar
    self.songlist_score_color = self.theme.songlist_score_colorVar
    self.songlistcd_score_color = self.theme.songlistcd_score_colorVar

    self.song_cd_xpos = theme.song_cd_Xpos
    self.song_cdscore_xpos = theme.song_cdscore_Xpos
    self.song_list_xpos = theme.song_list_Xpos
    self.song_listscore_xpos = theme.song_listscore_Xpos
    self.song_listcd_list_xpos = theme.song_listcd_list_Xpos
    self.song_listcd_cd_xpos = theme.song_listcd_cd_Xpos
    self.song_listcd_cd_ypos = theme.song_listcd_cd_Ypos
    self.song_listcd_score_xpos = theme.song_listcd_score_Xpos
    self.song_listcd_score_ypos = theme.song_listcd_score_Ypos
  
  def renderUnselectedItem(self, scene, i, n):
    w, h = scene.engine.view.geometry[2:4]
    font = scene.engine.data.songListFont
    lfont = scene.engine.data.songListFont
    sfont = scene.engine.data.shadowfont
    font = scene.engine.data.songListFont
    if not scene.items or scene.itemIcons is None:
      return
    item = scene.items[i]
    y = h*(.7825-(.0459*(n+1)))
    
    if scene.img_tier:
      imgwidth = scene.img_tier.width1()
      imgheight = scene.img_tier.height1()
      wfactor = 381.1/imgwidth
      hfactor = 24.000/imgheight
      if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo) and scene.img_tier:
        scene.engine.drawImage(scene.img_tier, scale = (wfactor,-hfactor), coord = (w/1.587, h-((0.055*h)*(n+1))-(0.219*h)))

    icon = None
    if isinstance(item, Song.SongInfo):
      if item.icon != "":
        try:
          icon = scene.itemIcons[item.icon]
          imgwidth = icon.width1()
          wfactor = 23.000/imgwidth
          scene.engine.drawImage(icon, scale = (wfactor,-wfactor), coord = (w/2.86, h-((0.055*(n+1))-(0.219*h))))
        except KeyError:
          pass
    elif isinstance(item, Song.LibraryInfo):
      try:
        icon = scene.itemIcons["Library"]
        imgwidth = icon.width1()
        wfactor = 23.000/imgwidth
        scene.engine.drawImage(icon, scale = (wfactor,-wfactor), coord = (w/2.86, h-((0.055*(n+1))-(0.219*h))))
      except KeyError:
        pass
    elif isinstance(item, Song.RandomSongInfo):
      try:
        icon = scene.itemIcons["Random"]
        imgwidth = icon.width1()
        wfactor = 23.000/imgwidth
        scene.engine.drawImage(icon, scale = (wfactor,-wfactor), coord = (w/2.86, h-((0.055*(n+1))-(0.219*h))))
      except KeyError:
        pass
    
    if isinstance(item, Song.SongInfo) or isinstance(item, Song.LibraryInfo):
      c1,c2,c3 = self.song_name_text_color
      glColor4f(c1,c2,c3,1)
    elif isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
      c1,c2,c3 = self.career_title_color
      glColor4f(c1,c2,c3,1)
    elif isinstance(item, Song.RandomSongInfo):
      c1,c2,c3 = self.song_name_text_color
      glColor4f(c1,c2,c3,1)
    
    text = item.name
    
    
    if isinstance(item, Song.SongInfo) and item.getLocked():
      text = _("-- Locked --")
      
    if isinstance(item, Song.SongInfo): #MFH - add indentation when tier sorting
      if scene.tiersPresent or icon:
        text = "   " + text
      

    # evilynux - Force uppercase display for Career titles
    maxwidth = .55
      
    if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
      text = string.upper(text)
      
    scale = .0015
    wt, ht = font.getStringSize(text, scale = scale)

    while wt > maxwidth:
      tlength = len(text) - 4
      text = text[:tlength] + "..."
      wt, ht = font.getStringSize(text, scale = scale)
      if wt < .45:
        break
      
      
    font.render(text, (.35, .0413*(n+1)+.15), scale = scale)

    if isinstance(item, Song.SongInfo):
      if not item.getLocked():
        try:
          difficulties = item.partDifficulties[scene.scorePart.id]
        except KeyError:
          difficulties = []
        for d in difficulties:
          if d.id == scene.scoreDifficulty.id:
            scores = item.getHighscores(d, part = scene.scorePart)
            if scores:
              score, stars, name, scoreExt = scores[0]
              try:
                notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
              except ValueError:
                notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                handicap = 0
                handicapLong = "None"
                originalScore = score
              break
            else:
              score, stars, name = 0, 0, "---"
        else:
          score, stars, name = _("Nil"), 0, "---"
        
        if score == _("Nil") and scene.nilShowNextScore:   #MFH
          for d in difficulties:   #MFH - just take the first valid difficulty you can find and display it.
            scores = item.getHighscores(d, part = scene.scorePart)
            if scores:
              score, stars, name, scoreExt = scores[0]
              try:
                notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
              except ValueError:
                notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                handicap = 0
                handicapLong = "None"
                originalScore = score
              break
            else:
              score, stars, name = 0, 0, "---"
        else:
          score, stars, name = _("Nil"), 0, "---"

        #evilynux - hit% and note streak if enabled
        scale = 0.0009
        if score is not _("Nil") and score > 0 and notesTotal != 0:
          text = "%.1f%% (%d)" % ((float(notesHit) / notesTotal) * 100.0, noteStreak)
          font.render(text, (.92, .0413*(n+1)+.163), scale=scale, align = 2)
              
        text = str(score)
        
        font.render(text, (.92, .0413*(n+1)+.15), scale=scale, align = 2)

  def renderSelectedItem(self, scene, n):
    w, h = scene.engine.view.geometry[2:4]
    font = scene.engine.data.songListFont
    lfont = scene.engine.data.songListFont
    sfont = scene.engine.data.shadowfont
    item = scene.selectedItem
    if not item:
      return
    if isinstance(item, Song.BlankSpaceInfo):
      return
    y = h*(.7825-(.0459*(n)))
    
    if scene.img_tier:
      imgwidth = scene.img_tier.width1()
      imgheight = scene.img_tier.height1()
      wfactor = 381.1/imgwidth
      hfactor = 24.000/imgheight
      if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
        scene.engine.drawImage(scene.img_tier, scale = (wfactor,-hfactor), coord = (w/1.587, h-((0.055*h)*(n+1))-(0.219*h)))
    
    if scene.img_selected:
      imgwidth = scene.img_selected.width1()
      imgheight = scene.img_selected.height1()
      wfactor = 381.5/imgwidth
      hfactor = 36.000/imgheight

      scene.engine.drawImage(scene.img_selected, scale = (wfactor,-hfactor), coord = (w/1.587, y*1.2-h*.213))
    
    
    icon = None
    if isinstance(item, Song.SongInfo):
      if item.icon != "":
        try:
          icon = scene.itemIcons[item.icon]
          imgwidth = icon.width1()
          wfactor = 23.000/imgwidth
          scene.engine.drawImage(icon, scale = (wfactor,-wfactor), coord = (w/2.86, h-((0.055*(n+1))-(0.219*h))))
        except KeyError:
          pass
      
      c1,c2,c3 = self.song_name_selected_color
      glColor3f(c1,c2,c3)
      if item.getLocked():
        text = item.getUnlockText()
      elif scene.careerMode and not item.completed:
        text = _("Play To Advance")
      elif scene.practiceMode:
        text = _("Practice")
      elif item.count:
        count = int(item.count)
        if count == 1: 
          text = _("Played Once")
        else:
          text = _("Played %d times.") % count
      else:
        text = _("Quickplay")
    elif isinstance(item, Song.LibraryInfo):
      try:
        icon = scene.itemIcons["Library"]
        imgwidth = icon.width1()
        wfactor = 23.000/imgwidth
        scene.engine.drawImage(icon, scale = (wfactor,-wfactor), coord = (w/2.86, h-((0.055*(n+1))-(0.219*h))))
      except KeyError:
        pass
      c1,c2,c3 = self.library_selected_color
      glColor3f(c1,c2,c3)
      if item.songCount == 1:
        text = _("There Is 1 Song In This Setlist.")
      elif item.songCount > 1:
        text = _("There Are %d Songs In This Setlist.") % (item.songCount)
      else:
        text = ""
    elif isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
      text = _("Tier")
      c1,c2,c3 = self.career_title_color
      glColor3f(c1,c2,c3)
    elif isinstance(item, Song.RandomSongInfo):
      try:
        icon = scene.itemIcons["Random"]
        imgwidth = icon.width1()
        wfactor = 23.000/imgwidth
        scene.engine.drawImage(icon, scale = (wfactor,-wfactor), coord = (w/2.86, h-((0.055*(n+1))-(0.219*h))))
      except KeyError:
        pass
      text = _("Random Song")
      c1,c2,c3 = self.career_title_color
      glColor3f(c1,c2,c3)
    
    font.render(text, (0.92, .13), scale = 0.0012, align = 2)
    
    maxwidth = .45
    if isinstance(item, Song.SongInfo) or isinstance(item, Song.LibraryInfo) or isinstance(item, Song.RandomSongInfo):
      c1,c2,c3 = self.song_name_selected_color
      glColor4f(c1,c2,c3,1)
    if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
      c1,c2,c3 = self.career_title_color
      glColor4f(c1,c2,c3,1)
    
    text = item.name
    
    if isinstance(item, Song.SongInfo) and item.getLocked():
      text = _("-- Locked --")
      
    if isinstance(item, Song.SongInfo): #MFH - add indentation when tier sorting
      if scene.tiersPresent or icon:
        text = "   " + text
      

    # evilynux - Force uppercase display for Career titles
    if isinstance(item, Song.TitleInfo) or isinstance(item, Song.SortTitleInfo):
      maxwidth = .55
      text = string.upper(text)
      
    scale = .0015
    wt, ht = font.getStringSize(text, scale = scale)

    while wt > maxwidth:
      tlength = len(text) - 4
      text = text[:tlength] + "..."
      wt, ht = font.getStringSize(text, scale = scale)
      if wt < .45:
        break
      
      
    font.render(text, (.35, .0413*(n+1)+.15), scale = scale) #add theme option for song_listCD_xpos

    if isinstance(item, Song.SongInfo):
      if not item.getLocked():
        try:
          difficulties = item.partDifficulties[scene.scorePart.id]
        except KeyError:
          difficulties = []
        for d in difficulties:
          if d.id == scene.scoreDifficulty.id:
            scores = item.getHighscores(d, part = scene.scorePart)
            if scores:
              score, stars, name, scoreExt = scores[0]
              try:
                notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
              except ValueError:
                notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                handicap = 0
                handicapLong = "None"
                originalScore = score
              break
            else:
              score, stars, name = 0, 0, "---"
        else:
          score, stars, name = _("Nil"), 0, "---"
        if score == _("Nil") and scene.nilShowNextScore:   #MFH
          for d in difficulties:   #MFH - just take the first valid difficulty you can find and display it.
            scores = item.getHighscores(d, part = scene.scorePart)
            if scores:
              score, stars, name, scoreExt = scores[0]
              try:
                notesHit, notesTotal, noteStreak, modVersion, handicap, handicapLong, originalScore = scoreExt
              except ValueError:
                notesHit, notesTotal, noteStreak, modVersion, oldScores1, oldScores2 = scoreExt
                handicap = 0
                handicapLong = "None"
                originalScore = score
              break
            else:
              score, stars, name = 0, 0, "---"
          else:
            score, stars, name = _("Nil"), 0, "---"

        scale = 0.0009
        if score is not _("Nil") and score > 0 and notesTotal != 0:
          text = "%.1f%% (%d)" % ((float(notesHit) / notesTotal) * 100.0, noteStreak)
          w, h = font.getStringSize(text, scale=scale)
          font.render(text, (.92, .0413*(n+1)+.163), scale=scale, align = 2)
        
        text = str(score)
        
        font.render(text, (.92, .0413*(n+1)+.15), scale=scale, align = 2)

  def renderAlbumArt(self, scene):
    if not scene.itemLabels:
      return
    w, h = scene.engine.view.geometry[2:4]
    item  = scene.items[scene.selectedIndex]
    i = scene.selectedIndex
    img = None
    lockImg = None
    if scene.itemLabels[i] == "Random":
      if scene.img_random_label:
        img = scene.img_random_label
        imgwidth = img.width1()
        wfactor = 155.000/imgwidth
      elif scene.img_empty_label:
        img = scene.img_empty_label
        imgwidth = img.width1()
        wfactor = 155.000/imgwidth
    elif not scene.itemLabels[i]:
      if scene.img_empty_label != None:
        imgwidth = scene.img_empty_label.width1()
        wfactor = 155.000/imgwidth
        img = scene.img_empty_label
    elif scene.itemLabels[i]:
      img = scene.itemLabels[i]
      imgwidth = img.width1()
      wfactor = 155.000/imgwidth
    if isinstance(item, Song.SongInfo) and item.getLocked():
      if scene.img_locked_label:
        imgwidth = scene.img_locked_label.width1()
        wfactor2 = 155.000/imgwidth
        lockImg = scene.img_locked_label
      elif scene.img_empty_label:
        imgwidth = scene.img_empty_label.width1()
        wfactor = 155.000/imgwidth
        img = scene.img_empty_label
    if img:
      scene.engine.drawImage(img, scale = (wfactor,-wfactor), coord = (.21*w,.59*h))
    if lockImg:
      scene.engine.drawImage(lockImg, scale = (wfactor2,-wfactor2), coord = (.21*w,.59*h))

  def renderForeground(self, scene):
    font = scene.engine.data.songListFont
    w, h = scene.engine.view.geometry[2:4]

    c1,c2,c3 = self.song_rb2_diff_color
    glColor3f(c1,c2,c3)
    
    font.render(_("DIFFICULTY"), (.095, .5325), scale = 0.0018)
    scale = 0.0014
    text = _("BAND")
    font.render(text, (.17, .5585), scale = scale, align = 2)
    text = _("GUITAR")
    font.render(text, (.17, .5835), scale = scale, align = 2)
    text = _("DRUM")
    font.render(text, (.17, .6085), scale = scale, align = 2)
    text = _("BASS")
    font.render(text, (.17, .6335), scale = scale, align = 2)
    text = _("VOCALS")
    font.render(text, (.17, .6585), scale = scale, align = 2)

    #Add support for lead and rhythm diff

    #Qstick - Sorting Text
    text = _("SORTING:") + "     "
    if scene.sortOrder == 0: #title
      text = text + _("ALPHABETICALLY BY TITLE")
    elif scene.sortOrder == 1: #artist
      text = text + _("ALPHABETICALLY BY ARTIST")
    elif scene.sortOrder == 2: #timesplayed
      text = text + _("BY PLAY COUNT")
    elif scene.sortOrder == 3: #album
      text = text + _("ALPHABETICALLY BY ALBUM")
    elif scene.sortOrder == 4: #genre
      text = text + _("ALPHABETICALLY BY GENRE")
    elif scene.sortOrder == 5: #year
      text = text + _("BY YEAR")
    elif scene.sortOrder == 6: #Band Difficulty
      text = text + _("BY BAND DIFFICULTY")
    elif scene.sortOrder == 7: #Band Difficulty
      text = text + _("BY INSTRUMENT DIFFICULTY")
    else:
      text = text + _("BY SONG COLLECTION")
      
    font.render(text, (.13, .152), scale = 0.0017)

    if scene.searchText:
      text = _("Filter: %s") % (scene.searchText) + "|"
      if not scene.matchesSearch(scene.items[scene.selectedIndex]):
        text += " (%s)" % _("Not found")
      font.render(text, (.05, .7), scale = 0.001)
    elif scene.songLoader:
      font.render(_("Loading Preview..."), (.05, .7), scale = 0.001)
    return
    if scene.img_list_button_guide:
      scene.engine.drawImage(scene.img_list_button_guide, scale = (.5, -.5), coord = (w*.5,0), fit = 2)
    if scene.songLoader:
      font.render(_("Loading Preview..."), (.5, .7), align = 1)
    if scene.img_list_fg:
      scene.engine.drawImage(scene.img_list_fg, scale = (1.0, -1.0), coord = (w/2,h/2), stretched = 3)
  
  def renderSelectedInfo(self, scene):
    w, h = scene.engine.view.geometry[2:4]
    font = scene.engine.data.songListFont
    item = scene.selectedItem
    if isinstance(item, Song.SongInfo):
      text = item.artist
      if (item.getLocked()):
        text = "" # avoid giving away artist of locked song

      scale = 0.0015
      wt, ht = font.getStringSize(text, scale=scale)
      
      while wt > .21:
        tlength = len(text) - 4
        text = text[:tlength] + "..."
        wt, ht = font.getStringSize(text, scale = scale)
        if wt < .22:
          break
        
      c1,c2,c3 = self.artist_text_color
      glColor3f(c1,c2,c3)
      
      text = string.upper(text)
      font.render(text, (.095, .432), scale = scale)
      
      if scene.img_diff3 != None:
        imgwidth = scene.img_diff3.width1()
        imgheight = scene.img_diff3.height1()
        wfactor1 = 13.0/imgwidth
      
      albumtag = item.album
      albumtag = string.upper(albumtag)
      wt, ht = font.getStringSize(albumtag, scale=scale)
      
      while wt > .21:
        tlength = len(albumtag) - 4
        albumtag = albumtag[:tlength] + "..."
        wt, ht = font.getStringSize(albumtag, scale = scale)
        if wt < .22:
          break                    

      font.render(albumtag, (.095, .465), scale = 0.0015)
      
      genretag = item.genre
      font.render(genretag, (.095, .485), scale = 0.0015)                                

      yeartag = item.year           
      font.render(yeartag, (.095, .505), scale = 0.0015)

   
      for i in range(5):
        glColor3f(1, 1, 1) 
        if i == 0:
          diff = item.diffSong
        elif i == 1:
          diff = item.diffGuitar
        elif i == 2:
          diff = item.diffDrums
        elif i == 3:
          diff = item.diffBass
        elif i == 4:
          diff = item.diffVocals
        if scene.img_diff1 == None or scene.img_diff2 == None or scene.img_diff3 == None:
          if diff == -1:
            font.render("N/A", (.18, .5585 + i*.025), scale = 0.0014)
          elif diff == 6:
            glColor3f(1, 1, 0)  
            font.render(str("*" * (diff -1)), (.18, 0.5685 + i*.025), scale = 0.003)
          else:
            font.render(str("*" * diff + " " * (5 - diff)), (.18, 0.5685 + i*.025), scale = 0.003)
        else:
          if diff == -1:
            font.render("N/A", (.18, .5585 + i*.025), scale = 0.0014)
          elif diff == 6:
            for k in range(0,5):
              scene.engine.drawImage(scene.img_diff3, scale = (wfactor1,-wfactor1), coord = ((.19+.03*k)*w, (0.2354-.0333*i)*h))
          else:
            for k in range(0,diff):
              scene.engine.drawImage(scene.img_diff2, scale = (wfactor1,-wfactor1), coord = ((.19+.03*k)*w, (0.2354-.0333*i)*h))
            for k in range(0, 5-diff):
              scene.engine.drawImage(scene.img_diff1, scale = (wfactor1,-wfactor1), coord = ((.31-.03*k)*w, (0.2354-.0333*i)*h))

  def renderMoreInfo(self, scene):
    if not scene.items:
      return
    if not scene.selectedItem:
      return
    item = scene.selectedItem
    i = scene.selectedIndex
    y = 0
    w, h = scene.engine.view.geometry[2:4]
    font = scene.engine.data.songListFont
    self.theme.fadeScreen(0.25)
    if scene.moreInfoTime < 500:
      y = 1.0-(float(scene.moreInfoTime)/500.0)
    yI = y*h
    if scene.img_panel:
      scene.engine.drawImage(scene.img_panel, scale = (1.0, -1.0), coord = (w*.5,h*.5+yI), stretched = 3)
    if scene.img_tabs:
      r0 = (0, (1.0/3.0), 0, .5)
      r1 = ((1.0/3.0),(2.0/3.0), 0, .5)
      r2 = ((2.0/3.0),1.0,0,.5)
      if scene.infoPage == 0:
        r0 = (0, (1.0/3.0), .5, 1.0)
        scene.engine.drawImage(scene.img_tab1, scale = (.5, -.5), coord = (w*.5,h*.5+yI))
        text = item.name
        if item.artist != "":
          text += " by %s" % item.artist
        if item.year != "":
          text += " (%s)" % item.year
        scale = font.scaleText(text, .45, .0015)
        font.render(text, (.52, .25-y), scale = scale, align = 1)
        if scene.itemLabels[i]:
          imgwidth = scene.itemLabels[i].width1()
          wfactor = 95.000/imgwidth
          scene.engine.drawImage(scene.itemLabels[i], (wfactor, -wfactor), (w*.375,h*.5+yI))
        elif scene.img_empty_label:
          imgwidth = scene.img_empty_label.width1()
          wfactor = 95.000/imgwidth
          scene.engine.drawImage(scene.img_empty_label, (wfactor, -wfactor), (w*.375,h*.5+yI))
        text = item.album
        if text == "":
          text = _("No Album")
        scale = font.scaleText(text, .2, .0015)
        font.render(text, (.56, .305-y), scale = scale)
        text = item.genre
        if text == "":
          text = _("No Genre")
        scale = font.scaleText(text, .2, .0015)
        font.render(text, (.56, .35-y), scale = scale)
      elif scene.infoPage == 1:
        r1 = ((1.0/3.0),(2.0/3.0), .5, 1.0)
        scene.engine.drawImage(scene.img_tab2, scale = (.5, -.5), coord = (w*.5,h*.5+yI))
      elif scene.infoPage == 2:
        r2 = ((2.0/3.0),1.0, .5, 1.0)
        scene.engine.drawImage(scene.img_tab3, scale = (.5, -.5), coord = (w*.5,h*.5+yI))
      scene.engine.drawImage(scene.img_tabs, scale = (.5*(1.0/3.0), -.25), coord = (w*.36,h*.72+yI), rect = r0)
      scene.engine.drawImage(scene.img_tabs, scale = (.5*(1.0/3.0), -.25), coord = (w*.51,h*.72+yI), rect = r1)
      scene.engine.drawImage(scene.img_tabs, scale = (.5*(1.0/3.0), -.25), coord = (w*.66,h*.72+yI), rect = r2)
