---
title: Making Transformers Digestible
description: Understanding transformers in LLMs using McDonalds!
slug: making-transformers-digestible
authors: pglover
tags: [ai, llm, large-language-models, transformers, engineering]
---

# Making Transformers Digestible: As Easy As Ordering at McDonald's

If you're finding it hard to wrap your head around how Transformer models in natural language processing work, allow me to simplify it for you. Let's use an analogy we can all relate to—ordering food at McDonald's!

![An example Transformer](/img/blogs/2023-07-05-Transformers/transformer.png)

<!--truncate-->

## Step 1: The Order - Encoder (Input Embedding and Positional Encoding)

When you place an order at McDonald's, think of it as an input sentence. The cashier takes your order and understands it. This is like the 'Input Embedding' component in a Transformer model, which transforms your words (order) into a format that the model (in this case, the kitchen) can understand.

Moreover, if you have special requests, say, 'no pickles,' the cashier notes this down. This process resembles 'Positional Encoding' in our Transformer model. Positional Encoding ensures that the model acknowledges the order of words in a sentence—just like how the cashier pays attention to the specific details of your order.

## Step 2: Preparing the Order - Encoder (Self-Attention and Feed-Forward)

Once your order makes its way to the kitchen, the chefs come into the picture. They are like the 'Self-Attention' mechanism in the Transformer model. They understand the roles of each item and how they relate to each other. For instance, they know that the extra cheese you requested should be on your burger and not your fries.

Following that, the 'Feed-Forward' network steps in, akin to the assembly line workers. They prepare your meal just as you requested, without questioning why you wanted extra cheese on your burger and not on your fries.

## Step 3: Quality Check - Decoder (Self-Attention and Feed-Forward)

Next, our Decoder acts like a quality check and packaging station. Here, another round of chefs, resembling 'Self-Attention', inspect your meal to ensure that it is made just right. Then, the packaging team, akin to the 'Feed-Forward' network, packs up your order. They do not make any changes to your original request, their job is to make sure your order is neatly packed and ready for delivery.

## Step 4: Consistent Communication - Decoder (Enc-Dec Attention)

It's important to note that the quality-check chefs maintain a direct line of communication with the preparation chefs. This is the 'Encoder-Decoder Attention' layer of a Transformer model. The Decoder can refer back to different parts of the input sentence, just like how the quality-check team can query the preparation team about the specifics of the original order. This step ensures that the Decoder has all the information it needs from the Encoder to accurately generate the output.

## Step 5: Bon Appétit! - Output

Finally, your neatly packed meal is handed over to you—this is the output sentence from the Transformer model. Your meal is ready, prepared exactly as you ordered, quality checked, and packed. 

In a Transformer model, there are multiple layers. It's like repeating the whole ordering, cooking, quality check, and packaging process several times to ensure your meal is as perfect as it can be. 

The Encoder processes the input (much like the kitchen staff preparing your order), the Decoder generates the output (like the quality-check and packaging process), and they communicate to ensure the final result is spot-on.

Hopefully, this analogy will help make the concept of Transformer models a little more digestible! After all, who knew understanding AI could make you hungry? Bon appétit!
