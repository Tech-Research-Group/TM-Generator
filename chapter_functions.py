from itertools import islice

import chapters.auxiliary_equipment as ae
import chapters.chapter1 as ch1
import chapters.destruction as d
import chapters.entity_declarations as ed
import chapters.front_matter as fm
import chapters.operator_instructions as oi

# import chapters.parts_information as pi
import chapters.pmcs_m as pm
import chapters.pmcs_o as po
import chapters.procedures_d as dp
import chapters.procedures_m as mp
import chapters.procedures_o as op
import chapters.rear_matter as rm
import chapters.supporting_information as si
import chapters.ts_depot as td
import chapters.ts_maintainer as tm
import chapters.ts_master_index_o as tsmi
import chapters.ts_operator as to
from chapters import rpstl

# from main import SYS_ACRONYM, manual, milstd, save_path


def get_entity_declarations(SYS_ACRONYM, manual, milstd, save_path) -> None:
    """Calls EntityDeclarations and all of it's methods to create an Entity Declarations section in XML."""
    ed.EntityDeclarations(SYS_ACRONYM, manual, milstd, save_path).entity_declarations()


def get_front_matter(
    CAGENO,
    FSC,
    manual,
    milstd,
    MODELNO,
    NIIN,
    PARTNO,
    save_path,
    SYS_ACRONYM,
    SYS_NAME,
    TMNO,
    UOC,
) -> None:
    """Calls FrontMatter and all of it's methods to create a Front Matter section in XML."""
    front_matter = fm.FrontMatter(
        CAGENO,
        FSC,
        manual,
        milstd,
        MODELNO,
        NIIN,
        PARTNO,
        save_path,
        SYS_ACRONYM,
        SYS_NAME,
        TMNO,
        UOC,
    )
    front_matter.production_start()
    front_matter.frntcover()
    front_matter.warning_summary()
    front_matter.loepwp()
    front_matter.titleblk()
    front_matter.contents()
    front_matter.howtouse()


def get_chapter1(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path) -> None:
    """Calls Chapter1 and all of it's methods to create a Chapter 1 section in XML."""
    chapter1 = ch1.Chapter1(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path)
    chapter1.start()
    chapter1.general_info()
    chapter1.equipment_description()
    chapter1.theory_operations()
    chapter1.end()


def get_operator_instructions(
    manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws
) -> None:
    """Calls OperatorInstructions and all of it's methods to create a Operator Instructions section in XML."""
    oper_instructions = oi.OperatorInstructions(
        manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path
    )
    oper_instructions.start()
    _o = 1
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        _o += 1
        if wp_title.lower() == "operator instructions":
            for row2 in islice(ws.rows, _o, None):
                wp_title2 = row2[2].value
                wpno = row2[1].value
                if wpno:
                    if wpno[0] == "O":
                        wp_title2 = wp_title2.replace("/", " or")
                        if "controls and indicators" in wp_title2.lower():
                            oper_instructions.ctrlindwp(wpno)
                        elif "unusual" in wp_title2.lower():
                            oper_instructions.opunuwp(wpno)
                        elif "emergency" in wp_title2.lower():
                            oper_instructions.emergencywp(wpno)
                        elif (
                            "data plate" in wp_title2.lower()
                            or "stowage" in wp_title2.lower()
                        ):
                            oper_instructions.stowagewp(wpno)
                        else:
                            oper_instructions.opusualwp(wpno, wp_title2)
    oper_instructions.end()


def get_ts_master_index(
    manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws
) -> None:
    """Calls TSMasterIndex and all of it's methods to create a Troubleshooting Master Index section in XML."""
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        wpno = row[1].value
        if wp_title.lower() == "troubleshooting master index":
            mi = tsmi.TSMasterIndex(
                manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path
            )
            mi.start()
            mi.tsindxwp(wpno)
            mi.end()


def get_operator_ts(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws) -> None:
    """Calls TSOperator and all of its medthods to create an Operator Troubleshooting Chapter in XML."""
    oper_ts = to.TSOperator(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path)
    oper_ts.start()
    T = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        T += 1
        if wp_title.lower() == "operator troubleshooting":
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
                else:
                    break
    oper_ts.end()


def get_maintainer_ts(
    manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws
) -> None:
    """Calls TSMaintainer and all of its medthods to create an Maintainer Troubleshooting Chapter in XML."""
    maint_ts = tm.TSMaintainer(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path)
    maint_ts.start()
    T = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        T += 1
        if wp_title.lower() == "maintainer troubleshooting":
            T += 1
            for row2 in islice(ws.rows, T, None):
                wp_title2 = row2[2].value
                wpno = row2[1].value
                if wpno and wpno[0] == "T":
                    wp_title2 = wp_title2.replace("/", "or")
                    if (
                        "introduction" in wp_title2.lower()
                        or "intro" in wp_title2.lower()
                    ):
                        maint_ts.tsintrowp(wpno)
                    elif "index" in wp_title2.lower():
                        maint_ts.tsindxwp(wpno)
                    else:
                        maint_ts.tswp(wpno, wp_title2)
                else:
                    break
    maint_ts.end()


def get_depot_ts(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws) -> None:
    """Calls TSDepot and all of its medthods to create a Depot Troubleshooting Chapter in XML."""
    depot_ts = td.TSDepot(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path)
    depot_ts.start()
    Mt = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        Mt += 1
        if wp_title.lower() == "depot troubleshooting":
            Mt += 1
            for row2 in islice(ws.rows, Mt, None):
                wp_title2 = row2[2].value
                wpno = row2[1].value
                if wpno and wpno[0] == "T":
                    wp_title2 = wp_title2.replace("/", "or")
                    if (
                        "troubleshooting intro" in wp_title2.lower()
                        or "troubleshooting introduction" in wp_title2.lower()
                    ):
                        depot_ts.tsintrowp(wpno)
                    elif "troubleshooting index" in wp_title2.lower():
                        depot_ts.tsindxwp(wpno)
                    elif "preshop" in wp_title2.lower():
                        depot_ts.pshopanalwp(wpno)
                    elif (
                        "component" in wp_title2.lower()
                        or "checklist" in wp_title2.lower()
                    ):
                        depot_ts.compchklistwp(wpno)
                    else:
                        depot_ts.tswp(wpno, wp_title2)
                else:
                    break
    depot_ts.end()


def get_operator_pmcs(
    manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws
) -> None:
    """Calls PMCS and all of its medthods to create an Operator PMCS chapter in XML."""
    oper_pmcs = po.PMCS(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path)
    oper_pmcs.start()

    P = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        P += 1
        if wp_title:
            if wp_title.lower() == "operator pmcs":
                P += 1
                for row2 in islice(ws.rows, P, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == "C":
                            if "intro" in wp_title2.lower():
                                oper_pmcs.pmcsintrowp(wpno)
                            elif "before" in wp_title2.lower():
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


def get_maintainer_pmcs(
    manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws
) -> None:
    """Calls PMCS and all of its medthods to create a Maintainer PMCS chapter in XML."""
    main_pmcs = pm.PMCS(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path)
    main_pmcs.start()

    P = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        P += 1
        if wp_title:
            if wp_title.lower() == "maintainer pmcs":
                P += 1
                for row2 in islice(ws.rows, P, None):
                    wpno = row2[1].value
                    wp_title2 = row2[2].value
                    if wpno:
                        if wpno[0] == "C":
                            if "intro" in wp_title2.lower():
                                main_pmcs.pmcsintrowp(wpno)
                            elif "before" in wp_title2.lower():
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


def get_operator_maintenance(
    manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws
) -> None:
    """Calls OperatorProcedures and all of its medthods to create an Operator Procedures chapter in XML."""
    oper_maintenance = op.OperatorProcedures(
        manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path
    )
    oper_maintenance.start()
    M = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        M += 1
        if wp_title.lower() == "operator maintenance":
            M += 1
            for row2 in islice(ws.rows, M, None):
                wpno = row2[1].value
                wp_title2 = row2[2].value
                proc_type = row2[3].value
                if wpno and wpno[0] == "M":
                    wp_title2 = wp_title2.replace("/", " or")
                    if proc_type:
                        oper_maintenance.maintwp(wpno, wp_title2, proc_type)
                else:
                    break
    oper_maintenance.end()


def get_maintainer_maintenance(
    manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws
) -> None:
    """Calls MaintainerProcedures and all of its medthods to create a Maintainer Procedures chapter in XML."""
    maint_maintenance = mp.MaintainerProcedures(
        manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path
    )
    maint_maintenance.start()
    y = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        y += 1
        if wp_title.lower() == "maintainer maintenance":
            y += 1
            for row2 in islice(ws.rows, y, None):
                wpno = row2[1].value
                wp_title2 = row2[2].value
                proc_type = row2[3].value
                if wpno and wpno[0] == "M" and wpno[3] != 9:
                    wp_title2 = wp_title2.replace("/", " or")
                    if "service upon receipt" in wp_title2.lower():
                        maint_maintenance.surwp(wpno)
                    elif proc_type:
                        maint_maintenance.maintwp(wpno, wp_title2, proc_type)
                else:
                    break
    maint_maintenance.end()


def get_depot_maintenance(
    manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws
) -> None:
    """Calls DepotProcedures and all of its medthods to create a Depot Procedures chapter in XML."""
    depot_maintenance = dp.DepotProcedures(
        manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path
    )
    depot_maintenance.start()
    y = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        y += 1
        if wp_title.lower == "depot maintenance":
            y += 1
            for row2 in islice(ws.rows, y, None):
                wpno = row2[1].value
                wp_title2 = row2[2].value
                proc_type = row2[3].value
                if wpno and wpno[0] == "M":
                    wp_title2 = wp_title2.replace("/", " or")
                    if proc_type:
                        depot_maintenance.maintwp(wpno, wp_title2, proc_type)
                    elif "preservation" in wp_title2.lower():
                        depot_maintenance.ppmgeninfowp(wpno)
                    elif "quality" in wp_title2.lower():
                        depot_maintenance.qawp(wpno)
                    else:
                        break
                else:
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


# def get_auxiliary(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws) -> None:
#     """Build the Auxiliary Equipment chapter from the worksheet."""
#     aux = ae.AuxiliaryEquipment(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path)
#     aux.start()

#     # Expecting columns: [?, WP No, Title, Proc Type, ...]
#     # Adjust indexes if your sheet differs.
#     rows = list(ws.iter_rows(min_row=2, values_only=True))

#     in_aux_section = False

#     for row in rows:
#         # Unpack defensively: handle sheets with extra cols
#         # col0 is ignored; adjust if your sheet’s layout differs
#         _, wpno, title, proc_type, *rest = (list(row) + [None, None, None, None])[:4]

#         title_l = (title or "").strip().lower()

#         # Not in Auxiliary section yet — look for the section header line
#         if not in_aux_section:
#             print(title_l)
#             # if title_l and any(s in title_l for s in cfg.auxiliary):
#             if title_l == "auxiliary equipment maintenance":
#                 in_aux_section = True
#             continue  # keep scanning until header is found

#         # We are in Auxiliary section: process WP rows.
#         wpno_s = (wpno or "").strip()
#         if not wpno_s:
#             # Blank / spacer row: ignore
#             continue

#         # If WP number no longer starts with M, we’ve hit the next chapter.
#         if not wpno_s.startswith("M"):
#             break

#         # Use the per-row title for routing, with safe replace
#         t = title or ""
#         t_for_print = t.replace("/", " or")
#         tl = t.lower()

#         # Route to the correct writer
#         if "manufactured items intro" in tl:
#             aux.manu_items_introwp(wpno_s, t_for_print)
#         elif "manufacturing procedure" in tl:
#             aux.manuwp(wpno_s, t_for_print)
#         elif "torque limits" in tl:
#             aux.torquewp(wpno_s, t_for_print)
#         elif "wiring diagram" in tl:
#             aux.wiringwp(wpno_s, t_for_print)
#         else:
#             # Only call generic WP if we have a proc_type
#             if proc_type:
#                 aux.auxeqpwp(wpno_s, t_for_print, proc_type)

#     aux.end()


def get_auxiliary(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws) -> None:
    """Build the Auxiliary Equipment chapter from the worksheet."""
    aux = ae.AuxiliaryEquipment(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path)
    aux.start()
    y = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        print(wp_title)
        y += 1
        if "auxiliary equipment maintenance" in wp_title.lower():
            y += 1
            for row2 in islice(ws.rows, y, None):
                wpno = row2[1].value
                wp_title2 = row2[2].value
                proc_type = row2[3].value
                if wpno and wpno[0] == "M":
                    wp_title2 = wp_title2.replace("/", " or")
                    # Route to the correct writer
                    if "manufactured items intro" in wp_title2:
                        aux.manu_items_introwp(wpno, wp_title2)
                    elif "manufacturing procedure" in wp_title2:
                        aux.manuwp(wpno, wp_title2)
                    elif "torque limits" in wp_title2:
                        aux.torquewp(wpno, wp_title2)
                    elif "wiring diagram" in wp_title2:
                        aux.wiringwp(wpno, wp_title2)
                    else:
                        # Only call generic WP if we have a proc_type
                        if proc_type:
                            aux.auxeqpwp(wpno, wp_title2, proc_type)
                else:
                    break
    aux.end()


def get_destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws) -> None:
    """Calls Destruction and all of it's methods to create a Destruction Chapter in XML."""
    destruct = d.Destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path)
    destruct.start()
    destruct.destruct_introwp()
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        wpno = row[1].value
        if wpno and wpno[0] == "D" and wpno[5] >= "2":
            destruct.destruct_materialwp(wpno, wp_title)
    destruct.end()


def get_rpstl(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws) -> None:
    """Calls Rpstl and all of it's methods to create a RPSTL Chapter in XML."""
    repair_parts = rpstl.Rpstl(manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path)
    repair_parts.start()

    R = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        R += 1
        if wp_title.lower() == "repair parts and special tools list":
            R += 1
            break
    for row2 in islice(ws.rows, R, None):
        wpno2 = row2[1].value
        wp_title2 = row2[2].value
        wp_title2 = wp_title2.replace("/", " or")
        if wpno2 and wpno2[0] == "R":
            if "intro" in wp_title2.lower():
                repair_parts.introwp()
            elif "bulk items" in wp_title2.lower():
                repair_parts.bulk_itemswp(wpno2, wp_title2)
            elif (
                "nsn index" in wp_title2.lower()
                or "national stock" in wp_title2.lower()
            ):
                repair_parts.nsnindxwp(wpno2, wp_title2)
            elif "pn index" in wp_title2.lower() or "part number" in wp_title2.lower():
                repair_parts.pnindxwp(wpno2, wp_title2)
            else:
                repair_parts.plwp(wpno2, wp_title2)
        else:
            break
    repair_parts.end()


def get_supporting_information(
    manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws
) -> None:
    """Calls SupportingInformation and all of it's methods to create a Supporting Info Chapter in XML."""
    support_info = si.SupportingInformation(
        manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path
    )
    support_info.start()
    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title.lower() == "supporting information":
            S += 1
            for row2 in islice(ws.rows, S, None):
                wpno = row2[1].value
                wp_title2 = row2[2].value
                if wpno and wpno[0] == "S":
                    if wp_title2.lower() == "references":
                        support_info.refwp(wpno)
                    elif wp_title2.lower() in ["coei & bii", "coei and bii"]:
                        support_info.coeibiiwp(wpno)
                    elif (
                        wp_title2.lower().startswith("additional authorization list")
                        or wp_title2.lower() == "aal"
                    ):
                        support_info.aalwp(wpno)
                    elif wp_title2.lower().startswith(
                        "expendable"
                    ) or wp_title2.lower().startswith("edil"):
                        support_info.explistwp(wpno)
                    elif wp_title2.lower().startswith(
                        "mandatory replacement parts"
                    ) or wp_title2.lower().startswith("mrp"):
                        support_info.mrplwp(wpno)
                    elif wp_title2.lower().startswith(
                        "critical safety items"
                    ) or wp_title2.lower().startswith("csi"):
                        support_info.csi_wp(wpno)
                    elif wp_title2.lower().startswith("support items"):
                        support_info.supitemwp(wpno)
                    elif wp_title2.lower().startswith("additional supporting"):
                        support_info.genwp(wpno)
    support_info.end()


def get_supporting_information_mac(
    manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws
) -> None:
    """Calls SupportingInformation and all of it's methods to create a Supporting Info Chapter in XML."""
    support_info = si.SupportingInformation(
        manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path
    )
    support_info.start()
    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title.lower() == "supporting information":
            S += 1
            for row2 in islice(ws.rows, S, None):
                wpno = row2[1].value
                wp_title2 = row2[2].value
                if wpno and wpno[0] == "S":
                    if wp_title2.lower() == "references":
                        support_info.refwp(wpno)
                    elif (
                        "intro" in wp_title2.lower()
                        or "introduction" in wp_title2.lower()
                    ):
                        support_info.macintrowp(wpno)
                    elif (
                        "mac" in wp_title2.lower()
                        or "maintenance allocation chart" in wp_title2.lower()
                    ):
                        support_info.macwp(wpno)
                    elif (
                        "coei" in wp_title2.lower()
                        or "components of end item" in wp_title2.lower()
                    ):
                        support_info.coeibiiwp(wpno)
                    elif (
                        wp_title2.lower().startswith("additional authorization list")
                        or wp_title2.lower() == "aal"
                    ):
                        support_info.aalwp(wpno)
                    elif wp_title2.lower().startswith(
                        "expendable"
                    ) or wp_title2.lower().startswith("edil"):
                        support_info.explistwp(wpno)
                    elif wp_title2.lower().startswith(
                        "tool"
                    ) or wp_title2.lower().startswith("til"):
                        support_info.toolidwp(wpno)
                    elif wp_title2.lower().startswith(
                        "mandatory replacement parts"
                    ) or wp_title2.lower().startswith("mrp"):
                        support_info.mrplwp(wpno)
                    elif wp_title2.lower().startswith(
                        "critical safety items"
                    ) or wp_title2.lower().startswith("csi"):
                        support_info.csi_wp(wpno)
                    elif wp_title2.lower().startswith("support items"):
                        support_info.supitemwp(wpno)
                    elif wp_title2.lower().startswith("additional supporting"):
                        support_info.genwp(wpno)
    support_info.end()


def get_supporting_information_nmwr(
    manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path, ws
) -> None:
    """Calls SupportingInformation and all of it's methods to create a Supporting Info Chapter in XML."""
    support_info = si.SupportingInformation(
        manual, milstd, SYS_ACRONYM, SYS_NAME, tmno, save_path
    )
    support_info.start()
    S = 0
    for row in islice(ws.rows, 1, None):
        wp_title = row[2].value
        S += 1
        if wp_title.lower() == "supporting information":
            S += 1
            for row2 in islice(ws.rows, S, None):
                wpno = row2[1].value
                wp_title2 = row2[2].value
                if wpno and wpno[0] == "S":
                    if wp_title2.lower() == "references":
                        support_info.refwp(wpno)
                    elif wp_title2.lower().startswith(
                        "expendable"
                    ) or wp_title2.lower().startswith("edil"):
                        support_info.explistwp(wpno)
                    elif wp_title2.lower().startswith(
                        "tool"
                    ) or wp_title2.lower().startswith("til"):
                        support_info.toolidwp(wpno)
                    elif wp_title2.lower().startswith(
                        "mandatory replacement parts"
                    ) or wp_title2.lower().startswith("mrp"):
                        support_info.mrplwp(wpno)
                    elif wp_title2.lower().startswith(
                        "critical safety items"
                    ) or wp_title2.lower().startswith("csi"):
                        support_info.csi_wp(wpno)
                    elif wp_title2.lower().startswith("additional supporting"):
                        support_info.genwp(wpno)
    support_info.end()


def get_rear_matter(manual, milstd, SYS_ACRONYM, save_path) -> None:
    """Calls RearMatter and all of it's methods to create a Rear Matter Chapter in XML."""
    rm.RearMatter(manual, milstd, SYS_ACRONYM, save_path).rear_matter()
