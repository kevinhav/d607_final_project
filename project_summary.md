# Disc Golf Flight Numbers

## Summary

For my final DATA 607 project, I thought it would be interesting to revisit one of my very first personal data projects and rebuild it, applying what I've learned throughout the semester. I'm an avid disc golfer, and seeing the sport starting to develop its scientific knowledge base has been very exciting and interesting to experience as I grow as a data scientist in parallel. 

### Introduction to disc golf's current climate

Disc golf is a relatively new sport that has experienced an explosive growth trajectory in the past couple of decades. Assuming you are familiar with golf, disc golf has a very similar format and scoring mechanic, with the main difference being that instead of clubbing golf balls into a hole, players throw flying discs, similar to Frisbees, into a target, usually in the form of a specific basket.

The modern version of the sport has been around for about half a century, and during the COVID-19 pandemic, experienced an explosion in popularity due to its ease of access, affordability, and low contact. With this sudden trajectory, the disc golf community has found itself flooded with new data, information, and perspectives. In a flood of new money and new players, the community found its current knowledge resources to be insufficient and has been turning to data-driven science to answer its questions.

Directly engaging in this exciting and dynamic time, I'd like to take a data science based approach to review one of the most well-known and yet mysterious frameworks in this sport; the disc golf Flight Rating System.


### Flight numbers and their challenges

One of the unique components to disc golf is its namesake; the discs. Disc golf discs are designed to be thrown much further than your standard Frisbee; elite distance players can throw these discs 600-700+ feet through the air, and even for amateurs, 250' to 400' is not uncommon.

The physics of these discs is very interesting and surprisingly complex; very small differences in the physical attributes, including shape, ratios, and plastic blends of the disc can result in a surprising differences in how two discs fly. One of the original disc golf manufacturers, Innova Disc Golf, invented a system to help try to categorize discs based on these physical attributes, so players could have an idea of how a disc would perform before purchasing. They named this framework the Innova Flight Number System.

 This system categorizes discs by four measures, which are represented numerically on their own disctinct scales.

- **Speed**: how fast the disc must be thrown in order to fly as the manufacturer intended
- **Glide**: how easily the disc is expected to move through the air
- **Turn**: the gyroscopic stability of the disc at *high* speeds (i.e. how the disc acts when first thrown)
- **Fade**: the gyroscopic stability of the disc at *low* speeds (i.e. how the disc acts as it finishes its flight)

While this system has been widely adopted by the community and other manufacturers as a standard, with every disc expected to have a set of flight numbers, the system is opaque and surrounded by mystery, with many in the community simply decrying the entire framework, expressing "flight numbers don't matter" as a common idiom.

A combination of player skill levels, differences in how manufacturers apply the flight number system, and even the plastic polymers that the disc is made from result in a wide range of characteristics from similarly classified discs.

### Comparing the flight number system to physical disc characteristics

My goal is to take physical measurements of common disc molds and compare them against their advertised flight numbers to see if there is a concrete relationship we can discover between the two.

For flight numbers, I will use the specifications provided by the original disc golf disc manufacturer, Innova Disc Golf, for many of their popular molds.

For the phsyical characteristics, I will use measurements provided by the Professional Disc Golf Association (PDGA), the organization that reviews and approves every disc for professional play.

My goal is not necessarily to predict a set of flight numbers for a given disc, but to instead simply evaluate if there are any measurable relationships between the physical characteristics of a given disc mold and its prescribed flight numbers.

### Additional Information

[Brief History of Disc Golf and the PDGA](https://www.pdga.com/history)

[Innova Flight Ratings System](https://www.innovadiscs.com/home/disc-golf-faq/flight-ratings-system/)

[PDGA Equipment Technical Standards](https://www.pdga.com/technical-standards/)