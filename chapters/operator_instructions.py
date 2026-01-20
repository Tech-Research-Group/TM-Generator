"""OPERATOR INSTRUCTIONS"""

import datetime
import math

import cfg
import views.isb as isb
import views.metadata as md


class OperatorInstructions:
    """Class to create various types of WP's included in Operator Instructions section of a TM."""

    date: str = datetime.datetime.today().strftime("%d %B %Y").upper()
    FPI_2C = "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN"
    FPI_2D = "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN"
    FPI_E = "-//USA-DOD//DTD -E TM Assembly REV E 8.0 20250417//EN"
    TAB_2 = "\t\t"
    TAB_3 = "\t\t\t"
    TAB_4 = "\t\t\t\t"

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
        """Function that creates Operator Instructions section starting tags of TM."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += '<opim chngno="0" revno="0" chap-toc="no">\n'
        tmp += '\t<titlepg maintlvl="operator">\n'
        tmp += f"\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n"
        tmp += "\t</titlepg>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-OPERATOR_INSTRUCTIONS_START.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def ctrlindwp(self, wpno) -> None:
        """Function to create Controls and Indicators section of Operator Instructions section."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE ctrlindwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE ctrlindwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE ctrlindwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<ctrlindwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'{self.TAB_2}<maintlvl level="operator"/>\n'
        tmp += f"{self.TAB_2}<title>DESCRIPTION AND USE OF OPERATOR CONTROLS AND INDICATORS</title>\n"
        tmp += "\t</wpidinfo>\n"
        tmp += "\t<intro>\n"
        tmp += f"{self.TAB_2}<para0-alt>\n"
        tmp += f"{self.TAB_3}<para0>\n"
        tmp += f"{self.TAB_4}<title>Introduction</title>\n"
        tmp += f"{self.TAB_4}<para></para>\n"
        tmp += f"{self.TAB_3}</para0>\n"
        tmp += f"{self.TAB_2}</para0-alt>\n"
        tmp += "\t</intro>\n"
        tmp += "\t<ctrlindtab>\n"
        tmp += "\t\t<title></title>\n"
        tmp += f'\t\t<figure id="{wpno}-{self.tmno}-F0001">\n'
        tmp += """\t\t\t<title></title>
                <graphic boardno=""/>
            </figure>
            <ctrlindrow>
                <key>1</key>
                <ctrlind></ctrlind>
                <function></function>
            </ctrlindrow>
            <ctrlindrow>
                <key>2</key>
                <ctrlind></ctrlind>
                <function></function>
            </ctrlindrow>
        </ctrlindtab>
        <ctrlindtab>
            <title></title>\n"""
        tmp += f'\t\t<figure id="{wpno}-{self.tmno}-F0002">\n'
        tmp += """\t\t\t<title></title>
            <graphic boardno=""/>
        </figure>
        <ctrlindrow>
            <key>1</key>
            <ctrlind></ctrlind>
            <function></function>
        </ctrlindrow>
        <ctrlindrow>
            <key>2</key>
            <ctrlind></ctrlind>
            <function></function>
        </ctrlindrow>
    </ctrlindtab>
</ctrlindwp>"""
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Description and Use of Operator Controls and Indicators.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.operator_instructions.append(file_name)
        cfg.prefix_file += 10

    def opusualwp(self, wpno, wp_title) -> None:
        """Function to create operating procedures WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE opusualwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE opusualwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE opusualwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<opusualwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += """<wpidinfo>
        <maintlvl level="operator"/>\n"""
        tmp += f"<title>{wp_title}</title>\n"
        tmp += "</wpidinfo>\n"
        tmp += isb.show()
        tmp += """\t<opertsk>
        <secref>
            <proc>
                <para></para>
            </proc>
        </secref>
    </opertsk>
    <opertsk>
        <site>
            <proc>
                <para></para>
            </proc>
        </site>
    </opertsk>
    <opertsk>
        <shelter>
            <proc>
                <para></para>
            </proc>
        </shelter>
    </opertsk>
    <opertsk>
        <prepforuse>
            <proc>
                <para></para>
            </proc>
        </prepforuse>
    </opertsk>
    <opertsk>
        <initial>
            <proc>
                <para></para>
            </proc>
        </initial>
    </opertsk>
    <opertsk>
        <oper>
            <proc>
                <para></para>
            </proc>
        </oper>
    </opertsk>
    <opertsk>
        <operaux>
            <proc>
                <para></para>
            </proc>
        </operaux>
    </opertsk>
    <opertsk>
        <prepmove>
            <proc>
                <para></para>
            </proc>
        </prepmove>
    </opertsk>
</opusualwp>"""
        file_name = f"{cfg.prefix_file:05d}-{wpno}-{wp_title}.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.operator_instructions.append(file_name)
        cfg.prefix_file += 10

    def opunuwp(self, wpno) -> None:
        """Function to create the operating under unusual conditions section."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE opunuwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE opunuwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE opunuwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<opunuwp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += """<wpidinfo>
        <maintlvl level="operator"/>
        <title>OPERATION UNDER UNUSUAL CONDITIONS</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += """\t<opunutsk>
        <unusualenv>
            <proc>
                <title>GENERAL INFORMATION</title>
                <para></para>
            </proc>
            <proc>
                <title>Operation on Sloped Terrain</title>
                <para></para>
            </proc>
            <proc>
                <title>Operation in Cold</title>
                <para></para>
            </proc>
            <proc>
                <title>Operation in Extreme Cold</title>
                <para></para>
            </proc>
            <proc>
                <title>Storage in Cold</title>
                <para></para>
            </proc>
            <proc>
                <title>Operation on in Extreme Heat</title>
                <para></para>
            </proc>
            <proc>
                <title>Operation on Sloped Terrain</title>
                <para></para>
            </proc>
            <proc>
                <title>Operation in Sandy or Dusty Areas</title>
                <para></para>
            </proc>
            <proc>
                <title>Operation in Rain</title>
                <para></para>
            </proc>
            <proc>
                <title>Operation in Freezing Rain and Snow</title>
                <para></para>
            </proc>
            <proc>
                <title>Operation in High Altitude</title>
                <para></para>
            </proc>
            <proc>
                <para>
                    <emphasis emph="bold">ALTITUDE</emphasis>
                </para>
            </proc>
            <proc>
                <title>Adjust Air Damper</title>
                <para></para>
            </proc>
        </unusualenv>
        <fording>
            <proc>
                <title>Fording and Swimming</title>
                <para></para>
            </proc>
        </fording>
        <decon>
            <proc>
                <title>Interim Chemical, Biological, Radiological, Nuclear and Explosives (CBRNE) Decontamination</title>
                <para></para>
            </proc>
        </decon>
        <ecm>
            <proc>
                <title>Jamming and Electronic Countermeasures (ECM)</title>
                <para></para>
            </proc>
        </ecm>
        <degraded>
            <proc>
                <title>Degraded Operation</title>
                <para></para>
            </proc>
        </degraded>
    </opunutsk>
</opunuwp>"""
        file_name = (
            f"{cfg.prefix_file:05d}-{wpno}-Operation Under Unusual Conditions.xml"
        )
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.operator_instructions.append(file_name)
        cfg.prefix_file += 10

    def emergencywp(self, wpno) -> None:
        """Function to create the emergency work package."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE emergencywp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE emergencywp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE emergencywp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<emergencywp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += """<wpidinfo>
        <maintlvl level="operator"/>
        <title>EMERGENCY</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += f"""\t<emergency>
		<proc>
			<para>There are no emergency operating procedures for the {self.sys_name} ({self.sys_acronym}).</para>
		</proc>
	</emergency>
</emergencywp>\n"""
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Emergency.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.operator_instructions.append(file_name)
        cfg.prefix_file += 10

    def stowagewp(self, wpno) -> None:
        """Function to create the decal/data plate guide work package."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE stowagewp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE stowagewp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE stowagewp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<stowagewp chngno="0" wpno="{wpno}-{self.tmno}" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += """<wpidinfo>
        <maintlvl level="operator"/>
        <title>DECAL/DATA PLATE GUIDE</title>
    </wpidinfo>\n"""
        tmp += f"""\t<intro>
		<para0>
			<title>Introduction</title>
			<para>This work package shows Item Unique Identification (IUID) decals, data plates, and stencils found on the {self.sys_name} ({self.sys_acronym}).</para>
		</para0>
	</intro>
    <stowinfo>
		<intro>
            <para0>
                <title>Stowage Requirements</title>
                <para>The {self.sys_acronym} (<xref figid="{wpno}-{self.tmno}-F0001"/>) is a ...</para>
            </para0>
        </intro>
        <figure id="{wpno}-{self.tmno}">
            <title>{self.sys_acronym}</title>
            <graphic boardno=""/>
        </figure>
	</stowinfo>
</stowagewp>\n"""
        file_name = (
            f"{cfg.prefix_file:05d}-{wpno}-Operations Decal Data Plate Guide.xml"
        )
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.operator_instructions.append(file_name)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create Operator Instructions section end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = "</opim>"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-OPERATOR_INSTRUCTIONS_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
