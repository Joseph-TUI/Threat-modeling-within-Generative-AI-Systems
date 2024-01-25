<p align="center">
	<a href="https://github.com/Joseph-TUI/Threat-modeling-within-Generative-AI-Systems/blob/main/README.md">
		<img align="center" alt="Threat modeling-Security Practices" src="/Pic/main.JPG" height="175">
	</a>
</p>

# Overview

Using a variety of test AI-generated chatbot applications, the three main assaults that were discovered are.	


| Attacks	| Description	|
|---	|---	|
| [Adversarial Attacks](https://ieeexplore.ieee.org/document/9256597)	| Attackers can craft input data in a way that subtly perturbs the input while remaining imperceptible to humans but causes the model to generate incorrect or harmful results.	|
| [Model Tampering](https://ieeexplore.ieee.org/document/10169568)	| This could involve modifying model parameters, weights, or architecture to induce biases, generate inappropriate content, or compromise the integrity of the generated outputs. |
| [Output Manipulation](https://ieeexplore.ieee.org/document/10352982)	| Attackers may seek to manipulate the generated content post-production, either to inject malicious content or to deceive users relying on the authenticity of the generated output.|


## Risk Assessment in AI Systems 

Assessing security risks in AI-based applications entails the evaluation of potential vulnerabilities and threats across development, deployment, and operational phases. Presented below are practical instances of security risks in AI applications, accompanied by considerations for risk assessment:


| Attacks	| Example	| Risk Calculation |
|---	|---	|---	|
| [Adversarial Attacks]	| For an AI In image recognition systems , adversaries may manipulate input images to mislead the AI model into making incorrect predictions.|Evaluate the robustness of the AI model against adversarial attacks. Consider the impact on decision-making accuracy and the likelihood of adversaries attempting such attacks .|
| [Model Tampering]	| An e-commerce recommendation system may be vulnerable to model poisoning, where malicious users provide false feedback to manipulate future recommendations.|Evaluate the susceptibility of the model to poisoning attacks and the potential impact on user experience and business integrity. Consider the likelihood of malicious actors attempting such attacks .|
| [Output Manipulation]	| If an AI system controlling critical infrastructure is not properly secured, it could be susceptible to hacking, leading to physical harm or disruption.|Assess the security measures in place, such as access controls, encryption, and intrusion detection systems. Calculate risk based on the potential consequences of unauthorized access or manipulation.|

The risks mentioned above are categorised according to the types of vulnerabilities displayed in the image below. Impact of the STRIDE model on three widely recognized chatbots, examining potential attacks.

<p align="center">
	<a href="https://github.com/Joseph-TUI/Threat-modeling-within-Generative-AI-Systems/blob/main/README.md">
		<img align="center" alt="Threat modeling-Security Practices" src="/Pic/Figure-1.JPG" height="510">
	</a>
</p>

## How to Calculate ?

Quantifying risk factors with exact numerical values proves challenging due to the subjective nature of judgments and the potential variability influenced by specific contexts and organizational factors. Nevertheless, a simplified illustration can be offered through the utilization of a qualitative risk matrix, wherein likelihood and impact are categorized into low, medium, and high ratings. 

Let's consider the example of data privacy in a healthcare AI application:

**Data Privacy and Protection:**

**Likelihood:**

* Low: Data is well-encrypted, and access controls are robust.
* Medium: Some vulnerabilities in data encryption and access controls.
* High: Weak encryption and lax access controls.

**Impact:**

* Low: Limited patient data exposure.
* Medium: Exposure of some sensitive patient information.
* High: Wide-scale exposure of sensitive patient information.

**Risk Calculation:**

* Low Likelihood + Low Impact = Low Risk
* Medium Likelihood + Medium Impact = Medium Risk
* High Likelihood + High Impact = High Risk

This risk assessment can be visualized using a risk matrix:

<p align="center">
	<a href="https://github.com/Joseph-TUI/Threat-modeling-within-Generative-AI-Systems/tree/main/tecdoc">
		<img align="center" alt="Threat modeling-Security Practices" src="/Pic/Risk.JPG" height="100">
	</a>
</p>

The matrix values can undergo additional refinement by considering the organization's risk tolerance and the particulars of the implemented security controls.

It is crucial to emphasize that the presented example is a simplification. In a practical setting, a thorough risk assessment would necessitate an in-depth examination of each risk factor, encompassing potential controls, mitigations, and the organization's overall risk appetite. Some organizations might opt for quantitative risk assessment methods, facilitating a more detailed and numeric analysis of likelihood and impact for a comprehensive understanding of risks.

Lets use the Formula R=P×Q×I, represents the Risk (R) as the product of Probability (P), Impact (I), and a factor representing the control effectiveness or Quality (Q). Let's use this formula in the context of data privacy in a healthcare AI application, considering a simplified scale of 1 to 3 for each factor.

In this scenario, we'll explore how an adversary might manipulate the output of a facial recognition AI model to achieve unauthorized access. The risk calculation will involve assessing the likelihood and impact of such an attack.

**Attack Scenario: Output Manipulation in Facial Recognition System**

**Likelihood (P):**

* Low: The system has robust anti-spoofing mechanisms, and the likelihood of successful manipulation is minimal.
* Medium: Some anti-spoofing measures are in place, but there are known vulnerabilities.
* High: Weak anti-spoofing measures, and it's relatively easy for an adversary to manipulate the system's output.

**Impact (I):**

* Low: Successful manipulation results in temporary access to a non-sensitive area.
* Medium: Unauthorized access to a moderately sensitive area.
* High: Full unauthorized access to highly sensitive information or areas.

**Quality/Control Effectiveness (Q):**

* Low: Limited or no real-time monitoring and response mechanisms in place.
* Medium: Some monitoring, but response mechanisms are not well-tailored to detect and counteract output manipulation.
* High: Advanced real-time monitoring and response mechanisms are in place to quickly detect and mitigate manipulation attempts.

<p align="center">
	<a href="https://github.com/Joseph-TUI/Threat-modeling-within-Generative-AI-Systems/tree/main/tecdoc">
		<img align="center" alt="Threat modeling-Security Practices" src="/Pic/Risk1.JPG" height="220">
	</a>
</p>

In this instance:

* The initial scenario portrays a situation of minimal risk, characterized by a low likelihood of successful manipulation and robust control effectiveness within the system.
* The subsequent scenario suggests a moderate level of risk, featuring moderate likelihood and impact, along with an average level of control effectiveness.
* The third scenario denotes a situation of elevated risk, arising from a confluence of high likelihood, substantial impact, and limited control effectiveness.

Organizations can employ the findings of this risk assessment to prioritize security measures, allocate resources effectively, and implement countermeasures for mitigating the identified risks. Continuous reassessment of these risks is imperative, especially given the evolving threat landscape and the dynamic nature of both the AI system and its surrounding environment.