import info


class subinfo(info.infoclass):
    def setTargets( self ):
        
        self.shortDescription = 'some toy apps & games'
        self.defaultTarget = 'gitHEAD'

    def setDependencies( self ):
#        self.dependencies['kde/amor'] = 'default'
        self.dependencies['kde/kteatime'] = 'default'
        self.dependencies['kde/ktux'] = 'default'

from Package.VirtualPackageBase import *

class Package( VirtualPackageBase ):
    def __init__( self ):
        VirtualPackageBase.__init__( self )

