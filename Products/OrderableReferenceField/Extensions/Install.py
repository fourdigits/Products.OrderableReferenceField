from cStringIO import StringIO
from Products.OrderableReferenceField.config import *
from Products.OrderableReferenceField.Extensions.utils import *
from Products.Archetypes.Extensions.utils import install_subskin

from Products.OrderableReferenceField import GLOBALS

def install(self):
    out = StringIO()

    install_subskin(self, out, GLOBALS)
    registerResources(self, out, 'portal_css', STYLESHEETS)
    registerResources(self, out, 'portal_javascripts', JAVASCRIPTS)

    out.write("Successfully installed OrderableReferenceField.")
    return out.getvalue()

def uninstall(self):
    out = StringIO()
    resetResources(self, out, 'portal_css', STYLESHEETS)
    resetResources(self, out, 'portal_javascripts', JAVASCRIPTS)
