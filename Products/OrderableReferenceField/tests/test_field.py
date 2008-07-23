##############################################################################
#
# OrderableReferenceField - Orderable Reference Field
# Copyright (C) 2006 Zest Software
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
##############################################################################
"""
$Id$
"""

import os, sys

if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

# Load fixture
import unittest
from Testing import ZopeTestCase
from Testing.ZopeTestCase import doctest
from Products.CMFPlone.tests import PloneTestCase

ZopeTestCase.installProduct('Archetypes')
ZopeTestCase.installProduct('OrderableReferenceField')

class OrderableReferenceFieldTest(PloneTestCase.PloneTestCase):

    def afterSetUp(self):
        from Products.OrderableReferenceField import OrderableReferenceField
        self.field = OrderableReferenceField('aField', relationship='aField')
        self.folder.validate_field = lambda *args, **kw: None

        self.folder.invokeFactory('Document', 'd1')
        self.folder.invokeFactory('Document', 'd2')        

    def test_defaults(self):
        self.assertEquals(self.field.get(self.folder), [])

    def test_getRaw(self):
        self.assertEquals(self.field.getRaw(self.folder), [])
        self.field.set(self.folder, [self.folder.d1.UID()])
        self.assertEquals(self.field.getRaw(self.folder),
                          [self.folder.d1.UID()])

    def test_set(self):
        self.assertEquals(self.field.get(self.folder), [])
        self.field.set(self.folder, [self.folder.d2, self.folder.d1])
        self.assertEquals(self.field.get(self.folder),
                          [self.folder.d2, self.folder.d1])


class OrderableReferenceFieldInstallTest(PloneTestCase.PloneTestCase):

    def testInstall(self):
        qi = self.portal.portal_quickinstaller
        qi.installProducts(('MarcoPolo',))

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(OrderableReferenceFieldTest))
    suite.addTest(unittest.makeSuite(OrderableReferenceFieldInstallTest))
    return suite

if __name__ == '__main__':
    framework(descriptions=0, verbosity=1)
