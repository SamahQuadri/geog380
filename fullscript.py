# Shayna Fever and Samah Quadri
# GEOG 380 Final Project
# 5/6/2019


# You will need to ensure that you have the Illinois zip code shapefile
# as well as the coal power plant shapefile. 

# Import arcpy module and set the environment.
import arcpy
from arcpy import env
env.workspace = "E:/GEOG380/FinalProject"


# This variable will represent the buffer distance.
# This python command will ask for the user input when the code is run.
# The user will have to input some distance in miles. These distances will typically
# range from 0-5 miles for winter months and 5-20 miles for summer months,
# depending on the current/expected meteorological conditions.
Distance__value_or_field_ = arcpy.GetParameterAsText(0)

# This section of the code is to assign variables to different shapefiles or outputs.
Illinois_CoalPlants = "Illinois_CoalPlants"
CoalPlantBuffer_shp = "E:/GEOG380/FinalProject/CoalPlantBuffer.shp"
ILZipCodes = "ILZipCodes"
IntersectLayer_shp = "E:/GEOG380\\FinalProject/IntersectLayer.shp"
IntersectLayer_shp__4_ = IntersectLayer_shp
IntersectLayer_shp__3_ = IntersectLayer_shp__4_
PolyIntersectStats = "E:/GEOG380/FinalProject/PolyIntersectStats"

# Here we are using the buffer tool. This will create a buffer around each of the coal
# plants based on the distance input by the user.
arcpy.Buffer_analysis(Illinois_CoalPlants, CoalPlantBuffer_shp, Distance__value_or_field_, "FULL", "ROUND", "NONE", "", "PLANAR")

# Now we are intersecting the illinois zip code shapefile with the newly created coal power
# plants buffer layer. Doing so will preserve the population information in the zip code shapefile. 
arcpy.Intersect_analysis("E:\\GEOG380\\FinalProject\\CoalPlantBuffer.shp #;ILZipCodes #", IntersectLayer_shp, "ALL", "", "INPUT")

# Here we are adding a new field to the attribute table of our newly created intersected layer.
# The new field that we are creating will hold the number of people within each buffer. 
arcpy.AddField_management(IntersectLayer_shp, "Areapop", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Now we are performing a calculation to fill in the new field. Essentially, this calcuation
# determines how many people from each zip code tract are within the buffer.
arcpy.CalculateField_management(IntersectLayer_shp__4_, "Areapop", "[POPULATION]*( [Shape_Area] / [Shape_Area] )", "VB", "")

# This last step sums over all the people within each buffer to determine overall how many people
# in Illinois are affected by the pollution by the coal power plants.
arcpy.Statistics_analysis(IntersectLayer_shp__3_, PolyIntersectStats, "Areapop SUM", "")

