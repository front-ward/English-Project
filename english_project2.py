import time
import random
import string

# --------------------------------
# Utility functions (used anywhere)
# --------------------------------

parameters_list = ["a", "b", "c", "d"]

def user_input(prompt, parameters):
    user_response = input(prompt).lower()
    if user_response in parameters:
        return user_response
    else:
        print("Invalid input")
        return user_input(prompt, parameters)

def generate_gibberish(length=20):
    return ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(length))


# --------------------------------
# Step 2A: Park Path → Interactions with friend → leads to park_scene()
# --------------------------------


def go_to_park():
    print("\nYou decide to go to the park with your friend. Sure, you should probably be focusing on class, but this feels like a unique opportunity. Honestly, you think to yourself, \"This probably will not even be that cool,\" partly because the weather is terrible for something like this, and partly because you just do not care that much. Maybe you are going because you are excited to meet new people, or maybe you are just looking for an excuse to skip class. Either way, your curiosity gets the better of you.")
    match (user_input("\nWhat do you want to say on your way there?\na: Are we meeting up with others?\nb: Do you have a pair of the special glasses?\n", parameters_list[:2])):
        case "a":
            print("\nYou: Are we meeting up with others?")
            time.sleep(1.5)
            print("Sarah: Yeah we are meeting up with my friend Kate. She is already at the park.")
        case "b":
            print("\nYou: Do you have a pair of the special glasses?")
            time.sleep(1.5)
            print("Sarah: Yeah, I have a pair. They made it really clear to us in class that we need them to watch...")
            time.sleep(1.5)
            print("Sarah: You brought a pair, right?")
            time.sleep(3.0)
            print("You: ...")
            time.sleep(4.5)
            print("Sarah: Well, I’m not going to share mine with you.")

    match (user_input("\nOn your way there you see a pair of those eclispe glasses on the ground. Do you pick them up?\na: Pick them up.\nb: Leave them there.\n", parameters_list[:2])):
        case "a":
            print("a: You pick them up.")
            print("\nYou: Oh, look! A pair of eclipse glasses. I definitely need these.")
            time.sleep(3.0)
            print("Sarah: You sure you want to grab those? They could be broken or something.")
            time.sleep(3.0)
            print("You: Nah, they look fine. I’ll just clean them up a bit.")
            park_scene(True)
        case "b":
            print("b: You leave them there.")
            park_scene(False)


def park_scene(has_glasses):
    print("\nYou arrive at the park, where a picnic blanket is already set up by one of Sarah’s friends. She smiles and waves as you approach.")
    input("Press Enter to continue...\n")
    print("Kate: Hi, I am Kate. And you are [blank]?")
    time.sleep(2.25)
    print("Narrator: I forgot to code the part where you enter your name. Just imagine your name here.")
    time.sleep(2.25)
    print("You: How did you know that?")
    time.sleep(1.5)
    print("Kate: Sarah talks about you all the time.")
    time.sleep(1.8)
    print("You: I hope that is a good thing. But knowing Sarah, it is probably not.")
    time.sleep(2.25)
    print("Kate: Yeah... it is not.")
    time.sleep(1.5)
    print("Sarah: Sorry! Haha.")
    time.sleep(1.8)
    print("You: Anyway, this weather kind of sucks.")
    time.sleep(1.5)
    print("Kate: I know, right? I can barely see anything. These glasses are more fog than lens at this point.")
    time.sleep(3.0)

    print("\nYou want to know what kate is talking about, but you do not have a pair of those glasses what do you do?\n")
    if has_glasses:
        match (user_input("a: Ask Kate to borrow her glasses.\nb: Use the glasses you found.\n", parameters_list[:2])):
            case "a":
                print("a: You ask Kate to borrow her glasses.")
                ask_kate()
            case "b":
                print("b: You use the glasses you found.")
                grounded_glasses()
    else:
        match (user_input("a: Ask Kate to borrow her glasses.\n", parameters_list[:1])):
            case "a":
                print("a: You ask Kate to borrow her glasses.")
                ask_kate()

def ask_kate():
    print("\nYou ask Kate if you can borrow her glasses, and she happily hands them over. You put them on and look up at the sky. Through the tinted lenses, you can just faintly make out the moon drifting in front of the sun, casting a soft, eerie glow over everything.")
    time.sleep(5.0)
    print("You: That is cool... I guess.")
    time.sleep(2.25)
    print("Kate: Yeah, I mean...")
    time.sleep(1.5)
    print("Kate: It was a good excuse to skip class.")
    time.sleep(2.25)
    print("You both laugh, the kind of laugh that comes from shared relief more than excitement.")
    time.sleep(3.0)
    print("You: Yeah. Maybe I will stop worrying about work for a while.")
    print("\nYou sit back on the blanket, letting the quiet settle in. For once, you are not thinking about grades, deadlines, or what comes next. You are just here, in the moment, watching the sky with a new friend. And that feels pretty good.")
    input("FIN")

def grounded_glasses():
    print("\nYou use the glasses you found on the floor and look up at the sky, hoping to catch a glimpse of the full eclipse. But you realize your mistake as soon as you look up. The glasses do not work, and a ray of sunlight immediately pierces through the lenses.")
    print("You should not have looked up...")
    input("Press Enter to continue...\n")
    print("In a painfully embarrassing turn of events, you end up sprinting to the emergency room with Sarah by your side. Thankfully, there is no permanent damage to your vision. Just to your pride.")
    print("You missed class, missed your chance to make a new friend, and missed the eclipse. All you got was a melted pair of knockoff eclipse glasses and a medical bill that says \"do not stare directly at the sun.\"")
    input("FIN")
    # END
    
    


# --------------------------------
# Step 2B: Class Path → leads to exam choice → take_quiz()
# --------------------------------

def go_to_class():
    print("\nYou feel a twinge of guilt as you think about skipping class to hang out. Tempting, sure, but your university doesn’t mess around. Miss one class and your grade could nosedive.")
    print("Good thing you showed up today. Turns out there's an exam tomorrow. Crisis narrowly avoided.")
    match (user_input("\nWhat will you do? Should you keep on this path of academic dedication?\na: Study for the exam.\nb: Play league of legends all night because studying is hard.\n", parameters_list[:2])):
        case "a":
            print("a: You study for the quiz.")
            take_quiz(True)
        case "b":
            print("b: You play league of legends all night.")
            take_quiz(False)


# --------------------------------
# Step 3: Take the exam → leads to good_academics() or bad_academics()
# --------------------------------

def take_quiz(should_take):
    input("Press Enter to continue...")
    time.sleep(3.0)
    print("\nThe next day...")
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
            user_ans = None

        questions_and_answers.append((i, question, correct_answer, user_ans))

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
        print("Now you can relax knowing you’re going to pass this class.")
        good_academics()
    else:
        print("You failed the exam. Maybe you should have studied more.")
        bad_academics()


# --------------------------------
# Step 4A: If passed → good ending
# --------------------------------

def good_academics():
    input("Press Enter to continue...")
    time.sleep(3.0)
    print("\nA couple weeks have passed since the exam and grades have come in.")
    print("Finally, your studying has paid off. You have passed! This was your hardest class, and it has you in high spirits. You give your friend Sarah a call to talk about how the term went.")
    input("Press Enter to continue...")
    print("\nYou: How were classes?")
    time.sleep(2.25)
    print("Sarah: Ugh, absolutely brutal.")
    time.sleep(3.0)
    print("You: Right? Everything in physics felt like alien language. I swear the professor was just making noises.")
    time.sleep(3.0)
    print("Sarah: I know, right? Anyway, thank goodness it is over. I barely survived.")
    time.sleep(3.0)
    print("You: So, doing anything fun now that we are free from academic prison?")
    time.sleep(3.0)
    print("Sarah: Yup! I am planning a road trip with my friends this summer. You should totally come. We need someone to bring snacks.")
    time.sleep(3.0)
    print("You: Tempting, but I think I have to adult this summer. I am trying to land an internship and maybe squeeze in a couple summer classes.")
    time.sleep(4.5)
    print("Sarah: Boooo. Okay, fine. I get it. You are out here being all responsible and stuff. But still, it would be nice to hang out more.")
    time.sleep(3.0)
    print("You: Yeah, sorry. School has been running my life lately. But I hope your road trip is amazing. Just do not forget sunscreen and snacks.")
    time.sleep(3.0)
    print("Sarah: Thanks! Good luck with the internship hunt. May the hiring gods smile upon you.")
    time.sleep(2.25)
    print("\nYou feel like it is your time now. School no longer feels like a burden or an afterthought. Sure, the curriculum is not easy, but it is something you are passionate about. Still, you cannot help but wonder if there are more important things in life than good grades and a good job.")
    # END OF GOOD ACADEMICS
    input("FIN")


# --------------------------------
# Step 4B: If failed → choose between retry or not
# --------------------------------

def bad_academics():
    input("Press Enter to continue...") 
    print("""\nYou take one look at the exam grade. "Yeesh," you think to yourself. That thing was a direct missile strike to your GPA. Panic sets in. "Is there a chance I am actually going to fail this class?" you wonder, sweat forming. "I should do something... but this material feels impossible." You stare at the giant and alarming red marks on your page. "Maybe I could talk to my professor... bribe them with cookies... or just beg for mercy. Yeah, mercy might work." """)
    match (user_input("\nWhat will you do?\na: Talk to your professor.\nb: Forget about the class.\n", parameters_list[:2])):
        case "a":
            print("a: You decide to talk to your professor.")
            print("""\nYou talk with your professor: Turns out he is not the evil scary demon from the depths of all that is unholy who is out to destroy your GPA. He is actually a pretty reasonable guy. Just... do not let any of your friends catch you saying that out loud. He tells you that if you can pass the Lab Exam, your grade will be okay. "Thank you so much," you say, smiling politely. But in your head, all you are thinking is, "Please, when is this academic nightmare going to end?" """)
            good_academics()
        case "b":
            print("b: You decide to forget about the class. You play league of legends because it cant be helped. ")
            print("\nA couple weeks have passed since the exam and grades have come in.")
            print('Man, I totally flunked that class, you tell yourself. I need to call Sarah to complain. She’ll understand.')
            print("You give her a ring. She picks up immediately.")
            input("Press Enter to continue...")
            print("\nSarah: So, how is the end of the semester looking?")
            time.sleep(2.25)
            print("You: ...")
            time.sleep(1.5)
            print("You: I flunked one of my classes.")
            time.sleep(2.25)
            print("Sarah: Womp womp.")
            time.sleep(1.5)
            print("You: Wow. Rude.")
            time.sleep(2.25)
            print("Sarah: I am kidding! That class was insane. I barely scraped by.")
            time.sleep(3.0)
            print("Sarah: I know another friend who is going to have to retake it too. You are not alone in the academic abyss.")
            time.sleep(3.75)
            print("You: Maybe I should have applied myself more. But honestly, it is hard to care when I am more emotionally invested in my breakfast than my classes.")
            time.sleep(4.5)
            print("Sarah: Maybe you should explore other majors.")
            time.sleep(2.25)
            print("You: Yeah, maybe.")
            time.sleep(1.5)
            print("You: I wish there was a major in doing nothing and playing video games.")
            time.sleep(3.0)
            print("Sarah: Yeah, it is called finance.")
            time.sleep(3.0)
            print("(Narrator: This is a topical college joke. We love you, finance majors. Kind of.)")
            time.sleep(3.0)
            print("You: Oh my god…")
            time.sleep(2.25)
            print("Sarah: Haha. Anyway, are you going to be free this summer?")
            time.sleep(3.0)
            print("You: Well, considering my career is in the gutter, I think my schedule has opened up.")
            time.sleep(3.0)
            print("Sarah: Perfect! I am planning a road trip with my friends. You should totally come. We need someone to bring snacks.")
            time.sleep(3.75)
            print("You: Wait, that actually sounds amazing. I am so in.")
            time.sleep(2.25)
            print("Sarah: Great! I will send you the details later.")
            time.sleep(3.0)
            print("Sarah: In the meantime, try not to do anything dumber than failing a class.")
            time.sleep(3.0)
            print("You: I’ll try not to.")
            time.sleep(1.5)
            print("""\nYou hang up and stare at the ceiling, thinking about what your future might hold. Maybe this major is not the right fit. Maybe no major is. And honestly, that is okay. You have time to figure it out. 
For now, maybe it is enough to just breathe, take things one day at a time, and enjoy the world around you: road trips, dumb jokes, late night snacks, and everything in between.""")
            # END OF BAD ACADEMICS
            input("FIN")

# --------------------------------
# Step 1: Entry point of the story
# --------------------------------

print("It’s a beautiful summer day, and you’re heading to class with a strange mix of excitement and anxiety. There’s supposed to be a full eclipse today, something rare, something worth seeing, but you’re worried you might miss it, stuck inside a lecture hall.")
print("Your new friend said they’d meet up to find the perfect spot to watch it. Part of you really wants to go. The other part keeps thinking about attendance policies and looming assignments.")

match (user_input("What will you do?\na: Watch the full eclipse with your friend Sarah!\nb: Go to class.\n", parameters_list[:2])):
    case "a":
        print("a: You head over to the park with your friend.")
        go_to_park()
    case "b":
        print("b: You go to class.")
        go_to_class()



# citations