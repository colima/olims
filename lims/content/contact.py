"""The contact person at an organisation.
"""
from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import manage_users
from dependencies.dependency import schemata
from dependencies import atapi
from dependencies.dependency import *
from dependencies.dependency import permissions
from dependencies.dependency import getToolByName
from dependencies.dependency import safe_unicode
from lims.config import ManageClients, PUBLICATION_PREFS, PROJECTNAME
from lims.content.person import Person
from lims import PMF, bikaMessageFactory as _
from lims.interfaces import IContact
from dependencies.dependency import implements
from lims.utils import isActive

schema = Person.schema.copy() + Schema((
    LinesField('PublicationPreference',
        vocabulary = PUBLICATION_PREFS,
        schemata = 'Publication preference',
        widget = MultiSelectionWidget(
            label=_("Publication preference"),
        ),
    ),
    BooleanField('AttachmentsPermitted',
        default = False,
        schemata = 'Publication preference',
        widget = BooleanWidget(
            label=_("Results attachments permitted"),
            description = _(
                "File attachments to results, e.g. microscope "
                "photos, will be included in emails to recipients "
                "if this option is enabled")
        ),
    ),
    ReferenceField('CCContact',
        schemata = 'Publication preference',
        vocabulary = 'getContacts',
        multiValued = 1,
        allowed_types = ('Contact',),
        relationship = 'ContactContact',
        widget = ReferenceWidget(
            checkbox_bound = 0,
            label=_("Contacts to CC"),
        ),
    ),
))

schema['JobTitle'].schemata = 'default'
schema['Department'].schemata = 'default'
# Don't make title required - it will be computed from the Person's Fullname
schema['title'].required = 0
schema['title'].widget.visible = False
schema.moveField('CCContact', before='AttachmentsPermitted')

class Contact(Person):
    implements(IContact)
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def Title(self):
        """ Return the contact's Fullname as title """
        return safe_unicode(self.getFullname()).encode('utf-8')

    security.declareProtected(ManageClients, 'hasUser')
    def hasUser(self):
        """ check if contact has user """
        return self.portal_membership.getMemberById(
            self.getUsername()) is not None

    def getContacts(self, dl=True):
        pairs = []
        objects = []
        for contact in self.aq_parent.objectValues('Contact'):
            if isActive(contact) and contact.UID() != self.UID():
                pairs.append((contact.UID(), contact.Title()))
                if not dl:
                    objects.append(contact)
        pairs.sort(lambda x, y: cmp(x[1].lower(), y[1].lower()))
        return dl and DisplayList(pairs) or objects

    def getParentUID(self):
        return self.aq_parent.UID();

atapi.registerType(Contact, PROJECTNAME)
