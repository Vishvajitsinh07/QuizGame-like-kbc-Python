import random
import time

def print_options(options):
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")

def ask_question(question, options, correct_answer, hint=None):
    random.shuffle(options)  # Shuffle the options
    print(f"\n{question}")
    print_options(options)

    if hint:
        print(f"\nHint: {hint}")

    user_answer = input("Your answer (1/2/3/4 or type 'quit' to end the game): ").lower()

    if user_answer == 'quit':
        return False, 0

    if user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
        if options[int(user_answer) - 1].lower() == correct_answer.lower():
            print("Correct answer!")
            return True, 10000
        else:
            print(f"Wrong answer! The correct answer is: {correct_answer}.")
            return False, 0
    elif user_answer.lower() == correct_answer.lower():
        print("Correct answer!")
        return True, 10000
    else:
        print(f"Wrong answer! The correct answer is: {correct_answer}.")
        return False, 0

def use_timer(options, correct_answer):
    time_limit = 60
    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < time_limit:
        answer = input(f"(You have {time_limit - int(elapsed_time)} seconds left): ")

        elapsed_time = time.time() - start_time

        if answer.lower() == 'quit':
            return False, 0

        if answer.isdigit() and 1 <= int(answer) <= len(options):
            if options[int(answer) - 1].lower() == correct_answer.lower():
                print("Correct answer!")
                return True, 10000
            else:
                print(f"Wrong answer! The correct answer is: {correct_answer}.")
                return False, 0
        elif answer.lower() == correct_answer.lower():
            print("Correct answer!")
            return True, 10000
        else:
            print(f"Invalid input! You have {time_limit - int(elapsed_time)} seconds left.")

    print(f"Time's up! The correct answer is: {correct_answer}.")
    return False, 0

def save_score(name, age, score):
    with open('leaderboard.txt', 'a') as file:
        file.write(f"Name: {name}, Age: {age}, Score: {score} rupees\n")
    print("Your score has been saved to the leaderboard.")

def play_game(interest):
    while True:
        name = input("Enter your name: ")
        if not name.isalpha():
            print("Invalid name! Name should only contain alphabets.")
        else:
            break

    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid age! Please enter a valid integer.")

    questions = {
        '1': cricket_questions.copy(),
        '2': kabaddi_questions.copy(),
        '3': movie_questions.copy(),
        '4': general_knowledge_questions.copy(),
    }

    if interest in questions:
        selected_questions = questions[interest]
    else:
        print("Invalid interest. Please choose again.")
        return

    total_questions = 10
    money = 1000
    streak_count = 0
    random.shuffle(selected_questions)

    for i in range(total_questions):
        question, options, correct_answer, hint = selected_questions.pop()
        print(f"\nQuestion {i + 1}:")
        print(f"{question}")
        print_options(options)

        correct, earned = use_timer(options, correct_answer)
        money += earned

        if not correct:
            print(f"\nGame over! You earned {money} rupees.")
            save_score(name, age, money)
            return

        streak_count += 1
        if streak_count == 5:
            print(f"Bonus! You've answered 5 questions correctly in a row. You earn an additional 15,000 rupees.")
            money += 15000
            streak_count = 0

    if streak_count == 0 and earned == 10000:
        print(f"Congratulations! You answered all the questions correctly.")
        money += 1000000
        print(f"You win {money} rupees plus a bonus of 100,000 rupees!")

    print(f"\nFinal score: {money} rupees.")
    save_score(name, age, money)

cricket_questions = [
    ("Who is the current captain of the Indian cricket team?", ["Virat Kohli", "Rohit Sharma", "Ajinkya Rahane", "KL Rahul"], "Rohit Sharma", "He is a prominent batsman."),
    ("Which team won the ICC Cricket World Cup 2023?", ["England", "New Zealand", "India", "Australia"], "India", "India won the ICC World Cup in 2023."),
    ("Who holds the record for the highest individual score in Test cricket?", ["Brian Lara", "Sachin Tendulkar", "Virender Sehwag", "Chris Gayle"], "Brian Lara", "He scored 400* in a single innings."),
    ("Who is the highest run-scorer in T20 internationals?", ["Virat Kohli", "Chris Gayle", "AB de Villiers", "Rohit Sharma"], "Virat Kohli", "He is also the highest in ODI cricket."),
    ("Which country is known as the birthplace of cricket?", ["India", "Australia", "England", "South Africa"], "England", "The first international cricket match was played there."),
    ("Which Indian cricketer holds the record for the fastest century in ODIs?", ["Virat Kohli", "Rohit Sharma", "Shikhar Dhawan", "MS Dhoni"], "Virat Kohli", "He scored a century in 52 balls."),
    ("Who is the only cricketer to have scored a double century in every format?", ["Chris Gayle", "David Warner", "Shikhar Dhawan", "Rohit Sharma"], "Rohit Sharma", "He has scored 3 double centuries."),
    ("Which Indian cricketer is known as 'The Wall'?", ["Virender Sehwag", "Rahul Dravid", "Sourav Ganguly", "VVS Laxman"], "Rahul Dravid", "He was known for his defensive batting."),
    ("Who won the IPL 2020 title?", ["Mumbai Indians", "Delhi Capitals", "Sunrisers Hyderabad", "Royal Challengers Bangalore"], "Mumbai Indians", "They won their fifth title."),
    ("Who is the first cricketer to score a century in all formats of international cricket?", ["Shikhar Dhawan", "Chris Gayle", "Rohit Sharma", "David Warner"], "Chris Gayle", "He is a West Indian cricketer."),
]

kabaddi_questions = [
    ("Which team has won the most Pro Kabaddi League titles?", ["Patna Pirates", "Bengaluru Bulls", "U Mumba", "Jaipur Pink Panthers"], "Patna Pirates", "They have won 3 times."),
    ("Who is known as the 'Record Breaker' in the sport of kabaddi?", ["Pardeep Narwal", "Rahul Chaudhari", "Pawan Sehrawat", "Deepak Niwas Hooda"], "Pardeep Narwal", "He holds the record for most points in a season."),
    ("Who was the captain of the Indian kabaddi team that won the gold medal in the 2018 Asian Games?", ["Ajay Thakur", "Rahul Chaudhari", "Anup Kumar", "Manjeet Chhillar"], "Ajay Thakur", "He led the team to victory in Jakarta."),
    ("Which country won the 2016 Kabaddi World Cup?", ["India", "Iran", "Pakistan", "Sri Lanka"], "India", "India defeated Iran in the final."),
    ("In which year did Pro Kabaddi League start?", ["2014", "2013", "2015", "2016"], "2014", "The league was launched in 2014."),
    ("Which team won the inaugural season of Pro Kabaddi?", ["Jaipur Pink Panthers", "Patna Pirates", "U Mumba", "Bengaluru Bulls"], "Jaipur Pink Panthers", "They won the first title in 2014."),
    ("Which team has the most successful raid points in Pro Kabaddi?", ["Pardeep Narwal", "Rahul Chaudhari", "Anup Kumar", "Pawan Sehrawat"], "Pardeep Narwal", "He is a kabaddi star."),
    ("Who is the first female kabaddi player to receive the Padma Shri award?", ["Kiran Choudhary", "Tejaswini Sawant", "Geeta Phogat", "Anjali Raut"], "Kiran Choudhary", "She received this award in 2020."),
    ("Who was the first to score 1000 points in Pro Kabaddi League?", ["Pardeep Narwal", "Rahul Chaudhari", "Pawan Sehrawat", "Ajay Thakur"], "Pardeep Narwal", "He achieved this feat."),
    ("Who is the highest scorer in Pro Kabaddi League's history?", ["Pardeep Narwal", "Rahul Chaudhari", "Pawan Sehrawat", "Deepak Niwas Hooda"], "Pardeep Narwal", "He is known as 'Record Breaker.'"),
]

movie_questions = [
    ("Which 2023 movie featured Ranbir Kapoor?", ["Animal", "Brahmastra", "Sanju", "Arjun"], "Animal", "Directed by Sandeep Reddy Vanga."),
    ("Which movie starred both Brad Pitt and Leonardo DiCaprio?", ["Once Upon a Time in Hollywood", "Titanic", "Inglourious Basterds", "The Revenant"], "Once Upon a Time in Hollywood", "Directed by Quentin Tarantino."),
    ("Which movie won the Best Picture Oscar in 2023?", ["Everything Everywhere All at Once", "The Fabelmans", "Top Gun: Maverick", "Avatar: The Way of Water"], "Everything Everywhere All at Once", "It was a surprising win at the Oscars."),
    ("Who directed the movie 'Inception'?", ["Christopher Nolan", "Steven Spielberg", "James Cameron", "Quentin Tarantino"], "Christopher Nolan", "Known for his mind-bending films."),
    ("Which animated film series features a character called Shrek?", ["Shrek", "Toy Story", "Finding Nemo", "Frozen"], "Shrek", "A green ogre with a heart of gold."),
    ("Which movie features the famous line 'I’ll be back'?", ["The Terminator", "The Matrix", "Die Hard", "Predator"], "The Terminator", "It starred Arnold Schwarzenegger."),
    ("Which actor won the Academy Award for Best Actor in 2020?", ["Joaquin Phoenix", "Leonardo DiCaprio", "Brad Pitt", "Matthew McConaughey"], "Joaquin Phoenix", "He won for 'Joker.'"),
    ("Which movie was the first in the Marvel Cinematic Universe?", ["Iron Man", "The Incredible Hulk", "Thor", "Captain America"], "Iron Man", "Released in 2008, launching the MCU."),
    ("Who is the lead actor in the movie 'Deadpool'?", ["Ryan Reynolds", "Hugh Jackman", "Chris Hemsworth", "Tom Holland"], "Ryan Reynolds", "He plays the title role."),
    ("Which film was the highest-grossing of all time until 2021?", ["Avatar", "Avengers: Endgame", "Titanic", "Star Wars"], "Avatar", "Directed by James Cameron."),
]

general_knowledge_questions = [
    ("Who wrote 'The Odyssey'?", ["Homer", "Shakespeare", "Dickens", "Austen"], "Homer", "An ancient Greek poet."),
    ("Which planet is closest to the sun?", ["Venus", "Earth", "Mercury", "Mars"], "Mercury", "It is the smallest planet in our solar system."),
    ("In which year did the Titanic sink?", ["1912", "1905", "1914", "1920"], "1912", "It sank on its maiden voyage."),
    ("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"], "Leonardo da Vinci", "A famous Renaissance artist."),
    ("Which is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "Pacific Ocean", "It covers more area than all other oceans combined."),
    ("Which city is known as the 'Big Apple'?", ["Los Angeles", "Chicago", "New York City", "San Francisco"], "New York City", "It is famous for its skyline."),
    ("Which country is the largest by area?", ["Russia", "Canada", "United States", "China"], "Russia", "It spans Europe and Asia."),
    ("Which is the tallest mountain in the world?", ["Mount Everest", "K2", "Kangchenjunga", "Mount Kilimanjaro"], "Mount Everest", "Located in the Himalayas."),
    ("Which animal is known as the 'King of the Jungle'?", ["Lion", "Elephant", "Tiger", "Bear"], "Lion", "It is a symbol of strength."),
    ("What is the longest river in the world?", ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"], "Amazon River", "It flows through South America."),
]

def main():
    print("------------------------------")
    print("Welcome to KBC Quiz Game!")
    print("------------------------------")
    interest = input(
        "Choose your interest: 1. Cricket 2. Kabaddi 3. Movies 4. General Knowledge\n")
    play_game(interest)

main()
