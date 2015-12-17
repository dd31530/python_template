#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
+----------------------------------------------------------------------------+
| pathUtils:  toolbox for pathname manipulation                              |
+---------+----------+----------+--------------------------------------------+
| version | datecode | author   | history                                    |
+---------+----------+----------+--------------------------------------------+
| 1.0     | 121116   | DD       | creation                                   |
| 1.1     | 121205   | DD       | replace unique default argument            |
|         |          |          | (filename='') by tuple (*args)             |
|         |          |          | in currentPath class methods               |
| 1.2     | 151215   | DD       | messagesUtils usage                        |
+---------+----------+----------+--------------------------------------------+
'''

VERSION = 'v1.1_121205'

##############################################################################
# external modules
##############################################################################


import os
import sys


##############################################################################
# local modules
##############################################################################


from messagesUtils import header, banner, footer


##############################################################################
# classes
##############################################################################

class currentPath:
   '''provide methods for getting project absolute pathnames.'''
   def __init__(self):
      self._bin = sys.path[0]
      self._cfg = self._bin.replace('bin', 'cfg')
      self._inp = self._bin.replace('bin', 'input')
      self._out = self._bin.replace('bin', 'output')
      self._tmp = self._bin.replace('bin', 'tmp')
      self._log = self._bin.replace('bin', 'log')

   def bin(self, *args):
      '''returns current project 'bin' absolute path.'''
      return os.path.join(self._bin, *args)
      
   def cfg(self, *args):
      '''returns current project 'cfg' absolute path.'''
      return os.path.join(self._cfg, *args)
      
   def inp(self, *args):
      '''returns current project 'input' absolute path.'''
      return os.path.join(self._inp, *args)
      
   def out(self, *args):
      '''returns current project 'output' absolute path.'''
      return os.path.join(self._out, *args)
      
   def tmp(self, *args):
      '''returns current project 'tmp' absolute path.'''
      return os.path.join(self._tmp, *args)
      
   def log(self, *args):
      '''returns current project 'log' absolute path.'''
      return os.path.join(self._log, *args)
      
   def isFile(self, filepath):
      '''returns true if file exists.'''
      if os.path.isfile(filepath):
         return True
      else:
         return False
      
   def isDir(self, dirpath):
      '''returns true if dir exists.'''
      if os.path.isdir(dirpath):
         return True
      else:
         return False
      

##############################################################################
# main
##############################################################################

if  __name__ == '__main__':
   from logUtils import Logger
   header()
   banner("Autotest...")
   cwd = currentPath()
   config_file = cwd.cfg('log.conf')
   if cwd.isFile(config_file):
      Logger.logr.info("le fichier %s existe!" % config_file)
   else:
      Logger.logr.warning("le fichier %s n'existe pas!" % config_file)
   if cwd.isDir(cwd.inp()):
      Logger.logr.info("le repertoire %s existe!" % cwd.inp())
   else:
      Logger.logr.warning("le repertoire %s n'existe pas!" % cwd.inp())
   output_file = cwd.out('result')
   if not cwd.isFile(output_file):
      Logger.logr.warning("le fichier %s n'existe pas!" % output_file)
   footer()


##############################################################################
# eof
##############################################################################
