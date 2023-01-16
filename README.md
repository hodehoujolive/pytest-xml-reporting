# GenerateXMLTestReport
Blog : How to generate test report using Pytest in XML?

### **Setting Up Pytest**


The installation of Pytest is simple. If you have cloned the repository, it is already installed, and you can skip this step. If you have not cloned the repository, follow these steps:

Make sure you have Homebrew on your machine because we will use a macOS operating system in this tutorial on how to generate test reports using pytest in XML.

- Type the following command in your terminal.

**brew install pipenv**


- Creation of Pipfile in an empty directory. This file is essential for using Pipenv. It's used to track your project's dependencies if you need to reinstall them.

[[Pipfile (github.com)](https://gist.github.com/hodehoujolive/06d8e8235737a49208fa3de4608d805c)

The python\_version parameter is the version of the base interpreter you specified when creating a new pipenv environment.

The packages section is the place where you can list the packages required for your project. "\*" is for installing the latest stable versions of the packages.

At the time of writing this blog on how to get the current URL in Selenium Python, the latest versions of Pytest and Selenium are Pytest 7.1.2 and 4.2.2, respectively.

- In your terminal, go to the directory and install the latest stable versions of the Pytest and Selenium packages with the command:

**Pipenv Install**
