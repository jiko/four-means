#!/bin/sh
# cribbed from http://odoepner.wordpress.com/2012/02/17/shell-script-to-generate-simple-index-html/

echo '<html>'
echo "\t<head>"
echo "\t\t<title>Four Means Index</title>"
echo "\t</head>"
echo "\t<body>"
echo "\t\t<p><a href='https://github.com/jiko/four-means'>source code</a></p>"
echo "\t\t<ul>"
sed 's/^.*/\t\t\t<li><a href="&">&<\/a><\/li>/'
echo "\t\t</ul>"
echo "\t</body>"
echo "</html>"
