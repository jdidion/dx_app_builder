#!/usr/bin/env python

import dxpy
import sys

sys.path.append('/opt/pythonlibs')
import asset_builder


@dxpy.entry_point('main')
def main(conf_json, asset_makefile=None, custom_asset=None):
    return asset_builder.build_asset(conf_json, asset_makefile, custom_asset)

dxpy.run()
