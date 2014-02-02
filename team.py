#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Michel Petit <petit.michel@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import optparse
import teamlib
import sys
#import urllib2
import locale
import gettext
from gettext import gettext as _
from teamlib.version import APP_VERSION
from teamlib.version import APP_NAME
from teamlib.Team import Team

local_path = os.path.realpath(os.path.dirname(sys.argv[0])) + os.sep + 'locale'

langs = []

lc, encoding = locale.getdefaultlocale()

if (lc):
	#If we have a default, it's the first in the list
	langs = [lc]
# Now lets get all of the supported languages on the system
language = os.environ.get('LANGUAGE', None)

if (language):
	"""langage comes back something like en_CA:en_US:en_GB:en
	on linuxy systems, on Win32 it's nothing, so we need to
	split it up into a list"""
	langs += language.split(":")
"""our defaults"""
langs += ["fr_FR", 'en_US']



gettext.bindtextdomain(APP_NAME, local_path)
gettext.textdomain(APP_NAME)

try:
    lang = gettext.translation(APP_NAME, local_path, languages=langs, fallback = False)
    _ = lang.ugettext
except IOError as e:
    print 'Translation not implemented yet!'
    print e.strerror

def main():
    parser = optparse.OptionParser(version="%prog " + APP_VERSION)
    parser.add_option("-t", "--token", dest="token", help=_("Token you must get from your administrator or by your settings page on Ruche web site you are using."), metavar=_("STRING"))
    parser.add_option("-u", "--url", dest="url", help=_("URL base to use for the request."), metavar=_("URL"))
    parser.add_option("--csv", dest='csv', help=_("Export response as CSV."), metavar=_('FILE'))
    parser.add_option("--xml", dest='xml', help=_("Export response as XML."), metavar=_('FILE'))
    parser.add_option("--json", dest='json', help=_("Export response as JSON."), metavar=_('FILE'))
    (options, args) = parser.parse_args()

    if(options.token and options.url):
        t = Team(options.token, options.url)


if __name__ == "__main__":
    main()

