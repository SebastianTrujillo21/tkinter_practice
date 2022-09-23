from calendar import day_abbr
import json

with open('data.json','r') as f:
    data=json.load(f)

fechas=data["fechas"]
enero=fechas["Enero"]
febrero=fechas["Febrero"]
print(enero)
print(febrero)