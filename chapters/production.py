###PRODUCTION FILE###

import datetime


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

    def buildProduction(self) -> None:
        """Function to create the stylesheets for the production file."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="40051D_6_5.fos" type="text/x-fosi" title="Screen Stylesheet" media="screen" alternate="yes"?>
<?xml-stylesheet href="C:/Program Files/PTC/Arbortext Editor/custom/doctypes/xslfo-main-TRG_Stable--2C 2023-12-11/xslfo-main-vTRG-2C_DAILYS.xsl" type="text/xsl" title="Print Stylesheet" media="print,pdf" alternate="yes"?>
<!--Arbortext, Inc., 1988-2024, v.4002-->\n"""
        elif self.mil_std == "2D":
            tmp += """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="40051D_7_0.fos" type="text/x-fosi" title="Screen Stylesheet" media="screen" alternate="yes"?>
<?xml-stylesheet href="C:/Program Files/PTC/Arbortext Editor/custom/doctypes/xslfo-main-TRG_Stable--2D 2025-07-18/xslfo-main-vTRG-2D_DAILY.xsl" type="text/xsl" title="Print Stylesheet" media="print,pdf" alternate="yes"?>
<!--Arbortext, Inc., 1988-2024, v.4002-->\n"""
        elif self.mil_std == "E":
            tmp += """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="40051E_8_0.fos" type="text/x-fosi" title="Screen Stylesheet" media="screen" alternate="yes"?>
<?xml-stylesheet href="C:/Program Files/PTC/Arbortext Editor/custom/doctypes/xslfo-main-TRG_Stable--2D 2025-07-18/xslfo-main-vTRG-2D_DAILY.xsl" type="text/xsl" title="Print Stylesheet" media="print,pdf" alternate="yes"?>
<!--Arbortext, Inc., 1988-2024, v.4002-->\n"""

        if self.mil_std == "2C":
            tmp += (
                f'<!DOCTYPE production PUBLIC "{self.FPI_2C}" "dtd/40051C_6_5.dtd" [\n'
            )
        elif self.mil_std == "2D":
            tmp = (
                f'<!DOCTYPE production PUBLIC "{self.FPI_2D}" "dtd/40051D_7_0.dtd" [\n'
            )
        elif self.mil_std == "E":
            tmp = f'<!DOCTYPE production PUBLIC "{self.FPI_E}" "dtd/40051E_8_0.dtd" [\n'

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
            tmp += f'\t<paper.manual maintlvls="12" maintitl="OPERATOR AND FIELD MAINTENANCE MANUAL INCLUDING REPAIR PARTS AND SPECIAL TOOLS LIST FOR {self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" pubno="TM {self.tmno}-12&amp;P" revno="0" rpstl="no" security="cui">\n'
        elif self.manual_type == "-13&P":
            tmp += f'\t<paper.manual maintlvls="13" maintitl="OPERATOR AND FIELD MAINTENANCE MANUAL INCLUDING REPAIR PARTS AND SPECIAL TOOLS LIST FOR {self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" pubno="TM {self.tmno}-13&amp;P" revno="0" rpstl="yes" security="cui">\n'
        elif self.manual_type == "-20":
            tmp += f'\t<paper.manual maintlvls="20" maintitl="FIELD MAINTENANCE MANUAL FOR {self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" pubno="TM {self.tmno}-20" revno="0" rpstl="only" security="cui">\n'
        elif self.manual_type == "-20P":
            tmp += f'\t<paper.manual maintlvls="20" maintitl="REPAIR PARTS LIST FOR {self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" pubno="TM {self.tmno}-20P" revno="0" rpstl="only" security="cui">\n'
        elif self.manual_type == "-23&P":
            tmp += f'\t<paper.manual maintlvls="23" maintitl="REPAIR PARTS LIST FOR {self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" pubno="TM {self.tmno}-23&amp;P" revno="0" rpstl="only" security="cui">\n'
        elif self.manual_type == "NMWR":
            tmp += f'\t<paper.manual maintlvls="nmwr" maintitl="NATIONAL MAINTENANCE WORK REQUIREMENT INCLUDING REPAIR PARTS AND SPECIAL TOOLS LIST FOR {self.sys_name.upper()}" multivolume="no" pubno="NMWR {self.tmno}" revno="0" rpstl="yes" security="cui">\n'
        tmp += """\t\t<paper.frnt>
            <xi:include href="files/"></xi:include>
            <xi:include href="files/"></xi:include>
            <xi:include href="files/"></xi:include>
            <xi:include href="files/"></xi:include>
            <xi:include href="files/"></xi:include>
            <xi:include href="files/"></xi:include>
        </paper.frnt>\n"""
        tmp += """\t\t<gim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Chapter 1 General Information" maintlvl="operator">
                <name></name>
            </titlepg>
            <xi:include href=""></xi:include>
        </gim>
        <opim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Chapter 2 Operator Instructions" maintlvl="operator">
                <name></name>
            </titlepg>
            <xi:include href=""></xi:include>
        </opim>
        <tim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Chapter 3 Operator Troubleshooting" maintlvl="operator">
                <name></name>
            </titlepg>
            <troublecategory>
                <xi:include href=""></xi:include>
            </troublecategory>
        </tim>
        <mim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Chapter 4 Operator Preventive Maintenance Checks and Services (PMCS)" maintlvl="operator">
                <name></name>
            </titlepg>
            <pmcscategory>
                <xi:include href=""></xi:include>
            </pmcscategory>
        </mim>
        <mim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Chapter 5 Operator Maintenance" maintlvl="operator">
                <name></name>
            </titlepg>
            <maintenancecategory>
                <xi:include href=""></xi:include>
            </maintenancecategory>
        </mim>
        <tim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Chapter 6 Maintainer Troubleshooting" maintlvl="maintainer">
                <name></name>
            </titlepg>
            <troublecategory>
                <xi:include href=""></xi:include>
            </troublecategory>
        </tim>
        <mim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Chapter 7 Maintainer Preventive Maintenance Checks and Services (PMCS)" maintlvl="maintainer">
                <name></name>
            </titlepg>
            <pmcscategory>
                <xi:include href=""></xi:include>
            </pmcscategory>
        </mim>
        <mim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Chapter 8 Maintainer Maintenance" maintlvl="maintainer">
                <name></name>
            </titlepg>
            <maintenancecategory>
                <xi:include href=""></xi:include>
            </maintenancecategory>
        </mim>
        <mim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Chapter 9 Auxiliary Equipment Maintenance" maintlvl="maintainer">
                <name></name>
            </titlepg>
            <auxiliarycategory>
                <xi:include href=""></xi:include>
            </auxiliarycategory>
        </mim>
        <dim chap-toc="no" chngno="0" revno="0">
            <titlepg comment="Chapter 10 Destruction of Equipment to Prevent Enemy Use" maintlvl="operator">
                <name></name>
            </titlepg>
            <xi:include href=""></xi:include>
        </dim>
        <pim chap-toc="no" chngno="0" dmwr-inclus="none" revno="0">
            <titlepg comment="Chapter 11 Repair Parts and Specials Tools List (RPSTL)" maintlvl="maintainer">
                <name></name>
            </titlepg>
            <xi:include href=""></xi:include>
        </pim>
        <sim chap-toc="no" chngno="0" revno="0" tocentry="1">
            <titlepg
                comment="Chapter 10 Support Information" maintlvl="operator">
                <name></name>
            </titlepg>
            <xi:include href=""></xi:include>
        </sim>
        <xi:include href="files/ZZZZZ_S99999_Rear Matter.xml"></xi:include>
    </paper.manual>
</production>"""

        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/production.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
