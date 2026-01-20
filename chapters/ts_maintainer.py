"""TROUBLESHOOTING MAINTAINER PROCEDURES"""

import datetime
import math

import cfg
import views.isb as isb
import views.metadata as md


class TSMaintainer:
    """Class to create various types of WP's included in Troubleshooting Maintainer Procedures of a TM."""

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
        """Function that creates PMCS starting tags of TM."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<tim chngno="0" revno="0" chap-toc="no">"""
        tmp += '\t<titlepg maintlvl="maintainer">\n'
        tmp += f"\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n"
        tmp += "\t</titlepg>\n" + "\t<troublecategory>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-TS_MAINTAINER_START.xml",
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
        tmp += f'<tsindxwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += f"""\t\t<title>TROUBLESHOOTING INDEX</title>
    </wpidinfo>
    <geninfo>
        <title>GENERAL</title>
        <para>This chapter provides operator and maintainer maintenance information and includes troubleshooting maintenance procedures.</para>
        <para>
            <emphasis emph="bold">MAINTAINER TROUBLESHOOTING INDEX</emphasis>
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
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Troubleshooting Index.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.ts_maintainer.append(file_name)
        cfg.prefix_file += 10

    def tsintrowp(self, wpno) -> None:
        """Function to create a Troubleshooting Intro WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE tsintrowp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE tsintrowp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE tsintrowp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<tsintrowp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += """<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>TROUBLESHOOTING INTRODUCTION</title>
        </wpidinfo>
        <geninfo>
            <title>GENERAL INFORMATION</title>
            <para></para>
        </geninfo>
        <para0>
            <title>GENERAL</title>
            <para></para>
            <para></para>
        </para0>
        <para0>
            <title>TROUBLESHOOTING INDEX</title>
            <para></para>
            <para></para>
        </para0>
        <para0>
            <title/>
            <para></para>
        </para0>
    </tsintrowp>"""
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Troubleshooting Introduction.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.ts_maintainer.append(file_name)
        cfg.prefix_file += 10

    def tswp(self, wpno, wp_title) -> None:
        """Function to create a Maintainer Troubleshooting WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += (
                f'<!DOCTYPE tswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
            )
        elif self.mil_std == "2D":
            tmp += (
                f'<!DOCTYPE tswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
            )
        elif self.mil_std == "E":
            tmp += (
                f'<!DOCTYPE tswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
            )
        tmp += f'<tswp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += f"""\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}</title>
        </wpidinfo>\n"""
        tmp += isb.show()
        tmp += """<tsproc>
            <faultproc>
                <title></title>
                <note>
                    <trim.para></trim.para>
                </note>
                <symptom></symptom>
                <malfunc label="malfunction"></malfunc>
                <action>
                    <step1>
                        <para></para>
                    </step1>
                    <figure id="">
                        <title></title>
                        <graphic boardno=""/>
                    </figure>
                    <step1>
                        <para></para>
                    </step1>
                    <figure id="">
                        <title></title>
                        <graphic boardno=""/>
                    </figure>
                    <step1>
                        <specpara>
                            <note>
                                <trim.para></trim.para>
                            </note>
                            <para></para>
                        </specpara>
                        <step2>
                            <para>PASS: </para>
                        </step2>
                        <step2>
                            <para>FAIL: </para>
                        </step2>
                        <step2>
                            <para>FAIL: </para>
                        </step2>
                    </step1>
                    <figure id="">
                        <title></title>
                        <graphic boardno=""/>
                    </figure>
                </action>
            </faultproc>
        </tsproc>
    </tswp>"""
        file_name = f"{cfg.prefix_file:05d}-{wpno}-{wp_title}.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.ts_maintainer.append(file_name)
        cfg.prefix_file += 10

    def end(self):
        """Function to create the Maintainer Troubleshooting end tags"""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = "\t</troublecategory>\n"
        tmp += "</tim>"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-TS_MAINTAINER_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
