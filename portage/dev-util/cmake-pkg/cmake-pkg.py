# -*- coding: utf-8 -*-
import info

class subinfo(info.infoclass):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = "git://cmake.org/cmake.git"        
        self.svnTargets['release'] = "git://cmake.org/cmake.git|release|"
        self.svnTargets['v2.8.2'] = "git://cmake.org/cmake.git|release|v2.8.2"
        for ver in ['2.8.0', '2.8.1', '2.8.2', '2.8.3', '2.8.8','2.8.10.2','2.8.11']:
            self.targets[ ver ] = "http://www.cmake.org/files/v2.8/cmake-" + ver + ".tar.gz"
            self.targetInstSrc[ ver ] = "cmake-" + ver
        self.patchToApply['2.8.0'] = ("cmake-2.8.0-20100512.diff", 1)
        self.patchToApply['2.8.1'] = ("cmake-2.8.1-20100511.diff", 1)
        self.patchToApply['2.8.3'] = ("cmake-2.8.3-20101222.diff", 1)
        self.patchToApply['2.8.8'] = ("cmake-2.8.3-20101222.diff", 1)
        self.patchToApply['2.8.10.2'] = ("cmake-2.8.10.diff", 1)
        self.patchToApply['2.8.11'] = ("cmake-2.8.10.diff", 1)
        self.patchToApply['release'] = ("0001-windows-fix.patch", 1)
        self.targetDigests['2.8.10.2'] = '2d868ccc3f9f2aa7c2844bd0a4609d5313edaaec'
        self.targetDigests['2.8.11'] = '7b7961402ec71d84052734da1bed2b28e6a2c4af'
        self.defaultTarget = '2.8.11'

    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self):
        CMakePackageBase.__init__(self)
        self.subinfo.options.merge.destinationPath = "dev-utils"
        self.subinfo.options.configure.defines = "-DKWSYS_INSTALL_LIB_DIR=lib -DKWSYS_INSTALL_INCLUDE_DIR=include"
