import info

class subinfo( info.infoclass ):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = "[git]kde:calligra"
        
        self.defaultTarget = 'gitHEAD'
        self.shortDescription = "The Calligra Suite of Applications"

    def setDependencies( self ):
        self.buildDependencies['kdesupport/eigen3'] = 'default'
        self.buildDependencies['win32libs/glew'] = 'default'
        self.buildDependencies['win32libs/boost-headers'] = 'default'
        self.buildDependencies['win32libs/boost-system'] = 'default'
        self.dependencies['win32libs/lcms2'] = 'default'
        self.dependencies['qt-libs/poppler'] = 'default'
        self.dependencies['kdesupport/qca'] = 'default'
        self.dependencies['win32libs/gsl'] = 'default'
        self.dependencies['win32libs/libwpg'] = 'default'
        self.dependencies['win32libs/libwpd'] = 'default'
        self.dependencies['win32libs/libgit2'] = 'default'
        self.dependencies['win32libs/exiv2'] = 'default'
        self.dependencies['win32libs/openjpeg'] = 'default'
        #self.dependencies['playground/kreport'] = 'default'
        #self.dependencies['playground/kproperty'] = 'default'
        self.dependencies['frameworks/kdelibs4support'] = 'default'
        #self.dependencies['playground/kdb'] = 'default'
        self.dependencies['win32libs/icu'] = 'default'
        self.dependencies['win32libs/vc'] = 'default'
        self.dependencies['frameworks/kf5calendarcore'] = 'default'
        self.dependencies['frameworks/kf5contacts'] = 'default'
        self.dependencies['frameworks/kf5akonadicontact'] = 'default'
        self.dependencies['frameworks/kf5akonadi'] = 'default'
        self.dependencies['kde/okular'] = 'default'
        self.dependencies['unmaintained/openexr'] = 'default'
#		self.dependencies['frameworks/'] = 'default'
		#self.dependencies['win32libs/pstoedit'] = 'default'
#        self.dependencies['win32libs/libfftw'] = 'default'

from Package.CMakePackageBase import *

class Package( CMakePackageBase ):
    def __init__( self ):
        CMakePackageBase.__init__( self )
        defines = ""
        defines += "-DBUILD_doc=OFF "
        defines += "-DMEMORY_LEAK_TRACKER=OFF"

        self.subinfo.options.configure.defines = defines
