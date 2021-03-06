# -*- coding: utf-8 -*-
import info


class subinfo(info.infoclass):
    def setDependencies( self ):
        self.buildDependencies['dev-util/extra-cmake-modules'] = 'default'
        self.dependencies['win32libs/libxslt'] = 'default'
        self.dependencies['libs/qtbase'] = 'default'
        self.dependencies['win32libs/sqlite'] = 'default'
        self.dependencies['win32libs/shared-mime-info'] = 'default'

    def setTargets( self ):
        #self.patchToApply['gitHEAD'] = [("akonadi-kde.conf-fix-1.10.80.diff", 1)]

        self.svnTargets['gitHEAD'] = '[git]kde:akonadi.git'
        self.shortDescription = "a storage service for PIM data and meta data"
        self.defaultTarget = 'gitHEAD'

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self ):
        CMakePackageBase.__init__( self )
        self.subinfo.options.configure.defines = ""
        if self.subinfo.options.features.akonadiBackendSqlite:
            self.subinfo.options.configure.defines += (
                    " -DINSTALL_QSQLITE_IN_QT_PREFIX=TRUE"
                    " -DDATABASE_BACKEND=SQLITE " )


