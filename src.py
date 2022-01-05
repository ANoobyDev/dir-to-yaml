import os, yaml

dir_init="test"                      # The dir to convert to yaml
yaml_pos="test/.list.yml"            # The yaml file

def dir_to_yaml(path):
    file_token = ''
    for root, dirs, files in os.walk(path):
        tree = {dir: dir_to_yaml(os.path.join(root, dir)) for dir in dirs}
        return tree

# End of program
with open(f"{yaml_pos}", "w") as f:
    yaml.dump(dir_to_yaml(dir_init), f)
    f.close()
