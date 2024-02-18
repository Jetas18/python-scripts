import os

dir_names = ["Images", "Archives", "Docs", "Others", "iso", "texts", "binaries_and_folders"]



chunk_main = os.listdir()



for i in dir_names:
    if i in chunk_main:
        chunk_main.remove(i)

binaries = []
images = []
archives = []
docs = []
others = []
isos = []
texts = []

def move_files(dir_name, files): 
    for j in files:
         os.system(f"mv \"{j}\" {dir_name}/\"{j}\"")

def create_dir(name):
    if not os.path.exists(name):
        os.mkdir(name)


arrays = [images, archives, docs, others, isos,  texts, binaries]


for i in dir_names:
    create_dir(i)


for i in chunk_main:
    if i.endswith(".jpg") or i.endswith(".png") or i.endswith(".webp") or i.endswith(".jpeg"):
        images.append(i)
    elif i.endswith(".py") :
        continue
    elif i.endswith(".gz") or i.endswith(".xz") or i.endswith(".zip"):
        archives.append(i)
    elif i.endswith(".pdf") or i.endswith(".epub"):
        docs.append(i)
       
    elif i.endswith(".AppImage") or i.endswith(".bin") or i.endswith(".run") or not(i.__contains__(".")):
        binaries.append(i)


    elif i.endswith(".txt"):
        texts.append(i)


    elif i.endswith(".iso"):
        isos.append(i)
    else:
        others.append(i)





for i, j in zip(dir_names, arrays):
    move_files(i, j)


