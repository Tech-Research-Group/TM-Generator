"""PREVENTIVE MAINTENANCE CHECKS & SERVICES"""
import cfg
import math

class PMCS:
    """Class to create various types of WP's included in the PMCS section of a TM."""
    def __init__(self, manual_type, milstd, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.milstd = milstd
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function to create the PMCS start tags."""
        cfg.prefix_file = (math.floor(cfg.prefix_file/1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
    <mim chngno="0" revno="0" chap-toc="no">\n'''
        tmp += '\t<titlepg maintlvl="maintainer">\n'
        tmp += '\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')' + '</name>\n'
        tmp += '\t</titlepg>\n'
        tmp += '<pmcscategory>\n'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-PMCS_START.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcsintrowp(self):
        """ Function to create a PMCS intro WP """
        tmp = '<pmcsintrowp wpno="M00101-' + self.sys_number + '" chngno="0">'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''\t\t<title>INTRODUCTION</title>
    </wpidinfo>
    <intro>
        <para0>
            <title>GENERAL</title>
            <para>A Preventive Maintenance Checks and Services (PMCS) table is provided in <xref wpid="MXXXXX-XX-XXXX-XXX"/>. Following procedures in table ensures equipment is kept in good operating condition and ready for its primary mission.</para>
            <para>Always observe WARNINGS and CAUTIONS appearing in PMCS tables. WARNINGS and CAUTIONS appear before applicable procedures. These WARNINGS and CAUTIONS must be observed to prevent serious personal injury or to prevent equipment damage.</para>
        </para0>
    </intro>
    <para0>
        <title>INTRODUCTION</title>\n'''
        tmp += '\t\t<para>PMCS are performed to keep ' + self.sys_name + ' (' + self.sys_acronym + f') in good operating condition and ready for its primary mission. Checks are used to find, correct, and report problems. PMCS is performed every day {self.sys_name} is in operation, and is done according to PMCS table provided. Pay attention to WARNING, CAUTION, and NOTE statements. A WARNING indicates that someone could be hurt or killed. A CAUTION indicates that equipment could be damaged. A NOTE may make your maintenance or repair task easier.</para>\n'
        tmp += '''<para>Be sure to perform scheduled PMCS. Always perform PMCS in same order so it becomes a habit. With practice, you will quickly recognize problems with equipment.</para>
        <para>Use <extref docno="DA Form 5988-E" posttext=", Equipment Maintenance and Inspection Worksheet"/> or <extref docno="DA Form 2404" posttext=", Equipment Inspection and Maintenance Worksheet"/>, to record any discovered faults. Do not record faults that you fix.</para>
    </para0>
    <para0>
        <title>PMCS PROCEDURES</title>
        <para>Tables in <xref wpid="MXXXXX-XX-XXXX-XXX"/> list inspections and care required to be performed by operator to keep your equipment in good operating condition. It is arranged so that you can perform operational checks as you walk around equipment.</para>
        <para>Tables in <xref wpid="MXXXXX-XX-XXXX-XXX"/> list inspections and care required to be performed by maintainer.</para>
        <para>Tables in <xref wpid="MXXXXX-XX-XXXX-XXX"/> list inspections and care required to be performed by operator to keep Burner, Gas Heating in good operating condition.</para>
        <subpara1>
            <title>Item Number</title>
            <para>Indicates reference number. When completing <extref docno="DA Form 5988-E"/> or <extref docno="DA Form 2404"/>, include item number for item to check/service indicating a fault. Item numbers appear in the order you must perform checks/services listed.</para>
        </subpara1>
        <subpara1>
            <title>Interval</title>
            <para>Indicates when you must perform procedure in procedure column.</para>
            <para><randlist>
                    <item>Before - perform before equipment operation</item>
                    <item>During - perform during equipment operation</item>
                    <item>After - perform after equipment has been operated</item>
                    <item>Daily - perform daily</item>
                    <item>Weekly - perform every week </item>
                    <item>Monthly - perform every month</item>
                    <item>Quarterly - perform every 3 months</item>
                    <item>Semi-annually - perform every 6 months</item>
                    <item>Annually - perform every 12 months</item>
                </randlist>
            </para>
        </subpara1>
        <subpara1>
            <title>Item to Check/Service</title>
            <para>Indicates item to be checked or serviced.</para>
        </subpara1>
        <subpara1>
            <title>Procedure</title>
            <para>Indicates procedure you must perform on the item listed in Item to Check/Service column. You must perform procedure at time specified in Interval column.</para>
        </subpara1>
        <subpara1>
            <title>Equipment Not Ready / Available If:</title>
            <para>Indicates faults which will prevent your equipment from performing its primary mission. If you perform procedures listed in Procedure column which show faults listed in this column, do not operate equipment. Follow standard procedures for maintaining equipment or reporting equipment failure.</para>
        </subpara1>
        <subpara1>
            <title>Other special entries</title>
            <para>Observe all special information and notes that appear in PMCS tables.</para>
        </subpara1>
        <subpara1>
            <title>Cleaning</title>
            <para>Proper cleaning of SYSTEM NAME and its components is an integral part of maintenance. It helps prevent possible problems in the future, so make it a habit to clean (SYSTEM NAME) and its components whenever necessary.</para>
        </subpara1>
        <subpara1>
            <title>Corrosion Prevention and Control (CPC)</title>
            <para>Corrosion Prevention and Control (CPC) of Army materiel is a continuing concern. It is important that any corrosion problems with this item be reported so that problem can be corrected and improvements can be made to prevent problems in future items. Items that are non-mission capable as a result of corrosion shall be recorded as corrosion failure using code 170. Corrosion specifically occurs with metals. It is an electro-chemical process that causes degradation of metals. It is commonly caused by exposure to moisture, acids, bases, or salts. An example is the rusting of iron.</para>
            <para>Corrosion damage in metals can be seen, depending on metal, as tarnishing, pitting, fogging, surface residue, and/or cracking. Plastics, composites, and rubbers can also degrade. Degradation is caused by thermal (heat), oxidation (oxygen), solvation (solvents), or photolytic (light, typically UV) processes. Most common exposures are excessive heat or light. Damage from these processes will appear as cracking, softening, swelling, and/or breaking. <extref docno="SF Form 368" posttext=", Product Quality Deficiency Report"/> should be submitted to address specified in <extref docno="DA PAM 750-8" posttext=", The Army Maintenance Management System (TAMMS) User&apos;s Manual"/>. Refer to <xref wpid="G00001-10-5419-233"/> for full list of corrosion definitions.</para>
        </subpara1>
        <subpara1>
            <title>Fluid Leakage</title>
            <para>It is necessary for you to know how fluid leakage affects status of Cold Weather Equipment (CWE). Following are types/classes of leakage you need to know to be able to determine status of CWE. Learn these leakage definitions and remember: when in doubt, notify your supervisor. Equipment operation is allowed with minor leakage (Class I or II). Consideration must be given to fluid capacity in item/system being checked/inspected. When in doubt, notify your supervisor.</para>
            <para>
                When operating with Class I or II leaks, check fluid levels more frequently than required in PMCS. Class III leaks should be reported immediately to your supervisor.<randlist bullet="yes">
                    <item>Class I. Seepage of fluid (as indicated by wetness or discoloration) but not great enough to form drops.</item>
                    <item>Class II. Leakage of fluid great enough to form drops, but not enough to cause drops to drip from item being checked/inspected.</item>
                    <item>Class III. Leakage of fluid great enough to form drops that fall from item being checked/inspected.</item>
                </randlist> 			 			
            </para>
        </subpara1>
    </para0>
</pmcsintrowp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-M00101-PMCS-Introduction.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_before(self, wpno):
        """ Function to create a PMCS WP. """
        tmp = f'<pmcswp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''\t\t<title>Before Maintainer Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>'''
        tmp += isb()
        tmp += f'\t<pmcstable id="{wpno}-' + self.sys_number +'-T0001">\n'
        tmp += '''\t\t<title>Before Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Before</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para/>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
        <pmcs-entry>
            <itemno>2</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n'''

        if self.milstd != "2D":
            tmp += '''\t<mrplpart>
        <title>Lorem Ipsum</title>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
    </mrplpart>\n'''
        tmp += '</pmcswp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-PMCS-Before.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_during(self, wpno):
        """ Function to create a PMCS WP. """
        tmp = f'<pmcswp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''\t\t<title>During Maintainer Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>\n'''
        tmp += isb()
        tmp += f'\t<pmcstable id="{wpno}-' + self.sys_number +'-T0001">\n'
        tmp += '''\t\t<title>During Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>During</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para/>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
        <pmcs-entry>
            <itemno>2</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n'''

        if self.milstd != "2D":
            tmp += '''\t<mrplpart>
        <title>Lorem Ipsum</title>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
    </mrplpart>\n'''
        tmp += '</pmcswp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-PMCS-During.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_after(self, wpno):
        """ Function to create a PMCS WP. """
        tmp = f'<pmcswp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''\t\t<title>After Maintainer Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>\n'''
        tmp += isb()
        tmp += f'\t<pmcstable id="{wpno}-' + self.sys_number +'-T0001">\n'
        tmp += '''\t\t<title>After Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>After</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para/>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
        <pmcs-entry>
            <itemno>2</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n'''

        if self.milstd != "2D":
            tmp += '''\t<mrplpart>
        <title>Lorem Ipsum</title>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
    </mrplpart>\n'''
        tmp += '</pmcswp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-PMCS-After.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10
                
    def pmcs_daily(self, wpno):
        """ Function to create a PMCS WP. """
        tmp = f'<pmcswp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''\t\t<title>Daily Maintainer Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>'''
        tmp += isb()
        tmp += f'\t<pmcstable id="{wpno}-' + self.sys_number +'-T0001">\n'
        tmp += '''<title>Daily Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Daily</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para/>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
        <pmcs-entry>
            <itemno>2</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n'''

        if self.milstd != "2D":
            tmp += '''\t<mrplpart>
        <title>Lorem Ipsum</title>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
    </mrplpart>\n'''
        tmp += '</pmcswp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-PMCS-Daily.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_weekly(self, wpno):
        """ Function to create a PMCS WP. """
        tmp = f'<pmcswp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''\t\t<title>Weekly Maintainer Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>'''
        tmp += isb()
        tmp += f'\t<pmcstable id="{wpno}-' + self.sys_number +'-T0001">\n'
        tmp += '''<title>Weekly Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Weekly</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para/>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
        <pmcs-entry>
            <itemno>2</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n'''

        if self.milstd != "2D":
            tmp += '''\t<mrplpart>
        <title>Lorem Ipsum</title>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
    </mrplpart>\n'''
        tmp += '</pmcswp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-PMCS-Weekly.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_monthly(self, wpno):
        """ Function to create a PMCS WP. """
        tmp = f'<pmcswp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''\t\t<title>Monthly Maintainer Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>'''
        tmp += isb()
        tmp += f'\t<pmcstable id="{wpno}-' + self.sys_number +'-T0001">\n'
        tmp += '''<title>Monthly Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Monthly</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para/>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
        <pmcs-entry>
            <itemno>2</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n'''

        if self.milstd != "2D":
            tmp += '''\t<mrplpart>
        <title>Lorem Ipsum</title>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
    </mrplpart>\n'''
        tmp += '</pmcswp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-PMCS-Monthly.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10
    
    def pmcs_quarterly(self, wpno):
        """ Function to create a PMCS WP. """
        tmp = f'<pmcswp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''\t\t<title>Quarterly Maintainer Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>'''
        tmp += isb()
        tmp += f'\t<pmcstable id="{wpno}-' + self.sys_number +'-T0001">\n'
        tmp += '''<title>Quarterly Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Quarterly</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para/>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
        <pmcs-entry>
            <itemno>2</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n'''

        if self.milstd != "2D":
            tmp += '''\t<mrplpart>
        <title>Lorem Ipsum</title>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
    </mrplpart>\n'''
        tmp += '</pmcswp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-PMCS-Quarterly.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_semi_annually(self, wpno):
        """ Function to create a PMCS WP. """
        tmp = f'<pmcswp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''\t\t<title>Semi-annually Maintainer Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>'''
        tmp += isb()
        tmp += f'\t<pmcstable id="{wpno}-' + self.sys_number +'-T0001">\n'
        tmp += '''<title>Semi-annually Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Semi-annually</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para/>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
        <pmcs-entry>
            <itemno>2</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n'''

        if self.milstd != "2D":
            tmp += '''\t<mrplpart>
        <title>Lorem Ipsum</title>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
    </mrplpart>\n'''
        tmp += '</pmcswp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-PMCS-Semi-annually.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_annually(self, wpno):
        """ Function to create a PMCS WP. """
        tmp = f'<pmcswp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="maintainer"/>\n'
        tmp += '''\t\t<title>Annually Maintainer Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>'''
        tmp += isb()
        tmp += f'\t<pmcstable id="{wpno}-' + self.sys_number +'-T0001">\n'
        tmp += '''<title>Annually Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Annually</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para/>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
        <pmcs-entry>
            <itemno>2</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                    <eqpnotavail>
                        <trim.para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n'''

        if self.milstd != "2D":
            tmp += '''\t<mrplpart>
        <title>Lorem Ipsum</title>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
    </mrplpart>\n'''
        tmp += '</pmcswp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-PMCS-Annually.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self):
        """ Function to create the PMCS section end tags """
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        tmp = '\t</pmcscategory>\n'
        tmp += '</mim>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-PMCS_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
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

