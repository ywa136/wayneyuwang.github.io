---
title: "The Sylvester Graphical Lasso (SyGlasso)"
collection: publications
permalink: /publication/syglasso_aistats2020
date: 2020-06-01
venue: 'The 23rd International Conference on Artificial Intelligence and Statistics (AISTATS)'
authors: '<b><i>Yu Wang</i></b>, Byoungwook Jang, Alfred Hero'
paperurl: 'http://proceedings.mlr.press/v108/wang20d'
excerpt_separator: ""
---
(SyGlasso) that captures multiway dependencies present in tensor-valued data. The model is based on the Sylvester equation that defines a generative model. The proposed model complements the tensor graphical lasso \citep{greenewald2017tensor} that imposes a Kronecker sum model for the inverse covariance matrix by providing an alternative Kronecker sum model that is generative and interpretable. A nodewise regression approach is adopted for estimating the conditional independence relationships among variables. The statistical convergence of the method is established, and empirical studies are provided to demonstrate the recovery of meaningful conditional dependency graphs. We apply the SyGlasso to an electroencephalography (EEG) study to compare the brain connectivity of alcoholic and nonalcoholic subjects. We demonstrate that our model can simultaneously estimate both the brain connectivity and its temporal dependencies.
