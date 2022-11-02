"""CHAPTER 1"""
import math
from dotenv import dotenv_values
import cfg

class Chapter1:
    """Class to create various types of WP's included in Chapter 1 of a TM."""
    config = dotenv_values(".env")  # take environment variables from .env.
    lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    TAB_2 = '\t\t'
    TAB_3 = '\t\t\t'
    TAB_4 = '\t\t\t\t'
    TAB_5 = '\t\t\t\t\t'
    TAB_6 = '\t\t\t\t\t\t'
    TAB_7 = '\t\t\t\t\t\t\t'
    TAB_8 = '\t\t\t\t\t\t\t\t'

    def __init__(self, config, manual_type, mil_std, sys_acronym, sys_name, sys_number, save_path):
        self.config = config
        self.manual_type = manual_type
        self.mil_std = mil_std
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function that creates chapter 1 header of TM."""
        cfg.prefix_file += 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
<gim revno="0" chngno="0" chap-toc="no">\n'''
        tmp += '<titlepg maintlvl="operator">\n'
        tmp += '\t\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')' + '</name>\n'
        tmp += '\t\t</titlepg>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + ' WIP/{:05d}-CHAP_1_START.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def general_info(self):
        """Function that creates General Info WP in chapter 1 of TM."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += '<ginfowp wpno="G00001-' + self.sys_number + '" chngno="0">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += self.TAB_2 + '<maintlvl level="operator"/>\n'
        tmp += self.TAB_2 + '<title>GENERAL INFORMATION</title>\n'
        tmp += '\t</wpidinfo>\n'
        tmp += '\t<scope>\n'
        tmp += self.TAB_2 + '<title/>\n'
        tmp += self.TAB_2 + '<para0>\n'
        tmp += self.TAB_3 + '<title/>\n'
        tmp += self.TAB_3 + \
            '<para>This technical manual provides operator instructions, troubleshooting procedures, Preventive Maintenance Checks and Services (PMCS), and maintenance procedures for the ' + \
            self.sys_name + "(" + self.sys_acronym + ').</para>\n'
        tmp += self.TAB_2 + '</para0>\n'
        tmp += self.TAB_2 + '<para0>\n'
        tmp += self.TAB_3 + '<title>Model Number and Equipment Name </title>\n'
        tmp += self.TAB_3 + '<para>' + self.lorem_ipsum + '</para>\n'
        tmp += self.TAB_3 + '<para>' + self.lorem_ipsum + '</para>\n'
        tmp += self.TAB_2 + '</para0>\n'
        tmp += self.TAB_2 + '<para0>\n'
        tmp += self.TAB_3 + '<title>Purpose of Equipment</title>\n'
        tmp += self.TAB_3 + '<para>' + self.lorem_ipsum + '</para>\n'
        tmp += self.TAB_2 + '</para0>\n'
        tmp += '\t</scope>\n'
        tmp += '''\t<mfrr>
        <title/>
        <mfrr.para service="army">Department of the Army forms and procedures used for equipment maintenance will be those prescribed by (as applicable) <extref docno="DA PAM 750-8" posttext=", The Army Maintenance Management System (TAMMS) Users Manual"/>, <extref docno="DA PAM 738-751" posttext=", Functional Users Manual for the Army Maintenance Management Systems - Aviation (TAMMS-A)"/>; or <extref docno="AR 700-138" posttext=", Army Logistics Readiness and Sustainability"/>.</mfrr.para>
    </mfrr>
    <eir>
        <title/>\n'''
        tmp += self.TAB_2 + "<para>If your " + self.sys_acronym + \
            " needs improvement, let us know. Send us an EIR. You, the user, are the only one who can tell us what you do not like about your equipment. Let us know why you don't like the design or performance.</para>\n"
        tmp += self.TAB_2 + '''<para>All non-Aviation/Missile EIRs and PQDRs must be submitted through the Product Data Reporting and Evaluation Program (PDREP) Web site. The PDREP site is: 
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
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
    </destructmat>
    <pssref>
        <title/>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
    </pssref>\n'''

        if self.mil_std == '2C' or self.mil_std == '2D':
            tmp += '''\t<transportability>
        <title>TRANSPORTABILITY GUIDANCE</title>
        <para>Instructions for transportability guidence can be found in <xref wpid="MXXXXX-XX-XXXX-XXX"/>.</para>
    </transportability>\n'''
        tmp += '''\t<nomenreflist>
        <title/>
        <para>'''
        tmp += '<table id="G00001-' + self.sys_number + '-T0001">'
        tmp += '''<title>Nomenclature Cross-Reference List</title>
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
        <para>'''
        tmp += '<table id="G00001-' + self.sys_number + '-T0002">'
        tmp += '''<title>List of Acronyms and Abbreviations</title>
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
    </loa>\n'''

        if self.manual_type != '-10':
            tmp += '''\t<qual.mat.info>
        <title>Quality of Material</title>
        <para>
            Material used for replacement, repair, or modification must meet the requirements of this <extref docno="TM 10-5419-224-13&amp;P"/>. If quality of material requirements are not stated in this <extref docno="TM 10-5419-224-13&amp;P"/>, the material must meet the requirements of the drawings, standards, specifications, or approved engineering change proposals applicable to the subject equipment.
        </para>
    </qual.mat.info>\n'''

        tmp += '''\t<!-- This section is OPTIONAL. -->
    <iuid>
        <title>ITEM UNIQUE IDENTIFICATION</title>
        <para>This equipment and/or its components/parts are marked with item unique identification (IUID) markings such as data plates, decals, or etchings. These markings must be scanned during performance of procedures to remove and replace items marked or when turning in items or receiving them from supply or another unit. For information on location of the IUID marking for the end item, refer to the decal/data plate guide contained in the operator manual for the equipment.</para>
    </iuid>\n'''

    # This should be correct according to MIL-STD 2D CHANGE 1 spec, but does NOT validate in ArborText
    #     if self.mil_std == '2D':
    #         tmp += '''\t<mrpref>
    #     <title>MANDATORY REPLACEMENT PARTS</title>
    #     <!-- This paragraph shall reference the mandatory replacement parts list work package, 
    #             if it exists. If there are no MRPs for equipment covered by the manual, insert 
    #             the following statement in this paragraph:
    #     -->
    #     <para>There are no mandatory replacement parts for (insert equipment name).</para>            
    # </mrpref>\n'''

        if self.manual_type != '-10':
            tmp += '''\t<supdata>
        <title>SUPPORTING INFORMATION FOR COMMON TOOLS, REPAIR PARTS, SPECIAL TOOLS, TMDE, AND SUPPORT EQUIPMENT</title>     
        <para>For authorized common tools and equipment, refer to the Modified Table of Organization and Equipment (MTOE), <extref docno="50-970" pretext="Common Table of Allowances (CTA) " posttext=", Expendable/Durable Items (Except: Medical, Class V, Repair Parts, and Heraldic Items)"/>; <extref docno="50-909" pretext="CTA " posttext=", Field and Garrison Furnishings and Equipment"/>; or <extref docno="8-100" pretext="CTA " posttext=", Army Medical Department Expendable/Durable Items"/>; as applicable to your unit.</para>
        <para>Special tools, TMDE, and support equipment are required. The Maintenance Allocation Chart (MAC) Introduction and MAC can be found in <xref wpid="SXXXXX-XX-XXXX-XXX"/> and <xref wpid="SXXXXX-XX-XXXX-XXX"/>, respectively.</para>
        <para>Repair parts are listed and illustrated in <xref wpid="RXX-XX-XXXX-XXX"/> through <xref wpid="RXXXXX-XX-XXXX-XXX"/> of this manual.</para>
    </supdata>'''
        tmp += '</ginfowp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-G00001-GeneralInfo.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def equipment_description(self):
        """ Function that create Equipment Description and Data section of Chapter 1 in TM Shell """
        tmp = '\n<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += '<descwp wpno="G00002-' + self.sys_number + '" chngno="0">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += self.TAB_2 + '<maintlvl level="operator"/>\n'
        tmp += self.TAB_2 + '<title>EQUIPMENT DESCRIPTION AND DATA</title>\n'
        tmp += '\t</wpidinfo>\n'
        tmp += '\t<eqpinfo>\n'
        tmp += self.TAB_2 + \
                '<title>EQUIPMENT CHARACTERISTICS, CAPABILITIES, AND FEATURES</title>\n'
        tmp += self.TAB_2 + '<eqpdesc>\n'
        tmp += self.TAB_3 + '<title>Characteristics</title>\n'
        tmp += self.TAB_3 + '<para>\n'
        tmp += self.TAB_4 + '<figure id="G00002-' + self.sys_number + '-F0001">\n'
        tmp += f'{self.TAB_5}<title>{self.sys_acronym} Deployed</title>\n'
        tmp += self.TAB_5 + '<graphic boardno="PLACEHOLDER"/>\n'
        tmp += self.TAB_4 + '</figure>\n'
        tmp += self.TAB_3 + '</para>\n'
        tmp += self.TAB_2 + '</eqpdesc>\n'
        tmp += self.TAB_2 + '<?Pub _newpage?>\n'
        tmp += self.TAB_2 + '<eqpdesc>\n'
        tmp += self.TAB_3 + '<title>Capabilities and Features</title>\n'
        tmp += self.TAB_3 + '<para>\n'
        tmp += self.TAB_4 + '<randlist bullet="yes">\n'
        tmp += self.TAB_5 + '<item>Lorem ipsum.</item>\n'
        tmp += self.TAB_5 + '<item>Lorem ipsum.</item>\n'
        tmp += self.TAB_4 + '</randlist>\n'
        tmp += self.TAB_3 + '</para>\n'
        tmp += self.TAB_2 + '</eqpdesc>\n'
        tmp += '\t</eqpinfo>\n'
        tmp += '\t<locdesc>\n'
        tmp += self.TAB_2 + '<title>LOCATION AND DESCRIPTION OF MAJOR COMPONENTS</title>\n'
        tmp += self.TAB_2 + \
                '<para>Refer to the following technical manuals for description of end items that are components of ' + \
                self.sys_acronym + ':\n'
        tmp += self.TAB_3 + '<randlist bullet="yes">\n'
        tmp += self.TAB_4 + '<item>Lorem ipsum.</item>\n'
        tmp += self.TAB_4 + '<item>Lorem ipsum.</item>\n'
        tmp += self.TAB_3 + '</randlist>\n'
        tmp += self.TAB_2 + '</para>\n'
        tmp += self.TAB_2 + '<comp-item>\n'
        tmp += self.TAB_3 + '<para>\n'
        tmp += self.TAB_4 + '<figure id="G00002-' + self.sys_number + '-F0005">\n'
        tmp += f'{self.TAB_5}<title>{self.sys_acronym}' + ' Exterior (Front)</title>\n'
        tmp += self.TAB_5 + '<graphic boardno="PLACEHOLDER"/>\n'
        tmp += self.TAB_4 + '</figure>\n'
        tmp += self.TAB_4 + '<table id="G00002-' + self.sys_number + '-T0004">\n'
        tmp += f'{self.TAB_5}<title>{self.sys_acronym}' + '</title>\n'
        tmp += self.TAB_5 + '<tgroup cols="3">\n'
        tmp += self.TAB_6 + '<colspec colname="col1" colwidth="0.30*"/>\n'
        tmp += self.TAB_6 + '<colspec colname="col2" colwidth="0.40*"/>\n'
        tmp += self.TAB_6 + '<colspec colname="col3" colwidth="2.30*"/>\n'
        tmp += self.TAB_6 + '<thead>\n'
        tmp += self.TAB_7 + '<row>\n'
        tmp += self.TAB_8 + '<entry>CALLOUT</entry>\n'
        tmp += self.TAB_8 + '<entry>ITEM</entry>\n'
        tmp += self.TAB_8 + '<entry>DESCRIPTION</entry>\n'
        tmp += self.TAB_7 + '</row>\n'
        tmp += self.TAB_6 + '</thead>\n'
        tmp += self.TAB_6 + '<tbody>\n'
        tmp += self.TAB_7 + '<row>\n'
        tmp += self.TAB_8 + '<entry>1</entry>\n'
        tmp += self.TAB_8 + '<entry>Lorem Ipsum</entry>\n'
        tmp += self.TAB_8 + '<entry>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</entry>\n'
        tmp += self.TAB_7 + '</row>\n'
        tmp += self.TAB_7 + '<row>\n'
        tmp += self.TAB_8 + '<entry>2</entry>\n'
        tmp += self.TAB_8 + '<entry>Lorem Ipsum</entry>\n'
        tmp += self.TAB_8 + '<entry>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</entry>\n'
        tmp += self.TAB_7 + '</row>\n'
        tmp += self.TAB_6 + '</tbody>\n'
        tmp += self.TAB_5 + '</tgroup>\n'
        tmp += self.TAB_4 + '</table>\n'
        tmp += self.TAB_3 + '</para>\n'
        tmp += self.TAB_2 + '</comp-item>\n'
        tmp += self.TAB_2 + '<comp-item>\n'
        tmp += self.TAB_3 + '<para></para>\n'
        tmp += self.TAB_3 + '<para>\n'
        tmp += self.TAB_4 + '<figure id="G00002-' + self.sys_number + '-F0006">\n'
        tmp += self.TAB_5 + '<title>Lorem Ipsum</title>\n'
        tmp += self.TAB_5 + '<graphic boardno="PLACEHOLDER"/>\n'
        tmp += self.TAB_4 + '</figure>\n'
        tmp += self.TAB_4 + '<table id="G00002-' + self.sys_number + '-T0005">\n'
        tmp += self.TAB_5 + '<title>Lorem Ipsum</title>\n'
        tmp += self.TAB_5 + '<tgroup cols="3">\n'
        tmp += self.TAB_6 + '<colspec colname="col1" colwidth="0.30*"/>\n'
        tmp += self.TAB_6 + '<colspec colname="col2" colwidth="0.40*"/>\n'
        tmp += self.TAB_6 + '<colspec colname="col3" colwidth="2.30*"/>\n'
        tmp += self.TAB_6 + '<thead>\n'
        tmp += self.TAB_7 + '<row>\n'
        tmp += self.TAB_8 + '<entry>CALLOUT</entry>\n'
        tmp += self.TAB_8 + '<entry>ITEM</entry>\n'
        tmp += self.TAB_8 + '<entry>DESCRIPTION</entry>\n'
        tmp += self.TAB_7 + '</row>\n'
        tmp += self.TAB_6 + '</thead>\n'
        tmp += self.TAB_6 + '<tbody>\n'
        tmp += self.TAB_7 + '<row>\n'
        tmp += self.TAB_8 + '<entry>1</entry>\n'
        tmp += self.TAB_8 + '<entry>Lorem Ipsum</entry>\n'
        tmp += self.TAB_8 + '<entry>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</entry>\n'
        tmp += self.TAB_7 + '</row>\n'
        tmp += self.TAB_7 + '<row>\n'
        tmp += self.TAB_8 + '<entry>2</entry>\n'
        tmp += self.TAB_8 + '<entry>Lorem Ipsum</entry>\n'
        tmp += self.TAB_8 + '<entry>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</entry>\n'
        tmp += self.TAB_7 + '</row>\n'
        tmp += self.TAB_7 + '<row>\n'
        tmp += self.TAB_8 + '<entry>3</entry>\n'
        tmp += self.TAB_8 + '<entry>Lorem Ipsum</entry>\n'
        tmp += self.TAB_8 + '<entry>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</entry>\n'
        tmp += self.TAB_7 + '</row>\n'
        tmp += self.TAB_7 + '<row>\n'
        tmp += self.TAB_8 + '<entry>4</entry>\n'
        tmp += self.TAB_8 + '<entry>Lorem Ipsum</entry>\n'
        tmp += self.TAB_8 + '<entry>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</entry>\n'
        tmp += self.TAB_7 + '</row>\n'
        tmp += self.TAB_6 + '</tbody>\n'
        tmp += self.TAB_5 + '</tgroup>\n'
        tmp += self.TAB_4 + '</table>\n'
        tmp += self.TAB_3 + '</para>\n'
        tmp += self.TAB_2 + '</comp-item>\n'
        tmp += '\t</locdesc>\n'

        if self.mil_std == '2C':
            tmp += '\t<eqpdiff>\n'
            tmp += self.TAB_2 + '<title>EQUIPMENT DIFFERENCES</title>\n'
            tmp += self.TAB_2 + '<para>' + self.lorem_ipsum + '</para>\n'
            tmp += '\t</eqpdiff>\n'

        tmp += '\t<eqpdata>\n'
        tmp += self.TAB_2 + '<title>EQUIPMENT DATA</title>\n'
        tmp += self.TAB_2 + '<para>' + self.lorem_ipsum + '</para>\n'
        tmp += self.TAB_2 + '<para>\n'
        tmp += self.TAB_3 + '<table id="G00002-' + self.sys_number + '-T0020">\n'
        tmp += self.TAB_4 + '<title>' + self.sys_acronym + ' Support Equipment Data</title>\n'
        tmp += self.TAB_4 + '<tgroup cols="2">\n'
        tmp += self.TAB_5 + '<colspec colname="col1"/>\n'
        tmp += self.TAB_5 + '<colspec colname="col2"/>\n'
        tmp += self.TAB_5 + '<tbody>\n'
        tmp += self.TAB_6 + '<row>\n'
        tmp += self.TAB_7 + '<entry colsep="0"><emphasis emph="bold">Dimensions:</emphasis></entry>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_6 + '</row>\n'
        tmp += self.TAB_6 + '<row>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_6 + '</row>\n'
        tmp += self.TAB_6 + '<row>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_6 + '</row>\n'

        tmp += self.TAB_6 + '<row>\n'
        tmp += self.TAB_7 + '<entry colsep="0"><emphasis emph="bold">Environmental Requirements:</emphasis></entry>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_6 + '</row>\n'
        tmp += self.TAB_6 + '<row>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_6 + '</row>\n'
        tmp += self.TAB_6 + '<row>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_6 + '</row>\n'

        tmp += self.TAB_6 + '<row>\n'
        tmp += self.TAB_7 + '<entry colsep="0"><emphasis emph="bold">References:</emphasis></entry>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_6 + '</row>\n'
        tmp += self.TAB_6 + '<row>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_6 + '</row>\n'
        tmp += self.TAB_6 + '<row>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_7 + '<entry></entry>\n'
        tmp += self.TAB_6 + '</row>\n'

        tmp += self.TAB_5 + '</tbody>\n'
        tmp += self.TAB_4 + '</tgroup>\n'
        tmp += self.TAB_3 + '</table>\n'
        tmp += self.TAB_2 + '</para>\n'

        tmp += self.TAB_2 + '<para0>\n'
        tmp += self.TAB_3 + '<title>Performance Data</title>\n'
        tmp += self.TAB_3 + '<para>Operating the ' + self.sys_acronym + \
                ' outside of these specifications may cause equipment damage due to freezing or overheating.</para>\n'
        tmp += self.TAB_2 + '</para0>\n'
        tmp += '\t</eqpdata>\n'
        tmp += '</descwp>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
                ' WIP/{:05d}-G00002-EquipmentDescription.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def theory_operations(self):
        """ Function to create the theory of operations section """
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += '<thrywp wpno="G00003-' + self.sys_number + '" chngno="0">'
        tmp += '\t<wpidinfo>\n'
        tmp += self.TAB_2 + '<maintlvl level="operator"/>\n'
        tmp += self.TAB_2 + '''<title>THEORY OF OPERATION</title>
        </wpidinfo>
        <intro>
            <para0>
                <title>Introduction</title>\n'''
        tmp += self.TAB_2 + '<para>The ' + self.sys_name + ' is (' + \
            self.sys_acronym + ') (<xref figid="G00003-' + \
            self.sys_number + '-F0001"/>) consists of ... ' + 'The ' + \
            self.sys_acronym + ' theory of operation by major component is described in the following paragraphs.</para>\n'
        tmp += self.TAB_2 + '<para>\n'
        tmp += self.TAB_3 + '<figure id="G00003-' + self.sys_number + '-F0001">\n'
        tmp += self.TAB_4 + '''<title>Lorem Ipsum</title>
                        <graphic boardno="PLACEHOLDER"/>
                    </figure>
                </para>
            </para0>
        </intro>
        <systhry>
            <title>LOREM IPSUM</title>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
        </systhry>
        <systhry>
            <title>LOREM IPSUM</title>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
            <para>\n'''
        tmp += self.TAB_3 + '<figure id="G00003-' + self.sys_number + '-F0002">\n'
        tmp += self.TAB_4 + '''<title>Lorem Ipsum</title>
                    <graphic boardno="PLACEHOLDER"/>
                </figure>
            </para>
        </systhry>
    </thrywp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-G00003-TheoryOfOperations.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10
        
    def end(self):
        """ Function to create chapter 1 end tags """
        tmp = '</gim>'
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type + \
            ' WIP/{:05d}-CHAP_1_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 1