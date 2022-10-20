"""SOFTWARE INFORMATION INSTRUCTIONS"""
import cfg
import math
class SoftwareInformation:
    """Class to create various types of WP's included in the Software Information chapter of a TM."""
    lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    def __init__(self, manual_type, mil_std, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.mil_std = mil_std
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function that creates the Software Information chapter header of TM."""
        cfg.prefix_file = (math.floor(cfg.prefix_file/1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
<soim revno="0" chngno="0" chap-toc="no">\n'''
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<titlepg maintlvl="operator">\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<titlepg maintlvl="maintainer">\n'
        tmp += '\t\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')' + '</name>\n'
        tmp += '\t\t</titlepg>\n'
        tmp += '\t\t<softwarecategory>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-SOFTWARE_INFO_START.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softginfowp(self):
        """Function to create the Software General Information WP."""
        tmp = '<softginfowp chngno="0" wpno="S00101-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '\t\t<title>SOFTWARE GENERAL INFORMATION</title>\n'
        tmp += '\t</wpidinfo>\n'
        tmp += isb()
        tmp += '\t<scope>\n'
        tmp += '\t\t<title/>\n'
        tmp += '\t\t<para0>' + self.lorem_ipsum + '</para0>\n'
        tmp += '\t</scope>\n'

        tmp += '\t<mfrr>\n'
        tmp += '\t\t<title/>\n'
        tmp += '\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t</mfrr>\n'

        tmp += '\t<eir>\n'
        tmp += '\t\t<title/>\n'
        tmp += '\t\t<para0>' + self.lorem_ipsum + '</para0>\n'
        tmp += '\t</eir>\n'

        tmp += '\t<softsysover>\n'
        tmp += '\t\t<title/>\n'
        tmp += '\t\t<para0>' + self.lorem_ipsum + '</para0>\n'
        tmp += '\t</softsysover>\n'

        tmp += '\t<softdocover>\n'
        tmp += '\t\t<title/>\n'
        tmp += '\t\t<para0>' + self.lorem_ipsum + '</para0>\n'
        tmp += '\t</softdocover>\n'

        tmp += "\t<!-- OTHER OPTIONS THAT CAN BE INCLUDED: -->\n"
        tmp += '\t<!-- wrntyref | destructmat | nomenreflist -->\n'

        tmp += '\t<loa>\n'
        tmp += '\t\t<title/>\n'
        tmp += '\t\t<para0>' + self.lorem_ipsum + '</para0>\n'
        tmp += '\t</loa>\n'
        tmp += '</softginfowp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-S00101-SoftwareGeneralInfo.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softsumwp(self):
        """Function to create the Software Summary WP."""
        tmp = '<softsumwp chngno="0" wpno="S00102-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '\t\t<title>SOFTWARE SUMMARY</title>\n'
        tmp += '\t</wpidinfo>\n'
        tmp += isb()
        tmp += "\t<!-- OTHER OPTIONS THAT CAN BE INCLUDED HERE: -->\n"
        tmp += '\t<!-- alert;, soft_app? -->\n'
        tmp += '\t<soft_inventory>\n'
        tmp += '\t\t<para0>\n'
        tmp += '\t\t\t<title>Software Inventory</title>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t</para0>\n'
        tmp += '\t</soft_inventory>\n'

        tmp += '\t<soft_environment>\n'
        tmp += '\t\t<para0>\n'
        tmp += '\t\t\t<title>Software Environment</title>\n'
        tmp += '\t\t\t<para>' + self.lorem_ipsum + '</para>\n'
        tmp += '\t\t</para0>\n'
        tmp += '\t</soft_environment>\n'

        tmp += "\t<!-- OTHER OPTIONS THAT CAN BE INCLUDED HERE: -->\n"
        tmp += '\t<!-- soft_secpriv?, soft_superctrls?, soft_assistreport? -->\n'
        tmp += '</softsumwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-S00102-SoftwareSummary.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softeffectwp(self):
        """Function to create the Software Information Effectivity WP."""

    def softdiffversionwp(self):
        """Function to create the Software Information Differences Between Software Versions WP."""

    def softfeaturescapwp(self):
        """Function to create the Software Information Features and Capabilities WP."""
        tmp = '<softfeaturescapwp chngno="0" wpno="S00105-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '\t\t<title>SOFTWARE FEATURES AND CAPABILITIES</title>\n'
        tmp += '\t</wpidinfo>\n'
        tmp += isb()
        tmp += proc()
        tmp += proc()
        tmp += '</softfeaturescapwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-S00105-SWFeaturesCapabilities.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10
    def softscreendisplaywp(self):
        """Function to create the Software Information Screen Displays WP."""
        tmp = '<softscreendisplaywp chngno="0" wpno="S00106-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>SCREEN DISPLAYS</title>
    </wpidinfo>\n'''
        tmp += isb()
        tmp += proc()
        tmp += proc()
        tmp += '</softscreendisplaywp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-S00106-SoftwareScreenDisplays.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softmenuwp(self):
        """Function to create the Software Information Menus and Directories WP."""
        tmp = '<softmenuwp chngno="0" wpno="S00107-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '\t\t<title>MENU/DIRECTORIES</title>\n'
        tmp += '\t</wpidinfo>\n'
        tmp += isb()
        tmp += proc()
        tmp += proc()
        tmp += '</softmenuwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-S00107-SoftwareMenu.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softtoolswp(self):
        """Function to create the Software Tools and Buttons WP."""
        tmp = '<softtoolswp chngno="0" wpno="S00108-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '\t\t<title>TOOLS AND BUTTONS</title>\n'
        tmp += '\t</wpidinfo>\n'
        tmp += isb()
        tmp += '\t<ctrlindtab>\n'
        tmp += '\t\t<title>Lorem Ipsum</title>\n'
        tmp += '\t\t<figure id="SXXXXX-XX-XXXX-XXX-FXXXX">\n'
        tmp += '\t\t\t<title>Lorem Ipsum</title>\n'
        tmp += '\t\t\t<graphic boardno="PLACEHOLDER"/>\n'
        tmp += '\t\t</figure>\n'
        tmp += '\t\t<ctrlindrow>\n'
        tmp += '\t\t\t<key></key>\n'
        tmp += '\t\t\t<ctrlind></ctrlind>\n'
        tmp += '\t\t\t<function></function>\n'
        tmp += '\t\t</ctrlindrow>\n'
        tmp += '\t\t<ctrlindrow>\n'
        tmp += '\t\t\t<key></key>\n'
        tmp += '\t\t\t<ctrlind></ctrlind>\n'
        tmp += '\t\t\t<function></function>\n'
        tmp += '\t\t</ctrlindrow>\n'
        tmp += '\t\t<ctrlindrow>\n'
        tmp += '\t\t\t<key></key>\n'
        tmp += '\t\t\t<ctrlind></ctrlind>\n'
        tmp += '\t\t\t<function></function>\n'
        tmp += '\t\t</ctrlindrow>\n'
        tmp += '\t\t<ctrlindrow>\n'
        tmp += '\t\t\t<key></key>\n'
        tmp += '\t\t\t<ctrlind></ctrlind>\n'
        tmp += '\t\t\t<function></function>\n'
        tmp += '\t\t</ctrlindrow>\n'
        tmp += '\t\t<ctrlindrow>\n'
        tmp += '\t\t\t<key></key>\n'
        tmp += '\t\t\t<ctrlind></ctrlind>\n'
        tmp += '\t\t\t<function></function>\n'
        tmp += '\t\t</ctrlindrow>\n'
        tmp += '\t</ctrlindtab>\n'
        tmp += '\t<ctrlindtab>\n'
        tmp += '\t\t<title>Lorem Ipsum</title>\n'
        tmp += '\t\t<figure id="SXXXXX-XX-XXXX-XXX-FXXXX">\n'
        tmp += '\t\t\t<title>Lorem Ipsum</title>\n'
        tmp += '\t\t\t<graphic boardno="PLACEHOLDER"/>\n'
        tmp += '\t\t</figure>\n'
        tmp += '\t\t<ctrlindrow>\n'
        tmp += '\t\t\t<key></key>\n'
        tmp += '\t\t\t<ctrlind></ctrlind>\n'
        tmp += '\t\t\t<function></function>\n'
        tmp += '\t\t</ctrlindrow>\n'
        tmp += '\t\t<ctrlindrow>\n'
        tmp += '\t\t\t<key></key>\n'
        tmp += '\t\t\t<ctrlind></ctrlind>\n'
        tmp += '\t\t\t<function></function>\n'
        tmp += '\t\t</ctrlindrow>\n'
        tmp += '\t\t<ctrlindrow>\n'
        tmp += '\t\t\t<key></key>\n'
        tmp += '\t\t\t<ctrlind></ctrlind>\n'
        tmp += '\t\t\t<function></function>\n'
        tmp += '\t\t</ctrlindrow>\n'
        tmp += '\t</ctrlindtab>\n'
        tmp += '</softtoolswp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-S00108-SWToolsAndButtons.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softsecprivwp(self):
        """Function to create the Software Information Security and Privacy Procedures WP."""
        tmp = '<softsecprivwp chngno="0" wpno="S00109-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '\t\t<title>SECURITY AND PRIVACY PROCEDURES</title>\n'
        tmp += '\t</wpidinfo>\n'
        tmp += isb()
        tmp += proc()
        tmp += proc()
        tmp += '</softsecprivwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-S00109-SecurityPrivacyProcedures.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softsuperctrlswp(self):
        """Function to create the Software Supervisory Controls WP."""

    def softpowerupwp(self):
        """Function to create the Software Powerup/Powerdown Procedures WP."""
        tmp = '<softpowerupwp chngno="0" wpno="S00111-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '\t\t<title>POWERUP/STARTUP AND POWERDOWN/SHUTDOWN PROCEDURES</title>\n'
        tmp += '\t</wpidinfo>\n'
        tmp += isb()
        tmp += proc()
        tmp += proc()
        tmp += '</softpowerupwp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-S00111-SWPowerProcedures.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def softaccesswp(self):
        """Function to create the Accessing/Exiting Software
         WP."""
        tmp = '<softaccesswp chngno="0" wpno="S00111-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        if self.manual_type == '-10' or self.manual_type == '-13&P':
            tmp += '\t\t<maintlvl level="operator"/>\n'
        elif self.manual_type == '-23&P':
            tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '\t\t<title>ACCESSING/EXITING SOFTWARE</title>\n'
        tmp += '\t</wpidinfo>\n'
        tmp += isb()
        tmp += proc()
        tmp += proc()
        tmp += '</softaccesswp>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-S00111-AccessingExitingSoftware.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self):
        """Function to create the Software Information chapter end tags."""
        tmp = '\t</softwarecategory>'
        tmp += '</soim>'
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-SOFTWARE_INFO_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
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

def proc():
    """Function to create a filled in <proc> block."""
    tmp = '''\t<proc>
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
        <figure id="SXXXXX-XX-XXXX-XXX-FXXX1">
            <title>Lorem Ipsum</title>
            <graphic boardno="PLACEHOLDER"/>
        </figure>
        <step1>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
        </step1>
        <step1>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
        </step1>
    </proc>\n'''
    return tmp