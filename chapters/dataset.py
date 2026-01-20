###DATASET FILE###

import datetime


class DataSet:
    """Class to create a dataset.xml file for Arbortext."""

    date: str = datetime.datetime.today().strftime("%d %B %Y").upper()
    FPI_2C = "-//USA-DOD//DTD -1/2C TM Assembly REV C 6.5 20200930//EN"
    FPI_2D = "-//USA-DOD//DTD -1/2D TM Assembly REV D 7.0 20220130//EN"
    FPI_E = "-//USA-DOD//DTD -E TM Assembly REV E 8.0 20250417//EN"

    def __init__(self, manual_type, sys_acronym, sys_name, tmno, save_path) -> None:
        self.manual_type = manual_type
        self.sys_acronym = sys_acronym
        self.sys_name = sys_name
        self.tmno = tmno
        self.save_path = save_path

    def build_dataset(self) -> None:
        """Function to build the dataset.xml for the IADS project."""
        tmp = f"""<?xml version="1.0" encoding="UTF-8"?>
<Dataset xmlns:xsd="http://www.w3.org/2001/XMLSchema"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Weapsys>{self.sys_name}</Weapsys>
	<Id>TM {self.tmno}</Id>
	<PubDate>{self.date}</PubDate>
	<Revision>0</Revision>
	<Distribution></Distribution>
	<!-- <DtdDirPath>./dtd</DtdDirPath> -->
	<TocFilepath>toc.xml</TocFilepath>
	<Description>{self.sys_name}</Description>
	<Image></Image>
	<Watermark></Watermark>
	<PMCSLogging>
		<SubmitMode>IADS</SubmitMode>
	</PMCSLogging>
	<!--<ConfigurationGroups>
		<ConfigurationGroup Name="TYPE" Image="">
			<Configuration Label="" Applicable="" Description=""/>
			<Configuration Label="" Applicable="" Description=""/>
		</ConfigurationGroup>
	</ConfigurationGroups>-->
</Dataset>"""

        with open(
            f"{self.save_path}/{self.sys_acronym} {self.manual_type} IADS/dataset.xml",
            "w",
            encoding="UTF-8",
        ) as _f:
            _f.write(tmp)
