import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'

    def setTargets( self ):
        self.targets['0.0.1'] = 'http://www.kdab.com/~andy/setupdll.zip'
        self.svnTargets['gitHEAD'] = "[git]kde:scratch/aholzammer/setupdll.git"
        self.targetConfigurePath['0.0.1'] = 'setupdll'
        self.defaultTarget = 'gitHEAD'


class Package(CMakePackageBase):
    def __init__( self, **args ):
        CMakePackageBase.__init__( self )

