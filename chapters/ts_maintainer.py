"""TROUBLESHOOTING MAINTAINER PROCEDURES"""
import math
import cfg
import views.isb as isb

class TSMaintainer:
    """Class to create various types of WP's included in Troubleshooting Maintainer Procedures of a TM."""

    def __init__(self, manual_type, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function that creates PMCS starting tags of TM."""
        cfg.prefix_file = (math.floor(cfg.prefix_file / 1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
<tim chngno="0" revno="0" chap-toc="no">'''
        tmp += '\t<titlepg maintlvl="maintainer">\n'
        tmp += f'\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n'
        tmp += '\t</titlepg>\n' + '<troublecategory>\n'
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-TS_MAINTAINER_START.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def tsindxwp(self, wpno):
        """Function to create a Troubleshooting Index WP."""
        tmp = f'<tsindxwp chngno="0" wpno="{wpno}-{self.sys_number}">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += f'''\t\t<title>TROUBLESHOOTING INDEX</title>
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
        with open(f"{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-{wpno}-Troubleshooting-Index.txt", 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def tsintrowp(self, wpno):
        """Function to create a Troubleshooting Intro WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<tsintrowp chngno="0" wpno="{wpno}-self.sys_number">\n'
        tmp += '''<wpidinfo>
            <maintlvl level="maintainer"/>
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
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-{wpno}-Troubleshooting-Introduction.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def tswp(self, wpno, wp_title):
        """Function to create a Maintainer Troubleshooting WP."""
        tmp = f'<tswp chngno="0" wpno="{wpno}-{self.sys_number}">\n'
        tmp += f'''<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}</title>
        </wpidinfo>\n'''
        tmp += isb.show()
        tmp += '''<tsproc>
            <faultproc>
                <title>LOREM IPSUM</title>
                <note>
                    <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
                </note>
                <symptom>Lorem ipsum dolor sit amet.</symptom>
                <malfunc label="malfunction">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</malfunc>
                <action>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>
                    <figure id="T00101-XX-XXXX-XXX-F0001">
                        <title>Lorem Ipsum</title>
                        <graphic boardno="PLACEHOLDER"/>
                    </figure>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>
                    <figure id="T00101-XX-XXXX-XXX-F0002">
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
                    <figure id="T00101-XX-XXXX-XXX-F0003">
                        <title>Lorem Ipsum</title>
                        <graphic boardno="PLACEHOLDER"/>
                    </figure>
                </action>
            </faultproc>
        </tsproc>
    </tswp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                  ' WIP/{:05d}-{}-{}.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self):
        """ Function to create the Maintainer Troubleshooting end tags """
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        tmp = '\t</troublecategory>\n'
        tmp += '</tim>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                  ' WIP/{:05d}-TS_MAINTAINER_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
