words=[]

def welcome_screen():
    initial_response=input("Type \"Start\" to start.")
    while(initial_response not in ["start", "Start", "START"]):
        print("Sorry, that's not an option.")
        initial_response=input("Type \"Start\" to start.")
    begin_game()

def word_prompt(part_of_speech):
    global words
    words.append(input("Enter " + part_of_speech + '.'))

def begin_game():
    word_prompt("a verb")
    word_prompt("an adjective ending in -er")
    word_prompt("a verb")
    word_prompt("a noun")
    word_prompt("a noun")
    word_prompt("a noun")
    word_prompt("a plural noun")
    word_prompt("a verb")
    word_prompt("a noun")
    word_prompt("a plural noun")
    word_prompt("a noun")
    word_prompt("an adverb")
    word_prompt("a verb")
    integrate_words()

def integrate_words():
    global words
    global story
    story[1]=words[0]
    story[6]=words[0]
    del words[0]
    story[16]=words[0]
    del words[0]
    story[21]=words[0]
    del words[0]
    story[24]=words[0]
    del words[0]
    story[26]=words[0]
    del words[0]
    story[37]=words[0]
    del words[0]
    story[39]=words[0]
    del words[0]
    story[51]=words[0]
    story[60]=words[0]
    story[92]=words[0]
    story[96]=words[0]
    del words[0]
    story[67]=words[0]
    del words[0]
    story[72]=words[0]
    del words[0]
    story[75]=words[0]
    del words[0]
    story[84]=words[0]
    del words[0]
    story[100]=words[0]
    del words[0]
    print()
    write_story()

def write_story():
    global story
    for i in range(len(story)):
        if story[i] not in ['.', ',', '!', '—', ':'] and story[i-1]!='—':
            print(' ', end = '')
        if story[i]!='br':
            print(story[i], end = '')
        else:
            print()

story=['To', 1, ',', 'or', 'not', 'to', 6, '—', 'that', 'is', 'the', 'question', ':', 'br', 'Whether', "'tis", 16, 'in', 'the', 'mind', 'to', 21, 'br', 'The', 24, 'and', 26, 'of', 'outrageous', 'fortune', 'br', 'Or', 'to', 'take', 'arms', 'against', 'a', 37, 'of', 39, 'br', 'And', 'by', 'opposing', 'end', 'them', '.', 'To', 'die', ',', 'to', 51, '—', 'br', 'No', 'more', '—', 'and', 'by', 'a', 60, 'to', 'say', 'we', 'end', 'br', 'The', 67, 'and', 'the', 'thousand', 'natural', 72, 'br', 'That', 75, 'is', 'heir', 'to', '—', "'tis", 'a', 'consummation', 'br', 84, 'to', 'be', 'wished', '!', 'To', 'die,', 'to', 92, '.', 'br', 'To', 96, ',', 'perchance', 'to', 100]
# Story source: Hamlet by Shakespeare
# Mad Libs source: https://libwww.freelibrary.org/explore/topic/shakespeare/mad-libs

# Initialization:
print("Welcome to mad libs!")
welcome_screen()