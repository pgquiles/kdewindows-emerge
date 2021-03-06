# -*- coding: utf-8 -*-
import os

import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets( self ):
        self.svnTargets['gitHEAD'] = '[git]kde:kdeconnect-kde'
        self.defaultTarget = 'gitHEAD'
        self.shortDescription = "KDE Connect adds communication between KDE and your smartphone"


    def setDependencies( self ):
        self.buildDependencies["dev-util/extra-cmake-modules"] = "default"
        self.dependencies['libs/qtbase'] = 'default'
        self.dependencies['libs/qtquick1'] = 'default'
        self.dependencies['kdesupport/qca'] = 'default'
        self.dependencies['frameworks/ki18n'] = 'default'
        self.dependencies['frameworks/kconfigwidgets'] = 'default'
        self.dependencies['frameworks/kdbusaddons'] = 'default'
        self.dependencies['frameworks/kiconthemes'] = 'default'
        self.dependencies['frameworks/knotifications'] = 'default'
        #self.dependencies['qt-libs/snorenotify'] = 'default'
        self.dependencies['frameworks/kcmutils'] = 'default'


class Package( CMakePackageBase ):
    def __init__( self, **args ):
        CMakePackageBase.__init__(self)
