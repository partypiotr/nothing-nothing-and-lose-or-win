controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    _3rr0r = sprites.create(img`
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
`, SpriteKind.Player)
    _3rr0r.follow(mySprite)
    pause(5000)
    mySprite.destroy(effects.coolRadial, 500)
    _3rr0r.destroy(effects.fountain, 500)
    my_enemy.destroy(effects.warmRadial, 500)
    game.over(true, effects.slash)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    _3rr0r = sprites.create(img`
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
`, SpriteKind.Player)
    _3rr0r.follow(mySprite)
    pause(5000)
    mySprite.destroy(effects.coolRadial, 500)
    _3rr0r.destroy(effects.fountain, 500)
    my_enemy.destroy(effects.warmRadial, 500)
    game.over(false, effects.melt)
})
let _3rr0r: Sprite = null
let my_enemy: Sprite = null
let mySprite: Sprite = null
effects.smiles.startScreenEffect()
mySprite = sprites.create(img`
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
`, SpriteKind.Player)
mySprite.setPosition(7, 9)
controller.moveSprite(mySprite)
my_enemy = sprites.create(img`
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
`, SpriteKind.Enemy)
forever(function () {
    music.playMelody("D - D A E B E B ", 143)
})
