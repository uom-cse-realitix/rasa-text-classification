# Text Classification based on RASA NLU

Tested multiple word embeddings.

## Supervised Embeddings

Supervised Embeddings: Intent Classifier TensorFlow Embedding

The intent classifier `intent_classifier_tensorflow_embedding` was developed by Rasa and is inspired by Facebook’s starspace paper. Instead of using pretrained embeddings and training a classifier on top of that, it trains word embeddings from scratch. It is typically used with the `intent_featurizer_count_vectors` component which counts how often distinct words of your training data appear in a message and provides that as input for the intent classifier. In the illustration below you can see how the count vectors would differ for the sentences My bot is the best bot and My bot is great, e.g. bot appears twice in My bot is the best bot. Instead of using word token counts, you can also use ngram counts by changing the analyzer property of the `intent_featurizer_count_vectors` component to char. This makes the intent classification more robust against typos, but also increases the training time.

<img src="https://blog.rasa.com/content/images/2019/02/image.png" >

Furthermore, another count vector is created for the intent label. In contrast to the classifier with pretrained word embeddings the tensorflow embedding classifier also supports messages with multiple intents (e.g. if your user says Hi, how is the weather? the message could have the intents greet and ask_weather) which means the count vector is not necessarily one-hot encoded. The classifier learns separate embeddings for feature and intent vectors. Both embeddings have the same dimensions, which makes it possible to measure the vector distance between the embedded features and the embedded intent labels using cosine similarity. During the training, the cosine similarity between user messages and associated intent labels is maximized.

## Setting up

Please use the exported `conda` environment file named as `environment.yml` in the root directory in order to set up the environment for this project. Change the `prefix` in the file accordingly.

## References

1. [Rasa NLU in Depth: Part 1 – Intent Classification](https://blog.rasa.com/rasa-nlu-in-depth-part-1-intent-classification/)
2. [Enhancing Rasa NLU models with Custom Components](https://blog.rasa.com/enhancing-rasa-nlu-with-custom-components/)
3. [Text Classification using SpaCy](https://www.kaggle.com/poonaml/text-classification-using-spacy)
4. [Class Imbalance](https://rasa.com/docs/rasa/nlu/choosing-a-pipeline/#class-imbalance)
3. [Text Classification using SpaCy](https://www.kaggle.com/poonaml/text-classification-using-spacy)