"""TROUBLESHOOTING MAINTAINER PROCEDURES"""
import cfg
import math

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
        cfg.prefix_file = (math.floor(cfg.prefix_file/1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
    <tim chngno="0" revno="0" chap-toc="no">'''
        tmp += '\t<titlepg maintlvl="maintainer">\n'
        tmp += '\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')</name>\n'
        tmp += '\t</titlepg>\n'
        tmp += '<troublecategory>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-TS_MAINTAINER_START.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def tsintrowp(self):
        """Function to create a Troubleshooting Intro WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += '<tsintrowp chngno="0" wpno="T00101-' + self.sys_number+ '">\n'
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
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-T00101-Troubleshooting-Introduction.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def tswp(self, wpno, wp_title):
        """Function to create a Maintainer Troubleshooting WP."""
        tmp = f'<tswp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}</title>
        </wpidinfo>\n'''
        tmp += isb()
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
