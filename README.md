# Crochet-Simulator
*Simulate basic crochet stitches, gauge squares and patterns!*

By Hannah Gross ~ MIDS Spring 2021 ~ hannah.gross@berkeley.edu


Inspired by my sweater-wearing 15lb chihuahua, Stellaluna, Crochet Simulator was developed as a tool to help myself, and other avid crochet people properly size their crocheted wearables. This project draws on the traditional sizing solution - gauge squares - and goes further to allow users to simulate full on crochet patterns. The Simulator also functions as an inventory where the user can record and save their previously created yarns, stitches, rows and patterns.

This project is also attributable to Bill Lubanovic, who in the first chapter of *‘Introducing Python, Modern Computing in Simple Packages’* demonstrated the complexity of computer programming with just a few rows of a knitting pattern. The parallels between crochet and programming were simply far too compelling for me to ignore. Both communicate algorithms in their own languages, require an interpreter and are used to create complex structures with only a few basic elements. In programming those elements would be basic data types, in crochet there is yarn, hook and stitch type. We use these three elements to create stitches, the simplest structure in crochet. Every attribute of a stitch is derived from its three basic elements. Those attributes are height, width, weight, and the amount of yarn needed to create it. With stitches, we can create rows, imagine a one-dimensional array of stitches. Then we can create patterns, vertically stacked rows, imagine a multi-dimensional array of stitches. Again, every data attribute of a stitch, row, and pattern come from these basic compositional elements.

Traditional ontologies depict complex systems of inheritance, where objects are structured based on shared attributes. I found that the relationship between my objects was not hierarchical and my more complex objects (stitch, row and pattern) all shared the same attributes. This realization informed the underlying philosophy of my project, ontology composition. Put simply, ontology composition is the idea of creating new objects by combining other objects. With just a few data attributes of yarn, hook and stitch type, we can perform simple calculations to predict the final metrics of complex crochet projects, thus solving the issue of sizing crocheted wearables.

![Stellaluna in her purple sweater](https://github.com/[hannah144]/[Crochet-Simulator]/blob/[master]/Images/Stellaluna_Purple_Sweater.png?raw=true)
