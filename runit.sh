#! /bin/sh
cd "$(dirname "$(readlink -f "$0")")"
wget -m http://archive.luftdaten.info/
find archive.luftdaten.info -name \*.csv -mtime -2 | parallel --verbose -j 5 -n1 python ./luftdaten2graphite.py
