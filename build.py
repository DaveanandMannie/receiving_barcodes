import PyInstaller.__main__

if __name__ == '__main__':
    PyInstaller.__main__.run([
        '--name=Receiving_Barcode_Generator',
        '--onedir',
        '--windowed',
        '--add-data=./resources;resources',
        '--add-data=./.venv/Lib/site-packages/customtkinter;customtkinter',
        '--icon=./resources/icon.ico',
        '--distpath=./builds',
        '-y',
        '--clean',
        'gui.py',
    ])