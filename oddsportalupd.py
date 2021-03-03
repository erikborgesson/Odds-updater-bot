#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' erik.borgesson@hotmail.com '''

from selenium import webdriver
import pandas as pd
import time
from telegrambot import telegram_bot_sendtext

driver = webdriver.Chrome("Path to your chromedriver)
driver.get('https://www.oddsportal.com/tennis/netherlands/atp-rotterdam/')

latestgames = []

elem = driver.find_element_by_xpath('//*[@id="tournamentTable"]').get_attribute('outerHTML')   
 
odds = pd.read_html(elem) 
odds = odds[0].dropna()

latestgamestr = odds.iloc[-1][-6]

if '});' in latestgamestr:
        skit, players = latestgamestr.split('});')
        latestgames.append(players)
else:
        latestgames.append(latestgamestr)

while True:
    
    elemo = driver.find_element_by_xpath('//*[@id="tournamentTable"]').get_attribute('outerHTML')  
    
    odds = pd.read_html(elem) 
    odds = odds[0].dropna()
    
    latestgamestr = odds.iloc[-1][-6]
 
  
    if '});' in latestgamestr:
        skit, player = latestgamestr.split('});')
        latestgames.append(players)
       
        if latestgames[-1] != latestgames[-2]:
            telegram_bot_sendtext('New game on OddsPortal: \n' + players + '\nOdds: ' + str(odds.iloc[-1][-3]) + ' - ' + str(odds.iloc[-1][-2]) + '\nLeague')
    
        driver.refresh()
        time.sleep(5)
    
    else:
        latestgames.append(latestgamestr)
    
        if latestgames[-1] != latestgames[-2]:
            telegram_bot_sendtext('New game on OddsPortal: \n' + latestgamestr + '\nOdds: ' + str(odds.iloc[-1][-3]) + ' - ' + str(odds.iloc[-1][-2]) + '\nLeague')
        
        driver.refresh()
        time.sleep(5)
    