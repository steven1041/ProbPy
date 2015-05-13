#!/usr/bin/env python3

from setuptools import setup
import sys

sys.path.append("ProbPy")
import ProbPy

setup(name="ProbPy",
      version="1.1",
      description="Multi Variable Probability Calculus Library",
      long_description="ProbPy is a Python library that aims to simplify" +
                       "calculations with discrete multi variable" +
                       "probabilistic distributions by offering an" +
                       "abstraction over how data is stored and how the" +
                       "operations between distributions are performed.\n" +
                       "\n" +
                       "The library can be used in the implementation of" +
                       "many algorithms such as Bayes Theorem, Bayesian" +
                       "Inference algorithms like Variable Elimination," +
                       "Gibbs Ask (MCMC), HMMs implementations," +
                       "Information Theory, etc.\n" +
                       "\n" +
                       "Currently, there are implementation for Bayesian" +
                       "and Markov Networks with some inference" +
                       "algorithms implemented.\n"
                       "\n" +
                       "For more information check the GitHub page at:" +
                       "https://github.com/petermlm/ProbPy.",

      author="Pedro Melgueira",
      author_email="pedromelgueira@gmail.com",

      url="https://github.com/petermlm/ProbPy",

      packages=["ProbPy"],

      keywords='probability calculus random variable bayes bayesian network \
               information theory markov',
      license="MIT License",
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Education',
                   'Intended Audience :: End Users/Desktop',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Software Development :: Libraries'
                   ]
      )
