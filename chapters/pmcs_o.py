"""PREVENTIVE MAINTENANCE CHECKS & SERVICES"""

import datetime
import math

import cfg
import views.isb as isb
import views.metadata as md


class PMCS:
    """Class to create various types of WP's included in the PMCS section of a TM."""

    date: str = datetime.datetime.today().strftime("%d %B %Y").upper()
    FPI_2C = "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN"
    FPI_2D = "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN"
    FPI_E = "-//USA-DOD//DTD -E TM Assembly REV E 8.0 20250417//EN"

    def __init__(
        self, manual_type, mil_std, sys_acronym, sys_name, tmno, save_path
    ) -> None:
        self.manual_type = manual_type
        self.mil_std = mil_std
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.tmno = tmno
        self.save_path = save_path

    def start(self) -> None:
        """Function to create the PMCS start tags."""
        # cfg.prefix_file = math.floor(cfg.prefix_file / 1000) * 1000
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
    <mim chngno="0" revno="0" chap-toc="no">\n"""
        tmp += '\t<titlepg maintlvl="operator">\n'
        tmp += f"\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n"
        tmp += "\t</titlepg>\n" + "<pmcscategory>\n" ""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-OPERATOR_PMCS_START.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcsintrowp(self) -> None:
        """Function to create a PMCS intro WP"""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE pmcsintrowp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE pmcsintrowp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE pmcsintrowp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += '<pmcsintrowp wpno="C00001-' + self.tmno + '" chngno="0" security="cui">'

        # WP.METADATA Section
        tmp += md.show("pmcsintrowp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="operator"/>\n'
        tmp += """\t\t<title>INTRODUCTION</title>
    </wpidinfo>
    <intro>
        <para0>
            <title>GENERAL</title>
            <para>A Preventive Maintenance Checks and Services (PMCS) table is provided in <xref wpid=""/>. Following procedures in table ensures equipment is kept in good operating condition and ready for its primary mission.</para>
            <para>Always observe WARNINGS and CAUTIONS appearing in PMCS tables. WARNINGS and CAUTIONS appear before applicable procedures. These WARNINGS and CAUTIONS must be observed to prevent serious personal injury or to prevent equipment damage.</para>
        </para0>
    </intro>
    <para0>
        <title>INTRODUCTION</title>"""
        tmp += f"<para>PMCS are performed to keep {self.sys_name} ({self.sys_acronym}) in good operating condition and ready for its primary mission. Checks are used to find, correct, and report problems. PMCS is performed every day (insert equipment name) is in operation, and is done according to PMCS table provided. Pay attention to WARNING, CAUTION, and NOTE statements. A WARNING indicates that someone could be hurt or killed. A CAUTION indicates that equipment could be damaged. A NOTE may make your maintenance or repair task easier.</para>\n"

        tmp += """<para>Be sure to perform scheduled PMCS. Always perform PMCS in same order so it becomes a habit. With practice, you will quickly recognize problems with equipment.</para>
        <para>Use <extref docno="DA Form 5988-E" posttext=", Equipment Maintenance and Inspection Worksheet"/> or <extref docno="DA Form 2404" posttext=", Equipment Inspection and Maintenance Worksheet"/>, to record any discovered faults. Do not record faults that you fix.</para>
    </para0>
    <para0>
        <title>PMCS PROCEDURES</title>
        <para>Tables in <xref wpid=""/> list inspections and care required to be performed by operator to keep your equipment in good operating condition. It is arranged so that you can perform operational checks as you walk around equipment.</para>
        <para>Tables in <xref wpid=""/> list inspections and care required to be performed by maintainer.</para>
        <para>Tables in <xref wpid=""/> list inspections and care required to be performed by operator to keep Burner, Gas Heating in good operating condition.</para>
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
            <para>Proper cleaning of (insert equipment name) and its components is an integral part of maintenance. It helps prevent possible problems in the future, so make it a habit to clean (insert equipment name) and its components whenever necessary.</para>
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
</pmcsintrowp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-C00001-PMCS Introduction.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_before(self, wpno) -> None:
        """Function to create a PMCS WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<pmcswp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("pmcswp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="operator"/>\n'
        tmp += """\t\t<title>Before Operator Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>"""
        tmp += isb.show()
        tmp += f'\t<pmcstable id="{wpno}-{self.tmno}-T0001">\n'
        tmp += """\t\t<title>Before Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Before</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
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
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n"""

        tmp += "</pmcswp>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-PMCS Before.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_during(self, wpno) -> None:
        """Function to create a PMCS WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<pmcswp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("pmcswp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="operator"/>\n'
        tmp += """\t\t<title>During Operator Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += f'\t<pmcstable id="{wpno}-{self.tmno}-T0001">\n'
        tmp += """\t\t<title>During Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>During</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
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
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n"""

        tmp += "</pmcswp>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-PMCS During.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_after(self, wpno) -> None:
        """Function to create a PMCS WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<pmcswp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("pmcswp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="operator"/>\n'
        tmp += """\t\t<title>After Operator Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += f'\t<pmcstable id="{wpno}-{self.tmno}-T0001">\n'
        tmp += """\t\t<title>After Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>After</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
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
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n"""

        tmp += "</pmcswp>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-PMCS After.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_daily(self, wpno) -> None:
        """Function to create a PMCS WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<pmcswp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("pmcswp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="operator"/>\n'
        tmp += """\t\t<title>Daily Operator Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>"""
        tmp += isb.show()
        tmp += f'\t<pmcstable id="{wpno}-{self.tmno}-T0001">\n'
        tmp += """<title>Daily Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Daily</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
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
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n"""

        tmp += "</pmcswp>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-PMCS Daily.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_weekly(self, wpno) -> None:
        """Function to create a PMCS WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<pmcswp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("pmcswp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="operator"/>\n'
        tmp += """\t\t<title>Weekly Operator Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>"""
        tmp += isb.show()
        tmp += f'\t<pmcstable id="{wpno}-{self.tmno}-T0001">\n'
        tmp += """<title>Weekly Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Weekly</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
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
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para> </trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n"""

        tmp += "</pmcswp>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-PMCS Weekly.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_monthly(self, wpno) -> None:
        """Function to create a PMCS WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<pmcswp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("pmcswp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="operator"/>\n'
        tmp += """\t\t<title>Monthly Operator Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>"""
        tmp += isb.show()
        tmp += f'\t<pmcstable id="{wpno}-{self.tmno}-T0001">\n'
        tmp += """<title>Monthly Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Monthly</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
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
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para> </trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n"""

        tmp += "</pmcswp>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-PMCS Monthly.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_quarterly(self, wpno) -> None:
        """Function to create a PMCS WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<pmcswp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("pmcswp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="operator"/>\n'
        tmp += """\t\t<title>Quarterly Operator Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>"""
        tmp += isb.show()
        tmp += f'\t<pmcstable id="{wpno}-{self.tmno}-T0001">\n'
        tmp += """<title>Quarterly Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Quarterly</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
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
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n"""

        tmp += "</pmcswp>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-PMCS Quarterly.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_semi_annually(self, wpno) -> None:
        """Function to create a PMCS WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<pmcswp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("pmcswp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="operator"/>\n'
        tmp += """\t\t<title>Semi-annually Operator Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>"""
        tmp += isb.show()
        tmp += f'\t<pmcstable id="{wpno}-{self.tmno}-T0001">\n'
        tmp += """<title>Semi-annually Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Semi-annually</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
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
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>\n"""

        tmp += "</pmcswp>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-PMCS Semi-annually.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pmcs_annually(self, wpno) -> None:
        """Function to create a PMCS WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE pmcswp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<pmcswp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("pmcswp", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += '\t\t<maintlvl level="operator"/>\n'
        tmp += """\t\t<title>Annually Operator Preventive Maintenance Checks and Services (PMCS) Procedures</title>
    </wpidinfo>"""
        tmp += isb.show()
        tmp += f'\t<pmcstable id="{wpno}-{self.tmno}-T0001">\n'
        tmp += """<title>Annually Preventive Maintenance Checks and Services Procedures</title>
        <pmcs-intervals>
            <interval>Annually</interval>
        </pmcs-intervals>
        <pmcs-entry>
            <itemno>1</itemno>
            <interval></interval>
            <checked></checked>
            <pmcsproc>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
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
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
                <pmcsstep1>
                    <para></para>
                    <eqpnotavail>
                        <trim.para></trim.para>
                    </eqpnotavail>
                </pmcsstep1>
            </pmcsproc>
        </pmcs-entry>
    </pmcstable>
<pmcswp>\n"""

        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-PMCS Annually.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create the PMCS section end tags"""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = "\t</pmcscategory>\n" + "</mim>"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-OPERATOR_PMCS_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
