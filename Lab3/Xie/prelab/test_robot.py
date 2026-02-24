from robot import Robot

def main():
    bot = Robot(robot_id=101, status=True, location="A3")
    print("Initial:", bot)

    bot.moveBot("B2")
    print("After moveBot:", bot)

    bot.changeStatus()
    print("After changeStatus:", bot)

    bot.changeStatus()
    bot.moveBot("C5")
    print("Final:", bot)

if __name__ == "__main__":
    main()
