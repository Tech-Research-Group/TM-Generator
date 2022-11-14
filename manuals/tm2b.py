"""MIL-STANDARD 2B BUILD FUNCTIONS"""
from dotenv import dotenv_values

import chapter_functions as cf

config = dotenv_values(".env")  # take environment variables from .env.

def build_10(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws, chb_1, chb_2,
             chb_5, chb_tmi) -> None:
    """Calls methods to build each work package for a -10 TM shell using MIL-STD-2B."""
    # ENTITY DECLARATIONS
    cf.get_entity_declarations(SYS_ACRONYM, manual, milstd, save_path)
    # FRONT MATTER
    cf.get_front_matter(FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    # CHAPTER1
    cf.get_chapter1(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    # OPERATOR INSTRUCTIONS
    cf.get_operator_instructions(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # TROUBLESHOOTING MASTER INDEX
    if chb_tmi.get() == 1:
        cf.get_ts_master_index(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # OPERATOR TROUBLESHOOTING
    cf.get_operator_ts(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # OPERATOR PMCS
    cf.get_operator_pmcs(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # OPERATOR MAINTENANCE PROCEDURES
    cf.get_operator_maintenance(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)

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
        cf.get_destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # SUPPORTING INFORMATION
    cf.get_supporting_information(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # REAR MATTER
    cf.get_rear_matter(manual, SYS_ACRONYM, save_path)


def build_13p(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws, chb_1, chb_2,
              chb_5, chb_tmi) -> None:
    """Calls methods to build each work package for a -13&P TM shell using MIL-STD-2B."""
    # ENTITY DECLARATIONS
    cf.get_entity_declarations(SYS_ACRONYM, manual, milstd, save_path)
    # FRONT MATTER
    cf.get_front_matter(FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    # CHAPTER1
    cf.get_chapter1(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    # OPERATOR INSTRUCTIONS
    cf.get_operator_instructions(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # TROUBLESHOOTING MASTER INDEX
    if chb_tmi.get() == 1:
        cf.get_ts_master_index(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # OPERATOR TROUBLESHOOTING
    cf.get_operator_ts(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # OPERATOR PMCS
    cf.get_operator_pmcs(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # OPERATOR MAINTENANCE PROCEDURES
    cf.get_operator_maintenance(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # MAINTAINER TROUBLESHOOTING
    cf.get_maintainer_ts(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # MAINTAINER PMCS
    cf.get_maintainer_pmcs(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # MAINTAINER MAINTENANCE
    cf.get_maintainer_maintenance(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
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
    cf.get_parts_information(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # DESTRUCTION - OPTIONAL
    if chb_5.get() == 1:
        cf.get_destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # SUPPORTING INFORMATION
    cf.get_supporting_information_mac(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # REAR MATTER
    cf.get_rear_matter(manual, SYS_ACRONYM, save_path)


def build_23p(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws, chb_1, chb_2,
              chb_5, chb_tmi) -> None:
    """Calls methods to build each work package for a -23&P TM shell using MIL-STD-2B."""
    # ENTITY DECLARATIONS
    cf.get_entity_declarations(SYS_ACRONYM, manual, milstd, save_path)
    # FRONT MATTER
    cf.get_front_matter(FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    # CHAPTER1
    cf.get_chapter1(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    # TROUBLESHOOTING MASTER INDEX
    if chb_tmi.get() == 1:
        cf.get_ts_master_index(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # MAINTAINER TROUBLESHOOTING
    cf.get_maintainer_ts(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # MAINTAINER PMCS
    cf.get_maintainer_pmcs(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # MAINTAINER MAINTENANCE
    cf.get_maintainer_maintenance(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
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
    cf.get_parts_information(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # DESTRUCTION - OPTIONAL
    if chb_5.get() == 1:
        cf.get_destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # SUPPORTING INFORMATION
    cf.get_supporting_information_mac(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # REAR MATTER
    cf.get_rear_matter(manual, SYS_ACRONYM, save_path)


def build_nmwr(FSC, manual, milstd, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws) -> None:
    """Calls methods to build each work package for a NMWR shell using MIL-STD-2B."""
    # ENTITY DECLARATIONS
    cf.get_entity_declarations(SYS_ACRONYM, manual, milstd, save_path)
    # FRONT MATTER
    cf.get_front_matter(FSC, manual, NIIN, PART_NO, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    # CHAPTER1
    cf.get_chapter1(manual, milstd, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path)
    # DEPOT TROUBLESHOOTING
    cf.get_depot_ts(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # DEPOT MAINTENANCE PROCEDURES
    cf.get_depot_maintenance(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # PARTS INFORMATION
    cf.get_parts_information()
    # SUPPORTING INFORMATION
    cf.get_supporting_information_nmwr(manual, SYS_ACRONYM, SYS_NAME, SYS_NUMBER, save_path, ws)
    # REAR MATTER
    cf.get_rear_matter(manual, SYS_ACRONYM, save_path)
