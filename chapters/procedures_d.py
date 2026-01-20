"""DEPOT PROCEDURES"""

import datetime
import math

import cfg
import views.followon_maintsk as followon_maintsk
import views.isb as isb
import views.metadata as md
import views.proc as proc


class DepotProcedures:
    """Class to create various types of WP's included in Depot Procedures of a TM."""

    date: str = datetime.datetime.today().strftime("%d %B %Y").upper()
    FPI_2C = "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN"
    FPI_2D = "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN"
    FPI_E = "-//USA-DOD//DTD -E TM Assembly REV E 8.0 20250417//EN"

    def __init__(
        self, manual_type, milstd, sys_acronym, sys_name, tmno, save_path
    ) -> None:
        self.manual_type = manual_type
        self.milstd = milstd
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.tmno = tmno
        self.save_path = save_path

    def start(self) -> None:
        """Function to create Depot Procedures start tags."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<mim chngno="0" revno="0" chap-toc="no">\n"""
        tmp += '\t<titlepg maintlvl="depot">\n'
        tmp += "\t\t<name>" + self.sys_name + " (" + self.sys_acronym + ")</name>\n"
        tmp += "\t</titlepg>\n" + "\t<depotcategory>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-DEPOT_MAINTENANCE_START.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def ppmgeninfowp(self, wpno) -> None:
        """Function to create the Preservation, Packaging, and Marking General Information WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'

        if self.milstd == "2C":
            tmp += f'<!DOCTYPE ppmgeninfowp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.milstd == "2D":
            tmp += f'<!DOCTYPE ppmgeninfowp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.milstd == "E":
            tmp += f'<!DOCTYPE ppmgeninfowp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<ppmgeninfowp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += """<wpidinfo>
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
</ppmgeninfowp>\n"""
        file_name = (
            f"{cfg.prefix_file:05d}-{wpno}-Preservation Packaging Marking Gen Info.xml"
        )
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.procedures_d.append(file_name)
        cfg.prefix_file += 10

    def maintwp(self, wpno, wp_title, proc_type) -> None:
        """Function to create Depot Procedures WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'

        if self.milstd == "2C":
            tmp += f'<!DOCTYPE maintwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.milstd == "2D":
            tmp += f'<!DOCTYPE maintwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.milstd == "E":
            tmp += f'<!DOCTYPE maintwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<maintwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += """\t<wpidinfo>
        <maintlvl level="depot"/>\n"""
        if proc_type.lower() == "prepforuse":
            tmp += f"<title>{wp_title}</title>\n"
        elif proc_type.lower() == "prepship":
            tmp += f"<title>{wp_title}</title>\n"
        elif proc_type.lower() == "prepstore":
            tmp += f"<title>{wp_title}</title>\n"
        else:
            tmp += f"<title>{wp_title} <brk/> {proc_type.upper()}</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += isb.show()
        tmp += "\t<maintsk>\n"
        tmp += f"\t\t<{proc_type.lower()}>\n"
        tmp += proc.show()
        tmp += f"\t\t</{proc_type.lower()}>\n"
        tmp += "\t</maintsk>\n"
        tmp += followon_maintsk.show()
        tmp += "</maintwp>"

        if (
            proc_type == "prepforuse"
            or proc_type == "prepship"
            or proc_type == "prepstore"
        ):
            file_name = f"{cfg.prefix_file:05d}-{wpno.upper()}-{wp_title}.xml"
            with open(
                f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
                "w",
                encoding="UTF-8",
            ) as _f:
                _f.write(tmp)
        else:
            file_name = f"{cfg.prefix_file:05d}-{wpno.upper()}-{wp_title}-{proc_type.upper()}.xml"
            with open(
                f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
                "w",
                encoding="UTF-8",
            ) as _f:
                _f.write(tmp)
        cfg.procedures_d.append(file_name)
        cfg.prefix_file += 10

    def qawp(self, wpno) -> None:
        """Function to create a Quality Assurance Requirements WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'

        if self.milstd == "2C":
            tmp += (
                f'<!DOCTYPE qawp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
            )
        elif self.milstd == "2D":
            tmp += (
                f'<!DOCTYPE qawp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
            )
        elif self.milstd == "E":
            tmp += (
                f'<!DOCTYPE qawp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
            )
        tmp += f'<qawp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += """\t<wpidinfo>
        <maintlvl level="depot"/>
        <title>>QUALITY ASSURANCE REQUIREMENTS</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += """\t<responsibility>
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
							<entry>INSERT TM NAME HERE Container</entry>
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
</qawp>\n"""
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Quality Assurance Requirements.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.procedures_d.append(file_name)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create Depot Procedures end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = "\t</depotcategory>\n" + "</mim>"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-DEPOT_MAINTENANCE_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
