"""REAR MATTER"""

import datetime


class RearMatter:
    """Class to create various types of WP's included in the Rear Matter section of a TM."""

    date: str = datetime.datetime.today().strftime("%d %B %Y").upper()
    FPI_2C = "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN"
    FPI_2D = "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN"
    FPI_E = "-//USA-DOD//DTD -E TM Assembly REV E 8.0 20250417//EN"

    def __init__(self, manual_type, mil_std, sys_acronym, save_path) -> None:
        self.manual_type = manual_type
        self.mil_std = mil_std
        self.sys_acronym = sys_acronym
        self.save_path = save_path

    def rear_matter(self) -> None:
        """Function to create rear matter."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += (
                f'<!DOCTYPE rear PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
            )
        elif self.mil_std == "2D":
            tmp += (
                f'<!DOCTYPE rear PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
            )
        elif self.mil_std == "E":
            tmp += (
                f'<!DOCTYPE rear PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
            )
        tmp += """<rear>
    <aindx>
        <title>ALPHABETICAL INDEX</title>
        <!-- trim.para is optional -->
        <trim.para/>
        <col.title>Subject</col.title>
        <col.title>WP Sequence #</col.title>
        <alphaindx>A</alphaindx>
        <indexentry>
            <title>Additional Authorization List (AAL)</title>
            <wpno wpref="XX-XXXX-XXX"/>
            <pageno></pageno>
        </indexentry>
        <alphaindx></alphaindx>
        <indexentry>
            <title></title>
            <wpno wpref="XX-XXXX-XXX"/>
            <pageno></pageno>
        </indexentr
        <alphaindx></alphaindx>
        <indexentry>
            <title></title>
            <wpno wpref="XX-XXXX-XXX"/>
            <pageno></pageno>
        </indexentry>
    </aindx>
    <da2028>
        <graphic boardno="da2028_sample_F"/>
    </da2028>
    <da2028>
        <graphic boardno="da2028_sample_R"/>
    </da2028>
    <da2028>
        <graphic boardno="da2028_F"/>
    </da2028>
    <da2028>
        <graphic boardno="da2028_R"/>
    </da2028>
    <da2028>
        <graphic boardno="da2028_F"/>
    </da2028>
    <da2028>
        <graphic boardno="da2028_R"/>
    </da2028>
    <da2028>
        <graphic boardno="da2028_F"/>
    </da2028>
    <da2028>
        <graphic boardno="da2028_R"/>
    </da2028>
    <authent boardno="Auth_sample"/>
    <back boardno="metric_equivalents"/>
</rear>"""
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/ZZZZZ-REAR MATTER.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
            _f.close()
