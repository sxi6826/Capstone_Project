from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):

        Topo.__init__( self )

        # Add hosts and switches)
        Switch_one = self.addSwitch( 's1' )
        Switch_two = self.addSwitch( 's2' )
        Switch_three = self.addSwitch( 's3' )
        Switch_four = self.addSwitch( 's4' )
        Switch_five = self.addSwitch( 's5' )

        Host_one = self.addHost( 'h1' )
        Host_two = self.addHost( 'h2' )
        Host_three = self.addHost( 'h3' )
        Host_four = self.addHost( 'h4' )
        Host_five = self.addHost( 'h5' )
        Host_six = self.addHost( 'h6' )
        Host_seven = self.addHost( 'h7' )
        Host_eight = self.addHost( 'h8' )
        Host_nine = self.addHost( 'h9' )
        Host_ten = self.addHost( 'h10' )
        Host_eleven = self.addHost( 'h11' )
        Host_twelve = self.addHost( 'h12' )


        # Add links between hosts and switches
        self.addLink( Host_one, Switch_one )
        self.addLink( Host_two, Switch_one )
        self.addLink( Host_three, Switch_one )
        self.addLink( Host_four, Switch_two )
        self.addLink( Host_five, Switch_two )
        self.addLink( Host_six, Switch_three )
        self.addLink( Host_seven, Switch_three )
        self.addLink( Host_eight, Switch_four )
        self.addLink( Host_nine, Switch_four )
        self.addLink( Host_ten, Switch_five )
        self.addLink( Host_eleven, Switch_five )
        self.addLink( Host_twelve, Switch_five )

        self.addLink( Switch_two, Switch_one )
        self.addLink( Switch_two, Switch_four )
        self.addLink( Switch_two, Switch_five )
        self.addLink( Switch_two, Switch_three )

topos = { 'mytopo': ( lambda: MyTopo() ) }
