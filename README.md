# Cracking a Companion Arbiter PUF
The problem revolves around breaking a cryptographic primitive known as the Companion Arbiter PUF (CAR-PUF) using machine learning techniques. Here's a detailed explanation of the concepts and the task:

## 1. Physical Unclonable Function (PUF)
A Physical Unclonable Function (PUF) is a hardware security primitive designed to create unique and unpredictable responses to given challenges. They are based on the inherent physical variations in semiconductor manufacturing, making them unclonable and resistant to duplication. These properties make PUFs useful for applications like device authentication, cryptographic key generation, and secure identification.

## 2. Arbiter PUFs
An Arbiter PUF is a type of PUF that uses multiple PUFs to generate its responses.
It consists of a chain of k PUFs. Each PUF can either swap the upper and lower signal paths or keep them intact based on a bit in the input challenge. Each signal path has a unique delay, and the delays accumulate as the signal propagates through the PUFs.
Based on the delays of the upper ($t_u$) and lower ($t_l$) paths, the response is 0 if ( $\Delta = t_u - t_l) < 0 $, else 1.

## 3. Companion Arbiter PUFs
The **Companion Arbiter PUF (CAR-PUF)** extends the basic Arbiter PUF concept to enhance security by introducing a second reference PUF and a secret threshold $\tau$.
A CAR-PUF consists of two arbiter PUFs, A working PUF and a reference PUF. Given a binary challenge both the PUF are simulated and delays of each path are measured. Let $\Delta_w$ and $\Delta_r$ represent the delays in the working and the reference PUF. Then the response is:
0 if $|\Delta_w - \Delta_r| <= \tau$ else 1.

The task is to show that a CAR-PUF can be broken using a single linear machine learning model. Despite the added complexity introduced by the reference PUF and threshold $\tau$, it is possible to construct a feature map $\phi$ and a linear model W, b such that it perfectly predicts the CAR-PUF's responses.

The model is available in model.py and the derivation for the linear model can be seen in report.pdf.
