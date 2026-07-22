from rabbit_turtle import race_run, result
def main():
    rabbit_text, turtle_text, winner = race_run()
    result(rabbit_text, turtle_text, winner)

if __name__ == "__main__":
    main()
