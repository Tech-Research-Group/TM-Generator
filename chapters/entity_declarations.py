"""ENTITY DECLARATIONS"""


class EntityDeclarations:
    """A class that is used to create the entity declarations file."""

    def __init__(self, sys_acronym, manual_type, milstd, save_path) -> None:
        self.sys_acronym = sys_acronym
        self.manual_type = manual_type
        self.milstd = milstd
        self.save_path = save_path

    def entity_declarations(self) -> None:
        """Method to create the entity declarations file."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>'
        if self.milstd == "2C":
            tmp += """<?xml-stylesheet href="40051C_6_5.fos" type="text/x-fosi" title="Editor Stylesheet" media="screen" alternate="yes"?>
<?xml-stylesheet href="C:/Program Files/PTC/Arbortext Editor/custom/doctypes/xslfo-main-TRG_Stable--2C 2023-12-11/xslfo-main-vTRG-2C_DAILYS.xsl" type="text/xsl" media="print,pdf" alternate="yes" title="Print Stylesheet"?>
<!DOCTYPE production PUBLIC "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN" "40051C_6_5.dtd" [\n"""
        elif self.milstd == "2D":
            tmp += """<?xml-stylesheet href="40051D_7_0.fos" type="text/x-fosi" title="Editor Stylesheet" media="screen" alternate="yes"?>
<?xml-stylesheet href="C:/Program Files/PTC/Arbortext Editor/custom/doctypes/xslfo-main-TRG_Stable--2D 2025-04-14/xslfo-main-vTRG-2D_DAILY.xsl" type="text/xsl" media="print,pdf" alternate="yes" title="Print Stylesheet"?>
<!DOCTYPE production PUBLIC "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN" "40051D_7_0.dtd" [\n"""
        elif self.milstd == "E":
            tmp += """<?xml-stylesheet href="40051E_8_0.fos" type="text/x-fosi" title="Editor Stylesheet" media="screen" alternate="yes"?>
<?xml-stylesheet href="C:/Program Files/PTC/Arbortext Editor/custom/doctypes/40051E_8_0/estyle-v8_0/xslfo-main-v8_0.xsl" type="text/xsl" media="print,pdf" alternate="yes" title="Print Stylesheet"?>
<!DOCTYPE production PUBLIC "-//USA-DOD//DTD -1/2E TM Assembly REV E 8.0 20250417//EN" "40051E_8_0.dtd" [\n"""

        tmp += """\t<!NOTATION SVG SYSTEM "-//W3C//DTD SVG 1.1//EN">
\t<!ENTITY Auth_sample SYSTEM "graphics-SVG/Auth_sample.svg" NDATA SVG>
\t<!ENTITY Biological_Symbol SYSTEM "graphics-SVG/Biological_Symbol.svg" NDATA SVG>
\t<!ENTITY Chemical SYSTEM "graphics-SVG/Chemical.svg" NDATA SVG>
\t<!ENTITY da2028_F SYSTEM "graphics-SVG/da2028_F.svg" NDATA SVG>
\t<!ENTITY da2028_R SYSTEM "graphics-SVG/da2028_R.svg" NDATA SVG>
\t<!ENTITY da2028_sample_F SYSTEM "graphics-SVG/da2028_sample_F.svg" NDATA SVG>
\t<!ENTITY da2028_sample_R SYSTEM "graphics-SVG/da2028_sample_R.svg" NDATA SVG>
\t<!ENTITY Ear_Protection_Symbol SYSTEM "graphics-SVG/Ear_Protection_Symbol.svg" NDATA SVG>
\t<!ENTITY Electrical-hand SYSTEM "graphics-SVG/Electrical-hand.svg" NDATA SVG>
\t<!ENTITY Electrical_Symbols SYSTEM "graphics-SVG/Electrical_Symbols.svg" NDATA SVG>
\t<!ENTITY Example-US-Army-Authentication-Ltr SYSTEM "graphics-SVG/Example-US-Army-Authentication-Ltr.svg" NDATA SVG>
\t<!ENTITY Explosion SYSTEM "graphics-SVG/Explosion.svg" NDATA SVG>
\t<!ENTITY Eye_Protection SYSTEM "graphics-SVG/Eye_Protection.svg" NDATA SVG>
\t<!ENTITY Falling SYSTEM "graphics-SVG/Falling.svg" NDATA SVG>
\t<!ENTITY Falling_Parts SYSTEM "graphics-SVG/Falling_Parts.svg" NDATA SVG>
\t<!ENTITY Fire SYSTEM "graphics-SVG/Fire.svg" NDATA SVG>
\t<!ENTITY Flying_Particles_wShield SYSTEM "graphics-SVG/Flying_Particles_wShield.svg" NDATA SVG>
\t<!ENTITY Heavy_Object SYSTEM "graphics-SVG/Heavy_Object.svg" NDATA SVG>
\t<!ENTITY Heavy_Parts-above SYSTEM "graphics-SVG/Heavy_Parts-above.svg" NDATA SVG>
\t<!ENTITY Heavy_Parts-foot SYSTEM "graphics-SVG/Heavy_Parts-foot.svg" NDATA SVG>
\t<!ENTITY Heavy_Parts-hand SYSTEM "graphics-SVG/Heavy_Parts-hand.svg" NDATA SVG>
\t<!ENTITY Heavy_Parts-wall SYSTEM "graphics-SVG/Heavy_Parts-wall.svg" NDATA SVG>
\t<!ENTITY Hot_Area SYSTEM "graphics-SVG/Hot_Area.svg" NDATA SVG>
\t<!ENTITY Laser_Light SYSTEM "graphics-SVG/Laser_Light.svg" NDATA SVG>
\t<!ENTITY metric_equivalents SYSTEM "graphics-SVG/metric_equivalents.svg" NDATA SVG>
\t<!ENTITY Missing SYSTEM "graphics-SVG/missingIcon.svg" NDATA SVG>
\t<!ENTITY Moving_Parts-arm SYSTEM "graphics-SVG/Moving_Parts-arm.svg" NDATA SVG>
\t<!ENTITY Moving_Parts-fingers SYSTEM "graphics-SVG/Moving_Parts-fingers.svg" NDATA SVG>
\t<!ENTITY Moving_Parts-rollers SYSTEM "graphics-SVG/Moving_Parts-rollers.svg" NDATA SVG>
\t<!ENTITY Placeholder SYSTEM "graphics-SVG/Placeholder.svg" NDATA SVG>
\t<!ENTITY Poison SYSTEM "graphics-SVG/Poison.svg" NDATA SVG>
\t<!ENTITY Radiation SYSTEM "graphics-SVG/Radiation.svg" NDATA SVG>
\t<!ENTITY RPSTL_Placeholder SYSTEM "graphics-SVG/RPSTL_Placeholder.svg" NDATA SVG>
\t<!ENTITY Sharp_Object-foot SYSTEM "graphics-SVG/Sharp_Object-foot.svg" NDATA SVG>
\t<!ENTITY Sharp_Object-in_hand SYSTEM "graphics-SVG/Sharp_Object-in_hand.svg" NDATA SVG>
\t<!ENTITY Sharp_Object-puncture SYSTEM "graphics-SVG/Sharp_Object-puncture.svg" NDATA SVG>
\t<!ENTITY Slick_Floor SYSTEM "graphics-SVG/Slick_Floor.svg" NDATA SVG>
\t<!ENTITY Vapor SYSTEM "graphics-SVG/Vapor.svg" NDATA SVG>
]>\n"""

        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/00000-Entity Declarations.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
