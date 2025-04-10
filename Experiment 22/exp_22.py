class Event:
    """Represents an event with details like name, date, venue, and activities."""
   
    def __init__(self, name, date, venue):
        self.name = name
        self.date = date
        self.venue = venue
        self.organizers = []  # List to store organizers
        self.participants = []  # List to store participants
        self.activities = []  # List to store event activities

    def add_organizer(self, organizer):
        """Assigns an organizer to the event."""
        self.organizers.append(organizer)

    def add_participant(self, participant):
        """Registers a participant for the event."""
        self.participants.append(participant)

    def add_activity(self, activity):
        """Adds an activity to the event."""
        self.activities.append(activity)

    def display_event_details(self):
        """Displays event details including organizers, participants, and activities."""
        print(f"\nEvent: {self.name}")
        print(f"Date: {self.date}, Venue: {self.venue}")
        print("\nOrganizers:")
        for organizer in self.organizers:
            print(f"- {organizer.name} ({organizer.role})")
       
        print("\nParticipants:")
        for participant in self.participants:
            print(f"- {participant.name} (Age: {participant.age})")
       
        print("\nActivities:")
        for activity in self.activities:
            print(f"- {activity.name} (Time: {activity.time})")

class Organizer:
    """Represents an organizer who manages the event."""
   
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Participant:
    """Represents a participant who registers for an event."""
   
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Activity:
    """Represents an activity that takes place in an event."""
   
    def __init__(self, name, time):
        self.name = name
        self.time = time

# ------------------------------- DEMO USAGE -------------------------------

# Creating an event
college_fest = Event("TechFest 2025", "10th April 2025", "College Auditorium")

# Creating organizers
organizer1 = Organizer("Alice", "Event Coordinator")
organizer2 = Organizer("Bob", "Logistics Manager")

# Adding organizers to the event
college_fest.add_organizer(organizer1)
college_fest.add_organizer(organizer2)

# Creating participants
participant1 = Participant("Charlie", 20)
participant2 = Participant("Daisy", 22)

# Registering participants
college_fest.add_participant(participant1)
college_fest.add_participant(participant2)

# Creating activities
activity1 = Activity("Coding Competition", "10:00 AM")
activity2 = Activity("Music Concert", "5:00 PM")

# Adding activities
college_fest.add_activity(activity1)
college_fest.add_activity(activity2)

# Displaying event details
college_fest.display_event_details()
