"""FRONT MATTER"""
import math
from dotenv import dotenv_values
import cfg


class FrontMatter:
    """Class to create various types of WP's included in the Front Matter section of a TM."""
    config = dotenv_values(".env")  # take environment variables from .env.
    TAB_2 = '\t\t'
    TAB_3 = '\t\t\t'
    TAB_4 = '\t\t\t\t'
    TAB_5 = '\t\t\t\t\t'
    TAB_6 = '\t\t\t\t\t\t'
    TAB_7 = '\t\t\t\t\t\t\t'
    TAB_8 = '\t\t\t\t\t\t\t\t'

    def __init__(self, config, fsc, manual_type, niin, part_no, sys_acronym, sys_name, sys_number, save_path):
        self.config = config
        self.fsc = fsc
        self.manual_type = manual_type
        self.niin = niin
        self.part_no = part_no
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def title_page(self):
        """Function to create title page XML."""
        cfg.prefix_file = (math.floor(cfg.prefix_file / 1000) * 1000) + 10
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n' + '<production chngdate="11 SEPTEMBER 2022" chnglevel="0" date="11 SEPTEMBER 2022" pin="XX-XXX-XX">\n'
        if self.manual_type == '-10':
            tmp += f'\t<paper.manual maintitl="OPERATOR MANUAL FOR {self.sys_name.upper()} ({self.sys_acronym})" maintlvls="10" multivolume="no" pubno="TM {self.sys_number} {self.manual_type}" revno="0" rpstl="no">\n'
        elif self.manual_type == '-12&P':
            tmp += f'\t<paper.manual maintitl="OPERATOR AND FIELD MAINTENANCE MANUAL FOR {self.sys_name.upper()} ({self.sys_acronym})" maintlvls="13" multivolume="no" pubno="TM {self.sys_number}-12" revno="0" rpstl="yes">\n'
        elif self.manual_type == '-13&P':
            tmp += f'\t<paper.manual maintitl="OPERATOR AND FIELD MAINTENANCE MANUAL FOR {self.sys_name.upper()} ({self.sys_acronym})" maintlvls="13" multivolume="no" pubno="TM {self.sys_number}-13" revno="0" rpstl="yes">\n'
        elif self.manual_type == '-23&P':
            tmp += f'\t<paper.manual maintitl="REPAIR PARTS LIST FOR {self.sys_name.upper()} ({self.sys_acronym})" maintlvls="23" multivolume="no" pubno="TM {self.sys_number}-23" revno="0" rpstl="only">\n'
        elif self.manual_type == 'NMWR':
            tmp += f'\t<paper.manual maintitl="END ITEM" maintlvls="nmwr" multivolume="no" pubno="NMWR {self.sys_number}" revno="0" rpstl="yes">\n'
        tmp += self.TAB_2 + '<paper.frnt>\n'
        tmp += self.TAB_3 + '<frntcover>\n'
        tmp += self.TAB_4 + '<?Pub Dtl?>\n'
        tmp += self.TAB_4 + '<tmtitle>\n'
        if self.manual_type == '-10':
            tmp += f'{self.TAB_5}<tmno>TM {self.sys_number} {self.manual_type}</tmno>\n'
        elif self.manual_type == '-12&P':
            tmp += f'{self.TAB_5}<tmno>TM {self.sys_number} {self.manual_type}</tmno>\n'
        elif self.manual_type == '-13&P':
            tmp += f'{self.TAB_5}<tmno>TM {self.sys_number} {self.manual_type}</tmno>\n'
        elif self.manual_type == '-23&P':
            tmp += f'{self.TAB_5}<tmno>TM {self.sys_number} {self.manual_type}</tmno>\n'
        elif self.manual_type == 'NMWR':
            tmp += f'{self.TAB_5}<tmno>NMWR {self.sys_number}</tmno>\n'
        tmp += self.TAB_5 + '<prtitle>\n'
        tmp += self.TAB_6 + '<sysnomen>\n'
        tmp += f'{self.TAB_7}<name>{self.sys_name}</name>\n'
        tmp += self.TAB_7 + '<modelno>(GREEN)</modelno>\n'
        tmp += self.TAB_7 + '<nsn>\n'
        tmp += f'{self.TAB_8}<fsc>{self.fsc}</fsc>\n'
        tmp += f'{self.TAB_8}<niin>{self.niin}</niin>\n'
        tmp += self.TAB_7 + '</nsn>\n'
        tmp += f'{self.TAB_7}<partno>{self.part_no}</partno>\n'
        tmp += self.TAB_7 + '<eic>255</eic>\n'
        tmp += self.TAB_6 + '</sysnomen>\n'
        tmp += self.TAB_5 + '</prtitle>\n'
        tmp += self.TAB_4 + '</tmtitle>\n'
        tmp += self.TAB_4 + '<graphic boardno="I06023300001"/>\n'
        tmp += self.TAB_4 + '<notices>\n'
        tmp += self.TAB_5 + '<dist>\n'
        tmp += self.TAB_6 + '<a.statement/>\n'
        tmp += self.TAB_5 + '</dist>\n'
        tmp += self.TAB_4 + '</notices>\n'
        tmp += f"{self.TAB_4}<servnomen>{self.config.get('HEADQUARTERS')}</servnomen>\n"
        tmp += self.TAB_4 + '<date>11 SEPTEMBER 2022</date>\n'
        tmp += self.TAB_3 + '</frntcover>\n'

        with open(f"{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-FrontCover.txt",
                  'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def warning_summary(self):
        """Function to create Warning Summary section."""
        tmp = '\n<?xml version="1.0" encoding="UTF-8"?>\n' + '<warnsum>\n'
        tmp += f"\t<para>{self.config.get('WARNING_SUMMARY')}</para>\n"
        tmp += '\t<first_aid>\n'
        tmp += self.TAB_2 + '<title>First Aid</title>\n'
        tmp += f"{self.TAB_2}<para>{self.config.get('SW_FIRSTAID')}</para>\n"
        tmp += '\t</first_aid>\n'
        tmp += '\t<safety>\n'
        tmp += self.TAB_2 + '<title>Explanation of Safety Warning Icons</title>\n'
        # Beginning of explanation of safety warning icons section
        # EAR PROTECTION
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Ear_Protection_Symbol"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>EAR PROTECTION</title>\n'
        tmp += f"{self.TAB_4}<text>{self.config.get('SW_EAR_PROTECTION')}</text>\n"

        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        # ELECTRICAL
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Electrical_Symbols"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>ELECTRICAL</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('SW_ELECTRICAL') + '</text>\n'
        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        # FALLING
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Falling"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>FALLING</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('SW_FALLING') + '</text>\n'
        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        # FALLING PARTS
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Falling_Parts"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>FALLING PARTS</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('SW_FALLING_PARTS') + '</text>\n'

        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        # FLYING PARTICLES
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Flying_Particles_wShield"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>FLYING PARTICLES</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('SW_FLYING_PARTICLES') + '</text>\n'

        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        # HEAVY OBJECT
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Heavy_Object"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>HEAVY OBJECT</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('SW_HEAVY_OBJECT') + '</text>\n'
        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        # HEAVY PARTS ABOVE
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Heavy_Parts-above"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>HEAVY PARTS</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('SW_HEAVY_PARTS_ABOVE') + '</text>\n'

        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        # HEAVY PARTS FOOT
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Heavy_Parts-foot"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>HEAVY PARTS</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('SW_HEAVY_PARTS_FOOT') + '</text>\n'

        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        # HEAVY PARTS HAND
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Heavy_Parts-hand"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>HEAVY PARTS</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('SW_HEAVY_PARTS_HAND') + '</text>\n'

        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        # HEAVY PARTS WALL
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Heavy_Parts-wall"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>HEAVY PARTS</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('SW_HEAVY_PARTS_WALL') + '</text>\n'

        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        # HOT AREA
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Hot_Area"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>HOT AREA</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('SW_HOT_AREA') + '</text>\n'
        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        # MOVING PARTS FINGERS
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Moving_Parts-fingers"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>MOVING PARTS</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('SW_MOVING_PARTS') + '</text>\n'
        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        # SHARP OBJECT IN HAND
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Sharp_Object-in_hand"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>SHARP OBJECT</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('SW_SHARP_OBJECT') + '</text>\n'
        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        # SLICK FLOOR
        tmp += self.TAB_2 + '<sfty-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Slick_Floor"/>\n'
        tmp += self.TAB_3 + '<sftydesc>\n'
        tmp += self.TAB_4 + '<title>SLICK FLOOR</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('SW_SLICK_FLOOR') + '</text>\n'
        tmp += self.TAB_3 + '</sftydesc>\n'
        tmp += self.TAB_2 + '</sfty-icons>\n'
        tmp += '\t</safety>\n'
        tmp += '\t<warninfo>\n'

        # General safety warnings descriptions section
        tmp += self.TAB_2 + '<title>GENERAL SAFETY WARNINGS DESCRIPTIONS</title>\n'
        tmp += self.TAB_2 + '<warning>\n'
        tmp += self.TAB_3 + '<icon-set boardno="Slick_Floor"/>\n'
        tmp += self.TAB_3 + \
               '<trim.para>All doors and doorways must remain unblocked, both inside and outside, during operation of system to allow for egress during an emergency. Failure to comply may result in serious injury or death to personnel. Seek immediate medical attention if injury occurs.</trim.para>\n'
        tmp += self.TAB_2 + '</warning>\n'

        tmp += self.TAB_2 + '<warning>\n'
        tmp += self.TAB_3 + '<icon-set boardno="Electrical_Symbols"/>\n'
        tmp += f'{self.TAB_3}<trim.para>Interior and exterior areas of {self.sys_acronym.upper()} may be a wet environment. Electrical cables and controls should not be handled with wet hands or while standing in water. Failure to comply may result in serious injury or death to personnel. Seek immediate medical attention if injury occurs.</trim.para>\n'

        tmp += self.TAB_2 + '</warning>\n'

        tmp += self.TAB_2 + '<warning>\n'
        tmp += self.TAB_3 + '<icon-set boardno="Electrical_Symbols"/>\n'
        tmp += self.TAB_3 + \
               '<trim.para>Power source and ' + self.sys_acronym.upper() + ' container must all be grounded to ensure safety of personnel during operation. Operating ' + self.sys_acronym.upper() + ' components while ungrounded or improperly grounded may expose personnel to risk of shock resulting in serious injury or death to personnel. Seek immediate medical attention if injury occurs.</trim.para>\n'
        tmp += self.TAB_3 + \
               '<trim.para>High voltage is present during operation. All electrical safety precautions must be followed when operating or maintaining equipment. Failure to comply may result in death or serious injury to personnel. Seek immediate medical attention if exposed to electricity.</trim.para>\n'
        tmp += self.TAB_3 + \
               '<trim.para>Source power must be off prior to connecting or removing power cables to ' + self.sys_acronym.upper() + ' shelter.</trim.para>\n'
        tmp += self.TAB_3 + \
               '<trim.para>All jewelry must be removed before starting work. Metal objects, such as rings or tools, can cause short circuits when contacting live circuits. A direct short can cause instant heating of metal resulting in severe burns. Failure to comply may result in serious injury or death to personnel. Seek immediate medical attention if exposed to electricity.</trim.para>\n'
        tmp += self.TAB_2 + '</warning>\n'
        tmp += '\t</warninfo>\n'

        # Explanation of hazardous material icons section
        tmp += '\t<hazmat>\n'
        tmp += self.TAB_2 + '<title>EXPLANATION OF HAZARDOUS MATERIALS ICONS</title>\n'
        tmp += self.TAB_2 + '<haz-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Biological_Symbol"/>\n'
        tmp += self.TAB_3 + '<hazdesc>\n'
        tmp += self.TAB_4 + '<title>BIOLOGICAL</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('HM_BIOLOGICAL') + '</text>\n'
        tmp += self.TAB_3 + '</hazdesc>\n'
        tmp += self.TAB_2 + '</haz-icons>\n'

        tmp += self.TAB_2 + '<haz-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Chemical"/>\n'
        tmp += self.TAB_3 + '<hazdesc>\n'
        tmp += self.TAB_4 + '<title>CHEMICAL</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('HM_CHEMICAL') + '</text>\n'
        tmp += self.TAB_3 + '</hazdesc>\n'
        tmp += self.TAB_2 + '</haz-icons>\n'

        tmp += self.TAB_2 + '<haz-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Explosion"/>\n'
        tmp += self.TAB_3 + '<hazdesc>\n'
        tmp += self.TAB_4 + '<title>EXPLOSION</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('HM_EXPLOSION') + '</text>\n'
        tmp += self.TAB_3 + '</hazdesc>\n'
        tmp += self.TAB_2 + '</haz-icons>\n'

        tmp += self.TAB_2 + '<haz-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Eye_Protection"/>\n'
        tmp += self.TAB_3 + '<hazdesc>\n'
        tmp += self.TAB_4 + '<title>EYE PROTECTION</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('HM_EYE_PROTECTION') + '</text>\n'

        tmp += self.TAB_3 + '</hazdesc>\n'
        tmp += self.TAB_2 + '</haz-icons>\n'

        tmp += self.TAB_2 + '<haz-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Fire"/>\n'
        tmp += self.TAB_3 + '<hazdesc>\n'
        tmp += self.TAB_4 + '<title>FIRE</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('HM_FIRE') + '</text>\n'
        tmp += self.TAB_3 + '</hazdesc>\n'
        tmp += self.TAB_2 + '</haz-icons>\n'

        tmp += self.TAB_2 + '<haz-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Poison"/>\n'
        tmp += self.TAB_3 + '<hazdesc>\n'
        tmp += self.TAB_4 + '<title>POISON</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('HM_POISON') + '</text>\n'
        tmp += self.TAB_3 + '</hazdesc>\n'
        tmp += self.TAB_2 + '</haz-icons>\n'

        tmp += self.TAB_2 + '<haz-icons>\n'
        tmp += self.TAB_3 + '<symbol boardno="Vapor"/>\n'
        tmp += self.TAB_3 + '<hazdesc>\n'
        tmp += self.TAB_4 + '<title>VAPOR</title>\n'
        tmp += f'{self.TAB_4}<text>' + self.config.get('HM_VAPOR') + '</text>\n'
        tmp += self.TAB_3 + '</hazdesc>\n'
        tmp += self.TAB_2 + '</haz-icons>\n'

        # Explanation of general hazardous materials descriptions section
        tmp += self.TAB_2 + '<title>GENERAL HAZARDOUS MATERIALS DESCRIPTIONS</title>\n'
        tmp += self.TAB_2 + '<hazard>\n'
        tmp += self.TAB_3 + '<hazid>CLEANING PRODUCTS</hazid>\n'
        tmp += self.TAB_3 + '<symbol boardno="Chemical"/>\n'
        tmp += self.TAB_3 + '<symbol boardno="Poison"/>\n'
        tmp += f'{self.TAB_3}<para>' + self.config.get('HM_CLEANING') + '</para>\n'
        tmp += self.TAB_2 + '</hazard>\n'

        tmp += self.TAB_2 + '<hazard>\n'
        tmp += self.TAB_3 + '<hazid>WASTEWATER</hazid>\n'
        tmp += self.TAB_3 + '<symbol boardno="Biological_Symbol"/>\n'
        tmp += f'{self.TAB_3}<para>' + self.config.get('HM_WASTEWATER') + '</para>\n'
        tmp += f'{self.TAB_3}<para>' + self.config.get('HM_WASTEWATER_2') + '</para>\n'
        tmp += self.TAB_2 + '</hazard>\n'

        tmp += self.TAB_2 + '<hazard>\n'
        tmp += self.TAB_3 + '<hazid>ISOPROPYL ALCOHOL</hazid>\n'
        tmp += self.TAB_3 + '<symbol boardno="Eye_Protection"/>\n'
        tmp += self.TAB_3 + '<symbol boardno="Vapor"/>\n'
        tmp += f'{self.TAB_3}<para>' + self.config.get('HM_ISOPROPYL') + '</para>\n'
        tmp += self.TAB_2 + '</hazard>\n'

        tmp += self.TAB_2 + '<hazard>\n'
        tmp += self.TAB_3 + '<hazid>FUEL</hazid>\n'
        tmp += self.TAB_3 + '<symbol boardno="Fire"/>\n'
        tmp += f'{self.TAB_3}<para>' + self.config.get('HM_FUEL') + '</para>\n'
        tmp += self.TAB_2 + '</hazard>\n'
        tmp += '\t</hazmat>\n' + '</warnsum>\n'

        with open(
                f"{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-WarningSummary.txt",
                'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def loep(self):
        """Function to create the List of Effective Pages/WP's section."""
        tmp = '''<loepwp>
        <title>List of Effective Pages/Work Packages</title>
        <note>
            <trim.para>NOTE: Zero in the "Change No." column indicates an original page or work package.</trim.para>
        </note>
        <issuechg>
            <trim.para>Date of issue for the original manual is:</trim.para>
            <issued>
                <chgno>Original Draft</chgno>
                <chgdate julian="XXXXXX">XXXXXX</chgdate>
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
        <chghistory modified="none">
            <pageno></pageno>
            <pageno></pageno>
            <chgno>0</chgno>
        </chghistory>
        <chghistory modified="none">
            <pageno></pageno>
            <pageno></pageno>
            <chgno>0</chgno>
        </chghistory>

        <!--   WP#: 0001  -->
        <chghistory modified="none">\n'''
        tmp += '<wpno wpref="G00001-' + self.sys_number + '"/>\n'
        tmp += '''<wppages>X pgs</wppages>
            <chgno></chgno>
        </chghistory>

        <!--   WP#: 0002  -->
        <chghistory modified="none">\n'''
        tmp += '<wpno wpref="G00002-' + self.sys_number + '"/>\n'
        tmp += '''<wppages>X pgs</wppages>
            <chgno>0</chgno>
        </chghistory>

        <!--   WP#: 0003  -->
        <chghistory modified="none">\n'''
        tmp += '<wpno wpref="G00003-' + self.sys_number + '"/>\n'
        tmp += '''<wppages>X pgs</wppages>
            <chgno>0</chgno>
        </chghistory>
    </loepwp>'''

        with open(f"{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-LOEP.txt", 'w',
                encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 1

    def tb_toc_htu(self):
        """Function that creates Title Block, TOC & How to Use sections."""
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
<titleblk>
    <servnomen>HEADQUARTERS, DEPARTMENT OF THE ARMY</servnomen>
    <city>WASHINGTON</city>
    <state>DC</state>
    <date>11 SEPTEMBER 2022</date>
    <prtitle>
        <sysnomen>\n'''
        tmp += '\t\t\t<name>' + self.sys_name.upper() + ' (' + self.sys_acronym.upper() + ')' + '</name>\n'
        tmp += '\t\t\t<modelno>GREEN </modelno>\n'
        tmp += '\t\t\t<nsn>\n'
        tmp += '\t\t\t\t<fsc>' + self.fsc + '</fsc>\n'
        tmp += '\t\t\t\t<niin>' + self.niin + '</niin>\n'
        tmp += '''\t\t\t</nsn>
        </sysnomen>
    </prtitle>
    <reporting>
        <title/>
        <para/>
        <reporting.para service="army">You can help improve this publication. If you find any errors, or if you would like to recommend any improvements to the procedures in this publication, please let us know. The preferred method is to submit your <extref docno="DA Form 2028" posttext=" (Recommended Changes to Publications and Blank Forms)"/> through the Internet on the TACOM Unique Logistics Support Applications (TULSA) Web site. The Internet address is 
            <internet>
                <homepage protocol="https" uri="tulsa.tacom.army.mil"/>
            </internet>. Access to all applications requires CAC authentication, and you must complete the Access Request form the first time you use it. The <extref docno="DA Form 2028"/> is located under the TULSA Applications on the left-hand navigation bar. Fill out the form and click on SUBMIT. Using this form on the TULSA Web site will enable us to respond more quickly to your comments and to better manage the <extref docno="DA Form 2028"/> program. You may also mail, e-mail, or fax your comments or <extref docno="DA Form 2028"/> directly to the U.S. Army TACOM Life Cycle Management Command. The postal mail address is <proponent>
            <name>U.S. Army Tank-Automotive and Armaments Command, ATTN: AMSTA-LCL-IMP/TECH PUBS, MS 727,</name>
            <address>
                <street>6501 E. 11 Mile Road,</street>
                <city>Warren,</city>
                <state>MI </state>
                <zip>48397-5000</zip>
            </address>
            </proponent>. The e-mail address is 
                <internet>
                    <email address="usarmy.detroit.tacom.mbx.ilsc-tech-pubs@army.mil"/>
                </internet>. The fax number is <phone type="dsn" receive="fax">786-1856</phone> or <phone type="coml" receive="fax">(586) 282-1856</phone>. A reply will be furnished to you.
        </reporting.para>
        <para/>
    </reporting>
    <notices>
        <dist>
            <a.statement/>
        </dist>
        <!-- CHANGE: Commercial equipment logos if required<general_purpose_notices><title>USE OF MANUFACTURER'S NAME OR LOGO</title><text>Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise, does not constitute or imply endorsement, recommendation, or favoring by the United States Government of one specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise, over another.</text></general_purpose_notices> -->
    </notices>
</titleblk>
<contents>
    <title/>
    <col.title>WP Sequence No.</col.title>
    <col.title>Page No.</col.title>
    <contententry>
        <title/>
    </contententry>
</contents>\n'''
        if self.manual_type.lower() != 'nmwr':
            tmp += '''<howtouse>
    <title/>
    <para0>
        <title>HOW TO OBTAIN TECHNICAL MANUALS</title>\n'''
            tmp += f"\t\t<para>{self.config.get('OBTAIN_TM_P1')}</para>\n"
            tmp += f"{self.TAB_2}<para>{self.config.get('OBTAIN_TM_P2')}</para>\n"
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>Instructions for Unit Publications Clerk</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('UNIT_PUB_CLERK_P1') + '</para>\n'

            tmp += f"{self.TAB_3}<para>{self.config.get('UNIT_PUB_CLERK_P2')}</para>\n"

            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += '\t</para0>\n'
            tmp += '\t<para0>\n'
            tmp += self.TAB_2 + '<title>HOW TO USE THIS MANUAL</title>\n'
            tmp += f'{self.TAB_2}<para>' + self.config.get('HOW_TO_USE') + '</para>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>FRONT MATTER</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('FRONT_MATTER') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'

            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + \
               '<title>CHAPTER 1 - GENERAL INFORMATION, EQUIPMENT DESCRIPTION, AND THEORY OF OPERATION</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('CHAPTER_1') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>CHAPTER 2 - OPERATOR INSTRUCTIONS</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('OPERATOR_INSTRUCTIONS') + '</para>\n'

            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>CHAPTER 3 - TROUBLESHOOTING INDEX</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('TS_INDEX') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>CHAPTER 4 - CREW TROUBLESHOOTING PROCEDURES</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('CREW_TS') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>CHAPTER 5 - MAINTAINER TROUBLESHOOTING PROCEDURES</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('MAINTAINER_TS') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + \
               '<title>CHAPTER 6 - PREVENTIVE MAINTENANCE CHECKS AND SERVICES (PMCS) MAINTENANCE INSTRUCTIONS</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('PMCS') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>CHAPTER 7 - CREW MAINTENANCE INSTRUCTIONS</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('CREW_MAINTENANCE') + '</para>\n'

            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>CHAPTER 8 - MAINTAINER MAINTENANCE INSTRUCTIONS</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('MAINTAINER_MAINTENANCE') + '</para>\n'

            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + \
               '<title>CHAPTER 9 - DESTRUCTION OF EQUIPMENT TO PREVENT ENEMY USE</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('DESTRUCTION') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>CHAPTER 10 - REPAIR PARTS AND SPECIAL TOOLS LIST</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('RPSTL') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>CHAPTER 11 - SUPPORTING INFORMATION</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('SUPPORTING_INFO') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>REAR MATTER</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('REAR_MATTER') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += '\t</para0>\n'
            tmp += '\t<para0>\n'
            tmp += self.TAB_2 + '<title>Manual Organization and Page Numbering System</title>\n'
            tmp += f'{self.TAB_2}<para>' + self.config.get('PAGE_NUM_SYSTEM') + '</para>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>Finding Information</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('FINDING_INFO_1') + '</para>\n'
            tmp += self.TAB_3 + \
               '<!-- CHANGE: USE the index statement applicable to your TM or none if that applies. -->\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('FINDING_INFO_2') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>Example:</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('EXAMPLE') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>Alphabetical Index</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('ALPHABETICAL_INDEX') + '</para>\n'

            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += '''\t</para0>
                <para0>
            \t<!-- CHANGE: Remove items that are not used -->
            \t<title>Initial Setup Information</title>'''
            tmp += '\t<para>' + self.config.get('INITIAL_SETUP_INFO') + '</para>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_2 + '<title>Tools</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('TOOLS') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'

            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>Materials</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('MATERIALS') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'

            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>Mandatory Replacement Parts</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('MRP') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>Personnel Required</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('PERSONNEL_REQUIRED') + '</para>\n'

            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>References</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('REFERENCES') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>Equipment Condition</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('EQUPMENT_CONDITION') + '</para>\n'

            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>Special Environmental Condition</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('SPECIAL_ENV_CONDITION') + '</para>\n'

            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>Drawings Required</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('DRAWINGS_REQUIRED') + '</para>\n'

            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>Estimated Time to Complete</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('EST_TIME_TO_COMPLETE') + '</para>\n'

            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += '\t</para0>\n'
            tmp += '\t<para0>\n'
            tmp += self.TAB_2 + '<title>Finding Information</title>\n'
            tmp += f'{self.TAB_2}<para>' + self.config.get('FINDING_INFO_1') + '</para>\n'
            tmp += self.TAB_2 + '<!-- CHANGE: Use the index statement applicable to your TM or none if that applies -->\n'
            tmp += f'{self.TAB_2}<para>' + self.config.get('FINDING_INFO_2') + '</para>\n'
            tmp += '\t</para0>\n'
            tmp += '\t<para0>\n'
            tmp += self.TAB_2 + '<title>How To Fix An Equipment Malfunction</title>\n'
            tmp += f'{self.TAB_2}<para>' + self.config.get(
                'HOW_TO_FIX_EQUIPMENT_MALFUNCTION') + ' <!--DELETE THIS SENTENCE IF NOT USED-->\n'

            tmp += self.TAB_2 + '</para>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>Preparing for a Task</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('PREP_FOR_TASK') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += self.TAB_2 + '<subpara1>\n'
            tmp += self.TAB_3 + '<title>Performing the Task</title>\n'
            tmp += f'{self.TAB_3}<para>' + self.config.get('PERFORMING_TASK') + '</para>\n'
            tmp += self.TAB_2 + '</subpara1>\n'
            tmp += '\t</para0>\n'
            tmp += '</howtouse>\n'
        tmp += '</paper.frnt>\n'

        with open(
                f"{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-TitleBlock_TOC_HowToUse.txt",
                'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10
