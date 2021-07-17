import requests
from cred import cred

def test_post_headers_body_json():
    url = 'https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&user_id='+cred.userid+'&api_key='+cred.api_key+'&format=json&nojsoncallback=1'
    resp = requests.post(url) 
    resp_body = resp.json()
    print(resp_body)

    assert resp.status_code == 200
    
    assert resp_body['stat'] == 'ok'
