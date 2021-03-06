# -*- coding: utf-8 -*-
import info

from Package.CMakePackageBase import *

class subinfo(info.infoclass):
    def setTargets( self ):
        self.svnTargets['svnHEAD'] = "trunk/playground/games#norecursive;trunk/playground/games/kamala#main;trunk/playground/games/cmake"
        self.defaultTarget = 'svnHEAD'

    def setDependencies( self ):
        self.dependencies['win32libs/sqlite'] = 'default'

        self.dependencies['kde/kdegames'] = 'default'
#        self.dependencies['testing/glew'] = 'default'


class Package(CMakePackageBase):
    def __init__( self, **args ):
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.onlyBuildTargets = 'kamala'



