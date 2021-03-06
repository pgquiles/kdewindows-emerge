import EmergeDebug
import info


class subinfo(info.infoclass):
    def setTargets( self ):
        self.versionInfo.setDefaultValues( )

        self.shortDescription = "Scripts and data for building API documentation (dox) in a standard format and style."
        

    def setDependencies( self ):
        self.buildDependencies["virtual/base"] = "default"
        self.buildDependencies["dev-util/cmake"] = "default"
        self.runtimeDependencies["dev-util/doxygen"] = "default"
        self.runtimeDependencies["python/pyyaml"] = "default"
        self.runtimeDependencies["python/jinja2"] = "default"
        self.runtimeDependencies["python/doxyqml"] = "default"

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__( self ):
        CMakePackageBase.__init__( self )        
        # this program needs python 2.7
        self.subinfo.options.configure.defines = " -DPYTHON_EXECUTABLE=%s/python.exe" % emergeSettings.get("Paths","PYTHON27","").replace("\\","/")
        
    
    def configure(self):
        if not ("Paths","Python27") in emergeSettings:
            EmergeDebug.die("Please make sure Paths/Python27 is set in your kdesettings.ini")
        return CMakeBuildSystem.configure(self)


    
    def install(self):
        python = os.path.join(emergeSettings.get("Paths","PYTHON27"), "python")
        os.makedirs(os.path.join(self.imageDir(), "bin"))
        for script in ["depdiagram-generate", "depdiagram-prepare", "kgenapidox", "kgenframeworksapidox"]:
            utils.createBat(os.path.join(self.imageDir(), "bin", "%s.bat" % script),
                            "%s %s %%*" % (python, os.path.join(EmergeStandardDirs.emergeRoot( ), "scripts", script)))
        return CMakeBuildSystem.install(self)
