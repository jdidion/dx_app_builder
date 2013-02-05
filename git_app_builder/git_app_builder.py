# Copyright (C) 2013 DNAnexus, Inc.
#
# This file is part of dx_app_builder.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may not
#   use this file except in compliance with the License. You may obtain a copy
#   of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import dxpy

sys.path.append('/opt/pythonlibs')
import app_builder

@dxpy.entry_point('main')
def main(repo_url, ref='master', credentials=None, recurse=False, publish=False, extra_flags=""):

    clone_dir = app_builder.clone_repository(repo_url, ref=ref, credentials=credentials)

    if recurse:
        for app_dir in app_builder.find_app_directories(clone_dir):
            app_builder.create_app(app_dir, publish=publish, extra_flags=extra_flags)
    else:
        app_builder.create_app(clone_dir, publish=publish, extra_flags=extra_flags)

    return {}


dxpy.run()
