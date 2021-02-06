from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework import status
class UserActivationView(APIView):
    def get (self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        print(uid,token)
        post_url = web_url + f"/auth/users/activation/"#/?uid={uid}&token={token}"
        post_data = {'uid': uid, 'token': token}
        result = requests.post(post_url,data=post_data)
        content = result.text

        print(result.status_code)
        if(result.status_code<200 or result.status_code>300):
            return Response("Activation is not possible because token is not correct. Do not try to abuse the system. We are watching you.",status.HTTP_403_FORBIDDEN)
        return Response("You are now an active user. Enjoy the platform by logging in :) ")