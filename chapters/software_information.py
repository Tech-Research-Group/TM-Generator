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

    def start(self) -> None:
        """Function that creates the Software Information chapter header of TM."""
        # cfg.prefix_file = math.floor(cfg.prefix_file / 1000) * 1000
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<soim revno="0" chngno="0" chap-toc="no">\n"""
        if self.manual_type == "-10" or self.manual_type == "-13&P":
            tmp += '\t\t<titlepg maintlvl="operator">\n'
        elif self.manual_type == "-23&P":
            tmp += '\t\t<titlepg maintlvl="maintainer">\n'
        tmp += (
            "\t\t\t<name>" + self.sys_name + " (" + self.sys_acronym + ")" + "</name>\n"
        )
        tmp += "\t\t</titlepg>\n"
        tmp += "\t\t<softwarecategory>\n"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-SOFTWARE_INFO_START.xml".format(cfg.prefix_file),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softginfowp(self) -> None:
        """Function to create the Software General Information WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softginfowp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softginfowp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softginfowp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            '<softginfowp chngno="0" wpno="S00101-' + self.tmno + '" security="cui">\n'
        )

        # WP.METADATA Section
        tmp += md.show("softginfowp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        if self.manual_type == "-10" or self.manual_type == "-13&P":
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == "-23&P":
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
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
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-S00101-Software General Info.xml".format(
                cfg.prefix_file
            ),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softsumwp(self) -> None:
        """Function to create the Software Summary WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softsumwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softsumwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softsumwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += '<softsumwp chngno="0" wpno="S00102-' + self.tmno + '" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("softsumwp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        if self.manual_type == "-10" or self.manual_type == "-13&P":
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == "-23&P":
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
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
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-S00102-Software Summary.xml".format(cfg.prefix_file),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softeffectwp(self) -> None:
        """Function to create the Software Information Effectivity WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softeffectwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softeffectwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softeffectwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'

    def softdiffversionwp(self) -> None:
        """Function to create the Software Information Differences Between Software Versions WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softdiffversionwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softdiffversionwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softdiffversionwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'

    def softfeaturescapwp(self) -> None:
        """Function to create the Software Information Features and Capabilities WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softfeaturescapwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd"dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softfeaturescapwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softfeaturescapwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            '<softfeaturescapwp chngno="0" wpno="S00105-'
            + self.tmno
            + '" security="cui">\n'
        )

        # WP.METADATA Section
        tmp += md.show("softfeaturescapwp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        if self.manual_type == "-10" or self.manual_type == "-13&P":
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == "-23&P":
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += "\t\t<title>SOFTWARE FEATURES AND CAPABILITIES</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += proc.show()
        tmp += proc.show()
        tmp += "</softfeaturescapwp>"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-S00105-SW Features Capabilities.xml".format(
                cfg.prefix_file
            ),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softscreendisplaywp(self) -> None:
        """Function to create the Software Information Screen Displays WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softscreendisplaywp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd"dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softscreendisplaywp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softscreendisplaywp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            '<softscreendisplaywp chngno="0" wpno="S00106-'
            + self.tmno
            + '" security="cui">\n'
        )

        # WP.METADATA Section
        tmp += md.show("softscreendisplaywp", self.tmno)

        tmp += """\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>SCREEN DISPLAYS</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += proc.show()
        tmp += proc.show()
        tmp += "</softscreendisplaywp>"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-S00106-Software Screen Displays.xml".format(
                cfg.prefix_file
            ),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softmenuwp(self) -> None:
        """Function to create the Software Information Menus and Directories WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softmenuwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd"dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softmenuwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softmenuwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            '<softmenuwp chngno="0" wpno="S00107-' + self.tmno + '" security="cui">\n'
        )

        # WP.METADATA Section
        tmp += md.show("softmenuwp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        if self.manual_type == "-10" or self.manual_type == "-13&P":
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == "-23&P":
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += "\t\t<title>MENU/DIRECTORIES</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += proc.show()
        tmp += proc.show()
        tmp += "</softmenuwp>"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-S00107-Software Menu.xml".format(cfg.prefix_file),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softtoolswp(self) -> None:
        """Function to create the Software Tools and Buttons WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softtoolswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd"dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softtoolswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softtoolswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            '<softtoolswp chngno="0" wpno="S00108-' + self.tmno + '" security="cui">\n'
        )

        # WP.METADATA Section
        tmp += md.show("softtoolswp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        if self.manual_type == "-10" or self.manual_type == "-13&P":
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == "-23&P":
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
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
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-S00108-SW Tools And Buttons.xml".format(
                cfg.prefix_file
            ),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softsecprivwp(self) -> None:
        """Function to create the Software Information Security and Privacy Procedures WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softsecprivwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softsecprivwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softsecprivwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            '<softsecprivwp chngno="0" wpno="S00109-'
            + self.tmno
            + '" security="cui">\n'
        )

        # WP.METADATA Section
        tmp += md.show("softsecprivwp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        if self.manual_type == "-10" or self.manual_type == "-13&P":
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == "-23&P":
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += "\t\t<title>SECURITY AND PRIVACY PROCEDURES</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += proc.show()
        tmp += proc.show()
        tmp += "</softsecprivwp>"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-S00109-Security And Privacy Procedures.xml".format(
                cfg.prefix_file
            ),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softsuperctrlswp(self) -> None:
        """Function to create the Software Supervisory Controls WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softsuperctrlswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softsuperctrlswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softsuperctrlswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'

    def softpowerupwp(self) -> None:
        """Function to create the Software Powerup/Powerdown Procedures WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softpowerupwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softpowerupwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softpowerupwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            '<softpowerupwp chngno="0" wpno="S00111-'
            + self.tmno
            + '" security="cui">\n'
        )

        # WP.METADATA Section
        tmp += md.show("softpowerupwp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        if self.manual_type == "-10" or self.manual_type == "-13&P":
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == "-23&P":
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += "\t\t<title>POWERUP/STARTUP AND POWERDOWN/SHUTDOWN PROCEDURES</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += proc.show()
        tmp += proc.show()
        tmp += "</softpowerupwp>"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-S00111-SW Power Procedures.xml".format(
                cfg.prefix_file
            ),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softaccesswp(self) -> None:
        """Function to create the Accessing/Exiting Software
        WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE softaccesswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE softaccesswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE softaccesswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            '<softaccesswp chngno="0" wpno="S00111-' + self.tmno + '" security="cui">\n'
        )

        # WP.METADATA Section
        tmp += md.show("softaccesswp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        if self.manual_type == "-10" or self.manual_type == "-13&P":
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == "-23&P":
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += "\t\t<title>ACCESSING/EXITING SOFTWARE</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += proc.show()
        tmp += proc.show()
        tmp += "</softaccesswp>"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-S00111-Accessing Exiting Software.xml".format(
                cfg.prefix_file
            ),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create the Software Information chapter end tags."""
        tmp = "\t</softwarecategory>"
        tmp += "</soim>"
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-SOFTWARE_INFO_END.xml".format(cfg.prefix_file),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
