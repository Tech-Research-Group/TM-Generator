"""AUXILIARY EQUIPMENT MAINTENANCE INSTRUCTIONS"""
import cfg
import math

class AuxiliaryEquipment:
    """Class to create various types of WP's included in the Auxiliary Equipment
    Maintenance Instructions chapter of a TM.
    """
    lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    def __init__(self, manual_type, mil_std, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.mil_std = mil_std
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function that creates the Auxiliary Equipment Maintenance
        Instructions chapter header of TM.
        """
        cfg.prefix_file = (math.floor(cfg.prefix_file/1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
<mim revno="0" chngno="0" chap-toc="no">\n'''
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<titlepg maintlvl="operator">\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<titlepg maintlvl="maintainer">\n'
        tmp += '\t\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')' + '</name>\n'
        tmp += '\t\t</titlepg>\n'
        tmp += '\t\t<auxiliarycategory>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-AUXILIARY_START.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def auxeqpwp(self):
        """Function to create an Auxiliary Equipment Maintenance Instructions WP."""
        index = 1
        tasks = ('Storage', 'Preventive Maintenance', 'Lubrication', 'Operating Checks', 'Adjustments')
        for task in tasks:
            tmp = '<auxeqpwp chngno="0" wpno="O0100' + str(index) + '-' + self.sys_number + '">\n'
            tmp += '\t<wpidinfo>\n'
            if self.manual_type == '-10' or self.manual_type == '-13&P':
                tmp += '\t\t<maintlvl level="operator"/>\n'
            elif self.manual_type == '-23&P':
                tmp += '\t\t<maintlvl level="maintainer"/>\n'
            tmp += '\t\t<title>' + task.upper() + '</title>\n'
            tmp += '\t</wpidinfo>\n'
            tmp += isb()
            tmp += '\t<proc>\n'
            tmp += '\t\t<title>' + task + '</title>\n'
            tmp += '\t\t<step1>\n'
            tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
            tmp += '\t\t</step1>\n'
            tmp += '\t\t<step1>\n'
            tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
            tmp += '\t\t</step1>\n'
            tmp += '\t\t<step1>\n'
            tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
            tmp += '\t\t</step1>\n'
            tmp += '\t</proc>\n'
            tmp += '</auxeqpwp>\n'
            with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
                ' WIP/{:05d}'.format(cfg.prefix_file) + str(index) + '-O0100' + str(index) + '-Auxiliary' + task + 'WP.txt', 'w', encoding='UTF-8') as _f:
                _f.write(tmp)
            index += 1
            cfg.prefix_file += 10

    def manu_items_introwp(self):
        """Function to create the Illustrated List of Manufactured Items WP."""
        tmp = '<manu_items_introwp chngno="0" wpno="O01006-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''<title>ILLUSTRATED LIST OF MANUFACTURED ITEMS INTRODUCTION</title>
    </wpidinfo>
    <intro>
        <para0>
            <title>SCOPE</title>
            <para>This work package includes complete instructions for making items authorized to be manufactured or fabricated at the (enter applicable maintenance level).</para>
            <subpara1>
                <title>How to Use the Index of Manufactured Items</title>
                <para>A part number index in alphanumeric order is provided for cross-referencing the part number of the item to be manufactured to the information that covers fabrication criteria.</para>
            </subpara1>
            <subpara1>
                <title>Explanation of the Illustrations of Manufactured Items</title>
                <para>All instructions needed by maintenance personnel to manufacture the item shall be provided and shall include illustrations as required. (When applicable, a reference to the associated parts information TM or parts information work package shall be entered here.) All bulk materials needed for manufacture of an item are listed by part number or specification number in a tabular list on the illustration.</para>
            </subpara1>
        </para0>
    </intro>
    <manuindx>
        <title>INDEX OF MANUFACTURED ITEMS</title>
        <partdesc>
            <partno></partno>
            <cageno></cageno>
            <dwgno></dwgno>
        </partdesc>
        <partdesc>
            <partno></partno>
            <cageno></cageno>
            <dwgno></dwgno>
        </partdesc>
        <partdesc>
            <partno></partno>
            <cageno></cageno>
            <dwgno></dwgno>
        </partdesc>
        <partdesc>
            <partno></partno>
            <cageno></cageno>
            <dwgno></dwgno>
        </partdesc>
        <partdesc>
            <partno></partno>
            <cageno></cageno>
            <dwgno></dwgno>
        </partdesc>
    </manuindx>
</manu_items_introwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-O01006-IllustratedListIntroWP.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def manuwp(self):
        """Function to create the Manufacturing Procedures WP."""
        tmp = '<manuwp chngno="0" wpno="O01007-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''<title>MANUFACTURING PROCEDURES</title>
    </wpidinfo>\n'''
        tmp += isb()
        tmp += '''\t<manuitem>
    </manuitem>
</manuwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-O01007-ManufacturingProceduresWP.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def torquewp(self):
        """Function to create the Torque Limits WP."""
        tmp = '<torquewp chngno="0" wpno="O01008-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''<title>TORQUE LIMITS</title>
    </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<torqueval>\n'
        tmp += '\t\t<title>TORQUE LIMITS</title>\n'
        tmp += '\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t</torqueval>\n'
        tmp += '</torquewp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-O01008-TorqueLimitsWP.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def wiringwp(self):
        """Function to create the Wiring Diagrams WP."""
        tmp = '<wiringwp chngno="0" wpno="O01009-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''<title>WIRING DIAGRAMS</title>
    </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<intro>\n'
        tmp += '\t\t<para0>' + self.lorem_ipsum + '</para0>\n'
        tmp += '\t</intro>\n'
        tmp += '\t<abbrev>\n'
        tmp += '\t\t<title>Lorem Ipsum</title>\n'
        tmp += '\t\t<figure id="MXXXXX-XX-XXXX-XXX-FXXX3"></figure>\n'
        tmp += '\t\t<para0>' + self.lorem_ipsum + '</para0>\n'
        tmp += '\t</abbrev>\n'
        tmp += '\t<component_desc>\n'
        tmp += '\t\t<para0>' + self.lorem_ipsum + '</para0>\n'
        tmp += '\t</component_desc>\n'
        tmp += '\t<wireid>\n'
        tmp += '\t\t<title>Lorem Ipsum</title>\n'
        tmp += '\t\t<figure id="MXXXXX-XX-XXXX-XXX-FXXX3"></figure>\n'
        tmp += '\t\t<para0>' + self.lorem_ipsum + '</para0>\n'
        tmp += '\t</wireid>\n'
        tmp += '\t<wire_color>\n'
        tmp += '\t\t<para0>' + self.lorem_ipsum + '</para0>\n'
        tmp += '\t</wire_color>\n'
        tmp += '\t<wiringdiag>\n'
        tmp += '\t\t<title>Lorem Ipsum</title>\n'
        tmp += '\t\t<figure id="MXXXXX-XX-XXXX-XXX-FXXX3"></figure>\n'
        tmp += '\t\t<para0>' + self.lorem_ipsum + '</para0>\n'
        tmp += '\t</wiringdiag>\n'
        tmp += '</wiringwp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-O01009-WiringDiagramsWP.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10
        
    def end(self):
        """Function to create the Auxiliary Equipment Maintenance
        Instructions chapter end tags.
        """
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        tmp = '\t</auxiliarycategory>\n'
        tmp += '</mim>'

        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-AUXILIARY_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
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
        <mtrlpart>
            <mtrlpart-setup-item>
                <name></name>
                <qty></qty>
                <itemref>
                    <xref itemid="XX-XXXX-XXX" wpid="XX-XXXX-XXX"/>
                </itemref>
            </mtrlpart-setup-item>
        </mtrlpart>
        <persnreq>
            <persnreq-setup-item>
                <name></name>
            </persnreq-setup-item>
        </persnreq>
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