# -*- coding: UTF-8 -*-
import os
import os.path
import logging
import logging.config
import io
import sys
import configparser
import time
import specvideoproject_converter
import shutil
import urllib.request
import os, os.path

global log
global myname




def download_urllib():
    filePrice = u'specvideoproject.xlsx'  
    urlPrice  =  'http://bosch-congress-system.ru/files/Price_bosch_all.xlsx'

    sss = urllib.request.urlopen(urlPrice).read()       #Скачиваем сначала страницу
    print(len(sss))

    if os.path.exists(filePrice):
        os.remove(filePrice)
    f = open(filePrice, 'wb')                    #Теперь записываем файл
    f.write(sss)
    f.close()
        
    if os.path.exists('new_'+filePrice):
        if os.path.exists('old_'+filePrice):
           os.remove('old_'+filePrice)
        os.rename('new_'+filePrice, 'old_'+filePrice)
    os.rename(filePrice, 'new_'+filePrice)



def make_loger():
    global log
    logging.config.fileConfig('logging.cfg')
    log = logging.getLogger('logFile')



def main( ):
    global  myname
    global  mydir
   
    make_loger()
    log.info('------------  '+myname +'  ------------')

    download_urllib()
#    if  specvideoproect_downloader.download( myname ) :
    specvideoproject_converter.convert2csv( myname )
    shutil.copy2( myname + '.csv', 'c://AV_PROM/prices/' + myname +'/'+ myname + '.csv')
    shutil.copy2( 'python.log',    'c://AV_PROM/prices/' + myname +'/python.log')

if __name__ == '__main__':
    global  myname
    global  mydir
    myname   = os.path.basename(os.path.splitext(sys.argv[0])[0])
    mydir    = os.path.dirname (sys.argv[0])
    if ('' != mydir) : os.chdir(mydir)
    main( )
 
#os.system(r'c:\prices\_scripts\remove_tmp_profiles.cmd')