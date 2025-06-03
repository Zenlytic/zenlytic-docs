import os
import re

def fix_image_paths(directory):
    # Walk through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # Read the file content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace ../assets/ with /assets/
                new_content = re.sub(r'!\[(.*?)\]\(\.\./assets/(.*?)\)', r'![\1](/assets/\2)', content)
                
                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == '__main__':
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    fix_image_paths(script_dir) 