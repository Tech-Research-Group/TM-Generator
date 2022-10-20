"""PARTS INFORMATION"""
import math
import cfg

class PartsInformation:
    """Class to create various types of WP's included in Parts Information list of a TM."""
    def __init__(self, manual_type, sys_acronym, sys_name, sys_number, save_path):
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.sys_number = sys_number
        self.save_path = save_path

    def start(self):
        """Function to create Parts Information list section start tags."""
        cfg.prefix_file = (math.floor(cfg.prefix_file/1000) * 1000) + 10
        tmp = '''<?xml version="1.0" encoding="UTF-8"?>
    <pim chngno="0" revno="0" chap-toc="no" dmwr-inclus="none">\n'''
        tmp += '\t<titlepg maintlvl="operator">\n'
        tmp += '\t\t<name>' + self.sys_name + ' (' + self.sys_acronym + ')</name>\n'
        tmp += '\t</titlepg>\n'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-PARTS_INFO_START.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def introwp(self):
        """Function that creates the Parts Information list Introduction WP."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += '<introwp chngno="0" wpno="R00001-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>PARTS INFORMATION INTRODUCTION</title>
        </wpidinfo>
        <title>INTRODUCTION</title>
        <para0>
            <!-- ADD TM TITLE IN THIS AREA  -->
            <title>SCOPE</title>
            <para>This Parts Information list lists authorized spares and repair parts; special tools; special test, measurement, and diagnostic equipment (TMDE); and other special support equipment required for performance of field maintenance of {self.sys_name} ({self.sys_acronym}). It authorizes requisitioning, issue, and disposition of spares, repair parts, and special tools as indicated by source, maintenance, and recoverability (SMR) codes.</para>
        </para0>
        <para0>
            <title>GENERAL</title>
            <para>In addition to Introduction work package, this Parts Information list is divided into following work packages.<seqlist>
                    <item>Repair Parts List Work Packages. Work packages containing lists of spare and repair parts authorized for use in performance of maintenance at levels determined by MAC/SMR code. These work packages also include parts which must be removed for replacement of authorized parts. Parts lists are composed of functional groups in ascending alphanumeric sequence, with parts in each group listed in ascending figure and item number sequence. Sending units, brackets, filters, and bolts are listed with component they mount on. Bulk materials are listed by item name in Bulk Items work package which follows last Parts List work package. Repair parts kits are listed at end of individual work packages. Repair parts kits for reparable special tools are also listed in a separate work package. Items listed are shown on associated illustrations.</item>
                    <item>Bulk Items Work Package. This work package lists all items identified as &lsquo;bulk&rsquo; in parts lists. Due to nature of bulk items, this work package does not include a Figure.</item>
                    <item>Special Tools List Work Packages. This work package lists those special tools, special TMDE, and special support equipment authorized by this Parts Information list (as indicated by Basis of Issue (BOI) information in DESCRIPTION AND USABLE ON CODE (UOC) column). Tools that are components of common tool sets and/or Class VII are not listed.</item>
                    <item>Cross-Reference Indexes Work Packages. There are two cross-reference indexes work packages in this Parts Information list. National Stock Number (NSN) Index work package refers you to Figure and item number for each NSN listed in Parts Information list. Part Number Index work package refers you to figure and item number for each part number listed in Parts Information list.</item>
                </seqlist>
            </para>
        </para0>
        <para0>
            <title>EXPLANATION OF COLUMNS IN REPAIR PARTS LIST AND SPECIAL TOOLS LIST WORK PACKAGES</title>
            <para>ITEM NO. (Column 1). Indicates number used to identify items called out in illustration.</para>
            <para>SMR CODE (Column 2). SMR code containing supply/requisitioning information, maintenance level authorization criteria, and disposition instruction, as shown in following breakout. This entry may be subdivided into 4 subentries, one for each service.<table frame="none">
                    <title>SMR Code Explanation</title>
                    <tgroup align="left" char=" " charoff="50" cols="6">
                        <colspec colname="col1" colwidth="0.75*"/>
                        <colspec colname="col2" colwidth="1*"/>
                        <colspec colname="col3" colwidth="1*"/>
                        <colspec colname="col4" colwidth="1*"/>
                        <colspec colname="col5" colwidth="1.25*"/>
                        <colspec colname="col6" colwidth="0.75*"/>
                        <tbody valign="top">
                            <row>
                                <entry align="center" colsep="0" morerows="0" rotate="no" rowsep="0" valign="bottom"/>
                                <entry align="center" colsep="0" morerows="0" rotate="no" rowsep="0" valign="bottom">Source <?Pub _newline?>
                                    <emphasis emph="uline">Code</emphasis>
                                    <?Pub _newline?>
                                    <emphasis emph="uline">XX</emphasis>
                                </entry>
                                <entry align="center" colsep="0" morerows="0" nameend="col4" namest="col3" rotate="no" rowsep="0" valign="bottom">Maintenance<?Pub _newline?>
                                    <emphasis emph="uline">Code</emphasis>
                                    <?Pub _newline?>
                                    <emphasis emph="uline">XX</emphasis>
                                </entry>
                                <entry align="center" colsep="0" morerows="0" rotate="no" rowsep="0" valign="bottom">Recoverability<?Pub _newline?>
                                    <emphasis emph="uline">Code</emphasis>
                                    <?Pub _newline?>
                                    <emphasis emph="uline">X</emphasis>
                                </entry>
                                <entry colsep="0" rowsep="0" valign="top"/>
                            </row>
                            <row>
                                <entry colsep="0" rowsep="0" valign="top"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">1st two<?Pub _newline?>positions:<?Pub _newline?>How to get <?Pub _newline?> an item.</entry>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">3rd position:<?Pub _newline?>Who can install,<?Pub _newline?>replace, or use <?Pub _newline?> item.</entry>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">4th position:<?Pub _newline?>Who can do<?Pub _newline?>complete repair<?Pub _newline?>on item.</entry>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">5th position:<?Pub _newline?>Who determines<?Pub _newline?>disposition action on<?Pub _newline?>unserviceable items.</entry>
                                <entry colsep="0" rowsep="0" valign="top"/>
                            </row>
                            <row>
                                <entry colsep="0" nameend="col6" namest="col1"/>
                            </row>
                        </tbody>
                    </tgroup>
                </table>
            </para>
            <?Pub _newpage?>
            <!-- added to move note from bottom of page july25  -->
            <note>
                <trim.para>Complete Repair: Maintenance capacity, capability, and authority to perform all corrective maintenance tasks of "Repair" function in a use/user environment in order to restore serviceability to a failed item.</trim.para>
            </note>
            <para>Source Code. Source code tells you how you get an item needed for maintenance, repair, or overhaul of an end item/equipment. Explanations of source codes follow:</para>
            <para>
                <table frame="none">
                    <title>Source Code Explanation</title>
                    <tgroup align="left" char=" " charoff="50" cols="4" colsep="0" rowsep="0">
                        <colspec colname="col1" colwidth="2*"/>
                        <colspec colname="col2" colwidth="8*"/>
                        <colspec colname="col3" colwidth="0.5*"/>
                        <colspec colname="col4" colwidth="14*"/>
                        <thead valign="top">
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="1" valign="bottom">Source Code</entry>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="1" valign="bottom">Application/Explanation</entry>
                            </row>
                        </thead>
                        <tbody valign="top">
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">PA</entry>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="9" rotate="no" rowsep="0">Stock items, use applicable NSN to requisition/request items with these source codes. They are authorized to level indicated by code entered in third position of SMR code.<note>
                                        <trim.para>Items coded PC are subject to deterioration.</trim.para>
                                    </note>
                                </entry>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">PB</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">PC</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">PD</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">PE</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">PF</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">PG</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">PH</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">PR</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">PZ</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry/>
                                <entry/>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">KD</entry>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="2" rotate="no" rowsep="0" valign="middle">Items with these codes are not to be requested/requisitioned individually. They are part of a kit that is authorized to maintenance level indicated in third position of SMR code. Complete kit must be requisitioned and applied.</entry>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">KF</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry align="left" morerows="0" rotate="no" rowsep="0" valign="middle">KB</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry rotate="no" rowsep="0" valign="middle"/>
                                <entry rotate="no"/>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">MF-Made at </entry>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="7" rotate="no" rowsep="0">Items with these codes are not to be requisitioned/requested individually. They must be made from bulk material which is identified by part number in DESCRIPTION AND USABLE ON CODE (UOC) entry and listed in bulk material group work package of Parts Information list. If item is authorized to you by third position code of SMR code, but source code indicates it is made at higher level, order item from higher level of maintenance.</entry>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">maintainer class</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">MH-Made at below </entry>
                                <entry/>
                            </row>
                            <row>
                                <entry rotate="no" valign="middle"/>
                                <entry rotate="no"valign="middle">depot sustainment</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">ML-Made at SRA</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry rotate="no" valign="middle"/>
                                <entry rotate="no" valign="middle">MD-Made at depot</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry rotate="no" valign="middle"/>
                                <entry rotate="no" valign="middle">MG-Navy only</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry rotate="no" rowsep="0" valign="middle"/>
                                <entry rotate="no"/>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">AF-Assembled by</entry>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="9" rotate="no" rowsep="0">Items with these codes are not to be requested/requisitioned individually. Parts that make up assembled item must be requisitioned or fabricated and assembled at level of maintenance indicated by source code. If third position of SMR code authorizes you to replace item, but source code indicates item is assembled at a higher level, order item from higher level of maintenance. </entry>
                            </row>
                            <row>
                                <entry rotate="no" valign="middle"/>
                                <entry rotate="no" valign="middle">maintainer class</entry>
                                <entry rotate="no" valign="middle"/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">AH-Assembled by </entry>
                                <entry/>
                            </row>
                            <row>
                                <entry rotate="no" valign="middle"/>
                                <entry rotate="no" valign="middle">below depot </entry>
                                <entry/>
                            </row>
                            <row>
                                <entry rotate="no" valign="middle"/>
                                <entry rotate="no" valign="middle">sustainment class</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry align="left" morerows="0" rotate="no" rowsep="0" valign="middle">AL-Assembled by </entry>
                                <entry/>
                            </row>
                            <row>
                                <entry rotate="no" valign="middle"/>
                                <entry rotate="no" valign="middle">SRA</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry align="left" morerows="0" rotate="no" rowsep="0" valign="middle">AD-Assembled by</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry rotate="no" valign="middle"/>
                                <entry rotate="no" valign="middle">depot</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">AG-Navy only</entry>
                                <entry/>
                            </row>
                            <row>
                                <entry rotate="no" valign="middle"/>
                                <entry rotate="no" valign="middle"/>
                                <entry rotate="no" valign="middle"/>
                                <entry rotate="no" valign="middle"/>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">XA</entry>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">Do not requisition an "XA" coded item. Order next higher assembly. (Refer to NOTE below.)</entry>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">XB</entry>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">If an item is not available from salvage, order it using CAGEC and P/N.</entry>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">XC</entry>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Installation drawings, diagrams, instruction sheets, field service drawings; identified by manufacturer&apos;s P/N. </entry>
                            </row>
                            <row>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">XD</entry>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Item is not stocked. Order an XD-coded item through local purchase or normal supply channels using CAGEC and P/N given, if no NSN is available. </entry>
                            </row>
                        </tbody>
                    </tgroup>
                </table>
            </para>
            <note>
                <trim.para>Cannibalization or controlled exchange, when authorized, may be used as a source of supply for items with above source codes except for those items source coded "XA" or those aircraft support items restricted by requirements of <extref docno="AR 750-1"/>.</trim.para>
            </note>
            <para>Maintenance Code. Maintenance code tell you level(s) of maintenance authorized to use and repair support items. Maintenance codes are entered in third and fourth positions of SMR code as follows: </para>
            <para>Third Position. Maintenance code entered in third position tells you lowest maintenance class authorized to remove, replace, and use an item. Maintenance code entered in third position will indicate authorization to following classes of maintenance:<table frame="none">
                    <tgroup align="left" char=" " charoff="50" cols="4">
                        <colspec colname="col0" colwidth="0.22*"/>
                        <colspec colname="col1" colwidth="1.00*"/>
                        <colspec colname="col2" colwidth="0.25*"/>
                        <colspec colname="col3" colwidth="4.03*"/>
                        <thead valign="bottom">
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="1" valign="bottom">Maintenance <?Pub _newline?>Code</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="1" valign="bottom">Application/Explanation</entry>
                            </row>
                        </thead>
                        <tbody valign="top">
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" rotate="no" rowsep="0" valign="middle">C -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry rotate="no" rowsep="0">Crew</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">F -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Maintainer maintenance can remove, replace, and use item.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">H -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Below Depot Sustainment maintenance can remove, replace, and use item.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">L -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Specialized repair activity can remove, replace, and use item.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">G -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Afloat and ashore intermediate maintenance can remove, replace, and use item. (Navy only).</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">K -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Contractor facility can remove, replace, and use item.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">Z -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Item is not authorized to be removed, replaced, or used at any maintenance level.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">D -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Depot can remove, replace, and use item.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry rotate="no" rowsep="0"/>
                            </row>
                        </tbody>
                    </tgroup>
                </table>
            </para>
            <note>
                <trim.para>Army will use C in third position. However, for joint service publications, other services may use O.</trim.para>
            </note>
            <para esd="no" hcp="no">Fourth Position. Maintenance code entered in fourth position tells you whether or not item is to be repaired and identifies lowest maintenance class with capability to do complete repair (perform all authorized repair functions).</para>
            <para>
                <table frame="none">
                    <tgroup align="left" char=" " charoff="50" cols="4">
                        <colspec colname="col0" colwidth="0.25*"/>
                        <colspec colname="col1" colwidth="1*"/>
                        <colspec colname="col2" colwidth="0.25*"/>
                        <colspec colname="col3" colwidth="4*"/>
                        <thead valign="bottom">
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="1" valign="bottom">Maintenance <?Pub _newline?>Code</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="1" valign="bottom">Application/Explanation</entry>
                            </row>
                        </thead>
                        <tbody valign="top">
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" rotate="no" rowsep="0" valign="middle">C -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry rotate="no" rowsep="0">Crew (operator) is lowest class that can do complete repair.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">F -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Maintainer is lowest class that can do complete repair of item.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">H -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Below Depot Sustainment is lowest class that can do complete repair of item.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">L -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Specialized repair activity is lowest class that can do complete repair of item</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" rotate="no" rowsep="0" valign="middle">D -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" rotate="no" rowsep="0">Depot is lowest class that can do complete repair of item.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">G -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Both afloat and ashore intermediate levels are capable of complete repair of item. (Navy only)</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">K -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Complete repair is done at contractor facility.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">Z -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Nonrepairable. No repair is authorized.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="middle">B -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">No repair is authorized. No parts or special tools are authorized for maintenance of "B" coded item. However, item may be reconditioned by adjusting, lubricating, etc., at user level.</entry>
                            </row>
                        </tbody>
                    </tgroup>
                </table>
            </para>
            <?Pub _newpage?>
            <para esd="no" hcp="no">Recoverability Code. Recoverability codes are assigned to items to indicate disposition action on unserviceable items. Recoverability code is shown in fifth position of SMR code as follows:<table frame="none">
                    <tgroup align="left" char=" " charoff="50" cols="4">
                        <colspec colname="col0" colwidth="0.25*"/>
                        <colspec colname="col1" colwidth="1*"/>
                        <colspec colname="col2" colwidth="0.25*"/>
                        <colspec colname="col3" colwidth="4*"/>
                        <thead valign="bottom">
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="1" valign="bottom">Recoverability<?Pub _newline?>Code</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="1" valign="bottom">Application/Explanation</entry>
                            </row>
                        </thead>
                        <tbody valign="top">
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Z - </entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Nonrepairable item. When unserviceable, condemn and dispose of item at level of maintenance shown in third position of SMR code.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">F -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Reparable item. When uneconomically reparable, condemn and dispose of item at field level.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">H -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Reparable item. When uneconomically reparable, condemn and dispose of item at below depot sustainment.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" rotate="no" rowsep="0">D -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" rotate="no" rowsep="0">Reparable item. When beyond lower level repair capability, return to depot. Condemnation and disposal of item are not authorized below depot.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">L -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Reparable item. Condemnation and disposal not authorized below Specialized Repair Activity (SRA).</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">A -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Item requires special handling or condemnation procedures because of specific reasons (such as precious metal content, high dollar value, critical material, or hazardous material). Refer to appropriate manuals/directives for specific instructions.</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">G -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Field level reparable item. Condemn and dispose at either afloat or ashore intermediate levels. (Navy only)</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">K -</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">Reparable item. Condemnation and disposal to be performed at contractor facility.</entry>
                            </row>
                        </tbody>
                    </tgroup>
                </table>
            </para>
            <para>NSN (Column (3)). NSN(s) for item is listed in this column.</para>
            <para>CAGEC (Column (4)). Commercial and Government Entity Code (CAGEC) is a five-digit code which is used to identify manufacturer, distributor, or Government agency/activity that supplies item.</para>
            <para>PART NUMBER (Column (5)). Indicates primary number used by manufacturer (individual, company, firm, corporation, or Government activity), which controls design and characteristics of item by means of its engineering drawings, specifications, standards, and inspection requirements to identify an item or range of items.</para>
            <note>
                <trim.para>When you use an NSN to requisition an item, item you receive may have a different part number from number listed.</trim.para>
            </note>
            <para>DESCRIPTION AND USABLE ON CODE (UOC) (Column (6)). This column includes following information:<seqlist>
                    <item>Federal item name, and when required, a minimum description to identify item.</item>
                    <item>Part numbers of any bulk materials required if item is to be locally manufactured or fabricated.</item>
                    <item>Hardness Critical Item (HCI). Items that require special handling or procedures to ensure protection against electromagnetic pulse (EMP) damage are marked with letters &lsquo;HCI.&rsquo;</item>
                    <item>Statement END OF FIGURE appears below last item description in column (6) for each Figure in repair parts list, special tools repair parts, kits, bulk items, and special tools list work packages.</item>
                    <item>Refer to Usable on Code details presented later in this work package under SPECIAL INFORMATION.</item>
                </seqlist>
            </para>
            <para>QTY (Column (7)). QTY (quantity per Figure) column indicates quantity of item used in breakout shown on illustration/Figure. A "V" appearing in this column instead of a quantity indicates that quantity is variable and quantity may change from application to application.</para>
        </para0>
        <?Pub _newpage?>
        <para0>
            <title>EXPLANATION OF CROSS-REFERENCE INDEXES WORK PACKAGES FORMAT AND COLUMNS</title>
            <para>
                <seqlist>
                    <item>National Stock Number (NSN) Index Work Package. NSN&apos;s in this index are listed in National Item Identification Number (NIIN) sequence. <randlist bullet="no">
                            <item>STOCK NUMBER Column. This column lists NSN in NIIN sequence. NIIN consists of last nine digits of NSN. When using this column to locate an item, ignore first four digits of NSN. However, complete NSN should be used when ordering items by stock number.</item>
                            <item>For example, if NSN is 5385-01-574-1476, NIIN is 01-574-1476.</item>
                            <item>FIG. Column. This column lists number of Figure where item is identified/located. Figures are in numerical order in repair parts list and special tools list work packages. </item>
                            <item>ITEM Column. Item number identifies item associated with Figure listed in adjacent FIG. column. This item is also identified by NSN listed on same line.</item>
                        </randlist>
                    </item>
                    <item>Part Number (P/N) Index Work Package. P/Ns in this index are listed in ascending alphanumeric sequence (vertical arrangement of letter and number combinations which places first letter or digit of each group in order A through Z, followed by numbers 0 through 9 and each following letter or digit in like order.)<randlist bullet="no">
                            <item>PART NUMBER Column. Indicates P/N assigned to item.</item>
                            <item>FIG. Column. This column lists number of Figure where item is identified/located in repair parts list and special tools list work packages.</item>
                            <item>ITEM Column. Item number is number assigned to item as it appears in figure referenced in adjacent Figure number column.</item>
                        </randlist>
                    </item>
                </seqlist>
            </para>
        </para0>
        <para0>
            <title>SPECIAL INFORMATION</title>
            <para> UOC appears in lower left corner of Description Column heading. Usable on codes are shown as "UOC:" in Description Column (justified left) on first line under applicable item/nomenclature. Uncoded items are applicable to all models. Examples of UOCs used in this Parts Information list are:<table frame="none">
                    <tgroup align="left" char=" " charoff="50" cols="4">
                        <colspec colname="col0" colwidth="0.25*"/>
                        <colspec colname="col1" colwidth="1*"/>
                        <colspec colname="col2" colwidth="0.25*"/>
                        <colspec colname="col3" colwidth="4*"/>
                        <thead valign="bottom">
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="1" valign="bottom">Code</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="1" valign="bottom">Used On</entry>
                            </row>
                        </thead>
                        <!-- ADD EACH UOC TYPE IN THIS AREA  -->
                        <tbody valign="top">
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">KAE</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">{self.sys_name} ({self.sys_acronym}), GREEN</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">KAF</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">{self.sys_name} ({self.sys_acronym}), TAN</entry>
                            </row>
                        </tbody>
                    </tgroup>
                </table>
            </para>
            <para>Fabrication Instructions. Bulk materials required to manufacture items are listed in bulk material functional group of this Parts Information list. Part numbers for bulk material are also referenced in Description Column of line item entry for item to be manufactured/fabricated. Detailed fabrication instructions for items source coded to be manufactured or fabricated are found in this manual <xref wpid="R00001-10-7360-233"/>.</para>
            <para>Index Numbers. Items which have word BULK in figure column will have an index number shown in item number column. This index number is a cross-reference between NSN / P/N index work packages and bulk material list in repair parts list work package.</para>
        </para0>
        <para0>
            <title/>
            <!-- ADD TM TILE HERE  -->
            <para>Associated Publications. Publication(s) listed below pertain to (SYSTEM NAME):
                <table frame="none">
                    <tgroup align="left" char=" " charoff="50" cols="4">
                        <colspec colname="col0" colwidth="0.1*"/>
                        <colspec colname="col1" colwidth="1.5*"/>
                        <colspec colname="col2" colwidth="0.1*"/>
                        <colspec colname="col3" colwidth="4*"/>
                        <thead valign="bottom">
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="1" valign="bottom">Publication</entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="1" valign="bottom">Short Title</entry>
                            </row>
                        </thead>
                        <tbody valign="top">                          
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">
                                    <extref docno="TM 10-5430-237-12&amp;P"/>
                                </entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">OPERATOR`S AND UNIT MAINTENANCE MANUAL (INCLUDING REPAIR PARTS AND SPECIAL TOOLS LIST) FOR TANK, FABRIC, COLLAPSIBLE</entry>
                            </row>                           
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">
                                    <extref docno="TM 55-8145-236-13&amp;P"/>
                                </entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">OPERATOR, UNIT, AND DIRECT SUPPORT MAINTENANCE (INCLUDING REPAIR PARTS AND SPECIAL TOOLS LIST) TRIPLE (TRICON) CONTAINER TYPES 1 AND 2</entry>
                            </row>
                            <row>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">
                                    <extref docno="TM 10-7310-283-23&amp;P"/>
                                </entry>
                                <entry colsep="0" rotate="no" rowsep="0"/>
                                <entry colsep="0" morerows="0" rotate="no" rowsep="0" valign="top">FIELD MAINTENANCE MANUAL (INCLUDING REPAIR PARTS AND SPECIAL TOOLS LIST) FOR BURNER, MULTI-FUEL, MODULAR</entry>
                            </row>
                        </tbody>
                    </tgroup>
                </table>
            </para>
        </para0>
        <?Pub _newpage?>
        <para0>
            <title>HOW TO LOCATE REPAIR PARTS</title>
            <para>
                <seqlist>
                    <item>When NSNs or Part Numbers Are Not Known.<randlist bullet="no">
                            <item>First. Using table of contents, determine assembly group to which item belongs. This is necessary since Figures are prepared for assembly groups and subassembly groups, and lists are divided into same groups.</item>
                            <item>Second. Find Figure covering functional group or sub functional group to which item belongs.</item>
                            <item>Third. Identify item on figure and note number(s).</item>
                            <item>Fourth. Look in repair parts list work packages for Figure and item numbers. NSNs and part numbers are on same line as associated item numbers.</item>
                        </randlist>
                    </item>
                    <item>When NSN Is Known.<randlist bullet="no">
                            <item>First. If you have NSN, look in STOCK NUMBER column of NSN index work package. NSN is arranged in NIIN sequence. Note Figure and item number next to NSN.</item>
                            <item>Second. Turn to Figure and locate item number. Verify that item is one you are looking for.</item>
                        </randlist>
                    </item>
                    <item>When Part Number Is Known.<randlist bullet="no">
                            <item>First. If you have P/N and not NSN, look in PART NUMBER column of P/N index work package. Identify Figure and item number.</item>
                            <item>Second. Look up item on Figure in applicable repair parts list work package.</item>
                        </randlist>
                    </item>
                </seqlist>
            </para>
        </para0>
    </introwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-R00001-PartsInfo-Introduction.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def plwp(self, wpno, wp_title):
        """ Function to create list of parts for a subsystem WP. """
        tmp = f'<plwp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += f'''<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>{wp_title}</title>
        </wpidinfo>
        <pi.category>
            <figure id="MXXXXX-XX-XXXX-XXX-FXXXX">
                <title>Lorem Ipsum</title>
                <subfig sheet="1" totalsheets="X">
                    <graphic boardno="PLACEHOLDER"/>
                </subfig>
                <subfig sheet="2" totalsheets="X">
                    <graphic boardno="PLACEHOLDER"/>
                </subfig>
                <subfig sheet="3" totalsheets="X">
                    <graphic boardno="PLACEHOLDER"/>
                </subfig>
            </figure>
            <fncgrp>
                <fnccode>XXXXX</fnccode>
                <fnctitle>Lorem Ipsum</fnctitle>
            </fncgrp>
            <pi.item id="XX-XXXX-XXX" indent="0">
                <callout assocfig="MXXXXX-XX-XXXX-XXX-FXXXX" label="1"/>
                <qty>X</qty>
                <smr sourcecode="PA" maintcode="FD" recovercode="D"/>
                <nsn>
                    <fsc>XXXXX</fsc>
                    <niin>XXXXX</niin>
                </nsn>
                <partno></partno>
                <cageno></cageno>
                <name>XXXXXXXXXX</name>
                <desc>XXXXXXXXXXXXXXXXXXXX</desc>
            </pi.item>
            <pi.item id="XX-XXXX-XXX" indent="0">
                <callout assocfig="MXXXXX-XX-XXXX-XXX-FXXXX" label="1"/>
                <qty>X</qty>
                <smr sourcecode="PA" maintcode="FD" recovercode="D"/>
                <nsn>
                    <fsc>XXXXX</fsc>
                    <niin>XXXXX</niin>
                </nsn>
                <partno>XXXXX</partno>
                <cageno>XXXXX</cageno>
                <name>XXXXXXXXXX</name>
                <desc>XXXXXXXXXXXXXXXXXXXX</desc>
            </pi.item>
        </pi.category>
    </plwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{} {}.txt'.format(cfg.prefix_file, wpno, wp_title), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def bulk_itemswp(self, wpno):
        """ Function to create Bulk Items List WP. """
        tmp = f'<bulk_itemswp chngno="0" wpno="{wpno}-' + self.sys_number + '">\n'
        tmp += '''<wpidinfo>
            <maintlvl level="maintainer"/>
            <title id="X">BULK ITEMS</title>
        </wpidinfo>
        <fncgrp>
            <fnccode></fnccode>
            <fnctitle id="X">BULK MATERIAL</fnctitle>
        </fncgrp>
        <pi.item id="BIL_1" indent="0">
        <callout assocfig="XXXXXX-XX-XXXX-XXX-XXXXX" label="1"/>
        <qty></qty>
        <smr sourcecode="PA" maintcode="FD" recovercode="X"/>
        <nsn>
            <fsc></fsc>
            <niin/>
        </nsn>
        <partno></partno>
        <cageno></cageno>
        <name></name>
        <desc></desc>
    </pi.item>
    <pi.item id="BIL_2" indent="0">
        <callout assocfig="XXXXXX-XX-XXXX-XXX-XXXXX" label="2"/>
        <qty></qty>
        <smr sourcecode="PA" maintcode="FD" recovercode="D"/>
        <nsn>
            <fsc></fsc>
            <niin/>
        </nsn>
        <partno></partno>
        <cageno></cageno>
        <name></name>
        <desc></desc>
    </pi.item>
    <pi.item id="BIL_3" indent="0">
        <callout assocfig="XXXXXX-XX-XXXX-XXX-XXXXX" label="1"/>
        <qty></qty>
        <smr sourcecode="PA" maintcode="FD" recovercode="D"/>
        <nsn>
            <fsc></fsc>
            <niin/>
        </nsn>
        <partno></partno>
        <cageno></cageno>
        <name></name>
        <desc></desc>
    </pi.item>
    <pi.item id="BIL_4" indent="0">
        <callout assocfig="XXXXXX-XX-XXXX-XXX-XXXXX" label="2"/>
        <qty></qty>
        <smr sourcecode="PA" maintcode="FD" recovercode="D"/>
        <nsn>
            <fsc></fsc>
            <niin/>
        </nsn>
        <partno></partno>
        <cageno></cageno>
        <name></name>
        <desc></desc>
    </pi.item>
    <pi.item id="BIL_5" indent="0">
        <callout assocfig="XXXXXX-XX-XXXX-XXX-XXXXX" label="3"/>
        <qty></qty>
        <smr sourcecode="PA" maintcode="FD" recovercode="D"/>
        <nsn>
            <fsc></fsc>
            <niin/>
        </nsn>
        <partno></partno>
        <cageno></cageno>
        <name></name>
        <desc></desc>
    </pi.item>
    </bulk_itemswp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-BulkItems.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def nsnindxwp(self, wpno):
        """ Function to create NSN Index WP. """
        tmp = f'<nsnindxwp wpno="{wpno}-' + self.sys_number + '" chngno="0">\n'
        tmp += '''<?Pub Dtl?>
        <wpidinfo>
            <maintlvl level="maintainer" />
            <title>NATIONAL STOCK NUMBER INDEX</title>
        </wpidinfo>
        <nsnindx>
            <nsnindxrow>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <callout assocfig="XXXXXX-XX-XXXX-XXX-F0001" label="1"/>
        </nsnindxrow>
        <nsnindxrow>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <callout assocfig="XXXXXX-XX-XXXX-XXX-F0002" label="1"/>
        </nsnindxrow>
        <nsnindxrow>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <callout assocfig="XXXXXX-XX-XXXX-XXX-F0003" label="1"/>
        </nsnindxrow>
        <nsnindxrow>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <callout assocfig="XXXXXX-XX-XXXX-XXX-F0004" label="1"/>
        </nsnindxrow>
        <nsnindxrow>
            <nsn>
                <fsc></fsc>
                <niin></niin>
            </nsn>
            <callout assocfig="XXXXXX-XX-XXXX-XXX-F0005" label="1"/>
        </nsnindxrow>
        </nsnindx>
    </nsnindxwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-NSNIndex.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def pnindxwp(self, wpno):
        """ Function to create Part Number WP. """
        tmp = f'<pnindxwp wpno="{wpno}-' + self.sys_number + '" chngno="0">\n'
        tmp += '''<wpidinfo>
            <maintlvl level="maintainer" />
            <title>PART NUMBER INDEX</title>
        </wpidinfo>
        <pnindx>
            <pnindxrow>
            <partno></partno>
            <cageno></cageno>
            <callout assocfig="XXXXXX-XX-XXXX-XXX-F0001" label="1"/>
        </pnindxrow>
        <pnindxrow>
            <partno></partno>
            <cageno></cageno>
            <callout assocfig="XXXXXX-XX-XXXX-XXX-F0002" label="1"/>
        </pnindxrow>
        <pnindxrow>
            <partno></partno>
            <cageno></cageno>
            <callout assocfig="XXXXXX-XX-XXXX-XXX-F0003" label="1"/>
        </pnindxrow>
        <pnindxrow>
            <partno></partno>
            <cageno></cageno>
            <callout assocfig="XXXXXX-XX-XXXX-XXX-F0004" label="1"/>
        </pnindxrow>
        <pnindxrow>
            <partno></partno>
            <cageno></cageno>
            <callout assocfig="XXXXXX-XX-XXXX-XXX-F0005" label="1"/>
        </pnindxrow>
        <pnindxrow>
            <partno></partno>
            <cageno></cageno>
            <callout assocfig="XXXXXX-XX-XXXX-XXX-F0006" label="1"/>
        </pnindxrow>
        </pnindx>
    </pnindxwp>'''
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-{}-PartNumberIndex.txt'.format(cfg.prefix_file, wpno), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 10
        
    def end(self):
        """ Function to create Parts Information list section end tags """
        cfg.prefix_file = (math.ceil(cfg.prefix_file/1000) * 1000) - 1
        tmp = '</pim>'
        with open(self.save_path + '/' + self.sys_acronym + ' ' + self.manual_type +
                ' WIP/{:05d}-PARTS_INFO_END.txt'.format(cfg.prefix_file), 'w', encoding='UTF-8') as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
