"""CHAPTER 1"""

import datetime
import math

import cfg
import views.metadata as md


class Chapter1:
    """Class to create various types of WP's included in Chapter 1 of a TM."""

    date: str = datetime.datetime.today().strftime("%d %B %Y").upper()
    FPI_2C = "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN"
    FPI_2D = "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN"
    FPI_E = "-//USA-DOD//DTD -E TM Assembly REV E 8.0 20250417//EN"
    TAB_2 = "\t\t"
    TAB_3 = "\t\t\t"
    TAB_4 = "\t\t\t\t"
    TAB_5 = "\t\t\t\t\t"
    TAB_6 = "\t\t\t\t\t\t"
    TAB_7 = "\t\t\t\t\t\t\t"
    TAB_8 = "\t\t\t\t\t\t\t\t"

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
        """Function that creates Chapter 1 header of TM."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<gim revno="0" chngno="0" chap-toc="no">\n"""
        tmp += '\t<titlepg maintlvl="operator">\n'
        tmp += f"\t\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n"
        tmp += "\t\t</titlepg>\n"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + f" IADS/files/{cfg.prefix_file:05d}-CHAPTER_1_START.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def general_info(self) -> None:
        """Function that creates General Info WP in chapter 1 of TM."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE ginfowp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE ginfowp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE ginfowp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<ginfowp wpno="G00001-{self.tmno}" chngno="0" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("G00001", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'{self.TAB_2}<maintlvl level="operator"/>\n'
        tmp += f"{self.TAB_2}<title>GENERAL INFORMATION</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += "\t<scope>\n"
        tmp += f"{self.TAB_2}<title/>\n"
        tmp += f"{self.TAB_2}<para0>\n"
        tmp += f"{self.TAB_3}<title/>\n"
        tmp += (
            self.TAB_3
            + "<para>This technical manual provides operator instructions, troubleshooting procedures, Preventive Maintenance Checks and Services (PMCS), and maintenance procedures for the "
            + self.sys_name
            + "("
            + self.sys_acronym
            + ").</para>\n"
        )
        tmp += f"{self.TAB_2}</para0>\n"
        tmp += f"{self.TAB_2}<para0>\n"
        tmp += f"{self.TAB_3}<title>Model Number and Equipment Name </title>\n"
        tmp += f"{self.TAB_3}<para></para>\n"
        tmp += f"{self.TAB_3}<para></para>\n"
        tmp += f"{self.TAB_2}</para0>\n"
        tmp += f"{self.TAB_2}<para0>\n"
        tmp += f"{self.TAB_3}<title>Purpose of Equipment</title>\n"
        tmp += f"{self.TAB_3}<para></para>\n"
        tmp += f"{self.TAB_2}</para0>\n"
        tmp += "\t</scope>\n"
        tmp += """\t<mfrr>
        <title/>
        <mfrr.para service="army">Department of the Army forms and procedures used for equipment maintenance will be those prescribed by (as applicable) <extref docno="DA PAM 750-8" posttext=", The Army Maintenance Management System (TAMMS) Users Manual"/>, <extref docno="DA PAM 738-751" posttext=", Functional Users Manual for the Army Maintenance Management Systems - Aviation (TAMMS-A)"/>; or <extref docno="AR 700-138" posttext=", Army Logistics Readiness and Sustainability"/>.</mfrr.para>
    </mfrr>
    <eir>
        <title/>\n"""
        tmp += (
            self.TAB_2
            + "<para>If your "
            + self.sys_acronym
            + " needs improvement, let us know. Send us an EIR. You, the user, are the only one who can tell us what you do not like about your equipment. Let us know why you don't like the design or performance.</para>\n"
        )
        tmp += (
            self.TAB_2
            + """<para>All non-Aviation/Missile EIRs and PQDRs must be submitted through the Product Data Reporting and Evaluation Program (PDREP) Web site. The PDREP site is:
            <internet show.address="yes">
                <homepage protocol="https" uri="www.pdrep.csd.disa.mil/"/>
            </internet>.
        </para>
        <para>If you do not have internet access, you may submit your information using an <extref docno="SF 368" posttext=" (Product Quality Deficiency Report)"/>. You can send your <extref docno="SF 368"/> using email, regular mail, or fax using the addresses/fax numbers specified in <extref docno="DA PAM 750-8" posttext=", The Army Maintenance Management System (TAMMS) Users Manual"/>. We will send you a reply.</para>
    </eir>
    <cpcdata>
        <title/>
        <para>Corrosion prevention and control of Army materiel is a continuing concern. It is important that any corrosion problems with this item be reported so that the problem can be corrected and improvements can be made to prevent the problem in future items. The term "corrosion" means the deterioration of a material or its properties due to a reaction of that material with its chemical environment. An example is the rusting of iron.</para>
        <para>Corrosion damage in metals can be seen, depending on the metal, as tarnishing, pitting, fogging, surface residue, and/or cracking. Plastics, composites, and rubbers can also degrade (also considered to be corrosion based on the above definition of corrosion). Degradation is caused by thermal (heat), oxidation (oxygen), solvation (solvents), or photolytic (light, typically ultraviolet) processes.</para>
        <para>The most common exposures are excessive heat or light. Damage from these processes will appear as cracking, softening, swelling, and/or breaking. The US Army has defined the following nine (9) forms of corrosion used to evaluate the deterioration of metals. These shall be used when evaluating and documenting corrosion.<randlist bullet="no">
                <item>UNIFORM (or general attack): Affects a large area of exposed metal surface, like rust on steel or tarnish on silver. It gradually reduces the thickness of the metal until it fails.</item>
                <item>CREVICE: Occurs in crevices created by rubber seals, gaskets, bolt heads, lap joints, dirt or other surface deposits. It will develop anywhere moisture or other corrosive agents are trapped and unable to drain or evaporate.</item>
                <item>SELECTIVE LEACHING: One element, usually the anodic element of an alloy, corrodes away, leaving the cathodic element. This can create holes in metal.</item>
                <item>INTERGRANULAR: Metal deterioration caused by corrosion on the bonds between or across the grain boundaries of the metal. The metal will appear to be peeling off in sheets, flaking, or being pushed apart by layers. A particular type of intergranular corrosion is exfoliation.</item>
                <item>PITTING: This can result from conditions similar to those for crevice corrosion. Pits can develop on various materials due to their composition. Weapon boxes are big victims of pitting.</item>
                <item>EROSION: Results when a moving fluid (liquid or gas) flows across a metal surface, particularly when solid particles are present in the fluid. Corrosion actually occurs on the surface of the metal, but the moving fluid washes away the corrosion and exposes a new metal surface, which also corrodes.</item>
                <item>FRETTING: Occurs as a result of small, repetitive movements (e.g., vibration) between two surfaces in contact with each other. It's usually identified by a black powder corrosion product or pits on the surface.</item>
                <item>GALVANIC: Occurs when two different types of metal come in contact with each other, like steel bolts on aluminum, for example. This is a common problem on aircraft because of their mix of metals.</item>
                <item>STRESS: Term used to describe corrosion cracking and corrosion fatigue.</item>
            </randlist>
        </para>
        <para>Where an item is not ready/available due to one of these forms of corrosion, it shall be recorded as a corrosion failure in the inspection record and the appropriate code (170) for corrosion shall be used when requesting/performing maintenance.</para>
        <para>If a corrosion problem is identified, it can be reported as an EIR or PQDR. Use of key words such as "corrosion," "rust," "deterioration," or "cracking" will ensure that the information is identified as a CPC problem. <extref docno="SF Form 368" posttext=", Product Quality Deficiency Report"/> should be submitted to the address specified in <extref docno="DA PAM 750-8" posttext=", The Army Maintenance Management System (TAMMS) Users Manual"/>.</para>
    </cpcdata>
    <destructmat>
        <title/>
        <para></para>
    </destructmat>
    <pssref>
        <title/>
        <para></para>
    </pssref>\n"""
        )

        if self.mil_std == "2C" or self.mil_std == "2D":
            tmp += """\t<transportability>
        <title>TRANSPORTABILITY GUIDANCE</title>
        <para>Instructions for transportability guidence can be found in <xref wpid="MXXXXX-XX-XXXX-XXX"/>.</para>
    </transportability>\n"""
        tmp += """\t<nomenreflist>
        <title/>
        <para>"""
        tmp += '<table id="G00001-' + self.tmno + '-T0001">'
        tmp += """<title>Nomenclature Cross-Reference List</title>
                <tgroup cols="2">
                    <colspec colname="col1"/>
                    <colspec colname="col2"/>
                    <thead>
                        <row>
                            <entry>Common Name</entry>
                            <entry>Official Nomenclature</entry>
                        </row>
                    </thead>
                    <tbody>
                        <row>
                            <entry></entry>
                            <entry></entry>
                        </row>
                        <row>
                            <entry></entry>
                            <entry></entry>
                        </row>
                        <row>
                            <entry></entry>
                            <entry></entry>
                        </row>
                    </tbody>
                </tgroup>
            </table>
        </para>
    </nomenreflist>
    <loa>
        <title/>
        <para>"""
        tmp += '<table id="G00001-' + self.tmno + '-T0002">'
        tmp += """<title>List of Acronyms and Abbreviations</title>
                <tgroup cols="2">
                    <colspec colname="col1"/>
                    <colspec colname="col2"/>
                    <thead>
                        <row>
                            <entry>Acronym/Abbreviation</entry>
                            <entry>Meaning</entry>
                        </row>
                    </thead>
                    <tbody>
                        <row>
                            <entry></entry>
                            <entry></entry>
                        </row>
                        <row>
                            <entry></entry>
                            <entry></entry>
                        </row>
                        <row>
                            <entry></entry>
                            <entry></entry>
                        </row>
                    </tbody>
                </tgroup>
            </table>
        </para>
    </loa>\n"""

        if self.manual_type != "-10":
            tmp += """\t<qual.mat.info>
        <title>Quality of Material</title>
        <para>
            Material used for replacement, repair, or modification must meet the requirements of this <extref docno="TM 10-5419-224-13&amp;P"/>. If quality of material requirements are not stated in this <extref docno="TM 10-5419-224-13&amp;P"/>, the material must meet the requirements of the drawings, standards, specifications, or approved engineering change proposals applicable to the subject equipment.
        </para>
    </qual.mat.info>\n"""

        tmp += """\t<iuid>
        <title>ITEM UNIQUE IDENTIFICATION</title>
        <para>This equipment and/or its components/parts are marked with item unique identification (IUID) markings such as data plates, decals, or etchings. These markings must be scanned during performance of procedures to remove and replace items marked or when turning in items or receiving them from supply or another unit. For information on location of the IUID marking for the end item, refer to the decal/data plate guide contained in the operator manual for the equipment.</para>
    </iuid>\n"""

        if self.mil_std == "2D":
            tmp += """\t<mrpref>
        <title>MANDATORY REPLACEMENT PARTS</title>
        <!-- This paragraph shall reference the mandatory replacement parts list work package,
                if it exists. If there are no MRPs for equipment covered by the manual, insert
                the following statement in this paragraph:
        -->
        <para>There are no mandatory replacement parts for (insert equipment name).</para>
    </mrpref>\n"""

        if self.manual_type != "-10":
            tmp += """\t<supdata>
        <title>SUPPORTING INFORMATION FOR COMMON TOOLS, REPAIR PARTS, SPECIAL TOOLS, TMDE, AND SUPPORT EQUIPMENT</title>
        <para>For authorized common tools and equipment, refer to the Modified Table of Organization and Equipment (MTOE), <extref docno="50-970" pretext="Common Table of Allowances (CTA) " posttext=", Expendable/Durable Items (Except: Medical, Class V, Repair Parts, and Heraldic Items)"/>; <extref docno="50-909" pretext="CTA " posttext=", Field and Garrison Furnishings and Equipment"/>; or <extref docno="8-100" pretext="CTA " posttext=", Army Medical Department Expendable/Durable Items"/>; as applicable to your unit.</para>
        <para>Special tools, TMDE, and support equipment are required. The Maintenance Allocation Chart (MAC) Introduction and MAC can be found in <xref wpid="SXXXXX-XX-XXXX-XXX"/> and <xref wpid="SXXXXX-XX-XXXX-XXX"/>, respectively.</para>
        <para>Repair parts are listed and illustrated in <xref wpid="RXX-XX-XXXX-XXX"/> through <xref wpid="RXXXXX-XX-XXXX-XXX"/> of this manual.</para>
    </supdata>"""
        tmp += "</ginfowp>\n"
        file_name = f"{cfg.prefix_file:05d}-G00001-General Information.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.chapter1.append(file_name)
        cfg.prefix_file += 10

    def equipment_description(self) -> None:
        """Function that create Equipment Description and Data section of Chapter 1 in TM Shell"""
        tmp = '\n<?xml version="1.0" encoding="UTF-8"?>\n'

        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE descwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE descwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE descwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<descwp wpno="G00002-{self.tmno}" chngno="0" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("G00002", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'{self.TAB_2}<maintlvl level="operator"/>\n'
        tmp += f"{self.TAB_2}<title>EQUIPMENT DESCRIPTION AND DATA</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += "\t<eqpinfo>\n"
        tmp += f"{self.TAB_2}<title>EQUIPMENT CHARACTERISTICS, CAPABILITIES, AND FEATURES</title>\n"
        tmp += f"{self.TAB_2}<eqpdesc>\n"
        tmp += f"{self.TAB_3}<title>Characteristics</title>\n"
        tmp += f"{self.TAB_3}<para>\n"
        tmp += f'{self.TAB_4}<figure id="G00002-{self.tmno}-F0001">\n'
        tmp += f"{self.TAB_5}<title>{self.sys_acronym} Deployed</title>\n"
        tmp += f'{self.TAB_5}<graphic boardno="PLACEHOLDER"/>\n'
        tmp += f"{self.TAB_4}</figure>\n"
        tmp += f"{self.TAB_3}</para>\n"
        tmp += f"{self.TAB_2}</eqpdesc>\n"
        tmp += f"{self.TAB_2}<eqpdesc>\n"
        tmp += f"{self.TAB_3}<title>Capabilities and Features</title>\n"
        tmp += f"{self.TAB_3}<para>\n"
        tmp += f'{self.TAB_4}<randlist bullet="yes">\n'
        tmp += f"{self.TAB_5}<item></item>\n"
        tmp += f"{self.TAB_5}<item></item>\n"
        tmp += f"{self.TAB_4}</randlist>\n"
        tmp += f"{self.TAB_3}</para>\n"
        tmp += f"{self.TAB_2}</eqpdesc>\n"
        tmp += "\t</eqpinfo>\n"
        tmp += "\t<locdesc>\n"
        tmp += (
            f"{self.TAB_2}<title>LOCATION AND DESCRIPTION OF MAJOR COMPONENTS</title>\n"
        )
        tmp += (
            self.TAB_2
            + "<para>Refer to the following technical manuals for description of end items that are components of "
            + self.sys_acronym
            + ":\n"
        )
        tmp += f'{self.TAB_3}<randlist bullet="yes">\n'
        tmp += f"{self.TAB_4}<item></item>\n"
        tmp += f"{self.TAB_4}<item></item>\n"
        tmp += f"{self.TAB_3}</randlist>\n"
        tmp += f"{self.TAB_2}</para>\n"
        tmp += f"{self.TAB_2}<comp-item>\n"
        tmp += f"{self.TAB_3}<para>\n"
        tmp += f'{self.TAB_4}<figure id="G00002-{self.tmno}-F0005">\n'
        tmp += f"{self.TAB_5}<title>{self.sys_acronym} Exterior (Front)</title>\n"
        tmp += f'{self.TAB_5}<graphic boardno="PLACEHOLDER"/>\n'
        tmp += f"{self.TAB_4}</figure>\n"
        tmp += f'{self.TAB_4}<table id="G00002-{self.tmno}-T0004">\n'
        tmp += f"{self.TAB_5}<title>{self.sys_acronym}</title>\n"
        tmp += f'{self.TAB_5}<tgroup cols="3">\n'
        tmp += f'{self.TAB_6}<colspec colname="col1" colwidth="0.30*"/>\n'
        tmp += f'{self.TAB_6}<colspec colname="col2" colwidth="0.40*"/>\n'
        tmp += f'{self.TAB_6}<colspec colname="col3" colwidth="2.30*"/>\n'
        tmp += f"{self.TAB_6}<thead>\n"
        tmp += f"{self.TAB_7}<row>\n"
        tmp += f"{self.TAB_8}<entry>CALLOUT</entry>\n"
        tmp += f"{self.TAB_8}<entry>ITEM</entry>\n"
        tmp += f"{self.TAB_8}<entry>DESCRIPTION</entry>\n"
        tmp += f"{self.TAB_7}</row>\n"
        tmp += f"{self.TAB_6}</thead>\n"
        tmp += f"{self.TAB_6}<tbody>\n"
        tmp += f"{self.TAB_7}<row>\n"
        tmp += f"{self.TAB_8}<entry>1</entry>\n"
        tmp += f"{self.TAB_8}<entry></entry>\n"
        tmp += f"{self.TAB_8}<entry></entry>\n"
        tmp += f"{self.TAB_7}</row>\n"
        tmp += f"{self.TAB_7}<row>\n"
        tmp += f"{self.TAB_8}<entry>2</entry>\n"
        tmp += f"{self.TAB_8}<entry></entry>\n"
        tmp += f"{self.TAB_8}<entry></entry>\n"
        tmp += f"{self.TAB_7}</row>\n"
        tmp += f"{self.TAB_6}</tbody>\n"
        tmp += f"{self.TAB_5}</tgroup>\n"
        tmp += f"{self.TAB_4}</table>\n"
        tmp += f"{self.TAB_3}</para>\n"
        tmp += f"{self.TAB_2}</comp-item>\n"
        tmp += f"{self.TAB_2}<comp-item>\n"
        tmp += f"{self.TAB_3}<para></para>\n"
        tmp += f"{self.TAB_3}<para>\n"
        tmp += f'{self.TAB_4}<figure id="G00002-{self.tmno}-F0006">\n'
        tmp += f"{self.TAB_5}<title></title>\n"
        tmp += f'{self.TAB_5}<graphic boardno="PLACEHOLDER"/>\n'
        tmp += f"{self.TAB_4}</figure>\n"
        tmp += f'{self.TAB_4}<table id="G00002-{self.tmno}-T0005">\n'
        tmp += f"{self.TAB_5}<title></title>\n"
        tmp += f'{self.TAB_5}<tgroup cols="3">\n'
        tmp += f'{self.TAB_6}<colspec colname="col1" colwidth="*"/>\n'
        tmp += f'{self.TAB_6}<colspec colname="col2" colwidth="*"/>\n'
        tmp += f'{self.TAB_6}<colspec colname="col3" colwidth="*"/>\n'
        tmp += f"{self.TAB_6}<thead>\n"
        tmp += f"{self.TAB_7}<row>\n"
        tmp += f"{self.TAB_8}<entry>CALLOUT</entry>\n"
        tmp += f"{self.TAB_8}<entry>ITEM</entry>\n"
        tmp += f"{self.TAB_8}<entry>DESCRIPTION</entry>\n"
        tmp += f"{self.TAB_7}</row>\n"
        tmp += f"{self.TAB_6}</thead>\n"
        tmp += f"{self.TAB_6}<tbody>\n"
        tmp += f"{self.TAB_7}<row>\n"
        tmp += f"{self.TAB_8}<entry>1</entry>\n"
        tmp += f"{self.TAB_8}<entry></entry>\n"
        tmp += f"{self.TAB_8}<entry></entry>\n"
        tmp += f"{self.TAB_7}</row>\n"
        tmp += f"{self.TAB_7}<row>\n"
        tmp += f"{self.TAB_8}<entry>2</entry>\n"
        tmp += f"{self.TAB_8}<entry></entry>\n"
        tmp += f"{self.TAB_8}<entry></entry>\n"
        tmp += f"{self.TAB_7}</row>\n"
        tmp += f"{self.TAB_7}<row>\n"
        tmp += f"{self.TAB_8}<entry>3</entry>\n"
        tmp += f"{self.TAB_8}<entry></entry>\n"
        tmp += f"{self.TAB_8}<entry></entry>\n"
        tmp += f"{self.TAB_7}</row>\n"
        tmp += f"{self.TAB_7}<row>\n"
        tmp += f"{self.TAB_8}<entry>4</entry>\n"
        tmp += f"{self.TAB_8}<entry></entry>\n"
        tmp += f"{self.TAB_8}<entry></entry>\n"
        tmp += f"{self.TAB_7}</row>\n"
        tmp += f"{self.TAB_6}</tbody>\n"
        tmp += f"{self.TAB_5}</tgroup>\n"
        tmp += f"{self.TAB_4}</table>\n"
        tmp += f"{self.TAB_3}</para>\n"
        tmp += f"{self.TAB_2}</comp-item>\n"
        tmp += "\t</locdesc>\n"

        if self.mil_std == "2C":
            tmp += "\t<eqpdiff>\n"
            tmp += f"{self.TAB_2}<title>EQUIPMENT DIFFERENCES</title>\n"
            tmp += f"{self.TAB_2}<para></para>\n"
            tmp += "\t</eqpdiff>\n"

        tmp += "\t<eqpdata>\n"
        tmp += f"{self.TAB_2}<title>EQUIPMENT DATA</title>\n"
        tmp += f"{self.TAB_2}<para></para>\n"
        tmp += f"{self.TAB_2}<para>\n"
        tmp += f'{self.TAB_3}<table id="G00002-{self.tmno}-T0020">\n'
        tmp += (
            self.TAB_4
            + "<title>"
            + self.sys_acronym
            + " Support Equipment Data</title>\n"
        )
        tmp += f'{self.TAB_4}<tgroup cols="2">\n'
        tmp += f'{self.TAB_5}<colspec colname="col1"/>\n'
        tmp += f'{self.TAB_5}<colspec colname="col2"/>\n'
        tmp += f"{self.TAB_5}<tbody>\n"
        tmp += f"{self.TAB_6}<row>\n"
        tmp += (
            self.TAB_7
            + '<entry colsep="0"><emphasis emph="bold">Dimensions:</emphasis></entry>\n'
        )
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_6}</row>\n"
        tmp += f"{self.TAB_6}<row>\n"
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_6}</row>\n"
        tmp += f"{self.TAB_6}<row>\n"
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_6}</row>\n"

        tmp += f"{self.TAB_6}<row>\n"
        tmp += (
            self.TAB_7
            + '<entry colsep="0"><emphasis emph="bold">Environmental Requirements:</emphasis></entry>\n'
        )
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_6}</row>\n"
        tmp += f"{self.TAB_6}<row>\n"
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_6}</row>\n"
        tmp += f"{self.TAB_6}<row>\n"
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_6}</row>\n"

        tmp += f"{self.TAB_6}<row>\n"
        tmp += (
            self.TAB_7
            + '<entry colsep="0"><emphasis emph="bold">References:</emphasis></entry>\n'
        )
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_6}</row>\n"
        tmp += f"{self.TAB_6}<row>\n"
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_6}</row>\n"
        tmp += f"{self.TAB_6}<row>\n"
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_7}<entry></entry>\n"
        tmp += f"{self.TAB_6}</row>\n"

        tmp += f"{self.TAB_5}</tbody>\n"
        tmp += f"{self.TAB_4}</tgroup>\n"
        tmp += f"{self.TAB_3}</table>\n"
        tmp += f"{self.TAB_2}</para>\n"

        tmp += f"{self.TAB_2}<para0>\n"
        tmp += f"{self.TAB_3}<title>Performance Data</title>\n"
        tmp += f"{self.TAB_3}<para>Operating the {self.sys_acronym} outside of these specifications may cause equipment damage due to freezing or overheating.</para>\n"
        tmp += f"{self.TAB_2}</para0>\n"
        tmp += "\t</eqpdata>\n"
        tmp += "</descwp>\n"
        file_name = f"{cfg.prefix_file:05d}-G00002-Equipment Description and Data.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.chapter1.append(file_name)
        cfg.prefix_file += 10

    def theory_operations(self) -> None:
        """Function to create the theory of operations section"""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE thrywp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE thrywp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE thrywp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<thrywp wpno="G00003-{self.tmno}" chngno="0" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("G00003", self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'{self.TAB_2}<maintlvl level="operator"/>\n'
        tmp += (
            self.TAB_2
            + """<title>THEORY OF OPERATION</title>
    </wpidinfo>
    <intro>
        <para0>
            <title>Introduction</title>\n"""
        )
        tmp += (
            self.TAB_2
            + "<para>The "
            + self.sys_name
            + " is ("
            + self.sys_acronym
            + ') (<xref figid="G00003-'
            + self.tmno
            + '-F0001"/>) consists of ... '
            + "The "
            + self.sys_acronym
            + " theory of operation by major component is described in the following paragraphs.</para>\n"
        )
        tmp += f"{self.TAB_2}<para>\n"
        tmp += f'{self.TAB_3}<figure id="G00003-{self.tmno}-F0001">\n'
        tmp += (
            self.TAB_4
            + """<title></title>
                        <graphic boardno="PLACEHOLDER"/>
                    </figure>
                </para>
            </para0>
        </intro>
        <systhry>
            <title></title>
            <para></para>d
        </systhry>
        <systhry>
            <title></title>
            <para></para>
            <para>\n"""
        )
        tmp += f'{self.TAB_3}<figure id="G00003-{self.tmno}-F0002">\n'
        tmp += (
            self.TAB_4
            + """<title></title>
                <graphic boardno="PLACEHOLDER"/>
            </figure>
        </para>
    </systhry>
</thrywp>"""
        )
        file_name = f"{cfg.prefix_file:05d}-G00003-Theory Of Operations.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.chapter1.append(file_name)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create Chapter 1 end tags"""
        tmp = "</gim>"
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + f" IADS/files/{cfg.prefix_file:05d}-CHAPTER_1_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
