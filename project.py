import os
import shutil

# .exe , .msi, .gif, .png, .jep, .csv, .pdf, .xls, .xlsx, .ppt, .pptx., .doc

from_dir = "C:/Users/ultim/Downloads"
to_dir = "C:/Users/ultim/OneDrive/Desktop/BYJU Coding/Class Activities/C102_assets-main"

list_of_files = os.listdir(from_dir)
print(list_of_files)

#Move all image files from downloads folder to another folder
for file_name in list_of_files:
    
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == "":
        continue
    if extension in [".pdf", ".txt", ".doc", ".docx"]:

        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "Document_Files"
        path3 = to_dir + "/" + "Document_Files" + "/" + file_name
        print("path1 ", path1)
        print("path3" , path3)

        # Check if Folder/Directory path exists before Moving
        # Else make a new Folder/Directory Then Move
        
        if os.path.exists(path2):
         print("Moving " + file_name + ".....")

         # Move from path1 ---> path3
         shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)

      
         