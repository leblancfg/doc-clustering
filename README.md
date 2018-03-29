# doc-clustering
Simple use of [Natural Language Processing](https://en.wikipedia.org/wiki/Natural_language_processing) (NLP) to help cluster Service Desk tickets into categories.

## How it works
The script uses a process called [Latent Dirichlet Allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) (LDA) to model the content of the documents into a mixture of topics. These topics are then tied to certain words, each with its probability distribution. We can then use that model to predict the topics contained in documents it has never seen before. In our particular implementation, we can then automatically suggest to our Service Desk users the most probable action to take, or boilerplate response to send back, based on the contents of the ticket.

## Requirements
The script was written with, and only tested on,
* python==2.7.12
* gensim==0.13.1
* nltk==3.2.1
* stop_words==2015.2.23.1 

## Reference
Multilingual topic models for unaligned text, by J Boyd-Graber, DM Blei

(http://www.auai.org/uai2009/papers/UAI2009_0194_e9b915894f2228eb675c97f199bebe6d.pdf)

Latent Dirichlet Allocation (LDA) with Python by Jordan Barber

(https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html)

## Next Steps
This project is now archived. It has been useful to solve a one-time problem my team was facing. Unless this situation arises again, no additional work will be put in.

Here are some suggestions for next steps to undertake:
* Turn into more global package, for use in data pipeline
* As incoming text was both french and english, could be made to also spit out detected language -> better boilerplate reply recommendations.
