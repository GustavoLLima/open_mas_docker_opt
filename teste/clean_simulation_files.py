import os
import glob
import time

if __name__ == '__main__':
    files_to_delete = [
        "/teste/important/m1_output.txt",
        "/teste/important/m1_alive.txt",
        "/teste/important/m2_output.txt",
        "/teste/important/m2_alive.txt"
    ]

    file_path = "/teste/jacamo/integra_gold_miners/src/agt/list/"
    
    for clean_up in glob.glob(file_path+'*.*'):
        if not clean_up.endswith('.gitkeep'):
            files_to_delete.append(clean_up)

    for filename in files_to_delete:
        if os.path.exists(filename):
            print("Deleting file: "+filename)
            os.remove(filename)
        else:
            print(filename + " does not exists")

    # filename = "/teste/important/m1_output.txt"
    # if os.path.exists(filename):
    #     print("Deleting file: "+filename)
    #     os.remove(filename)
    # else:
    #     print(filename + " does not exists")

    # filename = "/teste/important/m1_alive.txt"
    # if os.path.exists(filename):
    #     print("Deleting file: "+filename)
    #     os.remove(filename)
    # else:
    #     print(filename + " does not exists")

    # filename = "/teste/important/m2_output.txt"
    # if os.path.exists(filename):
    #     print("Deleting file: "+filename)
    #     os.remove(filename)
    # else:
    #     print(filename + " does not exists")

    # filename = "/teste/important/m2_alive.txt"
    # if os.path.exists(filename):
    #     print("Deleting file: "+filename)
    #     os.remove(filename)
    # else:
    #     print(filename + " does not exists")


    # filename = "/teste/important/errors.txt"
    # if os.path.exists(filename):
    #     print("Deleting file: "+filename)
    #     os.remove(filename)
    # else:
    #     print(filename + " does not exists")


    # file_path = "/teste/jacamo/integra_gold_miners/src/agt/list/"
    # for clean_up in glob.glob(file_path+'*.*'):
    #     #print(clean_up)
    #     if not clean_up.endswith('.gitkeep'):
    #         print("Deleting file: "+clean_up) 
    #         os.remove(clean_up)
