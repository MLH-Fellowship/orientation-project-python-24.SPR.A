'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill

app = Flask(__name__)

data = {
    "experience": [
        Experience("Software Developer",
                   "A Cool Company",
                   "October 2022",
                   "Present",
                   "Writing Python Code",
                   "example-logo.png")
    ],
    "education": [
        Education("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "80%",
                  "example-logo.png")
    ],
    "skill": [
        Skill("Python",
              "1-2 Years",
              "example-logo.png")
    ]
}


@app.route('/test')
def hello_world():
    '''
    A simple test route for returning a JSON response with a greeting message.

    Returns
    -------
    json
        Returns a JSON test message.
    '''

    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Route for creating a new experience and fetching all experiences.

    Returns
    -------
    json
        The experience(s) as a JSON object, or an error message.
    '''
    response = None
    if request.method == 'GET':
        index = request.args.get('index')
        experiences = data.get('experience',[])
        if index is not None:
            try:
                index = int(index)
                if 0 <= index < len(experiences):
                    response = jsonify(experiences[index])
                else:
                    response = jsonify({'error':'Experience does not exist'}), 404
            except ValueError:
                response = jsonify({'error':'Experience does not exist'}), 404
        else:
            response = jsonify(experiences)

    if request.method == 'POST':
        required_fields = ['title','company','start_date','end_date','description','logo']
        if not request.json:
            response = jsonify({'error':'Filed Creating Experience'}), 400
        else:
            missing_fields = [field.capitalize() for field in required_fields
                               if field not in request.json]
            if len(missing_fields) > 0:
                response = jsonify({'error':f'Missing Field: {missing_fields[0]}'}), 400
            else:
                experiences = data.get('experience',[])
                experience_id = len(experiences)
                experiences.append(request.json)
                data['experience'] = experiences
                response = jsonify({'id':experience_id})
    return response
@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    '''
    Route for creating a new education and fetching all educations.

    Returns
    -------
    json
        The education(s) as a JSON object, or an error message.
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Route for creating a new skill and fetching all skills.

    Returns
    -------
    json
        The skill(s) as a JSON object, or an error message.
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})
