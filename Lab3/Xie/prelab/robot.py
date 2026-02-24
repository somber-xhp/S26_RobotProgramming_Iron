class Robot:
    def __init__(self, robot_id, status=True, location="A1"):
        self.id_number = robot_id
        self.status = status  # True = online, False = offline
        self.location = location

    def moveBot(self, new_location):
        self.location = new_location

    def changeStatus(self):
        self.status = not self.status

    def __str__(self):
        status_text = "online" if self.status else "offline"
        return f"Robot(ID={self.id_number}, status={status_text}, location={self.location})"
