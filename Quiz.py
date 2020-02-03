# Create a quiz game. Make an HTTP request to the Open Trivia API at each round of the game to get a new question
# At the end of each round ask the user if they want to play again. Keep playing until they type "quit"
# Keep track of the users score! X right out of Y rounds.
# python3 -m pip install [packages]

import requests, json, pprint, random, html

url = "https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple"
end_game = ""
right = 0
total = 0

while (end_game != "quit"):

    request = requests.get(url)

    if (request.status_code != 200):
        end_game = input("There was a problem retrieving the question. Please press enter to try again, or press 'quit' to exit the game. ")

    else:
        # this is a dictionary with two keys, response_code : int, and results: list
        # results is a list, where index 0 is all the data in a dictionary (there is only one index anyways lol)
        # to get what we want, we do dictionary["key"][index of the list]["dictionary key again]
        # tldr, dictionary --> list --> dictionary, key, index, key.
        data = json.loads(request.text)
        question = data["results"][0]["question"]
        answers = data["results"][0]["incorrect_answers"]           # this is a list
        correct_answer = data["results"][0]["correct_answer"]
        answers.append(correct_answer)
        random.shuffle(answers)                                     # shuffled answers
        answer_number = 1

        print(html.unescape(question) + "\n")                       # html module to print questions properly

        for answer in answers:
            print(str(answer_number) + " - " + html.unescape(answer))
            answer_number += 1

        user_answer = input("\nType 1, 2, 3, or 4. ")
        user_answer = answers[int(user_answer)-1]                   # if user enters "1" we get index "0". now check to see if it's right

        if (user_answer == correct_answer):
            print("You got it right! The correct answer was", html.unescape(correct_answer))
            right += 1
        else:
            print("You got it wrong! The correct answer was", html.unescape(correct_answer))

        total += 1
        end_game = input("Do you want to play again? Press enter to play again, or quit to end. \n").lower()

print(f"Thanks for playing! You got {right} out of {total} games correct.")

# should really do data validation but I'll do that later, just validating data type and if it's in range
# if type(...) != int then ...
# if user_input < 0 or > 4 then ...