import os

# Set the directory where the project is located
project_dir = '/home/ubuntu/ult/pragalub'  # Change this to your directory

# Traverse all files in the project directory
for root, dirs, files in os.walk(project_dir):
    # Skip the .git directory
    if '.git' in root:
        continue
    
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(root, file)
        
        try:
            # Open the file with UTF-8 encoding
            with open(file_path, 'r+', encoding='utf-8') as f:
                content = f.read()
                # Replace all occurrences of pyPandeyLogs with pyPragyanLogs
                updated_content = content.replace('pyPandeyLogs', 'pyPandeyLogs') 
                
                # Write the updated content back to the file
                f.seek(0)
                f.write(updated_content)
                f.truncate()
        
        except UnicodeDecodeError:
            # If a UnicodeDecodeError occurs, try opening with a different encoding
            try:
                with open(file_path, 'r+', encoding='ISO-8859-1') as f:
                    content = f.read()
                    # Replace all occurrences of pyPandeyLogs with pyPragyanLogs
                    updated_content = content.replace('pyPandeyLogs', 'pyPragyanLogs')
                    
                    # Write the updated content back to the file
                    f.seek(0)
                    f.write(updated_content)
                    f.truncate()
            except Exception as e:
                print(f"Failed to process {file_path} due to error: {e}")
        except PermissionError:
            # Skip files with permission issues and continue with the next file
            print(f"Permission denied for {file_path}. Skipping.")
            continue

print("Update completed!")
