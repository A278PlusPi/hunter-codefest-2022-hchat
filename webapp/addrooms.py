import json
import os
from textwrap import indent

# highest num is 86597
classNum = 86597      
# need to load all directories into list
REL_PATH = 'src/components/CUNY-CLASSES-JSON/'
dir = os.listdir(REL_PATH)

def createJson(school, key, major, desc):
    return {"school": school, "major": major, "room_num": key, "room_desc": desc}
def createsmalljson(key, major, desc):
    return {"major": major, "room_num": str(key), "room_desc": desc}

    
# then append to every directory
for s in dir:
    print(s)
    school = s
    file = open(REL_PATH+s+"/"+school+".json", "w")
    # add new object to each one
    """ 
    major: school
    room_num: count+1
    room_desc: school
    """
    schoolJsonObj = createsmalljson(classNum+1, school, school)
    classNum+=1
    json.dump(schoolJsonObj, file, indent=4)
    file.close()
    _PATHS = open(REL_PATH+school+"/"+"_PATHS.json", "r")
    data = json.load(_PATHS)
    _PATHS.close()
    data.append({"name": school, "path": (school + ".json")})
    _PATHS.close()
    _PATHS_write = open(REL_PATH+school+"/"+"_PATHS.json", "w")
    json.dump(data, _PATHS_write, indent=4)
    _PATHS_write.close()
    # modify _PATHS json in each dir to contain the new paths to those jsons
    # create new json in every directory with one object filename school.json
    """ 
    major: room
    room_num: count+1
    room_desc: room
    """
    list = os.listdir(REL_PATH+school)
    for f in list:
        print("file is " + (REL_PATH+school+"/"+f))
        major_file_read = open(REL_PATH+school+"/"+f, "r")
        major = f.strip(".json")
        if (major == "_PATHS" or major == school):
            major_file_read.close()
            continue
        majorJsonObj = createsmalljson(classNum+1, major, major)
        classNum += 1
        majorJson = json.load(major_file_read)
        majorJson.append(majorJsonObj)
        major_file_read.close()
        
        major_file_write = open(REL_PATH+school+"/"+f, "w")
        
        json.dump(majorJson, major_file_write, indent=4)
        major_file_write.close()

# in react
# modify code somewhere to read new rooms as chatrooms instead of lists
# modify roomlist component to give different class for school/major rooms
# set school/major rooms to first element with flex property order: 1;
# modify roomlist component to give chatrooms bold font weight


