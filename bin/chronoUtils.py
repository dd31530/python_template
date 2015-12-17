#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
+----------------------------------------------------------------------------+
| chronoUtils:  these are my own time count utilities                        |
+---------+----------+----------+--------------------------------------------+
| version | datecode | author   | history                                    |
+---------+----------+----------+--------------------------------------------+
| 1.0     | 121119   | DD       | creation                                   |
| 1.1     | 151215   | DD       | messagesUtils usage                        |
+---------+----------+----------+--------------------------------------------+
'''

VERSION = 'v1.1_151215'

##############################################################################
# external modules
##############################################################################


import time as t


##############################################################################
# local modules
##############################################################################


from messagesUtils import header, banner, footer


##############################################################################
# classes
##############################################################################


class startChrono:
   '''
   provide chronograph functionalities
   '''
   def __init__(self):
      '''
      start chronograph
      '''
      self._start = t.time()
      self._ref = self._start

   def partial(self):
      '''
      returns partial elapsed time
      '''
      self._partial = t.time()
      partial = self._partial - self._ref
      self._ref = self._partial
      return "partial elapsed time: %.2f s" % partial

   def stop(self):
      '''
      returns total elapsed time
      '''
      total = t.time() - self._start
      return "total elapsed time: %.2f s" % total


##############################################################################
# main
##############################################################################


if  __name__ == '__main__':

   from logUtils import Logger
   header()
   banner('Autotest...')
   test_chronometre = startChrono()
   t.sleep(1)
   Logger.logr.info(test_chronometre.partial())
   t.sleep(1)
   Logger.logr.info(test_chronometre.partial())
   t.sleep(1)
   Logger.logr.info(test_chronometre.partial())
   Logger.logr.info(test_chronometre.stop())
   footer()


##############################################################################
# eof
##############################################################################
