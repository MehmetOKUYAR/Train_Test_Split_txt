# Train Test Split txt
 
### Configure your data folders
we take the image paths in your file and then append them to a list as seen below. additionally you can increase the number of these folders
~~~~
7  # ------- get the path of the images -----------
8  # ------- you can increase the folders to train on more images ----------- 
9  Folder1 = glob('Folder1_path/*.jpg')
10 print('Folder1 size :',len(Folder1))
11
12 Folder2 = glob ('Folder2_path/*.jpg')
13 print('Folder2 size :',len(Folder2))
14 
15 img_files=[]
16
17 # ------- append the images to the list -----------
18 for img_path in Folder1:
19    img_files.append(img_path)
20
21 for img_path in Folder2:
22    img_files.append(img_path)
~~~~~~~~~~~

