# Create a quiz game. Make an HTTP request to the Open Trivia API at each round of the game to get a new question
# At the end of each round ask the user if they want to play again. Keep playing until they type "quit"
# Keep track of the users score! X right out of Y rounds.

import requests, json, random, pprint

exit_game = ""
while (exit_game != "quit"):

    right = 0;
    total = 0;

    request = requests.get("https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple")
    # dictionary, two keys, key : integer, key : list, list has one index, it's a dictionary, dictionary["name of key"]
    request_json = json.loads(request.text)

    pprint.pprint(request_json)

    print("The category of this question is", (request_json["results"][0]["category"]).lower())
    print("")
    print(request_json["results"][0]["question"])

    options = request_json["results"][0]["incorrect_answers"]
    options.append(request_json["results"][0]["correct_answer"])
    random.shuffle(options)

    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])

    exit_game = input("Do you want to play again? Type 'quit' to quit. ")

print(f"Your score is {right} out of {total}.")