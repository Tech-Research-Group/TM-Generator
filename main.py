""" TM SHELL GENERATOR """
import os
import shutil
import tkinter as tk
from tkinter import Button, Checkbutton, filedialog, Entry, IntVar, Label, messagebox, StringVar
from tkinter.constants import FALSE
from tkinter.ttk import Combobox
import contextlib
import openpyxl as xl
from dotenv import dotenv_values
import manuals.tm2b as tm2b
import manuals.tm2c as tm2c
import manuals.tm2d as tm2d

global chbox_1, chbox_2, chbox_3, chbox_4, chbox_5, chbox_6
config = dotenv_values(".env")  # take environment variables from .env.
excelFile = None
manual = ''
milstd = ''
workbook = None
ws = None

CBX_MANUAL = ''
CBX_MIL_STD = ''
ERRORS = []
FSC = ''
ICON = r"C:\\Users\\nicho\\Desktop\\Dev Projects\\TM Generator\\logo_TRG.ico"
NIIN = ''
PART_NO = ''
SYS_ACRONYM = ''
SYS_NAME = ''
SYS_NUMBER = ''
TAB_2 = '\t\t'
TAB_3 = '\t\t\t'
TAB_4 = '\t\t\t\t'
TAB_5 = '\t\t\t\t\t'
TAB_6 = '\t\t\t\t\t\t'
TAB_7 = '\t\t\t\t\t\t\t'
TAB_8 = '\t\t\t\t\t\t\t\t'
UOC = ''


def form_validation(save_path) -> None:
    """Validates the items that are part of the form.
    Turns input fields red if empty. Adds error messages to the errors list."""
    global ERRORS, SYS_ACRONYM, SYS_NUMBER, SYS_NAME, FSC, NIIN, PART_NO, UOC
    ERRORS = []
    SYS_NAME = ent_sys_name.get()
    SYS_ACRONYM = ent_sys_acronym.get()
    SYS_NUMBER = ent_sys_number.get()
    FSC = ent_fsc.get()
    NIIN = ent_niin.get()
    PART_NO = ent_part_no.get()
    UOC = ent_uoc.get()

    # Form Validation to make sure all fields are filled out
    if SYS_NAME == '':
        lbl_sys_name.configure(fg='red')
        ERRORS.append('SYSTEM NAME is required.\n')
    else:
        lbl_sys_name.configure(fg='black')
    if SYS_ACRONYM == '':
        lbl_sys_acronym.configure(fg='red')
        ERRORS.append('SYSTEM ACRONYM is required.\n')
    else:
        lbl_sys_acronym.configure(fg='black')
    if SYS_NUMBER == '':
        lbl_sys_number.configure(fg='red')
        ERRORS.append('SYSTEM NUMBER is required.\n')
    else:
        lbl_sys_number.configure(fg='black')
    if FSC == '':
        lbl_fsc.configure(fg='red')
        ERRORS.append('FSC is required.\n')
    else:
        lbl_fsc.configure(fg='black')
    if NIIN == '':
        lbl_niin.configure(fg='red')
        ERRORS.append('NIIN is required.\n')
    else:
        lbl_niin.configure(fg='black')
    if PART_NO == '':
        lbl_part_no.configure(fg='red')
        ERRORS.append('PART NUMBER is required.\n')
    else:
        lbl_part_no.configure(fg='black')
    if UOC == '':
        lbl_uoc.configure(fg='red')
        ERRORS.append('UOC is required.\n')
    else:
        lbl_uoc.configure(fg='black')
    # If errors list contains errors, display them in a message box.
    if ERRORS:
        messagebox.showerror("Error", show_errors())
    # If no errors, build the TM.
    else:
        build_tm(save_path)

def show_errors() -> str:
    """Combines all form errors and returns them as a string."""
    error_string = ''
    for error in ERRORS:
        error_string += error
    return error_string

def clear_form() -> None:
    """Clears all the form fields."""
    ent_sys_name.delete(0, 'end')
    ent_sys_acronym.delete(0, 'end')
    ent_sys_number.delete(0, 'end')
    ent_fsc.delete(0, 'end')
    ent_niin.delete(0, 'end')
    ent_part_no.delete(0, 'end')
    ent_uoc.delete(0, 'end')

    # Reset the Comoboxes
    CBX_MANUAL.current(0)
    CBX_MIL_STD.current(0)

    # Reset the Checkboxes
    chbox_1.deselect()
    chbox_2.deselect()
    chbox_3.deselect()
    chbox_4.deselect()
    chbox_5.deselect()
    chbox_6.deselect()

    chbox_3['state'] = 'disable'
    chbox_4['state'] = 'disable'

def build_tm(save_path) -> None:
    """Check the TM/MIL-STD versions and start to build TM."""
    global milstd, manual
    milstd = CBX_MIL_STD.get()
    manual = CBX_MANUAL.get()
    # Build the TM based on the selected MIL-STD and Manual Type
    if milstd == '2B':
        if manual == "-10":
            create_tm_wip_dir(save_path)
            tm2b.build_10(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws, chb_1, chb_2, chb_5)
            print(f'Building...{manual} TM Shell using MIL-STD-{milstd}')
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "-13&P":       
            create_tm_wip_dir(save_path)
            tm2b.build_13p(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws, chb_1, chb_2, chb_5)
            print(f'Building...{manual} TM Shell using MIL-STD-{milstd}')
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "-23&P":
            create_tm_wip_dir(save_path)         
            tm2b.build_23p(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws, chb_1, chb_2, chb_5)
            print(f'Building...{manual} TM Shell using MIL-STD-{milstd}')
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "NMWR":
            create_tm_wip_dir(save_path)
            tm2b.build_nmwr(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
            print(f'Building...{manual} NMWR Shell using MIL-STD-{milstd}')
            messagebox.showinfo("Success!", "Your NMWR has been created.")
    elif milstd == '2C':
        if manual == "-10":
            create_tm_wip_dir(save_path)
            tm2c.build_10(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws, chb_1, chb_2, chb_5, chb_6)
            print(f'Building...{manual} TM Shell using MIL-STD-{milstd}')
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "-13&P":
            create_tm_wip_dir(save_path)
            tm2c.build_13p(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws, chb_1, chb_2, chb_5, chb_6)
            print(f'Building...{manual} TM Shell using MIL-STD-{milstd}')
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "-23&P":
            create_tm_wip_dir(save_path)
            tm2c.build_23p(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws, chb_1, chb_2, chb_5, chb_6)
            print(f'Building...{manual} TM Shell using MIL-STD-{milstd}')
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "NMWR":
            create_tm_wip_dir(save_path)     
            tm2c.build_nmwr(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
            print(f'Building...{manual} NMWR Shell using MIL-STD-{milstd}')
            messagebox.showinfo("Success!", "Your NMWR has been created.")
    elif milstd == '2D':
        if manual == "-10":
            create_tm_wip_dir(save_path)
            tm2d.build_10_tm(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws, chb_1, chb_2, chb_3, chb_4, chb_5, chb_6)
            print(f'Building...{manual} TM Shell using MIL-STD-{milstd}')
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "-12&P":
            create_tm_wip_dir(save_path)
            tm2d.build_12p_tm(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws, chb_1, chb_2, chb_5, chb_6)
            print(f'Building...{manual} TM Shell using MIL-STD-{milstd}')
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "NMWR":
            create_tm_wip_dir(save_path)
            tm2d.build_nmwr(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
            print(f'Building...{manual} NMWR Shell using MIL-STD-{milstd}')
            messagebox.showinfo("Success!", "Your NMWR has been created.")

def create_tm_wip_dir(save_path) -> None:
    """Creates the WIP directory for generated TM files.
    Deletes the current one if it exists."""
    man = CBX_MANUAL.get()
    # Directory
    directory = f"{SYS_ACRONYM} {man} WIP"
    # Parent Directory path
    parent_dir = f"{save_path}/"
    # Path
    path = os.path.join(parent_dir, directory)
    # Remove folder if a folder is already present
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)
    # Create the directory
    # '/home / User / Documents'
    os.mkdir(path)
    print(f"Creating the {directory} directory!")

def save_folder() -> str:
    """File dialog to save the folder."""
    if not ERRORS:
        save_path = filedialog.askdirectory(initialdir="/", title="Save file")
        print(save_path)
        if save_path == "":
            messagebox.showerror("Error", " Please select a save location.")
        else:
            form_validation(save_path)
    else:
        messagebox.showerror("Error", ERRORS)
        print(ERRORS)

# Comboboxes
def maincombo() -> None:
    """Creates the two comboboxes and binds one to another."""
    global CBX_MANUAL, CBX_MIL_STD
    man = StringVar()
    std = StringVar()
    man = ('-10', '-13&P', '-23&P', 'NMWR')
    std = ('2B', '2C', '2D')
    CBX_MIL_STD = Combobox(root, values=std, font='helvetica 13', width=33)
    CBX_MIL_STD.grid(column=1, row=7)
    CBX_MIL_STD['state'] = 'readonly'
    CBX_MIL_STD.current(0)
    CBX_MIL_STD.bind('<<ComboboxSelected>>', combofill)
    CBX_MANUAL = Combobox(root, values=man, font='helvetica 13', width=18, justify='left')
    CBX_MANUAL.grid(column=3, row=7)
    CBX_MANUAL['state'] = 'readonly'
    CBX_MANUAL.current(0)

def combofill(_e) -> None:
    """Checks what MIL-STD is selected to fill the TM type combobox."""
    if CBX_MIL_STD.get() == '2B':
        man = ('-10', '-13&P', '-23&P', 'NMWR')
        chbox_3['state'] = 'disable'
        chbox_4['state'] = 'disable'
        chbox_6['state'] = 'disable'
    elif CBX_MIL_STD.get() == '2C':
        man = ('-10', '-13&P', '-23&P', 'NMWR')
        chbox_3['state'] = 'disable'
        chbox_4['state'] = 'disable'
        chbox_6['state'] = 'active'
    elif CBX_MIL_STD.get() == '2D':
        man = ('-10', '-12&P', 'NMWR')
        chbox_3['state'] = 'active'
        chbox_4['state'] = 'active'
        chbox_6['state'] = 'active'
    else:
        man = ()
        chbox_3['state'] = 'disable'
        chbox_4['state'] = 'disable'
        chbox_6['state'] = 'disable'
    CBX_MANUAL.config(values=man)

def open_tm_tracker():
    global excelFile, workbook, ws
    try:
        excelFile = filedialog.askopenfilename(initialdir="~", title="Select TM Tracker",
            filetypes=(("Excel File", "*xlsx"), ("All Files",".")))
        if excelFile == "":
            raise FileNotFoundError("No TM tracker selected.")
    except FileNotFoundError as err:
        messagebox.showerror("Error", err)
    else:
        workbook = xl.load_workbook(excelFile)
        ws = workbook.active

def autofill() -> None:
    """Automatically fills in Entries with dummy data."""
    ent_sys_name.insert(0, 'Expeditionary TRICON Food Sanitation System')
    ent_sys_number.insert(0, '10-5419-224')
    ent_sys_acronym.insert(0, 'ETFSS')
    ent_niin.insert(0, '01-686-0248')
    ent_fsc.insert(0, '5419')
    ent_uoc.insert(0, 'SHELTER, EXPANDABLE, ETFSS (GREEN)')
    ent_part_no.insert(0, '9-1-1121-1')

root = tk.Tk()
root.geometry('935x470')
root.title('TM Generator')
root.resizable(width=FALSE, height=FALSE)

with contextlib.suppress(tk.TclError):
    root.iconbitmap(ICON)
# System name
lbl_sys_name = Label(root, text='SYSTEM NAME: ', font='helvetica 13 bold', pady=5)
lbl_sys_name.grid(column=0, row=2)

ent_sys_name = Entry(root, text='Expeditionary TRICON Food Sanitation System',
                     font='helvetica 13', width=35, justify='left')
ent_sys_name.grid(column=1, row=2)

# System Number
lbl_sys_number = Label(root, text='SYSTEM NUMBER: ',
                       font='helvetica 13 bold', pady=5)
lbl_sys_number.grid(column=0, row=3)

ent_sys_number = Entry(root, font='helvetica 13', width=35, justify='left')
ent_sys_number.grid(column=1, row=3)

# System acronym
lbl_sys_acronym = Label(root, text='SYSTEM ACRONYM: ',
                        font='helvetica 13 bold', pady=5)
lbl_sys_acronym.grid(column=2, row=3)

ent_sys_acronym = Entry(root, font='helvetica 13', width=20, justify='left')
ent_sys_acronym.grid(column=3, row=3)

# NIIN
lbl_niin = Label(root, text='NIIN: ', font='helvetica 13 bold', pady=5)
lbl_niin.grid(column=0, row=5)

ent_niin = Entry(root, font='helvetica 13', width=35, justify="left")
ent_niin.grid(column=1, row=5)

# FSC
lbl_fsc = Label(root, text='FSC: ', font='helvetica 13 bold', pady=5)
lbl_fsc.grid(column=2, row=5)

ent_fsc = Entry(root, font='helvetica 13', width=20, justify="left")
ent_fsc.grid(column=3, row=5)

# UOC
lbl_uoc = Label(root, text='UOC: ', font='helvetica 13 bold', pady=5)
lbl_uoc.grid(column=0, row=6)

ent_uoc = Entry(root, font='helvetica 13', width=35, justify='left')
ent_uoc.grid(column=1, row=6)

# PN
lbl_part_no = Label(root, text='PART NUMBER: ', font='helvetica 13 bold', pady=5)
lbl_part_no.grid(column=2, row=6)

ent_part_no = Entry(root, font='helvetica 13', width=20, justify='left')
ent_part_no.grid(column=3, row=6)

# MIL-STD
lbl_mil_std = Label(root, text='MIL-STD: ', font='helvetica 13 bold', pady=5)
lbl_mil_std.grid(column=0, row=7)

# Manual Type
lbl_man_type = Label(root, text='MANUAL TYPE: ', font='helvetica 13 bold', pady=5)
lbl_man_type.grid(column=2, row=7)

maincombo()

# OPTIONAL CHAPTERS
lbl_blank = Label(root, text='', font='helvetica 13 bold',
                         pady=5, anchor='w', width=35)
lbl_blank.grid(column=1, row=8)
lbl_add_chapters = Label(root, text='ADD OPTIONAL CHAPTERS:', font='helvetica 13 bold',
                         pady=5, anchor='w', width=35)
lbl_add_chapters.grid(column=1, row=9)

chb_1 = IntVar()
chb_2 = IntVar()
chb_3 = IntVar()
chb_4 = IntVar()
chb_5 = IntVar()
chb_6 = IntVar()
chbox_1 = Checkbutton(root, text='Auxillary Equipment Chapter', font='helvetica 13 bold',
                      variable=chb_1, onvalue=1, offvalue=0, width=35, anchor='w')
chbox_1.grid(column=1, row=10)
chbox_2 = Checkbutton(root, text='Ammunition Chapter', font='helvetica 13 bold',
                      variable=chb_2, onvalue=1, offvalue=0, width=35, anchor='w')
chbox_2.grid(column=1, row=11)
chbox_3 = Checkbutton(root, text='Shipment/Movement & Storage Chapter', font='helvetica 13 bold',
                      variable=chb_3, onvalue=1, offvalue=0, width=35, anchor='w', state='disable')
chbox_3.grid(column=1, row=12)
chbox_4 = Checkbutton(root, text='Ammunition Marking Chapter', font='helvetica 13 bold',
                      variable=chb_4, onvalue=1, offvalue=0, width=35, anchor='w', state='disable')
chbox_4.grid(column=1, row=13)
chbox_5 = Checkbutton(root, text='Destruction of Equipment Chapter', font='helvetica 13 bold',
                      variable=chb_5, onvalue=1, offvalue=0, width=35, anchor='w')
chbox_5.grid(column=1, row=14)
chbox_6 = Checkbutton(root, text='Software Information Chapter', font='helvetica 13 bold',
                      variable=chb_6, onvalue=1, offvalue=0, width=35, anchor='w', state='disable')
chbox_6.grid(column=1, row=15)

# Autofill Button
btn_autofill = Button(root, text='AUTOFILL FORM', font='helvetica 13 bold',bg='blue', fg='white',
                      command=autofill, width=15, pady=5, justify='left')
btn_autofill.grid(column=3, row=9)

# TM Tracker Button
btn_tm_tracker = Button(root, text='SELECT TRACKER', font='helvetica 13 bold',bg='blue', fg='white',
                      command=open_tm_tracker, width=15, pady=5, justify='left')
btn_tm_tracker.grid(column=3, row=11)

# Clear Button
btn_clear = Button(root, text='CLEAR FORM', font='helvetica 13 bold', bg='red', fg='white',
                      command=clear_form, width=15, pady=5, justify='left')
btn_clear.grid(column=3, row=13)

# Build TM Button
btn_build = Button(root, text='BUILD TM', font='helvetica 13 bold', bg='green', fg='white',
                      command=save_folder, width=15, pady=5, justify='left')
btn_build.grid(column=3, row=15)


root.mainloop()
