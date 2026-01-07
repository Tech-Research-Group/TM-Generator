"""DESTRUCTION OF EQUIPMENT TO PREVENT ENEMY USE"""

import datetime
import math

import cfg
import views.isb as isb
import views.metadata as md


class Destruction:
    """Class to create various types of WP's included in Desctruction section of a TM."""

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
        """Function to create Desctruction section start tags."""
        # cfg.prefix_file = math.floor(cfg.prefix_file / 1000) * 1000
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
    <dim chngno="0" revno="0" chap-toc="no">\n"""
        if self.manual_type == "-10":
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif (
            self.manual_type == "-12&P"
            or self.manual_type == "-13&P"
            or self.manual_type == "-23&P"
        ):
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += (
            "\t\t\t<name>" + self.sys_name + " (" + self.sys_acronym + ")" + "</name>\n"
        )
        tmp += "</titlepg>\n"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-DESTRUCTION_START.xml".format(cfg.prefix_file),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def destruct_introwp(self) -> None:
        """Function to create the Destruction section intro."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE destruct-introwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE destruct-introwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE destruct-introwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            '<destruct-introwp chngno="0" wpno="D00001-'
            + self.tmno
            + '" security="cui">'
        )

        # WP.METADATA Section
        tmp += md.show("destruct-introwp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        if self.manual_type == "-10":
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif (
            self.manual_type == "-12&P"
            or self.manual_type == "-13&P"
            or self.manual_type == "-23&P"
        ):
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += f"""\t\t<title>INTRODUCTION</title>
    </wpidinfo>
    <authorize_to_destroy>
        <title>AUTHORITY TO DESTROY</title>
        <para>Authorization. Only division or higher commanders have authority to order destruction of equipment. They may however, delegate this authority to subordinate commanders when situation demands it.</para>
    </authorize_to_destroy>
     <brk/>
    <report_destruct>
        <title>Reporting Destruction</title>
        <para>Report any destruction activity through command channels.</para>
    </report_destruct>
     <brk/>
    <general_destruct_info>
        <para0>
            <title>General Destruction Information</title>
            <para>{self.sys_name} ({self.sys_acronym}) does not contain classified equipment. Refer to Procedures for "Destruction of Equipment to Prevent Enemy Use" <extref docno="TM 750-244-3"/> for additional guidance.</para>
            <para>In the situation where {self.sys_acronym} must be destroyed, it can be destroyed via burning, explosives, burying, or any other means that would render it unusable for enemy.</para>
        </para0>
    </general_destruct_info>
    <degree_of_destruct>
        <title>Degree of Destruction</title>
        <para>
            <randlist>
                <item>Methods of Destruction. Choose methods of destruction which will cause such damage that it will be impossible to restore equipment to a usable condition within combat zone.</item>
                <item>Classified Equipment. Classified equipment must be destroyed to such a degree as to prevent duplication by, or revealing means of operation or function to enemy.</item>
                <item>Associated Classified Documents. Any classified documents, notes, instructions, or other written material pertaining to function, operation, maintenance, or employment, including drawings or parts lists, must be destroyed in a manner to render them useless to enemy.</item>
            </randlist>
        </para>
    </degree_of_destruct>\n"""
        tmp += "</destruct-introwp>"

        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-D00001-Destruction Introduction.xml".format(
                cfg.prefix_file
            ),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def destruct_materialwp(self, wpno, wp_title) -> None:
        """Function to create a Destruction WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE destruct-materialwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE destruct-materialwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE destruct-materialwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            f'<destruct-materialwp chngno="0" wpno="{wpno}-'
            + self.tmno
            + '" security="cui">'
        )

        # WP.METADATA Section
        tmp += md.show("destruct-materialwp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        if self.manual_type == "-10":
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif (
            self.manual_type == "-12&P"
            or self.manual_type == "-13&P"
            or self.manual_type == "-23&P"
        ):
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += f"""\t\t<title>{wp_title}</title>
    </wpidinfo>"""
        tmp += isb.show()
        tmp += """\t<proc>
        <title>Specific Destruction Procedures</title>
        <para></para>
    </proc>
</destruct-materialwp>"""
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-{}-{}.xml".format(cfg.prefix_file, wpno, wp_title),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create the Destruction section end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = "</dim>"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-DESTRUCTION_END.xml".format(cfg.prefix_file),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
