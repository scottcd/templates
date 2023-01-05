# file:         generate_template.py
# author:       Chandler Scott
# updated:      01/03/22
# description:  generate a template application

import os
import subprocess
import argparse

DEFAULT_APP_TYPE = 'react'
DEFAULT_PRIMARY_BACKGROUND_COLOR = '#FFF'
DEFAULT_SECONDARY_BACKGROUND_COLOR = '#282c34'
DEFAULT_PRIMARY_TEXT_COLOR = '#000'
DEFAULT_SECONDARY_TEXT_COLOR = '#FFF'
DEFAULT_HIGHLIGHT_COLOR = '#add8e6'


def os_check(): return 'wsl' if os.name == 'nt' else ''


def create_color_scheme(app_name, colors):

    primary_background = colors.get('primary_background')
    secondary_background = colors.get('secondary_background')
    primary_text = colors.get('primary_text')
    secondary_text = colors.get('secondary_text')
    highlight_color = colors.get('highlight_color')

    color_file = ('export const COLORS = {\n'
        f'\tprimaryBackground: "{primary_background}",\n'
        f'\tsecondaryBackground: "{secondary_background}",\n'
        f'\tprimaryText: "{primary_text}",\n'
        f'\tsecondaryText: "{secondary_text}",\n'
        f'\thighlightColor: "{highlight_color}"\n'
        '}'
    )

    subprocess.run(f"{os_check()} mkdir {app_name}/react-spa/src/values", shell=True)

    f = open(f"{app_name}/react-spa/src/values/colors.js", "w+")
    f.write(color_file)


def create_react_spa(app_name, colors):
    subprocess.run(f"{os_check()} mkdir {app_name}", shell=True)
    subprocess.run(f"npx create-react-app {app_name}/react-spa", shell=True)
    # create react application
    subprocess.run(f"npx create-react-app {app_name}/react-spa", shell=True)

    # copy the following:
    # - dockerfile
    # - deploy scripts
    # - app-shell
    # - app-shell components
    # - app-shell placeholder views
    # - package.json and package-lock.json
    subprocess.run(
        f'{os_check()} cp -r template-files/react/. {app_name}/react-spa', shell=True)

    subprocess.run(f"{os_check()} mkdir {app_name}/nginx", shell=True)
    subprocess.run(
        f'{os_check()} cp -r template-files/nginx/. {app_name}/nginx', shell=True)
    subprocess.run(
        f'{os_check()} cp -r template-files/docker-compose.yml {app_name}', shell=True)
    # add in custom color scheme
    create_color_scheme(app_name, colors)

    # remove unused files
    unused_files = 'App.test.js logo.svg reportWebVitals.js setupTests.js'
    subprocess.run(f'{os_check()} rm {unused_files}',
                   shell=True, cwd=(app_name + '/react-spa/src/'))
    # install routing dependency
    # subprocess.run(f'npm install --save react-router-dom',
    #                shell=True, cwd=app_name)

if __name__ == "__main__":
    # get arguments
    parser = argparse.ArgumentParser(description=('Create an application template.'))
    parser.add_argument('-name', '--app_name',  type=str,
                        dest='app_name', required=True,
                        help='name of application to be created')
    parser.add_argument('-type', '--app_type',  type=str,
                        dest='app_type', default=DEFAULT_APP_TYPE,
                        help='type of application to generate (options: react)')
    parser.add_argument('-bg1', '--primary_background',  type=str,
                        dest='primary_background_color', default=DEFAULT_PRIMARY_BACKGROUND_COLOR,
                        help="color for application's primary background")
    parser.add_argument('-bg2', '--secondary_background',  type=str,
                        dest='secondary_background_color', default=DEFAULT_SECONDARY_BACKGROUND_COLOR, 
                        help="color for application's secondary background")
    parser.add_argument('-t1', '--primary_text',  type=str,
                        dest='primary_text_color', default=DEFAULT_PRIMARY_TEXT_COLOR,
                        help="color for application's primary text")
    parser.add_argument('-t2', '--secondary_text',  type=str,
                        dest='secondary_text_color', default=DEFAULT_SECONDARY_TEXT_COLOR, 
                        help="color for application's secondary text")
    parser.add_argument('-highlight', '--highlight_color',  type=str,
                        dest='highlight_color', default=DEFAULT_HIGHLIGHT_COLOR,
                        help="highlight color for application buttons, pops, etc.")

    parsed_args = parser.parse_args()
    app_name = parsed_args.app_name
    app_type = parsed_args.app_type

    colors = {
        "primary_background": parsed_args.primary_background_color,
        "secondary_background": parsed_args.secondary_background_color,
        "primary_text": parsed_args.primary_text_color,
        "secondary_text": parsed_args.secondary_text_color,
        "highlight_color": parsed_args.highlight_color,
    }

    create_react_spa(app_name, colors)
