import os
import time


class MyCleaner:

    def __init__(self):
        self.initial_dest = "D:\\stuff"
        self.final_dest = "D:\\Chrome Downloads"
        self.i = 1

        self.list_dir = os.listdir(self.initial_dest)

    def clean(self):
        if self.list_dir:
            for file in self.list_dir:
                try:
                    os.rename(self.initial_dest + "\\" + file, self.final_dest + "\\" + file)
                except FileExistsError:
                    print("File {} exists already in the dest folder... "
                          "Renaming to {}".format(file, os.path.splitext(file)[0] + "_" + str(self.i)))
                    os.rename(self.initial_dest + "\\" + file, self.final_dest + "\\" + os.path.splitext(file)[0] +
                              "_" + str(self.i) + os.path.splitext(file)[1])
                    self.i += 1

            print("Successfully moved {} file(s).".format(len(self.list_dir)))

        else:
            print("Folder is already clean.")

    def show_state(self):
        print(len(self.list_dir))


while True:
    cleaner = MyCleaner()
    time.sleep(200)
    cleaner.clean()
