import json
from app import app


class EquipmentItem:
    level = 0
    force = 0
    intel = 0
    



@app.route('/getitemlist/<string:part>/', methods=['POST'])
def get_itemlist(part):
    result = []
    
    if part == 'weapon':
        result.append('knife')
        result.append('sword')
        result.append('staff')
        result.append('bow')
    elif part == 'title':
        result.append('babo')
        result.append('hogu')
        result.append('bs')
    elif part == 'creature':
        result.append('togu')
        result.append('ingyeo')
    
    
    return json.dumps(result)
