from models import Base, engine, session
from models.User import User
from models.Team import Team
from models.Member import Member

Base.metadata.create_all(engine)

# User and team creation
user_in_team = User(name='team mate', email='user@in.team')
user_without_team = User(name='alone', email='user@without.team')

team = Team()

user_in_team.teams.append(team)

session.add(user_in_team)
session.add(user_without_team)
session.add(team)
session.commit()

# Display all users
for user in session.query(User).all():
    print('{} - name : {} - email : {}'.format(user.id, user.name, user.email))
    for team in user.teams:
        print('Team of user {} - team_id : {}'.format(user.id, team.id))

# Display all teams
for team in session.query(Team).all():
    print('team id : {}'.format(team.id))
    for member in team.members:
        print('User n°{} - name : {} - email : {}'.format(member.id, member.name, member.email))
