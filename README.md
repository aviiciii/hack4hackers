# HackPortal - Hackathon Management Portal

***HackPortal*** is a web application built for managing hackathons, providing a platform for both hackers and organizers. This portal allows ***hackers*** to *register for the hackathon, access information about the event, view sponsors, announcements, and submit queries* to the organizers. ***Organizers*** have *superuser privileges*, enabling them to *manage the number of attendees, make announcements, and respond to hacker queries*.

## Features


*Hacker Login and Registration:*
*Hackers can log in using their unique team name and password.*
*New hackers can register for the hackathon by providing their team name, team members' names, password, and email.*

*Hackathon Information:*
Hackers can view details about the hackathon, including the schedule and sponsors.

*Announcements and Queries:*
Organizers can make announcements to all hackers through the portal.
Hackers can submit queries to the organizers, and organizers can provide necessary information or assistance.

*Attendee Management:*
Organizers have the ability to view and modify the number of hackers attending the hackathon.

***Installation and Setup***
 
-Clone the repository: git clone https://github.com/your-username/hackportal.git

-Navigate to the project directory: cd hackportal

-Create a virtual environment: python -m venv venv

-Activate the virtual environment:

-On Windows: venv\Scripts\activate

-On macOS/Linux: source venv/bin/activate

-Install the required dependencies: pip install -r requirements.txt

-Run the Django migrations: python manage.py migrate

-Create a superuser for organizer access: python manage.py createsuperuser

-Start the development server: python manage.py runserver

-Access the portal at http://127.0.0.1:8000/

-Technologies Used

-Django: Web framework for backend development.

-HTML/CSS/JavaScript: Frontend development for user interfaces.

-CockroachDB: Database for storing hackathon information and user data.

***Contributing***
-We welcome contributions to HackPortal! If you find any bugs or have ideas for new features, please feel free to open an issue or submit a pull request.

***License***
-This project is licensed under the MIT License - see the LICENSE file for details.

***Acknowledgments***
-We would like to thank all the contributors and the hackathon community for their support and feedback, which helped make this project a success. Happy hacking!

