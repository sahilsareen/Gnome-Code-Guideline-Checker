#!/usr/bin/env python

# script to check if any gnome coding guidelines are violated
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
            if lines[ lineNum ][ index - 1 ] != ' ' and lines[ lineNum ][ index - 1 ] not in [ '_', '(', '&', '*', '-', '(', '!','\t' ]:
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
