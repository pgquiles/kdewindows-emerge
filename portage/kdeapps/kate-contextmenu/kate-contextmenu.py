import info

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = '[git]kde:scratch/sengels/kate-context-menu'
        self.defaultTarget = 'gitHEAD'
        
        self.shortDescription = "a context menu for kate inside the windows explorer"

    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__( self ):
        CMakePackageBase.__init__( self )

