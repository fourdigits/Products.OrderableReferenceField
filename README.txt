Introduction
============

This product provides an Archetype field that's very similiar to the Archetypes
Reference field, with the addition that it stores the order of referenced objects.

Usage
-----

1. Install as usual in your Products directory.

2. Install it in Plone to make the skins available.

3. Add this line to your custom Archetype to import the fields::

    from Products.OrderableReferenceField import OrderableReferenceField

4. In your schema, add an OrderableReferenceField like this::

    BaseSchema + Schema(( ...
    OrderableReferenceField('afield', relationship='somrel'),
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


Copyright
---------
Copyright (C) 2006 "Zest Software":http://zestsoftware.nl
