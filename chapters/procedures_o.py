"""OPERATOR PROCEDURES"""
import math
import cfg
import views.followon_maintsk as followon_maintsk
import views.isb as isb
import views.proc as proc


class OperatorProcedures:
    """Class to create various types of WP's included in Operator Procedures of a TM."""
    def __init__(self, manual_type, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function to create Operator Procedures start tags."""
        cfg.prefix_file = (math.floor(cfg.prefix_file / 1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
<mim chngno="0" revno="0" chap-toc="no">\n'''
        tmp += '\t<titlepg maintlvl="operator">\n'
        tmp += f'\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n'
        tmp += '\t</titlepg>\n' + '\t<maintenancecategory>\n'
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-OPERATOR_START.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10
    
    def maintwp(self, wpno, wp_title, proc_type):
        """Function to create Operator Procedures WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-{self.sys_number}">\n'
        tmp += '''\t<wpidinfo>
        <maintlvl level="operator"/>\n'''
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
        """Function to create Operator Procedures end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = '\t</maintenancecategory>\n' + '</mim>'
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-OPERATOR_END.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 1

