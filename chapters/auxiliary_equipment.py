"""AUXILIARY EQUIPMENT MAINTENANCE INSTRUCTIONS"""

import datetime
import math

import cfg
import views.followon_maintsk as followon_maintsk
import views.isb as isb
import views.metadata as md
import views.proc as proc


class AuxiliaryEquipment:
    """Class to create various types of WP's included in the Auxiliary Equipment
    Maintenance Instructions chapter of a TM.
    """

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
        """Function that creates the Auxiliary Equipment Maintenance
        Instructions chapter header of TM.
        """
        # cfg.prefix_file = math.floor(cfg.prefix_file / 1000) * 1000
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<mim revno="0" chngno="0" chap-toc="no">\n"""
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
        tmp += "\t\t</titlepg>\n"
        tmp += "\t\t<auxiliarycategory>\n"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-AUXILIARY_EQUPMENT_START.xml".format(cfg.prefix_file),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def auxeqpwp(self, wpno, wp_title, proc_type) -> None:
        """Function to create an Auxiliary Equipment Maintenance Instructions WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE auxeqpwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE auxeqpwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE auxeqpwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'

        tmp += f'<auxeqpwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("auxeqpwp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += f"\t\t<title>{wp_title} <brk/> {proc_type.upper()}</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += "\t<maintsk>\n"
        tmp += f"\t\t<{proc_type}>\n"
        tmp += proc.show()
        tmp += f"\t\t</{proc_type}>\n"
        tmp += "\t</maintsk>\n"
        tmp += followon_maintsk.show()
        tmp += "</auxeqpwp>\n"

        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-{wp_title} {proc_type.upper()}.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def manu_items_introwp(self, wpno, wp_title) -> None:
        """Function to create the Illustrated List of Manufactured Items WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE manu_items_introwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE manu_items_introwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE manu_items_introwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += (
            f'<manu_items_introwp chngno="0" wpno="{wpno}-'
            + self.tmno
            + '" security="cui">\n'
        )

        # WP.METADATA Section
        tmp += md.show("manu_items_introwp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += """<title>ILLUSTRATED LIST OF MANUFACTURED ITEMS INTRODUCTION</title>
    </wpidinfo>
    <intro>
        <para0>
            <title>SCOPE</title>
            <para>This work package includes complete instructions for making items authorized to be manufactured or fabricated at the (enter applicable maintenance level).</para>
            <subpara1>
                <title>How to Use the Index of Manufactured Items</title>
                <para>A part number index in alphanumeric order is provided for cross-referencing the part number of the item to be manufactured to the information that covers fabrication criteria.</para>
            </subpara1>
            <subpara1>
                <title>Explanation of the Illustrations of Manufactured Items</title>
                <para>All instructions needed by maintenance personnel to manufacture the item shall be provided and shall include illustrations as required. (When applicable, a reference to the associated parts information TM or parts information work package shall be entered here.) All bulk materials needed for manufacture of an item are listed by part number or specification number in a tabular list on the illustration.</para>
            </subpara1>
        </para0>
    </intro>
    <manuindx>
        <title>INDEX OF MANUFACTURED ITEMS</title>
        <partdesc>
            <partno></partno>
            <cageno></cageno>
            <dwgno></dwgno>
        </partdesc>
        <partdesc>
            <partno></partno>
            <cageno></cageno>
            <dwgno></dwgno>
        </partdesc>
        <partdesc>
            <partno></partno>
            <cageno></cageno>
            <dwgno></dwgno>
        </partdesc>
        <partdesc>
            <partno></partno>
            <cageno></cageno>
            <dwgno></dwgno>
        </partdesc>
        <partdesc>
            <partno></partno>
            <cageno></cageno>
            <dwgno></dwgno>
        </partdesc>
    </manuindx>
</manu_items_introwp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-{wp_title}.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def manuwp(self, wpno, wp_title) -> None:
        """Function to create the Manufacturing Procedures WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE manuwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE manuwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE manuwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<manuwp chngno="0" wpno="{wpno}-' + self.tmno + '" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("manuwp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += """<title>MANUFACTURING PROCEDURES</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += """\t<manuitem>
    </manuitem>
</manuwp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-{wp_title}.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def torquewp(self, wpno, wp_title) -> None:
        """Function to create the Torque Limits WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE torquewp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE torquewp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE torquewp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<torquewp chngno="0" wpno="{wpno}-' + self.tmno + '" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("torquewp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += """<title>TORQUE LIMITS</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += "\t<torqueval>\n"
        tmp += "\t\t<title>TORQUE LIMITS</title>\n"
        tmp += "\t\t<para></para>\n"
        tmp += "\t</torqueval>\n"
        tmp += "</torquewp>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-{wp_title}.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def wiringwp(self, wpno, wp_title) -> None:
        """Function to create the Wiring Diagrams WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE wiringwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE wiringwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE wiringwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<wiringwp chngno="0" wpno="{wpno}-' + self.tmno + '" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("wiringwp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += """<title>WIRING DIAGRAMS</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += "\t<intro>\n"
        tmp += "\t\t<para0></para0>\n"
        tmp += "\t</intro>\n"
        tmp += "\t<abbrev>\n"
        tmp += "\t\t<title></title>\n"
        tmp += '\t\t<figure id=""></figure>\n'
        tmp += "\t\t<para0></para0>\n"
        tmp += "\t</abbrev>\n"
        tmp += "\t<component_desc>\n"
        tmp += "\t\t<para0></para0>\n"
        tmp += "\t</component_desc>\n"
        tmp += "\t<wireid>\n"
        tmp += "\t\t<title></title>\n"
        tmp += '\t\t<figure id=""></figure>\n'
        tmp += "\t\t<para0></para0>\n"
        tmp += "\t</wireid>\n"
        tmp += "\t<wire_color>\n"
        tmp += "\t\t<para0></para0>\n"
        tmp += "\t</wire_color>\n"
        tmp += "\t<wiringdiag>\n"
        tmp += "\t\t<title></title>\n"
        tmp += '\t\t<figure id=""></figure>\n'
        tmp += "\t\t<para0></para0>\n"
        tmp += "\t</wiringdiag>\n"
        tmp += "</wiringwp>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-{wp_title}.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create the Auxiliary Equipment Maintenance
        Instructions chapter end tags.
        """
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = "\t</auxiliarycategory>\n"
        tmp += "</mim>"

        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-AUXILIARY_EQUIPMENT_END.xml".format(cfg.prefix_file),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
