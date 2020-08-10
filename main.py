def on_b_pressed():
    global _3rr0r
    _3rr0r = sprites.create(img("""
        5 5 5 5 5 5 5 5 5 5 5 5 5 2 2 .
        2 2 . 8 2 5 5 5 5 2 2 2 5 5 5 .
        2 2 . . 5 5 5 a 8 . 2 2 5 2 5 5
        2 2 2 9 9 9 9 9 9 9 9 5 5 5 5 9
        2 2 2 2 2 8 8 2 2 2 2 5 5 5 . 9
        . . 8 3 3 3 3 3 3 3 2 2 5 3 3 9
        . e 7 3 2 9 8 2 8 8 3 8 8 a 9 3
        . 3 3 e 3 e e e 8 a 3 9 9 9 2 2
        e 3 7 e 3 7 7 e 8 7 2 3 3 a 3 a
        a 3 7 9 e 3 3 3 3 3 3 8 3 3 e .
        2 2 3 7 2 e 7 3 3 3 3 3 3 e e .
        2 . . 3 3 7 7 7 7 7 3 e e . 8 8
        . . . a a 3 9 7 3 3 e 8 8 8 . 8
        . . . . 7 7 3 3 e 7 3 . 7 8 8 .
        . 8 8 7 7 7 9 9 9 9 7 7 7 7 9 .
        . . . . . . . . . . 8 8 8 7 9 .
    """),
        SpriteKind.player)
    mySprite.set_image(sprites.food.big_burger)
    _3rr0r.say("I WANT... WAIT. IT,S A BURGER:-O. I WANT THIS BURGER!")
    pause(10000)
    _3rr0r.follow(mySprite)
    _3rr0r.say("OM NOM NOM.OH NO IT,S TOO BIG. OFF")
    pause(5000)
    mySprite.destroy(effects.cool_radial, 500)
    _3rr0r.destroy(effects.fountain, 500)
    my_enemy.destroy(effects.warm_radial, 500)
    mySprite.say("OFF :-(")
    pause(2000)
    game.over(True, effects.slash)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    global _3rr0r
    _3rr0r = sprites.create(img("""
            5 5 5 5 5 5 5 5 5 5 5 5 5 2 2 . 
                    2 2 . 8 2 5 5 5 5 2 2 2 5 5 5 . 
                    2 2 . . 5 5 5 a 8 . 2 2 5 2 5 5 
                    2 2 2 9 9 9 9 9 9 9 9 5 5 5 5 9 
                    2 2 2 2 2 8 8 2 2 2 2 5 5 5 . 9 
                    . . 8 7 7 8 7 2 2 2 2 2 5 3 3 9 
                    . . . 2 2 2 8 2 8 8 8 8 8 a 9 3 
                    . . 2 2 7 8 a 8 8 a a 9 9 9 2 2 
                    2 2 2 8 8 7 7 7 7 2 2 8 2 a a a 
                    a 9 9 9 a a a a 8 a 8 8 a . a . 
                    2 2 a a 9 . a a 8 8 8 9 . a . . 
                    2 . . . . 9 a a 8 a a a a . . . 
                    . . . a a a 9 9 8 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    mySprite.set_image(sprites.food.big_burger)
    _3rr0r.say("I WANT... WAIT. IT,S A BURGER:-O. I WANT THIS BURGER!")
    pause(10000)
    _3rr0r.follow(mySprite)
    _3rr0r.say("OM NOM NOM.OH NO IT,S TOO BIG. OFF")
    pause(5000)
    mySprite.destroy(effects.cool_radial, 500)
    _3rr0r.destroy(effects.fountain, 500)
    my_enemy.destroy(effects.warm_radial, 500)
    mySprite.say("OFF :-(")
    pause(2000)
    game.over(False, effects.melt)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_combos_attach_combo():
    pass
controller.combos.attach_combo("llrrbb", on_combos_attach_combo)

_3rr0r: Sprite = None
my_enemy: Sprite = None
mySprite: Sprite = None
effects.smiles.start_screen_effect()
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . 8 8 8 . . 8 8 8 . . . . . 
            . . . 8 1 8 8 8 8 1 8 . . . . . 
            . . . 8 1 1 1 1 1 1 8 . . . . . 
            . . . 8 8 1 f f 1 8 8 . . . . . 
            . . . . 8 1 f f 1 8 . . . . . . 
            . . . . 8 1 1 1 1 8 . . . . . . 
            . . . . 8 1 8 8 1 8 . . . . . . 
            . . . . 8 8 8 8 8 8 . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
mySprite.set_position(7, 9)
controller.move_sprite(mySprite)
my_enemy = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . 8 8 8 . . 8 8 8 . . . . . 
            . . . 8 1 8 8 8 8 1 8 . . . . . 
            . . . 8 1 1 1 1 1 1 8 . . . . . 
            . . . 8 8 1 2 2 1 8 8 . . . . . 
            . . . . 8 1 2 2 1 8 . . . . . . 
            . . . . 8 1 1 1 1 8 . . . . . . 
            . . . . 8 1 8 8 1 8 . . . . . . 
            . . . . 8 1 8 8 1 8 . . . . . . 
            . . . . 8 8 8 8 8 8 . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)

def on_forever():
    music.play_melody("D - D A E B E B ", 500)
forever(on_forever)
