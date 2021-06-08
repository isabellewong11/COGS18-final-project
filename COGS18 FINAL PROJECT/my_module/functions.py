"""A collection of functions for doing my project."""

import string
import random
import nltk

#Inputs that the chat can respond to, and outputs that the chat responds with
greetings_in = ['hi', 'hello', 'hey', 'howdy', 'hola', 'hiya', 'yo', 'shalom', 'greetings']
greetings_out = ['You seem cool, let’s hang out! We can watch a show or get food, what do you wanna do?', 
                "I can’t wait for us to become best friends! Let's watch a show or get food, what do you wanna do?",
                 'Hang out with me and get to know me! We can watch a show or get food, what do you wanna do?']

watch_in = ['watch', 'show']
watch_out = ['Awesome! First, can you guess what my favorite tv show is?', 
             'Sounds good! What do you think my favorite tv show is?', 
             'Dope. Can you guess my favorite show?']

tv_in = ['greys', 'anatomy', 'brooklyn', '99', 'parks', 'recreation', 'rec', 'how', 'met', 'mother','office', 'friends']
tv_out = ["Ok stop. I LOVE that show! We’re going to get along well.", 'Omg I was JUST watching that. Nice guess!']

hungry_in = ['get', 'food']
hungry_out = ["Ok yes I’m starving. Let’s eat! What do you think my favorite food is?",
              "I’m hungry too! Can you guess what I’m craving?"]

asian_in = ['sushi', 'ramen', 'poke', 'asian']
asian_out = ['Say LESS. Convoy is loaded with so many places we can go.', 
             'ABSOLUTELY. Let’s go to Convoy! There are so many places I wanna try.']

italian_in = ['pizza', 'pasta', 'italian']
italian_out = ['Absolutely. I’ve been wanting to go to Regents Pizzeria lately too, so let’s go!', 
               'You read my mind. I live right up the street from Regents Pizzeria—let’s go!']

mexican_in = ['tacos', 'burritos', 'mexican']
mexican_out = ['YES. we can go to the Taco Stand, it’s my favorite place!!', 
               'Yes, I am SO down. I’ve had the Taco Stand on my mind a lot lately. Let’s go!!']

unknown = ['Come again?', 'Sure ?', 'Huh?', 'Idk about that one.']

posi_in = ['yes', 'great', 'awesome', 'sure', 'yeah', 'good', 'cool', 'thanks', 'yay']
posi_out = ['Sick.', 'Awesome.', 'Tea.', 'Suuure.', 'Cool cool cool.', 'Love to see it.', 'Word.', 'Dope.']

question1 = "Eeeek I'm not good with questions :0 What I CAN do is suggest we watch a show or get food? Which do you wanna do?"  

def greet(input_string):
    """Intro to prompt questions for user.
    
    Parameters
    ----------
    input_string : string
        Response from user.
        
    Returns
    -------
    output : string
        Randomly selected string from list of responses.
    """
    
    #Check if input string is related to greeting and return appropriate response
    for word in input_string:
        if word in greetings_in:
            output = selector(input_string, greetings_in, greetings_out)
           
            return output
        
def watch(input_string):
    """Check to see if user wants to watch tv.
    
    Parameters
    ----------
    input_string : string
        Response from user.
        
    Returns
    -------
    output : string
        Randomly selected string from list of responses.
    """
    
    #Check if input string is related to watching tv and return appropriate response
    for word in input_string:
        if word in watch_in:
            output = selector(input_string, watch_in, watch_out)
            
            return output

def tv(input_string):
    """Check to see if user can guess my favorite tv show/s.
    
    Parameters
    ----------
    input_string : string
        Response from user.
        
    Returns
    -------
    output : string
        Randomly selected string from list of responses.
    """
    
    #Check if input string is mentions my favorite tv shows and return appropriate response
    for word in input_string:
        if word in tv_in:
            output = selector(input_string, tv_in, tv_out)        
            
            return output

def hungry(input_string):
    """Check to see if user wants to get food.
    
    Parameters
    ----------
    input_string : string
        Response from user.
        
    Returns
    -------
    output : string
        Randomly selected string from list of resposnses.
    """
    
    #Check if input string is related to getting food and return appropriate response
    for word in input_string:
        if word in hungry_in:
            output = selector(input_string, hungry_in, hungry_out)        
            
            return output

def asian_food(input_string):
    """Check to see if user guessed that I like Asian food.
    
    Parameters
    ----------
    input_string : string
        Response from user.
        
    Returns
    -------
    output : string
        Randomly selected string from list of responses.
    """
    
    #Check if input string mentions specified Asian food and return appropriate response
    for word in input_string:
        if word in asian_in:
            output = selector(input_string, asian_in, asian_out)   
            
            return output

def italian_food(input_string):
    """Check to see if user guessed that I like Italian food.
    
    Parameters
    ----------
    input_string : string
        Response from user.
        
    Returns
    -------
    output : string
        Randomly selected string from list of responses.
    """
    
    #Check if input string mentions specified Italian food and return appropriate response
    if is_in_list(input_string, italian_in):
        output = selector(input_string, italian_in, italian_out)        
        
        return(output)
    
     
def mexican_food(input_string):
    """Check to see if user guessed that I like Mexican food.
    
    Parameters
    ----------
    input_string : string
        Response from user.
        
    Returns
    -------
    output : string
        Randomly selected string from list of responses.
    """
    
    #Check if input string mentions specified Mexican food and return appropriate response
    for word in input_string:
        if word in mexican_in:
            output = selector(input_string, mexican_in, mexican_out)        
            
            return output

def posi_response(input_string):
    """Return positive response if the user says a positive word, unrelated to the other functions.
    
    Parameters
    ----------
    input_string : string
        Response from user.
        
    Returns
    -------
    output : string
        Randomly selected string from list of responses.
    """
    
    #Check if input string mentions a positive word and return appropriate response
    for word in input_string:
        if word in posi_in:
            output = selector(input_string, posi_in, posi_out)        
            
            return output

def is_question(input_string):
    """Check if the input is a question.
       Taken from A3.
    
    Parameters
    ----------
    input_string : string
        Response from user.
        
    Returns
    -------
    output : boolean
        True if input contains '?', False if not.
    """
    
    if '?' in input_string:
        output = True
    else:
        output = False
    
    return output

def remove_punctuation(input_string):
    """Take out punctuation symbols from user's input string.
       Taken from A3.
    
    Parameters
    ----------
    input_string : string
        Response from user.
        
    Returns
    -------
    out_string : string
        Response from user with punctuation removed.
    """
         
    out_string = ''
    
    for let in input_string:
        if let not in string.punctuation:
            out_string = out_string + let
    
    return out_string

def prepare_text(input_string):    
    """Prepares string to be processed by functions.
       Taken from A3.
    
    Parameters
    ----------
    input_string : string
        Response from user.
        
    Returns
    -------
    out_list : list
        List of seperated lowercase words from user, with punctuation removed.
    """
    
    out_list = []
    
    #Put user's string in lowercase
    temp_string = input_string.lower()
    
    #Then remove punctuation from string
    temp_string = remove_punctuation(temp_string)
    
    #Then split string and add the words to a list
    out_list = temp_string.split()
    
    return out_list

def selector(input_list, check_list, return_list):
    """Checks if user mentions a word that's in a specified list, then returns appropriate response.
       Taken from A3.
    
    Parameters
    ----------
    input_string : list
        Input string from user, seperated into a list.
    check_list : list
        Used to check if the user mentions something from this list. 
    return_list : list
        List with possible responses if input mentions something from check_list.
        
    Returns
    -------
    output : string or None
        Randomly selected string from return_list if conditions are met, otherwise None.
    """
    
    output = None
    
    for item in input_list:
        if item in check_list:
            output = random.choice(return_list)
            break
            
    return output

def end_chat(input_list):
    """Ends the chatbot if user says 'quit' or 'bye'.
       Taken and modified from A3.
    
    Parameters
    ----------
    input_list : list
        Input from user, seperated into words in a list.
        
    Returns
    -------
    output : boolean
        True if the user wants to end the chat, False otherwise.
    """
    
    if 'quit' in input_list:
        output = True
    elif 'bye' in input_list:
        output = True
    else:
        output = False
        
    return output

def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two.
       Taken from A3.
    
    Parameters
    ----------
    list_one : list
        List to be checked for any mentions of an element in list_two.
    list_two : list
        List that list_one uses to check itself for.
        
    Returns
    -------
    boolean
        True if list_one mentions something from list_two, False otherwise.
    """
    
    for element in list_one:
        if element in list_two:
            return True
    
    return False

def have_a_chat():
    """Main function to run our chatbot.
       Taken and modified from A3.
       
    """
    
    #Initiates the conversation.
    intro_msg = "Hey! Nice to meet you, I'm Isabelle."
    print(intro_msg)
    
    chat = True
    while chat:

        # Get a message from the user
        msg = input('YOU :\t')
        out_msg = None

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = "Alright, I'll pick you up in a few hours. See ya then!"
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(greet(msg))

            # Check if the input is about watching tv, add a watch output if so
            outs.append(watch(msg))            
            
            # Check if the input guessed my fav tv show, add tv output if so
            outs.append(tv(msg))
            
            # Check if the input is about getting food, add a hungry output if so
            outs.append(hungry(msg))
            
            # Check if the input guesses I like Asian food, add a Asian food output if so
            outs.append(asian_food(msg))
            
            # Check if the input guesses I like Italian food, add an Italian food output if so
            outs.append(italian_food(msg))
            
            # Check if the input guesses I like Mexican food, add a Mexican food output if so
            outs.append(mexican_food(msg))
            
            # Check if the input contains a positive word, add a positive response output if so
            outs.append(posi_response(msg))
          
            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = question1

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(unknown)

        print('ISABELLE:', out_msg)
        
        
        
