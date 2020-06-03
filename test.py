from datetime import datetime
from typing import List
from pydantic import BaseModel
import json


class PushEventModel(BaseModel):
    run_API_updater: bool
    project_url: str
    branch: str
    checkout_sha: str
    web_hook_token: str
    build_scenes: str
    scripting_define_symbols: str

    def funcname(self, name: str):
        if not name:
            print("NO tiene nombre")
        else:
            print("SI tiene nombre")

    def get_advance_options_as_params(self, bm: BaseModel) -> str:
        content = ""
        for key, value in bm.dict().items():
            if value is None or not str(value):
                continue

            if key == "run_API_updater" and str(value) == "True":
                key = "accept-apiupdate"
                value = ''

            if key == "build_scenes" or key == "scripting_define_symbols":
                value = str(value).replace(
                    " ", '\\ ').replace(",", ":").replace("'", "").strip("[]")

            advance_options_formatted = " -" + str(key) + " " + str(value)
            content += advance_options_formatted

        return content


external_data = {
    'run_API_updater': True,
    'project_url': 'https://gitlab.com/wololo-ci/pipeline_external_tools.git',
    'branch': '',
    'checkout_sha': '',
    'web_hook_token': '',
    'build_scenes': "['Assets/Test Scene.unity','Assets/Testscene2.unity',Assets/Testscene44.unity]",
    'scripting_define_symbols': "['Def_custom','my_custom_def']"

}

test = PushEventModel(**external_data)
print(test.get_advance_options_as_params(test))

# class CreateJson:
#     def build_json_from_list(self, lista: list):
#         # lenght: int = len(self.bc_advance_options.environment_vars)
#         # if lenght < 1:
#         #     return

#         data = {}
#         for idx, value in enumerate(lista):
#             value_split = str(value).split("=")
#             data[value_split[0]] = value_split[1]

#         json_data = json.dumps(data)
#         return json_data


# l = CreateJson()
# # lt = {'MY_VAR': '12', 'MY_CEV': 'c:/fran/Ld'}
# jsonData = l.build_json_from_list(
#     ['MY_VAR=12', 'MY_CEV=c:/fran/Ld', 'MY_CEV=c:/fran/Ld', 'MY_=c:/f'])
# print(jsonData)
