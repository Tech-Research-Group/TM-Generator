"""DEPOT PROCEDURES"""
import math
import cfg

class DepotProcedures:
    """Class to create various types of WP's included in Depot Procedures of a TM."""
    def __init__(self, manual_type, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function to create Depot Procedures start tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
    <mim chngno="0" revno="0" chap-toc="no">\n'''
        tmp += '\t<titlepg maintlvl="depot">\n'
        tmp += '\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')</name>\n'
        tmp += '\t</titlepg>\n'
        tmp += '\t<depotcategory>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-DEPOT_START.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def ppmgeninfowp(self, wpno):
        """Function to create the Preservation, Packaging, and Marking General Information WP."""
        tmp = f'<ppmgeninfowp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '''<wpidinfo>
        <maintlvl level="depot"/>
        <title>PRESERVATION, PACKAGING, AND MARKING GENERAL INFORMATION</title>
    </wpidinfo>
    t<geninfo>
        <para0>
            <title>PACKAGING</title>
            <para>Military preservation, Level A packing, and marking shall be accomplished in accordance with the specific packaging instructions <xref wpid="M00701-10-5419-215"/>.</para>
        </para0>
        <para0>
            <title>MARKING FOR STORAGE AND SHIPMENT</title>
            <para>Storage: In addition to any special markings called out on the special packaging instruction (SPI) or in the packaging requirements code, all unit packages, intermediate packs, exterior shipping containers, and, as applicable, unitized loads shall be marked in accordance with <extref docno="MIL-STD-129"/> including bar coding. The repair facility is responsible for application of special markings as required by <extref docno="MIL-STD-129"/> regardless of whether specified in the contract/order or not. Special markings include, but are not limited to, Shelf-life markings, structural markings, and transportation special handling markings. The marking of pilferable and sensitive materiel will not identify the nature of the materiel.</para>
            <para>Shipment: The repair facility shall apply identification and address markings with bar codes in accordance with <extref docno="MIL-STD-129"/>. A Military Shipment Label (MSL) is required for all shipments except contractor to contractor. The MSL will include both linear and 2D bar codes per the standard.</para>
            <para>Military Shipping Label: Military Shipment Labels may be created using the Computer Automated Transportation Tool Military Shipment Label/Issue Receipt Release Document (CATT MSL/IRRD).</para>
        </para0>
        <para0>
            <title>HEAT TREATMENT AND MARKING OF WOOD PACKAGING MATERIALS</title>
            <para>Wood Packaging Materials (WPM) (e.g., boxes, crates, skids, pallets, and any wood used as inner packaging made of non-manufactured wood) shall be constructed of lumber that has been heat-treated in accordance with the requirements of International Standard for Phytosanitary Measures (ISPM) –15. The WPM manufacturer shall be affiliated with an inspection agency accredited by the board of review of the American Lumber Standard Committee. The WPM manufacturer shall ensure traceability to the original source of heat treatment. Each piece of WPM shall be marked to show the conformance to the International Plant Protection Convention Standard. Certification markings shall be indelible and permanent. They may be stamped, stenciled, or branded directly onto or into the WPM. Certification marks shall be applied in a visible location on at least two opposite sides of the wood packaging product but are not required on each individual component piece of a wood packaging product. On dunnage, the marking shall be applied every 2 feet to opposite surfaces of each piece. If possible, the mark shall be visible when the dunnage is placed in the load to enable inspectors to verify the WPM’s compliance without unloading or unstuffing the container. Foreign manufacturers shall have the heat treatment of WPM verified in accordance with their National Plant Protection Organization’s compliance program.</para>
        </para0>
        <para0>
            <title>ALTERNATIVES</title>
            <para>The packaging requirements have been validated and the method of preservation/packing has proven successful in meeting the needs of the military distribution system, including undefined storage and shipment throughout the world. Tailoring of the packaging instructions may only be authorized by the packaging requirements developer. If tailored, prototype package is required to validate the sizes and fit requirements. Minor dimensional and size changes are acceptable provided email notification is provided to the packaging requirements developer. Any design changes or changes in the method of preservation that provide a cost savings without degrading the method of preservation or packing or affecting the serviceability of the item will be considered and responded to within 10 days of submission. The equipment proponent reserves the right to require testing to validate alternate preservation methods, materials, alternates, blocking, bracing, cushioning, and packing.</para>
        </para0>
        <para0>
            <title>REUSE OF PACKAGING MATERIALS</title>
            <para>The cushioning material and the fiberboard boxes may be reused provided:</para>
            <para>
                <randlist>
                    <item label="a.">There is no visible damage to material.</item>
                    <item label="b.">The foam cushioning has not taken a permanent set.</item>
                    <item label="c.">The fiberboard has no punctures, delaminating, or crushed flutes.</item>
                </randlist>
            </para>
            <para>The water vapor proof barrier bag shall never be reused. Always use new barrier material, evacuate air from the barrier bag, and conduct a snap test after 2 hours on each bag to ensure seal is holding. All components of the wood box/crate must be present, properly secured in position, and not broken. Splits are acceptable provided the boards remain secured and not loose. When reapplying the lid, fasteners shall be placed 1/2 inch away from the previous fastener hole. Strapping shall be applied per <extref docno="MIL-HDBK-774"/>.</para>
        </para0>
        <para0>
            <title>CONTAINER REPAIR</title>
            <para>Each long life metal reusable container will be inspected and reconditioned in accordance with <extref docno="TB 9-289"/>, <extref docno="TB 55-8100-200-24"/>, or <extref docno="SB 725-92-1"/> and the applicable container drawing package. Container drawings are available upon request from the packaging requirements developer. This reconditioning effort includes mandatory replacement of breather valves, humidity indicators, data plates, sealing gaskets, and desiccant, plus all shear mounts with an age factor of 5 years or older. It also includes a leak test after reconditioning, inspection and replacement of unserviceable wood skids, and touch up or total stripping and refinishing of the container surfaces with Chemical Agent Resistant Coating paint.</para>
        </para0>
    </geninfo>
</ppmgeninfowp>\n'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-PreservationPackagingMarkingGenInfo.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def inspect(self, wpno, wp_title):
        """Function to create Depot Procedures inspect WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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
        """Function to create Depot Procedures test WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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
        """Function to create Depot Procedures service WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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
        """Function to create Depot Procedures remove WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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
        """Function to create Depot Procedures install WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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
        """Function to create Depot Procedures replace WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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
        """Function to create Depot Procedures repair WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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
        """Function to create Depot Procedures pack WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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
        """Function to create Depot Procedures unpack WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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
        """Function to create Depot Procedures prepforuse WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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
                ' WIP/{:05d}-{}-{}-PREP FOR USE.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def clean(self, wpno, wp_title):
        """Function to create Depot Procedures clean WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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
        """Function to create Depot Procedures prepstore WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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
        """Function to create Depot Procedures prepship WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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
        """Function to create Depot Procedures transport WP."""
        tmp = f'<maintwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
        <maintlvl level="depot"/>
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

    def qawp(self, wpno):
        """Function to create a Quality Assurance Requirements WP."""
        tmp = f'<qawp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '''\t<wpidinfo>
        <maintlvl level="depot"/>
        <title>>QUALITY ASSURANCE REQUIREMENTS</title>
    </wpidinfo>\n'''
        tmp += isb()
        tmp += '''\t<responsibility>
		<title>STATEMENT OF RESPONSIBILITY</title>
		<para>The depot/contractor is responsible for complying with the quality assurance requirements contained in this work package and in accordance with International Standards Organization (ISO) 9000 Series standards or equivalent. The commodity manager reserves the right to perform inspections or make changes that ensure the depot work being done meets the quality standards of the NMWR and preserves the inherent reliability of the item.</para>
	</responsibility>
	<definitions>
		<title>DEFINITIONS</title>
		<para>For quality assurance terms and definitions, refer to the glossary in this NMWR.</para>
	</definitions>
	<specialreq>
		<!-- CHANGE: update or remove -->
		<title>SPECIAL REQUIREMENTS FOR INSPECTION TOOLS AND EQUIPMENT</title>
		<para>The overhaul facility is responsible for acquisitions, maintenance, calibration, and disposition of all inspection and test equipment. Test equipment to be used by AMC (Army) elements will be acquired in accordance with <extref docno="AR 750-43"/>. All instrumentation and inspection equipment used in compliance with this NMWR should be calibrated and controlled in accordance with <extref docno="MIL-I-45607B"/> or <extref docno="DESCOM-R702-1" posttext=", Depot Quality Systems (Army facility)"/>, with all standards traceable to the National Bureau of Standards. Descriptions of inspecting and measuring equipment are left to the discretion of the overhauling facility to be considered as good shop practice.</para>
	</specialreq>
	<certreq>
		<!-- CHANGE: update or remove -->
		<title>CERTIFICATION REQUIREMENTS</title>
		<para>The contractor/depot QA activity is responsible for ascertaining and certifying personnel skills, equipment, and material meet the requirements of the work to be accomplished. Unless otherwise specified in the contract or by PACM representative, the contractor/depot QA activity should provide the PA/CM with statements or other evidence that specifications for such special processes as welding, nondestructive testing, plating, etc., have been complied with. Personnel performing magnetic particle and penetrant tests should be certified in accordance with <extref docno="MIL-STD-410"/>.</para>
	</certreq>
	<quality_program>
		<!-- CHANGE: update or remove -->
		<title>QUALITY PROGRAM</title>
		<para>All requirements for a quality program shall be adhered to IAW their appropriate contracting agency. All maintenance materials should conform to their applicable MIL-DTL or MIL-STD. The inspection for the quality of the container can be found in <extref docno="MIL-STD-3037, Department of Defense Standard Practice Inspection Criteria for International Organization for Standardization (ISO) Containers and Department of Defense Standard Family of ISO Shelters"/>.</para>
	</quality_program>
	<inprocess>
		<!-- THIS IS BOILERPLATE -->
		<title>IN-PROCESS INSPECTIONS</title>
		<para>In-process quality assurance <emphasis emph="bold">(QA)</emphasis> inspections are contained throughout the overhaul procedures of this NMWR. These inspections are immediately preceded by a statement such as “QA check” to identify them. They are the minimum inspections required. Additional QA inspections may be established by the depot or the commodity manager.</para>
	</inprocess>
	<acceptance>
		<!-- THIS IS BOILERPLATE -->
		<title>ACCEPTANCE INSPECTIONS</title>
		<para>Items maintained in accordance with this NMWR will be accepted based on the following criteria:
			<seqlist>
				<item>Conformance to quality of material requirements.</item>
				<item>Conformance to all in-process quality assurance inspections.</item>
				<item>Conformance to all final assembly testing requirements.</item>
				<item>Conformance to the preservation, packaging, and marking requirements.</item>
			</seqlist>
			<?Pub _newpage?>
			<table>
				<title>Container - INSPECTION - ACCEPTANCE AND REJECTION CRITERIA</title>
				<tgroup cols="5">
					<colspec colname="col1"/>
					<colspec colname="col2"/>
					<colspec colname="col3"/>
					<colspec colname="col4"/>
					<colspec colname="col5"/>
					<tbody>
						<row>
							<entry align="center" morerows="1" valign="middle">COMPONENT</entry>
							<entry align="center" morerows="1" valign="middle">NORMAL INDICATION</entry>
							<entry align="center" morerows="1" valign="middle">MEASURED INDICATION</entry>
							<entry align="center" nameend="col5" namest="col4">INITIALS</entry>
						</row>
						<row>
							<entry align="center">TECH</entry>
							<entry align="center">INSP.</entry>
						</row>
						<row>
							<entry>Expeditionary TRICON Self Serve Laundry System (ETSSLS) Container</entry>
							<entry>Container complies with all requirements of <extref docno="MIL-STD-3037, Department of Defense Standard Practice Inspection Criteria for International Organization for Standardization (ISO) Containers and Department of Defense Standard Family of ISO Shelters"/>.</entry>
							<entry/>
							<entry/>
							<entry/>
						</row>
					</tbody>
				</tgroup>
			</table>
        </para>
    </acceptance>
</qawp>\n'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-QualityAssuranceRequirements.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self):
        """Function to create Depot Procedures end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        tmp = '\t</depotcategory>\n'
        tmp += '</mim>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-DEPOT_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 1

def followon_maintsk():
    """Function to create the Follow-on Maintenance WP."""
    tmp = '''<followon.maintsk>
    <proc>
        <title/>
        <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
    </proc>
</followon.maintsk>'''
    return tmp

def isb():
    """Function to create the Initial Setup Box."""
    isb_tmp = '''\n\t<initial_setup>
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

def proc():
    """Function to create a filled in <proc> block."""
    tmp = '''\n\t<proc>
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
