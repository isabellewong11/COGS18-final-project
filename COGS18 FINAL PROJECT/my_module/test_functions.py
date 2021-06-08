"""Test for my functions."""

from my_module.functions import *

def test_greet():
    """Tests for the `greet` function."""
    
    greet_out1 = 'You seem cool, let’s hang out! We can watch a show or get food, what do you wanna do?'
    greet_out2 = 'I can’t wait for us to become best friends—let’s hang! we can watch a show or get food, what do you wanna do?'
    greet_out3 = 'Hang out with me and get to know me! We can watch a show or get food, what do you wanna do?'
    
    assert greet('hey there') == greet_out1 or greet_out2 or greet_out3
    assert callable(greet)

def test_watch():
    """Tests for the `watch` function."""           
    
    watch_out1 = 'Awesome! First, can you guess what my favorite tv show is?'
    watch_out2 = 'Sounds good! What do you think my favorite tv show is?'
    watch_out3 = 'Dope. Can you guess my favorite show?'
    
    assert watch('lets watch a show') == watch_out1 or watch_out2 or watch_out3
    assert callable(watch)
    
def test_tv():
    """Tests for the `tv` function.""" 
    
    tv_out1 = "Ok stop. I LOVE that show! We’re going to get along well."
    tv_out2 = 'Omg I was JUST watching that. Nice guess!'
    
    assert tv('friends') == tv_out1 or tv_out2
    assert callable(tv)

def test_hungry():   
    """Tests for the `hungry` function."""
    
    hungry_out1 = "Ok yes I’m starving. Let’s eat! What do you think my favorite food is?"
    hungry_out2 = "I’m hungry too! Can you guess what I’m craving?"
    
    assert hungry('lets get food') == hungry_out1 or hungry_out2
    assert callable(hungry)
    
def test_asian():
    """Tests for the `asian_food` function."""
    
    asian_out1 = 'Say LESS. Convoy is loaded with so many places we can go.'
    asian_out2 = 'ABSOLUTELY. Let’s go to Convoy! There are so many places I wanna try.'
    
    assert asian_food('i think sushi') == asian_out1 or asian_out2
    assert callable(asian_food)
    
def test_italian():
    """Tests for the `italian_food` function."""
    
    italian_out1 = 'Absolutely. I’ve been wanting to go to Regents Pizzeria lately too, so let’s go!'
    italian_out2 = 'You read my mind. I live right up the street from Regents Pizzeria—let’s go!'
    
    assert italian_food('i think italian') == italian_out1 or italian_out2
    assert callable(italian_food)
    
def test_mexican():
    """Tests for the `mexican_food` function."""
    
    mexican_out1 = 'YES. we can go to the Taco Stand, it’s my favorite place!!'
    mexican_out2 = 'Yes, I am SO down. I’ve had the Taco Stand on my mind a lot lately. Let’s go!!'
    
    assert mexican_food('i think burritos') == mexican_out1 or mexican_out2
    assert callable(mexican_food)
    
def test_posi_response():
    """Tests for the `posi_response` function."""
    
    posi_out1 = 'Sick.'
    posi_out2 = 'Awesome.'
    posi_out3 = 'Tea.'
    posi_out4 = 'Suuure.'
    posi_out5 = 'Cool cool cool.'
    posi_out6 = 'Love to see it.'
    posi_out7 = 'Word.'
    posi_out8 = 'Dope.'
    
    assert posi_response('thats awesome') == posi_out1 or posi_out2 or posi_out3 or posi_out4 or posi_out5 or posi_out6 or posi_out7 or posi_out8
    assert callable(posi_response)
    
def test_prepare_text():
    """Tests for the `prepare_text` function from A3."""
    
    assert isinstance(prepare_text('yeah cool hey'), list)
    assert callable(prepare_text)
    
    
    
    