module Bob (responseFor) where

import Data.Char
responseFor :: String -> String
responseFor xs 
    | isQuestion xs = "Sure."
    | isYelling  xs = "Whoa, chill out!"
    | isBlank    xs = "Fine. Be that way!"
    | otherwise     = "Whatever."

isQuestion :: String -> Bool
isQuestion xs = last xs == '?'

isYelling :: String -> Bool
isYelling xs = allUpper xs || last xs == '!'

isBlank :: String -> Bool
isBlank xs = null [ x | x <- xs, Data.Char.isAlphaNum x ]

allUpper :: String -> Bool
allUpper xs = repeat 'A' <= [ x | x <- xs, Data.Char.isUpper x ] && [ x | x <- xs, Data.Char.isUpper x ] <= repeat 'Z'