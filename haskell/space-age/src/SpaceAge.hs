module SpaceAge (Planet(..), ageOn) where

data Planet = Mercury
            | Venus
            | Earth
            | Mars
            | Jupiter
            | Saturn
            | Uranus
            | Neptune

secondsOn :: Planet -> Float
secondsOn Mercury = 0.2408467
secondsOn Venus = 0.61519726
secondsOn Earth = 1
secondsOn Mars = 1.8808158
secondsOn Jupiter = 11.862615
secondsOn Saturn = 29.447498
secondsOn Uranus = 84.016846
secondsOn Neptune = 164.79132

ageOn :: Planet -> Float -> Float
ageOn planet seconds = seconds / (secondsOn planet * 31557600)

