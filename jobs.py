import random

def create_job_file(src,dest,new_files_dict):
    create_mkdir_jobs(src,dest,new_files_dict)
    create_copy_jobs(src,dest,new_files_dict)


def create_mkdir_jobs(src,dest,new_files_dict):
    with open(src+"/mkdirjobs.jb","w+") as mkdir_job:
        for key in new_files_dict:
            date = new_files_dict[key][1].replace(':',"/")
            dirpath = "mkdir -p " + dest + "/" + date + "\n"
            mkdir_job.write(dirpath)
    mkdir_job.close()
    
def create_copy_jobs(src,dest,new_files_dict):
    with open(src+"/copyjobs.jb","w+") as copy_job:
        for key in new_files_dict:
            src_path = new_files_dict[key][0]
            date = new_files_dict[key][1].replace(':',"/")
            dest_filename = dest + "/" + date + "/" + str(random.randint(1,1000000000)) + "." + src_path.split(".")[-1] 
            cpstr = "cp " + src_path + " " + dest_filename + "\n"
            copy_job.write(cpstr)
    copy_job.close()

