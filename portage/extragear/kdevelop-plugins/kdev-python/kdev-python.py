import info

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.svnTargets['5.0'] = '[git]kde:kdev-python|5.0|'
        self.defaultTarget = '5.0'

    def setDependencies( self ):
        self.shortDescription = "python support for kdevelop"
        self.buildDependencies['virtual/base'] = 'default'
        self.dependencies['extragear/kdevplatform'] = 'default'
        self.dependencies['binary/python-libs'] = 'default'

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__( self ):
        CMakePackageBase.__init__( self )

