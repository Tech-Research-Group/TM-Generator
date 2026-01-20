"""MAINTAINER PROCEDURES"""

import datetime
import math

import cfg
import views.followon_maintsk as followon_maintsk
import views.isb as isb
import views.metadata as md
import views.proc as proc


class MaintainerProcedures:
    """Class to create various types of WP's included in Maintainer Procedures of a TM."""

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
        """Function to create Maintainer Procedures start tags."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<mim chngno="0" revno="0" chap-toc="no">\n"""
        tmp += '\t<titlepg maintlvl="maintainer">\n'
        tmp += f"\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n"
        tmp += "\t</titlepg>\n" + "\t<maintenancecategory>"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-MAINTAINER_MAINTENANCE_START.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def surwp(self, wpno) -> None:
        """Function to create Service Upon Receipt WP."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>"""
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE surwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE surwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += (
                f'<!DOCTYPE surwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
            )
        tmp += f'<surwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += """\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>SERVICE UPON RECEIPT</title>
        </wpidinfo>\n"""
        tmp += isb.show()
        tmp += """<surtsk>
            <siting>"""
        tmp += proc.show()
        tmp += """</siting>
        </surtsk>
        <surtsk>
            <surmat>
                <unpack>"""
        tmp += proc.show()
        tmp += """</unpack>
                <chkeqp>
                    <title/>
                    <para></para>
                </chkeqp>
            </surmat>
        </surtsk>
        <surtsk>
            <preserv>"""
        tmp += proc.show()
        tmp += """</preserv>
        </surtsk>
        <surtsk>
            <prechkadj>"""
        tmp += proc.show()
        tmp += """</prechkadj>
        </surtsk>
        <surtsk>
            <precal>"""
        tmp += proc.show()
        tmp += """</precal>
        </surtsk>
        <surtsk>
            <calign>
                <alignproc>"""
        tmp += proc.show()
        tmp += """</alignproc>
            </calign>
        </surtsk>"""

        # TODO: Check to see if this is supposed to be -10 or -12
        if self.mil_std == "2D" and self.manual_type == ("-12", "-12&P", "-20", "-20P"):
            tmp += """<surtsk>
                <ammo.sur>"""
            tmp += proc.show()
            tmp += """</ammo.sur>
            </surtsk>"""

        tmp += """<surtsk>
            <other.surtsk>"""
        tmp += proc.show()
        tmp += """</other.surtsk>
        </surtsk>
    </surwp>"""
        file_name = f"{cfg.prefix_file:05d}-{wpno.upper()}-Service Upon Receipt.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.procedures_m.append(file_name)
        cfg.prefix_file += 10

    def maintwp(self, wpno, wp_title, proc_type) -> None:
        """Function to create Maintainer Procedures WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE maintwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE maintwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE maintwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<maintwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += """\t<wpidinfo>
        <maintlvl level="maintainer"/>\n"""
        if proc_type == "prepforuse":
            tmp += f"<title>{wp_title}</title>\n"
        elif proc_type == "prepship":
            tmp += f"<title>{wp_title}</title>\n"
        elif proc_type == "prepstore":
            tmp += f"<title>{wp_title}</title>\n"
        else:
            tmp += f"<title>{wp_title} <brk/> {proc_type.upper()}</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += "\t<maintsk>\n"
        tmp += f"\t\t<{proc_type}>\n"
        tmp += proc.show()
        tmp += f"\t\t</{proc_type}>\n"
        tmp += "\t</maintsk>\n"
        tmp += followon_maintsk.show()
        tmp += "</maintwp>"
        if (
            proc_type == "prepforuse"
            or proc_type == "prepship"
            or proc_type == "prepstore"
        ):
            file_name = f"{cfg.prefix_file:05d}-{wpno.upper()}-{wp_title}.xml"
            with open(
                f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
                "w",
                encoding="UTF-8",
            ) as _f:
                _f.write(tmp)
        else:
            file_name = f"{cfg.prefix_file:05d}-{wpno.upper()}-{wp_title}-{proc_type.upper()}.xml"
            with open(
                f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
                "w",
                encoding="UTF-8",
            ) as _f:
                _f.write(tmp)
        cfg.procedures_m.append(file_name)
        cfg.prefix_file += 10

    def gen_maintwp(self, wpno, wp_title) -> None:
        """Function to create Maintainer Procedures WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE gen.maintwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE gen.maintwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE gen.maintwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<gen.maintwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += """\t<wpidinfo>
        <maintlvl level="maintainer"/>\n"""
        tmp += f"<title>{wp_title}</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += proc.show()
        tmp += "</maintwp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno.upper()}-{wp_title}.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.procedures_m.append(file_name)
        cfg.prefix_file += 10

    def manu_items_introwp(self, wpno, wp_title) -> None:
        """Function to create Maintainer Procedures WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE manu_items_introwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE manu_items_introwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE manu_items_introwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<manu_items_introwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += """\t<wpidinfo>
        <maintlvl level="maintainer"/>\n"""
        tmp += f"<title>{wp_title}</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += """\t<intro>
        <para0>
            <title>ILLUSTRATED LIST OF MANUFACTURED ITEMS INTRODUCTION</title>
            <subpara1>
				<title>Scope</title>
				<para>This work package includes complete instructions for making items authorized to be manufactured or fabricated at the field level.</para>
			</subpara1>
			<subpara1>
				<title>How to Use the Index of Manufactured Items</title>
				<para>A part number index in alphanumeric order is provided for cross-referencing the part number of the item to be manufactured to the information that covers fabrication criteria.</para>
			</subpara1>
			<subpara1>
				<title>Explanation of Illustrations of Manufactured Items</title>
				<para>All instructions needed by maintenance personnel to manufacture the item shall be provided and shall include illustrations as required. Parts information can be found in <xref wpid=""/>. All bulk materials needed for manufacture of an item are listed by part number or specification number in a tabular list on the illustration.</para>
			</subpara1>
        </para0>"""
        tmp += "</manu_items_introwp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno.upper()}-{wp_title}.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.procedures_m.append(file_name)
        cfg.prefix_file += 10

    def manuwp(self, wpno, wp_title) -> None:
        """Function to create Manufacturing Procedures WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE manuwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE manuwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE manuwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<manuwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)
        tmp += """\t<wpidinfo>
        <maintlvl level="maintainer"/>\n"""
        tmp += f"<title>{wp_title}</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += """\t<manuitem>
        <title></title>
        <material-list-category>
            <title></title>
            <material-list id="">
                <name></name>
                <partno></partno>
                <cageno></cageno>
                <nsn>
                    <fsc></fsc>
                    <niin></niin>
                </nsn>
                <qty></qty>
                <itemref>
                    <xref wpid="" itemid=""/>
                </itemref>
            </material-list>
        </material-list-category>
        <proc>
			<title></title>
			<para></para>
		</proc>
    </manuitem>"""
        tmp += "</manuwp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno.upper()}-{wp_title}.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.procedures_m.append(file_name)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create Maintainer Procedures end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = "\t</maintenancecategory>\n" + "</mim>"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-MAINTAINER_MAINTENANCE_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
