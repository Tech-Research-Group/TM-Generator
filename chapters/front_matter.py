"""FRONT MATTER"""

import datetime
import math

import cfg
import views.metadata as md


class FrontMatter:
    """Class to create various types of WP's included in the Front Matter section of a TM."""

    date: str = datetime.datetime.today().strftime("%d %B %Y").upper()
    FPI_2C = "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN"
    FPI_2D = "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN"
    FPI_E = "-//USA-DOD//DTD -E TM Assembly REV E 8.0 20250417//EN"
    TAB_2 = "\t\t"
    TAB_3 = "\t\t\t"
    TAB_4 = "\t\t\t\t"
    TAB_5 = "\t\t\t\t\t"
    TAB_6 = "\t\t\t\t\t\t"
    TAB_7 = "\t\t\t\t\t\t\t"
    TAB_8 = "\t\t\t\t\t\t\t\t"

    def __init__(
        self,
        cageno,
        fsc,
        manual_type,
        mil_std,
        modelno,
        niin,
        partno,
        save_path,
        sys_acronym,
        sys_name,
        tmno,
        uoc,
    ) -> None:
        self.cageno = cageno
        self.fsc = fsc
        self.manual_type = manual_type
        self.mil_std = mil_std
        self.modelno = modelno
        self.niin = niin
        self.partno = partno
        self.save_path = save_path
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.tmno = tmno
        self.uoc = uoc

    def production_start(self) -> None:
        """Function that creates the opening production tag for the technical manual."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE production PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE production PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE production PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'

        tmp += f'<production chngdate="{self.date}" chnglevel="0" date="{self.date}" pin="XXX-XXX-XXX" xmlns:xi="http://www.w3.org/2001/XInclude">\n'
        tmp += f"""<applic_ref_list>
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
		</applic>\n"""

        if self.manual_type == "-10":
            tmp += f'\t<paper.manual maintlvls="10" maintitl="{self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" \
                    pubno="TM {self.tmno} {self.manual_type}" revno="0" rpstl="no" security="cui">\n'
        elif self.manual_type == "-12&P":
            tmp += f'\t<paper.manual maintlvls="12" maintitl="{self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" \
                    pubno="TM {self.tmno}-12&amp;P" revno="0" rpstl="yes" security="cui">\n'
        elif self.manual_type == "-13&P":
            tmp += f'\t<paper.manual maintlvls="13" maintitl="{self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" \
                    pubno="TM {self.tmno}-13&amp;P" revno="0" rpstl="yes" security="cui">\n'
        elif self.manual_type == "-20":
            tmp += f'\t<paper.manual maintlvls="20" maintitl="{self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" \
                    pubno="TM {self.tmno}-20" revno="0" rpstl="no" security="cui">\n'
        elif self.manual_type == "-20P":
            tmp += f'\t<paper.manual maintlvls="20" maintitl="{self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" \
                    pubno="TM {self.tmno}-20P" revno="0" rpstl="only" security="cui">\n'
        elif self.manual_type == "-23&P":
            tmp += f'\t<paper.manual maintlvls="23" maintitl="{self.sys_name.upper()} ({self.sys_acronym})" multivolume="no" \
                    pubno="TM {self.tmno}-23&amp;P" revno="0" rpstl="yes" security="cui">\n'
        elif self.manual_type == "NMWR":
            tmp += f'\t<paper.manual maintlvls="nmwr" maintitl="{self.sys_name.upper()}" multivolume="no" pubno="NMWR \
                    {self.tmno}" revno="0" rpstl="yes" security="cui">\n'
        tmp += f"{self.TAB_2}<paper.frnt>\n"

    def frntcover(self) -> None:
        """Function to create the frntcover WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'

        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE frntcover PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE frntcover PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE frntcover PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'

        tmp += f'{self.TAB_3}<frntcover security="cui">\n'
        tmp += f"{self.TAB_4}<tmtitle>\n"

        if self.manual_type in ["-10", "-12&P", "-13&P", "-20", "-20P", "-23&P"]:
            tmp += f"{self.TAB_5}<tmno>TM {self.tmno} {self.manual_type}</tmno>\n"
        elif self.manual_type == "NMWR":
            tmp += f"{self.TAB_5}<tmno>NMWR {self.tmno}</tmno>\n"

        tmp += f"{self.TAB_5}<prtitle>\n"
        tmp += f"{self.TAB_6}<sysnomen>\n"
        tmp += f"{self.TAB_7}<name>{self.sys_name}</name>\n"
        tmp += f"{self.TAB_7}<modelno>{self.modelno}</modelno>\n"
        tmp += f"{self.TAB_7}<nsn>\n"
        tmp += f"{self.TAB_8}<fsc>{self.fsc}</fsc>\n"
        tmp += f"{self.TAB_8}<niin>{self.niin}</niin>\n"
        tmp += f"{self.TAB_7}</nsn>\n"
        tmp += f"{self.TAB_7}<partno>{self.partno}</partno>\n"
        tmp += f"{self.TAB_7}<eic>N/A</eic>\n"
        tmp += f"{self.TAB_6}</sysnomen>\n"
        tmp += f"{self.TAB_5}</prtitle>\n"
        tmp += f"{self.TAB_4}</tmtitle>\n"
        tmp += f'{self.TAB_4}<graphic boardno=""/>\n'
        tmp += f"{self.TAB_4}<notices>\n"
        tmp += f"{self.TAB_5}<dist>\n"
        tmp += f"{self.TAB_6}<a.statement>\n"
        tmp += f"{self.TAB_7}<cti/>\n"
        tmp += f"{self.TAB_7}<reasondate></reasondate>\n"
        tmp += f"{self.TAB_7}<releaseagent></releaseagent>\n"
        tmp += f"{self.TAB_6}</a.statement>\n"
        tmp += f"{self.TAB_5}</dist>\n"
        tmp += f"{self.TAB_5}<export/>\n"
        tmp += f"{self.TAB_5}<destr>\n"
        tmp += f"""{self.TAB_6}<para>For classified documents, follow the procedures in <xref wpid="S00001-9-4120-433" itemid="NISPOM"/>,
                National Industrial Security Program Operating Manual and/or <xref wpid="S00001-9-4120-433" itemid="Info_Security"/>,
                Information Security Program. For unclassified, limited documents, destroy by any method that will prevent disclosure
                of contents or reconstruction of the document.</para>\n"""
        tmp += f"{self.TAB_5}</destr>\n"
        tmp += f"{self.TAB_4}</notices>\n"
        tmp += (
            self.TAB_4
            + """<cui_set>
                    <cntrlby></cntrlby>
                    <cui_ctgy></cui_ctgy>
                    <poc></poc>
                </cui_set>\n"""
        )
        tmp += (
            f"{self.TAB_4}<servnomen>HEADQUARTERS, DEPARTMENT OF THE ARMY</servnomen>\n"
        )
        tmp += f"{self.TAB_4}<date>{self.date}</date>\n"
        tmp += f"{self.TAB_3}</frntcover>\n"
        file_name = "00010-Front Cover.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.front_matter.append(file_name)
        cfg.prefix_file += 10

    def warning_summary(self) -> None:
        """Function to create Warning Summary section."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE warnsum PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE warnsum PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE warnsum PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += '<warnsum security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("warnsum", self.tmno)

        tmp += "\t<para>This warning summary contains general safety warnings and hazardous materials warnings that must be understood and applied during operation and maintenance of the &long.end.item.name;. Failure to observe these precautions could result in serious injury or death to personnel. Also included are explanations of safety and hazardous materials icons used within this technical manual.</para>\n"
        tmp += "\t<first_aid>\n"
        tmp += f"{self.TAB_2}<title>First Aid</title>\n"
        tmp += f'{self.TAB_2}<para>For First Aid information, refer to <xref wpid="S00001-9-4120-433" itemid="First_Aid" />, First Aid.</para>\n'
        tmp += "\t</first_aid>\n"

        # Beginning of explanation of safety warning icons section
        tmp += "\t<safety>\n"
        tmp += f"{self.TAB_2}<title>EXPLANATION OF SAFETY WARNING ICONS</title>\n"

        # EAR PROTECTION
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Ear_Protection_Symbol"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>EAR PROTECTION</title>\n"
        tmp += f"{self.TAB_4}<text>Headphones over ears show that noise level will harm ears.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"

        # ELECTRICAL
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Electrical_Symbols"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>ELECTRICAL</title>\n"
        tmp += f"{self.TAB_4}<text>Electrical wire to arm with electricity symbol running through hand shows that shock hazard is present.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"
        # FALLING
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Falling"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>FALLING</title>\n"
        tmp += f"{self.TAB_4}<text>Human figure in motion shows that falling from equipment presents a danger to life or limb.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"

        # FALLING PARTS
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Falling_Parts"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>FALLING PARTS</title>\n"
        tmp += f"{self.TAB_4}<text>Arrow bouncing off human shoulder and head shows that falling parts present a danger to life or limb.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"

        # FLYING PARTICLES
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Flying_Particles_wShield"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>FLYING PARTICLES</title>\n"
        tmp += f"{self.TAB_4}<text>Arrows bouncing off face shield show that particles flying through the air will harm face.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"

        # HEAVY OBJECT
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Heavy_Object"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>HEAVY OBJECT</title>\n"
        tmp += f"{self.TAB_4}<text>Human figure stooping over heavy object shows physical injury potential from improper lifting technique.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"

        # HEAVY PARTS ABOVE
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Heavy_Parts-above"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>HEAVY PARTS</title>\n"
        tmp += f"{self.TAB_4}<text>Heavy object on human figure shows that heavy parts present a danger to life or limb.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"

        # HEAVY PARTS FOOT
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Heavy_Parts-foot"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>HEAVY PARTS</title>\n"
        tmp += f"{self.TAB_4}<text>Foot with heavy object on top shows that heavy parts can crush and harm.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"

        # HEAVY PARTS HAND
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Heavy_Parts-hand"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>HEAVY PARTS</title>\n"
        tmp += f"{self.TAB_4}<text>Hand with heavy object on top shows that heavy parts can crush and harm.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"

        # HEAVY PARTS WALL
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Heavy_Parts-wall"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>HEAVY PARTS</title>\n"
        tmp += f"{self.TAB_4}<text>Heavy object pinning human figure against wall shows that heavy, moving parts present a danger to life or limb.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"

        # HOT AREA
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Hot_Area"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>HOT AREA</title>\n"
        tmp += f"{self.TAB_4}<text>Hand over object radiating heat shows that part is hot and can burn.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"

        # LASER LIGHT
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Laser_Light"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>LASER LIGHT</title>\n"
        tmp += f"{self.TAB_4}<text>Laser light hazard symbol indicates extreme danger for eyes from laser beams and reflections.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"

        # MOVING PARTS FINGERS
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Moving_Parts-fingers"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>MOVING PARTS</title>\n"
        tmp += f"{self.TAB_4}<text>Hand with fingers caught between gears shows that the moving parts of the equipment present a danger to life or limb.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"

        # SHARP OBJECT IN HAND
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Sharp_Object-in_hand"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>SHARP OBJECT</title>\n"
        tmp += f"{self.TAB_4}<text>Pointed object in hand shows that a sharp object presents a danger to limb.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"

        # SLICK FLOOR
        tmp += f"{self.TAB_2}<sfty-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Slick_Floor"/>\n'
        tmp += f"{self.TAB_3}<sftydesc>\n"
        tmp += f"{self.TAB_4}<title>SLICK FLOOR</title>\n"
        tmp += f"{self.TAB_4}<text>Wavy line on floor with legs prone shows that slick floor presents a danger for falling.</text>\n"
        tmp += f"{self.TAB_3}</sftydesc>\n"
        tmp += f"{self.TAB_2}</sfty-icons>\n"
        tmp += "\t</safety>\n"

        # General safety warnings descriptions section
        tmp += "\t<warninfo>\n"
        tmp += f"{self.TAB_2}<title>GENERAL SAFETY WARNINGS DESCRIPTIONS</title>\n"
        tmp += f"{self.TAB_2}<warning>\n"
        tmp += f'{self.TAB_3}<icon-set boardno="Slick_Floor"/>\n'
        tmp += (
            self.TAB_3
            + "<trim.para>All doors and doorways must remain unblocked, both inside and outside, during operation of system to allow for egress during an emergency. Failure to comply may result in serious injury or death to personnel. Seek immediate medical attention if injury occurs.</trim.para>\n"
        )
        tmp += f"{self.TAB_2}</warning>\n"

        tmp += f"{self.TAB_2}<warning>\n"
        tmp += f'{self.TAB_3}<icon-set boardno="Electrical_Symbols"/>\n'
        tmp += f"{self.TAB_3}<trim.para>Interior and exterior areas of {self.sys_acronym.upper()} may be a wet environment. Electrical cables and controls should not be handled with wet hands or while standing in water. Failure to comply may result in serious injury or death to personnel. Seek immediate medical attention if injury occurs.</trim.para>\n"
        tmp += f"{self.TAB_2}</warning>\n"

        tmp += f"{self.TAB_2}<warning>\n"
        tmp += f'{self.TAB_3}<icon-set boardno="Electrical_Symbols"/>\n'
        tmp += (
            self.TAB_3
            + "<trim.para>Power source and "
            + self.sys_acronym.upper()
            + " container must all be grounded to ensure safety of personnel during operation. Operating "
            + self.sys_acronym.upper()
            + " components while ungrounded or improperly grounded may expose personnel to risk of shock resulting in serious injury or death to personnel. Seek immediate medical attention if injury occurs.</trim.para>\n"
        )
        tmp += (
            self.TAB_3
            + "<trim.para>High voltage is present during operation. All electrical safety precautions must be followed when operating or maintaining equipment. Failure to comply may result in death or serious injury to personnel. Seek immediate medical attention if exposed to electricity.</trim.para>\n"
        )
        tmp += (
            self.TAB_3
            + "<trim.para>Source power must be off prior to connecting or removing power cables to "
            + self.sys_acronym.upper()
            + " shelter.</trim.para>\n"
        )
        tmp += (
            self.TAB_3
            + "<trim.para>All jewelry must be removed before starting work. Metal objects, such as rings or tools, can cause short circuits when contacting live circuits. A direct short can cause instant heating of metal resulting in severe burns. Failure to comply may result in serious injury or death to personnel. Seek immediate medical attention if exposed to electricity.</trim.para>\n"
        )
        tmp += f"{self.TAB_2}</warning>\n"
        tmp += "\t</warninfo>\n"

        # Explanation of hazardous material icons section
        tmp += "\t<hazmat>\n"
        tmp += f"{self.TAB_2}<title>EXPLANATION OF HAZARDOUS MATERIALS ICONS</title>\n"
        tmp += f"{self.TAB_2}<haz-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Biological_Symbol"/>\n'
        tmp += f"{self.TAB_3}<hazdesc>\n"
        tmp += f"{self.TAB_4}<title>BIOLOGICAL</title>\n"
        tmp += f"{self.TAB_4}<text>Abstract symbol bug shows that a material may contain bacteria or viruses that present a danger to life or health.</text>\n"
        tmp += f"{self.TAB_3}</hazdesc>\n"
        tmp += f"{self.TAB_2}</haz-icons>\n"

        tmp += f"{self.TAB_2}<haz-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Chemical"/>\n'
        tmp += f"{self.TAB_3}<hazdesc>\n"
        tmp += f"{self.TAB_4}<title>CHEMICAL</title>\n"
        tmp += f"{self.TAB_4}<text>Drops of liquid on hand shows that the material will cause burns or irritation to human skin or tissue.</text>\n"
        tmp += f"{self.TAB_3}</hazdesc>\n"
        tmp += f"{self.TAB_2}</haz-icons>\n"

        tmp += f"{self.TAB_2}<haz-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Explosion"/>\n'
        tmp += f"{self.TAB_3}<hazdesc>\n"
        tmp += f"{self.TAB_4}<title>EXPLOSION</title>\n"
        tmp += f"{self.TAB_4}<text>Rapidly expanding symbol shows that the material may explode if subjected to high temperatures, sources of ignition, or high pressure.</text>\n"
        tmp += f"{self.TAB_3}</hazdesc>\n"
        tmp += f"{self.TAB_2}</haz-icons>\n"

        tmp += f"{self.TAB_2}<haz-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Eye_Protection"/>\n'
        tmp += f"{self.TAB_3}<hazdesc>\n"
        tmp += f"{self.TAB_4}<title>EYE PROTECTION</title>\n"
        tmp += f"{self.TAB_4}<text>Person with goggles shows that the material will injure the eyes.</text>\n"

        tmp += f"{self.TAB_3}</hazdesc>\n"
        tmp += f"{self.TAB_2}</haz-icons>\n"

        tmp += f"{self.TAB_2}<haz-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Fire"/>\n'
        tmp += f"{self.TAB_3}<hazdesc>\n"
        tmp += f"{self.TAB_4}<title>FIRE</title>\n"
        tmp += f"{self.TAB_4}<text>Flame shows that a material may ignite and cause burns.</text>\n"
        tmp += f"{self.TAB_3}</hazdesc>\n"
        tmp += f"{self.TAB_2}</haz-icons>\n"

        tmp += f"{self.TAB_2}<haz-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Poison"/>\n'
        tmp += f"{self.TAB_3}<hazdesc>\n"
        tmp += f"{self.TAB_4}<title>POISON</title>\n"
        tmp += f"{self.TAB_4}<text>Skull and crossbones shows that a material is poisonous or is a danger to life.</text>\n"
        tmp += f"{self.TAB_3}</hazdesc>\n"
        tmp += f"{self.TAB_2}</haz-icons>\n"

        tmp += f"{self.TAB_2}<haz-icons>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Vapor"/>\n'
        tmp += f"{self.TAB_3}<hazdesc>\n"
        tmp += f"{self.TAB_4}<title>VAPOR</title>\n"
        tmp += f"{self.TAB_4}<text>Human figure in a cloud shows that material vapors present a danger to life or health.</text>\n"
        tmp += f"{self.TAB_3}</hazdesc>\n"
        tmp += f"{self.TAB_2}</haz-icons>\n"

        # Explanation of general hazardous materials descriptions section
        tmp += f"{self.TAB_2}<title>GENERAL HAZARDOUS MATERIALS DESCRIPTIONS</title>\n"
        tmp += f"{self.TAB_2}<hazard>\n"
        tmp += f"{self.TAB_3}<hazid>CLEANING PRODUCTS</hazid>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Chemical"/>\n'
        tmp += f'{self.TAB_3}<symbol boardno="Poison"/>\n'
        tmp += f"{self.TAB_3}<para>Personnel may be exposed to chemicals or other hazardous materials during cleaning operations. Personnel must wear gloves for protection while performing cleaning procedures. Failure to follow this warning may result in serious illness or death. Seek immediate medical attention if illness occurs.</para>\n"
        tmp += f"{self.TAB_2}</hazard>\n"

        tmp += f"{self.TAB_2}<hazard>\n"
        tmp += f"{self.TAB_3}<hazid>FUEL</hazid>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Fire"/>\n'
        tmp += f"{self.TAB_3}<para>Do not use diesel fuel, gasoline, or petroleum solvents for cleaning. These items are highly flammable and, if ignited, can cause injury or death to personnel and damage to equipment.</para>\n"
        tmp += f"{self.TAB_2}</hazard>\n"

        tmp += f"{self.TAB_2}<hazard>\n"
        tmp += f"{self.TAB_3}<hazid>ISOPROPYL ALCOHOL</hazid>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Eye_Protection"/>\n'
        tmp += f'{self.TAB_3}<symbol boardno="Vapor"/>\n'
        tmp += f"{self.TAB_3}<para>When using isopropyl alcohol, wear personal protective equipment (safety goggles or full face shield) to prevent injury to eyes or skin. Maintain proper ventilation to prevent inhalation of fumes. Maintain eye-wash and quick-drench facilities in work area.</para>\n"
        tmp += f"{self.TAB_2}</hazard>\n"

        tmp += f"{self.TAB_2}<hazard>\n"
        tmp += f"{self.TAB_3}<hazid>WASTEWATER</hazid>\n"
        tmp += f'{self.TAB_3}<symbol boardno="Biological_Symbol"/>\n'
        tmp += f"{self.TAB_3}<para>Wastewater generated during operation may contain biohazardous materials. When maintaining water plumbing or associated components, personnel must wear impermeable gloves, apron, and goggles for protection. Failure to comply can result in serious illness or death to personnel.</para>\n"
        tmp += f"{self.TAB_3}<para>Potable water hoses or fittings should not be handled directly after handling wastewater hoses or fittings. Wastewater items may contain bacteria or viruses that present a danger to life or health if not properly sanitized. Seek immediate medical attention if illness occurs.</para>\n"
        tmp += f"{self.TAB_2}</hazard>\n"
        tmp += "\t</hazmat>\n" + "</warnsum>\n"
        file_name = "00020-Warning Summary.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.front_matter.append(file_name)
        cfg.prefix_file += 10

    def loepwp(self) -> None:
        """Function to create the List of Effective Pages/WP's section."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE loepwp PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE loepwp PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE loepwp PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'

        tmp += '<loepwp security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("loepwp", self.tmno)

        tmp += f"""<title>LIST OF EFFECTIVE PACKAGES/WORK PACKAGES</title>
    <note>
        <trim.para>NOTE: Zero in the "Change No." column indicates an original page or work package.</trim.para>
    </note>
    <issuechg>
        <trim.para>Date of issue for the original manual is:</trim.para>
        <issued>
            <chgno>Original Draft</chgno>
            <chgdate julian="XXXXXX">{self.date}</chgdate>
        </issued>
    </issuechg>
    <totalnumberof>
        <text>THE TOTAL NUMBER OF PAGES FOR FRONT AND REAR MATTER IS </text>
        <totnum.frnt-rear-pages>XXXXXX</totnum.frnt-rear-pages>
        <text> AND THE TOTAL NUMBER OF WORK PACKAGES IS </text>
        <totnum.wps>X</totnum.wps>
        <text>, CONSISTING OF THE FOLLOWING:</text>
    </totalnumberof>
    <col.title>Page / WP No.</col.title>
    <col.title>Change No.</col.title>
    <chghistory modified="none">
        <title>Front Cover</title>
        <totnum.pages></totnum.pages>
        <chgno>0</chgno>
    </chghistory>
</loepwp>"""
        file_name = "00030-List of Effective Packages.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.front_matter.append(file_name)
        cfg.prefix_file += 10

    def titleblk(self) -> None:
        """Function that creates the Title Block."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE titleblk PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE titleblk PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE titleblk PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'

        tmp += '<titleblk security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("titleblk", self.tmno)

        tmp += f"""<servnomen>HEADQUARTERS, DEPARTMENT OF THE ARMY</servnomen>
    <city>WASHINGTON</city>
    <state>DC</state>
    <date>{self.date}</date>
    <prtitle>
        <sysnomen>\n"""
        tmp += f"{self.TAB_3}<name>{self.sys_name.upper()} ({self.sys_acronym.upper()})</name>\n"
        tmp += f"{self.TAB_3}<modelno>{self.modelno}</modelno>\n"
        tmp += f"{self.TAB_3}<nsn>\n"
        tmp += f"{self.TAB_4}<fsc>{self.fsc}</fsc>\n"
        tmp += f"{self.TAB_4}<niin>{self.niin}</niin>\n"
        tmp += f"{self.TAB_3}</nsn>\n"
        tmp += f"{self.TAB_3}<partno>{self.partno}</partno>\n"
        tmp += f"{self.TAB_3}<eic></eic>\n"
        tmp += """\t\t</sysnomen>
    </prtitle>
    <reporting>
        <title>REPORTING ERRORS AND RECOMMENDING IMPROVEMENTS</title>
        <para>You can help improve this manual. If you find any mistakes or if you know of a way to improve the procedures,
            please let us know. Mail your letter or <xref wpid="S00001-9-4120-433" itemid="Recommended_Changes" />
            (Recommended Changes to Publications and Blank Forms) located in the back of this manual, directly to:
            &proponent-address.army;. You may also send in your recommended changes via electronic mail. Our email address
            is <proponent>
                <name>Commander, U.S. Army Communications-Electronics Command</name>
                    <address><servnomen>HEADQUARTERS, DEPARTMENT OF THE ARMY</servnomen>
                        <street>6565 Surveillance Loop, Building 6001</street>
                        <city>Aberdeen Proving Ground</city>
                        <state>MD</state>
                        <zip>21005-1846</zip>
                        <country>United States</country>
                    </address>
                </proponent>. Our online web address for entering and submitting <xref wpid="S00001-9-4120-433"
                    itemid="Recommended_Changes" /> is <internet show.address="yes">
                        <homepage protocol="https" uri="https://pubsweb.redstone.army.mil/CECOM2028/Default.aspx" />
                    </internet>. A reply will be furnished to you.</para>
    </reporting>
    <notices>
        <dist>
            <a.statement>
                <cti/>
                <reasondate></reasondate>
                <releaseagent></releaseagent>
            </a.statement>
        </dist>
        <export/>
        <destr>
            <para>For classified documents, follow the procedures in <xref wpid="S00001-9-4120-433" itemid="NISPOM"/>,
                National Industrial Security Program Operating Manual and/or <xref wpid="S00001-9-4120-433" itemid="Info_Security"/>,
                Information Security Program. For unclassified, limited documents, destroy by any method that will prevent disclosure
                of contents or reconstruction of the document.</para>
        </destr>
    </notices>
</titleblk>\n"""
        file_name = "00040-Title Block.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.front_matter.append(file_name)
        cfg.prefix_file += 10

    def contents(self) -> None:
        """Function that creates the Title Block, TOC & How to Use sections."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE contents PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE contents PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE contents PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'

        tmp += """<contents security="cui">
    <title/>
    <col.title>WP Sequence No.</col.title>
    <col.title>Page No.</col.title>
    <contententry>
        <title/>
    </contententry>
</contents>\n"""
        file_name = "00050-TOC.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.front_matter.append(file_name)
        cfg.prefix_file += 10

    def howtouse(self) -> None:
        """Function that creates the How to Use section."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE howtouse PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE howtouse PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE howtouse PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += '<howtouse security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("howtouse", self.tmno)

        tmp += """\t<para0>
        <title>HOW TO USE THIS MANUAL</title>
        <para>In this manual, primary chapters appear in upper case/capital letters; work packages are presented in
            numeric sequence, e.g., 0001, 0002; paragraphs within a work package are not numbered and are presented in a
            titled format. For a first level paragraph, titles are in all upper case/capital letters, e.g., FRONT
            MATTER. Subordinate paragraph titles will have the first letter of the first word of each principle word all
            upper case/capital letters, e.g., Manual Organization and Page Numbering System. The location of additional
            material that must be referenced is clearly marked. Illustrations supporting maintenance procedures/text are
            located underneath, or as close as possible to, their referenced paragraph.</para>
        <subpara1>
            <title>Front Matter</title>
            <para>Front matter consists of front cover, warning summary, list of effective pages, title page, table of
                contents, and how to use this manual pages.</para>
        </subpara1>
        <subpara1>
            <title>Chapter 1 - General Information, Equipment Description, and Theory Of Operation</title>
            <para>Chapter 1 contains introductory information on the (insert equipment name)' and its associated equipment,
                as well as equipment description and data and theory of operation.</para>
        </subpara1>
        <subpara1>
            <title>Chapter 2 - Operator Instructions</title>
            <para>Chapter 2 contains preparation for use information, operating information for usual and unusual
                conditions, and controls and indicators.</para>
        </subpara1>
        <subpara1>
            <title>Chapter 3 - Operator Troubleshooting Procedures</title>
            <para>Chapter 3 contains the operator troubleshooting procedures to aid operator members identifying faults
                and correctly fixing them. The symptoms for faults are listed in the troubleshooting index (<xref
                    wpid="T00003-9-4120-433" />), along with the relevant corresponding WP.</para>
        </subpara1>
        <subpara1>
            <title>Chapter 4 - Operator PMCS Instructions</title>
            <para>Chapter 4 provides operator level PMCS procedures.</para>
        </subpara1>
        <subpara1>
            <title>Chapter 5 - Operator Maintenance Instructions</title>
            <para>Chapter 5 provides operator level maintenance procedures, including general and specific item
                maintenance.</para>
        </subpara1>
        <subpara1>
            <title>Chapter 6 - Maintainer Troubleshooting Procedures</title>
            <para>Chapter 6 provides the maintainer troubleshooting procedures to aid maintainers identifying faults and
                correctly fixing them.</para>
        </subpara1>
        <subpara1>
            <title>Chapter 7 - Maintainer PMCS Instructions</title>
            <para>Chapter 7 contains maintainer level PMCS procedures.</para>
        </subpara1>
        <subpara1>
            <title>Chapter 8 - Maintainer Maintenance Instructions</title>
            <para>Chapter 8 contains maintainer level maintenance procedures, including general and specific (insert equipment name) item
                maintenance.</para>
        </subpara1>
        <subpara1>
            <title>Chapter 9 - Auxiliary Equipment Maintenance</title>
            <para>Chapter 9 contains maintainer level maintenance procedures for auxiliary equipment for the (insert equipment name),
                including the electrical special purpose cable assembly.</para>
        </subpara1>
        <subpara1>
            <title>Chapter 10 - Destruction of Equipment to Prevent Enemy Use</title>
            <para>Chapter 10 contains Destruction of Equipment to Prevent Enemy Use Introduction and Destruction of
                Equipment to Prevent Enemy Use Procedures for the (insert equipment name) (<xref wpid="D00001-9-4120-433" />).</para>
        </subpara1>
        <subpara1>
            <title>Chapter 11 - Repair Parts and Special Tools List (RPSTL)</title>
            <para>Chapter 11 provides parts and special tools information for the (insert equipment name) (<xref wpid="R00001-9-4120-433" />).</para>
        </subpara1>
        <subpara1>
            <title>Chapter 12 - Supporting Information</title>
            <para>Chapter 12 contains references, the Maintenance Allocation Chart (MAC), the Components of End Items
                and Basic Issue Items (COEI/BII) lists, the Additional Authorization List (AAL), the Expendable and
                Durable Items list, the Tool Identification List (TIL), Mandatory Replacement Parts List (MRPL), and
                the Critical Safety Items (CSI) list.</para>
        </subpara1>
        <subpara1>
            <title>Rear Matter</title>
            <para>Rear matter consists of an alphabetical index, <xref wpid="S00001-9-4120-433" itemid="Recommended_Changes" />,
                Recommended Changes to Publications and Blank Forms, authentication page, and back cover.</para>
        </subpara1>
    </para0>
    <para0>
        <title>MANUAL ORGANIZATION AND PAGE NUMBERING SYSTEM</title>
        <para>The manual is divided into nine major chapters that detail the topics mentioned above. Within each chapter
            are work packages covering a wide range of topics. Each work package is numbered sequentially starting at
            page 1. The work package has its own page numbering scheme and is independent of the page numbering used by
            other work packages. Each page of a work package has a page number of the form XXXX-YY where XXXX is the
            work package number (e.g. 0010 is work package 10) and YY represents the number of the page within that work
            package. A page number such as 0010-1/blank means that page 1 contains information but page 2 of that work
            package has been intentionally left blank.</para>
        <subpara1>
            <title>Finding Information</title>
            <para>The table of contents permits the reader to find information in the manual quickly. The reader should
                start here first when looking for a specific topic. The table of contents lists the topics contained
                within each chapter and the work package sequence number where it can be found.</para>
        </subpara1>
        <subpara1>
            <title>Example:</title>
            <para>If the reader was looking for information about the purpose of the (insert equipment name), which is a general information
                topic, the table of contents indicates that general information can be found in chapter 1. Scanning down
                the listings for chapter 1, information on the purpose of the (insert equipment name) can be found in <xref wpid="G00001-9-4120-433" />,
                General Information. (i.e. work package <xref wpid="G00001-9-4120-433" />).</para>
        </subpara1>
        <subpara1>
            <title>Alphabetical Index</title>
            <para>An alphabetical index can be found at the back of the manual; specific topics are listed with the
                corresponding work package number.</para>
        </subpara1>
    </para0>
    <para0>
        <title>WARNINGs, CAUTIONs, and NOTEs</title>
        <para>Warning, caution, and note headings, chapter titles, and paragraph headings are printed in bold type.
            Warning icons may be included below the warning heading. Multiple warning, caution, or note paragraphs, if
            necessary, will appear below one warning, caution, or note heading. Prior to starting a WP, all warnings
            included in the WP should be reviewed, understood, and followed. Review the materials/parts in the initial
            setup of the WP for any hazardous materials used during maintenance of the equipment. Then refer to the
            detailed warnings for hazardous materials in the Warning Summary. Make sure to read all warnings within
            referenced WP that are required to complete tasks.</para>
        <para>
            <term.def>
                <term>WARNING</term>
                <def>
                    <para>Warning identifies a clear danger for injury or death to the person operating equipment or
                        performing maintenance if essential procedures are not observed. First aid information is
                        included in the event of injury. A warning is also used when there is danger to personnel and
                        equipment simultaneously.</para>
                </def>
            </term.def>
            <term.def>
                <term>CAUTION</term>
                <def>
                    <para>Caution identifies a clear risk of damage to, or destruction of, the equipment if the
                        procedure is not followed correctly.</para>
                </def>
            </term.def>
            <term.def>
                <term>NOTE</term>
                <def>
                    <para>Note is used to highlight essential information, conditions, or statements or convey important
                        instructional data to the user.</para>
                </def>
            </term.def>
        </para>
    </para0>
    <para0>
        <!-- CHANGE: Remove items that are not used -->
        <title>INITIAL SETUP INFORMATION</title>
        <para>Initial setup information can be found at the beginning of every procedural work package. Initial setup
            information applies to all tasks found in that work package</para>
        <subpara1>
            <title>Test Equipment</title>
            <!-- Repair parts for operator manuals are found in AAL; maintainer and above are
				found in RPSTL -->
            <para>Lists all expendable test equipment required to perform task. Test equipment
                is referenced to the applicable Tool Identification List (<xref wpid="S00007-9-4120-433" />).</para>
		 </subpara1>
        <subpara1>
            <title>Tools</title>
            <!-- Repair parts for operator manuals are found in AAL; maintainer and above are
				found in RPSTL -->
            <para>Lists all tools required to perform task. Tools
                are referenced to the applicable Tool Identification List (<xref wpid="S00007-9-4120-433" />).</para>
        </subpara1>
        <subpara1>
            <title>Materials</title>
            <!-- Repair parts for operator manuals are found in AAL; maintainer and above are
				found in RPSTL -->
            <para>Lists all expendable items, repair parts, and support materials required to perform task. Materials
                are referenced to the applicable Expendable and Durable Items List (<xref wpid="S00006-9-4120-433" />).</para>
        </subpara1>
        <subpara1>
            <title>Mandatory Replacement Parts</title>
            <para>Lists all parts that must be replaced during maintenance whether they have failed or not. Items are
                referenced to the Mandatory Replacement Parts List (<xref
                    wpid="S00008-9-4120-433" />).</para>
        </subpara1>
        <subpara1>
            <title>Personnel Required</title>
            <para>Lists the type of personnel required by MOS and designation. Quantity of MOS-specific personnel are
                given if more than one is required (e.g. Utilities Equipment Repairer 91C or Utilities Equipment
                Repairer 91C (2)). One skilled person may be identified with additional helpers that do not require a
                specific skill set. If the task does not require any specific skills, the number of people required will
                be identified with no MOS designation.</para>
        </subpara1>
        <subpara1>
            <title>References</title>
            <para>Lists other work packages, TMs, foldouts, and other sources that are required to complete a task.
                These references should be gathered prior to beginning the task. References listed in the Equipment
                Condition are not repeated here.</para>
        </subpara1>
        <subpara1>
            <title>Equipment Condition</title>
            <para>Lists any special state or condition the equipment must be placed before the task can be performed.
                Items are listed in the order required to perform and include reference to the appropriate source for
                setting up the condition.</para>
        </subpara1>
        <subpara1>
            <title>Special Environmental Condition</title>
            <para>Lists any special environmental conditions that are required before a task can be performed including
                the reason for the condition.</para>
        </subpara1>
        <subpara1>
            <title>Drawings Required</title>
            <para>Lists all drawings, diagrams, and/or schematics required to complete maintenance task which are not
                found in the work package.</para>
        </subpara1>
        <subpara1>
            <title>Estimated Time to Complete</title>
            <para>Estimated time to complete maintenance task based on Reliability, Availability, and Maintainability
                data.</para>
        </subpara1>
    </para0>
    <para0>
        <title>USING THE RPSTL</title>
        <para>The RPSTL lists repair parts and other special support equipment required for performance of field
            maintenance of (insert equipment name). It authorizes the requisitioning, issue, and disposition of repair
            parts as indicated by the source, maintenance, and recoverability (SMR) codes. All parts information can be
            found in the RPSTL (<xref wpid="R00002-9-4120-433" /> to <xref wpid="R00099-9-4120-433" />). Refer to <xref
                wpid="R00001-9-4120-433" /> for specific instructions on how to use the RPSTL.</para>
    </para0>
    <para0>
        <title>FINDING INFORMATION</title>
        <para>The table of contents permits the reader to find information in the manual quickly. The reader should
            start here first when looking for a specific topic. The table of contents sequentially lists the topics,
            figures, and tables contained within each chapter and the work package sequence number where it can be
            found.</para>
        <!-- CHANGE: Use the index statement applicable to your TM or none if that applies -->
        <para>Alternatively, the index, located in the back of the TM, lists work package titles alphabetically with the
            work package sequence number where it can be found.</para>
        <para>Alternatively, the detailed index, located in the back of the TM, lists topics and subtopics
            alphabetically with the work package sequence number where it can be found.</para>
    </para0>
    <para0>
        <title>HOW TO FIX AN EQUIPMENT MALFUNCTION</title>
        <para>Fault conditions can be found in the troubleshooting index work package (<xref
                wpid="T00003-9-4120-433" />). The reader will be directed to the appropriate work package to begin the
            troubleshooting process. The fault condition will be listed in the work package as a symptom with one or
            more possible malfunctions. Each malfunction will have one or more corrective actions to be performed. The
            corrective action may reference to another work package in the TM to proceed.</para>
        <subpara1>
            <title>Preparing for a Task</title>
            <para>Be sure the entire maintenance procedure is understood before beginning any maintenance task. Ensure
                that all reference materials, parts, and tools are handy. Read all steps before beginning.</para>
        </subpara1>
        <subpara1>
            <title>Performing the Task</title>
            <para>Pay attention to WARNING, CAUTION, and NOTE statements. A WARNING indicates that someone could be hurt
                or killed. A CAUTION indicates that equipment could be damaged. A NOTE may make your maintenance or
                repair task easier. Refer to the warning summary for explanations of all icons used in this manual. Use
                the List of Abbreviations/Acronyms (<xref wpid="G00001-9-4120-433" />) if the special abbreviations or
                unusual terms used in this manual are not understood. After each corrective action is completed, attempt
                to operate the equipment to determine if the fault is corrected.</para>
        </subpara1>
    </para0>
</howtouse>\n"""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        file_name = "00060-How To Use This Manual.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.front_matter.append(file_name)
        cfg.prefix_file += 1
