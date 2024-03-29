"""AMMUNITION MAINTENANCE INSTRUCTIONS"""
import cfg
import math

class Ammunition:
    """Class to create various types of WP's included in the Ammunition
    Maintenance Instructions chapter of a TM."""
    lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    def __init__(self, manual_type, mil_std, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.mil_std = mil_std
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function that creates the Ammunition Maintenance
        Instructions chapter header of TM."""
        cfg.prefix_file = (math.floor(cfg.prefix_file/1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
<mim revno="0" chngno="0" chap-toc="no">\n'''
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t<titlepg maintlvl="operator">\n'
        elif self.manual_type == '-23&P':
            tmp += '\t<titlepg maintlvl="maintainer">\n'
        tmp += '\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')' + '</name>\n'
        tmp += '\t</titlepg>\n'
        tmp += '\t<ammunitioncategory>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-AMMUNITION_START.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def ammoidentwp(self):
        """Function to create the Ammo Identification WP."""
        tmp = '<ammoidentwp chngno="0" wpno="O02000.5-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''<title>AMMUNITION IDENTIFICATION</title>
    </wpidinfo>\n'''
        tmp += isb()

        tmp += '</ammoidentwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-O02000.5-AmmoIdentification.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def surwp(self):
        """Function to create the Service Upon Receipt WP."""
        tmp = '<surwp chngno="0" wpno="O02001-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''<title>SERVICE UPON RECEIPT</title>
    </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<surtsk>\n'
        tmp += '\t\t<ammo.defect>\n'
        tmp += '\t\t\t<proc>\n'
        tmp += '\t\t\t\t<title/>\n'
        tmp += '\t\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t\t</proc>\n'
        tmp += '\t\t</ammo.defect>\n'
        tmp += '\t</surtsk>\n'
        tmp += '\t<surtsk>\n'
        tmp += '\t\t<ammo.handling>\n'
        tmp += '\t\t\t<unpack>\n'
        tmp += '\t\t\t\t<proc>\n'
        tmp += '\t\t\t\t\t<title/>\n'
        tmp += '\t\t\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t\t\t</proc>\n'
        tmp += '\t\t\t</unpack>\n'
        tmp += '\t\t\t<pack>\n'
        tmp += '\t\t\t\t<proc>\n'
        tmp += '\t\t\t\t\t<title/>\n'
        tmp += '\t\t\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t\t\t</proc>\n'
        tmp += '\t\t\t</pack>\n'
        tmp += '\t\t</ammo.handling>\n'
        tmp += '\t</surtsk>\n'
        tmp += "\t<!-- OTHER OPTIONAL SURTSK's THAT CAN BE INCLUDED: -->\n"
        tmp += '\t<!-- arm | calign | install | mark | other.surtsk | precal | prechkadj | preserv | shltr | siting | surmat -->\n'
        tmp += '</surwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-O02001-AmmunitionSURWP.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def ammowp(self):
        """Function to create the Ammunition Maintenance WP."""
        tmp = '<ammowp chngno="0" wpno="O02002-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''<title>AMMUNITION MAINTENANCE</title>
    </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<mark>\n'
        tmp += '\t\t<proc>\n'
        tmp += '\t\t\t<title/>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t</proc>\n'
        tmp += '\t</mark>\n'

        tmp += '\t<ammo.defect>\n'
        tmp += '\t\t<proc>\n'
        tmp += '\t\t\t<title/>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t</proc>\n'
        tmp += '\t</ammo.defect>\n'

        tmp += '\t<ammo.handling>\n'
        tmp += '\t\t<unpack>\n'
        tmp += '\t\t\t<proc>\n'
        tmp += '\t\t\t<title/>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t\t</proc>\n'
        tmp += '\t\t</unpack>\n'
        tmp += '\t\t<pack>\n'
        tmp += '\t\t\t<proc>\n'
        tmp += '\t\t\t<title/>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t\t</proc>\n'
        tmp += '\t\t</pack>\n'
        tmp += '\t</ammo.handling>\n'

        tmp += '\t<paint>\n'
        tmp += '\t\t<proc>\n'
        tmp += '\t\t\t<title/>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t</proc>\n'
        tmp += '\t</paint>\n'

        tmp += '\t<clean>\n'
        tmp += '\t\t\t<title/>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t</clean>\n'

        tmp += '</ammowp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-O02002-AmmunitionMaintenance.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def ammo_markingwp(self):
        """Function to create the Ammunition Marking Information WP."""
        tmp = '<ammo.markingwp chngno="0" wpno="O02003-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''<title>AMMUNITION MARKING INFORMATION</title>
    </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<mark>\n'
        tmp += '\t\t<proc>\n'
        tmp += '\t\t\t<title/>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t</proc>\n'
        tmp += '\t</mark>\n'

        tmp += '\t<ammo.handling>\n'
        tmp += '\t\t<pack>\n'
        tmp += '\t\t\t<proc>\n'
        tmp += '\t\t\t<title/>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t\t</proc>\n'
        tmp += '\t\t</pack>\n'
        tmp += '\t</ammo.handling>\n'

        tmp += '\t<ammotype>\n'
        tmp += '\t\t<proc>\n'
        tmp += '\t\t\t<title>AMMUNITION TYPES</title>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t</proc>\n'
        tmp += '\t</ammotype>\n'

        tmp += '</ammo.markingwp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-O02003-AmmunitionMarkingInfo.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def natowp(self):
        """Function to create the Foreign Ammunition (NATO) WP."""
        tmp = '<natowp chngno="0" wpno="O02004-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''<title>FOREIGN AMMUNITION (NATO)</title>
    </wpidinfo>\n'''
        tmp += isb()

        tmp += '\t<mark>\n'
        tmp += '\t\t<proc>\n'
        tmp += '\t\t\t<title/>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t</proc>\n'
        tmp += '\t</mark>\n'

        tmp += '\t<ammo.handling>\n'
        tmp += '\t\t<pack>\n'
        tmp += '\t\t\t<proc>\n'
        tmp += '\t\t\t<title/>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t\t</proc>\n'
        tmp += '\t\t</pack>\n'
        tmp += '\t</ammo.handling>\n'

        tmp += '\t<ammotype>\n'
        tmp += '\t\t<proc>\n'
        tmp += '\t\t\t<title>AMMUNITION TYPES</title>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t</proc>\n'
        tmp += '\t</ammotype>\n'

        tmp += '</natowp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-O02004-ForeignAmmunition.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self):
        """Function to create the Ammunition Maintenance Instructions chapter end tags."""
        tmp = '\t</ammunitioncategory>'
        tmp += '</mim>'
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-AMMUNITION_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
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
        <eqpconds>
            <eqpconds-setup-item>
                <condition></condition>
                <itemref>
                    <xref wpid="XX-XXXX-XXX"/>
                </itemref>
            </eqpconds-setup-item>
        </eqpconds>
        <ref>
            <ref-setup-item>
                <xref wpid="XX-XXXX-XXX"/>
            </ref-setup-item>
        </ref>
    </initial_setup>\n'''
    return isb_tmp