'''
Tests in Pytest
'''

from app import app
from models import Education


def test_client():
    '''
    Makes a request and checks the message received is the same
    '''
    response = app.test_client().get('/test')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, World!"


def test_experience():
    '''
    Add a new experience and then get all experiences. 
    
    Check that it returns the new experience in that list
    '''
    example_experience = {
        "title": "Software Developer",
        "company": "A Cooler Company",
        "start_date": "October 2022",
        "end_date": "Present",
        "description": "Writing JavaScript Code",
        "logo": "example-logo.png"
    }

    item_id = app.test_client().post('/resume/experience',
                                     json=example_experience).json['id']
    response = app.test_client().get('/resume/experience')
    assert response.json[item_id] == example_experience


def test_education():
    '''
    Add a new education and then get all educations. 
    
    Check that it returns the new education in that list
    '''
    example_education = {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png"
    }
    item_id = app.test_client().post('/resume/educations',
                                     json=example_education).json['id']

    response = app.test_client().get('/resume/educations')
    assert response.json[item_id] == example_education


def test_get_educations(mocker):
    '''
    Get all educations and check that it returns the list of educations
    '''
    mock_data = {
        'education': [
            Education(
                'Computer Science',
                'Western University',
                'September 2023',
                'July 2022',
                '90%',
                'fake-logo.png',
            )
        ]
    }
    mocker.patch.dict('app.data', mock_data, clear=True)

    expected_response = [
        {

            "course": "Computer Science",
            "end_date": 'July 2022',
            "grade": "90%",
            "logo": 'fake-logo.png',
            "school": 'Western University',
            "start_date": 'September 2023',
        }
    ]
    response = app.test_client().get('/resume/educations')
    assert response.status_code == 200
    assert response.json == expected_response


def test_skill():
    '''
    Add a new skill and then get all skills. 
    
    Check that it returns the new skill in that list
    '''
    example_skill = {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png"
    }

    item_id = app.test_client().post('/resume/skill',
                                     json=example_skill).json['id']

    response = app.test_client().get('/resume/skill')
    assert response.json[item_id] == example_skill
