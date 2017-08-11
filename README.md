# memogrep
A simple grep for Quiver memo.

## Usage
```sh
usage: memogrep.py [-h] -q QVLIBRARY_PATH [-i] [-b BULLET_TYPE]
                   [-n NUM_SPACES] [-t] [-v]
                   keyword [keyword ...]

Search for KEYWORD in my Quiver memo

positional arguments:
  keyword               search string

optional arguments:
  -h, --help            show this help message and exit
  -q QVLIBRARY_PATH, --qvlibrary-path QVLIBRARY_PATH
                        Path to Quiver library (Quiver.qvlibrary)
  -i, --ignore-case     Match case-insensitively
  -b BULLET_TYPE, --bullet-type BULLET_TYPE
                        Bullet type for title
  -n NUM_SPACES, --num-spaces NUM_SPACES
                        Num. of spaces on indent
  -t, --title           Displays title only
  -v, --version         show program's version number and exit
```

## Example
```sh
% ./memogrep.py -q ~/Dropbox/Sync/Quiver/Quiver.qvlibrary keyword
or
% myqvlibrary=`mdfind -onlyin ~ -name Quiver.qvlibrary | grep 'Quiver/Quiver.qvlibrary'`
% ./memogrep.py -q $myqvlibrary keyword

Use with [terminal markdown viewer](https://github.com/axiros/terminal_markdown_viewer)
% ./memogrep.py -q $myqvlibrary -i -n 0 -b '#' keyword | mdv -t 881.4906 - 
```
