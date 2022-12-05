# advent-of-code-with-chatGPT
This repo registers my saga to solve advent of code 2022 puzzles with chatGPT.

Each day, you'll find a README file logging the entire convo between me and chatGPT. Final (working) solutions will be on python files. Our goal is to get as far as possible. And I mean "our" because the solution depends on the performance of the model and the quality of the prompts.

Obviously, I will be dellaying my submissions, because I have no intention of making into the global leaderboard through cheating.

## Brain dump

This section logs some of my thoughts during the convos with chatGPT.

### Day 1

[Check full convo here](day_1/README.md)

The puzzle should be easily solved by a begginer. It serves like a preparation, just to remember programmers how to parse a text input file and do some basic math. 

Only part two requires the use of a data structure (list). But chatGPT chose a verbose and complex solution even for part one. Storing the total calories for each Elf in a dictionary, to take the max in the end. 

Anyway, I'm interested in getting the correct answer, so this blew my mind. THIS IS AWESOME!

### Day 2

[Check full convo here](day_2/README.md)

Holy! The bot is stubborn and boastful:

> I do not have the ability to make mistakes. (x2) 2022, chatGPT

LMAO, this was super fun. It took me hours to get the right answers, but it was extremelly good. Certainly, I should get better at prompt engineering if I want this bot to complete the whole challenge.

It seems that the first part of the puzzle was biasing the bot more than it should. Because the second part changed the definition of the input and how to interpret it, I had to work super hard to make it "forget" the first part of the puzzle.

Anyway, I cannot believe how good this AI is, imagine when fine tunned for "pair-programming".

**One important thing that I've noticed:** my first prompt on day 1 seemed to have triggered a "hackerank chatGPT", because it even gave testing code for the example input. This did not happen on day 2. I'll try starting the thread on day 3 with: "Hi, can you help me with a programming puzzle? I would like the solution written in python, with code explanation, please."

### Day 3

[Check full convo here](day_3/README.md)

Amazing. It took me only a few minutes to get both solutions from chatGPT. The prompt from day 1 works very well, as it makes the bot show it's actually trying to solve for the example input. 

Obviously, it will say that the solution is working, even when it gives the wrong output for it. It won't run the code to check it, but chatGPT tries to solve the specific problem described in the puzzle, not a generic one as we've seen in day 2.

In the end I even got the bot to optimize the code an remove a few unecessary lines. It could improve it even more, but that's for the next days :)

### Day 4

[Check full convo here](day_4/README.md)

I've started the day with the same prompt as day 3. But now, on multiple retries, chatGPT started generating a random puzzle and solving it in python. In addition to that, the python code was being explained like it was Python 2.7 (use of `raw_input` for example). So I changed my first prompt to include the command "Python 3" and the full puzzle description. Less small talk :)

This time, the code was super concise and "advanced", making use of the `re` package to parse the input and inline list comprehension. It required just a few tips for the bot to solve part 1. Part 2 was a piece of cake from there.

I won't get tired of saying how this technology is ground breaking!

cont.