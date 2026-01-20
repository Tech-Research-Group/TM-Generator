"""OPERATOR PROCEDURES"""

import datetime
import math

import cfg
import views.followon_maintsk as followon_maintsk
import views.isb as isb
import views.metadata as md
import views.proc as proc


class OperatorProcedures:
    """Class to create various types of WP's included in Operator Procedures of a TM."""

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
        """Function to create Operator Procedures start tags."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<mim chngno="0" revno="0" chap-toc="no">\n"""
        tmp += '\t<titlepg maintlvl="operator">\n'
        tmp += f"\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n"
        tmp += "\t</titlepg>\n" + "\t<maintenancecategory>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-OPERATOR_MAINTENANCE_START.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def maintwp(self, wpno, wp_title, proc_type) -> None:
        """Function to create Operator Procedures WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
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
        <maintlvl level="operator"/>\n"""
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
        cfg.procedures_o.append(file_name)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create Operator Procedures end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = "\t</maintenancecategory>\n" + "</mim>"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-OPERATOR_MAINTENANCE_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
