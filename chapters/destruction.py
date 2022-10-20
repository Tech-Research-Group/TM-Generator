"""DESTRUCTION OF EQUIPMENT TO PREVENT ENEMY USE"""
import cfg
import math

class Destruction:
    """Class to create various types of WP's included in Desctruction section of a TM."""
    def __init__(self, manual_type, milstd, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.milstd = milstd
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function to create Desctruction section start tags."""
        cfg.prefix_file = (math.floor(cfg.prefix_file/1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
    <dim chngno="0" revno="0" chap-toc="no">\n'''
        if self.manual_type == '-10' or self.manual_type == '-12&P' or self.manual_type == '-13&P':
            tmp += '<titlepg maintlvl="operator">\n'
        elif self.manual_type == '-23&P':
            tmp += '<titlepg maintlvl="maintainer">\n'
        tmp += '\t\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')' + '</name>\n'
        tmp += '</titlepg>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-DESTRUCTION_START.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def destruct_introwp(self):
        """Function to create the Destruction section intro."""
        tmp = '<destruct-introwp chngno="0" wpno="D00001-' + self.sys_number + '">'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-12&P' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += f'''\t\t<title>INTRODUCTION</title>
    </wpidinfo>
    <authorize_to_destroy>
        <title>AUTHORITY TO DESTROY</title>
        <para>Authorization. Only division or higher commanders have authority to order destruction of equipment. They may however, delegate this authority to subordinate commanders when situation demands it.</para>
    </authorize_to_destroy>
    <?Pub _newline?>
    <report_destruct>
        <title>Reporting Destruction</title>
        <para>Report any destruction activity through command channels.</para>
    </report_destruct>
    <?Pub _newline?>
    <general_destruct_info>
        <para0>
            <title>General Destruction Information</title>
            <para>{self.sys_name} ({self.sys_acronym}) does not contain classified equipment. Refer to Procedures for "Destruction of Equipment to Prevent Enemy Use" <extref docno="TM 750-244-3"/> for additional guidance.</para>
            <para>In the situation where {self.sys_acronym} must be destroyed, it can be destroyed via burning, explosives, burying, or any other means that would render it unusable for enemy.</para>
        </para0>
    </general_destruct_info>\n'''
        if self.milstd != '2B':
            tmp += '''<?Pub _newline?>
    <degree_of_destruct>
        <title>Degree of Destruction</title>
        <para>
            <randlist>
                <item>Methods of Destruction. Choose methods of destruction which will cause such damage that it will be impossible to restore equipment to a usable condition within combat zone.</item>
                <item>Classified Equipment. Classified equipment must be destroyed to such a degree as to prevent duplication by, or revealing means of operation or function to enemy.</item>
                <item>Associated Classified Documents. Any classified documents, notes, instructions, or other written material pertaining to function, operation, maintenance, or employment, including drawings or parts lists, must be destroyed in a manner to render them useless to enemy.</item></randlist>
        </para>
    </degree_of_destruct>\n'''
        tmp += '</destruct-introwp>'
    
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-D00001-Destruction-Introduction.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)   
        cfg.prefix_file += 10

    def destruct_materialwp(self, wpno, wp_title):
        """Function to create a Destruction WP."""
        tmp = f'<destruct-materialwp chngno="0" wpno="{wpno}-' + self.sys_number + '">'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-12&P' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += f'''\t\t<title>{wp_title}</title>
    </wpidinfo>'''
        tmp += isb()
        tmp += '''\t<proc>
        <title>Specific Destruction Procedures</title>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
    </proc>
</destruct-materialwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-{}.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self):
        """Function to create the Destruction section end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        tmp = '</dim>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-DESTRUCTION_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
        
def isb():
    """Function to create the Initial Setup Box."""
    isb_tmp = '''\n<initial_setup>
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
    