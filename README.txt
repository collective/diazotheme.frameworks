Introduction
============
This is a collection of Diazo themes meant to serve as parent themes. Most of 
these themes are molding the plone html into a framework complient html. 

The "plone" theme is the exeption to the rule. As a theme it adds html 
structures to the plone sunburst theme. It also contains a lot of utilities, 
like different colors and sizes of the plone logo and icons, and more.

Updating
========

Bootstrap
---------

To update the resources in this package to a newer version of Bootstrap,
do the following under an environment with a Bash or comparable shell::

   cd diazotheme.frameworks/diazotheme/framworks
   wget http://getbootstrap.com/2.3.2/assets/bootstrap.zip
   unzip -o bootstrap.zip
   rm bootstrap.zip
   cd bootstrap/examples
   for file in *.html; 
   do 
      wget https://github.com/twbs/bootstrap/raw/gh-pages/2.3.2/examples/$file -O $file;
   done

   cd ../js
   wget http://getbootstrap.com/2.3.2/assets/js/html5shiv.js -O html5shiv.js

The current version of Bootstrap is 2.3.2. Note that this version is not
backward compatible with the newer Bootstrap 3.x. The above instructions
should only be utilsed for 2.x series updates.
