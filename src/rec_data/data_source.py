class data_source:

    def __init__(self, url):
        self.url = url

usps = data_source('https://mapservices.nps.gov/arcgis/rest/services/NationalDatasets/NPS_Public_Roads/FeatureServer/1')
blm = data_source('https://gis.blm.gov/arcgis/rest/services/transportation/BLM_Natl_GTLF_Public_Display/MapServer/0')
usfs_roads = data_source('https://apps.fs.usda.gov/fsgisx05/rest/services/wo_nfs_gtac/EGIS_RecreationBasemap_01/MapServer/3')
usfs_trails = ''
