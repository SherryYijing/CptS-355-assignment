{-Haskell HW2 HUnit test cases
 Please add at least 2 additional tests for each problem-}

module HW2SampleTests
    where

import Test.HUnit
import Data.Char
import Data.List (sort)
import HW2

{- Two useful functions in the HUnit package are assertEqual and assertBool.
The arguments to 'assertEqual' are:
      a descriptive string
      the expected value
      the value being tested
The arguments to 'assertBool' are:
      a descriptive string
      the boolean value being tested
-}

-- Sample Tree Integer examples given in the assignment prompt; make sure to provide your own tree examples for both tree data types
-- Your trees should have minimum 4 levels. 
t1 =  NODE 
         "Science" 
         (NODE "and" (LEAF "School")(NODE 
                                      "Engineering" 
                                      (LEAF "of") 
                                      (LEAF "Electrical"))) 
          (LEAF "Computer")

t2 = NODE 1 (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6)) (NODE 7 (LEAF 8) (LEAF 9))

t3  = NODE 1 (NODE 2 (NODE 3 (LEAF 2) (LEAF 5)) (LEAF 1)) (NODE 1 (LEAF 8) (LEAF 5))

additionalTree1 = NODE 
        "!" 
        (NODE "smart" (LEAF "I")(NODE 
                                    "and" 
                                    (LEAF "am") 
                                    (LEAF "beautiful"))) 
          (LEAF "lady")

additionalTree2  = NODE 11 (NODE 12 (NODE 13 (LEAF 14) (LEAF 15)) (LEAF 16)) (NODE 17 (LEAF 18) (LEAF 19))
                                                                
left = NODE 1 (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6)) (NODE 7 (LEAF 8) (LEAF 9))
right = NODE 1 (NODE 2 (LEAF 3) (LEAF 6)) (NODE 7 (NODE 8 (LEAF 10) (LEAF 11)) (LEAF 9))

additionalLeft = NODE 2 (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6)) (NODE 9 (LEAF 8) (LEAF 1))
additionalRight = NODE 2 (NODE 2 (LEAF 3) (LEAF 6)) (NODE 9 (NODE 8 (LEAF 10) (LEAF 11)) (LEAF 1))

l1 = LEAF "1"
l2 = LEAF "2"
l3 = LEAF "3"
l4 = LEAF "4"
n1 = NODE "5" l1 l2
n2 = NODE "6" n1 l3
t4 = NODE "7" n2 l4

p1a_test1 = TestCase (assertEqual "intersect [2,2,5,6,6,8,9] [1,3,2,2,4,4,5,7,8,10]" (sort [2,5,8])  (sort (intersect [2,2,5,6,6,8,9] [1,3,2,2,4,4,5,7,8,10])) ) 
p1a_test2 = TestCase (assertEqual "intersect [5,6,7,8,9] [8,8,10,10,11,12,5]" (sort [5,8])  (sort (intersect [5,6,7,8,9] [8,8,10,10,11,12,5])) ) 
p1a_test3 = TestCase (assertEqual "intersect [\"a\",\"b\",\"d\"] [\"c\",\"e\",\"f\",\"g\"]" []  (intersect ["a","b","d"] ["c","e","f","g"]) ) 
p1a_additionalTest1 = TestCase (assertEqual "intersect [3,3,4,5,5,6,7] [2,5,3,3,4,4,6,8,9,10]" (sort [3,4,5,6]) (sort (intersect [3,3,4,5,5,6,7] [2,5,3,3,4,4,6,8,9,10])) ) 
p1a_additionalTest2 = TestCase (assertEqual "intersect [\"s\",\"h\",\"e\",\"r\",\"r\",\"y\"] [\"d\",\"o\",\"d\",\"s\",\"o\",\"n\"]" ["s"] (intersect ["s","h","e","r","r","y"] ["d","o","d","s","o","n"]) )

p1b_test1 = TestCase (assertEqual "intersectTail [2,2,5,6,6,8,9] [1,3,2,2,4,4,5,7,8,10]" (sort [2,5,8])  (sort (intersectTail [2,2,5,6,6,8,9] [1,3,2,2,4,4,5,7,8,10])) )
p1b_test2 = TestCase (assertEqual "intersectTail [5,6,7,8,9] [8,8,10,10,11,12,5]" (sort [5,8])  (sort (intersectTail [5,6,7,8,9] [8,8,10,10,11,12,5])) ) 
p1b_test3 = TestCase (assertEqual "intersect [\"a\",\"b\",\"d\"] [\"c\",\"e\",\"f\",\"g\"]" []  (intersectTail ["a","b","d"] ["c","e","f","g"]) ) 
p1b_additionalTest1 = TestCase (assertEqual "intersect [3,3,4,5,5,6,7] [2,5,3,3,4,4,6,8,9,10]" (sort [3,4,5,6]) (sort (intersect [3,3,4,5,5,6,7] [2,5,3,3,4,4,6,8,9,10])) ) 
p1b_additionalTest2 = TestCase (assertEqual "intersect [\"s\",\"h\",\"e\",\"r\",\"r\",\"y\"] [\"d\",\"o\",\"d\",\"s\",\"o\",\"n\"]" ["s"] (intersect ["s","h","e","r","r","y"] ["d","o","d","s","o","n"]) )

p1c_test1 = TestCase (assertEqual "intersectAll [[1,3,3,4,5,5,6],[3,4,5],[4,4,5,6],[3,5,6,6,7,8]]" (sort [5])  (sort (intersectAll [[1,3,3,4,5,5,6],[3,4,5],[4,4,5,6],[3,5,6,6,7,8]])) )
p1c_test2 = TestCase (assertEqual "intersectAll [[3,4],[-3,-4,3,4],[-3,-4,5,6]] " []  (sort (intersectAll [[3,4],[-3,-4,3,4],[-3,-4,5,6]])) )
p1c_test3 = TestCase (assertEqual "intersectAll [[3,4,5,5,6],[4,5,6],[],[3,4,5]] " []  (sort (intersectAll [[3,4,5,5,6],[4,5,6],[],[3,4,5]])) )
p1c_additionalTest1 = TestCase (assertEqual "intersect [[5,7,9],[2,4,6,9],[3,8,9]] " (sort [9]) (sort (intersectAll [[5,7,9],[2,4,6,9],[3,8,9]])) ) 
p1c_additionalTest2 = TestCase (assertEqual "intersect [[8],[1,2,3,4,5,6,7]] " [] (sort (intersectAll [[8],[1,2,3,4,5,6,7]])) )

p2_test1 = TestCase (assertEqual "partition (\\x -> (x<=4)) [1,7,4,5,3,8,2,3]" ([1,4,3,2,3],[7,5,8])  (partition (\x -> (x<=4)) [1,7,4,5,3,8,2,3]) )
p2_test2 = TestCase (assertEqual "partition null [[1,2],[1],[],[5],[],[6,7,8]]" ([[],[]],[[1,2],[1],[5],[6,7,8]])  (partition null [[1,2],[1],[],[5],[],[6,7,8]]) )
p2_test3 = TestCase (assertEqual "partition (elem 1) [[1,2],[1],[],[5],[],[6,7,8]] " ([[1,2],[1]],[[],[5],[],[6,7,8]])  (partition (elem 1) [[1,2],[1],[],[5],[],[6,7,8]] ) )
p2_additionalTest1 = TestCase (assertEqual "partition (\\x -> (x>=8)) [2,4,6,8,10,12,14,16,18] " ([8,10,12,14,16,18],[2,4,6])  (partition (\x -> (x>=8)) [2,4,6,8,10,12,14,16,18] ) )
p2_additionalTest2 = TestCase (assertEqual "partition (elem 5) [[1,2,5],[1],[],[5],[],[5,6,7,8]] " ([[1,2,5],[5],[5,6,7,8]],[[1],[],[]])  (partition (elem 5) [[1,2,5],[1],[],[5],[],[5,6,7,8]] ) )

p3a_test1 = TestCase (assertEqual "sumL [[1,2,3],[4,5],[6,7,8,9],[]]" 45 (sumL [[1,2,3],[4,5],[6,7,8,9],[]]) ) 
p3a_test2 = TestCase (assertEqual "sumL [[10,10],[10,10,10],[10]]" 60 (sumL [[10,10],[10,10,10],[10]]) ) 
p3a_test3 = TestCase (assertEqual "sumL [[]]" 0 (sumL [[]]) ) 
p3a_additionalTest1 = TestCase (assertEqual "sumL [[1],[2,3],[4,5,6],[]]" 21 (sumL [[1],[2,3],[4,5,6],[]]) ) 
p3a_additionalTest2 = TestCase (assertEqual "sumL [[],[],[],[]]" 0 (sumL [[],[],[],[]]) ) 

p3b_test1 = TestCase (assertEqual "sumMaybe [[(Just 1),(Just 2),(Just 3)],[(Just 4),(Just 5)],[(Just 6),Nothing ],[],[Nothing ]]" (Just 21) (sumMaybe [[(Just 1),(Just 2),(Just 3)],[(Just 4),(Just 5)],[(Just 6),Nothing ],[],[Nothing ]]) )
p3b_test2 = TestCase (assertEqual "sumMaybe [[(Just 10),Nothing],[(Just 10), (Just 10), (Just 10),Nothing,Nothing]]" (Just 40) (sumMaybe [[(Just 10),Nothing],[(Just 10), (Just 10), (Just 10),Nothing,Nothing]]) )
p3b_test3 = TestCase (assertEqual "sumMaybe [[Nothing ]]" (Nothing) (sumMaybe [[Nothing ]]) )
p3b_additionalTest1 = TestCase (assertEqual "sumMaybe [[(Just 0),(Just 1)],[(Just 4)],[(Just 6),Nothing ],[],[Nothing ]]" (Just 11) (sumMaybe [[(Just 0),(Just 1)],[(Just 4)],[(Just 6),Nothing ],[],[Nothing ]]) )
p3b_additionalTest2 = TestCase (assertEqual "sumMaybe [[Nothing],[],[Nothing ]]" (Just 0) (sumMaybe [[Nothing],[],[Nothing ]]) )

p3c_test1 = TestCase (assertEqual "sumEither [[IString \"1\",IInt 2,IInt 3],[IString \"4\",IInt 5],[IInt 6,IString \"7\"],[],[IString \"8\"]]" (IInt 36) (sumEither [[IString "1",IInt 2,IInt 3],[IString "4",IInt 5],[IInt 6,IString "7"],[],[IString "8"]]) )
p3c_test2 = TestCase (assertEqual "sumEither [[IString \"10\" , IInt 10],[],[IString \"10\"],[]]" (IInt 30) (sumEither [[IString "10" , IInt 10],[],[IString "10"],[]]) )
p3c_test3 = TestCase (assertEqual "sumEither  [[]]" (IInt 0) (sumEither  [[]]) )
p3c_additionalTest1 = TestCase (assertEqual "sumEither [[IString \"5\",IInt 7,IInt 9],[IString \"11\",IInt 13],[IInt 15,IString \"17\"],[],[IString \"19\"]]" (IInt 96) (sumEither [[IString "5",IInt 7,IInt 9],[IString "11",IInt 13],[IInt 15,IString "17"],[],[IString "19"]]) )
p3c_additionalTest2 = TestCase (assertEqual "sumEither [[IString \"1\",IInt 6],[IInt 5],[IString \"7\"],[]]" (IInt 19) (sumEither [[IString "1",IInt 6],[IInt 5],[IString "7"],[]]) )

p4a_test1 = TestCase (assertEqual "depthScan t1"  ["School","of","Electrical","Engineering","and","Computer","Science"] (depthScan t1) ) 
p4a_test2 = TestCase (assertEqual "depthScan t2" [4,5,3,6,2,8,9,7,1] (depthScan t2) ) 
p4a_additionalTest1 = TestCase (assertEqual "depthScan additionalTree1" ["I","am","beautiful","and","smart","lady","!"] (depthScan additionalTree1) ) 
p4a_additionalTest2 = TestCase (assertEqual "depthScan additionalTree2" [14,15,13,16,12,18,19,17,11] (depthScan additionalTree2) ) 

p4b_test1 = TestCase (assertEqual "depthSearch t3 1" 3 (depthSearch t3 1) ) 
p4b_test2 = TestCase (assertEqual "depthSearch t3 5" 4 (depthSearch t3 5) )
p4b_test3 = TestCase (assertEqual "depthSearch t3 4" (-1) (depthSearch t3 4) )
p4b_additionalTest1 = TestCase (assertEqual "depthSearch t3 2" 4 (depthSearch t3 2) )
p4b_additionalTest2 = TestCase (assertEqual "depthSearch t3 3" 3 (depthSearch t3 3) )

addedTree = NODE 2 (NODE 4 (NODE 6 (LEAF 4) (LEAF 5)) (LEAF 12)) (NODE 14 (NODE 16 (LEAF 10) (LEAF 11)) (LEAF 18))
p4c_test1 = TestCase (assertEqual ("addTrees "++ (show left) ++ (show right)) addedTree  (addTrees left right) ) 
additionalAddedTree = NODE 4 (NODE 4 (NODE 6 (LEAF 4) (LEAF 5)) (LEAF 12)) (NODE 18 (NODE 16 (LEAF 10) (LEAF 11)) (LEAF 2))
p4c_additionalTest1 = TestCase (assertEqual ("addTrees "++ (show left) ++ (show right)) additionalAddedTree (addTrees additionalLeft additionalRight) )  

p5_tree1test1 = TestCase (assertEqual "depthScan tree1" [5,3,6,2,4,8,9,7,1] (depthScan tree1) )
p5_tree1test2 = TestCase (assertEqual "depthSearch tree1 5" 4 (depthSearch tree1 5) )
p5_tree2test1 = TestCase (assertEqual "depthScan tree2" [6,4,3,7,11,5,10,9,1] (depthScan tree2) )
p5_tree2test2 = TestCase (assertEqual "depthSearch tree2 10" 3 (depthSearch tree2 10) )
p5addedTree = NODE 2 (NODE 7 (NODE 12 (LEAF 5) (LEAF 3)) (LEAF 6)) (NODE 16 (NODE 13 (LEAF 7) (LEAF 11)) (LEAF 19))
p5_test3 = TestCase (assertEqual ("addTrees "++ (show left) ++ (show right)) p5addedTree (addTrees tree1 tree2) ) 


tests = TestList [ TestLabel "Problem 1a - test1 " p1a_test1,
                   TestLabel "Problem 1a - test2 " p1a_test2,
                   TestLabel "Problem 1a - test3 " p1a_test3,
                   TestLabel "Problem 1a - additionalTest1 " p1a_additionalTest1,
                   TestLabel "Problem 1a - additionalTest2 " p1a_additionalTest2,                   
                   TestLabel "Problem 1b - test1 " p1b_test1,
                   TestLabel "Problem 1b - test2 " p1b_test2,                   
                   TestLabel "Problem 1b - test3 " p1b_test3,
                   TestLabel "Problem 1b - additionalTest1 " p1b_additionalTest1,
                   TestLabel "Problem 1b - additionalTest2 " p1b_additionalTest2,                                      
                   TestLabel "Problem 1c - test1 " p1c_test1,
                   TestLabel "Problem 1c - test2 " p1c_test2,
                   TestLabel "Problem 1c - test3 " p1c_test3, 
                   TestLabel "Problem 1b - additionalTest1 " p1c_additionalTest1,
                   TestLabel "Problem 1b - additionalTest2 " p1c_additionalTest2,                                     
                   TestLabel "Problem 2  - test1 " p2_test1,
                   TestLabel "Problem 2  - test2 " p2_test2,  
                   TestLabel "Problem 2  - test3 " p2_test3,
                   TestLabel "Problem 2 - additionalTest1 " p2_additionalTest1,
                   TestLabel "Problem 2 - additionalTest2 " p2_additionalTest2,
                   TestLabel "Problem 3a - test1 " p3a_test1,
                   TestLabel "Problem 3a - test2 " p3a_test2,  
                   TestLabel "Problem 3a - test3 " p3a_test3, 
                   TestLabel "Problem 3a - additionalTest1 " p3a_additionalTest1,
                   TestLabel "Problem 3a - additionalTest2 " p3a_additionalTest2,                   
                   TestLabel "Problem 3b - test1 " p3b_test1,
                   TestLabel "Problem 3b - test2 " p3b_test2,
                   TestLabel "Problem 3b - test3 " p3b_test3,
                   TestLabel "Problem 3b - additionalTest1 " p3b_additionalTest1,
                   TestLabel "Problem 3b - additionalTest2 " p3b_additionalTest2,
                   TestLabel "Problem 3c - test1 " p3c_test1,
                   TestLabel "Problem 3c - test2 " p3c_test2,
                   TestLabel "Problem 3c - test3 " p3c_test3,
                   TestLabel "Problem 3c - additionalTest1 " p3c_additionalTest1,
                   TestLabel "Problem 3c - additionalTest2 " p3c_additionalTest2,
                   TestLabel "Problem 4a - test1 " p4a_test1,
                   TestLabel "Problem 4a - test2 " p4a_test2,
                   TestLabel "Problem 4a - additionalTest1 " p4a_additionalTest1,
                   TestLabel "Problem 4a - additionalTest2 " p4a_additionalTest2,
                   TestLabel "Problem 4b - test1 " p4b_test1,
                   TestLabel "Problem 4b - test2 " p4b_test2,
                   TestLabel "Problem 4b - test3 " p4b_test3,
                   TestLabel "Problem 4b - additionalTest1 " p4b_additionalTest1,
                   TestLabel "Problem 4b - additionalTest2 " p4b_additionalTest2,
                   TestLabel "Problem 4c - test1 " p4c_test1,
                   TestLabel "Problem 4c - additionalTest1 " p4c_additionalTest1,
                   TestLabel "Problem 5 - tree1test1 " p5_tree1test1,
                   TestLabel "Problem 5 - tree1test2 " p5_tree1test2,
                   TestLabel "Problem 5 - tree2test1 " p5_tree2test1,
                   TestLabel "Problem 5 - tree2test2 " p5_tree2test2,
                   TestLabel "Problem 5 - test3 " p5_test3
                 ] 
                  

-- shortcut to run the tests
run = runTestTT  tests