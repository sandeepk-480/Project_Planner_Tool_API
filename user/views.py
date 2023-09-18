from rest_framework.views import APIView
from user.serializers import UserSerializer, UserGETSerializer, UserPatchSerializer
from rest_framework.response import Response
from rest_framework import status
from user.models import User
from team.models import Team
from team.serializers import TeamSerializer


class UserBase(APIView):
    """
    Base interface implementation for API's to manage users.
    """
    def post(self, request):
        response = self.create_user(request)
        return response
    

    def get(self,request,id=None):
        if 'id' in request.data:
            response = self.describe_user(request)
            return response
        elif id is not None:
            return self.get_user_teams(request,id)
        else:
            response = self.list_users()
            return response

    def patch(self, request):
        return self.update_user(request)




    # create a user
    def create_user(self, request: str) -> str:
        """
        :param request: A json string with the user details
        {
          "name" : "<user_name>",
          "description" : "<some description>",
          "display_name" : "<display name>"
        }
        :return: A json string with the response {"id" : "<user_id>"}

        Constraint:
            * user name must be unique
            * name can be max 64 characters
            * display name can be max 64 characters
            * must have creation time for the user
        """
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data.get('id')}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    # list all users
    def list_users(self) -> str:
        """
        :return: A json list with the response
        [
          {
            "name" : "<user_name>",
            "display_name" : "<display name>",
            "description" : "<some description>",
            "creation_time" : "<some date:time format>"
          }
        ]
        """
        data = User.objects.all()
        serializer = UserGETSerializer(data, many=True)
        return Response(serializer.data)



    # describe user
    def describe_user(self,request: str) -> str:
        """
        :param request: A json string with the user identifier
        {
          "id" : "<user_id>"
        }

        :return: A json string with the response

        {
          "name" : "<user_name>",
          "display_name" : "<display name>",
          "description" : "<some description>",
          "creation_time" : "<some date:time format>"
        }

        """
        data1 = request.data.get('id')
     
        try:
            data = User.objects.get(id=data1)
        except User.DoesNotExist:
            return Response({"MSG": "User with this ID Does not Exists"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserGETSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)



    # update user
    def update_user(self, request: str) -> str:
        """
        :param request: A json string with the user details
        {
          "id" : "<user_id>",
          "description" : "<some description>",
          "display_name" : "<display name>"
        }

        :return:

        Constraint:
            * user name cannot be updated
            * name can be max 64 characters
            * display name can be max 128 characters
        """
        dataa = request.data.get('id')
        data1 = User.objects.get(id = dataa)
        serializer = UserPatchSerializer(data1, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"MSG": "Updated"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)



    def get_user_teams(self, request,id) -> str:
        """
        :param request:
        {
          "id" : "<user_id>"
        }

        :return: A json list with the response.
        [
          {
            "name" : "<team_name>",
            "description" : "<some description>",
            "creation_time" : "<some date:time format>"
          }
        ]
        """
        # userid = request.data.get('id')
        data = []
        userid = id

        try:
            user = User.objects.get(id=userid)
        except User.DoesNotExist:
            return Response({"MSG": "User with this ID does not exist"}, status=status.HTTP_404_NOT_FOUND)

        for team in Team.objects.all():
            if user in team.users.all():
                data.append(team.id)

        teams = Team.objects.filter(id__in=data)
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)



