import time
import random
import string
parameters_list = ["a", "b", "c", "d"]
def user_input(prompt, parameters):
    user_response = input(prompt).lower()
    if user_response in parameters:
        return user_response
    else:
        print("Invalid input")
        return user_input(prompt, parameters)

def generate_gibberish(length=10):
    return ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(length))

def go_to_class():
    print("You feel a twinge of guilt as you think about skipping class to hang out. Tempting, sure, but your university doesn’t mess around. Miss one class and your grade could nosedive.")
    print("Good thing you showed up today. Turns out there's an exam tomorrow. Crisis narrowly avoided.")
    match (user_input("\nWhat will you do? Should you keep on this path of academic dedication?\na: Study for the exam.\nb: Play league all night because studying is hard.\n", parameters_list[:2])):
        case "a":
            print("a: You study for the quiz.")
            take_quiz(True)
        case "b":
            print("b: You play league all night.")
            take_quiz(False)
def generate_gibberish(length=20):
    return ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(length))

def take_quiz(should_take):
    print("\n--- Welcome to the Exam! ---")
    score = 0
    questions_and_answers = []

    for i in range(1, 6):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(['+', '-', '*'])
        question = f"{a} {op} {b}"
        correct_answer = eval(question)

        if should_take:
            prompt = f"Q{i}: What is {question}? "
        else:
            prompt = f"Q{i}: {generate_gibberish()} = ? "

        try:
            user_ans = int(input(prompt))
        except ValueError:
            user_ans = None  # treat invalid input as blank or wrong

        questions_and_answers.append((i, question, correct_answer, user_ans))

    # Now reveal answers and calculate score
    print("\n--- Exam Results ---")
    for i, question, correct_answer, user_ans in questions_and_answers:
        result = "Correct!" if user_ans == correct_answer else f"Wrong. Correct answer: {correct_answer}"
        print(f"Q{i}: {question} = {user_ans if user_ans is not None else 'Invalid'} → {result}")
        if user_ans == correct_answer:
            score += 1
    
    percent = (score / 5) * 100
    print(f"\nYou scored {score}/5. That's {percent}%.")
    if percent >= 60:
        print("You passed the exam! Good job!")
        print("Now you can relax knowing youre going to pass this class.")
        good_academics()
    else:
        print("You failed the exam. Maybe you should have studied more.")
        bad_academics()

def good_academics():
    time.sleep(2)
    print("...")
    print("A couple weeks have passed since the exam and grades have come in.")
    print("Finally, your studying has paid off. You have passed! This was your hardest class, and it has you in high spirits. You give your friend Sarah a call to talk about how the term went.")
    print("You: How were classes?")
    time.sleep(1.5)
    print("Sarah: Ugh, absolutely brutal.")
    time.sleep(2)
    print("You: Right? Everything in physics felt like alien language. I swear the professor was just making noises.")
    time.sleep(2)
    print("Sarah: I know, right? Anyway, thank goodness it is over. I barely survived.")
    time.sleep(2)
    print("You: So, doing anything fun now that we are free from academic prison?")
    time.sleep(2)
    print("Sarah: Yup! I am planning a road trip with my friends this summer. You should totally come. We need someone to bring snacks.")
    time.sleep(2)
    print("You: Tempting, but I think I have to adult this summer. I am trying to land an internship and maybe squeeze in a couple summer classes.")
    time.sleep(3)
    print("Sarah: Boooo. Okay, fine. I get it. You are out here being all responsible and stuff. But still, it would be nice to hang out more.")
    time.sleep(2)
    print("You: Yeah, sorry. School has been running my life lately. But I hope your road trip is amazing. Just do not forget sunscreen and snacks.")
    time.sleep(2)
    print("Sarah: Thanks! Good luck with the internship hunt. May the hiring gods smile upon you.")
    time.sleep(1.5)
    print("You feel like it is your time now. School no longer feels like a burden or an afterthought. Sure, the curriculum is not easy, but it is something you are passionate about. Still, you cannot help but wonder if there are more important things in life than good grades and a good job.")
    # END OF GOOD ACADEMICS

def bad_academics():
    print("""\nYou take one look at the exam grade. "Yeesh," you think to yourself. That thing was a direct missile strike to your GPA. Panic sets in. "Is there a chance I am actually going to fail this class?" you wonder, sweat forming. "I should do something... but this material feels impossible." You stare at the giant and alarming red marks on your page. "Maybe I could talk to my professor... bribe them with cookies... or just beg for mercy. Yeah, mercy might work." """)
    match (user_input("\nWhat will you do?\na: Talk to your professor.\nb: Forget about the class.\n", parameters_list[:2])):
        case "a":
            print("a: You decide to talk to your professor.")
            print("""\nYou talk with your professor: Turns out he is not the evil scary demon from the depths of all that is unholy who is out to destroy your GPA. He is actually a pretty reasonable guy. Just... do not let any of your friends catch you saying that out loud. He tells you that if you can pass the Lab Exam, your grade will be okay. "Thank you so much," you say, smiling politely. But in your head, all you are thinking is, "Please, when is this academic nightmare going to end?" """)
            good_academics()
        case "b":
            print("b: You decide to forget about the class. You play league because it cant be helped. ")
            time.sleep(2)
            print("...")
            print("A couple weeks have passed since the exam and grades have come in.")
            print('Man, I totally flunked that class, you tell yourself. I need to call Sarah to complain. She’ll understand.')
            print("You give her a ring. She picks up immediately.")
            print("Sarah: So, how is the end of the semester looking?")
            time.sleep(1.5)
            print("You: ...")
            time.sleep(1)
            print("You: I flunked one of my classes.")
            time.sleep(1.5)
            print("Sarah: Womp womp.")
            time.sleep(1)
            print("You: Wow. Rude.")
            time.sleep(1.5)
            print("Sarah: I am kidding! That class was insane. I barely scraped by.")
            time.sleep(2)
            print("Sarah: I know another friend who is going to have to retake it too. You are not alone in the academic abyss.")
            time.sleep(2.5)
            print("You: Maybe I should have applied myself more. But honestly, it is hard to care when I am more emotionally invested in my breakfast than my classes.")
            time.sleep(3)
            print("Sarah: Maybe you should explore other majors.")
            time.sleep(1.5)
            print("You: Yeah, maybe.")
            time.sleep(1)
            print("You: I wish there was a major in doing nothing and playing video games.")
            time.sleep(2)
            print("Sarah: Yeah, it is called finance.")
            time.sleep(2)
            print("(Narrator: This is a topical college joke. We love you, finance majors. Kind of.)")
            time.sleep(2)
            print("You: Oh my god…")
            time.sleep(1.5)
            print("Sarah: Haha. Anyway, are you going to be free this summer?")
            time.sleep(2)
            print("You: Well, considering my career is in the gutter, I think my schedule has opened up.")
            time.sleep(2)
            print("Sarah: Perfect! I am planning a road trip with my friends. You should totally come. We need someone to bring snacks.")
            time.sleep(2.5)
            print("You: Wait, that actually sounds amazing. I am so in.")
            time.sleep(1.5)
            print("Sarah: Great! I will send you the details later.")
            time.sleep(2)
            print("Sarah: In the meantime, try not to do anything dumber than failing a class.")
            time.sleep(2)
            print("You: I’ll try not to.")
            time.sleep(1)
            print("""\nYou hang up and stare at the ceiling, thinking about what your future might hold. Maybe this major is not the right fit. Maybe no major is. And honestly, that is okay. You have time to figure it out. 
For now, maybe it is enough to just breathe, take things one day at a time, and enjoy the world around you: road trips, dumb jokes, late night snacks, and everything in between.""")
            # END OF BAD ACADEMICS









def go_to_park():
  match (user_input("\nWhat will you do?\na: walk in silence\nb: talk with your friend.\n", parameters_list[:2])):
    case "a":
        print("a: You walk in silence.")
        park_scene()
    case "b":
        print("b: You talk with your friend.")
        # dialogue with friend
        match (user_input("\nWhat do you want to say?\na: Are we meeting up with others?\nb: Do you have a pair of the special glasses?\nc: Did you know the word eclispe is latin for big rock?\n", parameters_list[:3])):
            case "a":
                print("You: Are we meeting up with others?")
                park_scene()
            case "b":
                print("You: Do you have a pair of the special glasses?")
                time.sleep(1)
                print("Friend: Yeah, I have a pair. They made it really clear to us in class that we need them to watch...")
                time.sleep(1)
                print("Friend: You brought a pair, right?")
                time.sleep(2)
                print("You: ...")
                time.sleep(3)
                print("Friend: Well, im not going to share mine with you.")
                park_scene()
            case "c":
                print("You: Did you know the word eclispe is latin for big rock?")
                print("Friend: Really?")
                time.sleep(2)
                print(". . .")
                time.sleep(2)
                print("(Your friend isnt very smart)")
                park_scene()

def park_scene():
    # next part
    print()

print("It’s a beautiful summer day, and you’re heading to class with a strange mix of excitement and anxiety. There’s supposed to be an eclipse today—something rare, something worth seeing, but you’re worried you might miss it, stuck inside a lecture hall.")
print("Your new friend said they’d meet up to find the perfect spot to watch it. Part of you really wants to go. The other part keeps thinking about attendance policies and looming assignments.")
match (user_input("What will you do?\na: Watch the eclispe with your friend Sarah!\nb: Go to class.\n", parameters_list[:2])):
    case "a":
        print("a: You head over to the park with your friend.")
        go_to_park()
    case "b":
        print("b: You go to class.")
        go_to_class()


# for case a you will have the option to dialogue your friend chosing that or not still calls the same function that leads to the park dialogue

