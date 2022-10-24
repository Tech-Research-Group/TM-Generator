pyinstaller main.py --name='TM Generator' ^
    --onedir ^
    --windowed --noupx ^
    --icon=images\logo_TRG.ico ^
    --target-arch=x86_64 ^
    --splash=images\logo_TRG.ico ^
    --add-data="./.env;." ^
    --noconfirm --clean
