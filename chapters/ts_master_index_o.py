"""TROUBLESHOOTING MASTER INDEX"""

import datetime
import math

import cfg
import views.metadata as md


class TSMasterIndex:
    """Class to create various types of WP's included in the TS Master Index of a TM."""

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
        if (
            self.manual_type == "-10"
            or self.manual_type == "-12&P"
            or self.manual_type == "-13&P"
        ):
            level = "operator"
        elif self.manual_type == "NMWR":
            level = "depot"
        else:
            level = "maintainer"
        return level

    def start(self) -> None:
        """Function that creates TS Master Index WP starting tags of TM."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<tim chngno="0" revno="0" chap-toc="no">\n"""
        tmp += f'\t<titlepg maintlvl="{self.maintenance_level()}">\n'
        tmp += f"\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n"
        tmp += "\t</titlepg>\n"
        tmp += "\t<masterindexcategory>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-TS_MASTER_INDEX_START.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def tsindxwp(self, wpno) -> None:
        """Function to create a Troubleshooting Index WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE tsindxwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE tsindxwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE tsindxwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp = f'<tsindxwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += f"""\t\t<title>TROUBLESHOOTING INDEX</title>
    </wpidinfo>
    <geninfo>
        <title>GENERAL</title>
        <para>This chapter provides operator and maintainer maintenance information and includes troubleshooting maintenance procedures.</para>
        <para>
            <emphasis emph="bold">TROUBLESHOOTING INDEX</emphasis>
        </para>
        <para>Troubleshooting index lists common malfunctions that may occur during {self.sys_acronym} shelter inspection and operation. Find malfunction to be eliminated and go to indicated troubleshooting work package that follows. Index cannot list all malfunctions that may occur, all tests or inspections needed to find fault, nor all actions required to correct fault. If existing malfunction is not listed, or cannot be corrected through this troubleshooting index, notify next higher level of maintenance.</para>
    </geninfo>
    <tsindx.symptom>
        <title>Troubleshooting Index</title>
        <tsindx.symptom-category>
            <title></title>
            <tsindx.symptom-entry>
                <malfunc label="symptom"></malfunc>
                <action>
                    <para></para>
                </action>
            </tsindx.symptom-entry>
        </tsindx.symptom-category>
        <tsindx.symptom-category>
            <title></title>
            <tsindx.symptom-entry>
                <malfunc label="symptom"></malfunc>
                <action>
                    <para></para>
                </action>
            </tsindx.symptom-entry>
            <tsindx.symptom-entry>
                <malfunc label="symptom"></malfunc>
                <action>
                    <para></para>
                </action>
            </tsindx.symptom-entry>
        </tsindx.symptom-category>
    </tsindx.symptom>
</tsindxwp>"""
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Troubleshooting Master Index.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.ts_master_index_o.append(file_name)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create TS Master Index WP end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = "\t</masterindexcategory>\n" + "</tim>"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-TS_MASTER_INDEX_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
