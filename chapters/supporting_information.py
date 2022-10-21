"""SUPPORTING INFORMATION"""
import cfg
import math
from dotenv import dotenv_values

class SupportingInformation:
    """Class to create various types of WP's included in Supporting Info section of a TM."""
    config = dotenv_values(".env")  # take environment variables from .env.

    def __init__(self, manual_type, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function to create Supporting Info section start tags."""
        cfg.prefix_file = (math.floor(cfg.prefix_file/1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
    <sim chngno="0" revno="0" chap-toc="no">\n'''
        tmp += '\t<titlepg maintlvl="operator">\n'
        tmp += '\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')</name>\n'
        tmp += '\t</titlepg>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-SUPPORT_INFO_START.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def refwp(self, wpno):
        """Function to create References WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<refwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>REFERENCES</title>
    </wpidinfo>
    <scope>
        <title>Scope</title>
        <para>This work package lists all field manuals, forms, technical manuals, and miscellaneous publications referenced in this manual.</para>
    </scope>
    <publist>
        <title>ARMY REGULATIONS</title>
        <pubident>
            <name><extref docno="AR 700-138"/></name>
            <title>ARMY LOGISTICS READINESS AND SUSTAINABILITY</title>
        </pubident>
    </publist>
    <publist>
        <title>ARMY TECHNIQUES PUBLICATIONS</title>
        <pubident>
            <name><extref docno="ATP 3-11.32"/></name>
            <title>MULTI-SERVICE TACTICS, TECHNIQUES, AND PROCEDURES FOR CHEMICAL, BIOLOGICAL, RADIOLOGICAL, AND NUCLEAR PASSIVE DEFENSE</title>
        </pubident>
    </publist>
    <publist>
        <title>COMMON TABLE OF ALLOWANCES</title>
        <pubident>
            <name><extref docno="CTA 8-100"/></name>
            <title>ARMY MEDICAL DEPARTMENT EXPENDABLE/DURABLE ITEMS</title>
        </pubident>
        <pubident>
            <name><extref docno="CTA 50-909"/></name>
            <title>FIELD AND GARRISON FURNISHINGS AND EQUIPMENT</title>
        </pubident>
        <pubident>
            <name><extref docno="CTA 50-970"/></name>
            <title>EXPENDABLE/DURABLE ITEMS (EXCEPT MEDICAL, CLASS V, REPAIR PARTS, AND HERALDIC ITEMS)</title>
        </pubident>
    </publist>
    <publist>
        <title>DA PAMPHLETS</title>
        <pubident>
            <name><extref docno="DA PAM 25-40"/></name>
            <title>ARMY PUBLISHING PROGRAM PROCEDURES</title>
        </pubident>
        <pubident>
            <name><extref docno="DA PAM 738-751"/></name>
            <title>FUNCTIONAL USERS MANUAL FOR THE ARMY MAINTENANCE MANAGEMENT SYSTEM - AVIATION</title>
        </pubident>
        <pubident>
            <name><extref docno="DA PAM 750-8"/></name>
            <title>THE ARMY MAINTENANCE MANAGEMENT SYSTEM (TAMMS) USERS MANUAL</title>
        </pubident>
    </publist>
    <publist>
        <title>FORMS</title>
        <pubident>
            <name><extref docno="DA Form 12"/></name>
            <title>REQUEST FOR ESTABLISHMENT OF A PUBLICATIONS ACCOUNT</title>
        </pubident>
        <pubident>
            <name><extref docno="DA Form 2028"/></name>
            <title>RECOMMENDED CHANGES TO PUBLICATIONS AND BLANK FORMS</title>
        </pubident>
        <pubident>
            <name><extref docno="DA Form 2404 / DA Form 5988-E"/></name>
            <title>EQUIPMENT INSPECTION AND MAINTENANCE WORKSHEET</title>
        </pubident>
        <pubident>
            <name><extref docno="DA Form 2408-9"/></name>
            <title>EQUIPMENT CONTROL RECORD</title>
        </pubident>
        <pubident>
            <name><extref docno="SF 368"/></name>
            <title>PRODUCT QUALITY DEFICIENCY REPORT</title>
        </pubident>
    </publist>
    <publist>
        <title>LUBRICATION ORDERS</title>
        <pubident>
            <name><extref docno="LO 9-6115-642-12"/></name>
            <title>GENERATOR SET, SKID MOUNTED, TACTICAL QUIET 10 KW, 60 AND 400 HZ 60 HZ (NSN 6115-01-275-5061) PART NUMBER: MEP-803A EIC: VG3 CAGEC: 30554 400 HZ (6115-01-274-7392) PART NUMBER: MEP-813A EIC: VN3 CAGEC: 30554</title>
        </pubident>
    </publist>
    <publist>
        <title>TECHNICAL BULLETINS</title>
        <pubident>
            <name><extref docno="TB MED 530"/></name>
            <title>TRI-SERVICE FOOD CODE</title>
        </pubident>
    </publist>
    <publist>
        <title>TECHNICAL MANUALS</title>
        <pubident>
            <name><extref docno="TM 3-34.46"/></name>
            <title>THEATER OF OPERATIONS ELECTRICAL SYSTEMS</title>
        </pubident>
        <pubident>
            <name><extref docno="TM 9-2330-328-13&amp;P"/></name>
            <title>OPERATOR AND FIELD MAINTENANCE MANUAL INCLUDING REPAIR PARTS AND SPECIAL TOOLS LIST (RPSTL) FOR CHASSIS, CONTAINERIZED KITCHEN TRAIL: 7 1/2-TON, 4-WHEEL XCK2000 NSN 2330-01-471-7006 TRAILER: 7 1/2-TON, 4-WHEEL XCK2000E1 NSN 2330-01-506-5979</title>
        </pubident>
        <pubident>
            <name><extref docno="TM 9-6115-642-10"/></name>
            <title>OPERATOR'S MANUAL FOR GENERATOR SET, SKID MOUNTED, TACTICAL QUIET, 10 KW, 60 HZ MEP-803A (NSN 6115-01-275-5061) (EIC VG3) GENERATOR SET, SKID MOUNTED, TACTICAL QUIET, 10 KW, 400 HZ MEP-813A (NSN 6115-01-274-7392) (EIC VN3)</title>
        </pubident>
        <pubident>
            <name><extref docno="TM 9-6115-750-10"/></name>
            <title>OPERATOR'S MANUAL FOR GENERATOR SET, SKID MOUNTED 10KW ADVANCED MEDIUM MOBILE POWER SOURCES (AMMPS) MEP-1040 50/60 HZ (NSN: 6115-01-561-7455) (EIC: N/A) MEP-1041 400 HZ (NSN: 6115-01-561-7466) (EIC: N/A)</title>
        </pubident>
        <pubident>
            <name><extref docno="TM 10-7310-281-13&amp;P"/>
            </name>
            <title>OPERATOR AND FIELD MAINTENANCE MANUAL INCLUDING REPAIR PARTS AND SPECIAL TOOLS LIST FOR MODERN BURNER UNIT (MBU) NSN 7310-01-452-8137 MODERN BURNER UNIT (MBU-V3) NSN 7310-01-507-9310</title>
        </pubident>
        <pubident>
            <name><extref docno="TM 10-7360-211-13&amp;P"/></name>
            <title>OPERATOR'S, UNIT, AND DIRECT SUPPORT MAINTENANCE MANUAL INCLUDING REPAIR PARTS AND SPECIAL TOOLS LIST FOR FOOD SANITATION CENTER (FSC) MODEL FSC-90 NSN 7360-01-277-2558 MODEL FSC-2 NSN 7360-01-496-2112</title>
        </pubident>
        <pubident>
            <name><extref docno="TM 750-244-3"/></name>
            <title>PROCEDURES FOR DESTRUCTION OF EQUIPMENT TO PREVENT ENEMY USE (MOBILITY EQUIPMENT COMMAND)</title>
        </pubident>	
    </publist>
    <publist>
        <title>TRAINING CIRCULARS</title>
        <pubident>
            <name><extref docno="TC 4-02.1"/></name>
            <title>FIRST AID</title>
        </pubident>
    </publist>
</refwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-References.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def macintrowp(self, wpno):
        """Function to create the Introduction WP for the MAC."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<macintrowp wpno="{wpno}-' + self.sys_number + '" chngno="0">\n'
        tmp += '''\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>MAINTENANCE ALLOCATION CHART (MAC) INTRODUCTION</title>
    </wpidinfo>
    <intro>
        <para0>
            <title>INTRODUCTION<?Pub _newline?>The Army Maintenance System MAC</title>\n'''
        tmp += '\t\t\t<para>' + self.config.get("MAC_INTRO1")+ '</para>\n'
        tmp += '\t\t\t<para>' + self.config.get("MAC_INTRO2") + '\n'
        tmp += '\t\t\t\t<seqlist>' + '\n'
        tmp += '''\t\t\t\t\t<item>Field level maintenance classes:
                        <seqlist>
                            <item>Crew (operator) maintenance. This is the responsibility of a using organization to perform maintenance on its assigned equipment. It normally consists of inspecting, servicing, lubricating, adjusting, and replacing parts, minor assemblies, and subassemblies. Items with a &ldquo;C&rdquo; (&ldquo;O&rdquo; for joint service reporting) in the third position of the Source, Maintenance, and Recoverability (SMR) code may be replaced at the crew (operator) class. A code of &ldquo;C&rdquo; (&ldquo;O&rdquo; for joint service) in the fourth position of the SMR code indicates complete repair is authorized at the crew (operator) class.</item>
                            <item>Maintainer maintenance. This is maintenance accomplished on a component, accessory, assembly, subassembly, plug-in unit, or other portion by field level units. This maintenance is performed either on the system or after it is removed. An &ldquo;F&rdquo; in the third position of the SMR code indicates replacement of assemblies, subassemblies, or other components is authorized at this level. An &ldquo;F&rdquo; in the fourth position of the SMR code indicates complete repair of the identified item is allowed at the Maintainer class. Items repaired at this level are normally returned to the user after maintenance is performed.</item>
                        </seqlist>
                    </item>
                    <item>Sustainment level maintenance classes:
                        <seqlist>
                            <item>Below depot sustainment. This is maintenance accomplished on a component, accessory, assembly, subassembly, plug-in unit, or other portion either on the system or after it is removed. The item subject to maintenance has normally been forwarded to a maintenance facility away from the field level supporting units. An "H" in the third position of the SMR code indicates replacement of assemblies, subassemblies, or other components is authorized at this class. An "H" appearing in the fourth position of the SMR code indicates complete repair is possible at this class. Items are normally returned to the supply system after maintenance is performed at this class.</item>
                            <item>Depot. This is maintenance accomplished on a component, accessory, assembly, subassembly, plug-in unit, or other portion either on the system or after it is removed. Assets to be repaired at this class are normally returned to an Army Depot or authorized contractor facility. The replace function for this class of maintenance is indicated by the letter "D" or "K" appearing in the third position of the SMR code. A "D" or "K" appearing in the fourth position of the SMR code indicates complete repair is possible at the depot sustainment maintenance level. Items are returned to the supply system after maintenance is performed at this class.</item>
                        </seqlist>
                    </item>
                </seqlist>
            </para>
            <para>The tools and test equipment requirements table (immediately following the MAC) lists the tools and test equipment (both special tools and common tool sets) required for each maintenance task as referenced from the MAC.</para>
            <para>The remarks table (immediately following the tools and test equipment requirements) contains supplemental instructions and explanatory notes for a particular maintenance task.</para>
            <para>
                <emphasis emph="bold">Maintenance Functions (Tasks)</emphasis>
            </para>
            <para>Maintenance functions are limited to and defined as follows:
                <seqlist>\n'''
        tmp += '\t\t\t\t\t<item>' + self.config.get("INSPECT") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("TEST") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("SERVICE") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("ADJUST") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("ALIGN") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("CALIBRATE") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("REMOVE") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("INSTALL") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("REPLACE") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("REPAIR") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("PAINT") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("OVERHAUL") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("REBUILD") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("LUBRICATE") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("MARK") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("PACK") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("UNPACK") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("PRESERVE") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("PREPARE") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("ASSEMBLE") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("DISASSEMBLE") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("CLEAN") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("NONDESTRUCTIVE_INSPECTION") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("RADIO_INTERFERENCE") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("PLACE_IN_SERVICE") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("TOWING") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("JACKING") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("PARKING") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("MOORING") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("COVERING") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("HOISTING") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("SLING_LOADING") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("EXTERNAL_POWER") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("PREPSTORE") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("PREPSHIP") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("PREPSTORE") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("TRANSPORT") + '</item>\n'
        tmp += '\t\t\t\t\t<item>' + self.config.get("ARM") + '</item>\n'
        tmp += '''\t\t\t\t\t<item>Load. Step-by-step instructions for one of two tasks:
                        <seqlist>
                            <item>For transportation, the act of placing assets onto a transportation medium (e.g., pallet, truck, container).</item>
                            <item>For weapons/weapons systems, the act of placing munitions into the weapon/weapons system.</item>
                        </seqlist>
                    </item>
                    <item>Unload. Step-by-step instructions for one of two tasks:
                        <seqlist>
                            <item>For transportation, the act of removing assets from a transportation medium (e.g., pallet, truck, container).</item>
                            <item>For weapons/weapons systems, the act of removing munitions from the weapon/weapons system.</item>
                        </seqlist>
                    </item>
                    <item>Install peripheral device. Step-by-step instructions for installing peripheral devices such as printers, scanners, modems, etc.</item>
                    <item>Uninstall peripheral device. Step-by-step instructions for uninstalling peripheral devices such as printers, scanners, modems, etc.</item>
                    <item>Upgrade/patch. Step-by-step instructions for performing an upgrade to software or installing a patch to software.</item>
                    <item>Configure. Step-by-step instructions for configuring software for different uses/purposes and/or different users.</item>
                    <item>Debug. Step-by-step instructions for debugging software/correcting errors in the software.</item>
                </seqlist>
            </para>
            <para>
                <emphasis emph="bold">Explanation of Columns in the MAC</emphasis>
            </para>
            <para>Column (1) Group Number. Column (1) lists Functional Group Code (FGC) numbers, the purpose of which is to identify maintenance significant components, assemblies, subassemblies, and modules with the Next Higher Assembly (NHA).</para>
            <para>Column (2) Component/Assembly. Column (2) contains the item names of components, assemblies, subassemblies, and modules for which maintenance is authorized.</para>
            <para>Column (3) Maintenance Function. Column (3) lists the functions to be performed on the item listed in column (2). (For a detailed explanation of these functions, refer to maintenance functions (tasks) outlined previously.)</para>
            <para>Column (4) Maintenance Level. Column (4) specifies each level/class of maintenance authorized to perform each function listed in column (3), by indicating man-hours required in the appropriate sub-column. The man-hour figure is the task time multiplied by the number of maintainers required to perform that maintenance task. This time includes preparation (equipment conditions, inspections), task performance, follow-on maintenance and quality assurance (inspections) time. Crew maintenance time will be entered as task (clock) time only. If different maintenance classes perform the same maintenance functions due to the number or complexity of the tasks, appropriate man-hour figures are to be shown for each class. The symbol designations for the various maintenance levels and classes are as follows:
                <randlist bullet="no">
                    <title>
                        <emphasis emph="uline">Field:</emphasis>
                    </title>
                    <item>C Crew maintenance</item>
                    <item>F Maintainer maintenance</item>
                </randlist>
                <randlist bullet="no">
                    <title>
                        <emphasis emph="uline">Sustainment:</emphasis>
                    </title>
                    <item>L Specialized Repair Activity (SRA)</item>
                    <item>H Below depot maintenance</item>
                    <item>D Depot maintenance</item>
                </randlist>
            </para>
            <note>
                <trim.para>The "L" maintenance class is not included in column (4) of the MAC. Functions to this class of maintenance are identified by work time figure in the "H" column of column (4), and an associated reference code is used in the REMARKS column (6). This code is keyed to the remarks and the SRA complete repair application is explained there.</trim.para>
            </note>
            <para>Column (5) Tools and Equipment Reference Code. Column (5) specifies, by a number code, those common tool sets, kits, or outfits (not individual tools), common Test, Measurement and Diagnostic Equipment (TMDE), common tools that are not part of a set, kit, or outfit, special tools, special TMDE, and special support equipment required to perform the designated function. Codes are keyed to the entries in the tools and test equipment table.</para>
            <para>Column (6) Remarks Code. When applicable, this Column (6) contains a letter code, in alphabetical order, which is keyed to the remarks table entries.</para>
            <para>
                <emphasis emph="bold">Explanation of Columns in the Tools and Test Equipment Requirements</emphasis>
            </para>
            <para>Column (1) Tool or Test Equipment Reference Code. The tool or test equipment reference code correlates with a code used in column (5) of the MAC.</para>
            <para>Column (2) Maintenance Level. The lowest class of maintenance authorized to use the tool or test equipment.</para>
            <para>Column (3) Nomenclature. Name or identification of the tool or test equipment.</para>
            <para>Column (4) National Stock Number (NSN). The NSN of the tool or test equipment.</para>
            <para>Column (5) Tool Number. The manufacturer's part number.</para>
            <?Pub _newpage?>
            <para>
                <emphasis emph="bold">Explanation of Columns in the Remarks</emphasis>
            </para>
            <para>Column (1) Remarks Code. The code recorded in column (6) of the MAC.</para>
            <para>Column (2) Remarks. This column lists information pertinent to the maintenance task being performed as indicated in the MAC.</para>
        </para0>
    </intro>
</macintrowp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-MAC-Introduction.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def macwp(self, wpno):
        """Function to create the MAC WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<macwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>MAINTENANCE ALLOCATION CHART (MAC)</title>
    </wpidinfo>
    <mac>
        <title>Maintenance Allocation Chart for ...</title>
        <!-- THESE ENTRIES ARE JUST EXAMPLES. YOU MUST FILL THEM IN WITH YOUR OWN DATA. -->
        <mac-group-2lvl>
            <groupno>00</groupno>
            <compassemgroup-2lvl>
                <compassem>
                    <name></name>
                </compassem>
                <qualify-2lvl>
                    <maintfunc func="inspect"/>
                    <maintclass-2lvl>
                        <c></c>
                    </maintclass-2lvl>
                </qualify-2lvl>
            </compassemgroup-2lvl>
        </mac-group-2lvl>
        <mac-group-2lvl>
            <groupno>01</groupno>
            <compassemgroup-2lvl>
                <compassem>
                    <name></name>
                </compassem>
                <qualify-2lvl>
                    <maintfunc func="install"/>
                    <maintclass-2lvl>
                        <c/>
                    </maintclass-2lvl>
                </qualify-2lvl>
                <qualify-2lvl>
                    <maintfunc func="repair"/>
                    <maintclass-2lvl>
                        <c></c>
                    </maintclass-2lvl>
                </qualify-2lvl>
            </compassemgroup-2lvl>
        </mac-group-2lvl>
        <mac-group-2lvl>
            <groupno>02</groupno>
            <compassemgroup-2lvl>
                <compassem>
                    <name></name>
                </compassem>
                <qualify-2lvl>
                    <maintfunc func="none"/>
                    <maintclass-2lvl>
                        <c></c>
                    </maintclass-2lvl>
                </qualify-2lvl>
            </compassemgroup-2lvl>
        </mac-group-2lvl>
    </mac>
    <?Pub _newpage?>
    <tereqtab>
        <title>Tools and Test Equipment for ...</title>
        <!-- THESE ENTRIES ARE JUST EXAMPLES. YOU MUST FILL THEM IN WITH YOUR OWN DATA. -->
        <teref-group>
            <terefcode id="MAC_TOOL_01">1</terefcode>
            <maintenance lvl="c"/>
            <name></name>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <toolno></toolno>
        </teref-group>
        <teref-group>
            <terefcode id="MAC_TOOL_02">2</terefcode>
            <maintenance lvl="c"/>
            <name></name>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <toolno></toolno>
        </teref-group>
        <teref-group>
            <terefcode id="MAC_TOOL_03">3</terefcode>
            <maintenance lvl="c"/>
            <name></name>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <toolno></toolno>
        </teref-group>
        <teref-group>
            <terefcode id="MAC_TOOL_04">4</terefcode>
            <maintenance lvl="c"/>
            <name></name>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <toolno></toolno>
        </teref-group>
        <teref-group>
            <terefcode id="MAC_TOOL_05">5</terefcode>
            <maintenance lvl="c"/>
            <name></name>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <toolno></toolno>
        </teref-group>
    </tereqtab>
    <?Pub _newpage?>
    <remarktab>
        <title>Remarks for ...</title>
        <!-- THESE ENTRIES ARE JUST EXAMPLES. YOU MUST FILL THEM IN WITH YOUR OWN DATA. -->
        <remark-group>
            <remarkcode id="X">A</remarkcode>
            <remarks></remarks>
        </remark-group>
        <remark-group>
            <remarkcode id="X">B</remarkcode>
            <remarks></remarks>
        </remark-group>
        <remark-group>
            <remarkcode id="X">C</remarkcode>
            <remarks></remarks>
        </remark-group>
        <remark-group>
            <remarkcode id="X">D</remarkcode>
            <remarks></remarks>
        </remark-group>
        <remark-group>
            <remarkcode id="X">E</remarkcode>
            <remarks></remarks>
        </remark-group>
    </remarktab>
</macwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-MAC.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def coeibiiwp(self, wpno):
        """Function to create the COEI & BII Lists WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<coeibiiwp chngno="0" wpno="{wpno}-' + self.sys_number +'">\n'
        tmp += '''\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>COMPONENTS OF END ITEM (COEI) AND BASIC ISSUE ITEMS (BII) LIST</title>
    </wpidinfo>
    <intro frame="no">
        <para0>
            <title>COMPONENTS OF END ITEM (COEI) AND BASIC ISSUE ITEMS (BII) LIST<?Pub _newline?>INTRODUCTION</title>
            <subpara1>
                <title>Scope</title>
                <para>This work package lists COEI and BII for the Containerized Kitchen (CK) to help you inventory items for safe and efficient operation of the equipment.</para>
            </subpara1>
            <subpara1>
                <title>General</title>
                <para>The COEI and BII information is divided into the following lists:</para>
                <para>Components of End Item (COEI). This list is for information purposes only and is not authority to requisition replacements. These items are part of the CK. As part of the end item, these items must be with the end item whenever it is issued or transferred between property accounts. Items of COEI are removed and separately packaged for transportation or shipment only when necessary. Illustrations are furnished to help you find and identify the items.</para>
                <para>Basic Issue Items (BII). These essential items are required to place the CK in operation, operate it, and to do emergency repairs. Although shipped separately packaged, BII must be with the CK during operation and when it is transferred between property accounts. Listing these items is your authority to request/requisition them for replacement based on authorization of the end item by the Table of Organization and Equipment/Modified Table of Organization and Equipment (TOE/MTOE). Illustrations are furnished to help you find and identify the items.</para>
            </subpara1>
            <subpara1>               
                <title>Explanation of Columns in the COEI List and BII List:</title>
                <para>Column (1) Item Number. Gives you the reference number of the item listed.</para>
                <para>Column (2) National Stock Number (NSN) and Illustration. Identifies the stock number of the item to be used for requisitioning purposes and provides an illustration of the item.</para>
                <para>Column (3) Description, Part Number/(CAGEC). Identifies the Federal item name (in all capital letters) followed by a minimum description when needed. The stowage location of COEI and BII is also included in this column. The last line below the description is the CAGEC (Commercial and Government Entity Code) (in parentheses) and the part number.</para>
                <para>Column (4) Usable On Code. When applicable, gives you a code if the item you need is not the same for different models of equipment.</para>
                <para>Column (5) U/I. Unit of Issue (U/I) indicates the physical measurement or count of the item as issued per the National Stock Number shown in column (2).</para>
                <para>Column (6) Qty Rqr. Indicates the quantity required.</para>
            </subpara1>
        </para0>
    </intro>
    <?Pub _newpage?>
    <coei-opt id="coeitab">
        <title>Components of End Item (COEI) List</title>
            <!-- THESE ENTRIES ARE JUST EXAMPLES. YOU MUST FILL THEM IN WITH YOUR OWN DATA. -->
        <coei-opt-entry>
            <itemno id="COEI-1"></itemno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <graphic boardno="RPSTL_Placeholder"></graphic>
            <dcpno>
                <name></name>
                <desc></desc>
                <partno></partno>
                <cageno></cageno>
                <uoc></uoc>
            </dcpno>
            <ui></ui>
            <qty></qty>
        </coei-opt-entry>
        <coei-opt-entry>
            <itemno id="COEI-2"></itemno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <graphic boardno="RPSTL_Placeholder"></graphic>
            <dcpno>
                <name></name>
                <desc></desc>
                <partno></partno>
                <cageno></cageno>
                <uoc></uoc>
            </dcpno>
            <ui></ui>
            <qty></qty>
        </coei-opt-entry>
        <coei-opt-entry>
            <itemno id="COEI-3"></itemno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <graphic boardno="RPSTL_Placeholder"></graphic>
            <dcpno>
                <name></name>
                <desc></desc>
                <partno></partno>
                <cageno></cageno>
                <uoc></uoc>
            </dcpno>
            <ui></ui>
            <qty></qty>
        </coei-opt-entry>
    </coei-opt>
    <?Pub _newpage?>
        <!-- THESE ENTRIES ARE JUST EXAMPLES. YOU MUST FILL THEM IN WITH YOUR OWN DATA. -->
    <bii-opt id="biitab">
        <title>Basic Issue Items (BII) List</title>
        <bii-opt-entry>
            <itemno id="BII-1"></itemno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <graphic boardno="RPSTL_Placeholder"></graphic>
            <dcpno>
                <name></name>
                <desc></desc>
                <partno></partno>
                <cageno></cageno>
                <uoc></uoc>
            </dcpno>
            <ui></ui>
            <qty></qty>
        </bii-opt-entry>
        <bii-opt-entry>
            <itemno id="BII-2"></itemno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <graphic boardno="RPSTL_Placeholder"></graphic>
            <dcpno>
                <name></name>
                <desc></desc>
                <partno></partno>
                <cageno></cageno>
                <uoc></uoc>
            </dcpno>
            <ui></ui>
            <qty></qty>
        </bii-opt-entry>
        <bii-opt-entry>
            <itemno id="BII-3"></itemno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <graphic boardno="RPSTL_Placeholder"></graphic>
            <dcpno>
                <name></name>
                <desc></desc>
                <partno></partno>
                <cageno></cageno>
                <uoc></uoc>
            </dcpno>
            <ui></ui>
            <qty></qty>
        </bii-opt-entry>
    </bii-opt>
</coeibiiwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-COEI-BII-List.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def aalwp(self, wpno):
        """Function to create the Additional Authorization List (AAL) WP."""
        tmp = f'<aalwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>ADDITIONAL AUTHORIZATION LIST (AAL)</title>
    </wpidinfo>
    <intro>
        <para0>
            <title>INTRODUCTION</title>
            <subpara1>
                <title>Scope</title>
                <para>This work package lists additional items you are authorized for the support of the ETSSLS.</para>
            </subpara1>
            <subpara1>
                <title>General</title>
                <para>This list identifies items that do not have to accompany the ETSSLS and that do not have to be turned in with it. These items are all authorized to you by CTA, MTOE, TDA, or JTA.</para>
            </subpara1>
            <subpara1>
                <title>Explanation of Columns in the AAL</title>
                    <para>Column (1) National Stock Number (NSN). Identifies the stock number of the item to be used for requisitioning purposes.</para>
                    <para>Column (2) Description, Part Number/(CAGEC). Identifies the Federal item name (in all capital letters) followed by a minimum description when needed. The last line below the description is the part number and the Commercial and Government Entity Code (CAGEC) (in parentheses).</para>
                    <para>Column (3) Usable On Code. When applicable, gives you a code if the item you need is not the same for different models of equipment. These codes are identified below:
                        <table id="S0007-10-5419-215-T0001">
                            <tgroup cols="2">
                                <colspec colname="col1"/>
                                <colspec colname="col2"/>
                                <thead>
                                    <row>
                                        <entry>Code</entry>
                                        <entry>Used on</entry>
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
                                </tbody>
                            </tgroup>
                        </table>
                    </para>
                    <para>Column (4) U/I. Unit of Issue (U/I) indicates the physical measurement or count of the item as issued per the National Stock Number shown in column (1).</para>
                    <para>Column (5) Qty Recm. Indicates the quantity recommended.</para>
            </subpara1>
        </para0>
    </intro>
    <aal>
        <title>Additional Authorization List (AAL)</title>
        <!-- THESE ENTRIES ARE JUST EXAMPLES. YOU MUST FILL THEM IN WITH YOUR OWN DATA. -->
        <aal-entry>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0248</niin>
            </nsn>
            <dcpno>
                <name>Expeditionary TRICON Food Sanitation System (GREEN)</name>
                <partno>9-1-1121-1</partno>
                <cageno></cageno>
                <uoc>SHELTER, EXPANDABLE, ETFSS</uoc>
            </dcpno>
            <ui></ui>
            <qty>1</qty>
        </aal-entry>
        <aal-entry>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0260</niin>
            </nsn>
            <dcpno>
                <name>Expeditionary TRICON Food Sanitation System (TAN)</name>
                <partno>9-1-1121-2</partno>
                <cageno></cageno>
                <uoc>SHELTER, EXPANDABLE, ETFSS</uoc>
            </dcpno>
            <ui></ui>
            <qty>1</qty>
        </aal-entry>
         <aal-entry>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0272</niin>
            </nsn>
            <dcpno>
                <name>Expeditionary TRICON Food Sanitation System (RED)</name>
                <partno>9-1-1121-3</partno>
                <cageno></cageno>
                <uoc>SHELTER, EXPANDABLE, ETFSS</uoc>
            </dcpno>
            <ui></ui>
            <qty>1</qty>
        </aal-entry>
         <aal-entry>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0284</niin>
            </nsn>
            <dcpno>
                <name>Expeditionary TRICON Food Sanitation System (WHITE)</name>
                <partno>9-1-1121-4</partno>
                <cageno></cageno>
                <uoc>SHELTER, EXPANDABLE, ETFSS</uoc>
            </dcpno>
            <ui></ui>
            <qty>1</qty>
        </aal-entry>
         <aal-entry>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0296</niin>
            </nsn>
            <dcpno>
                <name>Expeditionary TRICON Food Sanitation System (BLUE)</name>
                <partno>9-1-1121-5</partno>
                <cageno></cageno>
                <uoc>SHELTER, EXPANDABLE, ETFSS</uoc>
            </dcpno>
            <ui></ui>
            <qty>1</qty>
        </aal-entry>
    </aal>
</aalwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-AAL.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def explistwp(self, wpno):
        """Function to create the EDIL List WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<explistwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>EXPENDABLE AND DURABLE ITEMS LIST</title>
    </wpidinfo>
    <intro>
        <para0>
            <title>INTRODUCTION</title>
            <subpara1>
                <title>Scope</title>
                <para>This work package lists expendable and durable items that you will need to operate and maintain the Containerized Kitchen (CK). This list is for information only and is not authority to requisition the listed items. These items are authorized to you by <extref docno="CTA 50-970" posttext=", Expendable/Durable Items (Except Medical, Class V Repair Parts, and Heraldic Items)"/>, <extref docno="CTA 50-909" posttext=", Field and Garrison Furnishings and Equipment"/> or <extref docno="CTA 8-100" posttext=", Army Medical Department Expendable/Durable Items"/>.</para>
            </subpara1>
            <subpara1>
                <title>Explanations of Columns in the Expendable/Durable Items List</title>
                <para>Column (1) Item No. This number is assigned to the entry in the list and is referenced in the narrative instructions to identify the item (e.g., Use brake fluid (WP 0098, item 5)).</para>
                <para>
                    Column (2) Level. This column includes the lowest level of maintenance that requires the listed item:
                    <randlist>
                        <item>C = Crew</item>
                    </randlist>
                </para>
                <para>Column (3) National Stock Number (NSN). This is the NSN assigned to the item which you can use to requisition it.</para>
                <para>Column (4) Item Name, Description, Part Number/(CAGEC). This column provides the other information you need to identify the item. The last line below the description is the part number and the Commercial and Government Entity Code (CAGEC) (in parentheses)</para>
                <para>Column (5) U/I. Unit of Issue (U/I) code shows the physical measurement or count of an item, such as gallon, dozen, gross, etc.</para>
            </subpara1>
        </para0>
    </intro>
    <explist>
        <title>Expendable and Durable Items List.</title>
        <!-- THESE ENTRIES ARE JUST EXAMPLES. YOU MUST FILL THEM IN WITH YOUR OWN DATA. -->
        <expdur-entry id="S00004-10-7360-226-EXP1">
            <itemno>1</itemno>
            <maintenance lvl="c"/>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0248</niin>
            </nsn>
            <name>Expeditionary TRICON Food Sanitation System (GREEN)</name>
            <desc></desc>
            <partno>9-1-1121-1</partno>
            <cageno></cageno>
            <ui></ui>
        </expdur-entry>
        <expdur-entry id="S00004-10-7360-226-EXP2">
            <itemno>2</itemno>
            <maintenance lvl="c"/>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0260</niin>
            </nsn>
            <name>Expeditionary TRICON Food Sanitation System (TAN)</name>
            <desc></desc>
            <partno>9-1-1121-2</partno>
            <cageno></cageno>
            <ui></ui>
        </expdur-entry>
        <expdur-entry id="S00004-10-7360-226-EXP3">
            <itemno>3</itemno>
            <maintenance lvl="c"/>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0272</niin>
            </nsn>
            <name>Expeditionary TRICON Food Sanitation System (RED)</name>
            <desc></desc>
            <partno>9-1-1121-3</partno>
            <cageno></cageno>
            <ui></ui>
        </expdur-entry>
        <expdur-entry id="S00004-10-7360-226-EXP4">
            <itemno>4</itemno>
            <maintenance lvl="c"/>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0284</niin>
            </nsn>
            <name>Expeditionary TRICON Food Sanitation System (WHITE)</name>
            <desc></desc>
            <partno>9-1-1121-4</partno>
            <cageno></cageno>
            <ui></ui>
        </expdur-entry>
        <expdur-entry id="S00004-10-7360-226-EXP5">
            <itemno>5</itemno>
            <maintenance lvl="c"/>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0296</niin>
            </nsn>
            <name>Expeditionary TRICON Food Sanitation System (BLUE)</name>
            <desc></desc>
            <partno>9-1-1121-5</partno>
            <cageno></cageno>
            <ui></ui>
        </expdur-entry>
    </explist>
</explistwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-EDIL.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def toolidwp(self, wpno):
        """Function to create the Tool Identification List WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<toolidwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>TOOL IDENTIFICATION LIST</title>
    </wpidinfo>
    <intro>
        <para0>
            <title>INTRODUCTION</title>
            <subpara1>
                <title>SCOPE</title>
                <para>This work package lists common tools and supplements and special tools/fixtures needed to maintain Expeditionary TRICON Self Serve Laundry System (ETSSLS).</para>
            </subpara1>
            <subpara1>
                <title>Explanation of Columns in the Tool Identification List</title>
                <para>
                    <emphasis emph="bold">Column (1) Item No.</emphasis> This number is assigned to entry in list and is referenced in initial setup to identify item (e.g., Extractor (WP 0090, item 32)).
                </para>
                <para>
                    <emphasis emph="bold">Column (2) Item Name.</emphasis> This column lists item by noun nomenclature and other descriptive features (e.g., Gauge, belt tension).
                </para>
                <para>
                    <emphasis emph="bold">Column (3) National Stock Number (NSN).</emphasis> This is the National Stock Number (NSN) assigned to item; use it to requisition item.
                </para>
                <para>
                    <emphasis emph="bold">Column (4) Part Number/(CAGEC).</emphasis> Indicates primary number used by manufacturer (individual, company, firm, corporation, or Government activity) which controls design and characteristics of item by means of its engineering drawings, specifications, standards, and inspection requirements to identify an item or range of items. Manufacturer&apos;s Commercial and Government Entity Code (CAGEC) is also included.
                </para>
                <para>
                    <emphasis emph="bold">Column (5) Reference.</emphasis> This column identifies authorizing supply catalog, components list, or RPSTL for items listed in this work package0.
                </para>
            </subpara1>
        </para0>
    </intro>
    <toolidlist>
        <title>Tool Identification List</title>
        <!-- THESE ENTRIES ARE JUST EXAMPLES. YOU MUST FILL THEM IN WITH YOUR OWN DATA. -->
        <tool-entry id="TIL_01">
            <itemno>1</itemno>
            <name>Expeditionary TRICON Food Sanitation System (GREEN)</name>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0248</niin>
            </nsn>
            <partcage>
                <partno>9-1-1121-1</partno>
                <cageno></cageno>
            </partcage>
            <extref docno="TM XX-XXXX-XXX" pretext="X"/>
        </tool-entry>
        <tool-entry id="TIL_02">
            <itemno>2</itemno>
            <name>Expeditionary TRICON Food Sanitation System (TAN)</name>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0260</niin>
            </nsn>
            <partcage>
                <partno>9-1-1121-2</partno>
                <cageno></cageno>
            </partcage>
            <extref docno="TM XX-XXXX-XXX" pretext="X"/>
        </tool-entry>
        <tool-entry id="TIL_03">
            <itemno>3</itemno>
            <name>Expeditionary TRICON Food Sanitation System (RED)</name>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0272</niin>
            </nsn>
            <partcage>
                <partno>9-1-1121-3</partno>
                <cageno></cageno>
            </partcage>
            <extref docno="TM XX-XXXX-XXX" pretext="X"/>
        </tool-entry>
        <tool-entry id="TIL_04">
            <itemno>4</itemno>
            <name>Expeditionary TRICON Food Sanitation System (WHITE)</name>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0284</niin>
            </nsn>
            <partcage>
                <partno>9-1-1121-4</partno>
                <cageno></cageno>
            </partcage>
            <extref docno="TM XX-XXXX-XXX" pretext="X"/>
        </tool-entry>
        <tool-entry id="TIL_05">
            <itemno>5</itemno>
            <name>Expeditionary TRICON Food Sanitation System (BLUE)</name>
            <nsn>
                <fsc>5419</fsc>
                <niin>01-686-0296</niin>
            </nsn>
            <partcage>
                <partno>9-1-1121-5</partno>
                <cageno></cageno>
            </partcage>
            <extref docno="TM XX-XXXX-XXX" pretext="X"/>
        </tool-entry>
    </toolidlist>
</toolidwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-TIL.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def mrplwp(self, wpno):
        """Function to create the Mandatory Replacement Parts WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<mrplwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>MANDATORY REPLACEMENT PARTS LIST</title>
    </wpidinfo>
    <intro>
        <para0>
            <title>INTRODUCTION</title>
            <subpara1>
                <title>SCOPE</title>
                <para>This work package includes a list of all the mandatory replacement parts referenced in the task initial setups and procedures including those referenced in Preventive Maintenance Checks and Services. These are items that must be replaced during maintenance whether they have failed or not. This includes items based on usage intervals such as miles, time, rounds fired, etc.</para>
            </subpara1>
            <subpara1>
                <title>Explanation of Columns in the Mandatory Replacement Parts List</title>
                <para>Column (1) Item No. This number is assigned to the entry in the list and is referenced in the narrative instructions to identify the item (e.g., Use O-ring (WP 0098, item 5)).</para>
                <para>Column (2) Part Number (CAGEC). Identifies the part number and CAGEC of the item to be used for requisitioning purposes.</para>
                <para>Column (3) National Stock Number (NSN) Identifies the stock number of the item to be used for requisitioning purposes.</para>
                <para>Column (4) Description This column lists the item by noun nomenclature and other descriptive features (e.g., Gauge, belt tension).</para>
                <para>Column (5) Qty. Indicates the quantity required.</para>
            </subpara1>
        </para0>
    </intro>
    <mrpl>
        <title>Mandatory Replacement Parts</title>
        <!-- THESE ENTRIES ARE JUST EXAMPLES. YOU MUST FILL THEM IN WITH YOUR OWN DATA. -->
        <mrpl-entry id="S00008-XX-XXXX-XXX-MRP_01">
            <itemno>1</itemno>
            <partno>MS21044C3</partno>
            <cageno>80205</cageno>
            <nsn>
                <fsc>5310</fsc>
                <niin>00-208-9255</niin>
            </nsn>
            <name>NUT, SELF-LOCKING, HEXAGON (#10-32, CRES)</name>
            <qty>1</qty>
        </mrpl-entry>
        <mrpl-entry id="S00008-XX-XXXX-XXX-MRP_02">
            <itemno>1</itemno>
            <partno></partno>
            <cageno></cageno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <name></name>
            <qty></qty>
        </mrpl-entry>
        <mrpl-entry id="S00008-XX-XXXX-XXX-MRP_03">
            <itemno>1</itemno>
            <partno></partno>
            <cageno></cageno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <name></name>
            <qty></qty>
        </mrpl-entry>
        <mrpl-entry id="S00008-XX-XXXX-XXX-MRP_04">
            <itemno>1</itemno>
            <partno></partno>
            <cageno></cageno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <name></name>
            <qty></qty>
        </mrpl-entry>
        <mrpl-entry id="S00008-XX-XXXX-XXX-MRP_05">
            <itemno>1</itemno>
            <partno></partno>
            <cageno></cageno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <name></name>
            <qty></qty>
        </mrpl-entry>
        
    </mrpl>
</mrplwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-MRP.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def csi_wp(self, wpno):
        """Function to create the Critical Safety Items WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<csi.wp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
		<maintlvl level="operator"/>
		<title>CRITICAL SAFETY ITEMS</title>
	</wpidinfo>
    <csi>
        <intro>
            <para0>
                <title>Introduction</title>
                <para>There are no critical safety items for the...</para>
            </para0>
        </intro>   
		<csi.tab>
			<title>Critical Safety Items List</title>
            <!-- THESE ENTRIES ARE JUST EXAMPLES. YOU MUST FILL THEM IN WITH YOUR OWN DATA. -->
			<csi-entry>
				<name>Expeditionary TRICON Food Sanitation System (GREEN)</name>
				<partno>9-1-1121-1</partno>
                <cageno></cageno>
                <desc></desc>
			</csi-entry>
            <csi-entry>
				<name>Expeditionary TRICON Food Sanitation System (TAN)</name>
				<partno>9-1-1121-2</partno>
                <cageno></cageno>
                <desc></desc>
			</csi-entry>
            <csi-entry>
				<name>Expeditionary TRICON Food Sanitation System (RED)</name>
				<partno>9-1-1121-3</partno>
                <cageno></cageno>
                <desc></desc>
			</csi-entry>
            <csi-entry>
				<name>Expeditionary TRICON Food Sanitation System (WHITE)</name>
				<partno>9-1-1121-4</partno>
                <cageno></cageno>
                <desc></desc>
			</csi-entry>
            <csi-entry>
				<name>Expeditionary TRICON Food Sanitation System (BLUE)</name>
				<partno>9-1-1121-6</partno>
                <cageno></cageno>
                <desc></desc>
			</csi-entry>
		</csi.tab>
	</csi>
</csi.wp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-CSI.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def supitemwp(self, wpno):
        """Function to create the Support Items WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<supitemwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
		<maintlvl level="operator"/>
		<title>SUPPORT ITEMS</title>
	</wpidinfo>
	<!-- OPTIONAL WORK PACKAGES -->
    <!-- intro?, (coei, bii)?, aal?, explist?, toolidlist?, mrpl?, csi? -->
    <intro>
        <para0>
            <title>Lorem Ipsum</title>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</para>
        </para0>
    </intro>  
</supitemwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-SupportItems.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def genwp(self, wpno):
        """Function to create the Support Items WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += f'<genwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
		<maintlvl level="operator"/>
		<title>ADDITIONAL SUPPORTING WORK PACKAGES</title>
	</wpidinfo>\n'''
        tmp += isb()
        tmp += '''<proc>
        <title>Lorem Ipsum</title>
        <step1>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
        </step1>
        <step1>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
        </step1>
        <step1>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
        </step1>
        <step1>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
        </step1>
        <step1>
            <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
        </step1>
    </proc>  
</genwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-AdditionalSupportingWP.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self):
        """ Function to create Supporting Info section end tags. """
        tmp = '</sim>'
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-SUPPORT_INFO_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
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
            