# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:05:47 2018

@author: rjr
"""

# A script to implement a forgetting curve algorithm


"""
Having observed that subsequent inter-repetition intervals are increasing by an approximately constant factor (e.g. two in the case of the SM-0 algorithm for English vocabulary), I decided to apply the following formula to calculate inter-repetition intervals:

I(1):=1
I(2):=6
for n>2 I(n):=I(n-1)*EF

where:

I(n) - inter-repetition interval after the n-th repetition (in days)
EF - easiness factor reflecting the easiness of memorizing and retaining a given item in memory (later called the E-Factor).

E-Factors were allowed to vary between 1.1 for the most difficult items and 2.5 for the easiest ones. At the moment of introducing an item into a SuperMemo database, its E-Factor was assumed to equal 2.5. In the course of repetitions this value was gradually decreased in case of recall problems. Thus the greater problems an item caused in recall, the more significant was the decrease of its E-Factor.

Shortly after the first SuperMemo program had been implemented, I noticed that E-Factors should not fall below the value of 1.3. Items having E-Factors lower than 1.3 were repeated annoyingly often and always seemed to have inherent flaws in their formulation (usually they did not conform to the minimum information principle). Thus not letting E-Factors fall below 1.3 substantially improved the throughput of the process and provided an indicator of items that should be reformulated. The formula used in calculating new E-Factors for items was constructed heuristically and did not change much in the following 3.5 years of using the computer-based SuperMemo method.

In order to calculate the new value of an E-Factor, the student has to assess the quality of his response to the question asked during the repetition of an item (my SuperMemo programs use the 0-5 grade scale - the range determined by the ergonomics of using the numeric key-pad). The general form of the formula used was:

EF':=f(EF,q)

where:

EF' - new value of the E-Factor
EF - old value of the E-Factor
q - quality of the response
f - function used in calculating EF'.

The function f had initially multiplicative character and was in later versions of SuperMemo program, when the interpretation of E-Factors changed substantially, converted into an additive one without significant alteration of dependencies between EF', EF and q. To simplify further considerations only the function f in its latest shape is taken into account:

EF':=EF-0.8+0.28*q-0.02*q*q

which is a reduced form of:

EF':=EF+(0.1-(5-q)*(0.08+(5-q)*0.02))

Note, that for q=4 the E-Factor does not change.

Let us now consider the final form of the SM-2 algorithm that with minor changes was used in the SuperMemo programs, versions 1.0-3.0 between December 13, 1987 and March 9, 1989 (the name SM-2 was chosen because of the fact that SuperMemo 2.0 was by far the most popular version implementing this algorithm).
"""

# Have the user input a number on a 0 - 5 scale (userRecall) (lowest - highest).  
# (userRecall / 100) * 2 will be the difficulty score which is associated with the notecard object ("correct" is 0.6)
