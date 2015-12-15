#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
+----------------------------------------------------------------------------+
| messagesUtils:  toolbox for displaying formated messages                   |
+---------+----------+----------+--------------------------------------------+
| version | datecode | author   | history                                    |
+---------+----------+----------+--------------------------------------------+
| 1.0     | 151214   | DD       | creation                                   |
+---------+----------+----------+--------------------------------------------+
'''

VERSION = 'v1.0_151214'

##############################################################################
# external modules
##############################################################################

import sys
import inspect
import ast
import datetime


##############################################################################
# functions 
##############################################################################

def header():
   '''
   displays current module docstring
   '''
   f=inspect.stack()[1][1]
   m=ast.parse(''.join(open(f)))
   print "\n%s" % ast.get_docstring(m)


def banner(mess):
   '''
   displays banner message
   '''
   sep = '\n+'+76*'-'+'+\n'
   mess = '| ' +mess + (75-len(mess))*' ' + '|'
   print sep, mess, sep


def footer(code=0):
   '''
   displays current module execution ending
   '''
   banner('end of ' + sys.argv[0])
   sys.exit(code)


def whosdaddy():
   '''
   return parent function name
   '''
   return inspect.stack()[3][3]


def whoami():
   '''
   return current function name
   '''
   whoami=whosdaddy()
   if whoami=='<module>': whoami='module'
   return whoami


def message(mess, severity='info '):
   '''
   print a formated message: "[severity] function name> mess"
      default severity value is 'info'
      for 'debug' severity, message will be display only if DEBUG=True
   '''
   if severity=='debug' and not DEBUG: return
   if TIMESTAMP:
     ts=datetime.datetime.strftime(datetime.datetime.now(), '%y-%m-%d %H:%M:%S ')
   else:
     ts=''
   print "%s[%s] %s> %s" % (ts, severity, whoami(), mess)


##############################################################################
# main
##############################################################################

DEBUG=True
TIMESTAMP=True

if  __name__ == '__main__':
   header()
   banner("Autotest: banner()") 
   message("Autotest: message()")
   if DEBUG:
      message("DEBUG is %s" % DEBUG, "debug")
   else:
      message("DEBUG is %s" % DEBUG)
   message("TIMESTAMP is %s" % TIMESTAMP)
   footer()


##############################################################################
# eof
##############################################################################
