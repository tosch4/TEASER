# Created July 2015
# TEASER 4 Development Team

"""This module contains an example how to generate archetype buildings using
TEASER API functions.
"""


def example_generate_archetype():
    """"This function demonstrates the generation of residential and
    non-residential archetype buildings using the API function of TEASER"""

    # First step: Import the TEASER API (called Project) into your Python
    # module

    from teaser.project import Project

    # To use the API instantiate the Project class and rename the Project. The
    # parameter load_data=True indicates that we load `iwu` typology archetype
    # data into our Project (e.g. for Material properties and typical wall
    # constructions. This can take a few seconds, depending on the size of the
    # used data base). Be careful: Dymola does not like whitespaces in names and
    # filenames, thus we will delete them anyway in TEASER.

    prj = Project(load_data=True)
    prj.name = "tabsplusair_test"

    """
    prj = Project(load_data=True)
    prj.name = "ArchetypeEFH"

    prj2 = Project(load_data=True)
    prj2.name = "ArchetypeMFH"

    prj3 = Project(load_data=True)
    prj3.name = "ArchetypeOffice"

    prj4 = Project(load_data=True)
    prj4.name = "TestControlParameters"
    """
    # There are two different types of archetype groups: residential and
    # non-residential buildings. Two API functions offer the opportunity to
    # generate specific archetypes.

    # To generate residential archetype buildings the function
    # Project.add_residential() is used. Seven parameters are compulsory,
    # additional parameters can be set according to the used method. `method`
    # and `usage` are used to distinguish between different archetype
    # methods. The name, year_of_construction, number and height of floors
    # and net_leased_area need to be set to provide enough information for
    # archetype generation. For specific information on the parameters please
    # read the docs.

    heating_profile_night_reduction = [292.15,
                    292.15,
                    292.15,
                    292.15,
                    292.15,
                    292.15,
                    292.15,
                    294.15,
                    294.15,
                    294.15,
                    294.15,
                    294.15,
                    294.15,
                    294.15,
                    294.15,
                    294.15,
                    294.15,
                    294.15,
                    294.15,
                    294.15,
                    294.15,
                    292.15,
                    292.15,
                    292.15]
    cooling_profile_night_reduction = [301.15,
                    301.15,
                    301.15,
                    301.15,
                    301.15,
                    299.15,
                    299.15,
                    299.15,
                    299.15,
                    299.15,
                    299.15,
                    299.15,
                    299.15,
                    299.15,
                    299.15,
                    299.15,
                    299.15,
                    299.15,
                    301.15,
                    301.15,
                    301.15,
                    301.15,
                    301.15,
                    301.15]

    # test for tabsplusair

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair1990heavy100",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair1990heavy200",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair1990light100",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair1990light200",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair2010heavy100",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair2010heavy200",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair2010light100",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair2010light200",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    # Project 1 includes all buildings of the building type 'single family house'

    """
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHradiator",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanel7040",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabs",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                         room_temp_control=False)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabswithRT",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                         room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplus",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=False)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabspluswithRT",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvective",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.convective_heating_cooling()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    
    prj.add_residential(
        method="iwu",
        usage="single_family_dwelling",
        name="EFH1",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="light")

    # Example Radiator heating system

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0)

    prj.add_residential(
        method="iwu",
        usage="single_family_dwelling",
        name="EFH2",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0)

    # Example Radiator heating system

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=40.0, specific_power_cool=40.0)
    
    
    #Project 2 includes all buildings of the building type 'multi family house'
    
    prj2.add_residential(
        method="iwu",
        usage="single_family_dwelling",
        name="MFH1",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0
    )

    # Example Radiator heating system

    bldg = prj2.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_heating_cooling(specific_power_heat=100.0, specific_power_cool=40,
                                                         room_temp_control=False)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    #Project 3 includes all buildings of the building type 'office'
    

    prj3.add_non_residential(
        method="bmvbs",
        usage="office",
        name="OfficeBuilding1",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.5,
        net_leased_area=4000.0
    )

    # Example underfloor heating system

    bldg = prj3.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_heating_cooling(specific_power_heat=40.0, specific_power_cool=40.0,
                                                         room_temp_control=False)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    #   ---------------------------

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanelKR04TN6",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.panel_test_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0, KR=0.4, TN=6)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanelKR04TN12",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.panel_test_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0, KR=0.4,
                                                               TN=12)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanelKR04TN24",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.panel_test_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0, KR=0.4,
                                                               TN=24)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanelKR04TN48",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.panel_test_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0, KR=0.4,
                                                               TN=48)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanelKR04TN96",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.panel_test_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0,
                                                               KR=0.4,
                                                               TN=96)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanelKR04TN192",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.panel_test_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0,
                                                               KR=0.4,
                                                               TN=192)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanelKR04TN384",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.panel_test_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0,
                                                               KR=0.4,
                                                               TN=384)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanelKR04TN3000",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.panel_test_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0,
                                                               KR=0.4,
                                                               TN=3000)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanelKR8TN1600",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.panel_test_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0,
                                                               KR=8,
                                                               TN=1600)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanelKR100TN1",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.panel_test_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0,
                                                               KR=100,
                                                               TN=1)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
    

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR01TN10",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=0.1, TN=10)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR05TN10",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=0.5, TN=10)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR1TN10",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=1, TN=10)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR2TN10",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=2, TN=10)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR4TN10",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=4, TN=10)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR01TN20",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=0.1, TN=20)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR01TN40",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=0.1, TN=40)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR01TN80",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=0.1, TN=80)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR01TN160",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=0.1, TN=160)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR01TN320",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=0.1, TN=320)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR100TN10",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=100, TN=10)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR200TN10",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=200, TN=10)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR500TN10",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=500, TN=10)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR1000TN100",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=1000, TN=100)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    prj4.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvectiveKR1500TN1",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj4.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_convective_heating_cooling(KR=1500, TN=1)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
    """

    # To generate non-residential archetype buildings (in this case an
    # office and a laboratory (a.k.a. institute)) the function
    # Project.add_non_residential() is used. The meaning of compulsory parameters
    # does not differ from the residential archetype building.
    """
    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="OfficeBuilding",
        year_of_construction=1988,
        number_of_floors=4,
        height_of_floors=3.5,
        net_leased_area=4500.0,
    )

    # Example underfloor heating system

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.underfloor_heating(specific_power_heat=100.0)

    prj.add_non_residential(
        method="bmvbs",
        usage="institute",
        name="InstituteBuilding",
        year_of_construction=1952,
        number_of_floors=5,
        height_of_floors=4.0,
        net_leased_area=3400.0,
    )

    prj.add_non_residential(
        method="bmvbs",
        usage="institute",
        name="InstituteBuildingMoisture",
        year_of_construction=1980,
        number_of_floors=3,
        height_of_floors=4.2,
        net_leased_area=3600.0,
        internal_gains_mode=3,
    )

    # Besides `iwu` and `bmvbs` there is a third option for archetype
    # generation. We integrated the typology of TABULA Germany
    # (http://webtool.building-typology.eu/#bm) and other countries are about to
    # follow. To use TABULA archetype simple choose `tabula_de` as the method
    # and `single_family_house`, `multi_family_house`, `terraced_house` or
    # `apartment_block` as the usage. In addition you can specify the
    # construction type of TABULA, chose between `tabula_standard` (default),
    # `tabula_retrofit` or `tabula_adv_retrofit`. In this case we generate one
    # single and one multi family house with TABULA typology.

    # Please not: as we need to load the construction information which are
    # rather big for TABULA, switching from one typology to another in the same
    # Project takes some seconds. If you know from beginning you will only use
    # TABULA typology you should instantiate you Project class without loading
    # data. Project(load_data=False).

    prj.add_residential(
        method="tabula_de",
        usage="single_family_house",
        name="ResidentialBuildingTabula",
        year_of_construction=1988,
        number_of_floors=3,
        height_of_floors=3.2,
        net_leased_area=280.0,
        construction_type="tabula_standard",
    )

    prj.add_residential(
        method="tabula_de",
        usage="multi_family_house",
        name="ResidentialBuildingTabulaMulti",
        year_of_construction=1960,
        number_of_floors=4,
        height_of_floors=3.2,
        net_leased_area=600.0,
        construction_type="tabula_retrofit",
    )
"""
    return prj
    #, prj2, prj3, prj4


if __name__ == "__main__":
    prj = example_generate_archetype()

    print("Example 1: That's it! :)")
