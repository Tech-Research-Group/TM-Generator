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

    def start(self) -> None:
        """Function that creates the Shipment/Movement and Storage Maintenance
        Instructions chapter header of TM."""
        # cfg.prefix_file = math.floor(cfg.prefix_file / 1000) * 1000
        tmp = '<?xml version="1.0" encoding="UTF-8"?>\n'
        tmp += '<mim revno="0" chngno="0" chap-toc="no">\n'
        tmp += '\t\t<titlepg maintlvl="operator">\n'
        tmp += (
            "\t\t\t<name>" + self.sys_name + " (" + self.sys_acronym + ")" + "</name>\n"
        )
        tmp += "\t\t</titlepg>\n"
        tmp += "\t\t<shipmentmovementstoragecategory>\n"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-SHIPPING/STORAGE_START.xml".format(cfg.prefix_file),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def prepstore(self) -> None:
        """Function to create Shipment/Movement and Storage Maintenance
        Instructions chapter prepstore WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE prepstore PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE prepstore PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE prepstore PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += '<maintwp chngno="0" wpno="M00601-' + self.tmno + '" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("prepstore", self.tmno)

        tmp += """\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>PREPARATION FOR STORAGE</title>
        </wpidinfo>\n"""
        tmp += isb.show()
        tmp += "\t<maintsk>\n"
        tmp += "\t\t<prepstore>\n"
        tmp += proc.show()
        tmp += "\t\t</prepstore>\n"
        tmp += "\t</maintsk>\n"
        tmp += followon_maintsk.show()
        tmp += "</maintwp>"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-M00601-Prep For Storage.xml".format(cfg.prefix_file),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def prepship(self) -> None:
        """Function to create Shipment/Movement and Storage Maintenance
        Instructions chapter prepship WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE prepship PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE prepship PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE prepship PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += '<maintwp chngno="0" wpno="M00602-' + self.tmno + '" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("maintwp", self.tmno)

        tmp += """\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>PREPARATION FOR SHIPPING</title>
        </wpidinfo>\n"""
        tmp += isb.show()
        tmp += "\t<maintsk>\n"
        tmp += "\t\t<prepship>\n"
        tmp += proc.show()
        tmp += "\t\t</prepship>\n"
        tmp += "\t</maintsk>\n"
        tmp += followon_maintsk.show()
        tmp += "</maintwp>"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-M00602-Prep For Shipment.xml".format(cfg.prefix_file),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def transport(self) -> None:
        """Function to create Shipment/Movement and Storage Maintenance
        Instructions chapter transport WP."""
        tmp: str = '<?xml version="1.0" encoding="UTF-8"?>\n'
        if self.mil_std == "2C":
            tmp += f'<!DOCTYPE transport PUBLIC "{self.FPI_2C}" "../dtd/40051C_6_5.dtd" [\n]>\n'
        elif self.mil_std == "2D":
            tmp += f'<!DOCTYPE transport PUBLIC "{self.FPI_2D}" "../dtd/40051D_7_0.dtd" [\n]>\n'
        elif self.mil_std == "E":
            tmp += f'<!DOCTYPE transport PUBLIC "{self.FPI_E}" "../dtd/40051E_8_0.dtd" [\n]>\n'
        tmp += '<maintwp chngno="0" wpno="M00603-' + self.tmno + '" security="cui">\n'

        # WP.METADATA Section
        tmp += md.show("maintwp", self.tmno)

        tmp += """\t<wpidinfo>
            <maintlvl level="maintainer"/>
            <title>TRANSPORT</title>
        </wpidinfo>\n"""
        tmp += isb.show()
        tmp += "\t<maintsk>\n"
        tmp += "\t\t<transport>\n"
        tmp += proc.show()
        tmp += "\t\t</transport>\n"
        tmp += "\t</maintsk>\n"
        tmp += followon_maintsk.show()
        tmp += "</maintwp>"
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-M00603-Transport.xml".format(cfg.prefix_file),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 10

    def end(self) -> None:
        """Function to create Shipment/Movement and Storage Maintenance
        Instructions chapter end tags."""
        tmp = "</mim>"
        cfg.prefix_file = (math.ceil(cfg.prefix_file / 1000) * 1000) - 1
        with open(
            self.save_path
            + "/"
            + self.sys_acronym
            + " "
            + self.manual_type
            + " IADS/files/{:05d}-SHIPPING/STORAGE_END.xml".format(cfg.prefix_file),
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
        cfg.prefix_file += 1
