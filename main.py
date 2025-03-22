import json
import requests
import constants

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

print(car_makes, makes_model, "\n ********\n")

# json -> data -> makes -> 0 -> dict(key, doc_count)

# per page 10 info
# max of 30 pages use min to confirm:
car_models = {}
for make in makes_model:
    res = requests.get(url=constants.CAR_MODEL.format(make = make.lower()), headers=constants.HEADERS)
    data = json.loads(res.content)
    models = data["data"]["models"]
    car_models_list = car_models.setdefault(make, [])
    for model in models:
        car_models_list.append(model["key"])
    car_models[make] = car_models_list
print("CAR Models: \n", car_models, "\n*****\n")

# data -> models -> dict(key, doc_count)

# method: get
"https://api.terrific.ie/api/ad-elastic-filters?&makes=hyundai" # without model
"https://api.terrific.ie/api/ad-elastic-filters?&makes=hyundai&models=santa+fe" # with model
# lower the values and if space is there use '+' sign in it.
