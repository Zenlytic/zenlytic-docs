
# Topics

Topics are collections of tables (views) that can be joined together using foreign keys. They are specified in their own yaml files. Each topic uses its model's `connection` that it is defined in to get data.

Topics exist to let you specify sections of your data that join together. They let you specify an explicit base view, and how joins work to connect other views to that base view. 

You do not need to specify a join to add a view to a topic if there is already a join from the view you're adding to the base view of the topic. If you want to override that existing join, you can do so on the topic, and that will change the logic of how the view you're adding is joined into the topic.

Topics are how Zoë understands what views join together and how she finds data that is related to each other.

