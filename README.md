# memogrep
A simple grep for Quiver memo.

## Usage
```sh
memogrep.py [-h] -q QVLIBRARY_PATH [-i] [-n NUM_SPACES] [-t] [-v] pattern

Search for PATTERN in my Quiver memo

positional arguments:
  pattern               search string

optional arguments:
  -h, --help            show this help message and exit
  -q QVLIBRARY_PATH, --qvlibrary-path QVLIBRARY_PATH
                        Path to Quiver library (Quiver.qvlibrary)
  -i, --ignore-case     Match case-insensitively
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
```
