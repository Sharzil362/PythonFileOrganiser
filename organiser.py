import os,shutil,time
location_input=input('Enter the location of the directory you want to organise: ')
modified=''
for count in location_input:
    if count=='\'':
        modified+=count
        modified+='\''
    else:
        modified+=count
modified+='\\'
raw_directory=modified
os.chdir(raw_directory)


for filename in os.listdir(raw_directory):
    directory = raw_directory
    if filename.endswith(".ipynb") or filename.endswith(".py"):
        z = os.path.getctime(filename)
        print(os.path.getmtime(filename))
        if os.path.exists('Programming'):
            pass
        else:
            os.mkdir('Programming')
        if len((time.ctime(z).split(' ')))==5:
            year=(time.ctime(z).split(' '))[4]
        else:
            year=(time.ctime(z).split(' '))[5]
        if year in os.listdir(directory + 'Programming'):
            pass
        else:
            parent_dir = directory + 'Programming'
            path = os.path.join(parent_dir, year)
            os.mkdir(path)
        if (time.ctime(z).split(' '))[1] in os.listdir(directory + 'Programming' + '\\' + year):
            pass
        else:
            parent_dir = directory + 'Programming' + '\\' + year
            path = os.path.join(parent_dir, (time.ctime(z).split(' '))[1])
            os.mkdir(path)
        if filename in os.listdir(raw_directory):
            i=0
            while True:
                if filename in os.listdir(directory + 'Programming'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1]):
                    i += 1
                    os.rename(filename,filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1]))
                    filename=filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1])
                else:
                    shutil.move(directory + filename, directory + 'Programming'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
                    break

        else:
            shutil.move(directory + filename, directory + 'Programming'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        z = os.path.getctime(filename)
        print(time.ctime(z).split(' '))
        if os.path.exists('IMAGES'):
            pass
        else:
            os.mkdir('IMAGES')
        if len((time.ctime(z).split(' ')))==5:
            year=(time.ctime(z).split(' '))[4]
        else:
            year=(time.ctime(z).split(' '))[5]
        if year in os.listdir(directory + 'IMAGES'):
            pass
        else:
            parent_dir = directory +'IMAGES'
            print(parent_dir)
            path = os.path.join(parent_dir,year)
            os.mkdir(path)
        if (time.ctime(z).split(' '))[1] in os.listdir(directory + 'IMAGES'+'\\'+year):
            pass
        else:
            parent_dir = directory + 'IMAGES'+'\\'+year
            path = os.path.join(parent_dir,(time.ctime(z).split(' '))[1])
            os.mkdir(path)
        if filename in os.listdir(raw_directory):
            i=0
            while True:
                if filename in os.listdir(directory + 'IMAGES'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1]):
                    i += 1
                    os.rename(filename,filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1]))
                    filename=filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1])
                else:
                    shutil.move(directory + filename, directory + 'IMAGES'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
                    break

        else:
            shutil.move(directory + filename, directory + 'IMAGES'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
    if filename.endswith(".exe") or filename.endswith(".msi") or filename.endswith(".iso"):
        z = os.path.getctime(filename)
        #month
        if os.path.exists('Software'):
            pass
        else:
            os.mkdir('Software')
        if len((time.ctime(z).split(' ')))==5:
            year=(time.ctime(z).split(' '))[4]
        else:
            year=(time.ctime(z).split(' '))[5]
        if year in os.listdir(directory + 'Software'):
            pass
        else:
            parent_dir = directory + 'Software'
            path = os.path.join(parent_dir,year)
            os.mkdir(path)
        if (time.ctime(z).split(' '))[1] in os.listdir(directory + 'Software'+'\\'+year):
            pass
        else:
            parent_dir = directory + 'Software'+'\\'+year
            path = os.path.join(parent_dir,(time.ctime(z).split(' '))[1])
            os.mkdir(path)
        if filename in os.listdir(raw_directory):
            i=0
            while True:
                if filename in os.listdir(directory + 'Software'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1]):
                    i += 1
                    os.rename(filename,filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1]))
                    filename=filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1])
                else:
                    shutil.move(directory + filename, directory + 'Software'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
                    break

        else:
            shutil.move(directory + filename, directory + 'Software'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
    if filename.endswith(".mkv") or filename.endswith(".mp4"):
        z = os.path.getctime(filename)
        if os.path.exists('Videos'):
            pass
        else:
            os.mkdir('Videos')
        if len((time.ctime(z).split(' ')))==5:
            year=(time.ctime(z).split(' '))[4]
        else:
            year=(time.ctime(z).split(' '))[5]
        if year in os.listdir(directory + 'Videos'):
            pass
        else:
            parent_dir = directory + 'Videos'
            path = os.path.join(parent_dir,year)
            os.mkdir(path)
        if (time.ctime(z).split(' '))[1] in os.listdir(directory + 'Videos'+'\\'+year):
            pass
        else:
            parent_dir = directory + 'Videos'+'\\'+year
            path = os.path.join(parent_dir,(time.ctime(z).split(' '))[1])
            os.mkdir(path)
        if filename in os.listdir(raw_directory):
            i=0
            while True:
                if filename in os.listdir(directory + 'Videos'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1]):
                    i += 1
                    os.rename(filename,filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1]))
                    filename=filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1])
                else:
                    shutil.move(directory + filename, directory + 'Videos'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
                    break

        else:
            shutil.move(directory + filename, directory + 'Videos'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
    if filename.endswith(".pdf"):
        z = os.path.getctime(filename)
        if os.path.exists('PDF'):
            pass
        else:
            os.mkdir('PDF')
        print(len(time.ctime(z).split(' ')))
        #year=''
        if len((time.ctime(z).split(' ')))==5:
            year=(time.ctime(z).split(' '))[4]
        else:
            year=(time.ctime(z).split(' '))[5]
        #print(year)
        if year in os.listdir(directory + 'PDF'):
            pass
        else:
            parent_dir = directory + 'PDF'
            print(parent_dir)
            path = os.path.join(parent_dir,year)
            os.mkdir(path)
        if (time.ctime(z).split(' '))[1] in os.listdir(directory + 'PDF'+'\\'+year):
            pass
        else:
            parent_dir = directory + 'PDF'+'\\'+year
            path = os.path.join(parent_dir,(time.ctime(z).split(' '))[1])
            os.mkdir(path)
        if filename in os.listdir(raw_directory):
            i=0
            while True:
                if filename in os.listdir(directory + 'PDF'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1]):
                    i += 1
                    os.rename(filename,filename[0:len(filename)-4]+'('+str(i)+')'+'.pdf')
                    filename = filename[0:len(filename) - 4] + '(' + str(i) + ')' + '.pdf'
                else:
                    shutil.move(directory + filename, directory + 'PDF'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
                    break

        else:
            shutil.move(directory + filename, directory + 'PDF'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
    if filename.endswith(".txt") or filename.endswith(".docx") or filename.endswith('.doc'):
        z = os.path.getctime(filename)
        if os.path.exists('Textfile'):
            pass
        else:
            os.mkdir('Textfile')
        if len((time.ctime(z).split(' ')))==5:
            year=(time.ctime(z).split(' '))[4]
        else:
            year=(time.ctime(z).split(' '))[5]
        if year in os.listdir(directory + 'Textfile'):
            pass
        else:
            parent_dir = directory + 'Textfile'
            path = os.path.join(parent_dir,year)
            os.mkdir(path)
        if (time.ctime(z).split(' '))[1] in os.listdir(directory + 'Textfile'+'\\'+year):
            pass
        else:
            parent_dir = directory + 'Textfile'+'\\'+year
            path = os.path.join(parent_dir,(time.ctime(z).split(' '))[1])
            os.mkdir(path)
        if filename in os.listdir(raw_directory):
            i=0
            while True:
                if filename in os.listdir(directory + 'Textfile'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1]):
                    i += 1
                    os.rename(filename,filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1]))
                    filename=filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1])
                else:
                    shutil.move(directory + filename, directory + 'Textfile'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
                    break

        else:
            shutil.move(directory + filename, directory + 'Textfile'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
    if filename.endswith(".zip") or filename.endswith(".rar"):
        z = os.path.getctime(filename)
        if os.path.exists('ZIP'):
            pass
        else:
            os.mkdir('ZIP')
        if len((time.ctime(z).split(' ')))==5:
            year=(time.ctime(z).split(' '))[4]
        else:
            year=(time.ctime(z).split(' '))[5]
        if year in os.listdir(directory + 'ZIP'):
            pass
        else:
            parent_dir = directory + 'ZIP'
            path = os.path.join(parent_dir, year)
            os.mkdir(path)
        if (time.ctime(z).split(' '))[1] in os.listdir(directory + 'ZIP' + '\\' + year):
            pass
        else:
            parent_dir = directory + 'ZIP' + '\\' + year
            path = os.path.join(parent_dir, (time.ctime(z).split(' '))[1])
            os.mkdir(path)
        if filename in os.listdir(raw_directory):
            i=0
            while True:
                if filename in os.listdir(directory + 'ZIP'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1]):
                    i += 1
                    os.rename(filename,filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1]))
                    filename=filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1])
                else:
                    shutil.move(directory + filename, directory + 'ZIP'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
                    break

        else:
            shutil.move(directory + filename, directory + 'ZIP'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
    if filename.endswith(".torrent"):
        z = os.path.getctime(filename)
        if os.path.exists('Torrent'):
            pass
        else:
            os.mkdir('Torrent')
        if len((time.ctime(z).split(' ')))==5:
            year=(time.ctime(z).split(' '))[4]
        else:
            year=(time.ctime(z).split(' '))[5]
        if year in os.listdir(directory + 'Torrent'):
            pass
        else:
            parent_dir = directory + 'Torrent'
            path = os.path.join(parent_dir, year)
            os.mkdir(path)
        if (time.ctime(z).split(' '))[1] in os.listdir(directory + 'Torrent' + '\\' + year):
            pass
        else:
            parent_dir = directory + 'Torrent' + '\\' + year
            path = os.path.join(parent_dir, (time.ctime(z).split(' '))[1])
            os.mkdir(path)
        if filename in os.listdir(raw_directory):
            i=0
            while True:
                if filename in os.listdir(directory + 'Torrent'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1]):
                    i += 1
                    os.rename(filename,filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1]))
                    filename=filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1])
                else:
                    shutil.move(directory + filename, directory + 'Torrent'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
                    break

        else:
            shutil.move(directory + filename, directory + 'Torrent'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
    if filename.endswith(".mp3"):
        z = os.path.getctime(filename)
        if os.path.exists('Audio'):
            pass
        else:
            os.mkdir('Audio')
        if len((time.ctime(z).split(' ')))==5:
            year=(time.ctime(z).split(' '))[4]
        else:
            year=(time.ctime(z).split(' '))[5]
        if year in os.listdir(directory + 'Audio'):
            pass
        else:
            parent_dir = directory + 'Audio'
            path = os.path.join(parent_dir, year)
            os.mkdir(path)
        if (time.ctime(z).split(' '))[1] in os.listdir(directory + 'Audio' + '\\' + year):
            pass
        else:
            parent_dir = directory + 'Audio' + '\\' + year
            path = os.path.join(parent_dir, (time.ctime(z).split(' '))[1])
            os.mkdir(path)
        if filename in os.listdir(raw_directory):
            i=0
            while True:
                if filename in os.listdir(directory + 'Audio'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1]):
                    i += 1
                    os.rename(filename,filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1]))
                    filename=filename[0:len(filename)-4]+'('+str(i)+')'+'.'+str(filename.split('.')[1])
                else:
                    shutil.move(directory + filename, directory + 'Audio'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])
                    break
        else:
            shutil.move(directory + filename, directory + 'Audio'+'\\'+year+'\\'+(time.ctime(z).split(' '))[1])


