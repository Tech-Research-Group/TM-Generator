"""ENTITY DECLARATIONS"""
class EntityDeclarations:
    """A class that is used to create the entity declarations file."""
    def __init__(self, sys_acronym, manual_type, milstd, save_path):
        self.sys_acronym = sys_acronym
        self.manual_type = manual_type
        self.milstd = milstd
        self.save_path = save_path

    def entity_declarations(self):
        """Method to create the entity declarations file."""
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet href="production.fos" type="text/x-fosi" media="editor" alternate="yes"?>
<!--Arbortext, Inc., 1988-2013, v.4002-->\n'''
        if self.milstd == "2B":
            tmp += '<!DOCTYPE production PUBLIC "-//USA-DOD//DTD MIL-STD-2361 TM Assembly REV E 5.0 20131101/EN" "production 5.1.dtd" [\n'
        elif self.milstd == "2C":
            tmp += '<!DOCTYPE production PUBLIC "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.3 20190614//EN" "production 6.3.dtd" [\n'
        elif self.milstd == "2D":
            tmp += '<!DOCTYPE production PUBLIC "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN" "40051D_7_0.dtd" [\n'
        tmp += '''<!NOTATION pdf SYSTEM "pdf">
<!NOTATION pdf SYSTEM "pdf">
<!NOTATION svg SYSTEM "svg">
<!ENTITY Auth_sample SYSTEM "graphics/Auth_sample.svg" NDATA svg>
<!ENTITY Biological_Symbol SYSTEM "graphics/Biological_Symbol.svg" NDATA svg>
<!ENTITY Chemical SYSTEM "graphics/Chemical.svg" NDATA svg>
<!ENTITY da2028_F SYSTEM "graphics/da2028_F.svg" NDATA svg>
<!ENTITY da2028_R SYSTEM "graphics/da2028_R.svg" NDATA svg>
<!ENTITY da2028_sample_F SYSTEM "graphics/da2028_sample_F.svg" NDATA svg>
<!ENTITY da2028_sample_R SYSTEM "graphics/da2028_sample_R.svg" NDATA svg>
<!ENTITY Ear_Protection_Symbol SYSTEM "graphics/Ear_Protection_Symbol.svg" NDATA svg>
<!ENTITY Electrical-hand SYSTEM "graphics/Electrical-hand.svg" NDATA svg>
<!ENTITY Electrical_Symbols SYSTEM "graphics/Electrical_Symbols.svg" NDATA svg>
<!ENTITY Example-US-Army-Authentication-Ltr SYSTEM "graphics/Example-US-Army-Authentication-Ltr.svg" NDATA svg>
<!ENTITY Explosion SYSTEM "graphics/Explosion.svg" NDATA svg>
<!ENTITY Eye_Protection SYSTEM "graphics/Eye_Protection.svg" NDATA svg>
<!ENTITY Falling SYSTEM "graphics/Falling.svg" NDATA svg>
<!ENTITY Falling_Parts SYSTEM "graphics/Falling_Parts.svg" NDATA svg>
<!ENTITY Fire SYSTEM "graphics/Fire.svg" NDATA svg>
<!ENTITY Flying_Particles_wShield SYSTEM "graphics/Flying_Particles_wShield.svg" NDATA svg>
<!ENTITY Heavy_Parts-above SYSTEM "graphics/Heavy_Parts-above.svg" NDATA svg>
<!ENTITY Heavy_Parts-foot SYSTEM "graphics/Heavy_Parts-foot.svg" NDATA svg>
<!ENTITY Heavy_Parts-hand SYSTEM "graphics/Heavy_Parts-hand.svg" NDATA svg>
<!ENTITY Heavy_Parts-wall SYSTEM "graphics/Heavy_Parts-wall.svg" NDATA svg>
<!ENTITY Heavy_Object SYSTEM "graphics/Heavy_Object.svg" NDATA svg>
<!ENTITY Hot_Area SYSTEM "graphics/Hot_Area.svg" NDATA svg>
<!ENTITY metric_equivalents SYSTEM "graphics/metric_equivalents.svg" NDATA svg>
<!ENTITY MISSING SYSTEM "graphics/missingIcon.svg" NDATA svg>
<!ENTITY missing SYSTEM "graphics/missingIcon.svg" NDATA svg>
<!ENTITY Moving_Parts-arm SYSTEM "graphics/Moving_Parts-arm.svg" NDATA svg>
<!ENTITY Moving_Parts-fingers SYSTEM "graphics/Moving_Parts-fingers.svg" NDATA svg>
<!ENTITY Moving_Parts-rollers SYSTEM "graphics/Moving_Parts-rollers.svg" NDATA svg>
<!ENTITY Placeholder SYSTEM "graphics/Placeholder.svg" NDATA svg>
<!ENTITY PLACEHOLDER SYSTEM "graphics/Placeholder.svg" NDATA svg>
<!ENTITY RPSTL_Placeholder SYSTEM "graphics/RPSTL_Placeholder.svg" NDATA svg>
<!ENTITY Poison SYSTEM "graphics/Poison.svg" NDATA svg>
<!ENTITY Radiation SYSTEM "graphics/Radiation.svg" NDATA svg>
<!ENTITY Sharp_Object-in_hand SYSTEM "graphics/Sharp_Object-in_hand.svg" NDATA svg>
<!ENTITY Sharp_Object-foot SYSTEM "graphics/Sharp_Object-foot.svg" NDATA svg>
<!ENTITY Sharp_Object-puncture SYSTEM "graphics/Sharp_Object-puncture.svg" NDATA svg>
<!ENTITY Slick_Floor SYSTEM "graphics/Slick_Floor.svg" NDATA svg>
<!ENTITY Vapor SYSTEM "graphics/Vapor.svg" NDATA svg>

<!ENTITY I06023300001 SYSTEM "graphics/I06023300001.svg" NDATA svg>

]>
<?Pub EntList alpha bull copy rArr sect trade amp hyphen shy deg sup2
OHgr?>\n '''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/00000-EntityDeclarations_SVG.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
