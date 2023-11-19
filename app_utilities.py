import os
import ruamel.yaml

# Creates a folder anywhere in the chalgen-online folder, paths deeper must be specified
def create_folder(name):
    current_directory = os.getcwd()
    new_folder_path = os.path.join(current_directory, name)
    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)
    else:
        print("CRITICAL: Folder path already exists")

# Creates a file anywhere in the chalgen-online folder, paths deeper must be specified
def create_file(name,text):
    current_directory = os.getcwd()
    new_folder_path = os.path.join(current_directory, name)
    with open(new_folder_path,'w') as file:
        # If theres text write it, if not just put nothing in it
        if (text):
            file.write(text)
        else:
            pass

# Creates a file anywhere in the chalgen-online folder, paths deeper must be specified
def create_yaml(name,data):
    yaml = ruamel.yaml.YAML()
    yaml.indent(offset=2)

    with open(name, 'w') as yaml_file:
        yaml.dump(data, yaml_file)

def folder_occupied(path):
    current_directory = os.getcwd()
    dir = os.listdir(os.path.join(current_directory,"competitions"))
    if len(dir) == 0:
        return False
    else:
        return True

def create_empty_comp(name,author,skill,description):
    comp_dir = os.path.join('competitions', name)
    create_folder(comp_dir)
    create_folder(os.path.join(comp_dir,"chals"))

    text = f"""# Welcome to CTFg!

## {name}

Author: {author}, Competition difficulty: {skill}

## Challenge Description: 
{description}

Competition generated using CHALGEN-Online - Created by Agneya Tharun
"""

    create_file(os.path.join('competitions',name,'Home.md'),text)
    data = {
        'entrypoint': ['Fesbuc'],
        'admin_email': 'admin@admin.com',
        'admin_password': 'ctfgadministrator',
        'homepage': 'Home.md'
    }
    create_yaml(os.path.join('competitions',name,'config.yaml'),data)
