import info

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = 'git://github.com/KDAB/GammaRay.git'
        self.defaultTarget = 'gitHEAD'

    def setDependencies( self ):
        self.shortDescription = "GammaRay is a tool to poke around in a Qt-application and also to manipulate the application to some extent"
        self.dependencies['libs/qt'] = 'default'
        #self.dependencies['testing/vtk'] = 'default'
        self.buildDependencies['virtual/base'] = 'default'

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__( self ):
        CMakePackageBase.__init__( self )
        self.subinfo.options.configure.defines = "-DGIT_EXECUTABLE=%s" % os.path.join(EmergeStandardDirs.emergeRoot(),"dev-utils","git","bin","git.exe").replace("\\","/")

