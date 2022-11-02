"""REAR MATTER"""
class RearMatter:
    """Class to create various types of WP's included in the Rear Matter section of a TM."""
    def __init__(self, manual_type, sys_acronym, save_path):
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.save_path = save_path

    def rear_matter(self):
        """Function to create rear matter."""
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
    <rear>
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
                <title>Lorem Ipsum</title>
                <wpno wpref="XX-XXXX-XXX"/>
                <pageno></pageno>
            </indexentry>
            <alphaindx></alphaindx>
            <indexentry>
                <title>Lorem Ipsum</title>
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
    </rear>
</paper.manual>
</production>'''
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/ZZZZZ-REAR_MATTER.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
            _f.close()
