-- CptS 355 - Spring 2020 Assignment 1
-- Please include your name and the names of the students with whom you discussed any of the problems in this homework

module HW1
     where

-- 1a. exists
-- a)
exists :: Eq t => t -> [t] -> Bool
exists x [] = False    -- This is a special situation if the list is empty.
exists x (y:ys) = if x == y then True else exists x ys -- If the first elemnt of list is difference with t then use recursive to judge if rest elemnts of list has same type with t.

-- 1b. type for exists
{--The Eq is a type signature that can compare the value of t and the list of t ([t]). If they have same type then return true.
   If use "exists :: t -> [t] -> Bool", it means that input t and t list and both are bool type. -}

-- 1.c countInList
countInList :: (Num p, Eq t) => t -> [t] -> p --The function will return a type of p value
countInList x [] = 0
--The normal situation that the list is not empty.
countInList x (y:ys) = if x == y then 1 + c else c
   where c = countInList x ys  --Define the same thing multiple time.

-- 2. listDiff
listDiff :: Eq a => [a] -> [a] -> [a]  --It means that we input two lists and return result list.
listDiff [] (n:ns) = []  
listDiff (n:ns) [] = ns  
listDiff (x:xs) (y:ys) 
   | x == y = listDiff xs ys
   | otherwise = append x (listDiff xs ys) where append x (result) = x:result

-- 3. firstN
firstN :: (Num t, Ord t) => [a] -> t -> [a]
firstN [] n = []
firstN (x:xs) n = if n == 0 then [] else x:(firstN xs (n-1))


-- 4. busFinder
busFinder :: Eq t => t -> [(a, [t])] -> [a]
busFinder x [] = []  --Special situation.
busFinder x (y:ys) = if(exists x (snd y)) then ((fst y):(busFinder x ys)) else (busFinder x ys)

-- 5. cumulativeSums
cumulativeSums :: Num a => [a] -> [a]
cumulativeSums [] = []  --If the list is empty.
cumulativeSums xs = helper xs 0 
   where helper [] n = []
         helper (x:xs) n = (n+x):helper xs (n+x)

-- 6. groupNleft
groupNleft :: Int -> [a] ->[[a]]
groupNleft n [] = []
groupNleft n xs = (take n xs):(groupNleft n (drop n xs))
