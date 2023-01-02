#
#
#

import os
import subprocess
import argparse

DEFAULT_APP_NAME =  os.getcwd()

if __name__ == "__main__":
    # get arguments
    parser = argparse.ArgumentParser( )
    parser.add_argument( '-name', '--app_name',  type=str,  dest='app_name', default=DEFAULT_APP_NAME, )

    parsed_args = parser.parse_args( )
    app_name = parsed_args.app_name

    subprocess.run(f'docker stop {app_name}', shell=True, cwd=app_name)

    