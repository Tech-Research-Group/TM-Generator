"""MAINTAINER PROCEDURES"""
import math
import cfg
import views.followon_maintsk as followon_maintsk
import views.isb as isb
import views.proc as proc

class MaintainerProcedures:
    """Class to create various types of WP's included in Maintainer Procedures of a TM."""
    def __init__(self, manual_type, mil_std, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.mil_std = mil_std
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function to create Maintainer Procedures start tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
<mim chngno="0" revno="0" chap-toc="no">\n'''
        tmp += '\t<titlepg maintlvl="maintainer">\n'
        tmp += f'\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n'
        tmp += '\t</titlepg>\n' + '\t<maintenancecategory>'
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-MAINTAINER_START.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def surwp(self, wpno):
        """Function to create Service Upon Receipt WP."""
        tmp = '''<!-- SERVICE UPON RECEIPT -->
    <!-- 
        PROHIBITED for -10      (MIL-STD 2B)
        OPTIONAL   for -10      (MIL-STD 2C/2D)
        REQUIRED   for -12/12&P (MIL-STD 2D)
        REQUIRED   for -13/13&P (MIL-STD 2B)
        OPTIONAL   for -13/13&P (MIL-STD 2C)
        REQUIRED   for -23/23&P (MIL-STD 2B)
        OPTIONAL   for -23/23&P (MIL-STD 2C) 
    -->
    <?xml version="1.0" encoding="UTF-8"?>'''
        tmp += f'<surwp chngno="0" wpno="{wpno}-{self.sys_number}">'
        tmp += '''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>SERVICE UPON RECEIPT</title>
        </wpidinfo>\n'''
        tmp += isb.show()
        tmp += '''<surtsk>
            <siting>'''
        tmp += proc.show()
        tmp += '''</siting>
        </surtsk>
        <surtsk>
            <surmat>
                <unpack>'''
        tmp += proc.show()
        tmp += '''</unpack>
                <chkeqp>
                    <title/>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                </chkeqp>
            </surmat>
        </surtsk>
        <surtsk>
            <preserv>'''
        tmp += proc.show()
        tmp += '''</preserv>
        </surtsk>
        <surtsk>
            <prechkadj>'''
        tmp += proc.show()
        tmp += '''</prechkadj>
        </surtsk>
        <surtsk>
            <precal>'''
        tmp += proc.show()
        tmp += '''</precal>
        </surtsk>
        <surtsk>
            <calign>
                <alignproc>'''
        tmp += proc.show()
        tmp += '''</alignproc>
            </calign>
        </surtsk>'''

        if self.mil_std == '2D' and self.manual_type == ('-12', '-12&P'):
            tmp += '''<surtsk>
                <ammo.sur>'''
            tmp += proc.show()
            tmp += '''</ammo.sur>
            </surtsk>'''

        tmp += '''<surtsk>
            <other.surtsk>'''
        tmp += proc.show()
        tmp += '''</other.surtsk>
        </surtsk>
    </surwp>'''
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-{wpno}-ServiceUponReceipt.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def maintwp(self, wpno, wp_title, proc_type):
        """Function to create Maintainer Procedures WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-{self.sys_number}">\n'
        tmp += '''\t<wpidinfo>
        <maintlvl level="maintainer"/>\n'''
        if proc_type.lower == 'prepforuse':
            tmp += f'<title>{wp_title}<?Pub _newline?>PREP FOR USE</title>\n'
        elif proc_type.lower == 'prepship':
            tmp += f'<title>{wp_title}<?Pub _newline?>PREP FOR SHIPMENT</title>\n'
        elif proc_type.lower == 'prepstore':
            tmp += f'<title>{wp_title}<?Pub _newline?>PREP FOR STORAGE</title>\n'
        else:
            tmp += f'<title>{wp_title}<?Pub _newline?>{proc_type.upper()}</title>\n'
        tmp += '\t</wpidinfo>\n'
        tmp += isb.show()
        tmp += '\t<maintsk>\n'
        tmp += f'\t\t<{proc_type.lower()}>\n'
        tmp += proc.show()
        tmp += f'\t\t</{proc_type.lower()}>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk.show()
        tmp += '</maintwp>'
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-{wpno}-{wp_title}-{proc_type}.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self):
        """Function to create Maintainer Procedures end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = '\t</maintenancecategory>\n' + '</mim>'
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-MAINTAINER_END.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
