import os
import ruamel.yaml
import json

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

def list_all_comps():
    current_directory = os.getcwd()
    dir = os.listdir(os.path.join(current_directory,"competitions"))
    return dir

def retrieve_first_comp():
    return list_all_comps()[0]

def extract_text(dir,filename):
    current_directory = os.getcwd()
    with open(os.path.join(current_directory,dir,filename),'r') as file:
        contents = file.read()
    return contents

def overwrite_file(dir,text):
    current_directory = os.getcwd()
    if (os.path.exists(os.path.join(current_directory,dir))):
        os.remove(os.path.join(current_directory,dir))
    else:
        pass
    create_file(os.path.join(current_directory,dir),text)

def get_all_environments():
    with open(os.path.join(os.getcwd(),'usable_chals.json'),'r') as file:
        data = json.load(file)
    return data['environments']

def get_environments(comp_name):
    directory = os.path.join(os.getcwd(),'competitions',comp_name,'chals')

    all_environments = get_all_environments()
    
    all_folders = [item for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item))]

    existing_environments = []
    
    for folder in all_folders:
        if folder in all_environments:
            existing_environments.append(folder)
    
    return existing_environments

print(get_environments('mcpshsf2024'))

# print(extract_text('competitions'+'/KhetarKoinCompetition','Home.md'))