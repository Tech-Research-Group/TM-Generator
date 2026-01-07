###TOC FILE###

import datetime


class TOC:
    """Class to create a toc.xml file for Arbortext."""

    date: str = datetime.datetime.today().strftime("%d %B %Y").upper()
    FPI_2C = "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN"
    FPI_2D = "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN"
    FPI_E = "-//USA-DOD//DTD -E TM Assembly REV E 8.0 20250417//EN"

    def __init__(self, manual_type, sys_acronym, save_path) -> None:
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.save_path = save_path

    def buildTOC(self) -> None:
        """Function to build the TOC.xml for the IADS project."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<toc xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<tocEntry title="FRONT MATTER">
		<tocEntry filename="files/"/>
		<tocEntry filename="files/" title="WARNING SUMMARY"/>
		<tocEntry filename="files/" title="LIST OF EFFECTIVE PAGES/WORK PACKAGES"/>
		<tocEntry filename="files/" title="TITLE BLOCK"/>
		<tocEntry filename="files/" title="HOW TO USE THIS MANUAL"/>
	</tocEntry>
	<tocEntry title="GENERAL INFORMATION">
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
	</tocEntry>
	<tocEntry title="OPERATOR INSTRUCTIONS">
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
	</tocEntry>
	<tocEntry title="OPERATOR TROUBLESHOOTING">
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
	</tocEntry>
	<tocEntry title="OPERATOR PREVENTIVE MAINTENANCE CHECKS AND SERVICES">
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
	</tocEntry>
	<tocEntry title="OPERATOR MAINTENANCE">
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
	</tocEntry>
	<tocEntry title="MAINTAINER TROUBLESHOOTING">
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
	</tocEntry>
	<tocEntry title="MAINTAINER PREVENTIVE MAINTENANCE CHECKS AND SERVICES">
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
	</tocEntry>
	<tocEntry title="MAINTAINER MAINTENANCE">
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
	</tocEntry>
	<tocEntry title="AUXILIARY EQUIPMENT MAINTENANCE">
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
	</tocEntry>
	<tocEntry title="DESTRUCTION OF EQUIPMENT TO PREVENT ENEMY USE">
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
	</tocEntry>
	<tocEntry title="REPAIR PARTS AND SPECIAL TOOLS LIST">
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
	</tocEntry>
	<tocEntry title="SUPPORTING INFORMATION">
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
		<tocEntry filename="files/"/>
	</tocEntry>
	<tocEntry title="REAR MATTER">
		<tocEntry filename="files/"/>
	</tocEntry>
</toc>"""

        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/toc.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
