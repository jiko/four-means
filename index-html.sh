#!/bin/sh
# cribbed from http://odoepner.wordpress.com/2012/02/17/shell-script-to-generate-simple-index-html/

echo '<html><head><title>Four Means Index</title></head>'
echo '<body><ul>'
sed 's/^.*/<li><a href="&">&<\/a><\/li>/'
echo '</ul></body></html>'
