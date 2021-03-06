# -*- coding: utf-8 -*-
import info
import portage

class subinfo(info.infoclass):
    def setTargets( self ):
        self.versionInfo.setDefaultValues()
        self.targetDigests['3.7.0'] = 'b61362b409bb7909a6d11097b5f69fded061073c'
        
        for ver in self.svnTargets.keys() | self.targets.keys():
            self.patchToApply[ ver ] = [("fix_shortpath.patch", 1)]

    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'
        self.dependencies['dev-util/llvm'] = 'default'

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self, **args ):
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.defines = " -DPYTHON_EXECUTABLE=%s/python.exe" % emergeSettings.get("Paths","PYTHON","").replace("\\","/")

    def configureOptions(self, defines=""):
        options = CMakePackageBase.configureOptions(self, defines)
        if self.buildType().startswith("Rel"):
            # forcing build in Release mode, RelWithDebInfo would take lots of disk space and memory during link
            options += ' -DCMAKE_BUILD_TYPE=Release'
        return options