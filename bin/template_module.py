#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
+----------------------------------------------------------------------------+
| template_module:  a module skeleton                                        |
+---------+----------+----------+--------------------------------------------+
| version | datecode | author   | history                                    |
+---------+----------+----------+--------------------------------------------+
| 1.0     | 151215   | DD       | creation                                   |
+---------+----------+----------+--------------------------------------------+
'''

VERSION = 'v1.0_151215'

##############################################################################
# external modules
##############################################################################


from ConfigParser import ConfigParser


##############################################################################
# local modules
##############################################################################


from logUtils import logging
from messagesUtils import header, banner, footer
from pathUtils import currentPath


##############################################################################
# classes 
##############################################################################


class template_class():
   pass


##############################################################################
# functions 
##############################################################################


def template_function():
   files=('fic1', 'fic2', 'fic3', 'fic4')
   logger.info('Entre dans la fonction...')
   try:
      with open(files[0]) as f:
         logger.debug("'%s' exists...", files[0])
   except IOError:
      logger.error("'%s' doesn't exist...", files[0])
      for i in range(1,4):
         try:
            with open(files[i]) as f:
                logger.debug("'%s' exists...", files[i])
         except IOError:
            logger.error("'%s' doesn't exist...", files[i])
   

def main():
   logger = logging.getLogger(__name__)
   logger.info("Bonjour!")
   template_function()
   logger.info("Au revoir!")


##############################################################################
# main
##############################################################################


if __name__ == '__main__':
   header()
   banner("Execution...")
   status=main()
   footer(status)


##############################################################################
# eof
##############################################################################
