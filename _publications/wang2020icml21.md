---
title: "SG-PALM: a Fast Physically Interpretable Tensor Graphical Model"
collection: publications
permalink: /publication/wang2020icml21
date: 2021-06-15T00:00:0000:00:00 + 0500
venue: 'Proceedings of the Thirty Eighth International Conference on Machine Learning (<b><i>under review</i></b>)'
pubtype: 'submitted'
authors: '<b><i>Y. Wang</i></b>, A. Hero'
excerpt_separator: ""
---
We propose a new graphical model inference procedure, called SG-PALM, for learning conditional dependency structure of high-dimensional tensor-variate data. Unlike most other tensor graphical models the proposed model is interpretable and computationally scalable to high dimension. Physical interpretability follows from the Sylvester generative (SG) model on which SG-PALM is based: the model is exact for any observation process that is a solution of a partial differential equation of Poisson type. Scalability follows from the fast proximal alternating linearized minimization (PALM) procedure that SG-PALM uses during training. We establish that SG-PALM converges linearly (i.e., geometric convergence rate) to a global optimum of its objective function. We demonstrate scalability and accuracy of SG-PALM for an important but challenging climate prediction problem: spatio-temporal forecasting of solar flares from multimodal imaging data.
