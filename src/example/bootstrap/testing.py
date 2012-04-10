from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class ExampleBootstrap(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import example.bootstrap
        xmlconfig.file('configure.zcml',
                       example.bootstrap,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'example.bootstrap:default')

EXAMPLE_BOOTSTRAP_FIXTURE = ExampleBootstrap()
EXAMPLE_BOOTSTRAP_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(EXAMPLE_BOOTSTRAP_FIXTURE, ),
                       name="ExampleBootstrap:Integration")