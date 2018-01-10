# Text Summarizer


## Summary:

Based on [this](https://www.reddit.com/r/dailyprogrammer/comments/683w4s/20170428_challenge_312_hard_text_summarizer/?st=jbuzvkww&sh=6b3755be) challenge from r/dailyprogrammer this project reads in a paragraph/article from a file and summarizes it in 3 sentences.  

## Breakdown:

Given an article/paragraph, and a set of stopwords(words in the English language that are common) the program analyzes each sentence for unique words, weights each sentence/gives each sentence a score, and provides a summary based on the 3 highest scoring sentences in chronological order.  


## Example Input/Output:

Input:

```
The purpose of this paper is to extend existing research on entrepreneurial team formation under a competence-based perspective by empirically testing the influence of the sectoral context on 
that dynamics. We use inductive, theory-building design to understand how different sectoral characteristics moderate the influence of entrepreneurial opportunity recognition on subsequent 
entrepreneurial team formation. A sample of 195 founders who teamed up in the nascent phase of Interned-based and Cleantech sectors is analysed. The results suggest a twofold moderating effect 
of the sectoral context. First, a technologically more challenging sector (i.e. Cleantech) demands technically more skilled entrepreneurs, but at the same time, it requires still fairly 
commercially experienced and economically competent individuals. Furthermore, the business context also appears to exert an important influence on team formation dynamics: data reveals that 
individuals are more prone to team up with co-founders possessing complementary know-how when they are starting a new business venture in Cleantech rather than in the Internet-based sector. 
Overall, these results stress how the business context cannot be ignored when analysing entrepreneurial team formation dynamics by offering interesting insights on the matter to prospective entrepreneurs and interested policymakers.
```

Output:

```
Unique/interesting words from the provided text: team, entrepreneurial, formation, influence, sectoral, context, business

The purpose of this paper is to extend existing research on entrepreneurial team formation under  a competence-based perspective by empirically testing the influence of the sectoral context on  that dynamics.

We use inductive, theory-building design to understand how different sectoral  characteristics moderate the influence of entrepreneurial opportunity recognition on subsequent  entrepreneurial team formation.

Furthermore, the business context  also appears to exert an important influence on team formation dynamics: data reveals that  individuals are more prone to team up with co-founders possessing complementary know-how when they  are starting a new business venture in Cleantech rather than in the Internet-based sector
```


