"""TM SHELL GENERATOR"""

import contextlib
import os
import shutil
from tkinter import filedialog, messagebox

import openpyxl as xl
import ttkbootstrap as ttk
from ttkbootstrap.constants import DANGER, END, FALSE, LEFT, PRIMARY, SUCCESS, W

import cfg
import chapters.dataset as ds
import chapters.production as prod
import chapters.toc as toc
import manuals.tm2c as tm2c
import manuals.tm2d as tm2d

global chbox_1, chbox_2, chbox_3, chbox_4, chbox_5, chbox_6, chbox_tmi
excelFile = None
manual = ""
milstd = ""
workbook = None
ws = None

CBX_MANUAL = None
CBX_MIL_STD = None
CAGENO = ""
CUSTOM_TBUTTON = "Custom.TButton"
ERRORS = []
FSC = ""
ICON = r"C:\\Users\\nicho\\OneDrive - techresearchgroup.com\\Documents\\GitHub\\TM-Generator\\logo_TRG.ico"
MODELNO = ""
NIIN = ""
PARTNO = ""
SYS_ACRONYM = ""
SYS_NAME = ""
TMNO = ""
TAB_2 = "\t\t"
TAB_3 = "\t\t\t"
TAB_4 = "\t\t\t\t"
TAB_5 = "\t\t\t\t\t"
TAB_6 = "\t\t\t\t\t\t"
TAB_7 = "\t\t\t\t\t\t\t"
TAB_8 = "\t\t\t\t\t\t\t\t"
UOC = ""


def form_validation(save_path) -> None:
    """Validates the items that are part of the form.
    Turns input fields red if empty. Adds error messages to the errors list."""
    global CAGENO, ERRORS, FSC, MODELNO, NIIN, PARTNO, SYS_ACRONYM, SYS_NAME, TMNO, UOC
    CAGENO = ent_cageno.get()
    ERRORS = []
    FSC = ent_fsc.get()
    MODELNO = ent_modelno.get()
    NIIN = ent_niin.get()
    PARTNO = ent_partno.get()
    SYS_ACRONYM = ent_sys_acronym.get()
    SYS_NAME = ent_sys_name.get()
    TMNO = ent_tmno.get()
    UOC = ent_uoc.get()

    # Form Validation to make sure all fields are filled out
    if SYS_NAME == "":
        lbl_sys_name.configure(foreground="red")
        ERRORS.append("SYSTEM NAME is required.\n")
    else:
        lbl_sys_name.configure(foreground="white")
    if SYS_ACRONYM == "":
        lbl_sys_acronym.configure(foreground="red")
        ERRORS.append("SYSTEM ACRONYM is required.\n")
    else:
        lbl_sys_acronym.configure(foreground="white")
    if TMNO == "":
        lbl_tmno.configure(foreground="red")
        ERRORS.append("TM NUMBER is required.\n")
    else:
        lbl_tmno.configure(foreground="white")
    if FSC == "":
        lbl_fsc.configure(foreground="red")
        ERRORS.append("FSC is required.\n")
    else:
        lbl_fsc.configure(foreground="white")
    if NIIN == "":
        lbl_niin.configure(foreground="red")
        ERRORS.append("NIIN is required.\n")
    else:
        lbl_niin.configure(foreground="white")
    if PARTNO == "":
        lbl_part_no.configure(foreground="red")
        ERRORS.append("PART NUMBER is required.\n")
    else:
        lbl_part_no.configure(foreground="white")
    if ERRORS:
        messagebox.showerror("Error", show_errors())
    # If no errors, build the TM.
    else:
        build_tm(save_path)


def show_errors() -> str:
    """Combines all form errors and returns them as a string."""
    error_string = ""
    for error in ERRORS:
        error_string += error
    return error_string


def clear_form() -> None:
    """Clears all the form fields."""
    ent_cageno.delete(0, END)
    ent_fsc.delete(0, END)
    ent_modelno.delete(0, END)
    ent_niin.delete(0, END)
    ent_partno.delete(0, END)
    ent_sys_acronym.delete(0, END)
    ent_sys_name.delete(0, END)
    ent_tmno.delete(0, END)
    ent_uoc.delete(0, END)

    # Reset the Comboboxes
    if CBX_MANUAL is not None:
        CBX_MANUAL.current(0)
    if CBX_MIL_STD is not None:
        CBX_MIL_STD.current(0)

    # Reset the Checkboxes
    chb_tmi.set(0)
    chb_1.set(0)
    chb_2.set(0)
    chb_3.set(0)
    chb_4.set(0)
    chb_5.set(0)
    chb_6.set(0)

    chbox_3["state"] = "disable"
    chbox_4["state"] = "disable"

    # Reset WP Numbering
    cfg.prefix_file = 0


def build_tm(save_path) -> None:
    """Check the TM/MIL-STD versions and start to build TM."""
    global milstd, manual
    milstd = CBX_MIL_STD.get()
    manual = CBX_MANUAL.get()

    if milstd == "2C":
        if manual == "-10":
            create_tm_wip_dir(save_path)
            production = prod.Production(
                CAGENO,
                FSC,
                manual,
                milstd,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
            )
            production.buildProduction()
            dataset = ds.DataSet(manual, SYS_ACRONYM, save_path)
            dataset.buildDataSet()
            table_of_contents = toc.TOC(manual, SYS_ACRONYM, save_path)
            table_of_contents.buildTOC()
            tm2c.build_10(
                CAGENO,
                FSC,
                manual,
                milstd,
                MODELNO,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
                ws,
                chb_1,
                chb_2,
                chb_5,
                chb_6,
                chb_tmi,
            )
            print(f"Building...{manual} TM Shell using MIL-STD-{milstd}")
            # Reset WP Numbering
            cfg.prefix_file = 0
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "-13&P":
            create_tm_wip_dir(save_path)
            production = prod.Production(
                CAGENO,
                FSC,
                manual,
                milstd,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
            )
            production.buildProduction()
            dataset = ds.DataSet(manual, SYS_ACRONYM, save_path)
            dataset.buildDataSet()
            table_of_contents = toc.TOC(manual, SYS_ACRONYM, save_path)
            table_of_contents.buildTOC()
            tm2c.build_13p(
                CAGENO,
                FSC,
                manual,
                milstd,
                MODELNO,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
                ws,
                chb_1,
                chb_2,
                chb_5,
                chb_6,
                chb_tmi,
            )
            print(f"Building...{manual} TM Shell using MIL-STD-{milstd}")
            # Reset WP Numbering
            cfg.prefix_file = 0
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "-23&P":
            create_tm_wip_dir(save_path)
            production = prod.Production(
                CAGENO,
                FSC,
                manual,
                milstd,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
            )
            production.buildProduction()
            dataset = ds.DataSet(manual, SYS_ACRONYM, save_path)
            dataset.buildDataSet()
            table_of_contents = toc.TOC(manual, SYS_ACRONYM, save_path)
            table_of_contents.buildTOC()
            tm2c.build_23p(
                CAGENO,
                FSC,
                manual,
                milstd,
                MODELNO,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
                ws,
                chb_1,
                chb_2,
                chb_5,
                chb_6,
                chb_tmi,
            )
            print(f"Building...{manual} TM Shell using MIL-STD-{milstd}")
            # Reset WP Numbering
            cfg.prefix_file = 0
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "NMWR":
            create_tm_wip_dir(save_path)
            production = prod.Production(
                CAGENO,
                FSC,
                manual,
                milstd,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
            )
            production.buildProduction()
            dataset = ds.DataSet(manual, SYS_ACRONYM, save_path)
            dataset.buildDataSet()
            table_of_contents = toc.TOC(manual, SYS_ACRONYM, save_path)
            table_of_contents.buildTOC()
            tm2c.build_nmwr(
                CAGENO,
                FSC,
                manual,
                milstd,
                MODELNO,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
                ws,
            )
            print(f"Building...{manual} NMWR Shell using MIL-STD-{milstd}")
            # Reset WP Numbering
            cfg.prefix_file = 0
            messagebox.showinfo("Success!", "Your NMWR has been created.")
    elif milstd == "2D":
        if manual == "-10":
            create_tm_wip_dir(save_path)
            production = prod.Production(
                CAGENO,
                FSC,
                manual,
                milstd,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
            )
            production.buildProduction()
            dataset = ds.DataSet(manual, SYS_ACRONYM, save_path)
            dataset.buildDataSet()
            table_of_contents = toc.TOC(manual, SYS_ACRONYM, save_path)
            table_of_contents.buildTOC()
            tm2d.build_10_tm(
                CAGENO,
                FSC,
                manual,
                milstd,
                MODELNO,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
                ws,
                chb_1,
                chb_2,
                chb_3,
                chb_4,
                chb_5,
                chb_6,
                chb_tmi,
            )
            print(f"Building...{manual} TM Shell using MIL-STD-{milstd}")
            # Reset WP Numbering
            cfg.prefix_file = 0
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "-12&P":
            create_tm_wip_dir(save_path)
            production = prod.Production(
                CAGENO,
                FSC,
                manual,
                milstd,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
            )
            production.buildProduction()
            dataset = ds.DataSet(manual, SYS_ACRONYM, save_path)
            dataset.buildDataSet()
            table_of_contents = toc.TOC(manual, SYS_ACRONYM, save_path)
            table_of_contents.buildTOC()
            tm2d.build_12p_tm(
                CAGENO,
                FSC,
                manual,
                milstd,
                MODELNO,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
                ws,
                chb_1,
                chb_2,
                chb_3,
                chb_4,
                chb_5,
                chb_6,
                chb_tmi,
            )
            print(f"Building...{manual} TM Shell using MIL-STD-{milstd}")
            # Reset WP Numbering
            cfg.prefix_file = 0
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "-20":
            create_tm_wip_dir(save_path)
            production = prod.Production(
                CAGENO,
                FSC,
                manual,
                milstd,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
            )
            production.buildProduction()
            dataset = ds.DataSet(manual, SYS_ACRONYM, save_path)
            dataset.buildDataSet()
            table_of_contents = toc.TOC(manual, SYS_ACRONYM, save_path)
            table_of_contents.buildTOC()
            tm2d.build_20_tm(
                CAGENO,
                FSC,
                manual,
                milstd,
                MODELNO,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
                ws,
                chb_1,
                chb_2,
                chb_3,
                chb_4,
                chb_5,
                chb_6,
                chb_tmi,
            )
            print(f"Building...{manual} TM Shell using MIL-STD-{milstd}")
            # Reset WP Numbering
            cfg.prefix_file = 0
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "-20P":
            create_tm_wip_dir(save_path)
            production = prod.Production(
                CAGENO,
                FSC,
                manual,
                milstd,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
            )
            production.buildProduction()
            dataset = ds.DataSet(manual, SYS_ACRONYM, save_path)
            dataset.buildDataSet()
            table_of_contents = toc.TOC(manual, SYS_ACRONYM, save_path)
            table_of_contents.buildTOC()
            tm2d.build_20p_tm(
                CAGENO,
                FSC,
                manual,
                milstd,
                MODELNO,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
                ws,
            )
            print(f"Building...{manual} TM Shell using MIL-STD-{milstd}")
            # Reset WP Numbering
            cfg.prefix_file = 0
            messagebox.showinfo("Success!", "Your technical manual has been created.")
        elif manual == "NMWR":
            create_tm_wip_dir(save_path)
            production = prod.Production(
                CAGENO,
                FSC,
                manual,
                milstd,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
            )
            production.buildProduction()
            dataset = ds.DataSet(manual, SYS_ACRONYM, save_path)
            dataset.buildDataSet()
            table_of_contents = toc.TOC(manual, SYS_ACRONYM, save_path)
            table_of_contents.buildTOC()
            tm2d.build_nmwr(
                CAGENO,
                FSC,
                manual,
                milstd,
                MODELNO,
                NIIN,
                PARTNO,
                SYS_ACRONYM,
                SYS_NAME,
                TMNO,
                UOC,
                save_path,
                ws,
            )
            print(f"Building...{manual} NMWR Shell using MIL-STD-{milstd}")
            # Reset WP Numbering
            cfg.prefix_file = 0
            messagebox.showinfo("Success!", "Your NMWR has been created.")


def create_tm_wip_dir(save_path) -> None:
    """Creates the IADS directory for generated TM files.
    Deletes the current one if it exists."""
    man = CBX_MANUAL.get()
    # Directory
    directory = f"{SYS_ACRONYM} {man} IADS"
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
    # Create the 'files' subdirectory inside IADS
    files_dir = os.path.join(path, "files")
    os.mkdir(files_dir)
    print(f"Creating the files directory inside {directory}!")


def save_folder() -> None:
    """File dialog to save the folder."""
    if not ERRORS:
        save_path = filedialog.askdirectory(initialdir="/", title="Save file")
        print(save_path)
        if save_path == "":
            messagebox.showerror("Error", " Please select a save location.")
        else:
            form_validation(save_path)
    else:
        messagebox.showerror("Error", show_errors())
        print(ERRORS)


# Comboboxes
def maincombo() -> None:
    """Creates the two comboboxes and binds one to another."""
    global CBX_MANUAL, CBX_MIL_STD
    man_values = ("-10", "-13&P", "-23&P", "NMWR")
    std_values = ("2C", "2D", "E")
    CBX_MIL_STD = ttk.Combobox(root, values=std_values, font="helvetica 13", width=28)
    CBX_MIL_STD.grid(column=1, row=8)
    CBX_MIL_STD["state"] = "readonly"
    CBX_MIL_STD.current(0)
    CBX_MIL_STD.bind("<<ComboboxSelected>>", combofill)
    CBX_MANUAL = ttk.Combobox(
        root, values=man_values, font="helvetica 13", width=28, justify="left"
    )
    CBX_MANUAL.grid(column=3, row=8)
    CBX_MANUAL["state"] = "readonly"
    CBX_MANUAL.current(0)


def combofill(_e) -> None:
    """Checks what MIL-STD is selected to fill the TM type combobox."""
    if CBX_MIL_STD.get() == "2C":
        man = ("-10", "-13&P", "-23&P", "NMWR")
        chbox_3["state"] = "disable"
        chbox_4["state"] = "disable"
        chbox_6["state"] = "active"
    elif CBX_MIL_STD.get() == "2D":
        man = ("-10", "-12&P", "-20", "-20P", "NMWR")
        chbox_3["state"] = "active"
        chbox_4["state"] = "active"
        chbox_6["state"] = "active"
    elif CBX_MIL_STD.get() == "E":
        man = ("-10", "-12&P", "NMWR")
        chbox_3["state"] = "active"
        chbox_4["state"] = "active"
        chbox_6["state"] = "active"
    else:
        man = ()
        chbox_3["state"] = "disable"
        chbox_4["state"] = "disable"
        chbox_6["state"] = "disable"
    if CBX_MANUAL is not None:
        CBX_MANUAL.config(values=man)


def open_tm_tracker():
    global excelFile, workbook, ws
    try:
        excelFile = filedialog.askopenfilename(
            initialdir="~",
            title="Select TM Tracker",
            filetypes=(
                ("Excel File", "*xlsx"),
                ("Comma-Separated Variable File", "*.csv"),
                ("All Files", "."),
            ),
        )
        if excelFile == "":
            raise FileNotFoundError("No TM tracker selected.")
    except FileNotFoundError as err:
        messagebox.showerror("Error", str(err))
    else:
        workbook = xl.load_workbook(excelFile)
        ws = workbook.active


def autofill() -> None:
    """Automatically fills in Entries with dummy data."""
    ent_sys_name.insert(0, "IMPROVED ENVIRONMENTAL CONTROL UNIT")
    ent_tmno.insert(0, "9-4120-433")
    ent_sys_acronym.insert(0, "IECU")
    ent_niin.insert(0, "01-592-7987")
    ent_fsc.insert(0, "4120")
    ent_uoc.insert(0, "")
    ent_partno.insert(0, "IECU-5200")


root = ttk.Window(themename="darkly")
root.geometry("935x590")
root.title("TM Generator")
root.resizable(width=FALSE, height=FALSE)

with contextlib.suppress(Exception):
    root.iconbitmap(ICON)

# System Name
lbl_sys_name = ttk.Label(root, text="SYSTEM NAME: ", font="helvetica 13 bold")
lbl_sys_name.grid(column=0, row=2, pady=5)

ent_sys_name = ttk.Entry(root, font="helvetica 13", width=30, justify="left")
ent_sys_name.grid(column=1, row=2, pady=5)

# System Acronym
lbl_sys_acronym = ttk.Label(root, text="SYSTEM ACRONYM: ", font="helvetica 13 bold")
lbl_sys_acronym.grid(column=2, row=2, pady=5)

ent_sys_acronym = ttk.Entry(root, font="helvetica 13", width=30, justify="left")
ent_sys_acronym.grid(column=3, row=2, pady=5)

# TM Number
lbl_tmno = ttk.Label(root, text="TM NUMBER: ", font="helvetica 13 bold")
lbl_tmno.grid(column=0, row=3, pady=5)

ent_tmno = ttk.Entry(root, font="helvetica 13", width=30, justify="left")
ent_tmno.grid(column=1, row=3, pady=5)

# Model Number
lbl_modelno = ttk.Label(root, text="MODEL NUMBER: ", font="helvetica 13 bold")
lbl_modelno.grid(column=2, row=3, pady=5)

ent_modelno = ttk.Entry(root, font="helvetica 13", width=30, justify="left")
ent_modelno.grid(column=3, row=3, pady=5)

# NIIN
lbl_niin = ttk.Label(root, text="NIIN: ", font="helvetica 13 bold")
lbl_niin.grid(column=0, row=5, pady=5)

ent_niin = ttk.Entry(root, font="helvetica 13", width=30, justify="left")
ent_niin.grid(column=1, row=5, pady=5)

# FSC
lbl_fsc = ttk.Label(root, text="FSC: ", font="helvetica 13 bold")
lbl_fsc.grid(column=2, row=5, pady=5)

ent_fsc = ttk.Entry(root, font="helvetica 13", width=30, justify="left")
ent_fsc.grid(column=3, row=5, pady=5)

# UOC
lbl_uoc = ttk.Label(root, text="UOC: ", font="helvetica 13 bold")
lbl_uoc.grid(column=0, row=6, pady=5)

ent_uoc = ttk.Entry(root, font="helvetica 13", width=30, justify="left")
ent_uoc.grid(column=1, row=6, pady=5)

# PN
lbl_part_no = ttk.Label(root, text="PART NUMBER: ", font="helvetica 13 bold")
lbl_part_no.grid(column=2, row=6, pady=5)

ent_partno = ttk.Entry(root, font="helvetica 13", width=30, justify="left")
ent_partno.grid(column=3, row=6, pady=5)

# CAGE Code
lbl_cageno = ttk.Label(root, text="CAGE CODE: ", font="helvetica 13 bold")
lbl_cageno.grid(column=0, row=7, pady=5)

ent_cageno = ttk.Entry(root, font="helvetica 13", width=30, justify="left")
ent_cageno.grid(column=1, row=7, pady=5)

# MIL-STD
lbl_mil_std = ttk.Label(root, text="MIL-STD: ", font="helvetica 13 bold")
lbl_mil_std.grid(column=0, row=8, pady=5)

# Manual Type
lbl_man_type = ttk.Label(root, text="MANUAL TYPE: ", font="helvetica 13 bold")
lbl_man_type.grid(column=2, row=8, pady=5)

maincombo()

# OPTIONAL CHAPTERS
lbl_blank = ttk.Label(root, text="", font="helvetica 13 bold", anchor="w", width=35)
lbl_blank.grid(column=1, row=9, pady=6)
lbl_add_chapters = ttk.Label(
    root,
    text="ADD OPTIONAL CHAPTERS:",
    font="helvetica 13 bold",
    anchor="w",
    width=35,
)
lbl_add_chapters.grid(column=1, row=10, pady=5)

chb_tmi = ttk.IntVar()
chb_1 = ttk.IntVar()
chb_2 = ttk.IntVar()
chb_3 = ttk.IntVar()
chb_4 = ttk.IntVar()
chb_5 = ttk.IntVar()
chb_6 = ttk.IntVar()

chbox_tmi = ttk.Checkbutton(
    root,
    text="Troubleshooting Master Index",
    variable=chb_tmi,
    onvalue=1,
    offvalue=0,
    width=50,
    style="Custom.TCheckbutton",
)
chbox_tmi.grid(column=1, row=11, sticky=W)

chbox_1 = ttk.Checkbutton(
    root,
    text="Auxillary Equipment Maintenance Instructions",
    variable=chb_1,
    onvalue=1,
    offvalue=0,
    width=50,
    style="Custom.TCheckbutton",
)
chbox_1.grid(column=1, row=12, sticky=W)

chbox_2 = ttk.Checkbutton(
    root,
    text="Ammunition Maintenance Instructions",
    variable=chb_2,
    onvalue=1,
    offvalue=0,
    width=50,
    style="Custom.TCheckbutton",
)
chbox_2.grid(column=1, row=13, sticky=W)

chbox_3 = ttk.Checkbutton(
    root,
    text="Test and Inspection Maintenance Instructions",
    variable=chb_3,
    onvalue=1,
    offvalue=0,
    width=50,
    state="disabled",
    style="Custom.TCheckbutton",
)
chbox_3.grid(column=1, row=14, sticky=W)

chbox_4 = ttk.Checkbutton(
    root,
    text="Shipment/Movementand Storage Maintenance Instructions",
    variable=chb_4,
    onvalue=1,
    offvalue=0,
    width=50,
    state="disabled",
    style="Custom.TCheckbutton",
)
chbox_4.grid(column=1, row=15, sticky=W)

chbox_5 = ttk.Checkbutton(
    root,
    text="Destruction of Equipment to Prevent Enemy Use",
    variable=chb_5,
    onvalue=1,
    offvalue=0,
    width=50,
    style="Custom.TCheckbutton",
)
chbox_5.grid(column=1, row=16, sticky=W)

chbox_6 = ttk.Checkbutton(
    root,
    text="Software Information",
    variable=chb_6,
    onvalue=1,
    offvalue=0,
    width=50,
    state="disabled",
    style="Custom.TCheckbutton",
)
chbox_6.grid(column=1, row=17, sticky=W)

# Create a custom style for the Checkbutton font
style = ttk.Style()
style.configure("Custom.TCheckbutton", font=("Helvetica", 13, "bold"))

# Autofill Button
btn_autofill = ttk.Button(
    root,
    text="AUTOFILL FORM",
    command=autofill,
    width=16,
)
btn_autofill.grid(column=3, row=9, pady=5)

# TM Tracker Button
btn_tm_tracker = ttk.Button(
    root,
    text="SELECT TRACKER",
    command=open_tm_tracker,
    width=16,
    # style="Select.TCheckbutton",
    style=CUSTOM_TBUTTON,
)
btn_tm_tracker.grid(column=3, row=11, pady=5)

# Clear Button
btn_clear = ttk.Button(
    root,
    text="CLEAR FORM",
    command=clear_form,
    width=16,
    # style="Clear.TCheckbutton",
    style=CUSTOM_TBUTTON,
)
btn_clear.grid(column=3, row=13, pady=5)

# Build TM Button
btn_build = ttk.Button(
    root,
    text="BUILD TM",
    command=save_folder,
    width=16,
    # style="Build.TCheckbutton",
    style=CUSTOM_TBUTTON,
)
btn_build.grid(column=3, row=15, pady=5)

# Create custom styles for the Buttons
style.configure(
    "Select.TCheckbutton",
    font=("Helvetica", 13, "bold"),
    bootstyle=PRIMARY,
    justify=LEFT,
)
style.configure(
    "Clear.TCheckbutton", font=("Helvetica", 13, "bold"), bootstyle=DANGER, justify=LEFT
)
style.configure(
    "Build.TCheckbutton",
    font=("Helvetica", 13, "bold"),
    bootstyle=SUCCESS,
    justify=LEFT,
)

# Create a custom style for the buttons with the dominant color
DOMINANT_COLOR = "#2067AD"
SUBORDINATE_COLOR = "#FFFFFF"
trg_style = ttk.Style()
trg_style.configure(
    CUSTOM_TBUTTON,
    font=("Helvetica", 14, "bold"),
    padding=10,
    relief="flat",
    foreground=SUBORDINATE_COLOR,
    background=DOMINANT_COLOR,
)


root.mainloop()
