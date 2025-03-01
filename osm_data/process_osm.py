from pyrosm import OSM
import geopandas as gpd

# Specify the path to your .pbf file
pbf_file = "yogyakarta.pbf"

# Initialize the OSM parser
osm = OSM(pbf_file)

# Extract building footprints
buildings = osm.get_buildings()

# Display the first few rows
print(buildings.head())

# Save to a GeoJSON file
buildings.to_file("yogyakarta_buildings.geojson", driver="GeoJSON")
