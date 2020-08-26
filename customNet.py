#!/usr/bin/env python

"""
"""
from mininet.topo import Topo

class Lab( Topo ):
    "Internet Topology Zoo Specimen."

    def addSwitch( self, name, **opts ):
        kwargs = { 'protocols' : 'OpenFlow13' }
        kwargs.update( opts )
        return super(Lab, self).addSwitch( name, **kwargs )

    def __init__( self ):
        "Create a topology."

        # Initialize Topology
        Topo.__init__( self )

        switches = []
        hosts = []

        switches.append(self.addSwitch('s1'))
        switches.append(self.addSwitch("s2"))

        hosts.append(self.addHost("h1"))
        hosts.append(self.addHost("h2"))

        self.addLink("s1", "h1")
        self.addLink("s2", "h2")
        self.addLink("s1", "s2")


topos = { 'lab': ( lambda: Lab() ) }

if __name__ == '__main__':
    from onosnet import run
    run( Lab() )
