---
abstract: To handle nonstationary dynamics and intersubject variability in fNIRS depression
  classification, we fuse temporal, spectral, spatial, and cross-channel features
  and design a multiscale DTW with temporal and channel attention. Individual and
  cohort templates are used jointly to capture fine-grained descriptors and subject-specific
  deviations. Feature subsets are selected using TopCombo, and classification employs
  a stacking ensemble with SVM, Random Forest, and XGBoost as base learners, along
  with a logistic regression meta-learner. Evaluation follows a strict subject-wise
  protocol to avoid leakage. All transformations and hyperparameters are fit within
  training folds, and inference is performed only on held-out subjects. On a cohort
  of 56 MDD patients and 53 healthy controls, the proposed framework achieves an accuracy
  of 0.90 and a macro F1-score of 0.898 under strict subject-wise cross-validation.
  Compared with representative baselines, macro F1 improves by about 4.3–7.5 percentage
  points, and the variance across folds is clearly reduced. These results indicate
  that coupling multi-view features with personalized multiscale alignment is critical
  for robust cross-subject generalization in fNIRS-based depression recognition.
authors:
- Siyao Yan
- Rui Yang
- Lu Zhang
- Jisheng Dang
- Hong Peng
- Bin Hu
categories:
- brite
date: '2026-03-11'
doi: 10.1016/j.bspc.2026.109924
featured: false
projects:
- brain-fnirs-prefrontal-cortex
- clinical-and-rehabilitation
publication: '*Biomedical Signal Processing and Control*'
publication_types:
- '2'
publishDate: 2026-03-11 15:40:02.673110+00:00
tags: []
title: Coupling multi-view features and personalized alignment for depression recognition
  with fNIRS
url_pdf: https://www.sciencedirect.com/science/article/pii/S1746809426004787

---
