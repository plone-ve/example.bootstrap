=================
example.bootstrap
=================


Introduction
============

*example.bootstrap* is an example of a installable Plone theme package that 
support the `Twitter Bootstrap <http://getbootstrap.com/>`_ integration with 
the `LESS`_ resources files using the `collective.lesscss`_ package in your 
theme package.


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)
- The `collective.lesscss`_ package (*will be installed as a dependency of this package*)


Features
========

- `Bootstrap v2.0.2 <http://getbootstrap.com/2.0.2/>`_ support included.
- It's an installable Plone Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.


Installation
============


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``example.bootstrap`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        example.bootstrap


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'example.bootstrap',
    ],


Resources
=========

The resources of this theme can be reached through

``/++bootstrap++less``
  To access to `LESS`_ resources files.

``/++bootstrap++js``
  To access to `jQuery`_ resources files.

``/++bootstrap++img``
  To access to images resources files.

There are placed at ``example.bootstrap/src/example/bootstrap/resources`` 
directory with following resources files:

::

    resources/
    ├── img
    │   ├── glyphicons-halflings.png
    │   └── glyphicons-halflings-white.png
    ├── js
    │   ├── bootstrap-alert.js
    │   ├── bootstrap-button.js
    │   ├── bootstrap-carousel.js
    │   ├── bootstrap-collapse.js
    │   ├── bootstrap-dropdown.js
    │   ├── bootstrap-modal.js
    │   ├── bootstrap-popover.js
    │   ├── bootstrap-scrollspy.js
    │   ├── bootstrap-tab.js
    │   ├── bootstrap-tooltip.js
    │   ├── bootstrap-transition.js
    │   ├── bootstrap-typeahead.js
    │   ├── README.md
    │   └── tests
    │       ├── index.html
    │       ├── unit
    │       │   ├── bootstrap-alert.js
    │       │   ├── bootstrap-button.js
    │       │   ├── bootstrap-collapse.js
    │       │   ├── bootstrap-dropdown.js
    │       │   ├── bootstrap-modal.js
    │       │   ├── bootstrap-popover.js
    │       │   ├── bootstrap-scrollspy.js
    │       │   ├── bootstrap-tab.js
    │       │   ├── bootstrap-tooltip.js
    │       │   ├── bootstrap-transition.js
    │       │   └── bootstrap-typeahead.js
    │       └── vendor
    │           ├── jquery.js
    │           ├── qunit.css
    │           └── qunit.js
    └── less
        ├── accordion.less
        ├── alerts.less
        ├── badges.less
        ├── bootstrap.less
        ├── breadcrumbs.less
        ├── button-groups.less
        ├── buttons.less
        ├── carousel.less
        ├── close.less
        ├── code.less
        ├── component-animations.less
        ├── dropdowns.less
        ├── forms.less
        ├── grid.less
        ├── hero-unit.less
        ├── labels.less
        ├── layouts.less
        ├── mixins.less
        ├── modals.less
        ├── navbar.less
        ├── navs.less
        ├── pager.less
        ├── pagination.less
        ├── popovers.less
        ├── progress-bars.less
        ├── reset.less
        ├── responsive.less
        ├── scaffolding.less
        ├── sprites.less
        ├── tables.less
        ├── thumbnails.less
        ├── tooltip.less
        ├── type.less
        ├── utilities.less
        ├── variables.less
        └── wells.less


Contribute
==========

- Issue Tracker: https://github.com/sneridagh/example.bootstrap/issues
- Source Code: https://github.com/sneridagh/example.bootstrap


License
=======

The project is licensed under the GPLv2.

Credits
-------

- Victor Fernandez de Alba (sneridagh)


Amazing contributions
---------------------

- Leonardo J. Caballero G. aka macagua (leonardocaballero at gmail dot com).

You can find an updated list of package contributors on https://github.com/sneridagh/example.bootstrap/contributors

.. _`example.bootstrap`: https://github.com/sneridagh/example.bootstrap
.. _`collective.lesscss`: http://pypi.org/project/collective.lesscss/
.. _`LESS`: http://lesscss.org/
.. _`jQuery`: https://jquery.com/
