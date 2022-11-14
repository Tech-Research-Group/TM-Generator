from dotenv import dotenv_values
from itertools import islice
import chapters.chapter1 as ch1
import chapters.destruction as d
import chapters.entity_declarations as ed
import chapters.front_matter as fm
import chapters.operator_instructions as oi
import chapters.parts_information as pi
import chapters.pmcs_m as pm
import chapters.pmcs_o as po
import chapters.procedures_d as dp
import chapters.procedures_m as mp
import chapters.procedures_o as op
import chapters.rear_matter as rm
import chapters.supporting_information as si
import chapters.ts_depot as td
import chapters.ts_maintainer as tm
import chapters.ts_operator as to
import chapters.ts_master_index_o as tsmi
import cfg
from chapters import rpstl

# from main import SYS_ACRONYM, manual, milstd, save_path
config = dotenv_values(".env")  # take environment variables from .env.


def get_entity_declarations(SYS_ACRONYM, manual, milstd, save_path):
    """Calls EntityDeclarations and all of it's methods to create an Entity Declarations section in XML."""
    ed.EntityDeclarations(SYS_ACRONYM, manual, milstd, save_path).entity_declarations()


def get_front_matter(FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path):
    """Calls FrontMatter and all of it's methods to create a Front Matter section in XML."""
    front_matter = fm.FrontMatter(config, FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    front_matter.title_page()
    front_matter.warning_summary()
    front_matter.loep()
    front_matter.tb_toc_htu()


def get_chapter1(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path):
    """Calls Chapter1 and all of it's methods to create a Chapter 1 section in XML."""
    chapter1 = ch1.Chapter1(config, manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    chapter1.start()
    chapter1.general_info()
    chapter1.equipment_description()
    chapter1.theory_operations()
    chapter1.end()


def get_operator_instructions(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls OperatorInstructions and all of it's methods to create a Operator Instructions section in XML."""
    oper_instructions = oi.OperatorInstructions(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_instructions.start()
    oper_instructions.controls_indicators()
    _o = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        _o += 1
        if wp_title:
            if any(s in wp_title.lower() for s in cfg.operation):
                _o += 1
                for row2 in islice(ws.rows, _o, None):
                    wp_title2 = row2[2].value
                    wpno = row2[1].value
                    if wpno:
                        if wpno[0] == 'O':
                            wp_title2 = wp_title2.replace("/", " or")
                            oper_instructions.operating_procedures(wpno, wp_title2)
                            if "unusual" in wp_title2:
                                oper_instructions.unusual_conditions(wpno)
                        if wp_title2 and "chapter" in wp_title2:
                            break
    oper_instructions.end()


def get_ts_master_index(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls TSMasterIndex and all of it's methods to create a Troubleshooting Master Index section in XML."""
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        if wp_title and any(s in wp_title.lower() for s in cfg.master_index):
            mi = tsmi.TSMasterIndex(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
            mi.start()
            mi.tsindxwp()
            mi.end()


def get_operator_ts(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls TSOperator and all of its medthods to create an Operator Troubleshooting Chapter in XML."""
    oper_ts = to.TSOperator(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_ts.start()
    T = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        T += 1
        if wp_title and any(s in wp_title.lower() for s in cfg.troubleshooting):
            T += 1
            for row2 in islice(ws.rows, T, None):
                wp_title2 = row2[2].value
                wpno = row2[1].value
                if wpno and wpno[0] == "T":
                    wp_title2 = wp_title2.replace("/", " or")
                    if "troubleshooting introduction" in wp_title2.lower():
                        oper_ts.tsintrowp(wpno)
                    elif "troubleshooting index" in wp_title2.lower():
                        oper_ts.tsindxwp(wpno)
                    else:
                        oper_ts.tswp(wpno, wp_title2)
                if wp_title2 and "chapter" in wp_title2.lower():
                    break
    oper_ts.end()


def get_maintainer_ts(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws) -> None:
    """Calls TSMaintainer and all of its medthods to create an Maintainer Troubleshooting Chapter in XML."""
    maint_ts = tm.TSMaintainer(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    maint_ts.start()
    T = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        T += 1
        if wp_title and any(s in wp_title.lower() for s in cfg.main_troub):
            T += 1
            for row2 in islice(ws.rows, T, None):
                wp_title2 = row2[2].value
                wpno = row2[1].value
                if wpno and wpno[0] == "T":
                    wp_title2 = wp_title2.replace("/", "or")
                    if "introduction" in wp_title2.lower() or "intro" in wp_title2.lower():
                        maint_ts.tsintrowp(wpno)
                    elif "index" in wp_title2.lower():
                        maint_ts.tsindxwp(wpno)
                    else:
                        maint_ts.tswp(wpno, wp_title2)
                if wp_title2 and "chapter" in wp_title2.lower():
                    break
    maint_ts.end()


def get_depot_ts(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls TSDepot and all of its medthods to create a Depot Troubleshooting Chapter in XML."""
    depot_ts = td.TSDepot(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    depot_ts.start()
    Mt = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Mt += 1
        if wp_title and any(s in wp_title.lower() for s in cfg.depot_troub):
            Mt += 1
            for row2 in islice(ws.rows, Mt, None):
                wp_title2 = row2[2].value
                wpno = row2[1].value
                if wpno and wpno[0] == "T":
                    wp_title2 = wp_title2.replace("/", "or")
                    if "troubleshooting intro" in wp_title2.lower() or \
                            "troubleshooting introduction" in wp_title2.lower():
                        depot_ts.tsintrowp(wpno)
                    elif "troubleshooting index" in wp_title2.lower():
                        depot_ts.tsindxwp(wpno)
                    elif "preshop" in wp_title2.lower():
                        depot_ts.pshopanalwp(wpno)
                    elif "component" in wp_title2.lower() or "checklist" in wp_title2.lower():
                        depot_ts.compchklistwp(wpno)
                    else:
                        depot_ts.tswp(wpno, wp_title2)
                if wp_title2 and "chapter" in wp_title2.lower():
                    break
    depot_ts.end()


def get_operator_pmcs(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls PMCS and all of its medthods to create an Operator PMCS chapter in XML."""
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


def get_maintainer_pmcs(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls PMCS and all of its medthods to create a Maintainer PMCS chapter in XML."""
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


def get_operator_maintenance(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls OperatorProcedures and all of its medthods to create an Operator Procedures chapter in XML."""
    oper_maintenance = op.OperatorProcedures(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    oper_maintenance.start()
    M = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        M += 1
        if wp_title and any(s in wp_title.lower() for s in cfg.oper_main):
            M += 1
            for row2 in islice(ws.rows, M, None):
                wpno = row2[1].value
                wp_title2 = row2[2].value
                proc_type = row2[3].value
                if wpno and wpno[0] == 'M':
                    wp_title2 = wp_title2.replace("/", " or")
                    if proc_type:
                        oper_maintenance.maintwp(wpno, wp_title2, proc_type)
                if wp_title2 and "chapter" in wp_title2.lower():
                    break
    oper_maintenance.end()


def get_maintainer_maintenance(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls MaintainerProcedures and all of its medthods to create a Maintainer Procedures chapter in XML."""
    maint_maintenance = mp.MaintainerProcedures(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    maint_maintenance.start()
    y = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        y += 1
        if wp_title and any(s in wp_title.lower() for s in cfg.main_main):
            y += 1
            for row2 in islice(ws.rows, y, None):
                wpno = row2[1].value
                wp_title2 = row2[2].value
                proc_type = row2[3].value
                if wpno and wpno[0] == 'M':
                    wp_title2 = wp_title2.replace("/", " or")
                    if "service upon receipt" in wp_title2.lower():
                        maint_maintenance.surwp(wpno)
                    elif proc_type:
                        maint_maintenance.maintwp(wpno, wp_title2, proc_type)
                if "chapter" in wp_title2.lower():
                    break
    maint_maintenance.end()

def get_depot_maintenance(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls DepotProcedures and all of its medthods to create a Depot Procedures chapter in XML."""
    depot_maintenance = dp.DepotProcedures(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    depot_maintenance.start()
    y = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        y += 1
        if wp_title and any(s in wp_title.lower() for s in cfg.depot_main):
            y += 1
            for row2 in islice(ws.rows, y, None):
                wpno = row2[1].value
                wp_title2 = row2[2].value
                proc_type = row2[3].value
                if wpno and wpno[0] == 'M':
                    wp_title2 = wp_title2.replace("/", " or")
                    if proc_type:
                        depot_maintenance.maintwp(wpno, wp_title2, proc_type)
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

def get_parts_information(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls PartsInformation and all of it's methods to create a Parts Info chapter in XML."""
    parts_info = pi.PartsInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    parts_info.start()
    parts_info.introwp()
    Re = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Re += 1
        if wp_title and any(s in wp_title.lower() for s in cfg.rpstl_check):
            Re += 1
            break
    for row2 in islice(ws.rows, Re, None):
        wpno2 = row2[1].value
        wp_title2 = row2[2].value
        wp_title2 = wp_title2.replace("/", " or")
        if wpno2 and wpno2[0] == "R":
            if "bulk items" in wp_title2.lower():
                parts_info.bulk_itemswp(wpno2)
            elif "nsn index" in wp_title2.lower() or "national stock" in wp_title2.lower():
                parts_info.nsnindxwp(wpno2)
            elif "pn index" in wp_title2.lower() or "part number" in wp_title2.lower():
                parts_info.pnindxwp(wpno2)
            else:
                parts_info.plwp(wpno2, wp_title2)
        if wp_title2 and "chapter" in wp_title2.lower():
            break
    parts_info.end()


def get_rpstl(config, manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls Rpstl and all of it's methods to create a RPSTL Chapter in XML."""
    repair_parts = rpstl.Rpstl(config, manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    repair_parts.start()

    R = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        R += 1
        if wp_title and any(s in wp_title.lower() for s in cfg.rpstl_check):
            R += 1
            break
    for row2 in islice(ws.rows, R, None):
        wpno2 = row2[1].value
        wp_title2 = row2[2].value
        wp_title2 = wp_title2.replace("/", " or")
        if wpno2 and wpno2[0] == "R":
            if "introduction" in wp_title2.lower() or "intro" in wp_title2.lower():
                repair_parts.introwp(wpno2)
            elif "bulk items" in wp_title2.lower():
                repair_parts.bulk_itemswp(wpno2)
            elif "nsn index" in wp_title2.lower() or "national stock" in wp_title2.lower():
                repair_parts.nsnindxwp(wpno2)
            elif "pn index" in wp_title2.lower() or "part number" in wp_title2.lower():
                repair_parts.pnindxwp(wpno2)
            else:
                repair_parts.plwp(wpno2, wp_title2)
        if wp_title2 and "chapter" in wp_title2.lower():
            break
    repair_parts.end()

def get_supporting_information(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls SupportingInformation and all of it's methods to create a Supporting Info Chapter in XML."""
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()
    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title and any(s in wp_title.lower() for s in cfg.support_info):
            S += 1
            for row2 in islice(ws.rows, S, None):
                wpno = row2[1].value
                wp_title2 = row2[2].value
                if wpno and wpno[0] == 'S':
                    if wp_title2.lower() == "references":
                        support_info.refwp(wpno)
                    elif wp_title2.lower() in ["coei & bii", "coei and bii"]:
                        support_info.coeibiiwp(wpno)
                    elif wp_title2.lower().startswith(
                            "additional authorization list") or wp_title2.lower() == "aal":
                        support_info.aalwp(wpno)
                    elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                        support_info.explistwp(wpno)
                    elif wp_title2.lower().startswith(
                            "mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                        support_info.mrplwp(wpno)
                    elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith(
                            "csi"):
                        support_info.csi_wp(wpno)
                    elif wp_title2.lower().startswith("support items"):
                        support_info.supitemwp(wpno)
                    elif wp_title2.lower().startswith("additional supporting"):
                        support_info.genwp(wpno)
    support_info.end()

def get_supporting_information_mac(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls SupportingInformation and all of it's methods to create a Supporting Info Chapter in XML."""
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()
    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title and any(s in wp_title.lower() for s in cfg.support_info):
            S += 1
            for row2 in islice(ws.rows, S, None):
                wpno = row2[1].value
                wp_title2 = row2[2].value
                if wpno and wpno[0] == 'S':
                    if wp_title2.lower() == "references":
                        support_info.refwp(wpno)
                    elif "intro" in wp_title2.lower() or "introduction" in wp_title2.lower():
                        support_info.macintrowp(wpno)
                    elif "mac" in wp_title2.lower() or "maintenance allocation chart" in wp_title2.lower():
                        support_info.macwp(wpno)
                    elif "coei" in wp_title2.lower() or "components of end item" in wp_title2.lower():
                        support_info.coeibiiwp(wpno)
                    elif wp_title2.lower().startswith(
                            "additional authorization list") or wp_title2.lower() == "aal":
                        support_info.aalwp(wpno)
                    elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                        support_info.explistwp(wpno)
                    elif wp_title2.lower().startswith("tool") or wp_title2.lower().startswith("til"):
                        support_info.toolidwp(wpno)
                    elif wp_title2.lower().startswith(
                            "mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                        support_info.mrplwp(wpno)
                    elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith(
                            "csi"):
                        support_info.csi_wp(wpno)
                    elif wp_title2.lower().startswith("support items"):
                        support_info.supitemwp(wpno)
                    elif wp_title2.lower().startswith("additional supporting"):
                        support_info.genwp(wpno)
    support_info.end()

def get_supporting_information_nmwr(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls SupportingInformation and all of it's methods to create a Supporting Info Chapter in XML."""
    support_info = si.SupportingInformation(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    support_info.start()
    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title and any(s in wp_title.lower() for s in cfg.support_info):
            S += 1
            for row2 in islice(ws.rows, S, None):
                wpno = row2[1].value
                wp_title2 = row2[2].value
                if wpno and wpno[0] == 'S':
                    if wp_title2.lower() == "references":
                        support_info.refwp(wpno)
                    elif wp_title2.lower().startswith("expendable") or wp_title2.lower().startswith("edil"):
                        support_info.explistwp(wpno)
                    elif wp_title2.lower().startswith("tool") or wp_title2.lower().startswith("til"):
                        support_info.toolidwp(wpno)
                    elif wp_title2.lower().startswith(
                            "mandatory replacement parts") or wp_title2.lower().startswith("mrp"):
                        support_info.mrplwp(wpno)
                    elif wp_title2.lower().startswith("critical safety items") or wp_title2.lower().startswith(
                            "csi"):
                        support_info.csi_wp(wpno)
                    elif wp_title2.lower().startswith("additional supporting"):
                        support_info.genwp(wpno)
    support_info.end()


def get_destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws):
    """Calls Destruction and all of it's methods to create a Destruction Chapter in XML."""
    destruct = d.Destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    destruct.start()
    destruct.destruct_introwp()
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        wpno = row[1].value
        if wpno and wpno[0] == 'D' and wpno[5] >= '2':
            destruct.destruct_materialwp(wpno, wp_title)
    destruct.end()


def get_rear_matter(manual, SYS_ACRONYM, save_path):
    """Calls RearMatter and all of it's methods to create a Rear Matter Chapter in XML."""
    rm.RearMatter(manual, SYS_ACRONYM, save_path).rear_matter()
