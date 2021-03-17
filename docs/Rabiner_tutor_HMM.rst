Notes on: Rabiner, L. R. (1990): A tutorial on hidden markov models and selected applications in speech recognition
===================================================================================================================

.. code-block:: bibtex

   @article{Rabiner_tutor_HMM,
     author    = {Rabiner, Lawrence R.},
     title     = {A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition},
     journal   = {Readings in Speech Recognition},
     pages     = {267–296},
     year      = {1990},
     doi       = {10.1016/b978-0-08-051584-7.50027-9},
     url       = {http://dx.doi.org/10.1016/b978-0-08-051584-7.50027-9},
     isbn      = {http://id.crossref.org/isbn/9781558601246},
     publisher = {Elsevier BV},
   }

Although initially introduced and studied in the late 1960s and early 1970s,
statistical methods of Markov source or hidden Markov modeling have become
increasingly popular in the last several years. There are two strong reasons why
this has occurred. First the models are very rich in mathematical structure and
hence can form the theoretical basis for use in a wide range of applications.
Second the models, when applied properly, work very well in practice for several
important applications. In this paper we attempt to carefully and methodically
review the theoretical aspects of this type of statistical modeling and show how
they have been applied to selected problems in machine recognition of speech.

INTRODUCTION
------------

Real-world processes generally produce observable outputs which can be
characterized as signals. The signals can be discrete in nature (e.g.,
characters from a finite alphabet, quantized vectors from a codebook, etc.), or
continuous in nature (e.g., speech samples, temperature measurements, music,
etc.). The signal source can be stationary (i.e., its statistical properties do
not vary with time), or nonstationary (i.e., the signal properties vary over
time). The signals can be pure (i.e., coming strictly from a single source), or
can be corrupted from other signal sources (e.g., noise) or by transmission
distortions, reverberation, etc.

A problem of fundamental interest is characterizing such real-world signals in
terms of signal models. There are several reasons why one is interested in
applying signal models. First of all, a signal model can provide the basis for a
theoretical description of a signal processing system which can be used to
process the signal so as to provide a desired output. For example if we are
interested in enhancing a speech signal corrupted by noise and transmission
distortion, we can use the signal model to design a system which will optimally
remove the noise and undo the transmission distortion. A second reason why
signal models are important is that they are potentially capable of letting us
learn a great deal about the signal source (i.e., the real-world process which
produced the signal) without having to have the source available. This property
is especially important when the cost of getting signals from the actual source
is high. In this case, with a good signal model, we can simulate the source and
learn as much as possible via simulations. Finally, the most important reason
why signal models are important is that they often work extremely well in
practice, and enable us to realize important practical systems-e.g., prediction
systems, recognition systems, identification systems, etc., in a very efficient
manner.

These are several possible choices for what type of signal model is used for
characterizing the properties of a given signal. Broadly one can dichotomize the
types of signal models into the class of deterministic models, and the class of
statistical models. Deterministic models generally exploit some known specific
properties of the signal, e.g., that the signal is a sine wave, or a sum of
exponentials, etc. In these cases, specification of the signal model is
generally straightforward; all that is required is to determine (estimate)
values of the parameters of the signal model (e.g., amplitude, frequency, phase
of a sine wave, amplitudes and rates of exponentials, etc.). The second broad
class of signal models is the set of statistical models in which one tries to
characterize only the statistical properties of the signal. Examples of such
statistical models include Gaussian processes, Poisson processes, Markov
processes, and hidden Markov processes, among others. The underlying assumption
of the statistical model is that the signal can be well characterized as a
parametric random process, and that the parameters of the stochastic process can
be determined (estimated) in a precise, well-defined manner.

For the applications of interest, namely speech processing, both deterministic
and stochastic signal models have had good success. In this paper we will
concern ourselves strictly with one type of stochastic signal model, namely the
hidden Markov model (HMM). (These models are referred to as Markov sources or
probabilistic functions of Markov chains in the communications literature.) We
will first review the theory of Markov chains and then extend the ideas to the
class of hidden Markov models using several simple examples. We will then focus
our attention on the three fundamental problems [#hmm1]_ for HMM design, namely:
the evaluation of the probability (or likelihood) of a sequence of observations
given a specific HMM; the determination of a best sequence of model states; and
the adjustment of model parameters so as to best account for the observed
signal. We will show that once these three fundamental problems are solved, we
can apply HMMs to selected problems in speech recognition.

Neither the theory of hidden Markov models nor its applications to speech
recognition is new. The basic theory was published in a series of classic papers
by Baum and his colleagues [1]-[5] in the late 1960s and early 1970s and was
implemented for speech processing applications by Baker [6] at CMU, and by
Jelinek and his colleagues at IBM [7]-[13] in the 1970s. However, widespread
understanding and application of the theory of HMMs to speech processing has
occurred only within the past several years. There are several reasons why this
has been the case. First, the basic theory of hidden Markov models was published
in mathematical journals which were not generally read by engineers working on
problems in speech processing. The second reason was that the original
applications of the theory to speech processing did not provide sufficient
tutorial material for most readers to understand the theory and to be able to
apply it to their own research. As a result, several tutorial papers were
written which provided a sufficient level of detail for a number of research
labs to begin work using HMMs in individual speech processing applications
[14]-[19]. This tutorial is intended to provide an overview of the basic theory
of HMMs (as originated by Baum and his colleagues), provide practical details on
methods of implementation of the theory, and describe a couple of selected
applications of the theory to distinct problems in speech recognition. The paper
combines results from a number of original sources and hopefully provides a
single source for acquiring the background required to pursue further this
fascinating area of research.

The organization of this paper is as follows. In Section II we review the theory
of discrete Markov chains and show how the concept of hidden states, where the
observation is a probabilistic function of the state, can be used effectively.
We illustrate the theory with two simple examples, namely coin-tossing, and the
classic balls-in-urns system. In Section III we discuss the three fundamental
problems of HMMs, and give several practical techniques for solving these
problems. In Section IV we discuss the various types of HMMs that have been
studied including ergodic as well as left-right models. In this section we also
discuss the various model features including the form of the observation density
function, the state duration density, and the optimization criterion for
choosing optimal HMM parameter values. In Section V we discuss the issues that
arise in implementing HMMs including the topics of scaling, initial parameter
estimates, model size, model form, missing data, and multiple observation
sequences. In Section VI we describe an isolated word speech recognizer,
implemented with HMM ideas, and show how it performs as compared to alternative
implementations. In Section VII we extend the ideas presented in Section VI to
the problem of recognizing a string of spoken words based on concatenating
individual HMMs of each word in the vocabulary. In Section VIII we briefly
outline how the ideas of HMM have been applied to a large vocabulary speech
recognizer, and in Section IX we summarize the ideas discussed throughout the
paper.

DISCRETE MARKOV PROCESSES [#hmm2]_
----------------------------------

.. _hmmfig1:

.. figure:: images/hmmfig1.png
   :align: center

   A Markov chain with 5 states (labeled :math:`S_1` to :math:`S_5`) with selected state transitions.

Consider a system which may be described at any time as being in one of a set of
:math:`N` distinct states, :math:`S_1, S_2, \ldots, S_N`, as illustrated in Fig.
1 (where :math:`N = 5` for simplicity). At regularly spaced discrete times, the
system undergoes a change of state (possibly back to the same state) according
to a set of probabilities associated with the state. We denote the time instants
associated with state changes as :math:`t = 1, 2, \ldots` , and we denote the
actual state at time :math:`t` as :math:`q_t`. A full probabilistic description
of the above system would, in general, require specification of the current
state (at time :math:`t`), as well as all the predecessor states. For the
special case of a discrete, first order, Markov chain, this probabilistic
description is truncated to just the current and the predecessor state, i.e.,

.. math::
   P[q_t = S_j \mid q_{t-1} = S_i, q_{t-2} = S_k, \ldots] = P[q_t = S_j \mid q_{t-1} = S_i].
   :label: hmmeq1

Further more we only consider those processes in which the right-hand side of
:eq:`hmmeq1` is independent of time, thereby leading to the set of state
transition probabilities :math:`a_{ij}` of the form

.. math::
   a_{ij} = P[q_t = S_j \mid q_{t-1} = S_i], \quad 1 \leq i, j \leq N
   :label: hmmeq2

with the state transition coefficients having the properties

.. math::
   a_{ij} & \geq 0 \\
   \sum_{j = 1}^{N} a_{ij} & = 1
   :label: hmmeq3

since they obey standard stochastic constraints.

The above stochastic process could be called an observable Markov model since
the output of the process is the set of states at each instant of time, where
each state corresponds to a physical (observable) event. To set ideas, consider
a simple 3-state Markov model of the weather. We assume that once a day (e.g.,
at noon), the weather is observed as being one of the following:

   State 1: rain or (snow)

   State 2: cloudy

   State 3: sunny

We postulate that the weather on day :math:`t` is characterized by a single one
of the three states above, and that the matrix :math:`A` of state transition
probabilities is

.. math::
   A = \{a_{ij}\} =
   \begin{bmatrix}
   0.4 & 0.3 & 0.3 \\
   0.2 & 0.6 & 0.2 \\
   0.1 & 0.1 & 0.8
   \end{bmatrix}
   .

Given that the weather on day 1 (:math:`t = 1`) is sunny (state 3), we can ask
the question: What is the probability (according to the model) that the weather
for the next 7 days will be "sun-sun-rain-rain-sun-cloudy-sun"? Stated more
formally, we define the observation sequence :math:`O` as
:math:`O = \{S_3, S_3, S_3, S_1, S_1, S_3, S_2, S_3\}`
corresponding to :math:`t = 1, 2, \ldots, 8,` and we
wish to determine the probability of :math:`O` , given the model. This
probability can be expressed (and evaluated) as

.. math::
   P(O \mid \text{Model}) & = P[S_3, S_3, S_3, S_1, S_1, S_3, S_2, S_3 \mid \text{Model}] \\
   & = P[S_3] \cdot P[S_3 \mid S_3] \cdot P[S_3 \mid S_3] \cdot P[S_1 \mid S_3] \\
   & \quad \cdot P[S_1 \mid S_1] \cdot P[S_3 \mid S_1] \mid P[S_2 \mid S_3] \mid P[S_3 \mid S_2] \\
   & = \pi_3 \cdot a_{33} a_{33} a_{31} a_{11} a_{13} a_{32} a_{23} \\
   & = 1 \times 0.8 \times 0.8 \times 0.1 \times 0.4 \times 0.3 \times 0.1 \times 0.2 \\
   & = 1.536 \times 10^{-4}

where we use the notation

.. math::
   \pi_i = P[q_1 = S_i], \quad 1 \leq i \leq N
   :label: hmmeq4

to denote the initial state probabilities.

Another interesting question we can ask (and answer using the model) is: Given
that the model is in a known state, what is the probability it stays in that
state for exactly :math:`d` days? This probability can be evaluated as the
probability of the observation sequence

.. math::
   O = \{S_i, S_i, S_i, \ldots, S_i, S_j \neq S_i\},

given the model, which is

.. math::
   P(O \mid \text{Model}, q_1 = S_i) = (a_{ii})^{d-1} (1 - a_{ii}) = p_i(d).
   :label: hmmeq5

The quantity :math:`p_i(d)` is the (discrete) probability density function of
duration :math:`d` in state :math:`i` . This exponential duration density is
characteristic of the state duration in a Markov chain. Based on :math:`p_i(d)`
, we can readily calculate the expected number of observations (duration) in a
state, conditioned on starting in that state as

.. math::
   \bar{d}_i & = \sum_{d=1}^{\infty} d p_i(d) \\
   & = \sum_{d=1}^{\infty} d (a_{ii})^{d-1} (1 - a_{ii}) = \dfrac{1}{1 - a_{ii}}.

Thus the expected number of consecutive days of sunny weather, according to the
model, is :math:`1/0.2 = 5` ; for cloudy it is :math:`2.5` ; for rain it is
:math:`1.67` .

Extension to Hidden Markov Models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Footnotes

.. [#hmm1] The idea of characterizing the theoretical aspects of hidden Markov
           modeling in terms of solving three fundamental problems is due to
           Jack Ferguson of IDA (Institute for Defense Analysis) who introduced
           it in lectures and writing.
.. [#hmm2] A good overview of discrete Markov processes is in [20, ch. 5].
