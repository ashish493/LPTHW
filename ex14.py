from sys import argv

script, user_name=argv
# This make a variable called 'prompt' which we set to what we want. Then, when
# inside the input() function, we insert the variable to output whatever
# prompt is set to. So the prompt will be >  with a space. You can shange all
# prompts in one place using this method.
prompt='>'

print(f"High {user_name} I'm the {script} script.")
print("I'd like to ask you a few questions .")
print(f"Do you like me,{user_name} ?")
likes=input(prompt)

print(f"Where do you live {user_name}?")
lives=input(prompt)

print("What kind of computer do you have?")
computer=input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
you live in {lives} .Not sure where that is.
And you have a {computer} computer. Nice.
""" )
