---
abstract: Assessing pain in non-verbal patients is challenging, often depending on
  clinical judgment which can be unreliable due to fluctuations in vital signs caused
  by underlying medical conditions. To date, there is a notable absence of objective
  diagnostic tests to aid healthcare practitioners in pain assessment, especially
  affecting critically-ill or advanced dementia patients. Neurophysiological information,
  i.e., functional near-infrared spectroscopy (fNIRS) or electroencephalogram (EEG),
  unveils the brain’s active regions and patterns, revealing the neural mechanisms
  behind the experience and processing of pain. This study focuses on assessing pain
  via the analysis of fNIRS signals combined with machine learning, utilising multiple
  fNIRS measures including oxygenated haemoglobin (ΔHBO2) and deoxygenated haemoglobin
  (ΔHHB). Initially, a channel selection process filters out highly contaminated channels
  with high-frequency and high-amplitude artifacts from the 24-channel fNIRS data.
  The remaining channels are then preprocessed by applying a low-pass filter and common
  average referencing to remove cardio-respiratory artifacts and common gain noise,
  respectively. Subsequently, the preprocessed channels are averaged to create a single
  time series vector for both ΔHBO2 and ΔHHB measures. From each measure, ten statistical
  features are extracted and fusion occurs at the feature level, resulting in a fused
  feature vector. The most relevant features, selected using the Minimum Redundancy
  Maximum Relevance method, are passed to a Support Vector Machines classifier. Using
  leave-one-subject-out cross validation, the system achieved an accuracy of 68.51%±9.02%
  in a multi-class task (No Pain, Low Pain, and High Pain) using a fusion of ΔHBO2
  and ΔHHB. These two measures collectively demonstrated superior performance compared
  to when they were used independently. This study contributes to the pursuit of an
  objective pain assessment and proposes a potential biomarker for human pain using
  fNIRS.
authors:
- Muhammad Umar Khan
- Maryam Sousani
- Niraj Hirachan
- Calvin Joseph
- Maryam Ghahramani
- Girija Chetty
- Roland Goecke
- Raul Fernandez-Rojas
categories:
- Brite
date: '2024-02-12'
doi: 10.3390/s24020458
featured: false
projects:
- brain-fnirs-prefrontal-cortex
- clinical-and-rehabilitation
publication: '*Sensors*'
publication_types:
- '2'
publishDate: 2024-02-12 08:19:37.072958+00:00
tags: []
title: 'Multilevel Pain Assessment with Functional Near-Infrared Spectroscopy: Evaluating
  ΔHBO2 and ΔHHB Measures for Comprehensive Analysis'
url_pdf: https://www.mdpi.com/1424-8220/24/2/458

---
