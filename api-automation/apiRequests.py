from cred import cred
import requests
def api(url):
    print()
    print()


    response = requests.post(url)
    resp = requests.post(url) 
    resp_body = resp.json()
    print(resp_body)


    print()
    print()


    print('response.content=',response.content)


    print()
    print()


    return response

url = 'https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&user_id='+cred.userid+'&api_key='+cred.api_key+'&format=json&nojsoncallback=1'

print(api(url))



print()
print()