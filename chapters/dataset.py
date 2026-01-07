###DATASET FILE###

import datetime


class DataSet:
    """Class to create a dataset.xml file for Arbortext."""

    date: str = datetime.datetime.today().strftime("%d %B %Y").upper()
    FPI_2C = "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN"
    FPI_2D = "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN"
    FPI_E = "-//USA-DOD//DTD -E TM Assembly REV E 8.0 20250417//EN"

    def __init__(self, manual_type, sys_acronym, save_path) -> None:
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.save_path = save_path

    def buildDataSet(self) -> None:
        """Function to build the dataset.xml for the IADS project."""
        tmp = """<?xml version="1.0" encoding="UTF-8"?>
<Dataset xmlns:xsd="http://www.w3.org/2001/XMLSchema"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Weapsys></Weapsys>
	<Id></Id>
	<PubDate></PubDate>
	<Revision></Revision>
	<Distribution></Distribution>
	<!-- <DtdDirPath>./dtd</DtdDirPath> -->
	<TocFilepath>TOC.xml</TocFilepath>
	<Description></Description>
	<Image></Image>
	<Watermark></Watermark>
	<PMCSLogging>
		<SubmitMode>IADS</SubmitMode>
	</PMCSLogging>
	<ConfigurationGroups>
		<ConfigurationGroup Name="TYPE" Image="">
			<Configuration Label="" Applicable="" Description=""/>
			<Configuration Label="" Applicable="" Description=""/>
		</ConfigurationGroup>
	</ConfigurationGroups>
</Dataset>"""

        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/dataset.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
