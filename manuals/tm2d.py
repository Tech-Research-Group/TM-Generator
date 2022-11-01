"""MIL-STANDARD 2D BUILD FUNCTIONS"""
from itertools import islice
from dotenv import dotenv_values
import chapters.ammunition as a
import chapters.ammunition_marking as am
import chapters.auxiliary_equipment as ae
import chapters.chapter1 as ch1
import chapters.destruction as d
import chapters.entity_declarations as ed
import chapters.front_matter as fm
import chapters.operator_instructions as oi
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
import cfg

config = dotenv_values(".env")  # take environment variables from .env.

def build_10_tm(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws, chb_1, chb_2, chb_3, chb_4, chb_5, chb_6) -> None:
    """Calls methods to build each work package for a -10 TM shell using MIL-STD-2D."""
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

def build_12p_tm(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws, chb_1, chb_2, chb_5, chb_6) -> None:
    """Calls methods to build each work package for a -12&P TM shell using MIL-STD-2D."""
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

def build_nmwr(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws) -> None:
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
