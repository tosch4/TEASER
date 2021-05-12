# Specify path to your simulation workspace
import os
import datetime
import read_results as res
import pandas as pd
from teaser.project import Project
import pickle

if __name__ == '__main__':

    workspace = os.path.join("D:\\", "tbl-cwe", "1_Building_simulation", "sim_results", "Building_Simulation_EFH_MFH_Office")
    print(workspace)
    RESULTS_PATH = os.path.join(workspace, "sim_results")

    """
    # Specify the signals you want to read i.e. Modelica naming of parameters PHeater and
    # PCooler for three thermal zones
    # Example:
    #
    # signals = [
    #    "multizoneSimpleHRS.PHeater[{}]".format(i + 1)
    #    for i in range(0,3)
    # ]
    # signals += [
    #    "multizoneSimpleHRS.PCooler[{}]".format(i + 1)
    #    for i in range(len(bldg.thermal_zones))
    #  ]
    """
    """
    signals = ['multizone.TOpe[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
    signals += ['multizone.TAir[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
    signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.tabsHeatingPower'.format(i + 1) for i in range(len(bldg.thermal_zones))]
    signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.tabsCoolingPower'.format(i + 1) for i in range(len(bldg.thermal_zones))]
    signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempHeatPanel.y'.format(i + 1) for i in range(len(bldg.thermal_zones))]
    signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempCoolPanel.y'.format(i + 1) for i in range(len(bldg.thermal_zones))]
    signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempHeatRem.y'.format(i + 1) for i in range(len(bldg.thermal_zones))]
    signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempHeatRem.y'.format(i + 1) for i in range(len(bldg.thermal_zones))]
    signals += ['multizone.PHeater[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
    signals += ['multizone.PCooler[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
    """

    load_pickle = os.path.join(utilities.get_default_path(), "teaser_pickle.p")

    pickle_prj = pickle.load(open(load_pickle, "rb"))
    print(pickle_prj)

    for bldg in pickle_prj.buildings:
        if "panel" in bldg.name:
            signals = ['multizone.TOpe[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TAir[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempHeatPanel.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempCoolPanel.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.PHeater[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.PCooler[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]

            res.read_results(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H", ),
                index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H", ),
                results_path=os.path.join(workspace),
                csv_path=os.path.join(workspace, "sim_results"),
            )
        elif "tabsplusair" in bldg.name:
            signals = ['multizone.TOpe[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TAir[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TAir[{}].heaterCoolerWithTabs6007C1.pITempHeatPanel.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.TAir[{}].heaterCoolerWithTabs6007C1.pITempCoolPanel.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.PHeater[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.PCooler[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]

            res.read_results(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H", ),
                index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H", ),
                results_path=os.path.join(workspace),
                csv_path=os.path.join(workspace, "sim_results"),
            )



    # Call read_results function

    """res.read_results(
        buildings=["EFHconvective1990heavy100"],
        signals=signals,
        index=pd.date_range(datetime.datetime(2020, 1, 1), periods=8761, freq="H",),
        index_res=pd.date_range(datetime.datetime(2020, 1, 1), periods=8761, freq="H",),
        results_path=os.path.join(workspace),
        csv_path=os.path.join(workspace, "sim_results"),
    )
    """