#!/usr/bin/env python3

from os import getenv

from ts_v2_catalog_backport.ts_v2_catalog_backport import TsV2CatalogBackporter

if __name__ == '__main__':
    backporter = TsV2CatalogBackporter(prefix=getenv('PREFIX', 'dev-'), debug=getenv('DEBUG', True))
    backporter.run()
