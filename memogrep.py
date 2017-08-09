#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# -*- coding: utf-8 -*-
#
# Last modified: Wed, 09 Aug 2017 12:15:39 -0400
# 
# (ex.) ./memogrep.py -q ~/Dropbox/Sync/Quiver/Quiver.qvlibrary keyword 
#
import argparse
import datetime
import json
import operator
import os
import sys
from pprint import pprint

__version__ = "1.0.0"

def contains_string(dict, query, ignorecase):
    if (ignorecase):
        return contains_string_ignorecase(dict, query)

    if "tags" in dict:
        for tag in dict["tags"]:
            if query in tag:
                return True

    if "title" in dict:
        if query in dict["title"]:
            return True

    if "cells" in dict:
        for cell in dict["cells"]:
            if query in cell["data"]:
                return True

    return False

def contains_string_ignorecase(dict, query):
    if "tags" in dict:
        for tag in dict["tags"]:
            if query.lower() in tag.lower():
                return True

    if "title" in dict:
        if query.lower() in dict["title"].lower():
            return True

    if "cells" in dict:
        for cell in dict["cells"]:
            if query.lower() in cell["data"].lower():
                return True

    return False

def toString(meta, content, headerOnly, num_spaces):
    RESET   = '\033[0m'
    RED     = '\033[1;31m'
    GREEN   = '\033[1;32m'
    YELLOW  = '\033[1;33m'
    BLUE    = '\033[1;34m'
    MAGENTA = '\033[1;35m'
    CYAN    = '\033[1;36m'
    dateStr = datetime.datetime.fromtimestamp(meta["created_at"]).strftime('%Y-%m-%d')
    tagList = []
    for tag in meta["tags"]:
        tagList.append("[")
        tagList.append(tag)
        tagList.append("]")

    tagStr = ''.join(tagList)
    str = "* %s%s %s%s%s %s%s" % (YELLOW, dateStr, BLUE, tagStr, GREEN, meta["title"], RESET)
    if not headerOnly:
        cellList = []
        for cell in content["cells"]:
            cellList.append(cell["data"])
            cellList.append("\n")
        bodyStr = ''.join(cellList)
        bodyStr = indent(bodyStr, num_spaces)
        str = str + '\n' + bodyStr + '\n'

    return str.encode('utf-8')

def indent(text, amount, ch=' '):
    # http://stackoverflow.com/questions/8234274/how-to-indent-the-contents-of-a-multi-line-string
    padding = amount * ch
    return ''.join(padding+line for line in text.splitlines(True))

def main():
    parser = argparse.ArgumentParser(description="Search for PATTERN in my Quiver memo")
    parser.add_argument('-q', '--qvlibrary-path', action='store', required=True,
            help='Path to Quiver library (Quiver.qvlibrary)')
    parser.add_argument('-i', '--ignore-case', action='store_true',
            help='Match case-insensitively')
    parser.add_argument('-n', '--num-spaces', action='store',
            help='Num. of spaces on indent', type=int, default=4)
    parser.add_argument('-t', '--title', action='store_true',
            help='Displays title only')
    parser.add_argument('-v', '--version', action='version',
            version=('memogrep.py %s' % __version__))
    parser.add_argument("pattern", metavar='keyword', nargs='+', help="search string")
    args = parser.parse_args()

    dictCreateDate = {}
    dictMeta = {}
    dictContent = {}
    for root, dirs, files in os.walk(args.qvlibrary_path):
        for dir in dirs:
            if dir.endswith(".qvnote") and 'Trash.qvnotebook' not in root and 'Tutorial.qvnotebook' not in root:
                file = os.path.join(os.path.join(root, dir), 'meta.json')
                if os.path.isfile(file):
                    with open(file) as data_file:
                        data = json.loads(data_file.read(), 'utf-8')
                        dictCreateDate[data["uuid"]] = data["created_at"]
                        dictMeta[data["uuid"]] = data

                contentfile = os.path.join(os.path.join(root, dir), 'content.json')
                if os.path.isfile(contentfile):
                    with open(contentfile) as content_file:
                        content_data = json.loads(content_file.read(), 'utf-8')
                        dictContent[data["uuid"]] = content_data

    sorted_dict = sorted(dictCreateDate.items(), key=operator.itemgetter(1), reverse=True)
    utf8_pattern_list = [x.decode('utf-8') for x in args.pattern]
    for tuple in sorted_dict:
        key = tuple[0];
        meta = dictMeta[key]
        content = dictContent[key]
        matched = True
        for utf8_pattern in utf8_pattern_list:
            if not contains_string(meta, utf8_pattern, args.ignore_case) and not contains_string(content, utf8_pattern, args.ignore_case):
                matched = False

        if matched:
            print toString(meta, content, args.title, args.num_spaces)

if __name__ == "__main__":
    main()
