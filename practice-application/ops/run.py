#
#
#

import os
import subprocess
import argparse

DEFAULT_APP_NAME =  os.path.basename(os.getcwd())

if __name__ == "__main__":
    # get arguments
    parser = argparse.ArgumentParser( )
    parser.add_argument( '-name', '--app_name',  type=str,  dest='app_name', default=DEFAULT_APP_NAME, )

    parsed_args = parser.parse_args( )
    app_name = parsed_args.app_name

    subprocess.run(f'docker run --rm -d -p 80:80 -t {app_name} {app_name}', shell=True)

    