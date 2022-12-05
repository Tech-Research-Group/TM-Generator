"""OPERATOR INSTRUCTIONS"""
import math
import cfg
import views.isb as isb
class OperatorInstructions:
    """Class to create various types of WP's included in Operator Instructions section of a TM."""
    lorem_ipsum = \
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    TAB_2 = '\t\t'
    TAB_3 = '\t\t\t'
    TAB_4 = '\t\t\t\t'

    def __init__(self, manual_type, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function that creates Operator Instructions section starting tags of TM."""
        cfg.prefix_file = (math.floor(cfg.prefix_file / 1000) * 1000) + 10
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += '<opim chngno="0" revno="0" chap-toc="no">\n' + '\t<titlepg maintlvl="operator">\n'
        tmp += f'\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n'
        tmp += '\t</titlepg>\n'
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-OPER_INSTRUCTIONS_START.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def controls_indicators(self):
        """Function to create Controls and Indicators section of Operator Instructions section."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += '<ctrlindwp chngno="0" wpno="O00001-' + self.sys_number + '">\n'
        tmp += '\t<?Pub Dtl?>\n'
        tmp += '\t<wpidinfo>\n'
        tmp += self.TAB_2 + '<maintlvl level="operator"/>\n'
        tmp += self.TAB_2 + '<title>DESCRIPTION AND USE OF OPERATOR CONTROLS AND INDICATORS</title>\n'
        tmp += '\t</wpidinfo>\n'
        tmp += '\t<intro>\n'
        tmp += self.TAB_2 + '<para0-alt>\n'
        tmp += self.TAB_3 + '<para0>\n'
        tmp += self.TAB_4 + '<title>Introduction</title>\n'
        tmp += f'{self.TAB_4}<para>{self.lorem_ipsum}</para>\n'
        tmp += self.TAB_3 + '</para0>\n'
        tmp += self.TAB_2 + '</para0-alt>\n'
        tmp += '\t</intro>\n'
        tmp += '\t<ctrlindtab>\n'
        tmp += '\t\t<title>Lorem Ipsum</title>\n'
        tmp += f'\t\t<figure id="O00001-{self.sys_number}-F0001">\n'
        tmp += '''\t\t\t<title>Lorem Ipsum</title>
                <graphic boardno="PLACEHOLDER"/>
            </figure>
            <ctrlindrow>
                <key>1</key>
                <ctrlind></ctrlind>
                <function></function>
            </ctrlindrow>
            <ctrlindrow>
                <key>2</key>
                <ctrlind></ctrlind>
                <function></function>
            </ctrlindrow>
        </ctrlindtab>
        <ctrlindtab>
            <title>Lorem Ipsum</title>\n'''
        tmp += f'\t\t<figure id="O00001-{self.sys_number}-F0011">\n'
        tmp += '''\t\t\t<title>Lorem Ipsum</title>
            <graphic boardno="PLACEHOLDER"/>
        </figure>
        <ctrlindrow>
            <key>1</key>
            <ctrlind></ctrlind>
            <function></function>
        </ctrlindrow>
        <ctrlindrow>
            <key>2</key>
            <ctrlind></ctrlind>
            <function></function>
        </ctrlindrow>
    </ctrlindtab>
</ctrlindwp>'''
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-O00001-ControlsIndicators.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def opusualwp(self, wpno, wp_title, cond_type):
        """Function to create operating procedures WP."""
        tmp = f'<opusualwp chngno="0" wpno="{wpno}-{self.sys_number}">\n'
        tmp += '''<wpidinfo>
        <maintlvl level="operator"/>\n'''
        tmp += f'<title>OPERATION UNDER USUAL CONDITIONS<?Pub _newline?>{wp_title}</title>\n'
        tmp += '</wpidinfo>\n'
        tmp += isb.show()
        tmp += f'''\t<opertsk>
        <{cond_type}>
            <proc>
                <title>Lorem Ipsum</title>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua</para>
            </proc>
        </{cond_type}>
    </opertsk>
</opusualwp>'''
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-{wpno}-{wp_title}.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def unusual_conditions(self, wpno):
        """Function to create the operating under unusual conditions section."""
        tmp = f'<opunuwp chngno="0" wpno="{wpno}-{self.sys_number}">\n'
        tmp += '''<wpidinfo>
        <maintlvl level="operator"/>
        <title>OPERATION UNDER UNUSUAL CONDITIONS</title>
    </wpidinfo>\n'''
        tmp += isb.show()
        tmp += f'''\t<opunutsk>
        <unusualenv>
            <proc>
                <title>GENERAL INFORMATION</title>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
            </proc>
            <proc>
                <title>Operation on Sloped Terrain</title>
                <note>
                    <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
                </note>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
            </proc>
            <proc>
                <title>Operation in Cold</title>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
            </proc>
            <proc>
                <title>Operation in Extreme Cold</title>
                <note>
                    <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
                </note>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
            </proc>
            <proc>
                <title>Storage in Cold</title>
                <note>
                    <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
                </note>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
            </proc>
            <proc>
                <title>Operation on in Extreme Heat</title>
                <note>
                    <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
                </note>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
            </proc>
            <proc>
                <title>Operation on Sloped Terrain</title>
                <note>
                    <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
                </note>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
            </proc>
            <proc>
                <title>Operation on Sloped Terrain</title>
                <note>
                    <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
                </note>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
            </proc>
            <proc>
                <title>Operation in Sandy or Dusty Areas</title>
                <note>
                    <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
                </note>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
            </proc>
            <proc>
                <title>Operation in Rain</title>
                <note>
                    <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
                </note>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
            </proc>
            <proc>
                <title>Operation in Freezing Rain and Snow</title>
                <note>
                    <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
                </note>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
            </proc>
            <proc>
                <title>Operation in High Altitude</title>
                <note>
                    <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</trim.para>
                </note>
                <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
            </proc>
            <proc>
                <para>
                    <emphasis emph="bold">ALTITUDE</emphasis>
                </para>
            </proc>
            <proc>
                <title>Adjust Air Damper</title>
                <step1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                </step1>
                <figure id="{wpno}-{self.sys_number}-F0001">
                    <title>Air Damper Adjustment</title>
                    <graphic boardno="PLACEHOLDER"/>
                </figure>
                <step1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                </step1>
                <step1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                </step1>
            </proc>
        </unusualenv>
    </opunutsk>
</opunuwp>'''
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-{wpno}-OperationUnderUnusualConditions.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10
        
    def end(self):
        """Function to create Operator Instructions section end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = '</opim>'
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-OPER_INSTRUCTIONS_END.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
