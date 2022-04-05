import os

from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.project import Project
from teaser.logic.buildingobjects.building import Building
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.useconditions \
    import UseConditions
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from datetime import datetime

# define vector for iteration
useCases = [["Living", "living"],  # MFH
            ["Hotel room", "hotelRoom"],  # Hotelzimmer
            ["Group Office (between 2 and 6 employees)", "groupOffice"],  # Gruppenbuero
            ["Meeting, Conference, seminar", "meeting"],  # Sitzungszimmer
            ["Bed room", "bedRoom"],  # Bettenzimmer
            ["Medical and therapeutic practices", "medical"]]  # Stationszimmer

# Construction Year, Height, Area, Room Length, Room Depth, minAHU, maxAHU
roomValues = [[2020, 2.5, 4, 5, 0, 2.5],  # MFH
              [2020, 2.5, 4, 5, 0, 2.5],  # Hotelzimmer
              [2020, 3, 6, 6, 0, 2.5],  # Gruppenbuero
              [2020, 3, 6, 6, 0, 2.5],  # Sitzungszimmer
              [2020, 2.5, 6, 6, 0, 2.5],  # Bettenzimmer
              [2020, 3, 6, 6, 0, 2.5]]  # Stationszimmer

for i in range(len(useCases)):
    prj = Project(load_data=True)
    prj.name = useCases[i][0]

    # load all use conditions
    prj.data.load_uc_binding()

    # set building parameters
    bldg = Building(parent=prj)
    bldg.name = useCases[i][0]
    bldg.year_of_construction = roomValues[i][0]
    bldg.height_of_floors = roomValues[i][1]
    # net_leased_area wird im Setter von ThermalZone.area gesetzt!
    # bldg.net_leased_area = roomValues[i][2]*roomValues[i][3]
    bldg.with_ahu = True
    bldg.internal_gains_mode = 3
    # bldg.central_ahu.efficiency_recovery_false = 0

    # set thermal zone parameters
    tz = ThermalZone(parent=bldg)
    tz.name = useCases[i][0]
    tz.area = roomValues[i][2]*roomValues[i][3]
    tz.volume = tz.area * bldg.height_of_floors
    tz.use_conditions = UseConditions(parent=tz)
    tz.use_conditions.load_use_conditions(useCases[i][0], prj.data)
    # tz.use_conditions.use_constant_infiltration = True # todo check if this works
    # tz.infiltration_rate = 0.06  # tz.use_conditions.infiltration_rate = 0.2
    # tz.use_conditions.with_ahu = True
    # tz.use_conditions.with_cooling = True
    # tz.use_conditions.with_heating = True
    # tz.use_conditions.max_ahu = 500.0 # m^3/(s*h), default = 0
    tz.use_conditions.HeaterOn = True
    tz.use_conditions.CoolerOn = True
    # setting min/max air volume flow >> necessary at relative occupancy?
    # tz.use_conditions.min_ahu = 0.1
    # tz.use_conditions.max_ahu = 5.0

    # tz.use_conditions.set_temp_heat = 293.15 # todo in modelica
    # todo shading

    # set archetype parameters
    outer_wall = OuterWall(tz)
    # 30 perc of outer wall area is window >> 70 perc for wall
    outer_wall.area = 0.7*(roomValues[i][1]*roomValues[i][2])
    # 270 deg = west --> probably highest solar radiation in the evening / night
    outer_wall.orientation = 270
    outer_wall.tilt = 90
    # outer_wall.load_type_element(2020, "tabula_standard_1_SFH")
    outer_wall.load_type_element(2000, "heavy")

    inner_wall = InnerWall(tz)
    inner_wall.area = (roomValues[i][1]*roomValues[i][2]+2*roomValues[i][1]*roomValues[i][3])
    inner_wall.tilt = 90
    inner_wall.load_type_element(bldg.year_of_construction, "tabula_standard_1_SFH")
    inner_wall.load_type_element(2000, "heavy")

    ceiling = Ceiling(tz)
    ceiling.area = tz.area
    ceiling.load_type_element(bldg.year_of_construction, "tabula_standard_1_SFH")

    floor = Floor(tz)
    floor.area = tz.area
    floor.load_type_element(bldg.year_of_construction, "tabula_standard_1_SFH")

    window = Window(tz)
    window.area = 0.3*outer_wall.area
    window.tilt = 90
    window.orientation = 270
    # window.load_type_element(bldg.year_of_construction, "Waermeschutzverglasung, dreifach")
    window.load_type_element(2000, "Kunststofffenster, Isolierverglasung")

    # calculation of resistance and capacity parameters (?)
    bldg.calc_building_parameter()

    # create AixLib model
    prj.used_library_calc = "AixLib"
    # wie viele Elemente werden erstellt?
    # 2 = TwoElement (Exterior, Interior)
    # 4 = FourElement (Exterior, Roof, Interior, Floor)
    prj.number_of_elements_calc = 2
    prj.weather_file_path = os.path.join(
        "D:/900_repository/tosch4/TEASER/teaser/data/input/inputdata/weatherdata/DEU_BW_Mannheim_107290_TRY2010_12_Jahr_BBSR.mos")

    # ...
    prj.calc_all_buildings()
    # ...
    prj.export_aixlib(path=os.path.join("D:/900_repository/dezintegral/AP1/"+datetime.now().strftime("%Y%m%d_%H%M")+"/"+useCases[i][1]+"/"))
