""" TM SHELL GENERATOR """
import os
# from plistlib import InvalidFileException
import shutil
import tkinter as tk
from tkinter import Button, Checkbutton, filedialog, Entry, IntVar, Label, messagebox, StringVar
from tkinter.ttk import Combobox
from dotenv import dotenv_values
import chapters.ammunition as a
import chapters.ammunition_marking as am
import chapters.auxiliary_equipment as ae
import chapters.chapter1 as ch1
import chapters.destruction as d
import chapters.entity_declarations as ed
import chapters.front_matter as fm
import chapters.operator_instructions as oi
import chapters.parts_information as pi
import chapters.procedures_d as dp
import chapters.procedures_m as mp
import chapters.procedures_o as op
import chapters.pmcs_m as pm
import chapters.pmcs_o as po
import chapters.rear_matter as rm
import chapters.shipment_instructions as sms
import chapters.software_information as s
import chapters.supporting_information as si
import chapters.ts_depot as td
import chapters.ts_maintainer as tm
import chapters.ts_master_index_o as tsmi_o
import chapters.ts_operator as to
from chapters import rpstl
import openpyxl as xl
from itertools import islice
import cfg

config = dotenv_values(".env")  # take environment variables from .env.

global chbox_1, chbox_2, chbox_3, chbox_4, chbox_5, chbox_6
errors = []
manual = ''
milstd = ''
CBX_MANUAL = ''
CBX_MIL_STD = ''
TAB_2 = '\t\t'
TAB_3 = '\t\t\t'
TAB_4 = '\t\t\t\t'
TAB_5 = '\t\t\t\t\t'
TAB_6 = '\t\t\t\t\t\t'
TAB_7 = '\t\t\t\t\t\t\t'
TAB_8 = '\t\t\t\t\t\t\t\t'

excelFile = None
workbook = None
ws = None

def form_validation(save_path) -> None:
    """Validates the items that are part of the form.
    Turns input fields red if empty. Adds error messages to the errors list."""
    global errors, SYS_ACRONYM, SYS_NUMBER, SYS_NAME, FSC, NIIN, PART_NO, UOC
    errors = []
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
        errors.append('SYSTEM NAME is required.\n')
    else:
        lbl_sys_name.configure(fg='black')
    if SYS_ACRONYM == '':
        lbl_sys_acronym.configure(fg='red')
        errors.append('SYSTEM ACRONYM is required.\n')
    else:
        lbl_sys_acronym.configure(fg='black')
    if SYS_NUMBER == '':
        lbl_sys_number.configure(fg='red')
        errors.append('SYSTEM NUMBER is required.\n')
    else:
        lbl_sys_number.configure(fg='black')
    if FSC == '':
        lbl_fsc.configure(fg='red')
        errors.append('FSC is required.\n')
    else:
        lbl_fsc.configure(fg='black')
    if NIIN == '':
        lbl_niin.configure(fg='red')
        errors.append('NIIN is required.\n')
    else:
        lbl_niin.configure(fg='black')
    if PART_NO == '':
        lbl_part_no.configure(fg='red')
        errors.append('PART NUMBER is required.\n')
    else:
        lbl_part_no.configure(fg='black')
    if UOC == '':
        lbl_uoc.configure(fg='red')
        errors.append('UOC is required.\n')
    else:
        lbl_uoc.configure(fg='black')
    # If errors list contains errors, display them in a message box.
    if errors:
        messagebox.showerror("Error", show_errors())
    # If no errors, build the TM.
    else:
        build_tm(save_path)

def show_errors() -> str:
    """Combines all form errors and returns them as a string."""
    error_string = ''
    for error in errors:
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
    if milstd == '2B' and manual == "-10":
        print('Building......................................' + manual + \
            ' TM Shell using MIL-STD-' + milstd)
        build_10_tm_2b(save_path)
    if milstd == '2B' and manual == "-13&P":
        print('Building......................................' + manual + \
            ' TM Shell using MIL-STD-' + milstd)
        build_13p_tm_2b(save_path)
    elif milstd == '2B' and manual == "-23&P":
        print('Building......................................' + manual + \
            ' TM Shell using MIL-STD-' + milstd)
        build_23p_tm_2b(save_path)
    elif milstd == '2B' and manual == "NMWR":
        print('Building......................................' + manual + \
            ' NMWR Shell using MIL-STD-' + milstd)
        build_nmwr_2b(save_path)
    if milstd == '2C' and manual == "-10":
        print('Building......................................' + manual + \
            ' TM Shell using MIL-STD-' + milstd)
        build_10_tm_2c(save_path)
    if milstd == '2C' and manual == "-13&P":
        print('Building......................................' + manual + \
            ' TM Shell using MIL-STD-' + milstd)
        build_13p_tm_2c(save_path)
    elif milstd == '2C' and manual == "-23&P":
        print('Building......................................' + manual + \
            ' TM Shell using MIL-STD-' + milstd)
        build_23p_tm_2c(save_path)
    elif milstd == '2C' and manual == "NMWR":
        print('Building......................................' + manual + \
            ' NMWR Shell using MIL-STD-' + milstd)
        build_nmwr_2c(save_path)
    elif milstd == '2D' and manual == "-10":
        print('Building......................................' + manual + \
            ' TM Shell using MIL-STD-' + milstd)
        build_10_tm_2d(save_path)
    elif milstd == '2D' and manual == "-12&P":
        print('Building......................................' + manual + \
            ' TM Shell using MIL-STD-' + milstd)
        build_12p_tm_2d(save_path)
    elif milstd == '2D' and manual == "NMWR":
        print('Building......................................' + manual + \
            ' NMWR Shell using MIL-STD-' + milstd)
        build_nmwr_2d(save_path)

def build_10_tm_2b(save_path) -> None:
    """Calls methods to build each work package for a -10 TM shell using MIL-STD-2B."""
    create_tm_wip_dir(save_path)
    ed.EntityDeclarations(SYS_ACRONYM, manual, milstd, save_path).entity_declarations()
    # FRONT MATTER
    front_matter = fm.FrontMatter(config, FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    front_matter.title_page()
    front_matter.loep()
    front_matter.tb_toc_htu()
    # CHAPTER1
    chapter1 = ch1.Chapter1(config, manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    chapter1.start()
    chapter1.general_info()
    chapter1.equipment_description()
    chapter1.theory_operations()
    chapter1.end()
    # OPERATOR INSTRUCTIONS
    oper_instructions = oi.OperatorInstructions(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_instructions.start()
    oper_instructions.controls_indicators()

    O = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        O += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.operation):
                O += 1
                for row2 in islice(ws.rows, O, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == 'O':
                            wp_title2 = wp_title2.replace("/", " or")
                            oper_instructions.operating_procedures(wpno, wp_title2)
                            if "unusual" in wp_title2:
                                oper_instructions.unusual_conditions(wpno)
                    if wp_title2:
                        if "chapter" in wp_title2:
                            break

    oper_instructions.end()
    # TROUBLESHOOTING MASTER INDEX
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.master_index):
                mi = tsmi_o.TSMasterIndex(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
                mi.start()
                mi.tsindxwp()
                mi.end()
    # OPERATOR TROUBLESHOOTING
    oper_ts = to.TSOperator(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_ts.start()
    oper_ts.tsintrowp()

    T = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        T += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.troubleshooting):
                T += 1
                for row2 in islice(ws.rows, T, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", " or")
                            if "troubleshooting index" in wp_title2.lower():
                                continue
                            else:
                                oper_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break

    oper_ts.end()
    # OPERATOR PMCS
    oper_pmcs = po.PMCS(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_pmcs.start()
    oper_pmcs.pmcsintrowp()
    P = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        P += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.operation):
                P += 1
                for row2 in islice(ws.rows, P, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'M':
                            if "before" in wp_title2.lower():
                                oper_pmcs.pmcs_before(wpno)
                            elif "during" in wp_title2.lower():
                                oper_pmcs.pmcs_during(wpno)
                            elif "after" in wp_title2.lower():
                                oper_pmcs.pmcs_after(wpno)
                            elif "daily" in wp_title2.lower():
                                oper_pmcs.pmcs_daily(wpno)
                            elif "weekly" in wp_title2.lower():
                                oper_pmcs.pmcs_weekly(wpno)
                            elif "monthly" in wp_title2.lower():
                                oper_pmcs.pmcs_monthly(wpno)
                            elif "quarterly" in wp_title2.lower():
                                oper_pmcs.pmcs_quarterly(wpno)
                            elif "semi" in wp_title2.lower():
                                oper_pmcs.pmcs_semi_annually(wpno)
                            elif "annually" in wp_title2.lower():
                                oper_pmcs.pmcs_annually(wpno)
                        else:
                            break
    oper_pmcs.end()
    # OPERATOR MAINTENANCE PROCEDURES
    oper_maintenance = op.OperatorProcedures(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_maintenance.start()

    M = 0
    for row in islice(ws.rows, 1,None):
        wp_title = row[2].value
        M += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.oper_main):
                M += 1
                for row2 in islice(ws.rows, M, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    proc_type = row2[3].value
                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", " or")
                            if proc_type:
                                if proc_type.lower() == "inspect":
                                    oper_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    oper_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    oper_maintenance.service(wpno, wp_title2)
                                elif proc_type.lower() == "remove":
                                    oper_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    oper_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "replace":
                                    oper_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    oper_maintenance.repair(wpno, wp_title2)
                                elif proc_type.lower() == "pack":
                                    oper_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    oper_maintenance.unpack(wpno, wp_title2)
                                elif proc_type.lower() == "clean":
                                    oper_maintenance.clean(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    oper_maintenance.prepforuse(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break
    oper_maintenance.end()
    # AUXILIARY EQUIPMENT - OPTIONAL
    if chb_1.get() == 1:
        aux_equip = ae.AuxiliaryEquipment(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        aux_equip.start()
        aux_equip.auxeqpwp()
        aux_equip.end()
    # AMMUNITION - OPTIONAL
    if chb_2.get() == 1:
        ammo = a.Ammunition(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        ammo.start()
        ammo.ammowp()
        ammo.ammo_markingwp()
        ammo.natowp()
        ammo.end()
    # DESTRUCTION - OPTIONAL
    if chb_5.get() == 1:
        destruct = d.Destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        destruct.start()
        destruct.destruct_introwp()
        for row in islice(ws.rows, 1 , None):
            wp_title = row[2].value
            wpno = row[1].value
            if wpno:
                if wpno[0] == 'D' and wpno[5] >= '2':
                    destruct.destruct_materialwp(wpno, wp_title)

        destruct.end()
    # SUPPORTING INFORMATION
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()

    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.support_info):
                S += 1
                for row2 in islice(ws.rows, S, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'S':
                            if wp_title2.lower() == "references":
                                support_info.refwp(wpno)
                            elif wp_title2.lower() == "coei & bii" or wp_title2.lower() == "coei and bii":
                                support_info.coeibiiwp(wpno)
                            elif wp_title2.lower().startswith("additional authorization list") or wp_title2.lower() == "aal":
                                support_info.aalwp(wpno)
                            elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                                support_info.explistwp(wpno)
                            elif wp_title2.lower().startswith("mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                                support_info.mrplwp(wpno)
                            elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith("csi"):
                                support_info.csi_wp(wpno)                          
                            elif wp_title2.lower().startswith("support items"):
                                support_info.supitemwp(wpno)
                            elif wp_title2.lower().startswith("additional supporting"):
                                support_info.genwp(wpno)

    support_info.end()
    rm.RearMatter(manual, SYS_ACRONYM, save_path).rear_matter()
    messagebox.showinfo("Success!")

def build_13p_tm_2b(save_path) -> None: 
    """Calls methods to build each work package for a -13&P TM shell using MIL-STD-2C."""
    create_tm_wip_dir(save_path)
    ed.EntityDeclarations(SYS_ACRONYM, manual, milstd, save_path).entity_declarations()
    # FRONT MATTER
    front_matter = fm.FrontMatter(config, FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    front_matter.title_page()
    front_matter.warning_summary()
    front_matter.loep()
    front_matter.tb_toc_htu()
    # CHAPTER1
    chapter1 = ch1.Chapter1(config, manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    chapter1.start()
    chapter1.general_info()
    chapter1.equipment_description()
    chapter1.theory_operations()
    chapter1.end()

    # OPERATOR INSTRUCTIONS
    oper_instructions = oi.OperatorInstructions(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_instructions.start()
    oper_instructions.controls_indicators()

    O = 1
    for row in islice(ws.rows, 1, None):
        O += 1
        wp_title = row[2].value
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.operation):
                O += 1
                for row2 in islice(ws.rows,O,None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value

                    if wpno:

                        if wpno[0] == 'O':
                            if "unusual" in wp_title2.lower():
                                oper_instructions.unusual_conditions(wpno)
                            else:
                                wp_title2 = wp_title2.replace("/", " or")
                                oper_instructions.operating_procedures(wpno, wp_title2)
                            
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break
    oper_instructions.end()
    # TROUBLESHOOTING MASTER INDEX
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.master_index):
                mi = tsmi_o.TSMasterIndex(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
                mi.start()
                mi.tsindxwp()
                mi.end()
    # OPERATOR TROUBLESHOOTING
    oper_ts = to.TSOperator(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_ts.start()
    oper_ts.tsintrowp()

    T = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        T += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.troubleshooting):
                T += 1
                for row2 in islice(ws.rows, T, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", " or")
                            if "troubleshooting index" in wp_title2.lower():
                                continue
                            else:
                                oper_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break
    oper_ts.end()
    # OPERATOR PMCS
    oper_pmcs = po.PMCS(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_pmcs.start()
    oper_pmcs.pmcsintrowp()
    P = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        P += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.operation):
                P += 1
                for row2 in islice(ws.rows, P, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'M':
                            if "before" in wp_title2.lower():
                                oper_pmcs.pmcs_before(wpno)
                            elif "during" in wp_title2.lower():
                                oper_pmcs.pmcs_during(wpno)
                            elif "after" in wp_title2.lower():
                                oper_pmcs.pmcs_after(wpno)
                            elif "daily" in wp_title2.lower():
                                oper_pmcs.pmcs_daily(wpno)
                            elif "weekly" in wp_title2.lower():
                                oper_pmcs.pmcs_weekly(wpno)
                            elif "monthly" in wp_title2.lower():
                                oper_pmcs.pmcs_monthly(wpno)
                            elif "quarterly" in wp_title2.lower():
                                oper_pmcs.pmcs_quarterly(wpno)
                            elif "semi" in wp_title2.lower():
                                oper_pmcs.pmcs_semi_annually(wpno)
                            elif "annually" in wp_title2.lower():
                                oper_pmcs.pmcs_annually(wpno)
                        else:
                            break
    oper_pmcs.end()
    # OPERATOR MAINTENANCE PROCEDURES
    oper_maintenance = op.OperatorProcedures(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_maintenance.start()
    x = 0
    for row in islice(ws.rows,1,None):
        wp_title = row[2].value
        x += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.oper_main):
                x += 1

                for row2 in islice(ws.rows,x,None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    proc_type = row2[3].value

                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", "or")
                            if proc_type:
                                if proc_type.lower() == "replace":
                                    oper_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "inspect":
                                    oper_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    oper_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    oper_maintenance.service(wpno,wp_title2)
                                elif proc_type.lower() == "remove":
                                    oper_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    oper_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    oper_maintenance.repair(wpno,wp_title2)
                                elif proc_type.lower() == "pack":
                                    oper_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    oper_maintenance.unpack(wpno,wp_title2)
                                elif proc_type.lower() == "clean":
                                    oper_maintenance.clean(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    oper_maintenance.prepforuse(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break
    oper_maintenance.end()
    # MAINTAINER TROUBLESHOOTING
    maint_ts = tm.TSMaintainer(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    maint_ts.start()
    maint_ts.tsintrowp()

    Mt = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Mt += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_troub):
                Mt += 1

                for row2 in islice(ws.rows, Mt, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", "or")
                            maint_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break

    maint_ts.end()
    # MAINTAINER PMCS
    main_pmcs = pm.PMCS(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    main_pmcs.start()
    main_pmcs.pmcsintrowp()
    P = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        P += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_pmcs):
                P += 1
                for row2 in islice(ws.rows, P, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'M':
                            if "before" in wp_title2.lower():
                                main_pmcs.pmcs_before(wpno)
                            elif "during" in wp_title2.lower():
                                main_pmcs.pmcs_during(wpno)
                            elif "after" in wp_title2.lower():
                                main_pmcs.pmcs_after(wpno)
                            elif "daily" in wp_title2.lower():
                                main_pmcs.pmcs_daily(wpno)
                            elif "weekly" in wp_title2.lower():
                                main_pmcs.pmcs_weekly(wpno)
                            elif "monthly" in wp_title2.lower():
                                main_pmcs.pmcs_monthly(wpno)
                            elif "quarterly" in wp_title2.lower():
                                main_pmcs.pmcs_quarterly(wpno)
                            elif "semi" in wp_title2.lower():
                                main_pmcs.pmcs_semi_annually(wpno)
                            elif "annually" in wp_title2.lower():
                                main_pmcs.pmcs_annually(wpno)
                        else:
                            break
    oper_pmcs.end()
    # MAINTAINER MAINTENANCE
    maint_maintenance = mp.MaintainerProcedures(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    maint_maintenance.start()

    y = 0
    for row in islice(ws.rows,1,None):
        wp_title = row[2].value
        y += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_main):
                y += 1

                for row2 in islice(ws.rows,y,None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    proc_type = row2[3].value

                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", " or")
                            if "service upon receipt" in wp_title2.lower():
                                maint_maintenance.surwp(wpno)
                            elif proc_type:
                                if proc_type.lower() == "replace":
                                    maint_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "inspect":
                                    maint_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    maint_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    maint_maintenance.service(wpno, wp_title2)
                                elif proc_type.lower() == "remove":
                                    maint_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    maint_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    maint_maintenance.repair(wpno, wp_title2)
                                elif proc_type.lower() == "pack":
                                    maint_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    maint_maintenance.unpack(wpno, wp_title2)
                                elif proc_type.lower() == "clean":
                                    maint_maintenance.clean(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    maint_maintenance.prepforuse(wpno, wp_title2)
                    if "chapter" in wp_title2.lower():
                        break
    maint_maintenance.end()
    # AUXILIARY EQUIPMENT - OPTIONAL
    if chb_1.get() == 1:
        aux_equip = ae.AuxiliaryEquipment(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        aux_equip.start()
        aux_equip.auxeqpwp()
        aux_equip.manu_items_introwp()
        aux_equip.manuwp()
        aux_equip.torquewp()
        aux_equip.wiringwp()
        aux_equip.end()
    # AMMUNITION - OPTIONAL
    if chb_2.get() == 1:
        ammunition = a.Ammunition(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        ammunition.start()
        ammunition.surwp()
        ammunition.ammowp()
        ammunition.ammo_markingwp()
        ammunition.natowp()
        ammunition.end()
    # PARTS INFORMATION
    parts_info = pi.PartsInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    parts_info.start()
    parts_info.introwp()
    Re = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Re += 1

        if wp_title:
            if any(s in wp_title.lower() for s in cfg.rpstl_check):
                Re += 1
                break
    for row2 in islice(ws.rows, Re, None):

        wpno2 = row2[1].value
        wp_title2 = row2[2].value
        wp_title2 = wp_title2.replace("/", " or")

        if wpno2:
            if wpno2[0] == "R":
                if "bulk items" in wp_title2.lower():
                    parts_info.bulk_itemswp(wpno2)
                elif "nsn index" in wp_title2.lower() or "national stock" in wp_title2.lower():
                    parts_info.nsnindxwp(wpno2)
                elif "pn index" in wp_title2.lower() or "part number" in wp_title2.lower():
                    parts_info.pnindxwp(wpno2)
                else:
                    parts_info.plwp(wpno2, wp_title2)
        if wp_title2:
            if "chapter" in wp_title2.lower():
                break

    parts_info.end()
    # DESTRUCTION - OPTIONAL
    if chb_5.get() == 1:
        destruct = d.Destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        destruct.start()
        destruct.destruct_introwp()
        for row in islice(ws.rows, 1 , None):
            wp_title = row[2].value
            wpno = row[1].value
            if wpno:
                if wpno[0] == 'D' and wpno[5] >= '2':
                    destruct.destruct_materialwp(wpno, wp_title)

        destruct.end()
    # SUPPORTING INFORMATION
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()

    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.support_info):
                S += 1
                for row2 in islice(ws.rows, S, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'S':
                            if "intro" in wp_title2.lower() or "introduction" in wp_title2.lower():
                                support_info.macintrowp(wpno)
                            elif wp_title2.lower() == "mac" or wp_title2.lower() == "maintenance allocation chart" or wp_title2.lower() == "maintenance allocation chart (mac)":
                                support_info.macwp(wpno)
                            elif wp_title2.lower() == "references":
                                support_info.refwp(wpno)
                            elif wp_title2.lower() == "coei & bii" or wp_title2.lower() == "coei and bii":
                                support_info.coeibiiwp(wpno)
                            elif wp_title2.lower().startswith("additional authorization list") or wp_title2.lower() == "aal":
                                support_info.aalwp(wpno)
                            elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                                support_info.explistwp(wpno)
                            elif wp_title2.lower().startswith("tool") or wp_title2.lower().startswith("til"):
                                support_info.toolidwp(wpno)
                            elif wp_title2.lower().startswith("mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                                support_info.mrplwp(wpno)
                            elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith("csi"):
                                support_info.csi_wp(wpno)                          
                            elif wp_title2.lower().startswith("additional supporting"):
                                support_info.genwp(wpno)
    support_info.end()
    rm.RearMatter(manual, SYS_ACRONYM, save_path).rear_matter()
    messagebox.showinfo("Success!", "Your technical manual has been created.")

def build_23p_tm_2b(save_path) -> None:
    """Calls methods to build each work package for a -23&P TM shell using MIL-STD-2B."""
    create_tm_wip_dir(save_path)
    ed.EntityDeclarations(SYS_ACRONYM, manual, milstd, save_path).entity_declarations()
    # FRONT MATTER
    front_matter = fm.FrontMatter(config, FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    front_matter.title_page()
    front_matter.warning_summary()
    front_matter.loep()
    front_matter.tb_toc_htu()
    # CHAPTER1
    chapter1 = ch1.Chapter1(config, manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    chapter1.start()
    chapter1.general_info()
    chapter1.equipment_description()
    chapter1.theory_operations()
    chapter1.end()
    # TROUBLESHOOTING MASTER INDEX
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.master_index):
                mi = tsmi_o.TSMasterIndex(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
                mi.start()
                mi.tsindxwp()
                mi.end()
    # MAINTAINER TROUBLESHOOTING
    maint_ts = tm.TSMaintainer(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    maint_ts.start()
    maint_ts.tsintrowp()

    Mt = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Mt += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_troub):
                Mt += 1

                for row2 in islice(ws.rows, Mt, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", "or")
                            maint_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break

    maint_ts.end()
    # MAINTAINER PMCS
    main_pmcs = pm.PMCS(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    main_pmcs.start()
    main_pmcs.pmcsintrowp()
    P = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        P += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_pmcs):
                P += 1
                for row2 in islice(ws.rows, P, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'M':
                            if "before" in wp_title2.lower():
                                main_pmcs.pmcs_before(wpno)
                            elif "during" in wp_title2.lower():
                                main_pmcs.pmcs_during(wpno)
                            elif "after" in wp_title2.lower():
                                main_pmcs.pmcs_after(wpno)
                            elif "daily" in wp_title2.lower():
                                main_pmcs.pmcs_daily(wpno)
                            elif "weekly" in wp_title2.lower():
                                main_pmcs.pmcs_weekly(wpno)
                            elif "monthly" in wp_title2.lower():
                                main_pmcs.pmcs_monthly(wpno)
                            elif "quarterly" in wp_title2.lower():
                                main_pmcs.pmcs_quarterly(wpno)
                            elif "semi" in wp_title2.lower():
                                main_pmcs.pmcs_semi_annually(wpno)
                            elif "annually" in wp_title2.lower():
                                main_pmcs.pmcs_annually(wpno)
                        else:
                            break
    main_pmcs.end()
    # MAINTAINER MAINTENANCE
    maint_maintenance = mp.MaintainerProcedures(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    maint_maintenance.start()

    y = 0
    for row in islice(ws.rows,1,None):
        wp_title = row[2].value
        y += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_main):
                y += 1

                for row2 in islice(ws.rows,y,None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    proc_type = row2[3].value

                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", " or")
                            if "service upon receipt" in wp_title2.lower():
                                maint_maintenance.surwp(wpno)
                            elif proc_type:
                                if proc_type.lower() == "replace":
                                    maint_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "inspect":
                                    maint_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    maint_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    maint_maintenance.service(wpno, wp_title2)
                                elif proc_type.lower() == "remove":
                                    maint_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    maint_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    maint_maintenance.repair(wpno, wp_title2)
                                elif proc_type.lower() == "pack":
                                    maint_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    maint_maintenance.unpack(wpno, wp_title2)
                                elif proc_type.lower() == "clean":
                                    maint_maintenance.clean(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    maint_maintenance.prepforuse(wpno, wp_title2)
                    if "chapter" in wp_title2.lower():
                        break
    maint_maintenance.end()
    # AUXILIARY EQUIPMENT - OPTIONAL
    if chb_1.get() == 1:
        aux_equip = ae.AuxiliaryEquipment(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        aux_equip.start()
        aux_equip.auxeqpwp()
        aux_equip.manu_items_introwp()
        aux_equip.manuwp()
        aux_equip.torquewp()
        aux_equip.wiringwp()
        aux_equip.end()
    # AMMUNITION - OPTIONAL
    if chb_2.get() == 1:
        ammo = a.Ammunition(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        ammo.start()
        ammo.surwp()
        ammo.ammowp()
        ammo.ammo_markingwp()
        ammo.natowp()
        ammo.end()
    # PARTS INFORMATION
    parts_info = pi.PartsInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    parts_info.start()
    parts_info.introwp()
    Re = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Re += 1

        if wp_title:
            if any(s in wp_title.lower() for s in cfg.rpstl_check):
                Re += 1
                break
    for row2 in islice(ws.rows, Re, None):

        wpno2 = row2[1].value
        wp_title2 = row2[2].value
        wp_title2 = wp_title2.replace("/", " or")

        if wpno2:
            if wpno2[0] == "R":
                if "bulk items" in wp_title2.lower():
                    parts_info.bulk_itemswp(wpno2)
                elif "nsn index" in wp_title2.lower() or "national stock" in wp_title2.lower():
                    parts_info.nsnindxwp(wpno2)
                elif "pn index" in wp_title2.lower() or "part number" in wp_title2.lower():
                    parts_info.pnindxwp(wpno2)
                else:
                    parts_info.plwp(wpno2, wp_title2)
        if wp_title2:
            if "chapter" in wp_title2.lower():
                break

    parts_info.end()
    # DESTRUCTION - OPTIONAL
    if chb_5.get() == 1:
        destruct = d.Destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        destruct.start()
        destruct.destruct_introwp()
        for row in islice(ws.rows, 1 , None):
            wp_title = row[2].value
            wpno = row[1].value
            if wpno:
                if wpno[0] == 'D' and wpno[5] >= '2':
                    destruct.destruct_materialwp(wpno, wp_title)

        destruct.end()
    # SUPPORTING INFORMATION
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()

    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.support_info):
                S += 1
                for row2 in islice(ws.rows, S, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'S':
                            if "intro" in wp_title2.lower() or "introduction" in wp_title2.lower():
                                support_info.macintrowp(wpno)
                            elif wp_title2.lower() == "mac" or wp_title2.lower() == "maintenance allocation chart" or wp_title2.lower() == "maintenance allocation chart (mac)":
                                support_info.macwp(wpno)
                            elif wp_title2.lower() == "references":
                                support_info.refwp(wpno)
                            elif wp_title2.lower() == "coei & bii" or wp_title2.lower() == "coei and bii":
                                support_info.coeibiiwp(wpno)
                            elif wp_title2.lower().startswith("additional authorization list") or wp_title2.lower() == "aal":
                                support_info.aalwp(wpno)
                            elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                                support_info.explistwp(wpno)
                            elif wp_title2.lower().startswith("tool") or wp_title2.lower().startswith("til"):
                                support_info.toolidwp(wpno)
                            elif wp_title2.lower().startswith("mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                                support_info.mrplwp(wpno)
                            elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith("csi"):
                                support_info.csi_wp(wpno)                          
                            elif wp_title2.lower().startswith("additional supporting"):
                                support_info.genwp(wpno)
    support_info.end()
    rm.RearMatter(manual, SYS_ACRONYM, save_path).rear_matter()
    messagebox.showinfo("Success!", "Your technical manual has been created.")

def build_nmwr_2b(save_path) -> None:
    """Calls methods to build each work package for a NMWR shell using MIL-STD-2B."""
    create_tm_wip_dir(save_path)
    ed.EntityDeclarations(SYS_ACRONYM, manual, milstd, save_path).entity_declarations()
    # FRONT MATTER
    front_matter = fm.FrontMatter(config, FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    front_matter.title_page()
    front_matter.warning_summary()
    front_matter.loep()
    front_matter.tb_toc_htu()
    # CHAPTER1
    chapter1 = ch1.Chapter1(config, manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    chapter1.start()
    chapter1.general_info()
    chapter1.equipment_description()
    chapter1.theory_operations()
    chapter1.end()
    # DEPOT TROUBLESHOOTING
    depot_ts = td.TSDepot(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    depot_ts.start()

    Mt = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Mt += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.depot_troub):
                Mt += 1

                for row2 in islice(ws.rows, Mt, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", "or")
                            if "troubleshooting intro" in wp_title2.lower() or "troubleshooting introduction" in wp_title2.lower():
                                depot_ts.tsintrowp(wpno)
                            elif "troubleshooting index" in wp_title2.lower():
                                depot_ts.tsindxwp(wpno)
                            elif "preshop" in wp_title2.lower():
                                depot_ts.pshopanalwp(wpno)
                            elif "component" in wp_title2.lower() or "checklist" in wp_title2.lower():
                                depot_ts.compchklistwp(wpno)
                            else:
                                depot_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break

    depot_ts.end()
    # DEPOT MAINTENANCE PROCEDURES
    depot_maintenance = dp.DepotProcedures(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    depot_maintenance.start()
    y = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        y += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.depot_main):
                y += 1
                for row2 in islice(ws.rows, y, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    proc_type = row2[3].value

                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", " or")
                            if proc_type:
                                if proc_type.lower() == "clean":
                                    depot_maintenance.clean(wpno, wp_title2)
                                if proc_type.lower() == "replace":
                                    depot_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "inspect":
                                    depot_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    depot_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    depot_maintenance.service(wpno, wp_title2)
                                elif proc_type.lower() == "remove":
                                    depot_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    depot_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    depot_maintenance.repair(wpno, wp_title2)
                                elif proc_type.lower() == "pack":
                                    depot_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    depot_maintenance.unpack(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    depot_maintenance.prepforuse(wpno, wp_title2)
                            elif "preservation" in wp_title2.lower():
                                depot_maintenance.ppmgeninfowp(wpno)
                            elif "quality" in wp_title2.lower():
                                depot_maintenance.qawp(wpno)
                            else:
                                break
                    if "chapter" in wp_title2.lower():
                        break
    # Other WP's to add later...
    # depot_maintenance.facilwp()   # Optional
    # depot_maintenance.oipwp() # Optional
    # depot_maintenance.mobilwp()   # Optional
    # depot_maintenance.manu_items_introwp() # Optional
    # depot_maintenance.manuwp()    # Optional
    # depot_maintenance.torquewp()  # Optional
    # depot_maintenance.inventorywp()   # Optional
    # depot_maintenance.storagewp() # Optional
    # depot_maintenance.wiringwp()  # Optional
    depot_maintenance.end()
    # PARTS INFORMATION
    parts_info = pi.PartsInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    parts_info.start()
    parts_info.introwp()
    Re = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Re += 1

        if wp_title:
            if any(s in wp_title.lower() for s in cfg.rpstl_check):
                Re += 1
                break
    for row2 in islice(ws.rows, Re, None):

        wpno2 = row2[1].value
        wp_title2 = row2[2].value
        wp_title2 = wp_title2.replace("/", " or")

        if wpno2:
            if wpno2[0] == "R":
                if "bulk items" in wp_title2.lower():
                    parts_info.bulk_itemswp(wpno2)
                elif "nsn index" in wp_title2.lower() or "national stock" in wp_title2.lower():
                    parts_info.nsnindxwp(wpno2)
                elif "pn index" in wp_title2.lower() or "part number" in wp_title2.lower():
                    parts_info.pnindxwp(wpno2)
                else:
                    parts_info.plwp(wpno2, wp_title2)
        if wp_title2:
            if "chapter" in wp_title2.lower():
                break

    parts_info.end()
    # SUPPORTING INFORMATION
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()

    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.support_info):
                S += 1
                for row2 in islice(ws.rows, S, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'S':
                            if wp_title2.lower() == "references":
                                support_info.refwp(wpno)
                            elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                                support_info.explistwp(wpno)
                            elif wp_title2.lower().startswith("tool") or wp_title2.lower().startswith("til"):
                                support_info.toolidwp(wpno)
                            elif wp_title2.lower().startswith("mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                                support_info.mrplwp(wpno)
                            elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith("csi"):
                                support_info.csi_wp(wpno)
                            elif wp_title2.lower().startswith("additional supporting"):
                                support_info.genwp(wpno)
    support_info.end()
    rm.RearMatter(manual, SYS_ACRONYM, save_path).rear_matter()
    messagebox.showinfo("Success!", "Your NMWR has been created.")

def build_10_tm_2c(save_path) -> None:
    """Calls methods to build each work package for a -10 TM shell using MIL-STD-2C."""
    create_tm_wip_dir(save_path)
    ed.EntityDeclarations(SYS_ACRONYM, manual, milstd, save_path).entity_declarations()
    # FRONT MATTER
    front_matter = fm.FrontMatter(config, FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    front_matter.title_page()
    front_matter.loep()
    front_matter.tb_toc_htu()
    # CHAPTER1
    chapter1 = ch1.Chapter1(config, manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    chapter1.start()
    chapter1.general_info()
    chapter1.equipment_description()
    chapter1.theory_operations()
    chapter1.end()
    # OPERATOR INSTRUCTIONS
    oper_instructions = oi.OperatorInstructions(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_instructions.start()
    oper_instructions.controls_indicators()

    O = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        O += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.operation):
                O += 1
                for row2 in islice(ws.rows, O, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == 'O':
                            wp_title2 = wp_title2.replace("/", " or")
                            oper_instructions.operating_procedures(wpno, wp_title2)
                            if "unusual" in wp_title2:
                                oper_instructions.unusual_conditions(wpno)
                    if wp_title2:
                        if "chapter" in wp_title2:
                            break

    oper_instructions.end()
    # TROUBLESHOOTING MASTER INDEX
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.master_index):
                mi = tsmi_o.TSMasterIndex(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
                mi.start()
                mi.tsindxwp()
                mi.end()
    # OPERATOR TROUBLESHOOTING
    oper_ts = to.TSOperator(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_ts.start()
    oper_ts.tsintrowp()

    T = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        T += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.troubleshooting):
                T += 1
                for row2 in islice(ws.rows, T, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", " or")
                            if "troubleshooting index" in wp_title2.lower():
                                continue
                            else:
                                oper_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break

    oper_ts.end()
    # OPERATOR PMCS
    oper_pmcs = po.PMCS(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_pmcs.start()
    oper_pmcs.pmcsintrowp()
    P = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        P += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.operation):
                P += 1
                for row2 in islice(ws.rows, P, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'M':
                            if "before" in wp_title2.lower():
                                oper_pmcs.pmcs_before(wpno)
                            elif "during" in wp_title2.lower():
                                oper_pmcs.pmcs_during(wpno)
                            elif "after" in wp_title2.lower():
                                oper_pmcs.pmcs_after(wpno)
                            elif "daily" in wp_title2.lower():
                                oper_pmcs.pmcs_daily(wpno)
                            elif "weekly" in wp_title2.lower():
                                oper_pmcs.pmcs_weekly(wpno)
                            elif "monthly" in wp_title2.lower():
                                oper_pmcs.pmcs_monthly(wpno)
                            elif "quarterly" in wp_title2.lower():
                                oper_pmcs.pmcs_quarterly(wpno)
                            elif "semi" in wp_title2.lower():
                                oper_pmcs.pmcs_semi_annually(wpno)
                            elif "annually" in wp_title2.lower():
                                oper_pmcs.pmcs_annually(wpno)
                        else:
                            break
    oper_pmcs.end()
    # OPERATOR MAINTENANCE PROCEDURES
    oper_maintenance = op.OperatorProcedures(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_maintenance.start()

    M = 0
    for row in islice(ws.rows, 1,None):
        wp_title = row[2].value
        M += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.oper_main):
                M += 1
                for row2 in islice(ws.rows, M, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    proc_type = row2[3].value
                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", " or")
                            if proc_type:
                                if proc_type.lower() == "inspect":
                                    oper_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    oper_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    oper_maintenance.service(wpno, wp_title2)
                                elif proc_type.lower() == "remove":
                                    oper_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    oper_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "replace":
                                    oper_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    oper_maintenance.repair(wpno, wp_title2)
                                elif proc_type.lower() == "pack":
                                    oper_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    oper_maintenance.unpack(wpno, wp_title2)
                                elif proc_type.lower() == "clean":
                                    oper_maintenance.clean(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    oper_maintenance.prepforuse(wpno, wp_title2)
                                elif proc_type.lower() == "prepstore":
                                    oper_maintenance.prepstore(wpno, wp_title2)
                                elif proc_type.lower() == "prepship":
                                    oper_maintenance.prepship(wpno, wp_title2)
                                elif proc_type.lower() == "transport":
                                    oper_maintenance.transport(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break
    oper_maintenance.end()
    # AUXILIARY EQUIPMENT - OPTIONAL
    if chb_1.get() == 1:
        aux_equip = ae.AuxiliaryEquipment(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        aux_equip.start()
        aux_equip.auxeqpwp()
        aux_equip.end()
    # AMMUNITION - OPTIONAL
    if chb_2.get() == 1:
        ammo = a.Ammunition(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        ammo.start()
        ammo.ammowp()
        ammo.ammo_markingwp()
        ammo.natowp()
        ammo.end()
    # DESTRUCTION - OPTIONAL
    if chb_5.get() == 1:
        destruct = d.Destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        destruct.start()
        destruct.destruct_introwp()
        for row in islice(ws.rows, 1 , None):
            wp_title = row[2].value
            wpno = row[1].value
            if wpno:
                if wpno[0] == 'D' and wpno[5] >= '2':
                    destruct.destruct_materialwp(wpno, wp_title)

        destruct.end()
    # SOFTWARE INFORMATION - OPTIONAL
    if chb_6.get() == 1:
        software = s.SoftwareInformation(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        software.start()
        software.softginfowp()
        software.softsumwp()
        software.softeffectwp()
        software.softdiffversionwp()
        software.softfeaturescapwp()
        software.softscreendisplaywp()
        software.softmenuwp()
        software.softtoolswp()
        software.softsecprivwp()
        software.softsuperctrlswp()
        software.softpowerupwp()
        software.softaccesswp()
        software.end()
    # SUPPORTING INFORMATION
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()

    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.support_info):
                S += 1
                for row2 in islice(ws.rows, S, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'S':
                            if wp_title2.lower() == "references":
                                support_info.refwp(wpno)
                            elif wp_title2.lower() == "coei & bii" or wp_title2.lower() == "coei and bii":
                                support_info.coeibiiwp(wpno)
                            elif wp_title2.lower().startswith("additional authorization list") or wp_title2.lower() == "aal":
                                support_info.aalwp(wpno)
                            elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                                support_info.explistwp(wpno)
                            elif wp_title2.lower().startswith("tool") or wp_title2.lower().startswith("til"):
                                support_info.toolidwp(wpno)
                            elif wp_title2.lower().startswith("mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                                support_info.mrplwp(wpno)
                            elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith("csi"):
                                support_info.csi_wp(wpno)                          
                            elif wp_title2.lower().startswith("support items"):
                                support_info.supitemwp(wpno)
                            elif wp_title2.lower().startswith("additional supporting"):
                                support_info.genwp(wpno)

    support_info.end()
    rm.RearMatter(manual, SYS_ACRONYM, save_path).rear_matter()
    messagebox.showinfo("Success!", "Your technical manual has been created.")

def build_13p_tm_2c(save_path) -> None:
    """Calls methods to build each work package for a -13&P TM shell using MIL-STD-2C."""
    create_tm_wip_dir(save_path)
    ed.EntityDeclarations(SYS_ACRONYM, manual, milstd, save_path).entity_declarations()
    # FRONT MATTER
    front_matter = fm.FrontMatter(config, FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    front_matter.title_page()
    front_matter.warning_summary()
    front_matter.loep()
    front_matter.tb_toc_htu()
    # CHAPTER1
    chapter1 = ch1.Chapter1(config, manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    chapter1.start()
    chapter1.general_info()
    chapter1.equipment_description()
    chapter1.theory_operations()
    chapter1.end()

    # OPERATOR INSTRUCTIONS
    oper_instructions = oi.OperatorInstructions(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_instructions.start()
    oper_instructions.controls_indicators()

    O = 1
    for row in islice(ws.rows, 1, None):
        O += 1
        wp_title = row[2].value
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.operation):
                O += 1
                for row2 in islice(ws.rows,O,None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value

                    if wpno:

                        if wpno[0] == 'O':
                            if "unusual" in wp_title2.lower():
                                oper_instructions.unusual_conditions(wpno)
                            else:
                                wp_title2 = wp_title2.replace("/", " or")
                                oper_instructions.operating_procedures(wpno, wp_title2)
                            
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break
    oper_instructions.end()
    # TROUBLESHOOTING MASTER INDEX
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.master_index):
                mi = tsmi_o.TSMasterIndex(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
                mi.start()
                mi.tsindxwp()
                mi.end()
    # OPERATOR TROUBLESHOOTING
    oper_ts = to.TSOperator(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_ts.start()
    oper_ts.tsintrowp()

    T = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        T += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.troubleshooting):
                T += 1
                for row2 in islice(ws.rows, T, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", " or")
                            if "troubleshooting index" in wp_title2.lower():
                                continue
                            else:
                                oper_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break
    oper_ts.end()
    # OPERATOR PMCS
    oper_pmcs = po.PMCS(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_pmcs.start()
    oper_pmcs.pmcsintrowp()
    P = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        P += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.operation):
                P += 1
                for row2 in islice(ws.rows, P, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'M':
                            if "before" in wp_title2.lower():
                                oper_pmcs.pmcs_before(wpno)
                            elif "during" in wp_title2.lower():
                                oper_pmcs.pmcs_during(wpno)
                            elif "after" in wp_title2.lower():
                                oper_pmcs.pmcs_after(wpno)
                            elif "daily" in wp_title2.lower():
                                oper_pmcs.pmcs_daily(wpno)
                            elif "weekly" in wp_title2.lower():
                                oper_pmcs.pmcs_weekly(wpno)
                            elif "monthly" in wp_title2.lower():
                                oper_pmcs.pmcs_monthly(wpno)
                            elif "quarterly" in wp_title2.lower():
                                oper_pmcs.pmcs_quarterly(wpno)
                            elif "semi" in wp_title2.lower():
                                oper_pmcs.pmcs_semi_annually(wpno)
                            elif "annually" in wp_title2.lower():
                                oper_pmcs.pmcs_annually(wpno)
                        else:
                            break
    oper_pmcs.end()
    # OPERATOR MAINTENANCE PROCEDURES
    oper_maintenance = op.OperatorProcedures(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_maintenance.start()
    x = 0
    for row in islice(ws.rows,1,None):
        wp_title = row[2].value
        x += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.oper_main):
                x += 1

                for row2 in islice(ws.rows,x,None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    proc_type = row2[3].value

                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", "or")
                            if proc_type:
                                if proc_type.lower() == "replace":
                                    oper_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "inspect":
                                    oper_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    oper_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    oper_maintenance.service(wpno,wp_title2)
                                elif proc_type.lower() == "remove":
                                    oper_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    oper_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    oper_maintenance.repair(wpno,wp_title2)
                                elif proc_type.lower() == "pack":
                                    oper_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    oper_maintenance.unpack(wpno,wp_title2)
                                elif proc_type.lower() == "clean":
                                    oper_maintenance.clean(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    oper_maintenance.prepforuse(wpno, wp_title2)
                                elif proc_type.lower() == "prepstore":
                                    oper_maintenance.prepstore(wpno, wp_title2)
                                elif proc_type.lower() == "prepship":
                                    oper_maintenance.prepship(wpno, wp_title2)
                                elif proc_type.lower() == "transport":
                                    oper_maintenance.transport(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break
    oper_maintenance.end()
    # MAINTAINER TROUBLESHOOTING
    maint_ts = tm.TSMaintainer(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    maint_ts.start()
    maint_ts.tsintrowp()

    Mt = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Mt += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_troub):
                Mt += 1

                for row2 in islice(ws.rows, Mt, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", "or")
                            maint_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break

    maint_ts.end()
    # MAINTAINER PMCS
    main_pmcs = pm.PMCS(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    main_pmcs.start()
    main_pmcs.pmcsintrowp()
    P = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        P += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_pmcs):
                P += 1
                for row2 in islice(ws.rows, P, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'M':
                            if "before" in wp_title2.lower():
                                main_pmcs.pmcs_before(wpno)
                            elif "during" in wp_title2.lower():
                                main_pmcs.pmcs_during(wpno)
                            elif "after" in wp_title2.lower():
                                main_pmcs.pmcs_after(wpno)
                            elif "daily" in wp_title2.lower():
                                main_pmcs.pmcs_daily(wpno)
                            elif "weekly" in wp_title2.lower():
                                main_pmcs.pmcs_weekly(wpno)
                            elif "monthly" in wp_title2.lower():
                                main_pmcs.pmcs_monthly(wpno)
                            elif "quarterly" in wp_title2.lower():
                                main_pmcs.pmcs_quarterly(wpno)
                            elif "semi" in wp_title2.lower():
                                main_pmcs.pmcs_semi_annually(wpno)
                            elif "annually" in wp_title2.lower():
                                main_pmcs.pmcs_annually(wpno)
                        else:
                            break
    oper_pmcs.end()
    # MAINTAINER MAINTENANCE
    maint_maintenance = mp.MaintainerProcedures(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    maint_maintenance.start()

    y = 0
    for row in islice(ws.rows,1,None):
        wp_title = row[2].value
        y += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_main):
                y += 1

                for row2 in islice(ws.rows,y,None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    proc_type = row2[3].value

                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", " or")
                            if "service upon receipt" in wp_title2.lower():
                                maint_maintenance.surwp(wpno)
                            elif proc_type:
                                if proc_type.lower() == "replace":
                                    maint_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "inspect":
                                    maint_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    maint_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    maint_maintenance.service(wpno, wp_title2)
                                elif proc_type.lower() == "remove":
                                    maint_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    maint_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    maint_maintenance.repair(wpno, wp_title2)
                                elif proc_type.lower() == "pack":
                                    maint_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    maint_maintenance.unpack(wpno, wp_title2)
                                elif proc_type.lower() == "clean":
                                    maint_maintenance.clean(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    maint_maintenance.prepforuse(wpno, wp_title2)
                                elif proc_type.lower() == "prepstore":
                                    maint_maintenance.prepstore(wpno, wp_title2)
                                elif proc_type.lower() == "prepship":
                                    maint_maintenance.prepship(wpno, wp_title2)
                                elif proc_type.lower() == "transport":
                                    maint_maintenance.transport(wpno, wp_title2)
                    if "chapter" in wp_title2.lower():
                        break
    maint_maintenance.end()
    # AUXILIARY EQUIPMENT - OPTIONAL
    if chb_1.get() == 1:
        aux_equip = ae.AuxiliaryEquipment(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        aux_equip.start()
        aux_equip.auxeqpwp()
        aux_equip.manu_items_introwp()
        aux_equip.manuwp()
        aux_equip.torquewp()
        aux_equip.wiringwp()
        aux_equip.end()
    # AMMUNITION - OPTIONAL
    if chb_2.get() == 1:
        ammunition = a.Ammunition(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        ammunition.start()
        ammunition.surwp()
        ammunition.ammowp()
        ammunition.ammo_markingwp()
        ammunition.natowp()
        ammunition.end()
    # DESTRUCTION - OPTIONAL
    if chb_5.get() == 1:
        destruct = d.Destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        destruct.start()
        destruct.destruct_introwp()
        for row in islice(ws.rows, 1 , None):
            wp_title = row[2].value
            wpno = row[1].value
            if wpno:
                if wpno[0] == 'D' and wpno[5] >= '2':
                    destruct.destruct_materialwp(wpno, wp_title)

        destruct.end()
    # SOFTWARE INFORMATION - OPTIONAL
    if chb_6.get() == 1:
        software = s.SoftwareInformation(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        software.start()
        software.softginfowp()
        software.softsumwp()
        software.softeffectwp()
        software.softdiffversionwp()
        software.softfeaturescapwp()
        software.softscreendisplaywp()
        software.softmenuwp()
        software.softtoolswp()
        software.softsecprivwp()
        software.softsuperctrlswp()
        software.softpowerupwp()
        software.softaccesswp()
        software.end()
    # RPSTL
    repair_parts = rpstl.Rpstl(config, manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    repair_parts.start()
    repair_parts.introwp()
    Re = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Re += 1

        if wp_title:
            if any(s in wp_title.lower() for s in cfg.rpstl_check):
                Re += 1
                break
    for row2 in islice(ws.rows, Re, None):

        wpno2 = row2[1].value
        wp_title2 = row2[2].value
        wp_title2 = wp_title2.replace("/", " or")

        if wpno2:
            if wpno2[0] == "R":
                if "bulk items" in wp_title2.lower():
                    repair_parts.bulk_itemswp(wpno2)
                elif "nsn index" in wp_title2.lower() or "national stock" in wp_title2.lower():
                    repair_parts.nsnindxwp(wpno2)
                elif "pn index" in wp_title2.lower() or "part number" in wp_title2.lower():
                    repair_parts.pnindxwp(wpno2)
                else:
                    repair_parts.plwp(wpno2, wp_title2)
        if wp_title2:
            if "chapter" in wp_title2.lower():
                break

    repair_parts.end()
    # SUPPORTING INFORMATION
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()

    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.support_info):
                S += 1
                for row2 in islice(ws.rows, S, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'S':
                            if "intro" in wp_title2.lower() or "introduction" in wp_title2.lower():
                                support_info.macintrowp(wpno)
                            elif wp_title2.lower() == "mac" or wp_title2.lower() == "maintenance allocation chart" or wp_title2.lower() == "maintenance allocation chart (mac)":
                                support_info.macwp(wpno)
                            elif wp_title2.lower() == "references":
                                support_info.refwp(wpno)
                            elif wp_title2.lower() == "coei & bii" or wp_title2.lower() == "coei and bii":
                                support_info.coeibiiwp(wpno)
                            elif wp_title2.lower().startswith("additional authorization list") or wp_title2.lower() == "aal":
                                support_info.aalwp(wpno)
                            elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                                support_info.explistwp(wpno)
                            elif wp_title2.lower().startswith("tool") or wp_title2.lower().startswith("til"):
                                support_info.toolidwp(wpno)
                            elif wp_title2.lower().startswith("mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                                support_info.mrplwp(wpno)
                            elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith("csi"):
                                support_info.csi_wp(wpno)                          
                            elif wp_title2.lower().startswith("support items"):
                                support_info.supitemwp(wpno)
                            elif wp_title2.lower().startswith("additional supporting"):
                                support_info.genwp(wpno)
    support_info.end()
    rm.RearMatter(manual, SYS_ACRONYM, save_path).rear_matter()
    messagebox.showinfo("Success!", "Your technical manual has been created.")

def build_23p_tm_2c(save_path) -> None:
    """Calls methods to build each work package for a -23&P TM shell using MIL-STD-2C."""
    create_tm_wip_dir(save_path)
    ed.EntityDeclarations(SYS_ACRONYM, manual, milstd, save_path).entity_declarations()
    # FRONT MATTER
    front_matter = fm.FrontMatter(config, FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    front_matter.title_page()
    front_matter.warning_summary()
    front_matter.loep()
    front_matter.tb_toc_htu()
    # CHAPTER1
    chapter1 = ch1.Chapter1(config, manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    chapter1.start()
    chapter1.general_info()
    chapter1.equipment_description()
    chapter1.theory_operations()
    chapter1.end()
    # TROUBLESHOOTING MASTER INDEX
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.master_index):
                mi = tsmi_o.TSMasterIndex(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
                mi.start()
                mi.tsindxwp()
                mi.end()
    # MAINTAINER TROUBLESHOOTING
    maint_ts = tm.TSMaintainer(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    maint_ts.start()
    maint_ts.tsintrowp()

    Mt = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Mt += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_troub):
                Mt += 1

                for row2 in islice(ws.rows, Mt, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", "or")
                            maint_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break

    maint_ts.end()
    # MAINTAINER PMCS
    main_pmcs = pm.PMCS(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    main_pmcs.start()
    main_pmcs.pmcsintrowp()
    P = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        P += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_pmcs):
                P += 1
                for row2 in islice(ws.rows, P, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'M':
                            if "before" in wp_title2.lower():
                                main_pmcs.pmcs_before(wpno)
                            elif "during" in wp_title2.lower():
                                main_pmcs.pmcs_during(wpno)
                            elif "after" in wp_title2.lower():
                                main_pmcs.pmcs_after(wpno)
                            elif "daily" in wp_title2.lower():
                                main_pmcs.pmcs_daily(wpno)
                            elif "weekly" in wp_title2.lower():
                                main_pmcs.pmcs_weekly(wpno)
                            elif "monthly" in wp_title2.lower():
                                main_pmcs.pmcs_monthly(wpno)
                            elif "quarterly" in wp_title2.lower():
                                main_pmcs.pmcs_quarterly(wpno)
                            elif "semi" in wp_title2.lower():
                                main_pmcs.pmcs_semi_annually(wpno)
                            elif "annually" in wp_title2.lower():
                                main_pmcs.pmcs_annually(wpno)
                        else:
                            break
    main_pmcs.end()
    # MAINTAINER MAINTENANCE
    maint_maintenance = mp.MaintainerProcedures(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    maint_maintenance.start()

    y = 0
    for row in islice(ws.rows,1,None):
        wp_title = row[2].value
        y += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_main):
                y += 1

                for row2 in islice(ws.rows,y,None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    proc_type = row2[3].value

                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", " or")
                            if "service upon receipt" in wp_title2.lower():
                                maint_maintenance.surwp(wpno)
                            elif proc_type:
                                if proc_type.lower() == "replace":
                                    maint_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "inspect":
                                    maint_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    maint_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    maint_maintenance.service(wpno, wp_title2)
                                elif proc_type.lower() == "remove":
                                    maint_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    maint_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    maint_maintenance.repair(wpno, wp_title2)
                                elif proc_type.lower() == "pack":
                                    maint_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    maint_maintenance.unpack(wpno, wp_title2)
                                elif proc_type.lower() == "clean":
                                    maint_maintenance.clean(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    maint_maintenance.prepforuse(wpno, wp_title2)
                                elif proc_type.lower() == "prepstore":
                                    maint_maintenance.prepstore(wpno, wp_title2)
                                elif proc_type.lower() == "prepship":
                                    maint_maintenance.prepship(wpno, wp_title2)
                                elif proc_type.lower() == "transport":
                                    maint_maintenance.transport(wpno, wp_title2)
                    if "chapter" in wp_title2.lower():
                        break
    maint_maintenance.end()
    # AUXILIARY EQUIPMENT - OPTIONAL
    if chb_1.get() == 1:
        aux_equip = ae.AuxiliaryEquipment(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        aux_equip.start()
        aux_equip.auxeqpwp()
        aux_equip.manu_items_introwp()
        aux_equip.manuwp()
        aux_equip.torquewp()
        aux_equip.wiringwp()
        aux_equip.end()
    # AMMUNITION - OPTIONAL
    if chb_2.get() == 1:
        ammo = a.Ammunition(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        ammo.start()
        ammo.surwp()
        ammo.ammowp()
        ammo.ammo_markingwp()
        ammo.natowp()
        ammo.end()
    # DESTRUCTION - OPTIONAL
    if chb_5.get() == 1:
        destruct = d.Destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        destruct.start()
        destruct.destruct_introwp()
        for row in islice(ws.rows, 1 , None):
            wp_title = row[2].value
            wpno = row[1].value
            if wpno:
                if wpno[0] == 'D' and wpno[5] >= '2':
                    destruct.destruct_materialwp(wpno, wp_title)

        destruct.end()
    # SOFTWARE INFORMATION - OPTIONAL
    if chb_6.get() == 1:
        software = s.SoftwareInformation(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        software.start()
        software.softginfowp()
        software.softsumwp()
        software.softeffectwp()
        software.softdiffversionwp()
        software.softfeaturescapwp()
        software.softscreendisplaywp()
        software.softmenuwp()
        software.softtoolswp()
        software.softsecprivwp()
        software.softsuperctrlswp()
        software.softpowerupwp()
        software.softaccesswp()
        software.end()
    # RPSTL
    repair_parts = rpstl.Rpstl(config, manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    repair_parts.start()
    repair_parts.introwp()
    Re = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Re += 1

        if wp_title:
            if any(s in wp_title.lower() for s in cfg.rpstl_check):
                Re += 1
                break
    for row2 in islice(ws.rows, Re, None):

        wpno2 = row2[1].value
        wp_title2 = row2[2].value
        wp_title2 = wp_title2.replace("/", " or")

        if wpno2:
            if wpno2[0] == "R":
                if "bulk items" in wp_title2.lower():
                    repair_parts.bulk_itemswp(wpno2)
                elif "nsn index" in wp_title2.lower() or "national stock" in wp_title2.lower():
                    repair_parts.nsnindxwp(wpno2)
                elif "pn index" in wp_title2.lower() or "part number" in wp_title2.lower():
                    repair_parts.pnindxwp(wpno2)
                else:
                    repair_parts.plwp(wpno2, wp_title2)
        if wp_title2:
            if "chapter" in wp_title2.lower():
                break

    repair_parts.end()
    # SUPPORTING INFORMATION
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()

    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.support_info):
                S += 1
                for row2 in islice(ws.rows, S, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'S':
                            if "intro" in wp_title2.lower() or "introduction" in wp_title2.lower():
                                support_info.macintrowp(wpno)
                            elif wp_title2.lower() == "mac" or wp_title2.lower() == "maintenance allocation chart" or wp_title2.lower() == "maintenance allocation chart (mac)":
                                support_info.macwp(wpno)
                            elif wp_title2.lower() == "references":
                                support_info.refwp(wpno)
                            elif wp_title2.lower() == "coei & bii" or wp_title2.lower() == "coei and bii":
                                support_info.coeibiiwp(wpno)
                            elif wp_title2.lower().startswith("additional authorization list") or wp_title2.lower() == "aal":
                                support_info.aalwp(wpno)
                            elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                                support_info.explistwp(wpno)
                            elif wp_title2.lower().startswith("tool") or wp_title2.lower().startswith("til"):
                                support_info.toolidwp(wpno)
                            elif wp_title2.lower().startswith("mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                                support_info.mrplwp(wpno)
                            elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith("csi"):
                                support_info.csi_wp(wpno)                          
                            elif wp_title2.lower().startswith("support items"):
                                support_info.supitemwp(wpno)
                            elif wp_title2.lower().startswith("additional supporting"):
                                support_info.genwp(wpno)
    support_info.end()
    rm.RearMatter(manual, SYS_ACRONYM, save_path).rear_matter()
    messagebox.showinfo("Success!", "Your technical manual has been created.")

def build_nmwr_2c(save_path) -> None:
    """Calls methods to build each work package for a NMWR shell using MIL-STD-2C."""
    create_tm_wip_dir(save_path)
    ed.EntityDeclarations(SYS_ACRONYM, manual, milstd, save_path).entity_declarations()
    # FRONT MATTER
    front_matter = fm.FrontMatter(config, FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    front_matter.title_page()
    front_matter.warning_summary()
    front_matter.loep()
    front_matter.tb_toc_htu()
    # CHAPTER1
    chapter1 = ch1.Chapter1(config, manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    chapter1.start()
    chapter1.general_info()
    chapter1.equipment_description()
    chapter1.theory_operations()
    chapter1.end()
    # DEPOT TROUBLESHOOTING
    depot_ts = td.TSDepot(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    depot_ts.start()

    Mt = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Mt += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.depot_troub):
                Mt += 1

                for row2 in islice(ws.rows, Mt, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", "or")
                            if "troubleshooting intro" in wp_title2.lower() or "troubleshooting introduction" in wp_title2.lower():
                                depot_ts.tsintrowp(wpno)
                            elif "troubleshooting index" in wp_title2.lower():
                                depot_ts.tsindxwp(wpno)
                            elif "preshop" in wp_title2.lower():
                                depot_ts.pshopanalwp(wpno)
                            elif "component" in wp_title2.lower() or "checklist" in wp_title2.lower():
                                depot_ts.compchklistwp(wpno)
                            else:
                                depot_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break

    depot_ts.end()
    # DEPOT MAINTENANCE PROCEDURES
    depot_maintenance = dp.DepotProcedures(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    depot_maintenance.start()
    y = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        y += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.depot_main):
                y += 1
                for row2 in islice(ws.rows, y, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    proc_type = row2[3].value

                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", " or")
                            if proc_type:
                                if proc_type.lower() == "clean":
                                    depot_maintenance.clean(wpno, wp_title2)
                                if proc_type.lower() == "replace":
                                    depot_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "inspect":
                                    depot_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    depot_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    depot_maintenance.service(wpno, wp_title2)
                                elif proc_type.lower() == "remove":
                                    depot_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    depot_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    depot_maintenance.repair(wpno, wp_title2)
                                elif proc_type.lower() == "pack":
                                    depot_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    depot_maintenance.unpack(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    depot_maintenance.prepforuse(wpno, wp_title2)
                            elif "preservation" in wp_title2.lower():
                                depot_maintenance.ppmgeninfowp(wpno)
                            elif "quality" in wp_title2.lower():
                                depot_maintenance.qawp(wpno)
                            else:
                                break
                    if "chapter" in wp_title2.lower():
                        break
    # Other WP's to add later...
    # depot_maintenance.facilwp()   # Optional
    # depot_maintenance.oipwp() # Optional
    # depot_maintenance.mobilwp()   # Optional
    # depot_maintenance.manu_items_introwp() # Optional
    # depot_maintenance.manuwp()    # Optional
    # depot_maintenance.torquewp()  # Optional
    # depot_maintenance.inventorywp()   # Optional
    # depot_maintenance.storagewp() # Optional
    # depot_maintenance.wiringwp()  # Optional
    depot_maintenance.end()
    # RPSTL
    repair_parts = rpstl.Rpstl(config, manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    repair_parts.start()
    repair_parts.introwp()
    Re = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Re += 1

        if wp_title:
            if any(s in wp_title.lower() for s in cfg.rpstl_check):
                Re += 1
                break
    for row2 in islice(ws.rows, Re, None):

        wpno2 = row2[1].value
        wp_title2 = row2[2].value
        wp_title2 = wp_title2.replace("/", " or")

        if wpno2:
            if wpno2[0] == "R":
                if "bulk items" in wp_title2.lower():
                    repair_parts.bulk_itemswp(wpno2)
                elif "nsn index" in wp_title2.lower() or "national stock" in wp_title2.lower():
                    repair_parts.nsnindxwp(wpno2)
                elif "pn index" in wp_title2.lower() or "part number" in wp_title2.lower():
                    repair_parts.pnindxwp(wpno2)
                else:
                    repair_parts.plwp(wpno2, wp_title2)
        if wp_title2:
            if "chapter" in wp_title2.lower():
                break

    repair_parts.end()
    # SUPPORTING INFORMATION
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()

    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.support_info):
                S += 1
                for row2 in islice(ws.rows, S, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'S':
                            if wp_title2.lower() == "references":
                                support_info.refwp(wpno)
                            elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                                support_info.explistwp(wpno)
                            elif wp_title2.lower().startswith("tool") or wp_title2.lower().startswith("til"):
                                support_info.toolidwp(wpno)
                            elif wp_title2.lower().startswith("mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                                support_info.mrplwp(wpno)
                            elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith("csi"):
                                support_info.csi_wp(wpno)
                            elif wp_title2.lower().startswith("additional supporting"):
                                support_info.genwp(wpno)
    support_info.end()
    rm.RearMatter(manual, SYS_ACRONYM, save_path).rear_matter()
    messagebox.showinfo("Success!", "Your NMWR has been created.")

def build_10_tm_2d(save_path) -> None:
    """Calls methods to build each work package for a -10 TM shell using MIL-STD-2D."""
    create_tm_wip_dir(save_path)
    ed.EntityDeclarations(SYS_ACRONYM, manual, milstd, save_path).entity_declarations()
    # FRONT MATTER
    front_matter = fm.FrontMatter(config, FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    front_matter.title_page()
    front_matter.loep()
    front_matter.tb_toc_htu()
    # CHAPTER1
    chapter1 = ch1.Chapter1(config, manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    chapter1.start()
    chapter1.general_info()
    chapter1.equipment_description()
    chapter1.theory_operations()
    chapter1.end()
    # OPERATOR INSTRUCTIONS
    oper_instructions = oi.OperatorInstructions(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_instructions.start()
    oper_instructions.controls_indicators()

    O = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        O += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.operation):
                O += 1
                for row2 in islice(ws.rows, O, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == 'O':
                            wp_title2 = wp_title2.replace("/", " or")
                            oper_instructions.operating_procedures(wpno, wp_title2)
                            if "unusual" in wp_title2:
                                oper_instructions.unusual_conditions(wpno)
                    if wp_title2:
                        if "chapter" in wp_title2:
                            break

    oper_instructions.end()
    # TROUBLESHOOTING MASTER INDEX
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.master_index):
                mi = tsmi_o.TSMasterIndex(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
                mi.start()
                mi.tsindxwp()
                mi.end()
    # OPERATOR TROUBLESHOOTING
    oper_ts = to.TSOperator(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_ts.start()
    oper_ts.tsintrowp()

    T = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        T += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.troubleshooting):
                T += 1
                for row2 in islice(ws.rows, T, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", " or")
                            if "troubleshooting index" in wp_title2.lower():
                                continue
                            else:
                                oper_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break

    oper_ts.end()
    # OPERATOR PMCS
    oper_pmcs = po.PMCS(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_pmcs.start()
    oper_pmcs.pmcsintrowp()
    P = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        P += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.operation):
                P += 1
                for row2 in islice(ws.rows, P, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'M':
                            if "before" in wp_title2.lower():
                                oper_pmcs.pmcs_before(wpno)
                            elif "during" in wp_title2.lower():
                                oper_pmcs.pmcs_during(wpno)
                            elif "after" in wp_title2.lower():
                                oper_pmcs.pmcs_after(wpno)
                            elif "daily" in wp_title2.lower():
                                oper_pmcs.pmcs_daily(wpno)
                            elif "weekly" in wp_title2.lower():
                                oper_pmcs.pmcs_weekly(wpno)
                            elif "monthly" in wp_title2.lower():
                                oper_pmcs.pmcs_monthly(wpno)
                            elif "quarterly" in wp_title2.lower():
                                oper_pmcs.pmcs_quarterly(wpno)
                            elif "semi" in wp_title2.lower():
                                oper_pmcs.pmcs_semi_annually(wpno)
                            elif "annually" in wp_title2.lower():
                                oper_pmcs.pmcs_annually(wpno)
                        else:
                            break
    oper_pmcs.end()
    # OPERATOR MAINTENANCE PROCEDURES
    oper_maintenance = op.OperatorProcedures(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_maintenance.start()

    M = 0
    for row in islice(ws.rows, 1,None):
        wp_title = row[2].value
        M += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.oper_main):
                M += 1
                for row2 in islice(ws.rows, M, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    proc_type = row2[3].value
                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", " or")
                            if proc_type:
                                if proc_type.lower() == "inspect":
                                    oper_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    oper_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    oper_maintenance.service(wpno, wp_title2)
                                elif proc_type.lower() == "remove":
                                    oper_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    oper_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "replace":
                                    oper_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    oper_maintenance.repair(wpno, wp_title2)
                                elif proc_type.lower() == "pack":
                                    oper_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    oper_maintenance.unpack(wpno, wp_title2)
                                elif proc_type.lower() == "clean":
                                    oper_maintenance.clean(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    oper_maintenance.prepforuse(wpno, wp_title2)
                                elif proc_type.lower() == "prepstore":
                                    oper_maintenance.prepstore(wpno, wp_title2)
                                elif proc_type.lower() == "prepship":
                                    oper_maintenance.prepship(wpno, wp_title2)
                                elif proc_type.lower() == "transport":
                                    oper_maintenance.transport(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break
    oper_maintenance.end()
     # AUXILIARY EQUIPMENT - OPTIONAL
    if chb_1.get() == 1:
        aux_equip = ae.AuxiliaryEquipment(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        aux_equip.start()
        aux_equip.auxeqpwp()
        aux_equip.end()
    # AMMUNITION - OPTIONAL
    if chb_2.get() == 1:
        ammo = a.Ammunition(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        ammo.start()
        # ammo.ammoidentwp() # TODO - Add Ammunition Identification WP
        ammo.ammowp()
        ammo.natowp()
        ammo.end()
    # SHIPMENT & STORAGE - OPTIONAL
    if chb_3.get() == 1:
        ship_store = sms.ShipmentInstructions(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        ship_store.start()
        ship_store.prepstore()
        ship_store.prepship()
        ship_store.transport()
        ship_store.end()
    # AMMUNITION MARKING - OPTIONAL
    if chb_4.get() == 1:
        ammo = am.AmmunitionMarking(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        ammo.start()
        ammo.ammo_markingwp()
        ammo.end()
    # DESCTRUCTION - OPTIONAL
    if chb_5.get() == 1:
        destruct = d.Destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        destruct.start()
        destruct.destruct_introwp()
        for row in islice(ws.rows, 1 , None):
            wp_title = row[2].value
            wpno = row[1].value
            if wpno:
                if wpno[0] == 'D' and wpno[5] >= '2':
                    destruct.destruct_materialwp(wpno, wp_title)

        destruct.end()
    # SOFTWARE INFORMATION - OPTIONAL
    if chb_6.get() == 1:
        software = s.SoftwareInformation(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        software.start()
        software.softginfowp()
        software.softsumwp()
        software.softeffectwp()
        software.softdiffversionwp()
        software.softfeaturescapwp()
        software.softscreendisplaywp()
        software.softmenuwp()
        software.softtoolswp()
        software.softsecprivwp()
        software.softsuperctrlswp()
        software.softpowerupwp()
        software.softaccesswp()
        software.end()
    # SUPPORTING INFORMATION
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()

    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.support_info):
                S += 1
                for row2 in islice(ws.rows, S, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'S':
                            if wp_title2.lower() == "references":
                                support_info.refwp(wpno)
                            elif wp_title2.lower() == "coei & bii" or wp_title2.lower() == "coei and bii":
                                support_info.coeibiiwp(wpno)
                            elif wp_title2.lower().startswith("additional authorization list") or wp_title2.lower() == "aal":
                                support_info.aalwp(wpno)
                            elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                                support_info.explistwp(wpno)
                            elif wp_title2.lower().startswith("mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                                support_info.mrplwp(wpno)
                            elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith("csi"):
                                support_info.csi_wp(wpno)                          
                            elif wp_title2.lower().startswith("support items"):
                                support_info.supitemwp(wpno)
                            elif wp_title2.lower().startswith("additional supporting"):
                                support_info.genwp(wpno)

    support_info.end()
    rm.RearMatter(manual, SYS_ACRONYM, save_path).rear_matter()
    messagebox.showinfo("Success!", "Your technical manual has been created.")

def build_12p_tm_2d(save_path) -> None:
    """Calls methods to build each work package for a -12&P TM shell using MIL-STD-2D."""
    create_tm_wip_dir(save_path)
    ed.EntityDeclarations(SYS_ACRONYM, manual, milstd, save_path).entity_declarations()
    # FRONT MATTER
    front_matter = fm.FrontMatter(config, FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    front_matter.title_page()
    front_matter.warning_summary()
    front_matter.loep()
    front_matter.tb_toc_htu()
    # CHAPTER1
    chapter1 = ch1.Chapter1(config, manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    chapter1.start()
    chapter1.general_info()
    chapter1.equipment_description()
    chapter1.theory_operations()
    chapter1.end()

    # OPERATOR INSTRUCTIONS
    oper_instructions = oi.OperatorInstructions(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_instructions.start()
    oper_instructions.controls_indicators()

    O = 1
    for row in islice(ws.rows, 1, None):
        O += 1
        wp_title = row[2].value
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.operation):
                O += 1
                for row2 in islice(ws.rows,O,None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value

                    if wpno:

                        if wpno[0] == 'O':
                            if "unusual" in wp_title2.lower():
                                oper_instructions.unusual_conditions(wpno)
                            else:
                                wp_title2 = wp_title2.replace("/", " or")
                                oper_instructions.operating_procedures(wpno, wp_title2)
                            
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break
    oper_instructions.end()
    # TROUBLESHOOTING MASTER INDEX
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.master_index):
                mi = tsmi_o.TSMasterIndex(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
                mi.start()
                mi.tsindxwp()
                mi.end()
    # OPERATOR TROUBLESHOOTING
    oper_ts = to.TSOperator(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_ts.start()
    oper_ts.tsintrowp()

    T = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        T += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.troubleshooting):
                T += 1
                for row2 in islice(ws.rows, T, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", " or")
                            if "troubleshooting index" in wp_title2.lower():
                                continue
                            else:
                                oper_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break
    oper_ts.end()
    # OPERATOR PMCS
    oper_pmcs = po.PMCS(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_pmcs.start()
    oper_pmcs.pmcsintrowp()
    P = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        P += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.operation):
                P += 1
                for row2 in islice(ws.rows, P, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'M':
                            if "before" in wp_title2.lower():
                                oper_pmcs.pmcs_before(wpno)
                            elif "during" in wp_title2.lower():
                                oper_pmcs.pmcs_during(wpno)
                            elif "after" in wp_title2.lower():
                                oper_pmcs.pmcs_after(wpno)
                            elif "daily" in wp_title2.lower():
                                oper_pmcs.pmcs_daily(wpno)
                            elif "weekly" in wp_title2.lower():
                                oper_pmcs.pmcs_weekly(wpno)
                            elif "monthly" in wp_title2.lower():
                                oper_pmcs.pmcs_monthly(wpno)
                            elif "quarterly" in wp_title2.lower():
                                oper_pmcs.pmcs_quarterly(wpno)
                            elif "semi" in wp_title2.lower():
                                oper_pmcs.pmcs_semi_annually(wpno)
                            elif "annually" in wp_title2.lower():
                                oper_pmcs.pmcs_annually(wpno)
                        else:
                            break
    oper_pmcs.end()
    # OPERATOR MAINTENANCE PROCEDURES
    oper_maintenance = op.OperatorProcedures(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_maintenance.start()
    x = 0
    for row in islice(ws.rows,1,None):
        wp_title = row[2].value
        x += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.oper_main):
                x += 1

                for row2 in islice(ws.rows,x,None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    proc_type = row2[3].value

                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", "or")
                            if proc_type:
                                if proc_type.lower() == "replace":
                                    oper_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "inspect":
                                    oper_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    oper_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    oper_maintenance.service(wpno,wp_title2)
                                elif proc_type.lower() == "remove":
                                    oper_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    oper_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    oper_maintenance.repair(wpno,wp_title2)
                                elif proc_type.lower() == "pack":
                                    oper_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    oper_maintenance.unpack(wpno,wp_title2)
                                elif proc_type.lower() == "clean":
                                    oper_maintenance.clean(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    oper_maintenance.prepforuse(wpno, wp_title2)
                                elif proc_type.lower() == "prepstore":
                                    oper_maintenance.prepstore(wpno, wp_title2)
                                elif proc_type.lower() == "prepship":
                                    oper_maintenance.prepship(wpno, wp_title2)
                                elif proc_type.lower() == "transport":
                                    oper_maintenance.transport(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break
    oper_maintenance.end()
    # MAINTAINER TROUBLESHOOTING
    maint_ts = tm.TSMaintainer(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    maint_ts.start()
    maint_ts.tsintrowp()

    Mt = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Mt += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_troub):
                Mt += 1

                for row2 in islice(ws.rows, Mt, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", "or")
                            maint_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break

    maint_ts.end()
    # MAINTAINER PMCS
    main_pmcs = pm.PMCS(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    main_pmcs.start()
    main_pmcs.pmcsintrowp()
    P = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        P += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_pmcs):
                P += 1
                for row2 in islice(ws.rows, P, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'M':
                            if "before" in wp_title2.lower():
                                main_pmcs.pmcs_before(wpno)
                            elif "during" in wp_title2.lower():
                                main_pmcs.pmcs_during(wpno)
                            elif "after" in wp_title2.lower():
                                main_pmcs.pmcs_after(wpno)
                            elif "daily" in wp_title2.lower():
                                main_pmcs.pmcs_daily(wpno)
                            elif "weekly" in wp_title2.lower():
                                main_pmcs.pmcs_weekly(wpno)
                            elif "monthly" in wp_title2.lower():
                                main_pmcs.pmcs_monthly(wpno)
                            elif "quarterly" in wp_title2.lower():
                                main_pmcs.pmcs_quarterly(wpno)
                            elif "semi" in wp_title2.lower():
                                main_pmcs.pmcs_semi_annually(wpno)
                            elif "annually" in wp_title2.lower():
                                main_pmcs.pmcs_annually(wpno)
                        else:
                            break
    main_pmcs.end()
    # MAINTAINER MAINTENANCE
    maint_maintenance = mp.MaintainerProcedures(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    maint_maintenance.start()

    y = 0
    for row in islice(ws.rows,1,None):
        wp_title = row[2].value
        y += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.main_main):
                y += 1

                for row2 in islice(ws.rows,y,None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    proc_type = row2[3].value

                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", " or")
                            if "service upon receipt" in wp_title2.lower():
                                maint_maintenance.surwp(wpno)
                            elif proc_type:
                                if proc_type.lower() == "replace":
                                    maint_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "inspect":
                                    maint_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    maint_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    maint_maintenance.service(wpno, wp_title2)
                                elif proc_type.lower() == "remove":
                                    maint_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    maint_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    maint_maintenance.repair(wpno, wp_title2)
                                elif proc_type.lower() == "pack":
                                    maint_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    maint_maintenance.unpack(wpno, wp_title2)
                                elif proc_type.lower() == "clean":
                                    maint_maintenance.clean(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    maint_maintenance.prepforuse(wpno, wp_title2)
                                elif proc_type.lower() == "prepstore":
                                    maint_maintenance.prepstore(wpno, wp_title2)
                                elif proc_type.lower() == "prepship":
                                    maint_maintenance.prepship(wpno, wp_title2)
                                elif proc_type.lower() == "transport":
                                    maint_maintenance.transport(wpno, wp_title2)
                    if "chapter" in wp_title2.lower():
                        break
    maint_maintenance.end()
    # AUXILIARY EQUIPMENT - OPTIONAL
    if chb_1.get() == 1:
        aux_equip = ae.AuxiliaryEquipment(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        aux_equip.start()
        aux_equip.auxeqpwp()
        aux_equip.manu_items_introwp()
        aux_equip.manuwp()
        aux_equip.torquewp()
        aux_equip.wiringwp()
        aux_equip.end()
    # AMMUNITION - OPTIONAL
    if chb_2.get() == 1:
        ammunition = a.Ammunition(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        ammunition.start()
        ammunition.surwp()
        ammunition.ammowp()
        ammunition.ammo_markingwp()
        ammunition.natowp()
        ammunition.end()
    # DESTRUCTION - OPTIONAL
    if chb_5.get() == 1:
        destruct = d.Destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        destruct.start()
        destruct.destruct_introwp()
        for row in islice(ws.rows, 1 , None):
            wp_title = row[2].value
            wpno = row[1].value
            if wpno:
                if wpno[0] == 'D' and wpno[5] >= '2':
                    destruct.destruct_materialwp(wpno, wp_title)

        destruct.end()
    # SOFTWARE INFORMATION - OPTIONAL
    if chb_6.get() == 1:
        software = s.SoftwareInformation(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
        software.start()
        software.softginfowp()
        software.softsumwp()
        software.softeffectwp()
        software.softdiffversionwp()
        software.softfeaturescapwp()
        software.softscreendisplaywp()
        software.softmenuwp()
        software.softtoolswp()
        software.softsecprivwp()
        software.softsuperctrlswp()
        software.softpowerupwp()
        software.softaccesswp()
        software.end()
    # RPSTL
    repair_parts = rpstl.Rpstl(config, manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    repair_parts.start()
    repair_parts.introwp()
    Re = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Re += 1

        if wp_title:
            if any(s in wp_title.lower() for s in cfg.rpstl_check):
                Re += 1
                break
    for row2 in islice(ws.rows, Re, None):

        wpno2 = row2[1].value
        wp_title2 = row2[2].value
        wp_title2 = wp_title2.replace("/", " or")

        if wpno2:
            if wpno2[0] == "R":
                if "bulk items" in wp_title2.lower():
                    repair_parts.bulk_itemswp(wpno2)
                elif "nsn index" in wp_title2.lower() or "national stock" in wp_title2.lower():
                    repair_parts.nsnindxwp(wpno2)
                elif "pn index" in wp_title2.lower() or "part number" in wp_title2.lower():
                    repair_parts.pnindxwp(wpno2)
                else:
                    repair_parts.plwp(wpno2, wp_title2)
        if wp_title2:
            if "chapter" in wp_title2.lower():
                break

    repair_parts.end()
    # SUPPORTING INFORMATION
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()

    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.support_info):
                S += 1
                for row2 in islice(ws.rows, S, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'S':
                            if "intro" in wp_title2.lower() or "introduction" in wp_title2.lower():
                                support_info.macintrowp(wpno)
                            elif wp_title2.lower() == "mac" or wp_title2.lower() == "maintenance allocation chart" or wp_title2.lower() == "maintenance allocation chart (mac)":
                                support_info.macwp(wpno)
                            elif wp_title2.lower() == "references":
                                support_info.refwp(wpno)
                            elif wp_title2.lower() == "coei & bii" or wp_title2.lower() == "coei and bii":
                                support_info.coeibiiwp(wpno)
                            elif wp_title2.lower().startswith("additional authorization list") or wp_title2.lower() == "aal":
                                support_info.aalwp(wpno)
                            elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                                support_info.explistwp(wpno)
                            elif wp_title2.lower().startswith("tool") or wp_title2.lower().startswith("til"):
                                support_info.toolidwp(wpno)
                            elif wp_title2.lower().startswith("mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                                support_info.mrplwp(wpno)
                            elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith("csi"):
                                support_info.csi_wp(wpno)                          
                            elif wp_title2.lower().startswith("support items"):
                                support_info.supitemwp(wpno)
                            elif wp_title2.lower().startswith("additional supporting"):
                                support_info.genwp(wpno)
    support_info.end()
    rm.RearMatter(manual, SYS_ACRONYM, save_path).rear_matter()
    messagebox.showinfo("Success!", "Your technical manual has been created.")

def build_nmwr_2d(save_path) -> None:
    create_tm_wip_dir(save_path)
    ed.EntityDeclarations(SYS_ACRONYM, manual, milstd, save_path).entity_declarations()
    # FRONT MATTER
    front_matter = fm.FrontMatter(config, FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    front_matter.title_page()
    front_matter.warning_summary()
    front_matter.loep()
    front_matter.tb_toc_htu()
    # CHAPTER1
    chapter1 = ch1.Chapter1(config, manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    chapter1.start()
    chapter1.general_info()
    chapter1.equipment_description()
    chapter1.theory_operations()
    chapter1.end()
    # DEPOT TROUBLESHOOTING
    depot_ts = td.TSDepot(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    depot_ts.start()

    Mt = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Mt += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.depot_troub):
                Mt += 1

                for row2 in islice(ws.rows, Mt, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == "T":
                            wp_title2 = wp_title2.replace("/", "or")
                            if "troubleshooting intro" in wp_title2.lower() or "troubleshooting introduction" in wp_title2.lower():
                                depot_ts.tsintrowp(wpno)
                            elif "troubleshooting index" in wp_title2.lower():
                                depot_ts.tsindxwp(wpno)
                            elif "preshop" in wp_title2.lower():
                                depot_ts.pshopanalwp(wpno)
                            elif "component" in wp_title2.lower() or "checklist" in wp_title2.lower():
                                depot_ts.compchklistwp(wpno)
                            else:
                                depot_ts.tswp(wpno, wp_title2)
                    if wp_title2:
                        if "chapter" in wp_title2.lower():
                            break

    depot_ts.end()
    # DEPOT MAINTENANCE PROCEDURES
    depot_maintenance = dp.DepotProcedures(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    depot_maintenance.start()
    y = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        y += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.depot_main):
                y += 1
                for row2 in islice(ws.rows, y, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    proc_type = row2[3].value

                    if wpno:
                        if wpno[0] == 'M':
                            wp_title2 = wp_title2.replace("/", " or")
                            if proc_type:
                                if proc_type.lower() == "clean":
                                    depot_maintenance.clean(wpno, wp_title2)
                                if proc_type.lower() == "replace":
                                    depot_maintenance.replace(wpno, wp_title2)
                                elif proc_type.lower() == "inspect":
                                    depot_maintenance.inspect(wpno, wp_title2)
                                elif proc_type.lower() == "test":
                                    depot_maintenance.test(wpno, wp_title2)
                                elif proc_type.lower() == "service":
                                    depot_maintenance.service(wpno, wp_title2)
                                elif proc_type.lower() == "remove":
                                    depot_maintenance.remove(wpno, wp_title2)
                                elif proc_type.lower() == "install":
                                    depot_maintenance.install(wpno, wp_title2)
                                elif proc_type.lower() == "repair":
                                    depot_maintenance.repair(wpno, wp_title2)
                                elif proc_type.lower() == "pack":
                                    depot_maintenance.pack(wpno, wp_title2)
                                elif proc_type.lower() == "unpack":
                                    depot_maintenance.unpack(wpno, wp_title2)
                                elif proc_type.lower() == "prepforuse":
                                    depot_maintenance.prepforuse(wpno, wp_title2)
                            elif "preservation" in wp_title2.lower():
                                depot_maintenance.ppmgeninfowp(wpno)
                            elif "quality" in wp_title2.lower():
                                depot_maintenance.qawp(wpno)
                            else:
                                break
                    if "chapter" in wp_title2.lower():
                        break
    # Other WP's to add later...
    # depot_maintenance.facilwp()   # Optional
    # depot_maintenance.oipwp() # Optional
    # depot_maintenance.mobilwp()   # Optional
    # depot_maintenance.manu_items_introwp() # Optional
    # depot_maintenance.manuwp()    # Optional
    # depot_maintenance.torquewp()  # Optional
    # depot_maintenance.inventorywp()   # Optional
    # depot_maintenance.storagewp() # Optional
    # depot_maintenance.wiringwp()  # Optional
    depot_maintenance.end()
    # RPSTL
    repair_parts = rpstl.Rpstl(config, manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    repair_parts.start()
    repair_parts.introwp()
    Re = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Re += 1

        if wp_title:
            if any(s in wp_title.lower() for s in cfg.rpstl_check):
                Re += 1
                break
    for row2 in islice(ws.rows, Re, None):

        wpno2 = row2[1].value
        wp_title2 = row2[2].value
        wp_title2 = wp_title2.replace("/", " or")

        if wpno2:
            if wpno2[0] == "R":
                if "bulk items" in wp_title2.lower():
                    repair_parts.bulk_itemswp(wpno2)
                elif "nsn index" in wp_title2.lower() or "national stock" in wp_title2.lower():
                    repair_parts.nsnindxwp(wpno2)
                elif "pn index" in wp_title2.lower() or "part number" in wp_title2.lower():
                    repair_parts.pnindxwp(wpno2)
                else:
                    repair_parts.plwp(wpno2, wp_title2)
        if wp_title2:
            if "chapter" in wp_title2.lower():
                break

    repair_parts.end()
    # SUPPORTING INFORMATION
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()

    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.support_info):
                S += 1
                for row2 in islice(ws.rows, S, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == 'S':
                            if wp_title2.lower() == "references":
                                support_info.refwp(wpno)
                            elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                                support_info.explistwp(wpno)
                            elif wp_title2.lower().startswith("tool") or wp_title2.lower().startswith("til"):
                                support_info.toolidwp(wpno)
                            elif wp_title2.lower().startswith("mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                                support_info.mrplwp(wpno)
                            elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith("csi"):
                                support_info.csi_wp(wpno)
                            elif wp_title2.lower().startswith("additional supporting"):
                                support_info.genwp(wpno)
    support_info.end()
    rm.RearMatter(manual, SYS_ACRONYM, save_path).rear_matter()
    messagebox.showinfo("Success!", "Your NMWR has been created.")

def create_tm_wip_dir(save_path) -> None:
    """Creates the WIP directory for generated TM files.
    Deletes the current one if it exists."""
    man = CBX_MANUAL.get()
    # Directory
    directory = SYS_ACRONYM + " " + man + " WIP"
    # Parent Directory path
    parent_dir = save_path + "/"
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
    if not errors:
        save_path = filedialog.askdirectory(initialdir="/", title="Save file")
        print(save_path)
        if save_path == "":
            messagebox.showerror("Error", " Please select a save location.")
        else:
            form_validation(save_path)
    else:
        messagebox.showerror("Error", "Please fill out all fields.")
        print(errors)

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
    excelFile = filedialog.askopenfilename(initialdir="~",title="Select TM Tracker",filetypes=(("Excel File", "*xlsx"),("All Files",".")))
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
root.resizable(False, False)
root.iconbitmap('images/logo_TRG.ico')

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
