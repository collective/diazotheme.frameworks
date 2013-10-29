#!/bin/bash

if [ -z $1 ] || [ $1 == "--help" ] || [ $1 == "-h" ];
then
    echo "Usage: $0 [version]"
    echo "Upgrades this package to the given version of Bootstrap."
    echo "For example, run '$0 2.3.2' to upgrade to version 2.3.2."
    exit
fi

version="$1"
echo "Downloading Bootstrap $version"
wget http://getbootstrap.com/$version/assets/bootstrap.zip -O bootstrap.zip
unzip -od diazotheme/frameworks/ bootstrap.zip
echo "Upgraded Bootstrap to $version"

for file in diazotheme/frameworks/bootstrap/examples/*.html; 
do 
   wget https://github.com/twbs/bootstrap/raw/gh-pages/$version/examples/`basename $file` -O $file;
   echo "Upgraded $file to $version"
done

wget http://getbootstrap.com/$version/assets/js/html5shiv.js -O diazotheme/frameworks/bootstrap/js/html5shiv.js
echo "Upgraded html5shiv to version used with Bootstrap $version"

echo "Cleaning up"
rm -rf bootstrap.zip bootstrap/



