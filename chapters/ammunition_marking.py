"""AMMUNITION MARKING MAINTENANCE INSTRUCTIONS"""

import datetime
import math

import cfg
import views.isb as isb
import views.metadata as md


class AmmunitionMarking:
    """Class to create various types of WP's included in the Ammunition
    Marking Maintenance Instructions chapter of a TM."""

    date: str = datetime.datetime.today().strftime("%d %B %Y").upper()
    FPI_2C = "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN"
    FPI_2D = "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN"
    FPI_E = "-//USA-DOD//DTD -E TM Assembly REV E 8.0 20250417//EN"

    def __init__(
        self, manual_type, mil_std, sys_acronym, sys_name, tmno, save_path
    ) -> None:
        self.manual_type = manual_type
        self.mil_std = mil_std
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.tmno = tmno
        self.save_path = save_path

    def start(self) -> None:
        """Function that creates the Ammunition Marking Maintenance
        Instructions chapter header of TM."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<mim revno="0" chngno="0" chap-toc="no">\n"""
        tmp += '\t<titlepg maintlvl="maintainer">\n'
        tmp += (
            "\t\t<name>" + self.sys_name + " (" + self.sys_acronym + ")" + "</name>\n"
        )
        tmp += "\t</titlepg>\n"
        tmp += "\t<ammunitioncategory>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-AMMO_MARKING_START.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def ammo_markingwp(self) -> None:
        """Function to create the Ammunition Marking Information WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE production PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE production PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE production PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            '<ammo.markingwp chngno="0" wpno="O0-' + self.tmno + '" security="cui">\n'
        )

        # WP.METADATA Section
        tmp += md.show("ammo.markingwp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += """<title>AMMUNITION MARKING INFORMATION</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += "\t<mark>\n"
        tmp += "\t\t<proc>\n"
        tmp += "\t\t\t<title/>\n"
        tmp += "\t\t\t<para></para>\n"
        tmp += "\t\t</proc>\n"
        tmp += "\t</mark>\n"

        tmp += "\t<ammo.handling>\n"
        tmp += "\t\t<pack>\n"
        tmp += "\t\t\t<proc>\n"
        tmp += "\t\t\t<title/>\n"
        tmp += "\t\t\t<para></para>\n"
        tmp += "\t\t\t</proc>\n"
        tmp += "\t\t</pack>\n"
        tmp += "\t</ammo.handling>\n"

        tmp += "\t<ammotype>\n"
        tmp += "\t\t<proc>\n"
        tmp += "\t\t\t<title>AMMUNITION TYPES</title>\n"
        tmp += "\t\t\t<para></para>\n"
        tmp += "\t\t</proc>\n"
        tmp += "\t</ammotype>\n"

        tmp += "</ammo.markingwp>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-O00001-Ammunition Marking Info.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create the Ammunition Marking Maintenance
        Instructions chapter end tags."""
        cfg.prefix_file = ((math.ceil(cfg.prefix_file / 1000)) * 1000) - 1
        tmp = "\t</ammunitioncategory>\n" + "</mim>"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-AMMO_MARKING_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
