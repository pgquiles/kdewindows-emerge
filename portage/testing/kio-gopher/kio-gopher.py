# -*- coding: utf-8 -*-
import info
from Package.CMakePackageBase import *

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = '[git]kde:kio-gopher.git'
        self.defaultTarget = 'gitHEAD'
        self.shortDescription = "Gopher kioslave"

    def setDependencies( self ):
        self.dependencies['kde/kdelibs'] = 'default'

class Package(CMakePackageBase):
    def __init__( self, **args ):
        CMakePackageBase.__init__(self)

