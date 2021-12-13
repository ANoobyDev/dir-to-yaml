import os, yaml

dir_list={}
dir_init="./test/"  
yaml_name=".list.yml"

for pos, dirs, files in os.walk(dir_init):
    for dir in dirs:    
        if '.' in dir:
            pass
        else:
            print(pos)
            print(dir)
    
exit()

# End of program
with open(f"{dir_init}{yaml_name}", "w") as f:
    yaml.dump(dir_list, f)
    f.close()
