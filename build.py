import subprocess
import os
import shutil

def build_executable():
    main_file = "aplicacaoTkin.py"
    
    
    dist_dir = os.path.join(os.getcwd(), 'dist')
    if not os.path.exists(dist_dir):
        os.makedirs(dist_dir)
    
    
    command = [
        "pyinstaller",
        "--onefile", 
        "--distpath", dist_dir, 
        main_file
    ]
    
    try:
        print(f"Building executable for {main_file}...")
        subprocess.run(command, check=True)
        print(f"Build completed successfully! Executable is in {dist_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error during build: {e}")
    finally:
        cleanup()

def cleanup():
    
    build_folders = ["build", "__pycache__"]
    spec_file = "aplicacaoTkin.spec"
    
    
    for folder in build_folders:
        if os.path.exists(folder):
            print(f"Removing folder: {folder}")
            shutil.rmtree(folder)
            print(f"Folder {folder} removed.")
    
    
    if os.path.exists(spec_file):
        print(f"Removing spec file: {spec_file}")
        os.remove(spec_file)
        print(f"Spec file {spec_file} removed.")
    
    print("Cleanup completed.")

if __name__ == "__main__":
    build_executable()
