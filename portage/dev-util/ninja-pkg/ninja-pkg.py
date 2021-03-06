# -*- coding: utf-8 -*-
import os

import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets( self ):
        """ """
        self.svnTargets['gitHEAD'] = "git://github.com/martine/ninja.git"
        for ver in ["1.6.0" ]:
            self.targets[ ver ] = "https://github.com/martine/ninja/archive/v%s.tar.gz" % ver
            self.targetInstSrc[ ver ] = "ninja-%s" % ver
            self.archiveNames[ ver] = "ninja-%s.tar.gz" % ver

        if compiler.isMSVC2015():
            self.defaultTarget = 'gitHEAD'
        else:
            self.defaultTarget = ver
        self.targetDigests['1.6.0'] = 'a6ff055691f6d355234298c21cc18961b4ca2ed9'

    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'

class Package(CMakePackageBase):
    def __init__( self, **args ):
        CMakePackageBase.__init__( self )
        self.subinfo.options.merge.destinationPath = "dev-utils"

    def configure(self):
        return True
        
    def make(self):
        self.enterSourceDir()
        command = "python configure.py --bootstrap"
        if compiler.isMinGW():
            command += " --platform=mingw"
        print(command)
        return self.system( command, "make" )
        
    def install(self):
        utils.copyFile(os.path.join(self.sourceDir(),"ninja.exe"),os.path.join(self.imageDir(),"bin","ninja.exe"))
        return True
        
