import os
import shutil

try:
    with open("sample.txt","r") as file:
        content = file.read()
        print("original File Content:")
        print(content)
    with open("output.txt","w")as file:
        file.write(content)
        file.write("\n this line was added automatically.")
        print("\n content copid to output.txt")
        os.rename("output.txt","new_output.txt")
        print("file renamed to new_output.txt")

        if not os.path.exist("Backup"):
            os.mkdir("Backup")

            shutil.move("new_output.txt","Backup/new_output.txt")
            print("file moved to backup folder")

except FileNotFoundError:
    print("Error:File not found.")
except PermissionError:
    print("Error:permission denied.")
except Exception as e:
    print("Unexpected Error:",e)