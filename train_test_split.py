from glob import glob
import os
from sklearn import model_selection



# ------- get the path of the images -----------
# ------- you can increase the folders to train on more images ----------- 
Folder1 = glob('Folder1/*.jpg')
print('Folder1 size :',len(Folder1))
Folder2 = glob ('Folder2/*.jpg')
print('Folder2 size :',len(Folder2))

img_files=[]

# ------- append the images to the list -----------
for img_path in Folder1:
    img_files.append(img_path)

for img_path in Folder2:
    img_files.append(img_path)


# ------- split the data into train and test -----------
df_train,df_test =model_selection.train_test_split(
        img_files,
        test_size=0.2,
        random_state=42,
        shuffle=True
    )

print('train size : ',len(df_train))
print('test size : ',len(df_test))

# ------- save the train and test data to the respective folders -----------
with open("train.txt", "w") as outfile:
    for train_path in df_train:
        outfile.write(train_path)
        outfile.write("\n")
    outfile.close()

with open("test.txt", "w") as outfile:
    for test_path in df_test:
        outfile.write(test_path)
        outfile.write("\n")
    outfile.close()

print('işlem Tamamlandı ! ')