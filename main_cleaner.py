import os
import time


class MyCleaner:

    def __init__(self):
        """Initialize folders if they do not exist yet and a counter for files with the same names. """
        self.initial_dest = "D:\\Chrome Downloads"

        self.final_dest = {"Art": "D:\\Photos and Videos",
                           "Docs": "D:\\Docs",
                           "E-books": "D:\\e-books",
                           "Other": "D:\\Chrome Downloads"}

        # Create folders if they do not exist
        for folder in self.final_dest.items():
            try:
                os.makedirs(folder[1])
            except FileExistsError:
                # directory already exists
                pass

        self.i = 1

    def clean(self):
        """Based on the extension of the file moves it to the correct folder."""
        list_dir = os.listdir(self.initial_dest)
        if list_dir:
            for file in list_dir:
                ext = os.path.splitext(file)[1]

                if ext.lower() in [".jpg", ".jpeg", ".mp4", ".avi", ".bmp", ".mkv"]:
                    self.move_file(file, self.final_dest["Art"])

                elif ext.lower() in [".pdf", ".doc", ".docx", ".xlsx", ".txt",
                                     ".csv", ".xls", ".accdb", ".pptx", ".rtf"]:
                    self.move_file(file, self.final_dest["Docs"])

                elif ext.lower() in [".epub", ".mobi"]:
                    self.move_file(file, self.final_dest["E-books"])

                else:
                    self.move_file(file, self.final_dest["Other"])

            print("Successfully moved {} file(s).".format(len(list_dir)))

        else:
            print("Folder is already clean.")

    def move_file(self, file, dest):
        """Actual function for moving (renaming) files. """
        try:
            os.rename(self.initial_dest + "\\" + file, dest + "\\" + file)
        except FileExistsError:
            print("File {} exists already in the dest folder...Renaming to {}".format(
                file, os.path.splitext(file)[0] + "_" + str(self.i)))
            os.rename(self.initial_dest + "\\" + file, dest + "\\" + os.path.splitext(file)[0] +
                      "_" + str(self.i) + os.path.splitext(file)[1])
            self.i += 1


cleaner = MyCleaner()
cleaner.clean()


"""
while True:
    cleaner = MyCleaner()
    time.sleep(200)
    cleaner.clean()
"""