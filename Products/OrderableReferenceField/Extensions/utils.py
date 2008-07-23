from Products.CMFCore.utils import getToolByName

def registerResources(self, out, toolname, resources):
    tool = getToolByName(self, toolname)
    existing = tool.getResourceIds()
    cook = False
    for resource in resources:
        if not resource['id'] in existing:
            # register additional resource in the specified registry...
            if toolname == "portal_css":
                tool.registerStylesheet(**resource)
            if toolname == "portal_javascripts":
                tool.registerScript(**resource)
            print >> out, "Added %s to %s." % (resource['id'], tool)
        else:
            # ...or update existing one
            parameters = tool.getResource(resource['id'])._data
            for key in [k for k in resource.keys() if k != 'id']:
                originalkey = 'original_'+key
                original = parameters.get(originalkey)
                if not original:
                    parameters[originalkey] = parameters[key]
                parameters[key] = resource[key]
                print >> out, "Updated %s in %s." % (resource['id'], tool)
                cook = True
    if cook:
        tool.cookResources()
    print >> out, "Successfuly Installed/Updated resources in %s." % tool

def resetResources(self, out, toolname, resources):
    # Revert resource customizations
    tool = getToolByName(self, toolname)
    for r in resources:
        resource = tool.getResource(r['id'])
        if not resource == None:
            for key in resource._data.keys():
                originalkey = 'original_'+key
                if resource._data.has_key(originalkey):
                    try: # <- BBB
                        resource._data[key] = resource._data[originalkey]['value']
                    except TypeError:
                        resource._data[key] = resource._data[originalkey]
                    del resource._data[originalkey]
