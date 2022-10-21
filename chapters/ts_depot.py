"""TROUBLESHOOTING DEPOT PROCEDURES"""
import math
import cfg

class TSDepot:
    """Class to create various types of WP's included in Troubleshooting Depot Procedures of a TM."""
    def __init__(self, manual_type, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function that creates Depot Troubleshooting starting tags of TM."""
        cfg.prefix_file = (math.floor(cfg.prefix_file/1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
<tim chngno="0" revno="0" chap-toc="no">'''
        tmp += '\t<titlepg maintlvl="depot">\n'
        tmp += '\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')</name>\n'
        tmp += '\t</titlepg>\n'
        tmp += '<troubledmwrnmwrcategory>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-TS_DEPOT_START.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10
    
    def tsintrowp(self, wpno):
        """Function to create a Depot Troubleshooting Intro WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<tsintrowp chngno="0" wpno="{wpno}-' + self.sys_number+ '">\n'
        tmp += '''<wpidinfo>
        <maintlvl level="depot"/>
        <title>TROUBLESHOOTING INTRODUCTION</title>
    </wpidinfo>
    <geninfo>
        <title>GENERAL INFORMATION</title>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
    </geninfo>
    <para0>
        <title>GENERAL</title>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
    </para0>
    <para0>
        <title>TROUBLESHOOTING INDEX</title>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</para>
    </para0>
    <para0>
        <title/>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
    </para0>
</tsintrowp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-Troubleshooting-Introduction.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def tsindxwp(self, wpno):
        """Function to create a Depot Troubleshooting Index WP."""
        tmp = f'<tsindxwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="depot"/>\n'
        tmp += f'''\t\t<title>TROUBLESHOOTING INDEX</title>
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
            <title>Lorem Ipsum</title>
            <tsindx.symptom-entry>
                <malfunc label="symptom">Lorem Ipsum</malfunc>
                <action>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                </action>
            </tsindx.symptom-entry>
        </tsindx.symptom-category>
        <tsindx.symptom-category>
            <title>Lorem Ipsum</title>
            <tsindx.symptom-entry>
                <malfunc label="symptom">Lorem Ipsum</malfunc>
                <action>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                </action>
            </tsindx.symptom-entry>
            <tsindx.symptom-entry>
                <malfunc label="symptom">Lorem Ipsum</malfunc>
                <action>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                </action>
            </tsindx.symptom-entry>
        </tsindx.symptom-category>
    </tsindx.symptom>
</tsindxwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-Troubleshooting-Index.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pshopanalwp(self, wpno):
        """Function to create a Preshop Analysis Work Package."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<pshopanalwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '''<wpidinfo>
            <maintlvl level="depot"/>
            <title>Preshop Analysis</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '''<scope>
		<title>SCOPE</title>
		<para>The purpose of the preshop analysis operations is to determine, at the highest assembly level possible, the work required to return the Expeditionary TRICON Self Serve Laundry System (ETSSLS) to a condition specified under the Scope of this NMWR found in <xref posttext=", General Information" wpid="G00001-10-5419-215"/>. If inspection at the highest assembly level is precluded by missing, damaged, or defective components, inspection will proceed at the next lower level. The preshop analysis checklist will be used to record the results of the analysis and any required maintenance. The preshop analysis checklists are to be reproduced locally, as needed.</para>
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
						<para>The following preshop analysis checklist should be used to identify components, assemblies, or subassemblies that require maintenance. Refer to <xref tableid="T10002-10-5419-215-T0001"/> to complete the preshop analysis for ETSSLS. The preshop analysis checklist should be used with the guidance of <xref wpid="M10001-10-5419-215"/>.</para>
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
</pshopanalwp>\n'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-PreshopAnalysis.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def compchklistwp(self, wpno):
        """Function to create a Depot Component Checklist WP."""
        tmp = f'<compchklistwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="depot"/>\n'
        tmp += '''\t\t<title>COMPONENT CHECKLIST</title>
    </wpidinfo>\n'''
        tmp += isb()
        tmp += '''\t<intro>
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
</compchklistwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-ComponentChecklist.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def tswp(self, wpno, wp_title):
        """Function to create a Depot Troubleshooting WP."""
        tmp = f'<tswp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
            <maintlvl level="depot"/>
            <title>{wp_title}</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += f'''<tsproc>
        <faultproc>
            <title>{wp_title}</title>
            <note>
                <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
            </note>
            <symptom>Lorem ipsum dolor sit amet.</symptom>
            <malfunc label="malfunction">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</malfunc>
            <action>
                <step1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                </step1>
                <figure id="{wpno}-{self.sys_number}-F0001">
                    <title>Lorem Ipsum</title>
                    <graphic boardno="PLACEHOLDER"/>
                </figure>
                <step1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                </step1>
                <figure id="{wpno}-{self.sys_number}-F0002">
                    <title>Lorem Ipsum</title>
                    <graphic boardno="PLACEHOLDER"/>
                </figure>
                <step1>
                    <specpara>
                        <note>
                            <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
                        </note>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </specpara>
                    <step2>
                        <para>PASS: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step2>
                    <step2>
                        <para>FAIL: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step2>
                    <step2>
                        <para>FAIL: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>						
                    </step2>
                </step1>
                <figure id="{wpno}-{self.sys_number}-F0003">
                    <title>Lorem Ipsum</title>
                    <graphic boardno="PLACEHOLDER"/>
                </figure>
            </action>
        </faultproc>
    </tsproc>
</tswp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-Troubleshooting-{}.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self):
        """Function to create the Depot Troubleshooting end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        tmp = '\t</troubledmwrnmwrcategory>\n'
        tmp += '</tim>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-TS_DEPOT_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 1

def isb():
    """Function to create the Initial Setup Box."""
    isb_tmp = '''\t<initial_setup>
        <testeqp>
            <testeqp-setup-item>
                <name></name>
                <itemref>
                    <xref itemid="XX-XXXX-XXX" wpid="XX-XXXX-XXX"/>
                </itemref>
            </testeqp-setup-item>
        </testeqp>
        <tools>
            <tools-setup-item>
                <name></name>
                <itemref>
                    <xref itemid="XX-XXXX-XXX" wpid="XX-XXXX-XXX"/>
                </itemref>
            </tools-setup-item>
        </tools>
        <!--<spectools>
            <spectools-setup-item>
                <name></name>
            </spectools-setup-item>
        </spectools>-->
        <mtrlpart>
            <mtrlpart-setup-item>
                <name></name>
                <qty></qty>
                <itemref>
                    <xref itemid="XX-XXXX-XXX" wpid="XX-XXXX-XXX"/>
                </itemref>
            </mtrlpart-setup-item>
        </mtrlpart>
        <!--<mrp>
            <mrp-setup-item>
                <name></name>
                <qty></qty>
                <itemref>
                    <xref itemid="XX-XXXX-XXX" wpid="XX-XXXX-XXX"/>
                </itemref>
            </mrp-setup-item>
        </mrp>-->
        <persnreq>
            <persnreq-setup-item>
                <name></name>
            </persnreq-setup-item>
        </persnreq>
        <ref>
            <ref-setup-item>
                <xref wpid="XX-XXXX-XXX"/>
            </ref-setup-item>
        </ref>
        <eqpconds>
            <eqpconds-setup-item>
                <condition></condition>
                <itemref>
                    <xref wpid="XX-XXXX-XXX"/>
                </itemref>
            </eqpconds-setup-item>
        </eqpconds>
    </initial_setup>\n'''
    return isb_tmp
