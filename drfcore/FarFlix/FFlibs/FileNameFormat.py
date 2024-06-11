import os

class FileNameFormat:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def get_files(self):
        print(os.listdir(self.folder_path))
        return os.listdir(self.folder_path)

    def format_name(self, name):
        # Split the filename from its extension
        base_name, ext = os.path.splitext(name)
        
        # Replace . and _ with space in the base name
        base_name = base_name.replace('.', ' ')
        base_name = base_name.replace('_', ' ')
        
        # Remove parentheses
        base_name = base_name.replace('(', '')
        base_name = base_name.replace(')', '')
        
        # Capitalize the base name
        base_name = base_name.title()
        
        # Join the formatted base name with its extension
        new_name = base_name + ext
        return new_name

    def rename_files(self):
        for filename in self.get_files():
            print(f"Before : {filename}")
            new_name = self.format_name(filename)
            old_file_path = os.path.join(self.folder_path, filename)
            new_file_path = os.path.join(self.folder_path, new_name)
            os.rename(old_file_path, new_file_path)

# Usage
path = r"D:\Simply_Movies\Bolly\2024_MoviesHut\Feb2024\3\\"
formatter = FileNameFormat(path)
formatter.rename_files()
