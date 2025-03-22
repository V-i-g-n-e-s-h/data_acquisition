import os
import json

import requests
from dotenv import load_dotenv
import pandas as pd

import constants


load_dotenv()
constants.HEADERS["authorization"] = os.getenv("AUTHORIZATION")

# car makes extracted:
res = requests.get(url=constants.CAR_MAKE_URL, headers= constants.HEADERS)
data = json.loads(res.content)
makes = data["data"]["makes"]

car_makes = {} # make name: records available
makes_model = [] # if records are more than 300 we are extracting it with model
for make in makes:
    car_makes[make["key"]] = make["doc_count"]
    if make["doc_count"] > 300:
        makes_model.append(make["key"])

# per page 10 info
# max of 30 pages use min to confirm:
car_models = {}
for make in makes_model:
    res = requests.get(url=constants.CAR_MODEL_URL.format(make = make.lower().replace("-", "+").replace(" ", "+")), headers=constants.HEADERS)
    data = json.loads(res.content)
    models = data["data"]["models"]
    car_models_list = car_models.setdefault(make, [])
    for model in models:
        car_models_list.append((model["key"], model["doc_count"]))
    car_models[make] = car_models_list


def process_json(data, df_datas):
    del_keys = {"images", "dealer", "finance_options", "ad_detail"} # process ad_extra_info, location

    for item in data:
        dict_data = item.get("_source", None)

        for i in del_keys:
            dict_data.pop(i)

        try:
            dict_data.update(dict_data.get("ad_extra_info", {})) # for few data extra info not available
        except:
            pass

        dict_data.pop("ad_extra_info")
        try:
            dict_data.update(dict_data.get("location", [{}])[0]) # for few location is empty
        except:
            pass
        dict_data.pop("location")
        
        df_datas.append(dict_data)
    return df_datas

df_datas = []

for make_name, make_doc_count in car_makes.items():
    if make_doc_count <= 300:
        for i in range(1, ((make_doc_count // 10) + (make_doc_count % 10 != 0) + 1)):
            response = requests.get(url=constants.CAR_URL_WITHOUT_MODEL.format(make=make_name.lower().replace("-", "+").replace(" ", "+"), page_no=i), headers=constants.HEADERS)
            df_datas = process_json(json.loads(response.content)["data"]["hits"]["hits"], df_datas)
    else:
        for model_name, model_doc_count in car_models[make_name]:
            for i in range(1, min(31, ((model_doc_count // 10) + (model_doc_count % 10 != 0) + 1))):
                response = requests.get(url=constants.CAR_URL_WITH_MODEL.format(make=make_name.lower().replace("-", "+").replace(" ", "+"), model=model_name.lower().replace("-", "+").replace(" ", "+"), page_no=i), headers=constants.HEADERS)
                df_datas = process_json(json.loads(response.content)["data"]["hits"]["hits"], df_datas)

df = pd.json_normalize(df_datas)
print(df.head())
df.to_excel("output.xlsx", index=False)