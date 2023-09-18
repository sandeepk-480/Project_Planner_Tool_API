from board.serializers import TaskSerializer, BoardGetSerializer, BoardPostSerializer, BoardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from board.models import Board,Task
from team.models import Team
import os
from django.conf import settings
from datetime import datetime



class ProjectBoardBase(APIView):
    """
    A project board is a unit of delivery for a project. Each board will have a set of tasks assigned to a team.
    """
    def post(self,request):
        if len(request.data)==3:
            return self.create_board(request)
        elif len(request.data)==1:
            return self.export_board(request)
        else:
            return self.add_task(request)
    
    def get(self,request):
        if request.data: 
            return self.list_boards(request)
        else:
            return self.list_all_boards(request)

    def patch(self,request):
        if len(request.data)==2:
            return self.update_task_status(request)
        else:
            return self.close_board(request)
    


    # create a board
    def create_board(self, request: str):
        """
        :param request: A json string with the board details.
        {
          "name" : "<board_name>",
          "description" : "<description>",
          "team_id" : "<team_id>"
        }
        :return: A json string with the response {"id" : "<board_id>"}


        Constraint:
         * board name must be unique for a team
         * board name can be max 64 characters
         * description can be max 128 characters
         * must have creation time for the board
        """
        data = request.data
        serializer = BoardPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Team_id": request.data.get('team_id')}, status=status.HTTP_200_OK)
        return Response(serializer.errors)


    # close a board
    def close_board(self, request: str) -> str:
        """
        :param request: A json string with the board identifier
        {
          "id" : "<board_id>"
        }

        :return:

        Constraint:
          * Set the board status to CLOSED and record the end_time date:time
          * You can only close boards with all tasks marked as COMPLETE
        """
        data = request.data.get('id')
        try:
            board = Board.objects.get(id=data)
        except Board.DoesNotExist:
            return Response({"MSG": "Board with this ID Does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        tasks = Task.objects.filter(board_id=board)
        for i in tasks:
            if i.status != "COMPLETE":
                return Response({"MSG":"All Task Should be Completed"})
        
        board.status = 'CLOSED'
        board.save()
        return Response({"MSG": "Board status updated"}, status=status.HTTP_200_OK)


    # add task to board
    def add_task(self, request: str) -> str:
        """
        :param request: A json string with the task details. Task is assigned to a team_id who works on the task
        {
          "board_id" : "<board_id>",
          "title" : "<task_name>",
          "description" : "<description>",
          "team_id" : "<team_id>",
          "status": "OPEN" | "IN_PROGRESS" | "COMPLETE",
          "creation_time" : "<date:time when task was created>"
        }
        :return: A json string with the response {"id" : "<task_id>"}

        Constraints:
         * task title must be unique for a board
         * title name can be max 64 characters
         * description can be max 128 characters
         * Can only add task to an OPEN board
        """
        data = request.data
        serializer = TaskSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            board = Board.objects.get(id=data['board_id'])
            
        except Board.DoesNotExist:
            # print(data['board_id'])
            return Response({"MSG": "Board with this ID does not exist"})
        
        if board.status == "OPEN":
            task = serializer.save()
            return Response({"id": task.id}, status=status.HTTP_200_OK)
        else:
            return Response({"MSG": "Can only add Task to OPEN Board"})
        
            

    # update the status of a task
    def update_task_status(self, request: str):
        """
        :param request: A json string with the task details
        {
          "id" : "<task_id>",
          "status" : "OPEN" | "IN_PROGRESS" | "COMPLETE"
        }
        """
        data = request.data
        try:
            task = Task.objects.get(id=data['id'])
        except Task.DoesNotExist:
            return Response({"MSG": "Task with this name does not exist"})
        
        task.status = data['status']
        task.save()
        return Response({"MSG": "Task Status Updated"}, status=status.HTTP_200_OK)
        

    # list all open boards for a team
    def list_boards(self, request: str) -> str:
        """
        :param request: A json string with the team identifier
        {
          "id" : "<team_id>"
        }

        :return:
        [
          {
            "id" : "<board_id>",
            "name" : "<board_name>"
          }
        ]
        """
        try:
            teamid = request.data.get('id')
            team = Team.objects.get(id=teamid)
            b = []
            board = Board.objects.filter(team_id=team)
            for boardd in board:
                if boardd.status=="OPEN":
                    b.append(boardd)
                else:
                    continue

            serializer = BoardGetSerializer(b, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Team.DoesNotExist:
            return Response({"MSG": "Team with this ID does not exist"}, status=status.HTTP_404_NOT_FOUND)


    def export_board(self, request: str) -> str:
        """
        Export a board in the out folder. The output will be a txt file.
        We want you to be creative. Output a presentable view of the board and its tasks with the available data.
        :param request:
        {
          "id" : "<board_id>"
        }
        :return:
        {
          "out_file" : "<name of the file created>"
        }
        """
        board_id = request.data.get('id')
        try:
            board = Board.objects.get(id=board_id)
        except Board.DoesNotExist:
            return Response({"MSG": "Board with this ID does not exist"}, status=status.HTTP_404_NOT_FOUND)

        tasks = Task.objects.filter(board_id=board)

        
        timestamp = datetime.now().strftime("%Y%m%d%H%M")
        filename = f"board_{board.name}_{timestamp}.txt"
        filepath = os.path.join(settings.MEDIA_ROOT, filename)


        with open(filepath, 'w') as file:
            file.write(f"Board Name: {board.name}\n")
            file.write(f"Description: {board.desc}\n")
            file.write(f"Status: {board.status}\n")
            file.write("Tasks:\n")

            for task in tasks:
                file.write(f"- Task Title: {task.title}\n")
                file.write(f"  Description: {task.desc}\n")
                file.write(f"  Status: {task.status}\n")
                file.write(f"  Creation Time: {task.creation_time}\n")

        # Return the name of the created text file
        return Response({"out_file": filename}, status=status.HTTP_200_OK)

    def list_all_boards(self, request=None):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data) 