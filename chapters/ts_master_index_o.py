"""TROUBLESHOOTING MASTER INDEX"""
import math
import cfg

class TSMasterIndex:
    """Class to create various types of WP's included in the TS Master Index of a TM."""
    def __init__(self, manual_type, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function that creates TS Master Index WP starting tags of TM."""
        cfg.prefix_file = (math.floor(cfg.prefix_file/1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
<tim chngno="0" revno="0" chap-toc="no">\n'''
        tmp += '\t<titlepg maintlvl="operator">\n'
        tmp += f'\t\t<name>{self.sys_name} ({self.sys_acronym})</name>\n'
        tmp += '\t</titlepg>\n'
        tmp += '\t<masterindexcategory>\n'
        with open(f'{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-TS_MASTER_INDEX_START.txt', 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def tsindxwp(self):
        """Function to create a Troubleshooting Index WP."""
        tmp = f'<tsindxwp chngno="0" wpno="T00000-{self.sys_number}">\n'
        tmp += '\t<wpidinfo>\n'
        tmp += '\t\t<maintlvl level="operator"/>\n'
        tmp += f'''\t\t<title>TROUBLESHOOTING INDEX</title>
    </wpidinfo>
    <geninfo>
        <title>GENERAL</title>
        <para>This chapter provides operator and maintainer maintenance information and includes troubleshooting maintenance procedures.</para>
        <para>
            <emphasis emph="bold">TROUBLESHOOTING INDEX</emphasis>
        </para>
        <para>Troubleshooting index lists common malfunctions that may occur during {self.sys_acronym} shelter inspection and operation. Find malfunction to be eliminated and go to indicated troubleshooting work package that follows. Index cannot list all malfunctions that may occur, all tests or inspections needed to find fault, nor all actions required to correct fault. If existing malfunction is not listed, or cannot be corrected through this troubleshooting index, notify next higher level of maintenance.</para>
    </geninfo>
    <tsindx.symptom>
        <title>Troubleshooting Index</title>
        <tsindx.symptom-category>
            <title>Lorem Ipsum</title>
            <tsindx.symptom-entry>
                <malfunc label="symptom">Lorem Ipsum</malfunc>
                <action>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                </action>
            </tsindx.symptom-entry>
        </tsindx.symptom-category>
        <tsindx.symptom-category>
            <title>Lorem Ipsum</title>
            <tsindx.symptom-entry>
                <malfunc label="symptom">Lorem Ipsum</malfunc>
                <action>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                </action>
            </tsindx.symptom-entry>
            <tsindx.symptom-entry>
                <malfunc label="symptom">Lorem Ipsum</malfunc>
                <action>
                    <para>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</para>
                </action>
            </tsindx.symptom-entry>
        </tsindx.symptom-category>
    </tsindx.symptom>
</tsindxwp>'''
        with open(f"{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-T00000-TSMasterIndex.txt", 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self):
        """Function to create TS Master Index WP end tags."""
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        tmp = '\t</masterindexcategory>\n' + '</tim>'
        with open(f"{self.save_path}/{self.sys_acronym} {self.manual_type} WIP/{cfg.prefix_file:05d}-TS_MASTER_INDEX_END.txt", 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 1       