def photoupload(file_name):
    print(file_name)
    with open("teacher/static/prof_imgs/"+file_name.name,"wb+") as dest:
        for i in file_name.chunks():
            dest.write(i)
    print("File Written")