---
title: "A Proximal Alternating Linearized Minimization Method for Tensor Graphical Models"
collection: publications
permalink: /publication/sg-palm_aistats2021
date: 2020-11-01
venue: 'The 24th International Conference on Artificial Intelligence and Statistics (AISTATS) (<b><i>Under reveiw</i></b>)'
authors: '<b><i>Yu Wang</i></b>, Alfred Hero'
excerpt_separator: ""
---
We consider the estimation of graphical models that characterize conditional dependency structure of high-dimensional tensor-variate data. In particular, we develop a significantly improved Sylvester graphical model~\citep{wang20sylvester}. Such models admit a generative stochastic representation for the tensor-variate random variable. A critical challenge of this model is the fact that its richer representation of conditional dependency leads to a highly coupled likelihood function. In this paper, we propose a proximal alternating linearized minimization method called SG-PALM for performing regularized precision matrix estimation for tensor-valued data in the Sylvester graphical modeling framework. A theoretical convergence analysis establishes linear convergence (i.e., geometric convergence rate) to a global optimum of the objective function. To demonstrate the scalability and accuracy of SG-PALM, we apply it to a novel application of forecasting solar flares from imaging data, and show that the estimated precision matrices can be utilized to construct simple and effective time series predictors for the solar atmosphere.
