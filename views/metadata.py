"""WP.METADATA"""

import datetime

date: str = datetime.datetime.today().strftime("%d %B %Y").upper()


def show(wpid, tmno) -> str:
    """Function to create the <wp.metadata> section of the work package."""
    return f"""\n\t<wp.metadata>
        <portionmark country="US" security="cui"/>
        <proponent>
            <name>US Army Communications-Electronics Command</name>
            <address>
                <street>6585 Surveillance Loop, Building 6002</street>
                <city>Aberdeen Proving Ground</city>
                <state>Maryland</state>
                <zip>21005</zip>
                <country>United States of America</country>
                <phone type="coml">443-861-6719 x0732</phone>
                <phone type="dsn">848-6719 x0732</phone>
                <internet>
                    <homepage protocol="https" uri="cecom.army.mil/"/>
                </internet>
            </address>
        </proponent>
        <tracking>
            <change.history id="{wpid}-CHNG0">
                <author>
                    <name></name>
                    <proponent>
                        <name>Tech Services Group Inc DBA Tech Research Group</name>
                        <address>
                            <street>144 Metro Center Blvd, Unit D</street>
                            <city>Warwick</city>
                            <state>Rhode Island</state>
                            <zip>02886</zip>
                            <country>United States of America</country>
                            <phone type="coml">401-921-0391</phone>
                            <internet>
                                <homepage protocol="http" uri="www.techresearchgroup.com/"/>
                            </internet>
                        </address>
                    </proponent>
                </author>
                <date>{date}</date>
                <wp.status type="draft"/>
                <reason>Initial Draft</reason>
                <qualityassurance>
                    <unverified/>
                </qualityassurance>
            </change.history>
        </tracking>
        <tminfono>
            <servbranch service="army" procuring="yes"/>
            <tmno>{tmno}</tmno>
        </tminfono>
        <applicability></applicability>
    </wp.metadata>\n"""
