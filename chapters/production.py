###PRODUCTION FILE###

import datetime

import cfg


class Production:
    """Class to create a production file for Arbortext."""

    date: str = datetime.datetime.today().strftime("%d %B %Y").upper()
    FPI_2C = "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN"
    FPI_2D = "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN"
    FPI_E = "-//USA-DOD//DTD -E TM Assembly REV E 8.0 20250417//EN"

    def __init__(
        self,
        cageno,
        fsc,
        manual_type,
        mil_std,
        niin,
        partno,
        sys_acronym,
        sys_name,
        tmno,
        uoc,
        save_path,
    ) -> None:
        self.cageno = cageno
        self.fsc = fsc
        self.manual_type = manual_type
        self.mil_std = mil_std
        self.niin = niin
        self.partno = partno
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.tmno = tmno
        self.uoc = uoc
        self.save_path = save_path

    def build_production(self) -> None:
        """Function to create the stylesheets for the production file."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += """<?xml-stylesheet href="40051D_6_5.fos" type="text/x-fosi" title="Screen Stylesheet" media="screen" alternate="yes"?>
<?xml-stylesheet href="C:/Program Files/PTC/Arbortext Editor/custom/doctypes/xslfo-main-TRG_Stable--2C 2023-12-11/xslfo-main-vTRG-2C_DAILYS.xsl" type="text/xsl" title="Print Stylesheet" media="print,pdf" alternate="yes"?>
<!--Arbortext, Inc., 1988-2024, v.4002-->\n"""
        elif self.mil_std == "2D":
            tmp += """<?xml-stylesheet href="40051D_7_0.fos" type="text/x-fosi" title="Screen Stylesheet" media="screen" alternate="yes"?>
<?xml-stylesheet href="C:/Program Files/PTC/Arbortext Editor/custom/doctypes/xslfo-main-TRG_Stable--2D 2025-07-18/xslfo-main-vTRG-2D_DAILY.xsl" type="text/xsl" title="Print Stylesheet" media="print,pdf" alternate="yes"?>
<!--Arbortext, Inc., 1988-2024, v.4002-->\n"""
        elif self.mil_std == "E":
            tmp += """<?xml-stylesheet href="40051E_8_0.fos" type="text/x-fosi" title="Screen Stylesheet" media="screen" alternate="yes"?>
<?xml-stylesheet href="C:/Program Files/PTC/Arbortext Editor/custom/doctypes/xslfo-main-TRG_Stable--2D 2025-07-18/xslfo-main-vTRG-2D_DAILY.xsl" type="text/xsl" title="Print Stylesheet" media="print,pdf" alternate="yes"?>
<!--Arbortext, Inc., 1988-2024, v.4002-->\n"""

        if self.mil_std == "2C":
            tmp += (
                f'<!DOCTYPE production PUBLIC "{self.FPI_2C}" "dtd/40051C_6_5.dtd" [\n'
            )
        elif self.mil_std == "2D":
            tmp += (
                f'<!DOCTYPE production PUBLIC "{self.FPI_2D}" "dtd/40051D_7_0.dtd" [\n'
            )
        elif self.mil_std == "E":
            tmp += (
                f'<!DOCTYPE production PUBLIC "{self.FPI_E}" "dtd/40051E_8_0.dtd" [\n'
            )

        tmp += """\t<!ENTITY % selection_boilerplate PUBLIC "-//USA-DOD//ENTITIES -1/2D Selection Boilerplate REV D 7.0 20220130//EN" "dtd/boilerplate/selectboil.ent"> %selection_boilerplate;
    <!ENTITY % editable_boilerplate PUBLIC "-//USA-DOD//ENTITIES -1/2D Editable Boilerplate REV D 7.0 20220130//EN" "dtd/boilerplate/editboil.ent"> %editable_boilerplate;
    <!ENTITY % prod_boilerplate PUBLIC "-//USA-DOD//ENTITIES -1/2D Production Boilerplate REV D 7.0 20220130//EN" "dtd/boilerplate/prodboil.ent"> %prod_boilerplate;
    <!ENTITY % gim_boilerplate PUBLIC "-//USA-DOD//ENTITIES -1/2D GIM Boilerplate REV D 7.0 20220130//EN" "dtd/boilerplate/gimboil.ent"> %gim_boilerplate;
    <!ENTITY % pimboil_boilerplate PUBLIC "-//USA-DOD//ENTITIES -1/2D Pimmboil Boilerplate REV D 7.0 20220130//EN" "dtd/boilerplate/pimboil.ent"> %pimboil_boilerplate;
    <!ENTITY % graphics PUBLIC "-//TRG//ENTITIES Graphics REV A 1.0 20241018//EN" "entities/graphics.ent"> %graphics;
    <!ENTITY % isb PUBLIC "-//TRG//ENTITIES Initial Setup Box REV A 1.0 20241018//EN" "entities/isb.ent"> %isb;
    <!ENTITY % warning_summary PUBLIC "-//TRG//ENTITIES Warning Summary REV A 1.0 20241018//EN" "entities/warning_summary.ent"> %warning_summary;
    <!ENTITY % wcn PUBLIC "-//TRG//ENTITIES Warnings Cautions Notes REV A 1.0 20241018//EN" "entities/wcn.ent"> %wcn;
    <!NOTATION svg SYSTEM "svg">
]>\n"""

        tmp += f'<production chngdate="{self.date}" chnglevel="0" date="{self.date}" pin="XXX-XXX-XXX" xmlns:xi="http://www.w3.org/2001/XInclude">\n'
        tmp += f"""\t<applic_ref_list>
		<applic id="" abbrevcode="">
			<name>{self.sys_name}</name>
			<nsn>
				<fsc>{self.fsc}</fsc>
				<niin>{self.niin}</niin>
			</nsn>
			<partno>{self.partno}</partno>
			<cageno>{self.cageno}</cageno>
			<single>
				<uoc>{self.uoc}</uoc>
			</single>
		</applic>
        <applic id="" abbrevcode="">
			<name></name>
			<nsn>
				<fsc></fsc>
				<niin></niin>
			</nsn>
			<partno></partno>
			<cageno></cageno>
			<single>
				<uoc></uoc>
			</single>
		</applic>
	</applic_ref_list>\n"""

        if self.manual_type == "-10":
            tmp += f'\t<paper.manual maintlvls="10" maintitl="OPERATOR MANUAL FOR {self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" pubno="TM {self.tmno} {self.manual_type}" revno="0" rpstl="no" security="cui">\n'
        elif self.manual_type == "-12&P":
            tmp += f'\t<paper.manual maintlvls="12" maintitl="OPERATOR AND FIELD MAINTENANCE MANUAL INCLUDING REPAIR PARTS AND SPECIAL TOOLS LIST FOR {self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" pubno="TM {self.tmno}-12&amp;P" revno="0" rpstl="yes" security="cui">\n'
        elif self.manual_type == "-13&P":
            tmp += f'\t<paper.manual maintlvls="13" maintitl="OPERATOR AND FIELD MAINTENANCE MANUAL INCLUDING REPAIR PARTS AND SPECIAL TOOLS LIST FOR {self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" pubno="TM {self.tmno}-13&amp;P" revno="0" rpstl="yes" security="cui">\n'
        elif self.manual_type == "-20":
            tmp += f'\t<paper.manual maintlvls="20" maintitl="FIELD MAINTENANCE MANUAL FOR {self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" pubno="TM {self.tmno}-20" revno="0" rpstl="no" security="cui">\n'
        elif self.manual_type == "-20P":
            tmp += f'\t<paper.manual maintlvls="20" maintitl="REPAIR PARTS LIST FOR {self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" pubno="TM {self.tmno}-20P" revno="0" rpstl="only" security="cui">\n'
        elif self.manual_type == "-23&P":
            tmp += f'\t<paper.manual maintlvls="23" maintitl="REPAIR PARTS LIST FOR {self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" pubno="TM {self.tmno}-23&amp;P" revno="0" rpstl="yes" security="cui">\n'
        elif self.manual_type == "NMWR":
            tmp += f'\t<paper.manual maintlvls="nmwr" maintitl="NATIONAL MAINTENANCE WORK REQUIREMENT INCLUDING REPAIR PARTS AND SPECIAL TOOLS LIST FOR {self.sys_name.upper()}" multivolume="no" pubno="NMWR {self.tmno}" revno="0" rpstl="yes" security="cui">\n'

        if self.sys_acronym == "":
            titlepg_name = self.sys_name
        else:
            titlepg_name = f"{self.sys_name} ({self.sys_acronym})"

        if cfg.front_matter:
            tmp += "\t\t<paper.frnt>\n"
            for filename in cfg.front_matter:
                tmp += f'\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t</paper.frnt>\n"

        if cfg.chapter1:
            tmp += f"""\t\t<gim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Chapter 1 General Information" maintlvl="operator">
                <name>{titlepg_name}</name>
            </titlepg>\n"""
            for filename in cfg.chapter1:
                tmp += f'\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t</gim>\n"

        if cfg.operator_instructions:
            tmp += f"""\t\t<opim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Operator Instructions" maintlvl="operator">
                <name>{titlepg_name}</name>
            </titlepg>\n"""
            for filename in cfg.operator_instructions:
                tmp += f'\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t</opim>\n"

        if cfg.ts_master_index_o:
            tmp += f"""\t\t<tim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Troubleshooting Master Index" maintlvl="operator">
                <name>{titlepg_name}</name>
            </titlepg>
            <masterindexcategory>\n"""
            for filename in cfg.ts_master_index_o:
                tmp += f'\t\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t\t</masterindexcategory>\n\t\t</tim>\n"

        if cfg.ts_operator:
            tmp += f"""\t\t<tim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Operator Troubleshooting" maintlvl="operator">
                <name>{titlepg_name}</name>
            </titlepg>
            <troublecategory>\n"""
            for filename in cfg.ts_operator:
                tmp += f'\t\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t\t</troublecategory>\n\t\t</tim>\n"

        if cfg.pmcs_o:
            tmp += f"""\t\t<mim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Operator Preventive Maintenance Checks and Services (PMCS)" maintlvl="operator">
                <name>{titlepg_name}</name>
            </titlepg>
            <pmcscategory>\n"""
            for filename in cfg.pmcs_o:
                tmp += f'\t\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t\t</pmcscategory>\n\t\t</mim>\n"

        if cfg.procedures_o:
            tmp += f"""\t\t<mim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Operator Maintenance" maintlvl="operator">
                <name>{titlepg_name}</name>
            </titlepg>
            <maintenancecategory>\n"""
            for filename in cfg.procedures_o:
                tmp += f'\t\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t\t</maintenancecategory>\n\t\t</mim>\n"

        if cfg.ts_maintainer:
            tmp += f"""\t\t<tim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Maintainer Troubleshooting" maintlvl="maintainer">
                <name>{titlepg_name}</name>
            </titlepg>
            <troublecategory>\n"""
            for filename in cfg.ts_maintainer:
                tmp += f'\t\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t\t</troublecategory>\n\t\t</tim>\n"

        if cfg.pmcs_m:
            tmp += f"""\t\t<mim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Maintainer Preventive Maintenance Checks and Services (PMCS)" maintlvl="maintainer">
                <name>{titlepg_name}</name>
            </titlepg>
            <pmcscategory>\n"""
            for filename in cfg.pmcs_m:
                tmp += f'\t\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t\t</pmcscategory>\n\t\t</mim>\n"

        if cfg.procedures_m:
            tmp += f"""\t\t<mim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Maintainer Maintenance" maintlvl="maintainer">
                <name>{titlepg_name}</name>
            </titlepg>
            <maintenancecategory>\n"""
            for filename in cfg.procedures_m:
                tmp += f'\t\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t\t</maintenancecategory>\n\t\t</mim>\n"

        if cfg.ts_depot:
            tmp += f"""\t\t<tim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Depot Troubleshooting" maintlvl="depot">
                <name>{titlepg_name}</name>
            </titlepg>
            <troublecategory>\n"""
            for filename in cfg.ts_depot:
                tmp += f'\t\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t\t</troublecategory>\n\t\t</tim>\n"

        if cfg.procedures_d:
            tmp += f"""\t\t<mim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Depot Maintenance" maintlvl="depot">
                <name>{titlepg_name}</name>
            </titlepg>
            <maintenancecategory>\n"""
            for filename in cfg.procedures_d:
                tmp += f'\t\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t\t</maintenancecategory>\n\t\t</mim>\n"

        if cfg.auxiliary_equipment:
            tmp += f"""\t\t<mim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Auxiliary Equipment Maintenance" maintlvl="maintainer">
                <name>{titlepg_name}</name>
            </titlepg>
            <auxiliarycategory>\n"""
            for filename in cfg.auxiliary_equipment:
                tmp += f'\t\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t\t</auxiliarycategory>\n\t\t</mim>\n"

        if cfg.ammunition:
            tmp += f"""\t\t<mim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Ammunition Maintenance" maintlvl="maintainer">
                <name>{titlepg_name}</name>
            </titlepg>
            <ammunitioncategory>\n"""
            for filename in cfg.ammunition:
                tmp += f'\t\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t\t</ammunitioncategory>\n\t\t</mim>\n"

        if cfg.shipment_instructions:
            tmp += f"""\t\t<mim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Shipment/Movement and Storage Maintenance" maintlvl="maintainer">
                <name>{titlepg_name}</name>
            </titlepg>
            <shipmentmovementstoragecategory>\n"""
            for filename in cfg.shipment_instructions:
                tmp += f'\t\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t\t</shipmentmovementstoragecategory>\n\t\t</mim>\n"

        if cfg.destruction:
            tmp += f"""\t\t<dim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Destruction of Equipment to Prevent Enemy Use" maintlvl="maintainer">
                <name>{titlepg_name}</name>
            </titlepg>\n"""
            for filename in cfg.destruction:
                tmp += f'\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t</dim>\n"

        if cfg.software_information:
            tmp += f"""\t\t<soim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Software Information" maintlvl="maintainer">
                <name>{titlepg_name}</name>
            </titlepg>\n"""
            for filename in cfg.software_information:
                tmp += f'\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t</soim>\n"

        if cfg.rpstl:
            tmp += f"""\t\t<pim chap-toc="no" chngno="0" dmwr-inclus="none" revno="0">
            <titlepg comment="Repair Parts and Specials Tools List (RPSTL)" maintlvl="maintainer">
                <name>{titlepg_name}</name>
            </titlepg>\n"""
            for filename in cfg.rpstl:
                tmp += f'\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t</pim>\n"

        if cfg.supporting_information:
            tmp += f"""\t\t<sim chap-toc="no" chngno="0" revno="0" tocentry="1">
            <titlepg comment="Support Information" maintlvl="maintainer">
                <name>{titlepg_name}</name>
            </titlepg>\n"""
            for filename in cfg.supporting_information:
                tmp += f'\t\t\t<xi:include href="files/{filename}"></xi:include>\n'
            tmp += "\t\t</sim>\n"

        tmp += (
            '\t\t<xi:include href="files/ZZZZZ_999999_Rear Matter.xml"></xi:include>\n'
        )
        tmp += """\t</paper.manual>
</production>"""

        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/production.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
