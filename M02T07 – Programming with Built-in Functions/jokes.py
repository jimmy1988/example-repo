#Import the random module
import random

#Declare a list of jokes and punchlines, each individual item is a dictionary
jokes = [
    {
        "joke": "Why don't scientists trust atoms?",
        "punchline": "Because they make up everything!"
    },
    {
        "joke": "Why did the scarecrow win an award?",
        "punchline": "Because he was outstanding in his field!"
    },
    {
        "joke": "Why don't skeletons fight each other?",
        "punchline": "They don't have the guts."
    },
    {
        "joke": "What do you call a fake noodle?",
        "punchline": "An impasta!"
    },
    {
        "joke": "Why did the bicycle fall over?",
        "punchline": "Because it was two-tired!"
    },
    {
        "joke": "What do you call a bear with no teeth?",
        "punchline": "A gummy bear!"
    },
    {
        "joke": "Why can't your nose be 12 inches long?",
        "punchline": "Because then it would be a foot!"
    },
    {
        "joke": "What do you call cheese that isn't yours?",
        "punchline": "Nacho cheese!"
    },
    {
        "joke": "Why did the golfer bring two pairs of pants?",
        "punchline": "In case he got a hole in one!"
    },
    {
        "joke": "How does a penguin build its house?",
        "punchline": "Igloos it together!"
    }
]

#randomly select a joke
joke = random.choice(jokes)
print(joke.get("joke")) #output the main joke to the console