# -*- coding: utf-8 -*-
import info
from Package.CMakePackageBase import *

class subinfo(info.infoclass):
    def setTargets( self ):
        for i in ( '0.18.0', '0.18.1', '0.18.2', '0.20.3' ):
            self.targets[ i ] = 'http://poppler.freedesktop.org/poppler-%s.tar.gz' % i
            self.targetInstSrc[ i ] = 'poppler-%s' % i
        self.svnTargets['gitHEAD'] = "git://git.freedesktop.org/git/poppler/poppler|master"
        self.svnTargets['0.18-branch'] = "git://git.freedesktop.org/git/poppler/poppler|poppler-0.18"
        self.svnTargets['0.20-branch'] = "git://git.freedesktop.org/git/poppler/poppler|poppler-0.20"
        self.targetDigests['0.18.2'] = '7ef4eec20e849024c0cdd7a49c428d20eb3de875'
        self.patchToApply["0.18.2"] = [("poppler-0.18.2-20130113.diff",1)]

        self.shortDescription = "PDF rendering library based on xpdf-3.0"
        self.defaultTarget = "0.18.2"

    def setDependencies( self ):
        self.dependencies['win32libs/freetype'] = 'default'
        self.dependencies['win32libs/openjpeg'] = 'default'
        self.dependencies['win32libs/lcms'] = 'default'
        self.dependencies['win32libs/zlib'] = 'default'
        self.dependencies['win32libs/jpeg'] = 'default'
        self.dependencies['win32libs/libpng'] = 'default'
        self.dependencies['win32libs/libxml2'] = 'default'
        self.runtimeDependencies['data/poppler-data'] = 'default'
        self.dependencies['libs/qt'] = 'default'

class Package(CMakePackageBase):
    def __init__( self, **args ):
        self.subinfo = subinfo()
        CMakePackageBase.__init__( self )

        self.subinfo.options.package.packageName = 'poppler'
        self.subinfo.options.configure.defines = "-DBUILD_QT4_TESTS=ON -DENABLE_XPDF_HEADERS=ON"

if __name__ == '__main__':
    Package().execute()
