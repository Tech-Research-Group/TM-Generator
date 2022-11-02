"""TROUBLESHOOTING OPERATOR PROCEDURES"""
import math
import cfg
import views.isb as isb

class TSOperator:
    """Class to create various types of WP's included in Troubleshooting Procedures of a TM."""
    def __init__(self, manual_type, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function that creates Troubleshooting Procedures starting tags of TM."""
        cfg.prefix_file = (math.floor(cfg.prefix_file/1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
    <tim chngno="0" revno="0" chap-toc="no">'''
        tmp += '\t<titlepg maintlvl="operator">\n'
        tmp += f'\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n'
        tmp += '\t</titlepg>\n' + '\t<troublecategory>\n'
        with open(f"{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-TS_OPERATOR_START.txt", 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10
        
    def tsintrowp(self):
        """Function to create a Troubleshooting Intro WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<tsintrowp chngno="0" wpno="T00001-{self.sys_number}">\n'
        tmp += f'''\t<wpidinfo>
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
</tsintrowp>\n'''
        with open(f"{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-T00001-Troubleshooting-Introduction.txt", 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def tswp(self, wpno, wp_title):
        """Function to create an Operator Troubleshooting WP."""
        tmp = f'<tswp chngno="0" wpno="{wpno}-{self.sys_number}">\n'
        tmp += f'''\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>{wp_title}</title>
    </wpidinfo>\n'''
        tmp += isb.show()
        tmp += f'''\t<tsproc>
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
        with open(f"{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-{wpno}-Troubleshooting-{wp_title}.txt", 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self):
        """Function to create the Operator Troubleshooting Procedures end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = '\t</troublecategory>\n' + '</tim>'
        with open(f"{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-TS_OPERATOR_END.txt", 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
