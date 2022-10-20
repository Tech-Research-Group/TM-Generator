"""OPERATOR INSTRUCTIONS"""
import cfg
import math

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
        cfg.prefix_file = (math.floor(cfg.prefix_file/1000) * 1000) + 10
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += '<opim chngno="0" revno="0" chap-toc="no">\n'
        tmp += '\t<titlepg maintlvl="operator">\n'
        tmp += '\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')</name>\n'
        tmp += '\t</titlepg>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-OPER_INSTRUCTIONS_START.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
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
        tmp += self.TAB_4 + '<para>' + self.lorem_ipsum + '</para>\n'
        tmp += self.TAB_3 + '</para0>\n'
        tmp += self.TAB_2 + '</para0-alt>\n'
        tmp += '\t</intro>\n'
        tmp += '\t<ctrlindtab>\n'
        tmp += '<title>Lorem Ipsum</title>\n'
        tmp += '<figure id="O00001-' + self.sys_number+ '-F0001">\n'
        tmp += '''<title>Lorem Ipsum</title>
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
            <title>Lorem Ipsum</title>'''
        tmp += '<figure id="O00001-' + self.sys_number + '-F0011">\n'
        tmp += '''<title>Lorem Ipsum</title>
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
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-O00001-ControlsIndicators.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def operating_procedures(self, wpno, wp_title):
        """Function to create operating procedures WP."""
        tmp = f'<opusualwp chngno="0" wpno="{wpno}-' + self.sys_number + '">'
        tmp += f'''<wpidinfo>
            <maintlvl level="operator"/>
            <title>OPERATION UNDER USUAL CONDITIONS<?Pub _newline?>{wp_title}</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += f'''\n<opertsk>
            <initial>
                <proc>
                    <title>Lorem Ipsum</title>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua:
                        <seqlist>
                            <title>Lorem Ipsum</title>
                            <item>Lorem ipsum dolor sit amet</item>
                            <item>Lorem ipsum dolor sit amet:
                                <randlist bullet="yes">
                                    <item>Lorem ipsum dolor sit amet</item>
                                    <item>Lorem ipsum dolor sit amet</item>
                                </randlist>
                            </item>
                        </seqlist>
                    </para>
                </proc>
                <proc>
                    <title>Power On</title>
                    <step1>
                        <specpara>
                            <warning>
                                <icon-set boardno="Falling"/>
                                <trim.para>Using a stepladder is a falling risk. Use caution when operating on a stepladder. Failure to comply may result in death or serious injury to personnel. If injury occurs, seek immediate medical attention.</trim.para>
                            </warning>
                            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
                        </specpara>
                    </step1>
                    <figure id="{wpno}-{self.sys_number}-F0001">
                        <title>Lorem Ipsum</title>
                        <graphic boardno="PLACEHOLDER"/>
                    </figure>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>
                </proc>
            </initial>
        </opertsk>
        <opertsk>
            <oper>
                <proc>
                    <title>Perform Checkout Procedures</title>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>
                    <figure id="{wpno}-{self.sys_number}-F0002">
                        <title>Lorem Ipsum</title>
                        <graphic boardno="PLACEHOLDER"/>
                    </figure>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>
                    <figure id="{wpno}-{self.sys_number}-F0003">
                        <title>Lorem Ipsum</title>
                        <graphic boardno="PLACEHOLDER"/>
                    </figure>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>
                </proc>
            </oper>
        </opertsk>
        <opertsk>
            <prepforuse>
                <proc>
                    <title>Lorem Ipsum</title>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>
                    <figure id="{wpno}-{self.sys_number}-F0004">
                        <title>Lorem Ipsum</title>
                        <graphic boardno="PLACEHOLDER"/>
                    </figure>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>	
                </proc>
            </prepforuse>
        </opertsk>
        <opertsk>
            <prepmove>
                <proc>
                    <title>Lorem Ipsum</title>
                    <step1>
                        <specpara>
                            <warning>
                                <icon-set boardno="Hot_Area"/>
                                <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</trim.para>
                            </warning>
                            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                        </specpara>
                    </step1>
                    <figure id="{wpno}-{self.sys_number}-F0005">
                        <title>Lorem Ipsum</title>
                        <graphic boardno="PLACEHOLDER"/>
                    </figure>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>
                    <figure id="{wpno}-{self.sys_number}-F0006">
                        <title>Lorem Ipsum</title>
                        <graphic boardno="PLACEHOLDER"/>
                    </figure>
                </proc>
            </prepmove>
        </opertsk>
        <opertsk>
            <site>
                <proc>
                    <title/>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>
                    <step1>
                        <specpara>
                            <caution>
                                <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</trim.para>
                                <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</trim.para>
                            </caution>
                            <note>
                                <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</trim.para>
                            </note>
                            <para>
                                <randlist bullet="yes">
                                    <item>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</item>
                                    <item>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</item>
                                    <item>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</item>
                                </randlist>
                            </para>
                        </specpara>
                    </step1>
                    <figure id="{wpno}-{self.sys_number}-F0007">
                        <title>Lorem Ipsum</title>
                        <graphic boardno="PLACEHOLDER"/>
                    </figure>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>
                    <figure id="{wpno}-{self.sys_number}-F0008">
                        <title>Lorem Ipsum</title>
                        <graphic boardno="PLACEHOLDER"/>
                    </figure>
                    <step1>
                        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    </step1>
                </proc>
            </site>
        </opertsk>
    </opusualwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-{}-OperationUnderUsualConditions-{}.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def unusual_conditions(self, wpno):
        """Function to create the operating under unusual conditions section."""
        tmp = f'<opunuwp chngno="0" wpno="{wpno}-' + self.sys_number + '">'
        tmp += '''<wpidinfo>
            <maintlvl level="operator"/>
            <title>OPERATION UNDER UNUSUAL CONDITIONS</title>
        </wpidinfo>\n'''
        tmp += isb()
        tmp += f'''\n<opunutsk>
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
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-{}-OperationUnderUnusualConditions.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10
        
    def end(self):
        """Function to create Operator Instructions section end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        tmp = '</opim>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-OPER_INSTRUCTIONS_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
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
