---
abstract: 'Sleep, notably active sleep (AS) and quiet sleep (QS), plays a pivotal
  role in the brain development and gradual maturation of (pre) term infants. Monitoring
  their sleep patterns is imperative, as it can serve as a tool in promoting neurological
  maturation and well-being, particularly important in preterm infants who are at
  an increased risk of immature brain development. An accurate classification of neonatal
  sleep states can contribute to optimizing treatments for high-risk infants, with
  respiratory rate (RR) and heart rate (HR) serving as key components in sleep assessment
  systems for neonates. Recent studies have demonstrated the feasibility of extracting
  both RR and HR using near-infrared spectroscopy (NIRS) in neonates. This study introduces
  a comprehensive sleep classification approach leveraging high-frequency NIRS signals
  recorded at a sampling rate of 100 Hz from a cohort of nine preterm infants admitted
  to a neonatal intensive care unit. Eight distinct features were extracted from the
  raw NIRS signals, including HR, RR, motion-related parameters, and proxies for neural
  activity. These features served as inputs for a deep convolutional neural network
  (CNN) model designed for the classification of AS and QS sleep states. The performance
  of the proposed CNN model was evaluated using two cross-validation approaches: ten-fold
  cross-validation of data pooling and five-fold cross-validation, where each fold
  contains two independently recorded NIRS data. The accuracy, balanced accuracy,
  F1-score, Kappa, and AUC-ROC (Area Under the Curve of the Receiver Operating Characteristic)
  were employed to assess the classifier performance. In addition, comparative analyses
  against six benchmark classifiers, comprising K-Nearest Neighbors, Naive Bayes,
  Support Vector Machines, Random Forest (RF), AdaBoost, and XGBoost (XGB), were conducted.
  Our results reveal the CNN model’s superior performance, achieving an average accuracy
  of 88%, a balanced accuracy of 94%, an F1-score of 91%, Kappa of 95%, and an AUC-ROC
  of 96% in data pooling cross-validation. Furthermore, in both cross-validation methods,
  RF and XGB demonstrated accuracy levels closely comparable to the CNN classifier.
  These findings underscore the feasibility of leveraging high-frequency NIRS data,
  coupled with NIRS-based HR and RR extraction, for assessing sleep states in neonates,
  even in an intensive care setting. The user-friendliness, portability, and reduced
  sensor complexity of the approach suggest its potential applications in various
  less-demanding settings. This research thus presents a promising avenue for advancing
  neonatal sleep assessment and its implications for infant health and development.'
authors:
- Naser Hakimi
- Emad Arasteh
- Maren Zahn
- Jörn M. Horschig
- Willy N. J. M. Colier
- Jeroen Dudink
- Thomas Alderliesten
categories: []
date: '2024-12-04'
doi: 10.3390/s24217004
featured: false
projects:
- brain-fnirs-prefrontal-cortex
- neonatal
publication: '*Sensors*'
publication_types:
- '2'
publishDate: 2024-12-04 08:34:22.211557+00:00
tags: []
title: Near-Infrared Spectroscopy for Neonatal Sleep Classification

---
