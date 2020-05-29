-- CptS 355 - Spring 2020 Assignment 2
-- Please include your name and the names of the students with whom you discussed any of the problems in this homework

module HW2
     where


{- intersect & intersectTail & intersectAll - 22%-}
--intersect
intersect :: Eq a => [a] -> [a] -> [a]
intersect [] [] = []
intersect x [] = []
intersect [] y = []
intersect x y | elem (head x) (tail x) = intersect (tail x) y  --Remove the duplicate from first list.
              | elem (head x) y = (head x) : intersect (tail x) y  --If first elemnt form first list is same with the element from second list, then keep this elemnt and do recursive.
              | otherwise = intersect (tail x) y  --This element from first list is unique, then do the next elemnt recursive.

--intersectTail
intersectTail :: Eq a => [a] -> [a] -> [a]
intersectTail l1 l2 = tailHelper l1 l2 [] 
                where tailHelper :: Eq a => [a] -> [a] -> [a] -> [a]
                      tailHelper (x:xs) l2 acc | elem x acc = tailHelper xs l2 acc
                                               | elem x l2 = reverse(tailHelper xs l2 (x:acc))
                                               | otherwise = tailHelper xs l2 acc
                      tailHelper l1 [] acc = acc
                      tailHelper [] l2 acc = acc
                      
--intersectAll
intersectAll :: Ord a => [[a]] -> [a]
intersectAll (x:xs) = foldl intersect x xs  --"foldl" iterates over the elements from left to right.

{-2 - partition - 10%-}
partition :: (a -> Bool) -> [a] -> ([a], [a])
partition x ys = (filter x ys, filter (not . x) ys)  --Use filter topick up the elements that satisfy condition.

{- 3 - sumL, sumMaybe, and sumEither - 27% -}
--sumL
sumL :: (Num b) => [[b]] -> b
sumL x = foldr (+) 0 (map sum x)  -- map' sum (x:xs) = (sum x) : (map' sum xs)

-- sumMaybe 
sumMaybe :: (Num a) => [[(Maybe a)]] -> Maybe a
sumMaybe [] = Nothing  --If input a empty list, return "Nothing".
sumMaybe [[Nothing]] = Nothing  --This situation return "Nothing" as well.
sumMaybe list = foldr addMaybe (Just 0) (map (foldr addMaybe (Just 0)) list)
                where addMaybe :: (Num a) => Maybe a -> Maybe a -> Maybe a  --Reference from PowerPointSlide "addMaybe function".
                      addMaybe Nothing Nothing = Nothing
                      addMaybe Nothing (Just y) = (Just y)
                      addMaybe (Just x) Nothing = (Just x)
                      addMaybe (Just x) (Just y) = (Just (x+y))

-- sumEither
data IEither  = IString String | IInt Int
                deriving (Show, Read, Eq)
sumEither :: [[IEither]] -> IEither
sumEither [[]] = IInt 0
sumEither list = foldr sumHelper (IInt 0) (map (foldr sumHelper (IInt 0)) list)
                 where sumHelper :: IEither -> IEither -> IEither
                       sumHelper (IInt x) (IInt y) = (IInt (x+y))
                       sumHelper (IString x) (IInt y) = (IInt ((getInt x) + y))
                       --getInt :: string -> Int
                       getInt z = read z ::Int

{-4 - depthScan, depthSearch, addTrees - 37%-}
data Tree a = LEAF a | NODE a (Tree a) (Tree a)
              deriving (Show, Read, Eq)

--depthScan
depthScan :: Tree a -> [a]  --depthScan recieve a tree type and return a list.
depthScan (LEAF v) = [v]  --Return leaf value.
depthScan (NODE v left right) = (depthScan left) ++ (depthScan right) ++ [v]  --Pre-order print first print left value and then print right value and finally print node value.
 
--depthSearch
depthSearch :: (Ord p, Num p, Eq a) =>Tree a -> a -> p
depthSearch t v | elem v (depthScan t) = depthHelper t v 1
                | otherwise = -1  --It means the tree didn't have this value that user input, then the depth return -1.
                  where depthHelper :: (Ord p, Num p, Eq a) => Tree a -> a -> p -> p 
                        depthHelper (LEAF x) v depth | x == v = depth  --We find target value and return it's depth.
                                                     | otherwise = -1
                        depthHelper (NODE x left right) v depth | elem v (depthScan left) = depthHelper left v (depth + 1)  --We search if our value exist in the left tree, if so then return final summational depth.
                                                                | elem v (depthScan right) = depthHelper right v (depth + 1)  --Same case but search in the right tree.
                                                                | otherwise = depth  --This special situation is for root unless root value doesn't have duplicate on children leaf.

--addTrees
addTrees :: Num a => Tree a -> Tree a -> Tree a
addTrees (LEAF x) (LEAF y) = (LEAF (x + y))  --Add the leaves of tree1 and tree2.
addTrees (NODE x x1 x2) (NODE y y1 y2) = (NODE (x + y) (addTrees x1 y1) (addTrees x2 y2)) 
addTrees (LEAF x) (NODE y y1 y2) = (NODE (x + y) y1 y2)  --If tree1's leaves are less than tree2, then return the rest of tree2.
addTrees (NODE x x1 x2) (LEAF y) = (NODE (x + y) x1 x2)  --Same case but return the rest of tree1.

{- 5- Create two trees of type Tree. The height of both trees should be at least 4. Test your functions depthScan, depthSearch, addTrees with those trees. 
The trees you define should be different than those that are given.   -}

tree1 = NODE 1 (NODE 4 (NODE 6 (LEAF 5) (LEAF 3)) (LEAF 2)) (NODE 7 (LEAF 8) (LEAF 9))
tree2 = NODE 1 (NODE 3 (LEAF 6) (LEAF 4)) (NODE 9 (NODE 5 (LEAF 7) (LEAF 11)) (LEAF 10))
