# -*- coding: utf-8 -*-
# Helper script for substitution of paths, independent of cmd or powershell
# copyright:
# Patrick von Reth <vonreth [AT] kde [DOT] org>

from emerge_config import *
import utils
import subprocess
import argparse


def subst( path, drive ):
    if not os.path.exists( path ):
        os.mkdir( path )
    command = "subst %s %s" % ( emergeSettings.get( "ShortPath", drive ), path)
    subprocess.Popen( command, stdout = subprocess.PIPE )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--subst", action = "store_true")
    parser.add_argument("--get", action = "store_true")
    parser.add_argument("rest", nargs = argparse.REMAINDER)
    args = parser.parse_args()

    if args.subst:
        if utils.varAsBool( emergeSettings.get( "ShortPath", "EMERGE_USE_SHORT_PATH", "False" ) ):
            subst( os.path.abspath( os.path.join( os.path.dirname( sys.argv[ 0 ] ), "..", ".." ) ), "EMERGE_ROOT_DRIVE" )
            subst( emergeSettings.get( "Paths", "DOWNLOADDIR" ), "EMERGE_DOWNLOAD_DRIVE" )
            subst( emergeSettings.get( "Paths", "KDESVNDIR" ), "EMERGE_SVN_DRIVE" )
            subst( emergeSettings.get( "Paths", "KDEGITDIR" ), "EMERGE_GIT_DRIVE" )
            print( emergeSettings.get( "ShortPath", "EMERGE_ROOT_DRIVE" ) )
        else:
            print( emergeRoot( ) )
    if args.get:
        print(emergeSettings.get(args.rest[0],args.rest[1],""))
