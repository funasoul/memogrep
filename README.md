# memogrep
A simple grep for [Quiver](http://happenapps.com/#quiver) memo.

## Usage
```sh
usage: memogrep.py [-h] [-q QVLIBRARY_PATH] [-i] [-b BULLET_TYPE]
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
% ./memogrep.py keyword
or
% myqvlibrary=`mdfind -onlyin ~ -name Quiver.qvlibrary | grep 'Quiver/Quiver.qvlibrary'`
% ./memogrep.py -q $myqvlibrary keyword
```
Use with [terminal markdown viewer](https://github.com/axiros/terminal_markdown_viewer)
```sh
% ./memogrep.py -i -n 0 -b '#' keyword | mdv -t 881.4906 - 
```
If you are using zsh/bash, following function might be your help.
```sh
function memogrep() {
  if hash mdv >/dev/null 2>&1; then
    memogrep.py -i -n 0 -b '#' $@ | mdv -t 881.4906 - | less -sIx4XF
  else
    memogrep.py -i $@ | less -sIx4XF
  fi
}
```

## Screenshot
![screenshot](https://raw.githubusercontent.com/funasoul/memogrep/images/memogrep.png)
