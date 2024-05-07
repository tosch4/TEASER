from enum import Enum
from teaser.logic.archetypebuildings.bmvbs.office import Office
from teaser.logic.archetypebuildings.bmvbs.custom.institute import Institute
from teaser.logic.archetypebuildings.bmvbs.custom.institute4 import Institute4
from teaser.logic.archetypebuildings.bmvbs.custom.institute8 import Institute8
from teaser.logic.archetypebuildings.urbanrenet.est1a import EST1a
from teaser.logic.archetypebuildings.urbanrenet.est1b import EST1b
from teaser.logic.archetypebuildings.urbanrenet.est2 import EST2
from teaser.logic.archetypebuildings.urbanrenet.est3 import EST3
from teaser.logic.archetypebuildings.urbanrenet.est4a import EST4a
from teaser.logic.archetypebuildings.urbanrenet.est4b import EST4b
from teaser.logic.archetypebuildings.urbanrenet.est5 import EST5
from teaser.logic.archetypebuildings.urbanrenet.est6 import EST6
from teaser.logic.archetypebuildings.urbanrenet.est7 import EST7
from teaser.logic.archetypebuildings.urbanrenet.est8a import EST8a
from teaser.logic.archetypebuildings.urbanrenet.est8b import EST8b
from teaser.logic.archetypebuildings.tabula.de.singlefamilyhouse import (
    SingleFamilyHouse,
)
from teaser.logic.archetypebuildings.tabula.dk.singlefamilyhouse import (
    SingleFamilyHouse as SingleFamilyHouse_DK,
)
from teaser.logic.archetypebuildings.tabula.de.terracedhouse import TerracedHouse
from teaser.logic.archetypebuildings.tabula.dk.terracedhouse import (
    TerracedHouse as TerracedHouse_DK,
)
from teaser.logic.archetypebuildings.tabula.de.multifamilyhouse import MultiFamilyHouse
from teaser.logic.archetypebuildings.tabula.de.apartmentblock import ApartmentBlock
from teaser.logic.archetypebuildings.tabula.dk.apartmentblock import (
    ApartmentBlock as ApartmentBlock_DK,
)
from teaser.logic.archetypebuildings.bmvbs.singlefamilydwelling import (
    SingleFamilyDwelling,
)


class GeometryData(Enum):
    IwuSingleFamilyDwelling = "iwu_single_family_dwelling"

    TabulaDeSingleFamilyHouse = "tabula_de_single_family_house"
    TabulaDeTerracedHouse = "tabula_de_terraced_house"
    TabulaDeMultiFamilyHouse = "tabula_de_multi_family_house"
    TabulaDeApartmentBlock = "tabula_de_apartment_block"

    TabulaDkSingleFamilyHouse = "tabula_dk_single_family_house"
    TabulaDkTerracedHouse = "tabula_dk_terraced_house"
    TabulaDkApartmentBlock = "tabula_dk_apartment_block"

    BmvbsOffice = "bmvbs_office"
    BmvbsInstitute = "bmvbs_institute"
    BmvbsInstitute4 = "bmvbs_institute4"
    BmvbsInstitute8 = "bmvbs_institute8"

    UrbanrenetEst1a = "urbanrenet_est1a"
    UrbanrenetEst1b = "urbanrenet_est1b"
    UrbanrenetEst2 = "urbanrenet_est2"
    UrbanrenetEst3 = "urbanrenet_est3"
    UrbanrenetEst4a = "urbanrenet_est4a"
    UrbanrenetEst4b = "urbanrenet_est4b"
    UrbanrenetEst5 = "urbanrenet_est5"
    UrbanrenetEst6 = "urbanrenet_est6"
    UrbanrenetEst7 = "urbanrenet_est7"
    UrbanrenetEst8a = "urbanrenet_est8a"
    UrbanrenetEst8b = "urbanrenet_est8b"

class ConstructionData(Enum):
    iwu_heavy = "iwu_heavy"
    iwu_light = "iwu_light"
    tabula_de_standard = "tabula_de_standard"
    tabula_de_retrofit = "tabula_de_retrofit"
    tabula_de_adv_retrofit = "tabula_de_adv_retrofit"
    tabula_dk_standard = "tabula_dk_standard"
    tabula_dk_retrofit = "tabula_dk_retrofit"
    tabula_dk_adv_retrofit = "tabula_dk_adv_retrofit"
    kfw_40 = "kfw_40"
    kfw_55 = "kfw_55"
    kfw_70 = "kfw_70"
    kfw_85 = "kfw_85"
    kfw_100 = "kfw_100"

    def get_prefix(self):
        parts = self.value.split("_", 2)
        if len(parts) == 2:
            return parts[0]
        elif len(parts) == 3:
            return "_".join(parts[:2])
        else:
            return self.value
    def is_iwu(self):
        return self.get_prefix() == "iwu"

    def is_tabula_de(self):
        return self.get_prefix() == "tabula_de"

    def is_tabula_dk(self):
        return self.get_prefix() == "tabula_dk"

    def is_kfw(self):
        return self.get_prefix() == "kfw"

#dictionary for each building class:
geometries = {
    #non residential:
    #BMVBS
    GeometryData.BmvbsOffice: Office,
    GeometryData.BmvbsInstitute: Institute,
    GeometryData.BmvbsInstitute4: Institute4,
    GeometryData.BmvbsInstitute8: Institute8,

    #residential:
    #IWU
    GeometryData.IwuSingleFamilyDwelling: SingleFamilyDwelling,
    #Tabula DE
    GeometryData.TabulaDeSingleFamilyHouse: SingleFamilyHouse,
    GeometryData.TabulaDeTerracedHouse: TerracedHouse,
    GeometryData.TabulaDeMultiFamilyHouse: MultiFamilyHouse,
    GeometryData.TabulaDeApartmentBlock: ApartmentBlock,
    #Tabula DK
    GeometryData.TabulaDkSingleFamilyHouse: SingleFamilyHouse_DK,
    GeometryData.TabulaDkTerracedHouse: TerracedHouse_DK,
    GeometryData.TabulaDkApartmentBlock: ApartmentBlock_DK,
    #Urbanrenet
    GeometryData.UrbanrenetEst1a: EST1a,
    GeometryData.UrbanrenetEst1b: EST1b,
    GeometryData.UrbanrenetEst2: EST2,
    GeometryData.UrbanrenetEst3: EST3,
    GeometryData.UrbanrenetEst4a: EST4a,
    GeometryData.UrbanrenetEst4b: EST4b,
    GeometryData.UrbanrenetEst5: EST5,
    GeometryData.UrbanrenetEst6: EST6,
    GeometryData.UrbanrenetEst7: EST7,
    GeometryData.UrbanrenetEst8a: EST8a,
    GeometryData.UrbanrenetEst8b: EST8b,
}

#allow certain geometries for the construction_data in each case
allowed_geometries = {
    ConstructionData.iwu_heavy: [GeometryData.IwuSingleFamilyDwelling, GeometryData.BmvbsOffice,
                                 GeometryData.BmvbsInstitute, GeometryData.BmvbsInstitute4,
                                 GeometryData.BmvbsInstitute8, GeometryData.UrbanrenetEst1a,
                                 GeometryData.UrbanrenetEst1b, GeometryData.UrbanrenetEst2,
                                 GeometryData.UrbanrenetEst3, GeometryData.UrbanrenetEst4a,
                                 GeometryData.UrbanrenetEst4b, GeometryData.UrbanrenetEst5,
                                 GeometryData.UrbanrenetEst6, GeometryData.UrbanrenetEst7,
                                 GeometryData.UrbanrenetEst8a, GeometryData.UrbanrenetEst8b],
    ConstructionData.iwu_light: [GeometryData.IwuSingleFamilyDwelling, GeometryData.BmvbsOffice,
                                 GeometryData.BmvbsInstitute, GeometryData.BmvbsInstitute4,
                                 GeometryData.BmvbsInstitute8, GeometryData.UrbanrenetEst1a,
                                 GeometryData.UrbanrenetEst1b, GeometryData.UrbanrenetEst2,
                                 GeometryData.UrbanrenetEst3, GeometryData.UrbanrenetEst4a,
                                 GeometryData.UrbanrenetEst4b, GeometryData.UrbanrenetEst5,
                                 GeometryData.UrbanrenetEst6, GeometryData.UrbanrenetEst7,
                                 GeometryData.UrbanrenetEst8a, GeometryData.UrbanrenetEst8b],

    ConstructionData.tabula_de_standard: [GeometryData.TabulaDeSingleFamilyHouse, GeometryData.TabulaDeTerracedHouse,
                                          GeometryData.TabulaDeMultiFamilyHouse, GeometryData.TabulaDeApartmentBlock],
    ConstructionData.tabula_de_retrofit: [GeometryData.TabulaDeSingleFamilyHouse, GeometryData.TabulaDeTerracedHouse,
                                          GeometryData.TabulaDeMultiFamilyHouse, GeometryData.TabulaDeApartmentBlock],
    ConstructionData.tabula_de_adv_retrofit: [GeometryData.TabulaDeSingleFamilyHouse, GeometryData.TabulaDeTerracedHouse,
                                              GeometryData.TabulaDeMultiFamilyHouse, GeometryData.TabulaDeApartmentBlock],

    ConstructionData.tabula_dk_standard: [GeometryData.TabulaDkSingleFamilyHouse, GeometryData.TabulaDkTerracedHouse,
                                          GeometryData.TabulaDkApartmentBlock],
    ConstructionData.tabula_dk_retrofit: [GeometryData.TabulaDkSingleFamilyHouse, GeometryData.TabulaDkTerracedHouse,
                                          GeometryData.TabulaDkApartmentBlock],
    ConstructionData.tabula_dk_adv_retrofit: [GeometryData.TabulaDkSingleFamilyHouse, GeometryData.TabulaDkTerracedHouse,
                                              GeometryData.TabulaDkApartmentBlock],

    ConstructionData.kfw_40: [GeometryData.IwuSingleFamilyDwelling, GeometryData.TabulaDeSingleFamilyHouse],
    ConstructionData.kfw_55: [GeometryData.IwuSingleFamilyDwelling, GeometryData.TabulaDeSingleFamilyHouse],
    ConstructionData.kfw_70: [GeometryData.IwuSingleFamilyDwelling, GeometryData.TabulaDeSingleFamilyHouse],
    ConstructionData.kfw_85: [GeometryData.IwuSingleFamilyDwelling, GeometryData.TabulaDeSingleFamilyHouse],
    ConstructionData.kfw_100: [GeometryData.IwuSingleFamilyDwelling, GeometryData.TabulaDeSingleFamilyHouse],
}
