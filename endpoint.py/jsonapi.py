from flask import Flask,jsonify
from datetime import datetime
from time import gmtime, strftime

today = datetime.today()
day = today.strftime('%A')

utc_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

app = Flask(__name__)

@app.route('/get_details/<slack_name>/<track>', methods = ['GET'])
def get_details(slack_name, track):

    data = {
        "slack_name":slack_name,
        "current_day":day,
        "utc_time":utc_time,
        "track":track,
        "github_file_url":"https://github.com/anenhle/json-api",
        "github_repo_url":"https://github.com/anenhle/json-api.git",
        "status_code": 200
    }

    json_data = jsonify(data)

    return json_data


if __name__ == '__main__':
    app.run(debug=True)