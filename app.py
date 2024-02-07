'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill #pylint: disable=unused-import
from utils import load_data, save_data #pylint: disable=unused-import

app = Flask(__name__)

data = load_data('data.json')


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
        index = request.args.get('index')
        if index is not None:
            try:
                index = int(index)
                education_data = data.get('education', [])
                if 0 <= index < len(education_data):
                    return jsonify(education_data[index])
                return jsonify({'error': 'Education does not exist'}), 404
            except ValueError:
                return jsonify({'error': 'Education does not exist'}), 404

        return jsonify(data.get('education', []))

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

  
@app.route('/resume/skill', methods=['GET', 'POST', 'DELETE', 'PUT'])
def skill():
    '''
    Route for creating a new skill and fetching all skills.

    Returns
    -------
    json
        The skill(s) as a JSON object, or an error message.
    '''
    if request.method == 'GET':
        index = request.args.get('index')
        skills = data.get('skill',[])
        if index is not None:
            try:
                index = int(index)
                if 0 <= index < len(skills):
                    return jsonify(skills[index])
                return jsonify({'error':'Skill does not exist'}), 404
            except ValueError:
                return jsonify({'error':'Skill does not exist'}), 404
        return jsonify(skills)
        
    if request.method == 'POST':
        return jsonify({})
    
    if request.method == 'DELETE':
        index = request.args.get('index')
        skills = data.get('skill',[])
        if index is None:
            return jsonify({'error':'Skill does not exist'}), 404
        try:
            index = int(index)
            if index < 0 or index >= len(skills):
                return jsonify({'error:': 'Skill does not exist'}), 404
            deleted_skill = skills.pop(index)
            save_data('data.json', data)
            return jsonify(deleted_skill), 200
        except ValueError:
            return jsonify({'error:': 'Skill does not exist'}), 404

    if request.method == 'PUT':
        skills = data.get('skill',[])
        index = request.args.get('index')
        if index is None or request.json is None:
            return jsonify({'error:': 'Skill does not exist'}), 404
        try:
            index = int(index)
            if index < 0 or index >= len(skills):
                return jsonify({'error:': 'Skill does not exist'}), 404
            skill_dict = request.json
            updated_skill = {'name': skill_dict['name'],
                                  'proficiency': skill_dict['proficiency'],
                                  'logo': skill_dict['logo']}
            skills[index] = updated_skill
            data['skill'] = skills
            save_data('data.json', data)
            return jsonify(updated_skill), 200
        except (ValueError, KeyError, TypeError):
            return jsonify({'error:': 'Skill does not exist'}), 404

    return jsonify({})