import os
import yaml

wahere_cd=""
dir_init="./test"

for dirs in os.listdir(dir_pos):
    print(dirs)
    ans=os.path.isfile(f"{dir_init}/{dirs}")
    print(f"{ans}\n")
    
exit()
# End of program
with open(f"{dir_init}/.list.yml", "w") as f:
    yaml.dump(dir_list, f)
    f.close()
