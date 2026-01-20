###TOC FILE###

import datetime

import cfg


class TOC:
    """Class to create a toc.xml file for Arbortext."""

    date: str = datetime.datetime.today().strftime("%d %B %Y").upper()
    FPI_2C = "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN"
    FPI_2D = "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN"
    FPI_E = "-//USA-DOD//DTD -E TM Assembly REV E 8.0 20250417//EN"

    def __init__(self, manual_type, sys_acronym, save_path) -> None:
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.save_path = save_path

    def build_toc(self) -> None:
        """Function to build the TOC.xml for the IADS project."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<toc xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <tocEntry title="FRONT MATTER">
		<tocEntry filename="files/00010_F00001_Front Cover.xml"/>
		<tocEntry filename="files/00020_F00002_Warning Summary.xml" title="WARNING SUMMARY"/>
		<tocEntry filename="files/00030_F00003_LOEP.xml" title="LIST OF EFFECTIVE PAGES/WORK PACKAGES"/>
		<tocEntry filename="files/00040_F00004_Title Block.xml" title="TITLE BLOCK"/>
		<tocEntry filename="files/00060_F00006_How To Use.xml" title="HOW TO USE THIS MANUAL"/>
	</tocEntry>\n"""

        if cfg.chapter1:
            tmp += '\t<tocEntry title="GENERAL INFORMATION">\n'
            for filename in cfg.chapter1:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.operator_instructions:
            tmp += '\t<tocEntry title="OPERATOR INSTRUCTIONS">\n'
            for filename in cfg.operator_instructions:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.ts_master_index_o:
            tmp += '\t<tocEntry title="TROUBLESHOOTING MASTER INDEX">\n'
            for filename in cfg.ts_master_index_o:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.ts_operator:
            tmp += '\t<tocEntry title="OPERATOR TROUBLESHOOTING">\n'
            for filename in cfg.ts_operator:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.pmcs_o:
            tmp += '\t<tocEntry title="OPERATOR PREVENTIVE MAINTENANCE CHECKS AND SERVICES">\n'
            for filename in cfg.pmcs_o:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.procedures_o:
            tmp += '\t<tocEntry title="OPERATOR MAINTENANCE">\n'
            for filename in cfg.procedures_o:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.ts_maintainer:
            tmp += '\t<tocEntry title="MAINTAINER TROUBLESHOOTING">\n'
            for filename in cfg.ts_maintainer:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.pmcs_m:
            tmp += '\t<tocEntry title="MAINTAINER PREVENTIVE MAINTENANCE CHECKS AND SERVICES">\n'
            for filename in cfg.pmcs_m:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.procedures_m:
            tmp += '\t<tocEntry title="MAINTAINER MAINTENANCE">\n'
            for filename in cfg.procedures_m:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.ts_depot:
            tmp += '\t<tocEntry title="DEPOT TROUBLESHOOTING">\n'
            for filename in cfg.ts_depot:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.procedures_d:
            tmp += '\t<tocEntry title="DEPOT MAINTENANCE">\n'
            for filename in cfg.procedures_d:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.auxiliary_equipment:
            tmp += '\t<tocEntry title="AUXILIARY EQUIPMENT MAINTENANCE">\n'
            for filename in cfg.auxiliary_equipment:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.ammunition:
            tmp += '\t<tocEntry title="AMMUNITION MAINTENANCE">\n'
            for filename in cfg.ammunition:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.shipment_instructions:
            tmp += '\t<tocEntry title="SHIPMENT/MOVEMENT AND STORAGE MAINTENANCE">\n'
            for filename in cfg.shipment_instructions:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.destruction:
            tmp += (
                '\t<tocEntry title="DESTRUCTION OF EQUIPMENT TO PREVENT ENEMY USE">\n'
            )
            for filename in cfg.destruction:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.software_information:
            tmp += '\t<tocEntry title="SOFTWARE INFORMATION">\n'
            for filename in cfg.software_information:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.rpstl:
            tmp += '\t<tocEntry title="REPAIR PARTS AND SPECIAL TOOLS LIST">\n'
            for filename in cfg.rpstl:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        if cfg.supporting_information:
            tmp += '\t<tocEntry title="SUPPORTING INFORMATION">\n'
            for filename in cfg.supporting_information:
                tmp += f'\t\t<tocEntry filename="files/{filename}"/>\n'
            tmp += "\t</tocEntry>\n"

        tmp += """\t<tocEntry title="REAR MATTER">
        <tocEntry filename="files/ZZZZZ_999999_Rear Matter.xml"/>
    </tocEntry>
</toc>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/toc.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
