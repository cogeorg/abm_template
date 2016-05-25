**abm_template** is a template for writing financial agent-based models in python. Despite it being aimed at financial agent-based models, it may easily be used for other economic agent-based models, albeit it is a bit too specific for agent-based models outside economics. It uses abstract base classes and is provided with a sample implementation in sample_model.py. The use of abstract based classes in agent-based modelling, and specifically the abm_template ensures high degree of intercompatibility between agent-based models created based on this framework. This renders this library particularly useful for institutions or groups of people who create multiple agent-based models, and want to gain extra value from being able to reuse and interchange parts of them in new work easily. For instance, it may be very useful for reseach groups, and for student projects which can grow and enrich a common library over time. The below will explain the structure of the library, the purpose of specific folders and files, as well as the sample implementation. For the documentation of specific functions please see the source code (particularly docstrings and comments).

The main part of the abm_template, as in the abstract class template itself, is stored in the **/src/** folder, and contains abstract classes for parts of an abstract agent-based model. These are described below:

- **baseagent.py**: a template for agents within the simulator, the agents which inherit from **BaseAgent** will thus have the same characteristics even if they are of distinct classes and distinct instances. Then these agents can be used within models in a consistent manner without worrying about the generic interface of an agent changing for each one. As such, each agent will have an identifier (a string, should be unique), parameters (a dictionary), state variables (a dictionary), and accounts (a list of transactions, see below: **bastransaction.py**). This file also specifies a standard way of printing an agent, standard way of importing the above from config files, and some standard other functions commonly used with agents within simulation.

- **baseconfig.py**: a template for the config of the simulator, or in other words the environment in which the agents above reside. Config is used to store all values in the simulation that pertains to all agents and not a specific one (those are stored in the agents themselves), as such it's the representation of the environment in which agents operate within the simulation. Thus, each instance of **BaseConfig** will have an identifier (a string, should be unique - usually there's only one environment but this does not need to be the case, we can have two environments representing two countries), static parameters, variable parameterss (both dictionaries), shocks, agents (lists). The file also specifies the commonly used standard functions for configs, including parameter handling, reading and writing config files, and finding agents by their IDs.

- **basemarket.py**: a template for market clearing mechanisms. In particular it implements a tatonnement function, which performs a Walrasian auction given a list of sellers (actual instances) and their supply functions (should only take the price as a parameter, though these can obviously depend on the agents' internal parameters), as well as a starting price from which the search algorithm begins. This procedure implements exponential search and should converge fast given properly defined supply and demand functions. **BaseMarket** also implements rationing procedures, which perform rationing given a list of agents and their excess supply or demand (negative number indicates demand, positive supply). Standard function performs this randomly, there is also a proportional version, which assigns transactions proportionately to the initial supply and demand, though the actual pairs of agents within the transactions are still randomly selected. The abstract version of rationing is the procedure which takes two additional functions as parameters, a matching functions which specifies for two agents the priority they are given in the queue (a float, the higher it is the higher the priority), and a binary function specifying whether a transaction between a pair of agents is allowed (returns a boolean value). Thus in this version the pairs are no longer random, and depend strictly on these two functions. In the future this class should also implement a limited order book.

- **basemeasurement.py**: a template for a class which handles the writing of the output of the model. The instance of this class will read a config specifying the name of the output file, and what should be written to its columns. The output file is always a csv file. **BaseMeasurement** class includes prototypes of standard functions, including ones for reading the config, opening (creating) the output file, writing to the file, and closing the file (these are usually called within the Runner class, see below). There is also a wrapper function, which in a concrete implementation consist of the specification of calculations that return the values to be saved in the output file and their connection with appropriate identifiers in the config file.

- **basemodel.py**: a template for a class which handles the updating of the model, that is the actual mechanism of the model. Ensures each instance has an identifier (a string, should be unique), model parameters (a dictionary), and interactions. Also ensures the updating is called from a function called **do_update** which contains the main update look, and may be linking to other functions in concrete implementations. The updating is to be called in the main loop in the runner. This can be observed in the sample model described below, even though it's a simple game theoretic model.

- **baserunner.py**: a template for a class which handles the running of the model, and calls Measurement, Updater, and Shocks classes. The instance of this class will have an indentifier (a string, should be unique if multiple runners are involved), number of sweeps per simulation (an integer). Ensures the main loop is called **do_run** in every implementation.

- **baseshock.py**: a template for a class which handles the shocks in the model. Ensures the shocks are run through a standard function **do_shock**. The shocks are to be called in the main loop in the runner. The nature of shocks very much depends on the concrete implementation, and as such only the above function is specified.

- **basetransaction.py**: a template for a class container for transactions. Intances of this class are supposed to represent transactions between agents and be assigned to assets within the agents in the simulation. This class ensures each transaction has a type (string), asset (string), from (agent), to (agent) , amount (float), interest (float), maturity (integer), time_of_default (integer). This class also ensures each transaction has a unique identifier (UUID), and contains some useful standard functions for adding or removing transaction to or from the books of agents, clearing or purging accounts, among others.

- **goodness.py**: this file is not a part of the abstract template as such, but is a tool that helps with agent-based models on an abstract level. This script allows for testing hypotheses given an output from an agent-based model. The details of how this scripts works are contained in the source code, extensive comments, and the sample script described below, but in general this script finds the goodness of the studied model through looking at the distance of the results from the target specified in the hypothesis. The idea is to run the model many times with varying parameters and see how good it does in relation to the hypotheses posed. This can be done for multivariate case as well.

The **/configs/** folder has sample config files that are needed by the instances of the abstract classes, these are in particular necessary for **BaseConfig**, **BaseRunner**, and **goodness**. Config files in **abm_template** are xml files, the structure of these is described within the source code, usually in the docstring of the function reading the config.

The **/samples/** folder consists of sample files necessary for the samples. Currently has mock outputs of an agent-based model, which we use for testing the goodness.py script. The folder also contains the concrete implementation of the above classes for the purposes of the example specified below.

The **/tests/** folder is very important. It contains tests for the template source files as described above. In principle every function should have a test written in here. We cannot directly test abstract base classes, as these cannot be instantialised. To test we create a minimal concrete implementations of these abstract classes, which only inherit the code in the abstract base class and don't add anything specific to the concrete implementation, and run tests on these. These tests are under development currently.

In the main folder we have the sample implementation of the **abm_template**, as described below. We also have the **calc_goodness.py** file which is a sample implementation of the **goodness.py** script. Further, the **abm_template_tests.py** invokes the tests described above.

The sample implementation is very basic and shows to implement the abstract base classes, the implementation is of a simple game with parameter
theta (a parameter which makes the payout matrix variable, as it depends on this parameter, thus creates a game which depends on this parameter), two agents, two choices of action (1,0) and a payout matrix (see a primer on game theory in case of doubts):

```
  	 1   				0
1 [	(1-theta,1-theta)	(-theta,0)	]
0 [	(0,-theta)			(0,0)		]
```

There are simple equilibria in this model:
Note that theta is known to both agents, there is common knowledge about theta.
If theta < 0, both agents find attack the dominant action: unique Nash equilibrium: {1, 1}
If theta > 1, both agents find refrain the dominant action: unique Nash equilibrium: {0, 0}
If theta is between [0, 1] both equilibria can be sustained as pure strategy Nash equilibria.

The main part of the simulation is the **sample_model.py** which specifies the above, but other classes are also implemented as necessary. The files associated with the sample implementation have names prefixed with sample, thus are easy to find or copy as a lump.

To run the sample implementation use:

```
python sample.py
```

All feature requests and bugs should be brought to the attention of the authors through issues in the github repository, or though email to one of the below addresses.

co-pierre.georg@uct.ac.za

pawel.fiedor@uct.ac.za

2016
