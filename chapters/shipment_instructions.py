"""SHIPMENT/MOVEMENT AND STORAGE MAINTENANCE INSTRUCTIONS"""
import cfg
import math

class ShipmentInstructions:
    """Class to create various types of WP's included in the Shipment/Movement and Storage
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
        """Function that creates the Shipment/Movement and Storage Maintenance
        Instructions chapter header of TM."""
        cfg.prefix_file = (math.floor(cfg.prefix_file/1000) * 1000) + 10
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += '<mim revno="0" chngno="0" chap-toc="no">\n'
        tmp += '\t\t<titlepg maintlvl="operator">\n'
        tmp += '\t\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')' + '</name>\n'
        tmp += '\t\t</titlepg>\n'
        tmp += '\t\t<shipmentmovementstoragecategory>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-SHIPPING/STORAGE_START.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def prepstore(self):
        """Function to create Shipment/Movement and Storage Maintenance
        Instructions chapter prepstore WP."""
        tmp = '<maintwp chngno="0" wpno="M00601-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>LOREM IPSUM<?Pub _newline?>PREPARATION FOR STORAGE</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<prepstore>\n'
        tmp += proc()
        tmp += '\t\t</prepstore>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-M00601-PrepForStorage.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def prepship(self):
        """Function to create Shipment/Movement and Storage Maintenance
        Instructions chapter prepship WP."""
        tmp = '<maintwp chngno="0" wpno="M00602-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>LOREM IPSUM<?Pub _newline?>PREPARATION FOR SHIPPING</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<prepship>\n'
        tmp += proc()
        tmp += '\t\t</prepship>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-M00602-PrepForShipment.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def transport(self):
        """Function to create Shipment/Movement and Storage Maintenance
        Instructions chapter transport WP."""
        tmp = '<maintwp chngno="0" wpno="M00603-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>LOREM IPSUM<?Pub _newline?>TRANSPORT</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<transport>\n'
        tmp += proc()
        tmp += '\t\t</transport>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-M00603-Transport.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self):
        """ Function to create Shipment/Movement and Storage Maintenance
        Instructions chapter end tags. """
        tmp = '</mim>'
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-SHIPPING/STORAGE_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
        
def followon_maintsk():
    """Function to create the Follow-on Maintenance WP."""
    tmp = '''\t<followon.maintsk>
        <proc>
            <title/>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
        </proc>
    </followon.maintsk>'''
    return tmp

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

def proc():
    """Function to create a filled in <proc> block."""
    tmp = '''\n<proc>
       <title>Lorem Ipsum</title>
        <step1>
            <specpara>
                <warning>
                    <icon-set boardno="Falling"/>
                    <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
                </warning>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
            </specpara>
        </step1>
        <step1>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
        </step1>
        <figure id="MXXXXX-XX-XXXX-XXX-FXXX1">
            <title>Lorem Ipsum</title>
            <graphic boardno="PLACEHOLDER"/>
        </figure>
        <step1>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
        </step1>
        <step1>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
        </step1>
        <figure id="MXXXXX-XX-XXXX-XXX-FXXX2">
            <title>Lorem Ipsum</title>
            <graphic boardno="PLACEHOLDER"/>
        </figure>
    </proc>\n'''
    return tmp
