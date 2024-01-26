# Samuel Nerayo
# CPSC-3400 -02 - HW1 - Finding Words Ladder

"""
From a given starting word, finding the shortest "ladder"
of single letter changes which leads to some final word,
where each intermediate state is also another word.
"""

import string
from collections import deque
import time


# Function that finds adjacent words
def adjacent_words(word, word_set):
    adj_words = set()

    # Looping over each position in the word
    for i in range(len(word)):
        for char in string.ascii_lowercase:  # Each lowercase letter in the alphabet
            # Creating a new word by replacing the character at position 'i' with 'char'
            new_word = word[:i] + char + word[
                                         i + 1:]

            # Check for equality in word_set with the original word
            if new_word in word_set and new_word != word:
                adj_words.add(new_word)  # Adding the word to the set if valid

    return adj_words


# Function to find word-ladder using BFS from start to end
def find_ladder(start, target, word_set):
    queue = deque([{start: [start]}])  # Using deque from the collection library
    used_words = set()  # Tracking used words

    while queue:  # Loop until the queue is empty
        curr_state = queue.popleft()  # Get the current state from the queue

        # Extracting current word and path from the current state
        curr_word = next(iter(curr_state))
        curr_path = curr_state[curr_word]

        # Checking if curr_word is equal to the target word
        if curr_word == target:
            return curr_path

        # Check if the curr_word was visited
        if curr_word not in used_words:
            used_words.add(curr_word)
            # Get the adjacent words function for the curr_word and sort them
            adj_words = adjacent_words(curr_word, word_set)

            for adj_word in adj_words:
                if adj_word not in used_words:
                    new_path = curr_path + [adj_word]  # Create a new list for the updated path
                    new_state = {adj_word: new_path}
                    queue.append(new_state)
    return None


# Helper function that gets the full path from the end state
def get_full_path(end_state):
    path_list = []  # empty list to store the path
    while end_state:
        curr_word = next(iter(end_state))  # get current word from end_state
        par_state = end_state[curr_word]  # get parent state corresponding to current word
        path_list.append(curr_word)  # add the current word to the path
        end_state = par_state  # for next iter, update end_state to the parent state

    return sorted(path_list)  # Sort the path for consistency


def main():
    # Read words from the file 'words.txt'
    with open('words.txt', 'r') as words_file:
        # Create a set of valid words
        word_set = {word.strip().lower() for word in words_file if len(word.strip()) <= 7}

    # Process pairs from the file 'pairs.txt' and find word ladders
    with open('pairs.txt', 'r') as pairs_file:
        for line in pairs_file:
            words = line.strip().lower().split()

            # Check if there are enough words in the line
            if len(words) < 2:
                pass
                # print(f"Error: Not enough words in the line - {line}")
            else:
                start, end = map(str.strip, words)

                # Check if both words have the same length
                if len(start) != len(end):
                    print(f"{start} and {end} are not the same length.")
                else:
                    # Call the find_ladder function to find the word ladder
                    start_time = time.process_time()  # Start timing
                    ladder = find_ladder(start, end, word_set)
                    end_time = time.process_time()  # End timing

                    # Print the result of the word ladder
                    print(f"** Looking for a ladder from {start} to {end}")
                    if ladder:
                        print("The ladder is:", " -> ".join(ladder))
                    else:
                        print(f"No ladder found from {start} to {end}.")
                    # printing the Elapsed time
                    print("Elapsed Time = {} seconds".format(end_time - start_time))


if __name__ == "__main__":
    main()
