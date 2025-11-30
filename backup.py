import os
import sys
import shutil
import datetime

def backup_files(source_dir, dest_dir):
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    
    if not os.path.exists(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return
    
    for filename in os.listdir(source_dir):
        src_path = os.path.join(source_dir, filename)
        
        if os.path.isfile(src_path):
            dest_path = os.path.join(dest_dir, filename)
            
            if os.path.exists(dest_path):
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_{timestamp}{ext}"
                dest_path = os.path.join(dest_dir, new_filename)
            
            try:
                shutil.copy2(src_path, dest_path)
                print(f"Copied: {src_path} -> {dest_path}")
            except Exception as e:
                print(f"Error copying {src_path}: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_dir> <destination_dir>")
        return
    
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    
    backup_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()