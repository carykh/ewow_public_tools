# ewow_public_tools
Various tools for EWOW! (like word counter)

# Word Counter
Here's how to count how many words are in your EWOW response.
* Download this repo
* Open a command prompt from this project folder
* Run this command:
  ```
  python get_word_count.py "How many words is this response?"
  ```
* This should return this result:
   ```
  That response is 6 words.
  ```
## Thoughts
* This is exactly the same Python function that we use to draw the blue word counter in the actual voting videos, so in theory, this counter should match the EWOW videos exactly. Still, try not to skirt the rules.
* Now you'll know the word count for weird edge cases like the one below!
 ```
  python get_word_count.py "CatBat - ? 456 two-words two words ### Try.to.cheat BLAH"\
  That response is 7 words.
  ```
* If EWOWers try to skirt the rules like the response above, and the voting videos claim it has "11 words" when it really looks like 20, I'm calling on voters to have some common sense and vote that response down for not being honest!
