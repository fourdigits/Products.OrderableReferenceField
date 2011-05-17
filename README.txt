Introduction
============

This product provides an Archetype field that's very similiar to the Archetypes
Reference field, with the addition that it stores the order of referenced objects.

You can use two different widget for manage reference order:

- the ``OrderableReferenceField`` (default ones), someway similar to the
  `InAndOutWidget`__
- the ``OrderableReferenceBrowserWidget``, that use the default `ReferenceBrowserWidget`__

__ http://plone.org/documentation/manual/developer-manual/archetypes/fields/widgets-reference#InAndOutWidget
__ http://plone.org/documentation/manual/developer-manual/archetypes/fields/widgets-reference#ReferenceBrowserWidget

Usage
-----

1. Add this package to your buildout or setup.py of your custom-package

3. Add one of those lines to your custom Archetype to import the fields::

    from Products.OrderableReferenceField import OrderableReferenceField
    
   or::
    
    from Products.OrderableReferenceField import OrderableReferenceBrowserWidget

4. In your schema, add an OrderableReferenceField like this::

    BaseSchema + Schema(( ...
        OrderableReferenceField('afield', relationship='somrel'),
        ...
    ))

   in alternative, write something like this for use the other widget::
   
    BaseSchema + Schema(( ...
        OrderableReferenceField('afield',
                                relationship='somrel',
                                OrderableReferenceField()),
        ...
    ))

Credits
-------

- Written by Daniel Nouri <d.nouri@zestsoftware.nl>

- Thanks to Ilia Goranov <babailiica@babailiica.com> for the JavaScript

- Thanks to Ender <Danny Bloemendaal, danny.bloemendaal@informaat.nl> for
  improving usability of the widget.

- Thanks to jladage <Jean-Paul Ladage, j.ladage@zestsoftware.nl> for adding the
  css and js to ResourceRegistries

- Thanks to mirella <Mirella van Teulingen, m.van.teulingen@zestsoftware.nl>
  for cleaning up the template by moving style elements to the css.

- Eggification by aclark

- Move install-code to GS-profiles by WouterVH

- ``OrderableReferenceBrowserWidget`` widget added by RedTurtle Technology
  <sviluppoplone@redturtle.net>

Copyright
---------

Copyright (C) 2006 "Zest Software": http://zestsoftware.nl
