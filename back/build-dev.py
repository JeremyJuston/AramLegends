import os
import subprocess
import time

CURRENT_DIRECTORY = os.getcwd()
directories = os.listdir(CURRENT_DIRECTORY)
NON_ANGULAR_DIRS = ['static', 'templates', 'back', 'api']


for directory in directories:
    if "." not in directory and directory not in NON_ANGULAR_DIRS:
        ANGULAR_PROJECT_PATH = os.path.join(CURRENT_DIRECTORY, directory)
        DIST_PATH = os.path.join(ANGULAR_PROJECT_PATH, 'dist', directory)

FLASK_STATIC_PATH = os.path.join(CURRENT_DIRECTORY, 'static')
FLASK_TEMPLATES_PATH = os.path.join(CURRENT_DIRECTORY, 'templates')

subprocess.Popen(('cd ' + ANGULAR_PROJECT_PATH + ' && ng build --watch --base-href /static/ &'), shell=True)


dir_exists = True

while dir_exists:
    
    try:
        files = os.listdir(DIST_PATH)
        static_files = []
        html_files = []
        
        for file in files:
            
            if '.js' in file or '.js.map' in file or '.ico' in file:
                static_files.append(file)
            
            if '.html' in file:
                html_files.append(file)
        
        if len(static_files) > 0:
            prev_static_files = os.listdir(FLASK_STATIC_PATH)
            print(prev_static_files)
            
            #for prev_file in prev_static_files:
                #subprocess.call(('del ' + FLASK_STATIC_PATH + '\\' + prev_file), shell=True)

            for static_file in static_files:
                subprocess.call(('cd ' + DIST_PATH + ' &&' + ' move ' + static_file + ' ' + FLASK_STATIC_PATH), shell=True)
        
        if len(html_files) > 0:
            prev_templates_files = os.listdir(FLASK_TEMPLATES_PATH)
            
            #for prev_file in prev_templates_files:
                #subprocess.call(('del ' + FLASK_TEMPLATES_PATH + '\\' + prev_file), shell=True)

            for html_file in html_files:
                subprocess.call(('cd ' + DIST_PATH + ' &&' + ' move ' + html_file + ' ' + FLASK_TEMPLATES_PATH), shell=True)
    
    except Exception as e:
        dir_exists = False
        print(e)
    time.sleep(10.0)
