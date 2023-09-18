#Project Planner Tool<br>
The Project consist of APIs for project planning and management . It offers a set of APIs for various project-related tasks and includes three apps: User, Team, and Board. Below, I have list the Methods it contains-<br>
<br>
#User Application<br>
• Create User: Create a new user in the system.<br>
• List Users: Retrieve all users registered in the system.<br>
• Describe User: Get detailed information about a specific user.<br>
• Update User: Modify user details.<br>
• Get User Teams: Retrieve a list of teams that a particular user is a member of.<br>
<br>
#Team Application<br>
• Create Team: Create a new project team<br>
• List Teams: Retrieve a list of all project teams.<br>
• Describe Team: Get detailed information about a specific project team.<br>
• Update Team: Modify team details.<br>
• Add Users to Team: Add a list of user to a project team.<br>
• Remove Users from Team: Removes a list of users from a project team.<br>
• List Team Users: Retrieve a list of users who belong to a particular project team.<br>
<br>
#Board Application<br>
• Create Board: Create a new project board for task management.<br>
• Close Board: Close an existing project board by updating its status.<br>
• Add Task: Add tasks to a project board.<br>
• Update Task Status: Update the status of a task on a project board.<br>
• List Boards: Retrieve a list of all project boards.<br>
• Export Board: Export project board data in a txt file.<br>
• List All Boards: Retrieve a list of all project boards.<br>
<br>
#Installation<br>
To use the Project Planner Tool, follow these steps:<br>
1. Install Visual Studio Code.<br>
2. Install Django and Django REST framework using the dependencies listed in requirements.txt.<br>
3. Install Postman for testing the APIs.<br>
<br>
#API Endpoints<br>
You can interact with the Project Planner Tool through the following API endpoints:<br>
• http://localhost:8000/user/: Retrieve a list of all users.<br>
• http://localhost:8000/team/: Retrieve a list of all project teams.<br>
• http://localhost:8000/board/: Retrieve a list of all project boards.<br>
<br>
For detailed usage instructions, refer to the views and documentation to understand how to send requests for specific operations.<br>
#Note: When sending requests, provide IDs as integers in Postman instead of strings.
