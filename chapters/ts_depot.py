"""TROUBLESHOOTING DEPOT PROCEDURES"""

import datetime
import math

import cfg
import views.isb as isb
import views.metadata as md


class TSDepot:
    """Class to create various types of WP's included in Troubleshooting Depot Procedures of a TM."""

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
        """Function that creates Depot Troubleshooting starting tags of TM."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<tim chngno="0" revno="0" chap-toc="no">"""
        tmp += '\t<titlepg maintlvl="depot">\n'
        tmp += f"\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n"
        tmp += "\t</titlepg>\n" + "\t<troubledmwrnmwrcategory>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-TS_DEPOT_START.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def tsintrowp(self, wpno) -> None:
        """Function to create a Depot Troubleshooting Intro WP."""
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
        <maintlvl level="depot"/>
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
        cfg.ts_depot.append(file_name)
        cfg.prefix_file += 10

    def tsindxwp(self, wpno) -> None:
        """Function to create a Depot Troubleshooting Index WP."""
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

        tmp += "\t<wpidinfo>\n" + '\t\t<maintlvl level="depot"/>\n'
        tmp += f"""\t\t<title>TROUBLESHOOTING INDEX</title>
    </wpidinfo>
    <geninfo>
        <title>GENERAL</title>
        <para>This chapter provides depot maintenance information and includes troubleshooting maintenance procedures.</para>
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
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Troubleshooting Index.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.ts_depot.append(file_name)
        cfg.prefix_file += 10

    def pshopanalwp(self, wpno) -> None:
        """Function to create a Preshop Analysis Work Package."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE pshopanalwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE pshopanalwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE pshopanalwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<pshopanalwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += """<wpidinfo>
            <maintlvl level="depot"/>
            <title>Preshop Analysis</title>
        </wpidinfo>\n"""
        tmp += isb.show()
        tmp += """<scope>
		<title>SCOPE</title>
		<para>The purpose of the preshop analysis operations is to determine, at the highest assembly level possible, the work required to return the INSERT TM NAME HERE to a condition specified under the Scope of this NMWR found in <xref posttext=", General Information" wpid="G00001-10-5419-215"/>. If inspection at the highest assembly level is precluded by missing, damaged, or defective components, inspection will proceed at the next lower level. The preshop analysis checklist will be used to record the results of the analysis and any required maintenance. The preshop analysis checklists are to be reproduced locally, as needed.</para>
	</scope>
	<proc>
		<title>Unpacking and Special Handling</title>
		<step1>
			<para></para>
		</step1>
		<step1>
			<para></para>
		</step1>
	</proc>
	<proc>
		<title>Checking Attached Documents</title>
		<para></para>
	</proc>
	<proc>
		<title>External Inspection</title>
		<step1>
			<para></para>
		</step1>
		<step1>
			<para></para>
		</step1>
	</proc>
	<proc>
		<title>Cleaning and Preservation</title>
		<para>If cleaning is required to perform the preshop analysis, clean only as necessary to make the analysis.</para>
	</proc>
	<pshopanal>
		<chklist>
			<coverpage>
				<partno/>
				<serialno/>
				<nsn>
					<fsc/>
					<niin/>
				</nsn>
				<modreq/>
				<reason/>
				<secitem/>
				<revtag/>
				<revform/>
				<name/>
				<sig/>
				<date/>
			</coverpage>
			<intro>
				<para0-alt>
					<para0>
						<title>PRESHOP ANALYSIS</title>
						<para> </para>
					</para0>
					<para0>
						<title>Introduction</title>
						<para>The following preshop analysis checklist should be used to identify components, assemblies, or subassemblies that require maintenance. Refer to <xref tableid="T10002-10-5419-215-T0001"/> to complete the preshop analysis for INSERT TM NAME HERE. The preshop analysis checklist should be used with the guidance of <xref wpid="M10001-10-5419-215"/>.</para>
					</para0>
					<para0>
						<title>Preshop Analysis Checklist</title>
						<para>The purpose of each column in the preshop analysis checklist is as follows:<randlist bullet="yes">
								<item>Inspection Point: Indicates the component to be inspected.</item>
								<item>Inspection: Provides inspection procedure.</item>
								<item>Condition: Describes the desired condition that maintenance personnel should look for.</item>
								<item>Corrective Action: Informs maintenance personnel where identified problems can be corrected within the NMWR or supporting documents.</item>
								<item>Remarks: Provides space for maintenance personnel to record results of inspections.</item>
								<item>Date Checked: Provides space for maintenance personnel to record the date of completion of each inspection/test.</item>
								<item>Checked By: Provides space for maintenance personnel to sign upon completion of each inspection/test.</item>
							</randlist>
						</para>
					</para0>
				</para0-alt>
			</intro>
			<pshopchk.tab>
				<table id="T10002-10-5419-215-T0001">
					<title>Preshop Analysis Checklist</title>
					<tgroup cols="7">
						<colspec colname="col1" colwidth="0.8*"/>
						<colspec colname="col2" colwidth="0.8*"/>
						<colspec colname="col3" colwidth="1.5*"/>
						<colspec colname="col4" colwidth="0.8*"/>
						<colspec colname="col5" colwidth="0.8*"/>
						<colspec colname="col6" colwidth="0.65*"/>
						<colspec colname="col7" colwidth="0.65*"/>
						<thead>
							<row>
								<entry align="center" valign="bottom">Inspection Point</entry>
								<entry align="center" valign="bottom">Inspection</entry>
								<entry align="center" valign="bottom">Condition</entry>
								<entry align="center" valign="bottom">Corrective Action</entry>
								<entry align="center" valign="bottom">Remarks</entry>
								<entry align="center" valign="bottom">Date Checked</entry>
								<entry align="center" valign="bottom">Checked By</entry>
							</row>
						</thead>
						<tbody>
							<row>
								<entry>I/O Pan Exterior </entry>
								<entry align="center" valign="bottom"/>
								<entry align="center" valign="bottom"/>
								<entry align="center" valign="bottom"/>
								<entry align="center" valign="bottom"/>
								<entry align="center" valign="bottom"/>
								<entry align="center" valign="bottom"/>
							</row>
							<row>
								<entry>I/O Pan Weldment</entry>
								<entry>Inspect I/O pan weldment for damage, corrosion, presence, and serviceability.</entry>
								<entry>Should allow for hose to be connected. </entry>
								<entry>If damaged, corroded, missing, or malfunctioning, replace IAW <extref docno="TM 10-5419-215-23&amp;P"/>.</entry>
								<entry/>
								<entry/>
								<entry/>
							</row>
							<row>
								<entry>Cold Water Inlet</entry>
								<entry>Inspect cold water inlet for damage, corrosion, presence, and serviceability. </entry>
								<entry>Should allow for hose to be connected. </entry>
								<entry>If damaged, corroded, missing, or malfunctioning, replace IAW <extref docno="TM 10-5419-215-23&amp;P"/>.</entry>
								<entry/>
								<entry/>
								<entry/>
							</row>
                        </tbody>
					</tgroup>
				</table>
			</pshopchk.tab>
		</chklist>
	</pshopanal>
</pshopanalwp>\n"""
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Preshop Analysis.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.ts_depot.append(file_name)
        cfg.prefix_file += 10

    def compchklistwp(self, wpno) -> None:
        """Function to create a Depot Component Checklist WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE compchklistwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE compchklistwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE compchklistwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<compchklistwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="depot"/>\n'
        tmp += """\t\t<title>COMPONENT CHECKLIST</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += """\t<intro>
		<para0>
			<title>Scope</title>
			<para>This work package includes a list which is to be copied for each item received for a preshop analysis. After copying one list for each item, the information required must be completed on the checklist prior to the preshop analysis.</para>
		</para0>
	</intro>
	<compchklist>
		<name/>
		<serialno/>
		<daterec/>
		<recfrom/>
		<compname/>
		<nsn>
			<fsc/>
			<niin/>
		</nsn>
		<partno/>
		<cageno/>
		<qty/>
		<qtyrec/>
		<damage/>
	</compchklist>
</compchklistwp>"""
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Depot Component Checklist.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.ts_depot.append(file_name)
        cfg.prefix_file += 10

    def tswp(self, wpno, wp_title) -> None:
        """Function to create a Depot Troubleshooting WP."""
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
            <maintlvl level="depot"/>
            <title>{wp_title}</title>
        </wpidinfo>\n"""
        tmp += isb.show()
        tmp += f"""<tsproc>
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
        file_name = f"{cfg.prefix_file:05d}-{wpno} {wp_title}.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.ts_depot.append(file_name)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create the Depot Troubleshooting end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = "\t</troubledmwrnmwrcategory>\n" + "</tim>"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-TS_DEPOT_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
