from flask import Flask, request, json, jsonify
import attendance

app = Flask(__name__)

members = attendance.read_members(app)

@app.route('/api/add', methods=['POST'])
def add():
    ''' insert a new entry '''
    data = request.get_json()
    
    active_members = members["active_members"]

    row = []
    for member in active_members:
        if member["id"] == data["id"]:
            for k,v in member.items():
                # watch for normal values
                if type(v) == str or type(v) == int:
                    row.append(v)
                else:
                    # if type == list
                    parents = ", ".join(v)
                    row.append(parents) 
            print(row)
            attendance.mark_present(row, 2)
            return jsonify(member)
    

app.run(port=5001, debug=True)