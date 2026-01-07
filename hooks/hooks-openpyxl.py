from PyInstaller.utils.hooks import collect_data_files, collect_submodules

hiddenimports = collect_submodules("openpyxl")

# Also include templates and package data openpyxl needs at runtime
datas = collect_data_files("openpyxl")
