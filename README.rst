=====================
diazotheme.frameworks
=====================


Introduction
============

``diazotheme.frameworks`` is a collection of Diazo themes meant to serve as parent themes. 
Most of these themes are molding the plone html into a framework compliant html.

The "plone" theme is the exception to the rule. As a theme it adds html 
structures to the plone sunburst theme. It also contains a lot of utilities, 
like different colors and sizes of the plone logo and icons, and more.

This package provides diazo themes based on many *CSS framework* using the **theming** and 
**packaging** features available for create `Diazo`_ theme using `plone.app.theming`_.

``diazotheme.frameworks`` package contains the following css framework implementations: 

- `Twitter Bootstrap CSS framework`_.
- `Zurb Foundation CSS framework`_.
- `Goldilocks Approach CSS framework`_.
- `Kube CSS framework`_.


Extending
=========


How to create a child theme
---------------------------

Any of the themes folders can be used to create your own child theme, 
based on `diazoframework.frameworks`_. You can either wrap the theme up in a package 
or you can create a zip file of the folder and upload that to the theme panel.

There are two ways of creating a child theme.


The package way
^^^^^^^^^^^^^^^

For this example, lets assume we are creating a package called
``diazotheme.newtheme`` and we will copy the ``bootstrap`` theme in this 
package.

1. Created the ``diazotheme.newtheme`` package (for instance through ``paster`` script).

2. Copy ``diazotheme.frameworks/diazotheme/frameworks/bootstrap`` to
   ``diazotheme.newtheme/diazotheme/newtheme/static`` (arbitrary
   name).

3. Remove ``diazotheme.frameworks/diazotheme/frameworks/bootstrap/examples`` directory.

4. Add `<plone:static directory="static" name="newtheme" type="theme"/>`
   to ``diazotheme.newtheme/diazotheme/newtheme/configure.zcml``.

5. Change ``diazotheme.newtheme/diazotheme/newtheme/static/manifest.cfg``
   to reflect the changes, so: ::

        [theme]
        title = New theme
        description = Describe the new theme
        rules = /++theme++newtheme/rules.xml
        prefix = /++theme++newtheme
        doctype = <!DOCTYPE html>
        preview = preview.png


The zip file way
^^^^^^^^^^^^^^^^

Again, lets assume we use the ``bootstrap`` theme and we want to end up
with the ``newtheme`` name.

1. Copy ``diazotheme.frameworks/diazotheme/frameworks/bootstrap`` to your file system.

2. Rename ``bootstrap`` to ``newtheme`` (the folder name will become the
   theme name in the theme panel)

3. Remove ``diazotheme.frameworks/diazotheme/frameworks/bootstrap/examples`` directory.

4. Change ``newtheme/manifest.cfg``
   to reflect the changes, so: ::

        [theme]
        title = New theme
        description = Describe the new theme
        rules = /++theme++newtheme/rules.xml
        prefix = /++theme++newtheme
        doctype = <!DOCTYPE html>
        preview = preview.png

4. Customize your theme.

5. When you are finished customizing, create a zip archive of the 
   ``newtheme`` folder.

6. Upload the ``newtheme.zip`` in the plone theme panel.


Screenshots
===========


Twitter Bootstrap Starter Theme
-------------------------------

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/diazotheme.frameworks/raw/master/diazotheme/frameworks/bootstrap/preview.png
  :alt: Twitter Bootstrap Starter Theme
  :align: center


Twitter Bootstrap Hero Theme
----------------------------

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/diazotheme.frameworks/raw/master/diazotheme/frameworks/bootstrap/examples/hero/preview.png
  :alt: Twitter Bootstrap Hero Theme
  :align: center


Twitter Bootstrap Marketing Narrow Theme
----------------------------------------

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/diazotheme.frameworks/raw/master/diazotheme/frameworks/bootstrap/examples/marketing-narrow/preview.png
  :alt: Twitter Bootstrap Marketing Narrow Theme
  :align: center


Zurb Foundation Example Theme
-----------------------------

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/diazotheme.frameworks/raw/master/diazotheme/frameworks/foundation/preview.png
  :alt: Zurb Foundation Example Theme
  :align: center


Zurb Foundation Blades of Steel Theme
-------------------------------------

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/diazotheme.frameworks/raw/master/diazotheme/frameworks/foundation/examples/bladesofsteel/preview.png
  :alt: Zurb Foundation Blades of Steel Theme
  :align: center


Zurb Foundation Coffee 'N Milk Theme
------------------------------------

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/diazotheme.frameworks/raw/master/diazotheme/frameworks/foundation/examples/coffeenmilk/preview.png
  :alt: Zurb Foundation Coffee 'N Milk Theme
  :align: center


Zurb Foundation Evergreen Theme
-------------------------------

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/diazotheme.frameworks/raw/master/diazotheme/frameworks/foundation/examples/evergreen/preview.png
  :alt: Zurb Foundation Evergreen Theme
  :align: center


Goldilocks Approach Black Theme
-------------------------------

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/diazotheme.frameworks/raw/master/diazotheme/frameworks/goldilocks/examples/black/preview.png
  :alt: Goldilocks Approach Black Theme
  :align: center


Goldilocks Approach White Theme
-------------------------------

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/diazotheme.frameworks/raw/master/diazotheme/frameworks/goldilocks/preview.png
  :alt: Goldilocks Approach White Theme
  :align: center


Kube Framework Theme
--------------------

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/diazotheme.frameworks/raw/master/diazotheme/frameworks/kube/preview.png
  :alt: Kube Framework Theme
  :align: center


Kube Demo Theme
---------------

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/diazotheme.frameworks/raw/master/diazotheme/frameworks/kube/examples/demo/preview.png
  :alt: Kube Demo Theme
  :align: center


Kube Start Theme
----------------

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/diazotheme.frameworks/raw/master/diazotheme/frameworks/kube/examples/start/preview.png
  :alt: Kube Start Theme
  :align: center


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)
- The ``plone.app.theming`` package (*You will need enable it to use this package*)


Features
========

- Provides the diazo rules for *Twitter Bootstrap Starter* theme.
- Provides the diazo rules for *Twitter Bootstrap Hero* theme.
- Provides the diazo rules for *Twitter Bootstrap Marketing Narrow* theme.
- Provides the diazo rules for *Zurb Foundation Example* theme.
- Provides the diazo rules for *Zurb Foundation Blades of Steel* theme.
- Provides the diazo rules for *Zurb Foundation Coffee 'N Milk* theme.
- Provides the diazo rules for *Zurb Foundation Evergreen* theme.
- Provides the diazo rules for *Goldilocks Approach Black* theme.
- Provides the diazo rules for *Goldilocks Approach White* theme.
- Provides the diazo rules for *Kube Framework* theme.
- Provides the diazo rules for *Kube Start* theme.
- Provides the diazo rules for *Kube Demo* theme.


Installation
============


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``diazotheme.frameworks`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        diazotheme.frameworks


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'diazotheme.frameworks',
    ],


Resources
=========

This package is the parent of all Plone diazo themes and 
provides rule that are practical to use in other diazo themes.

Twitter Bootstrap
-----------------

The resources of this framework can be reached through

- **Twitter Bootstrap Starter Theme**
    ``/++theme++bootstrap-framework``
- **Twitter Bootstrap Hero Theme**
    ``/++theme++bootstrap-hero``
- **Twitter Bootstrap Marketing Narrow Theme**
    ``/++theme++bootstrap-marketing-narrow``

There are placed at ``diazotheme.frameworks/diazotheme/frameworks/bootstrap`` 
directory with following resources files:

::

    _ bootstrap
      Provides the resources from *Twitter Bootstrap*.
      _ css
      _ examples
        _ hero
        _ marketing-narrow
        _ carousel.html
        _ fluid.html
        _ hero.html
        _ marketing-narrow.html
        _ starter-template.html
        _ sticky-footer.html
      _ img
      _ js
      _ rules
      _ index.html
      _ manifest.cfg
      _ preview.png
      _ README.txt
      _ rules.xml


This is the Bootstrap Theme applied through Diazo.

To apply this theme, in site setup:
- Install "Diazo theme support" under Add-on
- Select "(Unstyles)" as Default themes under Themes
- Enable "Bootstrap Theme (bootstrap)" under Diazo themes


Zurb Foundation
---------------

The resources of this framework can be reached through

- **Zurb Foundation Example Theme**
    ``/++theme++foundation-framework``
- **Zurb Foundation Blades of Steel**
    ``/++theme++foundstyles-bladesofsteel``
- **Zurb Foundation Coffee 'N Milk**
    ``/++theme++foundstyles-coffeenmilk``
- **Zurb Foundation Evergreen**
    ``/++theme++foundstyles-evergreen``

There are placed at ``diazotheme.frameworks/diazotheme/frameworks/foundation`` 
directory with following resources files:

::

    _ foundation
      Provides the resources from *Zurb Foundation*.
      _ examples
        _ bladesofsteel
        _ coffeenmilk
        _ evergreen
      _ images
      _ javascripts
      _ rules
      _ stylesheets
      _ humans.txt
      _ index.html
      _ manifest.cfg
      _ preview.png
      _ README.txt
      _ rules.xml


Goldilocks Approach
-------------------

The resources of this framework can be reached through

- **Goldilocks Approach Black**
    ``/++theme++goldilocks-black``
- **Goldilocks Approach White**
    ``/++theme++goldilocks-framework``

There are placed at ``diazotheme.frameworks/diazotheme/frameworks/goldilocks`` 
directory with following resources files:

::

    _ goldilocks
      Provides the resources from *Goldilocks Approach*.
      _ css
      _ examples
        _ black
      _ images
      _ js
      _ rules
      _ stylesheets
      _ example.html
      _ index.html
      _ manifest.cfg
      _ preview.png
      _ README.txt
      _ rules.xml


Kube CSS
--------

The resources of this framework can be reached through

- **Kube Framework Theme**
    ``/++theme++kube-framework``
- **Kube Start Theme**
    ``/++theme++kube-start``
- **Kube Demo Theme**
    ``/++theme++kube-demo``

There are placed at ``diazotheme.frameworks/diazotheme/frameworks/kube`` 
directory with following resources files:

::

    _ goldilocks
      Provides the resources from *Kube CSS*.
      _ css
      _ examples
        _ demo
        _ start
      _ less
      _ rules
      _ index.html
      _ manifest.cfg
      _ preview.png
      _ README.txt
      _ rules.xml


Plone Theme
-----------

The resources of this framework can be reached through

- **Plone Theme**
    ``/++theme++plone``

There are placed at ``diazotheme.frameworks/diazotheme/frameworks/plone`` 
directory with following resources files:

::

    _ goldilocks
      Provides the resources from *Plone Theme*.
      _ css
      _ favicon
      _ img
        _ background
        _ black
        _ default
        _ white
      _ js
      _ rules
        _ head
        _ icon
        _ logo
        _ utility
      _ index.html
      _ manifest.cfg
      _ preview.png
      _ README.txt
      _ rules.xml


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


Contribute
==========

- Issue Tracker: https://github.com/collective/diazotheme.frameworks/issues
- Source Code: https://github.com/collective/diazotheme.frameworks


License
=======

The project is licensed under the GPLv2.


Credits
-------

- Thijs Jonkman (t.jonkman at gmail dot com).


Amazing contributions
---------------------

- Leonardo J. Caballero G. aka macagua (leonardocaballero at gmail dot com).

You can find an updated list of package contributors on https://github.com/collective/diazotheme.frameworks/contributors

.. _`Twitter Bootstrap CSS framework`: http://twitter.github.io/
.. _`Diazo`: http://diazo.org
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
.. _`Zurb Foundation CSS framework`: http://foundation.zurb.com/
.. _`Goldilocks Approach CSS framework`: http://goldilocksapproach.com/
.. _`Kube CSS framework`: http://imperavi.com/kube/
.. _`diazoframework.frameworks`: https://github.com/TH-code/diazoframework.frameworks
.. _`diazotheme.frameworks`: https://github.com/collective/diazotheme.frameworks
