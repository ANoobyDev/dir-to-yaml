import os, yaml

dir_init="test"                      # The dir to convert to yaml
yaml_pos="test/.list.yml"            # The yaml file

def pathto_dict(path):
    file_token = ''
    for root, dirs, files in os.walk(path):
        if "." in dirs:
            pass
        else:
            tree = {dir: pathto_dict(os.path.join(root, dir)) for dir in dirs}
            print("ree")
            print(tree)
            return tree

# End of program
with open(f"{yaml_pos}", "w") as f:
    yaml.dump(pathto_dict("test"), f)
    f.close()
