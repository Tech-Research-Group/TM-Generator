"""INITIAL SETUP BOX"""

def show():
    """Function to create the Initial Setup Box."""
    return '''\t<initial_setup>
        <testeqp>
            <testeqp-setup-item>
                <name></name>
                <itemref>
                    <xref itemid="" wpid=""/>
                </itemref>
            </testeqp-setup-item>
        </testeqp>
        <tools>
            <tools-setup-item>
                <name></name>
                <itemref>
                    <xref itemid="" wpid=""/>
                </itemref>
            </tools-setup-item>
        </tools>
        <spectools>
            <spectools-setup-item>
                <name></name>
            </spectools-setup-item>
        </spectools>
        <mtrlpart>
            <mtrlpart-setup-item>
                <name></name>
                <qty></qty>
                <itemref>
                    <xref itemid="" wpid=""/>
                </itemref>
            </mtrlpart-setup-item>
        </mtrlpart>
        <mrp>
            <mrp-setup-item>
                <name></name>
                <qty></qty>
                <itemref>
                    <xref itemid="" wpid=""/>
                </itemref>
            </mrp-setup-item>
        </mrp>
        <persnreq>
            <persnreq-setup-item>
                <name></name>
            </persnreq-setup-item>
        </persnreq>
        <ref>
            <ref-setup-item>
                <xref wpid=""/>
            </ref-setup-item>
        </ref>
        <eqpconds>
            <eqpconds-setup-item>
                <condition></condition>
                <itemref>
                    <xref wpid=""/>
                </itemref>
            </eqpconds-setup-item>
        </eqpconds>
    </initial_setup>\n'''
