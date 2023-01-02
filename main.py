#
#
#

import subprocess
import argparse

DEFAULT_APP_NAME = 'test'

def create_react_spa (app_name):
    # create react application
    subprocess.run(f"npx create-react-app {app_name}", shell=True)
    
    # # copy app-shell code
    subprocess.run(f'wsl cp -r template-files/react/src/. {app_name}/src', shell=True)

    # # copy dockerfile
    subprocess.run(f'wsl cp template-files/react/* {app_name}', shell=True)

    # # copy operation code
    subprocess.run(f'wsl cp -r template-files/react/ops/. {app_name}/ops', shell=True)

    # # install routing dependency
    subprocess.run(f'npm install --save react-router-dom', shell=True, cwd=app_name)


if __name__ == "__main__":
    # get arguments
    parser = argparse.ArgumentParser( )
    parser.add_argument( '-name', '--app_name',  type=str,  dest='app_name', default=DEFAULT_APP_NAME, )

    parsed_args = parser.parse_args( )
    parsed_args.app_name

    create_react_spa(parsed_args.app_name)

    