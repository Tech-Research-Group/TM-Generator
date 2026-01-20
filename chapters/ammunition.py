"""AMMUNITION MAINTENANCE INSTRUCTIONS"""

import datetime
import math

import cfg
import views.isb as isb
import views.metadata as md


class Ammunition:
    """Class to create various types of WP's included in the Ammunition
    Maintenance Instructions chapter of a TM."""

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

    def maintenance_level(self) -> str:
        """Function to find maintenance level for a chapter or work package"""
        if self.manual_type == "-10":
            level = "operator"
        elif self.manual_type == "NMWR":
            level = "depot"
        else:
            level = "maintainer"
        return level

    def start(self) -> None:
        """Function that creates the Ammunition Maintenance
        Instructions chapter header of TM."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<mim revno="0" chngno="0" chap-toc="no">\n"""
        tmp += f'\t<titlepg maintlvl="{self.maintenance_level()}">\n'
        tmp += f"\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n"
        tmp += "\t</titlepg>\n"
        tmp += "\t<ammunitioncategory>\n"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + f" IADS/files/{cfg.prefix_file:05d}-AMMUNITION_START.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def ammoidentwp(self, wpno) -> None:
        """Function to create the Ammo Identification WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE ammoidentwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE ammoidentwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE ammoidentwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<ammoidentwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += """<title>AMMUNITION IDENTIFICATION</title>
    </wpidinfo>\n"""
        tmp += isb.show()

        tmp += "</ammoidentwp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Ammo Identification.xml"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + f" IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.ammunition.append(file_name)
        cfg.prefix_file += 10

    def surwp(self, wpno) -> None:
        """Function to create the Service Upon Receipt WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE surwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE surwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += (
                f'<!DOCTYPE surwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
            )
        tmp += f'<surwp chngno="0" wpno="{wpno}-{self.tmno}"  security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += """<title>SERVICE UPON RECEIPT</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += "\t<surtsk>\n"
        tmp += "\t\t<ammo.defect>\n"
        tmp += "\t\t\t<proc>\n"
        tmp += "\t\t\t\t<title/>\n"
        tmp += "\t\t\t\t<para></para>\n"
        tmp += "\t\t\t</proc>\n"
        tmp += "\t\t</ammo.defect>\n"
        tmp += "\t</surtsk>\n"
        tmp += "\t<surtsk>\n"
        tmp += "\t\t<ammo.handling>\n"
        tmp += "\t\t\t<unpack>\n"
        tmp += "\t\t\t\t<proc>\n"
        tmp += "\t\t\t\t\t<title/>\n"
        tmp += "\t\t\t\t\t<para></para>\n"
        tmp += "\t\t\t\t</proc>\n"
        tmp += "\t\t\t</unpack>\n"
        tmp += "\t\t\t<pack>\n"
        tmp += "\t\t\t\t<proc>\n"
        tmp += "\t\t\t\t\t<title/>\n"
        tmp += "\t\t\t\t\t<para></para>\n"
        tmp += "\t\t\t\t</proc>\n"
        tmp += "\t\t\t</pack>\n"
        tmp += "\t\t</ammo.handling>\n"
        tmp += "\t</surtsk>\n"
        tmp += "\t<!-- OTHER OPTIONAL SURTSK's THAT CAN BE INCLUDED: -->\n"
        tmp += "\t<!-- arm | calign | install | mark | other.surtsk | precal | prechkadj | preserv | shltr | siting | surmat -->\n"
        tmp += "</surwp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Ammunition SUR WP.xml"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + f" IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.ammunition.append(file_name)
        cfg.prefix_file += 10

    def ammowp(self, wpno) -> None:
        """Function to create the Ammunition Maintenance WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE ammowp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE ammowp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE ammowp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<ammowp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += """<title>AMMUNITION MAINTENANCE</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += "\t<mark>\n"
        tmp += "\t\t<proc>\n"
        tmp += "\t\t\t<title/>\n"
        tmp += "\t\t\t<para></para>\n"
        tmp += "\t\t</proc>\n"
        tmp += "\t</mark>\n"

        tmp += "\t<ammo.defect>\n"
        tmp += "\t\t<proc>\n"
        tmp += "\t\t\t<title/>\n"
        tmp += "\t\t\t<para></para>\n"
        tmp += "\t\t</proc>\n"
        tmp += "\t</ammo.defect>\n"

        tmp += "\t<ammo.handling>\n"
        tmp += "\t\t<unpack>\n"
        tmp += "\t\t\t<proc>\n"
        tmp += "\t\t\t<title/>\n"
        tmp += "\t\t\t<para></para>\n"
        tmp += "\t\t\t</proc>\n"
        tmp += "\t\t</unpack>\n"
        tmp += "\t\t<pack>\n"
        tmp += "\t\t\t<proc>\n"
        tmp += "\t\t\t<title/>\n"
        tmp += "\t\t\t<para></para>\n"
        tmp += "\t\t\t</proc>\n"
        tmp += "\t\t</pack>\n"
        tmp += "\t</ammo.handling>\n"

        tmp += "\t<paint>\n"
        tmp += "\t\t<proc>\n"
        tmp += "\t\t\t<title/>\n"
        tmp += "\t\t\t<para></para>\n"
        tmp += "\t\t</proc>\n"
        tmp += "\t</paint>\n"

        tmp += "\t<clean>\n"
        tmp += "\t\t\t<title/>\n"
        tmp += "\t\t\t<para></para>\n"
        tmp += "\t</clean>\n"

        tmp += "</ammowp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Ammunition Maintenance.xml"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + f" IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.ammunition.append(file_name)
        cfg.prefix_file += 10

    def ammo_markingwp(self, wpno) -> None:
        """Function to create the Ammunition Marking Information WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE ammo.markingwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE ammo.markingwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE ammo.markingwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<ammo.markingwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
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
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Ammunition Marking Info.xml"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + f" IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.ammunition.append(file_name)
        cfg.prefix_file += 10

    def natowp(self, wpno) -> None:
        """Function to create the Foreign Ammunition (NATO) WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE natowp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE natowp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE natowp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<natowp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += """<title>FOREIGN AMMUNITION (NATO)</title>
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

        tmp += "</natowp>\n"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Foreign Ammunition.xml"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + f" IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.ammunition.append(file_name)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create the Ammunition Maintenance Instructions chapter end tags."""
        tmp = "\t</ammunitioncategory>"
        tmp += "</mim>"
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + f" IADS/files/{cfg.prefix_file:05d}-AMMUNITION_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
