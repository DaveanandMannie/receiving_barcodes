import os
import shutil

import PyInstaller.__main__

if __name__ == '__main__':
    PyInstaller.__main__.run([
        '--name=Receiving_Barcode_Generator',
        '--onedir',
        '--windowed',
        '--add-data=./resources;resources',
        '--add-data=./venv/Lib/site-packages/customtkinter;customtkinter',
        '--icon=./resources/icon.ico',
        '--distpath=./builds',
        '-y',
        '--clean',
        'gui.py',
    ])

    build_path = os.path.abspath('./builds/Receiving_Barcode_Generator')
    source_resources_dir = os.path.join(build_path, '_internal', 'resources')
    shutil.move(source_resources_dir, build_path)

    shutil.rmtree(os.path.abspath('./build'))
