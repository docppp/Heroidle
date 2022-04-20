
def json_create():
    return '''{
  "user": "user1234",
  "character": {"lvl": 1,"exp": 0,"honor": 0,"mission": {}},
  "kingdom": {"cityhall": 1,"goldmine": 0,"stonemine": 0,"sawmill": 0,"trainingroom": 0},
  "warehouse": {
    "gold": {"amount": 10000,"onhand": 0,"onhandmax": 1000,"income": 10},
    "stone": {"amount": 10000,"onhand": 0,"onhandmax": 1000,"income": 10},
    "wood": {"amount": 10000,"onhand": 0,"onhandmax": 1000,"income": 10}
  }
}'''


def json_create():
    return '''{
  "01": "user1234",
  "02": {"03": 1,"04": 0,"05": 0,"06": {}},
  "07": {"08": 1,"09": 0,"0A": 0,"0B": 0,"0C": 0},
  "0D": {
    "0F": {"10": 10000,"11": 0,"12": 1000,"13": 10},
    "14": {"15": 10000,"16": 0,"17": 1000,"18": 10},
    "19": {"1A": 10000,"1B": 0,"1C": 1000,"1D": 10}
  }
}'''




gold_onhand = 0
stone_onhand = 0
wood_onhand = 0


def json_update():
    global gold_onhand
    global stone_onhand
    global wood_onhand
    gold_onhand += 10
    stone_onhand += 10
    wood_onhand += 10
    return f'''{{
      "user": "user1234",
      "character": {{"lvl": 1,"exp": 0,"honor": 0,"mission": {{}}}},
      "kingdom": {{"cityhall": 1,"goldmine": 0,"stonemine": 0,"sawmill": 0,"trainingroom": 0}},
      "warehouse": {{
        "gold": {{"amount": 10000,"onhand": {gold_onhand},"onhandmax": 1000,"income": 10}},
        "stone": {{"amount": 10000,"onhand": {stone_onhand},"onhandmax": 1000,"income": 10}},
        "wood": {{"amount": 10000,"onhand": {wood_onhand},"onhandmax": 1000,"income": 10}}
      }}
    }}'''
