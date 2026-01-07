"""TROUBLESHOOTING OPERATOR PROCEDURES"""

import datetime
import math

import cfg
import views.isb as isb
import views.metadata as md


class TSOperator:
    """Class to create various types of WP's included in Troubleshooting Procedures of a TM."""

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
        """Function that creates Troubleshooting Procedures starting tags of TM."""
        # cfg.prefix_file = math.floor(cfg.prefix_file / 1000) * 1000
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<tim chngno="0" revno="0" chap-toc="no">"""
        tmp += '\t<titlepg maintlvl="operator">\n'
        tmp += f"\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n"
        tmp += "\t</titlepg>\n" + "\t<troublecategory>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-TS_OPERATOR_START.xml",
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
        tmp += md.show("tsindxwp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="operator"/>\n'
        tmp += f"""\t\t<title>TROUBLESHOOTING INDEX</title>
    </wpidinfo>
    <geninfo>
        <title>GENERAL</title>
        <para>This chapter provides operator and maintainer maintenance information and includes troubleshooting maintenance procedures.</para>
        <para>
            <emphasis emph="bold">OPERATOR TROUBLESHOOTING INDEX</emphasis>
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
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-Troubleshooting Index.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
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
        tmp += md.show("tsintrowp", self.tmno)

        tmp += f"""\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>TROUBLESHOOTING INTRODUCTION</title>
    </wpidinfo>
    <geninfo>
		<title>GENERAL INFORMATION</title>
		<para>This work package describes the operator testing and troubleshooting process used to perform troubleshooting on the {self.sys_name} ({self.sys_acronym}) and includes information on the methods used to perform troubleshooting.</para>
	</geninfo>
	<para0>
		<title>GENERAL</title>
		<para>The troubleshooting procedures contained in this chapter list the symptoms, malfunctions, and corrective actions required to return the {self.sys_acronym} to normal operation. Perform the steps in the order they appear in the work packages.</para>
		<para>DO NOT START THE TASK UNTIL: The task is understood. The personnel, materials, replacement parts, and/or testing equipment for the task are prepared.</para>
		<para>All {self.sys_acronym} fault conditions can be found in the troubleshooting index work package (<xref wpid="TXXXXX-XX-XXXX-XXX"/>). The reader will be directed to the appropriate work package to begin the troubleshooting process. The fault condition will be listed in the work package as a symptom with one or more possible malfunctions. Each malfunction will have one or more corrective actions to be performed. After each corrective action is completed, attempt to operate the equipment to see if the fault is corrected.</para>
	</para0>
	<para0>
		<title>TROUBLESHOOTING INDEX</title>
		<para>The troubleshooting index (<xref wpid="TXXXXX-XX-XXXX-XXX"/>) is listed by subsystem in alphabetical order. Each symptom under the applicable subsystem will be listed in alphabetical order. Symptoms in the indicated work packages will also appear in alphabetical order.</para>
		<para>The troubleshooting index lists common malfunctions that may occur during {self.sys_acronym} inspection and operation. Find the malfunction to be addressed and go to the indicated troubleshooting work package. The troubleshooting index cannot list all malfunctions that may occur, all tests or inspections needed to find the fault, nor all actions required to correct the fault. If the existing malfunction is not listed, or cannot be corrected through this troubleshooting index, notify your supervisor.</para>
	</para0>
	<para0>
		<title/>
		<para>An example of the troubleshooting process is shown below. The symptom describes the problem being experienced. The malfunction is the cause of the symptom starting with the most likely cause or most easily remedied. Further malfunctions will describe alternate fault conditions. The corrective action shows the steps required to correct each malfunction.</para>
	</para0>
	<para0>
		<title>SYMPTOM</title>
		<para>No power to TRICON shelter.</para>
	</para0>
	<para0>
		<title>MALFUNCTION</title>
		<para>Power cable unplugged.</para>
	</para0>
	<para0>
		<title>CORRECTIVE ACTION</title>
		<para>STEP 1. Verify power cable is connected securely to power input receptacle.</para>
		<para>STEP 2. Verify power cable is securely connected at the source and the source is energized.</para>
		<para>STEP 3. Reset external power control circuit breaker by setting to OFF, then back to ON.</para>
	</para0>
</tsintrowp>\n"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-Troubleshooting Introduction.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def tswp(self, wpno, wp_title) -> None:
        """Function to create an Operator Troubleshooting WP."""
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
        tmp += md.show("tswp", self.tmno)

        tmp += f"""\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>{wp_title}</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += f"""\t<tsproc>
        <faultproc>
            <title>{wp_title}</title>
            <note>
                <trim.para></trim.para>
            </note>
            <symptom></symptom>
            <malfunc label="malfunction"></malfunc>
            <action>
                <step1>
                    <para></para>
                </step1>
                <figure id="{wpno}-{self.tmno}-F0001">
                    <title></title>
                    <graphic boardno="PLACEHOLDER"/>
                </figure>
                <step1>
                    <para></para>
                </step1>
                <figure id="{wpno}-{self.tmno}-F0002">
                    <title></title>
                    <graphic boardno="PLACEHOLDER"/>
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
                <figure id="{wpno}-{self.tmno}-F0003">
                    <title></title>
                    <graphic boardno="PLACEHOLDER"/>
                </figure>
            </action>
        </faultproc>
    </tsproc>
</tswp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno} {wp_title}.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create the Operator Troubleshooting Procedures end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = "\t</troublecategory>\n" + "</tim>"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-TS_OPERATOR_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
