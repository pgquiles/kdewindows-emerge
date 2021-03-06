import os

import info

import utils


class subinfo(info.infoclass):
    def setTargets( self ):
        for ver in ['2.7.2']:
            self.targets[ver] = 'http://www.mpir.org/mpir-' + ver + '.tar.bz2'
            self.targetInstSrc[ver] = "mpir-" + ver
        self.targetDigests['2.7.2'] = 'a285352d4299eb18d4f02a97e3232efab225e174'
        self.targetInstSrc['2.7.2'] = 'mpir-2.7.2'

        self.shortDescription = "Library for arbitrary precision integer arithmetic derived from version 4.2.1 of gmp"
        self.defaultTarget = '2.7.2'

    def setDependencies( self ):
        self.buildDependencies['virtual/base'] = 'default'
        if compiler.isMinGW():
                self.buildDependencies['dev-util/msys'] = 'default'
        else:
                self.buildDependencies['dev-util/yasm'] = 'default'

from Package.AutoToolsPackageBase import *
from Package.MakeFilePackageBase import *

class PackageMinGW(AutoToolsPackageBase):
    def __init__( self, **args ):
        AutoToolsPackageBase.__init__(self)
        abi = "ABI=64"
        if self.buildArchitecture()=="x86":
            abi = "ABI=32"
            self.platform = ""
        self.subinfo.options.configure.defines = "--enable-shared --disable-static --enable-gmpcompat --enable-cxx " + abi

class PackageMSVC(MakeFilePackageBase):
    def __init__( self, **args ):
            MakeFilePackageBase.__init__( self )

    def getBuildSettings( self ):
        build = ""
        toolsetSwitches = ""
        if compiler.isMSVC2012():
            build = "build.vc11"
            toolsetSwitches = "/property:PlatformToolset=v110"
        elif compiler.isMSVC2013():
            build = "build.vc12"
            toolsetSwitches = "/tv:12.0 /property:PlatformToolset=v120"
        elif compiler.isMSVC2015():
            build = "build.vc14"
            toolsetSwitches = "/tv:14.0 /property:PlatformToolset=v140"
        if self.buildType() == "Debug":
            bt = "Debug"
        else:
            bt = "Release"
        return build, bt, toolsetSwitches

    def configure( self ):
        os.putenv('YASMPATH', os.path.join(self.rootdir, 'dev-utils', 'bin'))
        return True

    def make( self ):
        build, bt, toolsetSwitches = self.getBuildSettings();

        return utils.system("msbuild /target:lib_mpir_gc \"%s\" /p:Configuration=%s %s" %
                (os.path.join(self.sourceDir(), build, "mpir.sln"), bt, toolsetSwitches)
        ) and utils.system("msbuild /target:dll_mpir_gc \"%s\" /p:Configuration=%s %s" %
                (os.path.join(self.sourceDir(), build, "mpir.sln"), bt, toolsetSwitches)
        )

    def unittest( self ):
        build, bt, toolsetSwitches = self.getBuildSettings();

        return utils.system("msbuild \"%s\" /p:Configuration=%s %s" %
                (os.path.join(self.sourceDir(), build, "mpir-tests.sln"), bt, toolsetSwitches)
        ) and utils.system(os.path.join("mpir-tests", "run-tests.py"));

    def install( self ):
        if not os.path.isdir( os.path.join( self.installDir() , "bin" ) ):
                os.makedirs( os.path.join( self.installDir() , "bin" ) )
        utils.copyFile(os.path.join( self.sourceDir(), 'dll', 'Win32', 'Release', 'mpir.dll'), os.path.join( self.installDir() , "bin" , "mpir.dll") )
        
        if not os.path.isdir( os.path.join( self.installDir() , "lib" ) ):
                os.makedirs( os.path.join( self.installDir() , "lib" ) )
        utils.copyFile(os.path.join( self.sourceDir(), 'dll', 'Win32', 'Release', 'mpir.lib'), os.path.join( self.installDir() , "lib" , "mpir.lib") )
        # a dirty workaround the fact that FindGMP.cmake will only look for gmp.lib
        utils.copyFile(os.path.join( self.installDir() , "lib" , "mpir.lib"), os.path.join( self.installDir() , "lib" , "gmp.lib") )

        if not os.path.isdir( os.path.join( self.installDir() , "include" ) ):
                os.makedirs( os.path.join( self.installDir() , "include" ) )
        utils.copyFile(os.path.join( self.sourceDir(), 'dll', 'Win32', 'Release', 'gmp.h'), os.path.join( self.installDir() , "include" , "gmp.h") )
        utils.copyFile(os.path.join( self.sourceDir(), 'dll', 'Win32', 'Release', 'gmpxx.h'), os.path.join( self.installDir() , "include" , "gmpxx.h") )
        utils.copyFile(os.path.join( self.sourceDir(), 'dll', 'Win32', 'Release', 'mpir.h'), os.path.join( self.installDir() , "include" , "mpir.h") )
        utils.copyFile(os.path.join( self.sourceDir(), 'dll', 'Win32', 'Release', 'mpirxx.h'), os.path.join( self.installDir() , "include" , "mpirxx.h") )
        utils.copyFile(os.path.join( self.sourceDir(), 'dll', 'Win32', 'Release', 'gmp-mparam.h'), os.path.join( self.installDir() , "include" , "gmp-mparam.h") )
        
        return True

if compiler.isMinGW():
    class Package(PackageMinGW):
        def __init__( self ):
            PackageMinGW.__init__( self )
else:
    class Package(PackageMSVC):
        def __init__( self ):
            PackageMSVC.__init__( self )

