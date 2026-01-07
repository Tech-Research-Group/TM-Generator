"""MIL-STANDARD 2C BUILD FUNCTIONS"""

import chapter_functions as cf
import chapters.ammunition as a
import chapters.software_information as so


def build_10(
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
    ws,
    chb_1,
    chb_2,
    chb_5,
    chb_6,
    chb_tmi,
) -> None:
    """Calls methods to build each work package for a -10 TM shell using MIL-STD-2C."""
    cf.get_entity_declarations(SYS_ACRONYM, manual, milstd, save_path)
    # FRONT MATTER
    cf.get_front_matter(
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
    # CHAPTER1
    cf.get_chapter1(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path)
    # OPERATOR INSTRUCTIONS
    cf.get_operator_instructions(
        manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws
    )
    # TROUBLESHOOTING MASTER INDEX
    if chb_tmi.get() == 1:
        cf.get_ts_master_index(
            manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws
        )
    # OPERATOR TROUBLESHOOTING
    cf.get_operator_ts(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # OPERATOR PMCS
    cf.get_operator_pmcs(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # OPERATOR MAINTENANCE PROCEDURES
    cf.get_operator_maintenance(
        manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws
    )
    # AUXILIARY EQUIPMENT - OPTIONAL
    if chb_1.get() == 1:
        cf.get_auxiliary(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # AMMUNITION - OPTIONAL
    if chb_2.get() == 1:
        pass
    # DESTRUCTION - OPTIONAL
    if chb_5.get() == 1:
        cf.get_destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # SOFTWARE INFORMATION - OPTIONAL
    if chb_6.get() == 1:
        pass
    # SUPPORTING INFORMATION
    cf.get_supporting_information(
        manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws
    )
    # REAR MATTER
    cf.get_rear_matter(manual, milstd, SYS_ACRONYM, save_path)


def build_13p(
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
    ws,
    chb_1,
    chb_2,
    chb_5,
    chb_6,
    chb_tmi,
) -> None:
    """Calls methods to build each work package for a -13&P TM shell using MIL-STD-2C."""
    cf.get_entity_declarations(SYS_ACRONYM, manual, milstd, save_path)
    # FRONT MATTER
    cf.get_front_matter(
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
    # CHAPTER1
    cf.get_chapter1(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path)
    # OPERATOR INSTRUCTIONS
    cf.get_operator_instructions(
        manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws
    )
    # TROUBLESHOOTING MASTER INDEX
    if chb_tmi.get() == 1:
        cf.get_ts_master_index(
            manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws
        )
    # OPERATOR TROUBLESHOOTING
    cf.get_operator_ts(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # MAINTAINER TROUBLESHOOTING
    cf.get_maintainer_ts(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # OPERATOR PMCS
    cf.get_operator_pmcs(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # MAINTAINER PMCS
    cf.get_maintainer_pmcs(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # OPERATOR MAINTENANCE PROCEDURES
    cf.get_operator_maintenance(
        manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws
    )
    # MAINTAINER MAINTENANCE PROCEDURES
    cf.get_maintainer_maintenance(
        manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws
    )
    # AUXILIARY EQUIPMENT - OPTIONAL
    if chb_1.get() == 1:
        cf.get_auxiliary(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # AMMUNITION - OPTIONAL
    if chb_2.get() == 1:
        pass
    # DESTRUCTION - OPTIONAL
    if chb_5.get() == 1:
        cf.get_destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # SOFTWARE INFORMATION - OPTIONAL
    if chb_6.get() == 1:
        pass
    # RPSTL
    cf.get_rpstl(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # SUPPORTING INFORMATION
    cf.get_supporting_information_mac(
        manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws
    )
    # REAR MATTER
    cf.get_rear_matter(manual, milstd, SYS_ACRONYM, save_path)


def build_23p(
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
    ws,
    chb_1,
    chb_2,
    chb_5,
    chb_6,
    chb_tmi,
) -> None:
    """Calls methods to build each work package for a -23&P TM shell using MIL-STD-2C."""
    cf.get_entity_declarations(SYS_ACRONYM, manual, milstd, save_path)
    # FRONT MATTER
    cf.get_front_matter(
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
    # CHAPTER1
    cf.get_chapter1(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path)
    # TROUBLESHOOTING MASTER INDEX
    if chb_tmi.get() == 1:
        cf.get_ts_master_index(
            manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws
        )
        # MAINTAINER TROUBLESHOOTING
    cf.get_maintainer_ts(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # MAINTAINER PMCS
    cf.get_maintainer_pmcs(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # MAINTAINER MAINTENANCE PROCEDURES
    cf.get_maintainer_maintenance(
        manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws
    )
    # AUXILIARY EQUIPMENT - OPTIONAL
    if chb_1.get() == 1:
        cf.get_auxiliary(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # AMMUNITION - OPTIONAL
    if chb_2.get() == 1:
        pass
    # DESTRUCTION - OPTIONAL
    if chb_5.get() == 1:
        cf.get_destruction(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # SOFTWARE INFORMATION - OPTIONAL
    if chb_6.get() == 1:
        pass
    # RPSTL
    cf.get_rpstl(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # SUPPORTING INFORMATION
    cf.get_supporting_information_mac(
        manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws
    )
    # REAR MATTER
    cf.get_rear_matter(manual, milstd, SYS_ACRONYM, save_path)


def build_nmwr(
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
) -> None:
    """Calls methods to build each work package for a NMWR shell using MIL-STD-2C."""
    cf.get_entity_declarations(SYS_ACRONYM, manual, milstd, save_path)
    # FRONT MATTER
    cf.get_front_matter(
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
    # CHAPTER1
    cf.get_chapter1(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path)
    # DEPOT TROUBLESHOOTING
    cf.get_depot_ts(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # DEPOT MAINTENANCE PROCEDURES
    cf.get_depot_maintenance(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # RPSTL
    cf.get_rpstl(manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws)
    # SUPPORTING INFORMATION
    cf.get_supporting_information_nmwr(
        manual, milstd, SYS_ACRONYM, SYS_NAME, TMNO, save_path, ws
    )
    # REAR MATTER
    cf.get_rear_matter(manual, milstd, SYS_ACRONYM, save_path)
