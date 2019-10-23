# SingleYarn.py

#Create an object of the CTextile class 
textile = CTextile( )

#Create a single yarn object:
yarn = CYarn( )

#Add 3 nodes to the yarn, specifying the coordinate positions only:
yarn.AddNode( CNode( XYZ(0, 0.0, 0)) )
yarn.AddNode( CNode( XYZ(1, 3.5, 0)) )
yarn.AddNode( CNode( XYZ(0, 7.0, 0)) )

# Set interpolation, defaults to periodic
yarn.AssignInterpolation( CInterpolationCubic())

#Define three different cross-sectional shapes at the master nodes 
sections = CYarnSectionInterpNode()
sections.AddSection(CSectionLenticular(1, 0.5, 0.1))
sections.AddSection(CSectionPowerEllipse( 1.0, 0.4, 0.4, 0.25) )

# Hybrid Section
Top = CSectionEllipse( 1.0, 0.4 )
Bottom = CSectionPowerEllipse( 1.0, 0.4, 0.4, 0.25 )
sections.AddSection( CSectionHybrid( Top, Bottom ) )

# Assign sections to yarn
yarn.AssignSection( sections )

# Add repeat vectors
yarn.AddRepeat( XYZ(3, 0, 0) )
yarn.AddRepeat( XYZ(0, 7, 0) )
yarn.AddRepeat( XYZ(0.5, 0, 1) )

# Add the yarn to the textile 
textile.AddYarn( yarn )	

Plower = XYZ(-0.5, 0, -0.5)
Pupper = XYZ(7.5, 35, 2.5)
textile.AssignDomain( CDomainPlanes(Plower, Pupper) )


# Add the textile with the name "single yarn" to the TexGen database
# If the script is run from within the TexGen GUI the yarn is displayed
AddTextile("yarn sections", textile)
