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
by Baum and his colleagues [Ref1]_, [Ref2]_, [Ref3]_, [Ref4]_, [Ref5]_ in the
late 1960s and early 1970s and was implemented for speech processing
applications by Baker [Ref6]_ at CMU, and by Jelinek and his colleagues at IBM
[Ref7]_, [Ref8]_, [Ref9]_, [Ref10]_, [Ref11]_, [Ref12]_, [Ref13]_ in the 1970s.
However, widespread understanding and application of the theory of HMMs to
speech processing has occurred only within the past several years. There are
several reasons why this has been the case. First, the basic theory of hidden
Markov models was published in mathematical journals which were not generally
read by engineers working on problems in speech processing. The second reason
was that the original applications of the theory to speech processing did not
provide sufficient tutorial material for most readers to understand the theory
and to be able to apply it to their own research. As a result, several tutorial
papers were written which provided a sufficient level of detail for a number of
research labs to begin work using HMMs in individual speech processing
applications [Ref14]_, [Ref15]_, [Ref16]_, [Ref17]_, [Ref18]_, [Ref19]_. This
tutorial is intended to provide an overview of the basic theory of HMMs (as
originated by Baum and his colleagues), provide practical details on methods of
implementation of the theory, and describe a couple of selected applications of
the theory to distinct problems in speech recognition. The paper combines
results from a number of original sources and hopefully provides a single source
for acquiring the background required to pursue further this fascinating area of
research.

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
.. [#hmm2] A good overview of discrete Markov processes is in [Ref20]_ ch. 5.

.. rubric:: References

.. [Ref1] L. E. Baum and T. Petrie, "Statistical inference for probabilistic functions of finite state Markov chains", Ann. Math. Stat., vol. 37, pp. 1554-1563, 1966.

.. [Ref2] L. E. Baum and J. A. Egon, "An inequality with applications to statistical estimation for probabilistic functions of a Markov process and to a model for ecology", Bull. Amer. Meteorol. Soc., vol. 73, pp. 360-363, 1967.

.. [Ref3] L. E. Baum and G. R. Sell, "Growth functions for transformations on manifolds", Pac. J. Math., vol. 27, no. 2, pp. 211-227, 1968.

.. [Ref4] L. E. Baum, T. Petrie, G. Soules and N. Weiss, "A maximization technique occurring in the statistical analysis of probabilistic functions of Markov chains", Ann. Math. Stat., vol. 41, no. 1, pp. 164-171, 1970.

.. [Ref5] L. E. Baum, "An inequality and associated maximization technique in statistical estimation for probabilistic functions of Markov processes", Inequalities, vol. 3, pp. 1-8, 1972.

.. [Ref6] J. K. Baker, "The dragon system—An overview", IEEE Trans. Acoust. Speech Signal Processing, vol. ASSP-23, no. 1, pp. 24-29, Feb. 1975.

.. [Ref7] F. Jelinek, "A fast sequential decoding algorithm using a stack", IBM J. Res. Develop., vol. 13, pp. 675-685, 1969.

.. [Ref8] L. R. Bahl and F. Jelinek, "Decoding for channels with insertions deletions and substitutions with applications to speech recognition", IEEE Trans. In format. Theory, vol. IT-21, pp. 404-411, 1975.

.. [Ref9] F. Jelinek, L. R. Bahl and R. L. Mercer, "Design of a linguistic statistical decoder for the recognition of continuous speech", IEEE Trans. Informat. Theory, vol. IT-21, pp. 250-256, 1975.

.. [Ref10] F. Jelinek, "Continuous speech recognition by statistical methods", Proc. IEEE, vol. 64, pp. 532-536, Apr. 1976.

.. [Ref11] R. Bakis, "Continuous speech word recognition via centisecond acoustic states", Proc. ASA Meeting, 1976-Apr.

.. [Ref12] F. Jelinek, L. R. Bahl and R. L. Mercer, "Continuous speech recognition: Statistical methods" in Handbook of Statistics II, The Netherlands, Amsterdam:North-Holland, 1982.

.. [Ref13] L. R. Bahl, F. Jelinek and R. L. Mercer, "A maximum likelihood approach to continuous speech recognition", IEEE Trans. Pattern Anal. Machine Intell., vol. PAMI-5, pp. 179-190, 1983.

.. [Ref14] S. E. Levinson, L. R. Rabiner and M. M. Sondhi, "An introduction to the application of the theory of probabilistic functions of a Markov process to automatic speech recognition", Bell Syst. Tech. J., vol. 62, no. 4, pp. 1035-1074, Apr. 1983.

.. [Ref15] B. H. Juang, "On the hidden Markov model and dynamic time warping for speech recognition—A unified view", AT&T Tech., vol. 63, no. 7, pp. 1213-1243, Sept. 1984.

.. [Ref16] L. R. Rabiner and B. H. Juang, "An introduction to hidden Markov models", IEEE ASSP Mag., vol. 3, no. 1, pp. 4-16, 1986.

.. [Ref17] J. S. Bridle, "Stochastic models and template matching: Some important relationships between two apparently different techniques for automatic speech recognition", Proc. Inst. of Acoustics Autum Conf., pp. 1-8, 1984-Nov.

.. [Ref18] J. Makhoul, S. Roucos and H. Gish, "Vector quantization in speech coding", Proc. IEEE, vol. 73, no. 11, pp. 1551-1588, Nov. 1985.

.. [Ref19] S. E. Levinson, "Structural methods in automatic speech recognition", Proc. IEEE, vol. 73, no. 11, pp. 1625-1650, Nov. 1985.

.. [Ref20] A. W. Drake, "Discrete—state Markov processes" in Fundamentals of Applied Probability Theory, NY, New York:McGraw-Hill, 1967.

.. [Ref21] A. J. Viterbi, "Error bounds for convolutional codes and an asymptotically optimal decoding algorithm", IEEE Trans. Informat. Theory, vol. IT-13, pp. 260-269, Apr. 1967.

.. [Ref22] G. D. Forney, "The Viterbi algorithm", Proc. IEEE, vol. 61, pp. 268-278, Mar. 1973.

.. [Ref23] A. P. Dempster, N. M. Laird and D. B. Rubin, "Maximum likelihood from incomplete data via the EM algorithm", J. Roy. Stat. Soc., vol. 39, no. 1, pp. 1-38, 1977.

.. [Ref24] L. A. Liporace, "Maximum likelihood estimation for multivariate observations of Markov sources", IEEE Trans. Informat. Theory, vol. IT-28, no. 5, pp. 729-734, 1982.

.. [Ref25] B. H. Juang, "Maximum likelihood estimation for mixture multivariate stochastic observations of Markov chains", AT&T Tech. J., vol. 64, no. 6, pp. 1235-1249, July-Aug. 1985.

.. [Ref26] B. H. Juang, S. E. Levinson and M. M. Sondhi, "Maximum likelihood estimation for multivariate mixture observations of Markov chains", IEEE Trans. Informat. Theory, vol. IT-32, no. 2, pp. 307-309, Mar. 1986.

.. [Ref27] A. B. Poritz, "Linear predictive hidden Markov models and the speech signal", Proc. ICASSP '82, pp. 1291-1294, 1982-May.

.. [Ref28] B. H. Juang and L. R. Rabiner, "Mixture autoregressive hidden Markov models for speech signals", IEEE Trans. Acoust. Speech Signal Processing, vol. ASSP-33, no. 6, pp. 1404-1413, Dec. 1985.

.. [Ref29] M. J. Russell and R. K. Moore, "Explicit modeling of state occupancy in hidden Markov models for automatic speech recognition", Proc. ICASSP'85, pp. 5-8, 1985-Mar.

.. [Ref30] S. E. Levinson, "Continuously variable duration hidden Markov models for automatic speech recognition", Computer Speech and Language, vol. 1, no. 1, pp. 29-45, Mar. 1986.

.. [Ref31] B. Lowerre and R. Reddy, "The HARPY speech understanding system" in Trends in Speech Recognition, NJ, Englewood Cliffs:Prentice-Hall, pp. 340-346, 1980.

.. [Ref32] L. R. Bahl, P. F. Brown, P. V. de Souza and R. L. Mercer, "Maximum mutual information estimation of hidden Markov model parameters for speech recognition", Proc. ICASSP '86, pp. 49-52, 1986-Apr.

.. [Ref33] Y. Ephraim, A. Dembo and L. R. Rabiner, "A minimum discrimination information approach for hidden Markov modeling", Proc. ICASSP '87, 1987-Apr.

.. [Ref34] B. H. Juang and L. R. Rabiner, "A probabilistic distance measure for hidden Markov models", AT&T Tech. J., vol. 64, no. 2, pp. 391-408, Feb. 1985.

.. [Ref35] L. R. Rabiner, B. H. Juang, S. E. Levinson and M. M. Sondhi, "Some properties of continuous hidden Markov model representations", AT&T Tech. J., vol. 64, no. 6, pp. 1251-1270, July-Aug. 1985.

.. [Ref36] F. Jelinek and R. L. Mercer, "Interpolated estimation of Markov source parameters from sparse data" in Pattern Recognition in Practice, The Netherlands, Amsterdam:North-Holland, pp. 381-397, 1980.

.. [Ref37] R. Schwartz, "Context-dependent modeling for acoustic-phonetic recognition of continuous speech", Conf. Proc. IEEE Int. Conf. on Acoustics Speech and Signal Processing, pp. 1205-1208, 1985-Apr.

.. [Ref38] K. F. Lee and H. W. Hon, "Large-vocabulary speaker-independent continuous speech recognition", Conf. Proc. IEEE Int. Conf. on Acoustics Speech and Signal Processing, pp. 123-126, 1988-Apr.

.. [Ref39] L. R. Rabiner, S. E. Levinson and M. M. Sondhi, "On the application of vector quantization and hidden Markov models to speaker-independent isolated word recognition", Bell Syst. Tech. J., vol. 62, no. 4, pp. 1075-1105, Apr. 1983.

.. [Ref40] L. R. Rabiner, S. E. Levinson and M. M. Sondhi, "On the use of hidden Markov models for speaker-independent recognition of isolated words from a medium-size vocabulary", AT&T Tech. J., vol. 63, no. 4, pp. 627-642, Apr. 1984.

.. [Ref41] R. Billi, "Vector quantization and Markov source models applied to speech recognition", Proc. ICASSP '82, pp. 574-577, 1982-May.

.. [Ref42] L. R. Rabiner, B. H. Juang, S. E. Levinson and M. M. Sondhi, "Recognition of isolated digits using hidden Markov models with continuous mixture densities", AT&T Tech. J., vol. 64, no. 6, pp. 1211-1222, July-Aug. 1986.

.. [Ref43] A. B. Poritz and A. G. Richter, "Isolated word recognition", Proc. ICASSP '86, pp. 705-708, 1986-Apr.

.. [Ref44] R. P. Lippmann, E. A. Martin and D. B. Paul, "Multistyle training for robust isolated word speech recognition", Proc. ICASSP '87, pp. 705-708, 1987-Apr.

.. [Ref45] D. B. Paul, "A speaker stress resistant HMM isolated word recognizer", Proc. ICASSP'87, pp. 713-716, 1987-Apr.

.. [Ref46] V. N. Gupta, M. Lennig and P. Mermelstein, "Integration of acoustic information in a large vocabulary word recognizer", Conf. Proc. IEEE Int. Conf. on Acoustics Speech and Signal Processing, pp. 697-700, 1987-Apr.

.. [Ref47] S. E. Levinson, "Continuous speech recognition by means of acoustic-phonetic classification obtained from a hidden Markov model", Proc. ICASSP '87, 1987-Apr.

.. [Ref48] J. C. Wilpon, L. R. Rabiner and T. Martin, "An improved word detection algorithm for telephone quality speech incorporating both syntactic and semantic constraints", AT&T Bell Labs Tech. J., vol. 63, no. 3, pp. 479-498, Mar. 1984.

.. [Ref49] J. G. Wilpon and L. R. Rabiner, "Application of hidden Markov models to automatic speech endpoint detection", Computer Speech and Language, vol. 2, no. 3/4, pp. 321-341, Sept./Dec. 1987.

.. [Ref50] A. Averbuch, "Experiments with the TANGORA 20000 word speech recognizer", Conf. Proc. IEEE Int. Conf. on Acoustics Speech and Signal Processing, pp. 701-704, 1987-Apr.

.. [Ref51] B. S. Atal and S. L. Hanauer, "Speech analysis and synthesis by linear prediction of the speech wave", J. Acoust. Soc. Am., vol. 50, pp. 637-655, 1971.

.. [Ref52] F. I. Itakura and S. Saito, "Analysis-synthesis telephony based upon the maximum likelihood method", Proc. 6th Int. Congress on Acoustics, pp. C17-20, 1968.

.. [Ref53] J. Makhoul, "Linear prediction: A tutorial review", Proc. IEEE, vol. 63, pp. 561-580, 1975.

.. [Ref54] J. D. Markel and A. H. Gray, Linear Prediction of Speech, NY, New York:Springer-Verlag, 1976.

.. [Ref55] Y. Tokhura, "A weighted cepstral distance measure for speech recognition", IEEE Trans. Acoust. Speech Signal Processing, vol. ASSP-35, no. 10, pp. 1414-1422, Oct. 1987.

.. [Ref56] B. H. Juang, L. R. Rabiner and J. G. Wilpon, "On the use of bandpass liftering in speech recognition", IEEE Trans. Acoust. Speech Signal Processing, vol. ASSP-35, no. 7, pp. 947-954, July 1987.

.. [Ref57] S. Furui, "Speaker independent isolated word recognition based on dynamics emphasized cepstrum", Trans. IECE of Japan, vol. 69, no. 12, pp. 1310-1317, Dec. 1986.

.. [Ref58] F. K. Soong and A. E. Rosenberg, "On the use of instantaneous and transitional spectral information in speaker recognition", Proc. ICASSP '86, pp. 877-880, 1986-Apr.

.. [Ref59] L. R. Rabiner, J. G. Wilpon and B. H. Juang, "A segmental k-means training procedure for connected word recognition", AT&T Tech. J., vol. 65, no. 3, pp. 21-31, May-June 1986.

.. [Ref60] L. R. Rabiner and S. E. Levinson, "A speaker-independent syntax-directed connected word recognition system based on hidden Markov models and level building", IEEE Trans. Acoust. Speech Signal Processing, vol. ASSP-33, no. 3, pp. 561-573, June 1985.

.. [Ref61] L. R. Rabiner, J. G. Wilpon and B. H. Juang, "A modei-based connected digit recognition system using either hidden Markov models or templates", Computer Speech and Language, vol. 1, no. 2, pp. 167-197, Dec. 1986.

.. [Ref62] H. Bourlard, Y. Kamp, H. Ney and C. J. Wellekens, "Speaker-dependent connected speech recognition via dynamic programming and statistical methods" in Speech and Speaker Recognition, Switzerland, Basel:Karger, pp. 115-148, 1985.

.. [Ref63] C. J. Wellekens, "Global connected digit recognition using Baum-Welch algorithm", Proc. ICASSP '86, pp. 1081-1084, 1986-Apr.

.. [Ref64] A. M. Derouault, "Context dependent phonetic Markov models for large vocabulary speech recognition", Proc. ICASSP '87, 1987-Apr.

.. [Ref65] B. Merialdo, "Speech recognition with very large size dictionary", Proc. ICASSP '87, 1987-Apr.

.. [Ref66] Y. L. Chow, "BYBLOS: The BBN continuous speech recognition system", Proc. ICASSP'87, 1987-Apr.
