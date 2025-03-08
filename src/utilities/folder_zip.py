import os
import uuid
import zipfile



class ZipFolder:


    def __init__(self,file_path:str) -> None:

        self.zip_folder = os.path.join("src\temp", file_path)
        if not os.path.exists(self.zip_folder):
            os.makedirs(self.zip_folder, exist_ok=True)

        self.zip_file_path = os.path.join(self.zip_folder, f"{str(uuid.uuid4())}.zip")
    


    def zip(self):
        with zipfile.ZipFile(self.zip_file_path, "w") as zip_file:
            for foldername, _, filenames in os.walk(self.zip_folder):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
            
                    if file_path != self.zip_file_path:
                        arcname = os.path.relpath(file_path, self.zip_folder)
                        zip_file.write(file_path, arcname)

        for root, _, files in os.walk(self.zip_folder):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path != self.zip_file_path:  
                    if not os.path.commonpath([file_path, self.zip_file_path]).startswith(self.zip_file_path):
                        os.remove(file_path)

        return self.zip_file_path




