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
use the ``upgrade.sh`` script::

   ./upgrade.sh 2.3.2

where the first argument is the version of Bootstrap to upgrade to.

The current version of Bootstrap is 2.3.2. Note that this version is not
backward compatible with the newer Bootstrap 3.x. For now, the above 
upgrade script **should** only be utilsed for 2.x series updates.
