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
        # cfg.prefix_file = math.floor(cfg.prefix_file / 1000) * 1000
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += '<opim chngno="0" revno="0" chap-toc="no">\n'

        # WP.METADATA Section
        tmp += md.show("destruct-introwp", self.tmno)

        tmp += '\t<titlepg maintlvl="operator">\n'
        tmp += f"\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n"
        tmp += "\t</titlepg>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-OPER_INSTRUCTIONS_START.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def controls_indicators(self) -> None:
        """Function to create Controls and Indicators section of Operator Instructions section."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE ctrlindwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE ctrlindwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE ctrlindwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += '<ctrlindwp chngno="0" wpno="O00001-' + self.tmno + '" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("ctrlindwp", self.tmno)

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
        tmp += f'\t\t<figure id="O00001-{self.tmno}-F0001">\n'
        tmp += """\t\t\t<title></title>
                <graphic boardno="PLACEHOLDER"/>
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
        tmp += f'\t\t<figure id="O00001-{self.tmno}-F0011">\n'
        tmp += """\t\t\t<title></title>
            <graphic boardno="PLACEHOLDER"/>
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
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-O00001-Controls Indicators.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def opusualwp(self, wpno, wp_title, cond_type) -> None:
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
        tmp += md.show("opusualwp", self.tmno)

        tmp += """<wpidinfo>
        <maintlvl level="operator"/>\n"""
        tmp += f"<title>OPERATION UNDER USUAL CONDITIONS <brk/> {wp_title}</title>\n"
        tmp += "</wpidinfo>\n"
        tmp += isb.show()
        tmp += f"""\t<opertsk>
        <{cond_type}>
            <proc>
                <title></title>
                <para></para>
            </proc>
        </{cond_type}>
    </opertsk>
</opusualwp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-{wp_title}.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def unusual_conditions(self, wpno) -> None:
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
        tmp += md.show("opunuwp", self.tmno)

        tmp += """<wpidinfo>
        <maintlvl level="operator"/>
        <title>OPERATION UNDER UNUSUAL CONDITIONS</title>
    </wpidinfo>\n"""
        tmp += isb.show()
        tmp += f"""\t<opunutsk>
        <unusualenv>
            <proc>
                <title>GENERAL INFORMATION</title>
                <para></para>
            </proc>
            <proc>
                <title>Operation on Sloped Terrain</title>
                <note>
                    <trim.para></trim.para>
                </note>
                <para></para>
            </proc>
            <proc>
                <title>Operation in Cold</title>
                <para></para>
            </proc>
            <proc>
                <title>Operation in Extreme Cold</title>
                <note>
                    <trim.para></trim.para>
                </note>
                <para></para>
            </proc>
            <proc>
                <title>Storage in Cold</title>
                <note>
                    <trim.para></trim.para>
                </note>
                <para></para>
            </proc>
            <proc>
                <title>Operation on in Extreme Heat</title>
                <note>
                    <trim.para></trim.para>
                </note>
                <para></para>
            </proc>
            <proc>
                <title>Operation on Sloped Terrain</title>
                <note>
                    <trim.para></trim.para>
                </note>
                <para></para>
            </proc>
            <proc>
                <title>Operation on Sloped Terrain</title>
                <note>
                    <trim.para></trim.para>
                </note>
                <para></para>
            </proc>
            <proc>
                <title>Operation in Sandy or Dusty Areas</title>
                <note>
                    <trim.para></trim.para>
                </note>
                <para></para>
            </proc>
            <proc>
                <title>Operation in Rain</title>
                <note>
                    <trim.para></trim.para>
                </note>
                <para></para>
            </proc>
            <proc>
                <title>Operation in Freezing Rain and Snow</title>
                <note>
                    <trim.para></trim.para>
                </note>
                <para></para>
            </proc>
            <proc>
                <title>Operation in High Altitude</title>
                <note>
                    <trim.para></trim.para>
                </note>
                <para></para>
            </proc>
            <proc>
                <para>
                    <emphasis emph="bold">ALTITUDE</emphasis>
                </para>
            </proc>
            <proc>
                <title>Adjust Air Damper</title>
                <step1>
                    <para></para>
                </step1>
                <figure id="{wpno}-{self.tmno}-F0001">
                    <title>Air Damper Adjustment</title>
                    <graphic boardno="PLACEHOLDER"/>
                </figure>
                <step1>
                    <para></para>
                </step1>
                <step1>
                    <para></para>
                </step1>
            </proc>
        </unusualenv>
    </opunutsk>
</opunuwp>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-{wpno}-Operation Under Unusual Conditions.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create Operator Instructions section end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = "</opim>"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-OPER_INSTRUCTIONS_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
