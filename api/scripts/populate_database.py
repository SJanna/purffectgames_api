import os
import django
from django.utils import timezone
from random import randint, choice
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'purffectgames_api.settings')  # Replace 'your_project_name' with your actual project name
django.setup()

from api.models import Client, Game, Rental  # Replace 'your_app' with your actual app name

fake = Faker()

# Populate Client model
def populate_clients(num_clients):
    for _ in range(num_clients):
        client = Client(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            identification_type=choice(['DNI', 'NIE', 'Passport']),
            identification_number=fake.random_number(digits=10),
            phone=fake.phone_number(),
            email=fake.email(),
            birth_date=fake.date_of_birth(),
            address=fake.street_address(),
            city=fake.city(),
            state=fake.state(),
            zip=fake.zipcode(),
        )
        client.save()

# Populate Game model
def populate_games(num_games):
    for _ in range(num_games):
        game = Game(
            title=' '.join(fake.words(nb=randint(1,5), unique=True)).title(),
            price=fake.random_number(digits=2),
            stock=randint(1, 10),
            image='https://source.unsplash.com/random?Videogame ' + fake.word(),
            release_date=fake.date_this_decade(),
            protagonist=fake.name(),
            director=fake.name(),
            productor=fake.name(),
            platform=choice(['PlayStation 2', 'Nintendo DS', 'Game Boy/Game Boy Color', 'PlayStation 4', 'Nintendo Switch', 'PlayStation', 'Nintendo Wii', 
                                'PlayStation 3', 'Xbox 360', 'Nintendo Entertainment System', 'Xbox One', 'Game Boy Advance', 'PlayStation Portable',
                                  'Nintendo 3DS', 'PlayStation 5', 'Xbox Series X/S', 'Nintendo GameCube', 'Xbox', 'Atari 2600', 'Sega Genesis']),

            popularity=fake.pyfloat(left_digits=2, right_digits=2, positive=True),
        
            genre=choice(['Action', 'Adventure', 'Role-playing', 'Simulation', 'Strategy', 'Sports', 'Puzzle', 'Idle', 'Arcade', 'Racing', 'Fighting', 'Shooter',
                            'Survival', 'Horror', 'Platformer', 'Stealth', 'Battle Royale', 'MMO', 'Sandbox', 'Open World', 'Rhythm', 'Educational', 'Trivia', 'Board',
                            'Card', 'Casual', 'Party', 'Music', 'Programming', 'Visual Novel', 'Dating Sim', 'Text Adventure', 'Interactive Movie', 'Tower Defense', 
                            'Metroidvania', 'Pinball', 'Roguelike', 'Roguelite', 'Tactical', 'Turn-based', 'Real-time', 'Real-time Strategy', 'Real-time Tactics',
                            'Multiplayer Online Battle Arena', 'Massively Multiplayer Online', 'First-person Shooter', 'Third-person Shooter',
                            'Hero Shooter', 'Light Gun', 'Dance', 'Fitness', 'Exergame', 'Augmented Reality', 'Virtual Reality',
                            'Artillery', 'Vehicular Combat', 'Flight Simulation', 'Train Simulation', 'Life Simulation', 'Construction and Management Simulation',
                            'Vehicle Simulation', 'Business Simulation', 'God Game', 'Social Simulation', 'City-building', 'Government Simulation', 'Art Game', 'Indie',
                            'Non-game', 'Christian Game', 'Electronic Sports', 'Esports', 'Competitive', 'Sports-based Fighting',
                            'Turn-based Strategy', 'Turn-based Tactics', 'Grand Strategy', '4X', 'Wargame'])
          )
        game.save()

# Populate Rental model
def populate_rentals(num_rentals, num_clients, num_games):
    for _ in range(num_rentals):
        rental = Rental(
            client=Client.objects.get(pk=randint(1, num_clients)),
            rental_date=fake.date_this_decade(),
            rental_deadline=fake.date_between(start_date=timezone.now(), end_date='+30d'),
            price=fake.random_number(digits=2)
        )
        rental.save()

        games_to_add = Game.objects.filter(pk__in=[randint(1, num_games), randint(1, num_games)])
        rental.games.set(games_to_add)

def run():
    num_clients = 20  # Adjust the number of clients as needed
    num_games = 150  # Adjust the number of games as needed
    num_rentals = 30  # Adjust the number of rentals as needed

    populate_clients(num_clients)
    populate_games(num_games)
    populate_rentals(num_rentals, num_clients, num_games)

    print("Database populated successfully!")
