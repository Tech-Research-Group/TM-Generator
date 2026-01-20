"""SOFTWARE INFORMATION INSTRUCTIONS"""

import datetime
import math

import cfg
import views.isb as isb
import views.metadata as md
import views.proc as proc


class SoftwareInformation:
    """Class to create various types of WP's included in the Software Information chapter of a TM."""

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
        """Function that creates the Software Information chapter header of TM."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<soim revno="0" chngno="0" chap-toc="no">\n"""
        tmp += f'\t<titlepg maintlvl="{self.maintenance_level()}">\n'
        tmp += (
            "\t\t<name>" + self.sys_name + " (" + self.sys_acronym + ")" + "</name>\n"
        )
        tmp += "\t</titlepg>\n"
        tmp += "\t<softwarecategory>\n"

        file_name = f"{cfg.prefix_file:05d}-SOFTWARE_INFORMATION_START.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.auxiliary_equipment.append(file_name)
        cfg.prefix_file += 10

    def softginfowp(self, wpno) -> None:
        """Function to create the Software General Information WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softginfowp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softginfowp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softginfowp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            f'<softginfowp chngno="0" wpno="{wpno}-' + self.tmno + '" security="cui">\n'
        )

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += "\t\t<title>SOFTWARE GENERAL INFORMATION</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += "\t<scope>\n"
        tmp += "\t\t<title/>\n"
        tmp += "\t\t<para0></para0>\n"
        tmp += "\t</scope>\n"

        tmp += "\t<mfrr>\n"
        tmp += "\t\t<title/>\n"
        tmp += "\t\t<para></para>\n"
        tmp += "\t</mfrr>\n"

        tmp += "\t<eir>\n"
        tmp += "\t\t<title/>\n"
        tmp += "\t\t<para0></para0>\n"
        tmp += "\t</eir>\n"

        tmp += "\t<softsysover>\n"
        tmp += "\t\t<title/>\n"
        tmp += "\t\t<para0></para0>\n"
        tmp += "\t</softsysover>\n"

        tmp += "\t<softdocover>\n"
        tmp += "\t\t<title/>\n"
        tmp += "\t\t<para0></para0>\n"
        tmp += "\t</softdocover>\n"

        tmp += "\t<!-- OTHER OPTIONS THAT CAN BE INCLUDED: -->\n"
        tmp += "\t<!-- wrntyref | destructmat | nomenreflist -->\n"

        tmp += "\t<loa>\n"
        tmp += "\t\t<title/>\n"
        tmp += "\t\t<para0></para0>\n"
        tmp += "\t</loa>\n"
        tmp += "</softginfowp>"

        file_name = f"{cfg.prefix_file:05d}-{wpno}-Software General Info.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.software_information.append(file_name)
        cfg.prefix_file += 10

    def softsumwp(self, wpno) -> None:
        """Function to create the Software Summary WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softsumwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softsumwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softsumwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            f'<softsumwp chngno="0" wpno="{wpno}-' + self.tmno + '" security="cui">\n'
        )

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += "\t\t<title>SOFTWARE SUMMARY</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += "\t<!-- OTHER OPTIONS THAT CAN BE INCLUDED HERE: -->\n"
        tmp += "\t<!-- alert;, soft_app? -->\n"
        tmp += "\t<soft_inventory>\n"
        tmp += "\t\t<para0>\n"
        tmp += "\t\t\t<title>Software Inventory</title>\n"
        tmp += "\t\t\t<para></para>\n"
        tmp += "\t\t\t<para></para>\n"
        tmp += "\t\t</para0>\n"
        tmp += "\t</soft_inventory>\n"

        tmp += "\t<soft_environment>\n"
        tmp += "\t\t<para0>\n"
        tmp += "\t\t\t<title>Software Environment</title>\n"
        tmp += "\t\t\t<para></para>\n"
        tmp += "\t\t</para0>\n"
        tmp += "\t</soft_environment>\n"

        tmp += "\t<!-- OTHER OPTIONS THAT CAN BE INCLUDED HERE: -->\n"
        tmp += "\t<!-- soft_secpriv?, soft_superctrls?, soft_assistreport? -->\n"
        tmp += "</softsumwp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Software Summary.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.software_information.append(file_name)
        cfg.prefix_file += 10

    def softeffectwp(self, wpno) -> None:
        """Function to create the Software Information Effectivity WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softeffectwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softeffectwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softeffectwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Software Information Effectivity.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.software_information.append(file_name)

    def softdiffversionwp(self, wpno) -> None:
        """Function to create the Software Information Differences Between Software Versions WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softdiffversionwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softdiffversionwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softdiffversionwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Software Information Differences Between Software Versions.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.software_information.append(file_name)

    def softfeaturescapwp(self, wpno) -> None:
        """Function to create the Software Information Features and Capabilities WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softfeaturescapwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd"dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softfeaturescapwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softfeaturescapwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            f'<softfeaturescapwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'
        )

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += "\t\t<title>SOFTWARE FEATURES AND CAPABILITIES</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += proc.show()
        tmp += proc.show()
        tmp += "</softfeaturescapwp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Software Information Features and Capabilities.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.software_information.append(file_name)
        cfg.prefix_file += 10

    def softscreendisplaywp(self, wpno) -> None:
        """Function to create the Software Information Screen Displays WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softscreendisplaywp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd"dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softscreendisplaywp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softscreendisplaywp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<softscreendisplaywp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += """\t\t<title>SCREEN DISPLAYS</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += proc.show()
        tmp += proc.show()
        tmp += "</softscreendisplaywp>"
        file_name = (
            f"{cfg.prefix_file:05d}-{wpno}-Software Information Screen Displays.xml"
        )
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.software_information.append(file_name)
        cfg.prefix_file += 10

    def softmenuwp(self, wpno) -> None:
        """Function to create the Software Information Menus and Directories WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softmenuwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd"dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softmenuwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softmenuwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<softmenuwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += "\t\t<title>MENU/DIRECTORIES</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += proc.show()
        tmp += proc.show()
        tmp += "</softmenuwp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Software Information Menus and Directories.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.software_information.append(file_name)
        cfg.prefix_file += 10

    def softtoolswp(self, wpno) -> None:
        """Function to create the Software Tools and Buttons WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softtoolswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd"dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softtoolswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softtoolswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<softtoolswp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += "\t\t<title>TOOLS AND BUTTONS</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += "\t<ctrlindtab>\n"
        tmp += "\t\t<title></title>\n"
        tmp += '\t\t<figure id="SXXXXX-XX-XXXX-XXX-FXXXX">\n'
        tmp += "\t\t\t<title></title>\n"
        tmp += '\t\t\t<graphic boardno="PLACEHOLDER"/>\n'
        tmp += "\t\t</figure>\n"
        tmp += "\t\t<ctrlindrow>\n"
        tmp += "\t\t\t<key></key>\n"
        tmp += "\t\t\t<ctrlind></ctrlind>\n"
        tmp += "\t\t\t<function></function>\n"
        tmp += "\t\t</ctrlindrow>\n"
        tmp += "\t\t<ctrlindrow>\n"
        tmp += "\t\t\t<key></key>\n"
        tmp += "\t\t\t<ctrlind></ctrlind>\n"
        tmp += "\t\t\t<function></function>\n"
        tmp += "\t\t</ctrlindrow>\n"
        tmp += "\t\t<ctrlindrow>\n"
        tmp += "\t\t\t<key></key>\n"
        tmp += "\t\t\t<ctrlind></ctrlind>\n"
        tmp += "\t\t\t<function></function>\n"
        tmp += "\t\t</ctrlindrow>\n"
        tmp += "\t\t<ctrlindrow>\n"
        tmp += "\t\t\t<key></key>\n"
        tmp += "\t\t\t<ctrlind></ctrlind>\n"
        tmp += "\t\t\t<function></function>\n"
        tmp += "\t\t</ctrlindrow>\n"
        tmp += "\t\t<ctrlindrow>\n"
        tmp += "\t\t\t<key></key>\n"
        tmp += "\t\t\t<ctrlind></ctrlind>\n"
        tmp += "\t\t\t<function></function>\n"
        tmp += "\t\t</ctrlindrow>\n"
        tmp += "\t</ctrlindtab>\n"
        tmp += "\t<ctrlindtab>\n"
        tmp += "\t\t<title></title>\n"
        tmp += '\t\t<figure id="SXXXXX-XX-XXXX-XXX-FXXXX">\n'
        tmp += "\t\t\t<title></title>\n"
        tmp += '\t\t\t<graphic boardno="PLACEHOLDER"/>\n'
        tmp += "\t\t</figure>\n"
        tmp += "\t\t<ctrlindrow>\n"
        tmp += "\t\t\t<key></key>\n"
        tmp += "\t\t\t<ctrlind></ctrlind>\n"
        tmp += "\t\t\t<function></function>\n"
        tmp += "\t\t</ctrlindrow>\n"
        tmp += "\t\t<ctrlindrow>\n"
        tmp += "\t\t\t<key></key>\n"
        tmp += "\t\t\t<ctrlind></ctrlind>\n"
        tmp += "\t\t\t<function></function>\n"
        tmp += "\t\t</ctrlindrow>\n"
        tmp += "\t\t<ctrlindrow>\n"
        tmp += "\t\t\t<key></key>\n"
        tmp += "\t\t\t<ctrlind></ctrlind>\n"
        tmp += "\t\t\t<function></function>\n"
        tmp += "\t\t</ctrlindrow>\n"
        tmp += "\t</ctrlindtab>\n"
        tmp += "</softtoolswp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Software Tools and Buttons.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.software_information.append(file_name)
        cfg.prefix_file += 10

    def softsecprivwp(self, wpno) -> None:
        """Function to create the Software Information Security and Privacy Procedures WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softsecprivwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softsecprivwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softsecprivwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<softsecprivwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += "\t\t<title>SECURITY AND PRIVACY PROCEDURES</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += proc.show()
        tmp += proc.show()
        tmp += "</softsecprivwp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Software Information Security and Privacy.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.software_information.append(file_name)
        cfg.prefix_file += 10

    def softsuperctrlswp(self, wpno) -> None:
        """Function to create the Software Supervisory Controls WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softsuperctrlswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softsuperctrlswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softsuperctrlswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Software Supervisory Controls.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.software_information.append(file_name)

    def softpowerupwp(self, wpno) -> None:
        """Function to create the Software Powerup/Powerdown Procedures WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softpowerupwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softpowerupwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softpowerupwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<softpowerupwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += "\t\t<title>POWERUP/STARTUP AND POWERDOWN/SHUTDOWN PROCEDURES</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += proc.show()
        tmp += proc.show()
        tmp += "</softpowerupwp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Software Powerup/Powerdown.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.software_information.append(file_name)
        cfg.prefix_file += 10

    def softaccesswp(self, wpno) -> None:
        """Function to create the Accessing/Exiting Software
        WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softaccesswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softaccesswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softaccesswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<softaccesswp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += "\t\t<title>ACCESSING/EXITING SOFTWARE</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += proc.show()
        tmp += proc.show()
        tmp += "</softaccesswp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Accessing/Exiting Software.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.software_information.append(file_name)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create the Software Information chapter end tags."""
        tmp = "\t</softwarecategory>"
        tmp += "</soim>"
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-SOFTWARE_INFORMATION_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
