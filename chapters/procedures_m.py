"""MAINTAINER PROCEDURES"""
import cfg
import math

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
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
    <mim chngno="0" revno="0" chap-toc="no">\n'''
        tmp += '\t<titlepg maintlvl="maintainer">\n'
        tmp += '\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')</name>\n'
        tmp += '\t</titlepg>\n'
        tmp += '\t<maintenancecategory>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-MAINTAINER_START.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
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
        tmp += f'<surwp chngno="0" wpno="{wpno}-' + self.sys_number + '">'
        tmp += '''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>SERVICE UPON RECEIPT</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '''<surtsk>
            <siting>'''
        tmp += proc()
        tmp += '''</siting>
        </surtsk>
        <surtsk>
            <surmat>
                <unpack>'''
        tmp += proc()
        tmp += '''</unpack>
                <chkeqp>
                    <title/>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                </chkeqp>
            </surmat>
        </surtsk>
        <surtsk>
            <preserv>'''
        tmp += proc()
        tmp += '''</preserv>
        </surtsk>
        <surtsk>
            <prechkadj>'''
        tmp += proc()
        tmp += '''</prechkadj>
        </surtsk>
        <surtsk>
            <precal>'''
        tmp += proc()
        tmp += '''</precal>
        </surtsk>
        <surtsk>
            <calign>
                <alignproc>'''
        tmp += proc()
        tmp += '''</alignproc>
            </calign>
        </surtsk>'''

        if self.mil_std == '2D' and self.manual_type == ('-12', '-12&P'):
            tmp += '''<surtsk>
                <ammo.sur>'''
            tmp += proc()
            tmp += '''</ammo.sur>
            </surtsk>'''

        tmp += '''<surtsk>
            <other.surtsk>'''
        tmp += proc()
        tmp += '''</other.surtsk>
        </surtsk>
    </surwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-ServiceUponReceipt.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def inspect(self, wpno, wp_title):
        """Function to create Maintainer Procedures inspect WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>INSPECT</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<inspect>\n'
        tmp += proc()
        tmp += '\t\t</inspect>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-{}-INSPECT.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def test(self, wpno, wp_title):
        """Function to create Maintainer Procedures test WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>TEST</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<test>\n'
        tmp += proc()
        tmp += '\t\t</test>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-{}-TEST.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def service(self, wpno, wp_title):
        """Function to create Maintainer Procedures service WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>SERVICE</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<service>\n'
        tmp += proc()
        tmp += '\t\t</service>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-{}-SERVICE.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def remove(self, wpno, wp_title):
        """Function to create Maintainer Procedures remove WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>REMOVE</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<remove>\n'
        tmp += proc()
        tmp += '\t\t</remove>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-{}-REMOVE.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def install(self, wpno, wp_title):
        """Function to create Maintainer Procedures install WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>INSTALL</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<install>\n'
        tmp += proc()
        tmp += '\t\t</install>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-{}-INSTALL.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def replace(self, wpno, wp_title):
        """Function to create Maintainer Procedures replace WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>REPLACE</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<replace>\n'
        tmp += proc()
        tmp += '\t\t</replace>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-{}-REPLACE.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def repair(self, wpno, wp_title):
        """Function to create Maintainer Procedures repair WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>REPAIR</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<repair>\n'
        tmp += proc()
        tmp += '\t\t</repair>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-{}-REPAIR.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pack(self, wpno, wp_title):
        """Function to create Maintainer Procedures pack WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>PACK</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<pack>\n'
        tmp += proc()
        tmp += '\t\t</pack>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-{}-PACK.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def unpack(self, wpno, wp_title):
        """Function to create Maintainer Procedures unpack WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>UNPACK</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<unpack>\n'
        tmp += proc()
        tmp += '\t\t</unpack>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-{}-UNPACK.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def prepforuse(self, wpno, wp_title):
        """Function to create Maintainer Procedures prepforuse WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>PREPARATION FOR USE</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<prepforuse>\n'
        tmp += proc()
        tmp += '\t\t</prepforuse>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-{}-PREPFORUSE.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def clean(self, wpno, wp_title):
        """Function to create Maintainer Procedures clean WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>CLEAN</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += '\t<maintsk>\n'
        tmp += '\t\t<clean>\n'
        tmp += proc()
        tmp += '\t\t</clean>\n'
        tmp += '\t</maintsk>\n'
        tmp += followon_maintsk()
        tmp += '</maintwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-{}-CLEAN.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def prepstore(self, wpno, wp_title):
        """Function to create Maintainer Procedures prepstore WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>PREPARATION FOR STORAGE</title>
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
                ' WIP/{:05d}-{}-{}-PREP STORAGE.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def prepship(self, wpno, wp_title):
        """Function to create Maintainer Procedures prepship WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>PREPARATION FOR SHIPPING</title>
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
                ' WIP/{:05d}-{}-{}-PREP SHIP.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def transport(self, wpno, wp_title):
        """Function to create Maintainer Procedures transport WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}<?Pub _newline?>TRANSPORT</title>
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
                ' WIP/{:05d}-{}-{}-TRANSPORT.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self):
        """Function to create Maintainer Procedures end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        tmp = '\t</maintenancecategory>\n'
        tmp += '</mim>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-MAINTAINER_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
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
