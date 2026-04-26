"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .adm import AdmFetcher
from .agco import AgcoFetcher
from .bunge import BungeFetcher
from .cf_industries import CfIndustriesFetcher
from .cnhi import CnhiFetcher
from .corteva import CortevaFetcher
from .deere import DeereFetcher
from .fmc import FmcFetcher
from .icl import IclFetcher
from .intrepid import IntrepidFetcher
from .kpluss import KplussFetcher
from .kubota import KubotaFetcher
from .mosaic import MosaicFetcher
from .nutrien import NutrienFetcher
from .oci import OciFetcher
from .sqm import SqmFetcher
from .taifer import TaiferFetcher
from .yara import YaraFetcher

FETCHERS = {
    "adm": AdmFetcher,
    "agco": AgcoFetcher,
    "bunge": BungeFetcher,
    "cf_industries": CfIndustriesFetcher,
    "cnhi": CnhiFetcher,
    "corteva": CortevaFetcher,
    "deere": DeereFetcher,
    "fmc": FmcFetcher,
    "icl": IclFetcher,
    "intrepid": IntrepidFetcher,
    "kpluss": KplussFetcher,
    "kubota": KubotaFetcher,
    "mosaic": MosaicFetcher,
    "nutrien": NutrienFetcher,
    "oci": OciFetcher,
    "sqm": SqmFetcher,
    "taifer": TaiferFetcher,
    "yara": YaraFetcher,
}
