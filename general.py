import os
# Each website Crawled is different project
#i am going to have a lot of shared functions in here

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project '+directory)
        os.makedirs(directory)


# Creating data files(files that go into project directory)

# multithreaded crawler(spes)

#create queue and crawled files(if not created)

def created_data_files(project_name,base_url):
    queue= project_name+'/queue.txt'
    crawled=project_name+'/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')


#create a new file

def write_file(path, data):
    f=open(path, 'w')
    f.write(data)
    f.close()

#created_data_files('spidercrawl','https://coolchand5725.com')

#writing data to an existing file

def append_to_file(path,data):
    f=open(path,'a')
    f.write(data+'\n')
    f.close()

#clearing the files(contents)

def delete_file_content(path):
    f=open(path,'w')
    pass

def file_to_set(file_name):
    results=set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

def set_to_file(links,file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file,link)
        
