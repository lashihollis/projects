import os

directory_path = "/Users/nathaniel.burren/data-platform-dbt/models/staging/zus/base"

for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        print(f"Processing file: {filename}")
        try:
          with open(file_path,'r') as file:
            content = file.read()
          with open(file_path,'w') as file:
            file.write(content.lower())
        except Exception as e:
          print(f"Error processing {filename}: {e}")
          