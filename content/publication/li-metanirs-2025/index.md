---
abstract: Functional near-infrared spectroscopy (fNIRS) is a crucial brain activity
  monitoring tool with remarkable potential applications in brain-computer interfaces
  (BCI), particularly in rehabilitation therapy for disabilities. However, the performance
  of fNIRS-based BCI systems remains suboptimal, such as motor execution (ME) and
  motor imagery (MI) decoding. Inspired by the successful application of the PoolFormer
  framework in visual tasks, we first proposed a novel long-range dilation multilayer
  perceptron (LongDilMLP) to utilize the hemodynamic characteristics of fNIRS. Furthermore,
  the LongDilMLP was integrated with the PoolFormer framework, called as MetaNIRS
  in this study. The proposed framework MetaNIRS was employed for both ME and MI classification
  tasks, achieving rigorous validation of its effectiveness and practical applicability.
  To evaluate the performance of MetaNIRS, two publicly available ME datasets (A and
  C) and one self-collected MI dataset (B) were employed. The experimental results
  demonstrated that the average accuracy were 76.00 %, 57.45 %, and 84.14 %, with
  cross-subject accuracy of 77.24 %, 58.55 %, and 85.52 %, respectively. Moreover,
  sensitivity experiments of model parameters showed the robustness. Ablation experiments
  highlighted the significance of each MetaNIRS component and the efficacy of LongDilMLP
  over traditional MLP. Additionally, visualization techniques enhanced the interpretability
  of MetaNIRS, indicating the main contribution of the first half signals for classification.
  Using the first half of signals, the average accuracy only reduced 4.30 %, 1.69
  %, and 1.11 %, respectively. These findings suggest that the superior performance
  of MetaNIRS, which provide an efficient general decoding framework for ME and MI.
authors:
- Yu Li
- Yu Sun
- Feng Wan
- Zhen Yuan
- Tzyy-Ping Jung
- Hongtao Wang
categories: []
date: '2025-08-04'
doi: 10.1016/j.neunet.2025.107873
featured: false
projects:
- brain-fnirs-motor-cortex
publication: '*Neural Networks*'
publication_types:
- '2'
publishDate: 2025-08-04 08:00:20.986010+00:00
tags: []
title: 'MetaNIRS: A general decoding framework for fNIRS based motor execution/imagery'

---
