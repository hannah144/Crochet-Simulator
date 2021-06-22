# Crochet-Simulator
*Simulate basic crochet stitches, gauge squares and patterns!*

By Hannah Gross ~ MIDS Spring 2021 ~ hannah.gross@berkeley.edu


Inspired by my sweater-wearing 15lb chihuahua, Stellaluna, Crochet Simulator was developed as a tool to help myself, and other avid crochet people properly size their crocheted wearables. This project draws on the traditional sizing solution - gauge squares - and goes further to allow users to simulate full on crochet patterns. The Simulator also functions as an inventory where the user can record and save their previously created yarns, stitches, rows and patterns.

This project is also attributable to Bill Lubanovic, who in the first chapter of *‘Introducing Python, Modern Computing in Simple Packages’* demonstrated the complexity of computer programming with just a few rows of a knitting pattern. The parallels between crochet and programming were simply far too compelling for me to ignore. Both communicate algorithms in their own languages, require an interpreter and are used to create complex structures with only a few basic elements. In programming those elements would be basic data types, in crochet there is yarn, hook and stitch type. We use these three elements to create stitches, the simplest structure in crochet. Every attribute of a stitch is derived from its three basic elements. Those attributes are height, width, weight, and the amount of yarn needed to create it. With stitches, we can create rows, imagine a one-dimensional array of stitches. Then we can create patterns, vertically stacked rows, imagine a multi-dimensional array of stitches. Again, every data attribute of a stitch, row, and pattern come from these basic compositional elements.

Traditional ontologies depict complex systems of inheritance, where objects are structured based on shared attributes. I found that the relationship between my objects was not hierarchical and my more complex objects (stitch, row and pattern) all shared the same attributes. This realization informed the underlying philosophy of my project, ontology composition. Put simply, ontology composition is the idea of creating new objects by combining other objects. With just a few data attributes of yarn, hook and stitch type, we can perform simple calculations to predict the final metrics of complex crochet projects, thus solving the issue of sizing crocheted wearables.

<p align="center">
  <img width=100% height=100% alt="Poncho+Sample_Blanket" src="https://github.com/hannah144/Crochet-Simulator/blob/256290ac4cf2ebfcfe0a652eddcaa7ff42e6d37f/Images/Picture1.png">
</p>

## Instructions

This project is intended for people familiar with crochet patterns, therefore the tester may experience some difficulty operating some of the high-level functions in this program. Because of this, I will provide some examples of row patterns and pattern sequences for the tester to reference. Additionally, there are some help functions within my code.

> Step 1. Access the command line and go to the local directory that houses Crochet Simulator.
> Step 2. Enter ’python crochet_simulator.py’ to begin.
> Step 3. Explore low-level functions! I suggest navigating the main menu and viewing pre-made objects. Navigation commands are prompted. Feel free to add a yarn, create a stitch or simulate a gauge square.
> Step 4. Explore high-level functions with care. As much as I’ve tried to protect against user error, this program expects a certain level of proficiency. To make a new row, you will have to select the stitches needed to construct it. Then you will be prompted to specify a row pattern. 

Creating a new pattern is like creating a row, but instead of stitches, patterns are created from rows. Below are some row patterns and pattern sequences for easy testing. If you’re feeling brave, you could also try to recreate some of my test gauge squares in Crochet Simulator Data.xlsx to see how accurate the predictions are.

#### Row Patterns:
> Sample 1: a*15 
> Sample 2: c + (a+b)*7

#### Pattern Sequence (use the row patterns above):
*Note: adding rows follows the same rules as matrix addition*
> Sample: (a+b)*10


