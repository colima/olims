from dependencies.dependency import DateTime
from dependencies.dependency import REFERENCE_CATALOG
from dependencies.dependency import WorkflowException
from dependencies.dependency import getToolByName
from lims import bikaMessageFactory as _
from lims.utils import t
from lims import logger
from lims.subscribers import skip
from lims.subscribers import doActionFor
# import App Plone/buildout-cache/eggs/Zope2-2.13.22-py2.7.egg/App
from dependencies import transaction

def AfterTransitionEventHandler(instance, event):

    # creation doesn't have a 'transition'
    if not event.transition:
        return

    debug_mode = True #App.config.getConfiguration().debug_mode "Commented by Yasir"
    if not debug_mode:
        return

    if not skip(instance, event.transition.id, peek=True):
        logger.debug("Started transition %s on %s" %
                    (event.transition.id, instance))
##    else:
##        logger.info("Ignored transition %s on %s" %
##                    (event.transition.id, instance))
