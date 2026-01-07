"""SUPPORTING INFORMATION"""

import datetime
import math

import cfg
import views.isb as isb
import views.metadata as md


class SupportingInformation:
    """Class to create various types of WP's included in Supporting Info section of a TM."""

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
        """Function to create Supporting Info section start tags."""
        # cfg.prefix_file = math.floor(cfg.prefix_file / 1000) * 1000
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
    <sim chngno="0" revno="0" chap-toc="no">\n"""
        tmp += '\t<titlepg maintlvl="operator">\n'
        tmp += "\t\t<name>" + self.sys_name + " (" + self.sys_acronym + ")</name>\n"
        tmp += "\t</titlepg>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-SUPPORT_INFO_START.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def refwp(self, wpno) -> None:
        """Function to create References WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE refwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE refwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += (
                f'<!DOCTYPE refwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
            )
        tmp += f'<refwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("refwp", self.tmno)

        tmp += """\t<wpidinfo>
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
</refwp>"""
        with open(
            (
                f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-References.xml"
            ),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def macintrowp(self, wpno) -> None:
        """Function to create the Introduction WP for the MAC."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE macintrowp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE macintrowp PUBLIC "{self.FPI_2D}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE macintrowp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<macintrowp wpno="{wpno}-{self.tmno}" chngno="0" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("macintrowp", self.tmno)

        tmp += """\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>MAINTENANCE ALLOCATION CHART (MAC) INTRODUCTION</title>
    </wpidinfo>
    <intro>
        <para0>
            <title>INTRODUCTION</title>
            <subpara1>
                <title>The Army Maintenance System MAC</title>
                <para>This introduction provides a general explanation of the maintenance levels/classes, tasks, and other information contained in the MAC. The MAC designates overall authority and responsibility for the performance of all maintenance tasks on the identified end item or component. The application of the maintenance tasks to the end item or component shall be consistent with the capacities and capabilities of the designated maintenance levels/classes that are shown in the MAC in column (4). Column (4) is divided into two secondary columns. These columns indicate the maintenance levels/classes of &quot;Field&quot; and &quot;Sustainment.&quot; Each maintenance level column is further divided into two sub-columns. These sub-columns identify the maintenance classes and are as follows:
                     <seqlist>
                        <item>Field level maintenance classes:
						<seqlist>
							<item>Crew (operator) maintenance. This is the responsibility of a using organization to perform maintenance on its assigned equipment. It normally consists of inspecting, servicing, lubricating, adjusting, and replacing parts, minor assemblies, and subassemblies. Items with a &quot;C&quot; (&quot;O&quot; for joint service reporting) in the third position of the Source, Maintenance, and Recoverability (SMR) code may be replaced at the crew(operator) class. A code of &quot;C&quot; (&quot;O&quot; for joint service) in the fourth position of the SMR code indicates complete repair is authorized at the crew (operator) class.</item>
							<item>Maintainer maintenance. This is maintenance accomplished on a component, accessory, assembly, subassembly, plug-in unit, or other portion by field-level units. This maintenance is performed either on the system or after it is removed. An &quot;F&quot; in the third position of the SMR code indicates replacement of assemblies, subassemblies, or other components is authorized at this level. An &quot;F&quot; in the fourth position of the SMR code indicates complete repair of the identified item is allowed at the Maintainer class. Items repaired at this level are normally returned to the user after maintenance is performed.</item>
                            </seqlist>
                        </item>
                        <item>Sustainment level maintenance classes: <seqlist>
                                <item>Depot. This is maintenance accomplished on a component, accessory, assembly, subassembly, plug-in unit, or other portion either on the system or after it is removed. Assets to be repaired at this class are normally returned to an Army Depot or authorized contractor facility. The &quot;replace&quot; task for this class of maintenance is indicated by the letter &quot;D&quot; or &quot;K&quot; appearing in the third position of the SMR code. A &quot;D&quot; or &quot;K&quot; appearing in the fourth position of the SMR code indicates complete repair is possible at the depot sustainment maintenance level. Items are returned to the supply system after maintenance is performed at this class.</item>
                            </seqlist>
                        </item>
                    </seqlist>
                </para>
                <para>The tools and test equipment requirements table (immediately following the MAC) lists the tools and test equipment (both special tools/kits and common tool sets) required for each maintenance task as referenced from the MAC. The remarks table (immediately following the tools and test equipment requirements) contains supplemental instructions and explanatory notes for a particular maintenance task.</para>
            </subpara1>
            <subpara1>
                <title>Maintenance tasks</title>
                <para>Maintenance tasks are limited to and defined as follows:
					<seqlist>
                        <item>Inspect. Step-by-step instructions to determine the serviceability of an item by comparing its physical, mechanical, and/or electrical characteristics with established standards through examination (e.g., by sight, sound, or feel).</item>
                        <item>Test. Step-by-step instructions to verify serviceability by measuring the mechanical, pneumatic, hydraulic, or electrical characteristics of an item and comparing those characteristics with prescribed standards, e.g., load testing of lift devices or hydrostatic testing of pressure hoses. For software, to verify usability/operability/functionality of the software.</item>
                        <item>Service. Step-by-step instructions to be performed periodically to keep an item in proper operating condition, such as replenishing fuel, lubricants, chemical fluids, or gases.</item>
                        <item>Remove. Step-by-step instructions for taking a component off an asset to facilitate other maintenance on a different component or on the same component (except for &quot;Replace&quot; and &quot;Repair.&quot; For software, it is step-by-step instructions for uninstalling/removing the software from a workstation or other viewing hardware.</item>
                        <item>Install. Step-by-step instructions for placing, positioning, or otherwise locating a component to make it part of a higher level end item. The &quot;install&quot; task is authorized by the LPD/MAC and the assigned maintenance level is shown as the third position code of the SMR code. For software, it is step-by-step instructions putting the software on a workstation or other viewing hardware.</item>
                        <item>Replace. Step-by-step instructions for taking off an unserviceable component and putting a serviceable component in its place. The &quot;replace&quot; task is authorized by the LPD/MAC and the assigned maintenance level is shown as the third position code of the SMR code.</item>
                        <item>Repair. Step-by-step instructions for restoring an item or software to a completely serviceable or fully mission capable status. The &quot;repair&quot; task is authorized by the LPD/MAC and the assigned maintenance level is shown as the fourth position code of the SMR code. The following definitions are applicable to the &quot;repair&quot; maintenance task: welding, grinding, riveting, straightening, facing, machining, and/or resurfacing.</item>
                        <item>Prepare for use. Step-by-step instructions required to make an asset ready for other maintenance (e.g., &quot;remove preservatives,&quot; &quot;lubricate,&quot; etc.).</item>
                        <item>Clean. Step-by-step instructions on how to remove dirt, corrosion, or other contaminants from equipment. Refer to appropriate painting, lubrication, and preservation methods to restore original corrosion prevention and control methods when removed as a result of cleaning and/or when using cleaning to remove corrosion from the item.</item>
                        <item>Place in service. Step-by-step instructions required to place an item into service that are not covered in the service upon receipt work package.</item>
                        <item>Preparation for storage. Step-by-step instructions for preparing the equipment for placement into administrative, short term, and/or long-term storage.</item>
                        <item>Preparation for shipment. Step-by-step instructions for preparing the equipment to be shipped or transported.</item>
						<item>Transport. Step-by-step instructions and guidance for transporting/shipping the equipment.</item>
						<item>Adjust. Step-by-step instructions to maintain or regulate, within prescribed limits, by bringing into proper position, or by setting the operating characteristics to specified parameters.</item>
						<item>Align. Step-by-step instructions to adjust specified variable elements of an item to bring about optimum or desired performance.</item>
						<item>Calibrate. Step-by-step instructions to determine and cause corrections to be made or to be adjusted on instruments of test, measuring, and diagnostic equipment used in precision measurement. It consists of comparisons of two instruments, one of which is a certified standard of known accuracy, to detect and adjust any discrepancy in the accuracy of the instrument being compared.</item>
						<item>Paint. Step-by-step instructions to prepare and apply coats of paint. When used for ammunition, the paint is applied to the ammunition and its packaging so they can be identified and protected.</item>
						<item>Overhaul. Step-by-step instructions to restore an item to a completely serviceable/operational condition as required by maintenance standards in the appropriate technical publications. &quot;Overhaul&quot; is normally the highest degree of maintenance performed by the Army. &quot;Overhaul&quot; does not normally return an item to a like new condition.</item>
						<item>Rebuild. Step-by-step instructions required for the restoration of unserviceable equipment to a like new condition in accordance with original manufacturing standards. &quot;Rebuild&quot; is the highest degree of materiel maintenance applied to Army equipment. The &quot;rebuild&quot; operation includes the act of returning to zero those age measurements (e.g., hours/miles) considered in classifying Army equipment/components.</item>
						<item>Lubricate. Step-by-step instructions for applying a material (e.g., oil or grease) to reduce friction and allow a component to operate in a more efficient manner.</item>
						<item>Mark. Step-by-step instructions for restoring obliterated identification on an asset.</item>
                        <item>Pack. Step-by-step instructions to place an item into a container for either storage or shipment after service and other maintenance operations have been completed.</item>
                        <item>Unpack. Step-by-step instructions for removing an asset from a storage or shipping container in preparation to perform further maintenance (e.g., &quot;repair&quot; or &quot;install&quot;).</item>
						<item>Preserve. Step-by-step instructions for treating systems and equipment, whether installed or stored, to ensure a serviceable condition.</item>
						<item>Assemble. Step-by-step instructions to join the component pieces of an asset together to make a complete serviceable asset.</item>
						<item>Disassemble. Step-by-step instructions to break down (take apart) a spare/functional group coded item to the level of its least component, which is assigned an SMR code for the level of maintenance under consideration (i.e., identified as maintenance significant).</item>
						<item>Nondestructive inspection. Step-by-step instructions on preparation and accomplishment inspections that do not destroy or damage the equipment.</item>
						<item>Radio interference suppression. Step-by-step instructions to ensure installed equipment, either communication or other electronics, does not interfere with installed communication equipment.</item>
						<item>Towing. Step-by-step instructions to connect one vehicle to another for the purpose of having one vehicle moved through the motive power of the other vehicle.</item>
						<item>Jacking. Step-by-step instructions to mechanically raise or lift a vehicle to facilitate maintenance on the vehicle.</item>
						<item>Parking. Step-by-step instructions to safely place a vehicle in a lot, ramp area or other designated location.</item>
						<item>Mooring. Step-by-step instructions to secure a vehicle by chains, ropes or other means to protect the vehicle from environmental conditions or secure for transportation.</item>
						<item>Covering. Step-by-step instructions to place a protective wrapping over a vehicle to protect it from environmental conditions or to hide (e.g., camouflage) it.</item>
						<item>Hoisting. Step-by-step instructions to allow a vehicle to be raised by cables or ropes through attaching points.</item>
						<item>Sling loading. Step-by-step instructions to place a sling around a vehicle to allow it to be raised.</item>
						<item>External power. Step-by-step instructions on how to apply electrical power from any authorized power source (e.g., external generator or facility power).</item>
                        <item>Arm. Step-by-step instructions on activating ammunition prior to use.</item>
                        <item>Load. Step-by-step instructions for one of two tasks:
							<seqlist>
                                <item>For transportation, the act of placing assets onto a transportation medium (e.g., pallet, truck, container).</item>
                                <item>For weapons/weapons systems, the act of placing ammunition into the weapon/weapons system.</item>
                            </seqlist>
                        </item>
                        <item>Unload. Step-by-step instructions for one of two tasks:
							<seqlist>
                                <item>For transportation, the act of removing assets from a transportation medium (e.g., pallet, truck, container).</item>
                                <item>For weapons/weapons systems, the act of removing ammunition from the weapon/weapons system.</item>
                            </seqlist>
                        </item>
						<item>Install peripheral device. Step-by-step instructions for installing peripheral devices such as printers, scanners, modems, etc.</item>
						<item>Uninstall peripheral device. Step-by-step instructions for uninstalling peripheral devices such as printers, scanners, modems, etc.</item>
						<item>Upgrade/patch. Step-by-step instructions for performing an upgrade to software or installing a patch to software.</item>
						<item>Configure. Step-by-step instructions for configuring software for different uses/purposes and/or different users.</item>
						<item>Debug. Step-by-step instructions for debugging software/correcting errors in the software.</item>
                    </seqlist>
                </para>
            </subpara1>
            <subpara1>
                <title>Explanation of Columns in the MAC</title>
                <para>Column (1) Group Number. Column (1) lists Functional Group Code (FGC) numbers, the purpose of which is to identify maintenance significant components, assemblies, subassemblies, and modules with the Next Higher Assembly (NHA).</para>
                <para>Column (2) Component/Assembly. Column (2) contains the item names of components, assemblies, subassemblies, and modules for which maintenance is authorized.</para>
                <para>Column (3) Maintenance task. Column (3) lists the tasks to be performed on the item listed in column (2). (For a detailed explanation of these tasks, refer to maintenance tasks outlined above.)</para>
                <para>Column (4) Maintenance Level. Column (4) specifies each level/class of maintenance authorized to perform each task listed in column (3), by indicating man-hours required in the appropriate sub-column. The man-hour figure is the task time multiplied by the number of maintainers required to perform that maintenance task. This time includes preparation (equipment conditions, inspections), task performance, follow-on maintenance and quality assurance (inspections) time. Crew maintenance time will be entered as task (clock) time only. If different maintenance classes perform the same maintenance tasks due to the number or complexity of the tasks, appropriate man-hour figures are to be shown for each class. The symbol designations for the various maintenance levels and classes are as follows:
					<randlist>
                        <item><emphasis emph="uline">Field</emphasis>: <randlist>
                                <item>C Crew Maintenance</item>
                                <item>F Maintainer maintenance</item>
                            </randlist>
                        </item>
                        <item><emphasis emph="uline">Sustainment</emphasis>:
							<randlist>
                                <item>L Special Repair Authority (SRA)</item>
                                <item>D Depot maintenance</item>
                            </randlist>
                            <note>
                                <trim.para>The &quot;L&quot; maintenance class is not included in column (4) of the MAC. Functions to this class of maintenance are identified by work time figure in the &quot;H&quot; column of column (4), and an associated reference code is used in the REMARKS column (6). This code is keyed to the remarks and the SRA complete repair application is explained there.</trim.para>
                            </note>
                        </item>
                    </randlist>
                </para>
                <para>Column (5) Tools and Equipment Reference Code. Column (5) specifies, by a number code, those common tool sets, kits, or outfits (not individual tools), common Test, Measurement and Diagnostic Equipment (TMDE), common tools that are not part of a set, kit, or outfit, special tools/kits, special TMDE, and special support equipment required to perform the designated function. Codes are keyed to the entries in the tools and test equipment table.</para>
                <para>Column (6) Remarks Code. When applicable, this Column (6) contains a letter code, in alphabetical order, that is keyed to the remarks table entries.</para>
            </subpara1>
            <subpara1>
                <title>Explanation of Columns in the Tools and Test Equipment Requirements</title>
                <para>
                    <randlist>
                        <item>Column (1) Tool or Test Equipment Reference Code. The tool or test equipment reference code correlates with a code used in column (5) of the MAC.</item>
                        <item>Column (2) Maintenance Level. The lowest class of maintenance authorized to use the tool or test equipment.</item>
                        <item>Column (3) Nomenclature. Name or identification of the tool or test equipment.</item>
                        <item>Column (4) National Stock Number (NSN). The NSN of the tool or test equipment.</item>
                        <item>Column (5) Tool Number. The manufacturer&apos;s part number</item>
                    </randlist>
                </para>
            </subpara1>
            <subpara1>
                <title>Explanation of Columns in the Remarks</title>
                <para>
                    <randlist>
                        <item>Column (1) Remarks Code. The code recorded in column (6) of the MAC.</item>
                        <item>Column (2) Remarks. This column lists information pertinent to the maintenance task being performed as indicated in the MAC.</item>
                    </randlist>
                </para>
            </subpara1>
        </para0>
    </intro>
</macintrowp>"""

        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-MAC Introduction.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def macwp(self, wpno) -> None:
        """Function to create the MAC WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE macwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE macwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += (
                f'<!DOCTYPE macwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
            )
        tmp += f'<macwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("macwp", self.tmno)

        tmp += """\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>MAINTENANCE ALLOCATION CHART (MAC)</title>
    </wpidinfo>
    <mac>
        <title>Maintenance Allocation Chart for ...</title>
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
    </mac>
    <?Pub _newpage?>
    <tereqtab>
        <title>Tools and Test Equipment for ...</title>
        <teref-group>
            <terefcode id=""></terefcode>
            <maintenance lvl=""/>
            <name></name>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <toolno></toolno>
        </teref-group>
        <teref-group>
            <terefcode id=""></terefcode>
            <maintenance lvl=""/>
            <name></name>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <toolno></toolno>
        </teref-group>
        <teref-group>
            <terefcode id=""></terefcode>
            <maintenance lvl=""/>
            <name></name>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <toolno></toolno>
        </teref-group>
        <teref-group>
            <terefcode id=""></terefcode>
            <maintenance lvl=""/>
            <name></name>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <toolno></toolno>
        </teref-group>
        <teref-group>
            <terefcode id=""></terefcode>
            <maintenance lvl=""/>
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
        <remark-group>
            <remarkcode id=""></remarkcode>
            <remarks></remarks>
        </remark-group>
        <remark-group>
            <remarkcode id=""></remarkcode>
            <remarks></remarks>
        </remark-group>
        <remark-group>
            <remarkcode id=""></remarkcode>
            <remarks></remarks>
        </remark-group>
        <remark-group>
            <remarkcode id=""></remarkcode>
            <remarks></remarks>
        </remark-group>
        <remark-group>
            <remarkcode id=""></remarkcode>
            <remarks></remarks>
        </remark-group>
    </remarktab>
</macwp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-MAC.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def coeibiiwp(self, wpno) -> None:
        """Function to create the COEI & BII Lists WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE coeibiiwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE coeibiiwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE coeibiiwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<coeibiiwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("coeibiiwp", self.tmno)

        tmp += """\t<wpidinfo>
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
        <coei-opt-entry>
            <itemno id=""></itemno>
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
            <itemno id=""></itemno>
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
            <itemno id=""></itemno>
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
    <bii-opt id="biitab">
        <title>Basic Issue Items (BII) List</title>
        <bii-opt-entry>
            <itemno id=""></itemno>
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
            <itemno id=""></itemno>
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
            <itemno id=""></itemno>
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
</coeibiiwp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-COEI BII List.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def aalwp(self, wpno) -> None:
        """Function to create the Additional Authorization List (AAL) WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE aalwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE aalwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += (
                f'<!DOCTYPE aalwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
            )
        tmp += f'<aalwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("aalwp", self.tmno)

        tmp += """\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>ADDITIONAL AUTHORIZATION LIST (AAL)</title>
    </wpidinfo>
    <intro>
        <para0>
            <title>INTRODUCTION</title>
            <subpara1>
                <title>Scope</title>
                <para>This work package lists additional items you are authorized for the support of the INSERT TM NAME HERE.</para>
            </subpara1>
            <subpara1>
                <title>General</title>
                <para>This list identifies items that do not have to accompany the INSERT TM NAME HERE and that do not have to be turned in with it. These items are all authorized to you by CTA, MTOE, TDA, or JTA.</para>
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
        <aal-entry>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <dcpno>
                <name></name>
                <partno></partno>
                <cageno></cageno>
                <uoc></uoc>
            </dcpno>
            <ui></ui>
            <qty></qty>
        </aal-entry>
        <aal-entry>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <dcpno>
                <name></name>
                <partno></partno>
                <cageno></cageno>
                <uoc></uoc>
            </dcpno>
            <ui></ui>
            <qty></qty>
        </aal-entry>
        <aal-entry>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <dcpno>
                <name></name>
                <partno></partno>
                <cageno></cageno>
                <uoc></uoc>
            </dcpno>
            <ui></ui>
            <qty>1</qty>
        </aal-entry>
    </aal>
</aalwp>"""
        with open(
            (
                f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-AAL.xml"
            ),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def explistwp(self, wpno) -> None:
        """Function to create the EDIL List WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE explistwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE explistwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE explistwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<explistwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("explistwp", self.tmno)

        tmp += """\t<wpidinfo>
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
        <expdur-entry id="">
            <itemno></itemno>
            <maintenance lvl=""/>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <name></name>
            <desc></desc>
            <partno></partno>
            <cageno></cageno>
            <ui></ui>
        </expdur-entry>
        <expdur-entry id="">
            <itemno></itemno>
            <maintenance lvl=""/>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <name></name>
            <desc></desc>
            <partno></partno>
            <cageno></cageno>
            <ui></ui>
        </expdur-entry>
        <expdur-entry id="">
            <itemno></itemno>
            <maintenance lvl=""/>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <name></name>
            <desc></desc>
            <partno></partno>
            <cageno></cageno>
            <ui></ui>
        </expdur-entry>
    </explist>
</explistwp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-EDIL.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def toolidwp(self, wpno) -> None:
        """Function to create the Tool Identification List WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE toolidwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE toolidwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE toolidwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<toolidwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("toolidwp", self.tmno)

        tmp += """\t<wpidinfo>
        <maintlvl level="operator"/>
        <title>TOOL IDENTIFICATION LIST</title>
    </wpidinfo>
    <intro>
        <para0>
            <title>INTRODUCTION</title>
            <subpara1>
                <title>SCOPE</title>
                <para>This work package lists common tools and supplements and special tools/fixtures needed to maintain Expeditionary TRICON Self Serve Laundry System (INSERT TM NAME HERE).</para>
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
        <tool-entry id="">
            <itemno></itemno>
            <name></name>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <partcage>
                <partno></partno>
                <cageno></cageno>
            </partcage>
            <extref docno="" pretext=""/>
        </tool-entry>
        <tool-entry id="">
            <itemno></itemno>
            <name></name>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <partcage>
                <partno></partno>
                <cageno></cageno>
            </partcage>
            <extref docno="" pretext=""/>
        </tool-entry>
        <tool-entry id="">
            <itemno></itemno>
            <name></name>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <partcage>
                <partno></partno>
                <cageno></cageno>
            </partcage>
            <extref docno="" pretext=""/>
        </tool-entry>
    </toolidlist>
</toolidwp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-TIL.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def mrplwp(self, wpno) -> None:
        """Function to create the Mandatory Replacement Parts WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE mrplwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE mrplwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE mrplwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<mrplwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("mrplwp", self.tmno)

        tmp += """\t<wpidinfo>
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
        <mrpl-entry id="">
            <itemno></itemno>
            <partno></partno>
            <cageno></cageno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <name></name>
            <qty></qty>
        </mrpl-entry>
        <mrpl-entry id="">
            <itemno></itemno>
            <partno></partno>
            <cageno></cageno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <name></name>
            <qty></qty>
        </mrpl-entry>
        <mrpl-entry id="">
            <itemno></itemno>
            <partno></partno>
            <cageno></cageno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <name></name>
            <qty></qty>
        </mrpl-entry>
        <mrpl-entry id="">
            <itemno></itemno>
            <partno></partno>
            <cageno></cageno>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <name></name>
            <qty></qty>
        </mrpl-entry>
        <mrpl-entry id="">
            <itemno></itemno>
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
</mrplwp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-MRP.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def csi_wp(self, wpno) -> None:
        """Function to create the Critical Safety Items WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE csi.wp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE csi.wp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE csi.wp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<csi.wp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("csi.wp", self.tmno)

        tmp += """\t<wpidinfo>
		<maintlvl level="operator"/>
		<title>CRITICAL SAFETY ITEMS</title>
	</wpidinfo>
    <csi>
        <intro>
            <para0>
                <title>Introduction</title>
                <para></para>
            </para0>
        </intro>
		<csi.tab>
			<title>Critical Safety Items List</title>
			<csi-entry>
				<name></name>
				<partno></partno>
                <cageno></cageno>
                <desc></desc>
			</csi-entry>
            <csi-entry>
				<name></name>
				<partno></partno>
                <cageno></cageno>
                <desc></desc>
			</csi-entry>
            <csi-entry>
				<name></name>
				<partno></partno>
                <cageno></cageno>
                <desc></desc>
			</csi-entry>
            <csi-entry>
				<name></name>
				<partno></partno>
                <cageno></cageno>
                <desc></desc>
			</csi-entry>
            <csi-entry>
				<name></name>
				<partno></partno>
                <cageno></cageno>
                <desc></desc>
			</csi-entry>
		</csi.tab>
	</csi>
</csi.wp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-CSI.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def supitemwp(self, wpno) -> None:
        """Function to create the Support Items WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE supitemwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE supitemwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE supitemwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<supitemwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("supitemwp", self.tmno)

        tmp += """\t<wpidinfo>
		<maintlvl level="operator"/>
		<title>SUPPORT ITEMS</title>
	</wpidinfo>
	<!-- OPTIONAL WORK PACKAGES -->
    <!-- intro?, (coei, bii)?, aal?, explist?, toolidlist?, mrpl?, csi? -->
    <intro>
        <para0>
            <title></title>
            <para></para>
        </para0>
    </intro>
</supitemwp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-Support Items.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def genwp(self, wpno) -> None:
        """Function to create the Support Items WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE genwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE genwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += (
                f'<!DOCTYPE genwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
            )
        tmp += f'<genwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("genwp", self.tmno)

        tmp += """\t<wpidinfo>
		<maintlvl level="operator"/>
		<title>ADDITIONAL SUPPORTING WORK PACKAGES</title>
	</wpidinfo>\n"""
        tmp += isb.show()
        tmp += """<proc>
        <title></title>
        <step1>
            <para></para>
        </step1>
        <step1>
            <para></para>
        </step1>
        <step1>
            <para></para>
        </step1>
        <step1>
            <para></para>
        </step1>
        <step1>
            <para></para>
        </step1>
    </proc>
</genwp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-Additional Supporting WP.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create Supporting Info section end tags."""
        tmp = "</sim>"
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-SUPPORT_INFO_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
