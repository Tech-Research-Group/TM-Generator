"""SHIPMENT/MOVEMENT AND STORAGE MAINTENANCE INSTRUCTIONS"""

import datetime
import math

import cfg
import views.followon_maintsk as followon_maintsk
import views.isb as isb
import views.metadata as md
import views.proc as proc


class ShipmentInstructions:
    """Class to create various types of WP's included in the Shipment/Movement and Storage
    Maintenance Instructions chapter of a TM."""

    date: str = datetime.datetime.today().strftime("%d %B %Y").upper()
    FPI_2C = "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN"
    FPI_2D = "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN"
    FPI_E = "-//USA-DOD//DTD -E TM Assembly REV E 8.0 20250417//EN"

    def __init__(
        self, manual_type, mil_std, sys_acronym, sys_name, tmno, save_path
    ) -> None:
        self.manual_type = manual_type
        self.mil_std = mil_std
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.tmno = tmno
        self.save_path = save_path

    def maintenance_level(self) -> str:
        """Function to find maintenance level for a chapter or work package"""
        if self.manual_type == "-10":
            level = "operator"
        elif self.manual_type == "NMWR":
            level = "depot"
        else:
            level = "maintainer"
        return level

    def start(self) -> None:
        """Function that creates the Shipment/Movement and Storage Maintenance
        Instructions chapter header of TM."""
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += '<mim revno="0" chngno="0" chap-toc="no">\n'
        tmp += f'\t<titlepg maintlvl="{self.maintenance_level()}">\n'
        tmp += (
            "\t\t\t<name>" + self.sys_name + " (" + self.sys_acronym + ")" + "</name>\n"
        )
        tmp += "\t\t</titlepg>\n"
        tmp += "\t\t<shipmentmovementstoragecategory>\n"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-SHIPPING_INSTRUCTIONS_START.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def prepstore(self, wpno) -> None:
        """Function to create Shipment/Movement and Storage Maintenance
        Instructions chapter prepstore WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE prepstore PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE prepstore PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE prepstore PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<maintwp chngno="0" wpno="{wpno}-' + self.tmno + '" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += """\t\t<title>PREPARATION FOR STORAGE</title>
        </wpidinfo>\n"""
        tmp += isb.show()
        tmp += "\t<maintsk>\n"
        tmp += "\t\t<prepstore>\n"
        tmp += proc.show()
        tmp += "\t\t</prepstore>\n"
        tmp += "\t</maintsk>\n"
        tmp += followon_maintsk.show()
        tmp += "</maintwp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Preparation For Storage.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.shipment_instructions.append(file_name)
        cfg.prefix_file += 10

    def prepship(self, wpno) -> None:
        """Function to create Shipment/Movement and Storage Maintenance
        Instructions chapter prepship WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE prepship PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE prepship PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE prepship PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<maintwp chngno="0" wpno="{wpno}-' + self.tmno + '" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += """\t\t<title>PREPARATION FOR SHIPPING</title>
        </wpidinfo>\n"""
        tmp += isb.show()
        tmp += "\t<maintsk>\n"
        tmp += "\t\t<prepship>\n"
        tmp += proc.show()
        tmp += "\t\t</prepship>\n"
        tmp += "\t</maintsk>\n"
        tmp += followon_maintsk.show()
        tmp += "</maintwp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Preparation For Shipment.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.shipment_instructions.append(file_name)
        cfg.prefix_file += 10

    def transport(self, wpno) -> None:
        """Function to create Shipment/Movement and Storage Maintenance
        Instructions chapter transport WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE transport PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE transport PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE transport PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += f'<maintwp chngno="0" wpno="{wpno}-' + self.tmno + '" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show(wpno, self.tmno)

        tmp += "\t<wpidinfo>\n"
        tmp += f'\t\t<maintlvl level="{self.maintenance_level()}"/>\n'
        tmp += """\t\t<title>TRANSPORT</title>
        </wpidinfo>\n"""
        tmp += isb.show()
        tmp += "\t<maintsk>\n"
        tmp += "\t\t<transport>\n"
        tmp += proc.show()
        tmp += "\t\t</transport>\n"
        tmp += "\t</maintsk>\n"
        tmp += followon_maintsk.show()
        tmp += "</maintwp>"
        file_name = f"{cfg.prefix_file:05d}-{wpno}-Transport.xml"
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{file_name}",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.shipment_instructions.append(file_name)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create Shipment/Movement and Storage Maintenance
        Instructions chapter end tags."""
        tmp = "</mim>"
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/files/{cfg.prefix_file:05d}-SHIPPING_INSTRUCTIONS_END.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
