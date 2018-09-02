from flask import Flask, request, json, jsonify
import attendance
import datetime

app = Flask(__name__)

members = attendance.read_members(app)

@app.route('/api/add', methods=['POST'])
def add():
    ''' insert a new entry '''
    data = request.get_json()
    
    active_members = members["active_members"]

    # prepare row for injecting into spreadsheet
    row         = []
    term        = members["term"]
    location    = members["location"]
    today       = datetime.date.today().strftime('%d/%m/%Y')


    for member in active_members:
        if member["id"] == data["id"]:
            for k, v in member.items():
                # break parents list to string
                if type(v) == list:
                    parents = ", ".join(v)
                    row.append(parents)
                else:
                    row.append(v)
            row.append(term)                        # append term
            row.append(today)                       # append date
            row.append(location)                    # append location
    
            attendance.mark_present(row, 2)
            return jsonify(member)
    

app.run(port=5001, debug=True)