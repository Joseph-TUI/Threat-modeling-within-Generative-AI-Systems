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


Assessing security risks in AI-based applications entails the evaluation of potential vulnerabilities and threats across development, deployment, and operational phases. Presented below are practical instances of security risks in AI applications, accompanied by considerations for risk assessment:


| Attacks	| Example	| Risk Calculation |
|---	|---	||---	|
| [Adversarial Attacks]	| In image recognition systems, adversaries may manipulate input images to mislead the AI model into making incorrect predictions.|Evaluate the robustness of the AI model against adversarial attacks. Consider the impact on decision-making accuracy and the likelihood of adversaries attempting such attacks .|
| [Model Tampering]	| An e-commerce recommendation system may be vulnerable to model poisoning, where malicious users provide false feedback to manipulate future recommendations.|Evaluate the susceptibility of the model to poisoning attacks and the potential impact on user experience and business integrity. Consider the likelihood of malicious actors attempting such attacks .|
| [Output Manipulation]	| If an AI system controlling critical infrastructure is not properly secured, it could be susceptible to hacking, leading to physical harm or disruption.|Assess the security measures in place, such as access controls, encryption, and intrusion detection systems. Calculate risk based on the potential consequences of unauthorized access or manipulation .|


Impact of the STRIDE model on three widely recognized chatbots, examining potential attacks.

<p align="center">
	<a href="https://github.com/Joseph-TUI/Threat-modeling-within-Generative-AI-Systems/blob/main/README.md">
		<img align="center" alt="Threat modeling-Security Practices" src="/Pic/Figure-1.JPG" height="500">
	</a>
</p>
