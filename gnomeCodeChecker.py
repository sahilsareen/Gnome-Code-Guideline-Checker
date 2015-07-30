#!/usr/bin/env python

# script to check if any GNOME coding guidelines are violated
# Copyright (C) 2015 Sahil Sareen (ssareen [ AT ] gnome [ DOT ] org)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import sys
import re

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

# Read the file
with open( sys.argv[1] ) as f:
    lines = f.readlines()

# Line Width
for lineNum in xrange( 0, len( lines ) ):
    if len( lines[ lineNum ] ) > 120:
        print "Line ", lineNum+1, " is greater than 120 charecters"
    
# Lines with trailing white-space or tabs
for lineNum in xrange( 0, len( lines ) ):
    if lines[ lineNum ].endswith(' \n'):
        print "Line ", lineNum+1, " has trailing whitespace"
    if lines[ lineNum ].endswith('\t\n'):
        print "Line ", lineNum+1, " has trailing tabspace"

# Single whitespace before "{"
for lineNum in xrange( 0, len( lines ) ):
    indexes = find( lines[ lineNum ], '{' )
    for index in indexes:
        if index > 1:
            if lines[ lineNum ][ index - 1 ] != ' ' and lines[ lineNum ][ index - 1 ] != '_':
                print "Line ", lineNum+1, " missing whitespace before {"
            elif lines[ lineNum ][ index - 2 ] == ' ' and lines[ lineNum ][ index - 1 ] != '_' \
                    and not ( re.findall( "\s*{", lines[ lineNum ] ) != [] and lines[ lineNum ][ 0 ] in [ '\t', ' ' ] ):
                print "Line ", lineNum+1, " multiple whitespace before {"

# Single whitespace before "("
for lineNum in xrange( 0, len( lines ) ):
    indexes = find( lines[ lineNum ], '(' )
    for index in indexes:
        if index > 1:
            if lines[ lineNum ][ index - 1 ] != ' ' and lines[ lineNum ][ index - 1 ] not in [ '_', '(', '&', '*', '-', '(', '!', '"', '\t' ]:
                print "Line ", lineNum+1, " missing whitespace before ("
            elif lines[ lineNum ][ index - 2 ] == ' ' and lines[ lineNum ][ index - 1 ] not in [ '_', '(' ] \
                    and not ( lines[ lineNum ].startswith(" *") or lines[ lineNum ].startswith("#") or
                              ( re.findall( "\s*\(", lines[ lineNum ] ) != [] and lines[ lineNum ][ 0 ] in [ '\t', ' ' ] ) ):
                print "Line ", lineNum+1, " multiple whitespace before ("
               
# No whitespce between round brackets "(xyz)"
for lineNum in xrange( 0, len( lines ) ):
    indexes = find( lines[ lineNum ], '(' )
    for index in indexes:
        if index > 1:
            if lines[ lineNum ][ index + 1 ] == ' ':
                print "Line ", lineNum+1, " has whitespace after ("

for lineNum in xrange( 0, len( lines ) ):
    indexes = find( lines[ lineNum ], ')' )
    for index in indexes:
        if index > 1:
            if lines[ lineNum ][ index - 1 ] == ' ':
                print "Line ", lineNum+1, " has whitespace before )"
