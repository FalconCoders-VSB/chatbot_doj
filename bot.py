import nltk
import time
import datetime

def get_time_period():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Morning"
    elif 12 <= current_hour < 17:
        return "Afternoon"
    elif 17 <= current_hour < 21:
        return "Evening"
    else:
        return "Night"
time_period = get_time_period()
print("Good", time_period + " Spark Have a great day!")
 

from nltk.chat.util import Chat, reflections

pairs=[  
        
          ['ipc|what is ipc|explain ipc|introduction to ipc', 
 ['IPC stands for the Indian Penal Code, which is the official criminal code of India.The IPC was implemented in 1860 and covers all substantive aspects of criminal lawIt is applicable throughout India except in Jammu & Kashmir..Example: \nSection 302 of IPC deals with punishment for murder, which can be a death penalty or life imprisonment.']],

['crpc|what is crpc|explain crpc|introduction to crpc', 
 ['CrPC stands for the Code of Criminal Procedure, which governs the procedure for the administration of criminal law in India.The CrPC was implemented in 1973 and provides the machinery for the investigation of crime, apprehension of suspected criminals, collection of evidence, determination of guilt or innocence of the accused, and the determination of punishment.It is the primary legislation concerning the conduct of criminal trials.Example: \nSection 41 of CrPC deals with the powers of the police to arrest without a warrant.']],

['contract act|what is indian contract act|explain contract act|introduction to indian contract act', 
 ['The Indian Contract Act, 1872, is the key law governing contracts in India.It specifies the conditions under which promises made by the parties to a contract are legally binding.The Act was implemented on 1st September 1872 and extends to the whole of India.Example: \nSection 10 of the Indian Contract Act specifies what agreements are contracts.']],

['consumer protection act|what is consumer protection act|explain consumer protection act|introduction to consumer protection act', 
 ['The Consumer Protection Act, 2019, was enacted to protect the interests of consumers in India.It provides for the establishment of consumer councils and other authorities for the settlement of consumer disputes.The Act was implemented on 20th July 2020 and aims to safeguard consumer rights.Example: \nSection 2(7) of the Consumer Protection Act defines a consumer as any person who buys any goods or hires any service for a consideration.']],

### Intermediate Law Questions

['section 144|what is section 144 in ipc|explain section 144|introduction to section 144 crpc', 
 ['Section 144 of the CrPC empowers a magistrate to issue an order in urgent cases of nuisance or apprehended danger.This section is often invoked to prevent unlawful assembly of people and to maintain public tranquility.The order issued under Section 144 can remain in force for up to two months.Example: \nSection 144 can be invoked to impose curfews or restrictions on public gatherings in a specific area.']],

['section 498a|what is section 498a in ipc|explain section 498a|introduction to section 498a ipc', 
 ['Section 498A of the IPC deals with the cruelty by a husband or his relatives towards a married woman.This section was implemented to protect married women from dowry harassment and other forms of cruelty.The section was added to the IPC in 1983, recognizing the need for stringent laws to protect women from domestic violence.Example: \nUnder Section 498A, a husband or relative can be punished with imprisonment of up to three years and a fine for subjecting a woman to cruelty.']],

['article 21|what is article 21|explain article 21|introduction to article 21', 
 ['Article 21 of the Indian Constitution guarantees the right to life and personal liberty to all individuals.It states that no person shall be deprived of their life or personal liberty except according to the procedure established by law.Article 21 is considered one of the most important fundamental rights and has been expansively interpreted by the courts to include various rights such as the right to privacy, the right to a fair trial, and the right to a clean environment.Example: \nThe right to privacy, recognized in the Puttaswamy case in 2017, is derived from Article 21.']],

['section 375|what is section 375 in ipc|explain section 375|introduction to section 375 ipc', 
 ['Section 375 of the IPC defines the offense of rape and lays down the circumstances under which sexual intercourse is considered to be rape.The section also lists exceptions, such as consensual intercourse within marriage, provided the wife is not under 15 years of age.This section was implemented as part of the IPC in 1860 and has been amended several times to broaden the definition and address issues like marital rape.Example: \nSection 375 was amended in 2013 following the Nirbhaya case to expand the definition of rape and increase the severity of punishment.']],
 
 # Department of Justice (DoJ) - Acts

['indian evidence act|what is indian evidence act|explain indian evidence act', 
 ['The Indian Evidence Act, 1872 defines the rules and standards by which evidence is admissible in courts.', 
  'It is essential for the functioning of the judicial system in India.', 
  'The act outlines what constitutes relevant and admissible evidence.',
  'Example: \npython\nSection 3: Definition of "Evidence"\n']],

['constitution of india|what is constitution of india|explain constitution of india', 
 ['The Constitution of India, 1950 is the supreme law of India.', 
  'It lays down the framework defining fundamental political principles.', 
  'The Constitution establishes the structure, procedures, and powers of government institutions.',
  'Example: \npython\nArticle 21: Right to Life and Personal Liberty\n']],
          ['legal services authorities act|what is legal services authorities act|explain legal services authorities act', 
 ['The Legal Services Authorities Act, 1987 provides free legal services to the weaker sections of society.', 
  'It organizes Lok Adalats for the settlement of disputes.', 
  'The act aims to promote justice on the basis of equal opportunity.',
  'Example: \npython\nSection 12: Criteria for giving legal services\n']],

['family courts act|what is family courts act|explain family courts act', 
 ['The Family Courts Act, 1984 establishes Family Courts to promote conciliation and secure the speedy settlement of disputes relating to marriage and family affairs.', 
  'The act seeks to provide a specialized forum for family matters.', 
  'Family Courts deal with issues such as divorce, custody, and alimony.',
  'Example: \npython\nSection 7: Jurisdiction\n']],

['arbitration and conciliation act|what is arbitration and conciliation act|explain arbitration and conciliation act', 
 ['The Arbitration and Conciliation Act, 1996 governs arbitration proceedings in India.It promotes arbitration and conciliation as alternative dispute resolution mechanisms.The act ensures that arbitration agreements and awards are enforceable in India.Example: \npython\nSection 7: Arbitration Agreement\n']],

['protection of women from domestic violence act|what is protection of women from domestic violence act|explain protection of women from domestic violence act', 
 ['The Protection of Women from Domestic Violence Act, 2005 provides protection to women from domestic violence.It defines domestic violence and prescribes remedies for victims.The act also provides for the appointment of Protection Officers to assist victimsExample: \npython\nSection 3: Definition of domestic violence\n']],

['sc/st act|scheduled castes and the scheduled tribes act|prevention of atrocities act|what is sc/st act|explain sc/st act', 
 ['The Scheduled Castes and the Scheduled Tribes (Prevention of Atrocities) Act, 1989 aims to prevent atrocities against members of SC/ST communities.It provides for special courts for the trial of such offenses.The act also prescribes stringent punishments for offenders.Example: Section 3: Punishments for offenses of atrocities`']],

['right to information act|rti|what is rti|explain right to information act', 
 ['The Right to Information (RTI) Act, 2005 provides citizens the right to request information from public authorities.The act promotes transparency and accountability in the functioning of the government.RTI is an important tool for ensuring good governance in India.Example: \npython\nSection 6: Request for obtaining information\n']],

### Advanced Law Questions

['section 377|what is section 377 in ipc|explain section 377|introduction to section 377 ipc', 
 ['Section 377 of the IPC criminalized sexual activities "against the order of nature," including homosexual acts.This section was a colonial-era law that was implemented in 1861 and was often used to harass and criminalize the LGBTQ+ community in India.In 2018, the Supreme Court of India decriminalized consensual homosexual acts between adults, partially striking down Section 377 as unconstitutional.Example: \nThe landmark judgment in the Navtej Singh Johar case decriminalized consensual same-sex relations by reading down Section 377.']],

['section 304b|what is section 304b in ipc|explain section 304b|introduction to section 304b ipc', 
 ['Section 304B of the IPC deals with dowry deaths, where the death of a woman is caused by burns, bodily injury, or otherwise within seven years of marriage, and it is shown that she was subjected to cruelty or harassment by her husband or his relatives in connection with any demand for dowry.This section was introduced in 1986 to address the increasing number of dowry-related deaths in India.The punishment under Section 304B is imprisonment for a term which shall not be less than seven years but which may extend to life imprisonment.Example: \nSection 304B is often invoked in cases where a bride dies under suspicious circumstances within a short period after marriage.']],

['section 354|what is section 354 in ipc|explain section 354|introduction to section 354 ipc', 
 ['Section 354 of the IPC deals with assault or criminal force to a woman with the intent to outrage her modesty.This section was implemented to protect women from physical assault or harassment that is intended to outrage their modesty.Section 354 has been amended multiple times to include stringent punishments and expand its scope to cover various forms of sexual harassment.Example: \nSection 354 includes offenses like molestation, stalking, and voyeurism, with punishments ranging from imprisonment to fines.']],

['section 124a|what is section 124a in ipc|explain section 124a|introduction to section 124a ipc', 
 ['Section 124A of the IPC deals with sedition, which involves any act or speech that brings or attempts to bring into hatred or contempt, or excites or attempts to excite disaffection towards the government established by law.This section was introduced during British rule in 1870 to suppress dissent and has been a subject of much debate in independent India.The punishment for sedition under Section 124A can be life imprisonment, with or without a fine, or imprisonment up to three years, with or without a fine.Example: \nSection 124A has been criticized for being used to stifle free speech and has been challenged in various courts for its validity.']],
          # Basic Queries

['what is department of justice|explain doj|introduction to doj|DOJ|doj', 
 ['The Department of Justice (DoJ) is part of the Ministry of Law & Justice, Government of India.It is headed by the Secretary and is responsible for implementing key legal and judicial initiatives.The DoJ oversees important schemes like the development of infrastructure facilities for the judiciary, the setting up of Fast Track Special Courts, and the eCourts Project for court computerization.']],

['what are the divisions of doj|explain divisions of doj|doj divisions', 
 ['The DoJ is divided into several key sections, each handling specific legal and judicial functions.These divisions include the administration of justice, judicial infrastructure, legal aid, and eCourts initiatives.You can learn more about each division on the official DoJ website.']],

['how many judges are appointed in india|number of judges in supreme court|high court judges', 
 ['The DoJ is responsible for appointing judges to the Supreme Court, High Courts, and District & Subordinate Courts.Currently, there are [specific number] judges in the Supreme Court, [specific number] in High Courts, and [specific number] in District & Subordinate Courts.The number of vacancies is updated regularly on the official DoJ website.']],
 
 
 # High Court Judges
['high court judges|number of high court judges in india|how many judges in high court',
 ['There are 25 High Courts in India.The total sanctioned strength of High Court judges is around 1,100.This number may vary due to vacancies or recent appointments.']],

# Supreme Court Judges
['supreme court judges|number of supreme court judges|how many judges in supreme court',
 ['The Supreme Court of India has a sanctioned strength of 34 judges.This includes the Chief Justice of India.The actual number may vary due to appointments or retirements.']],

# District Court Judges
['district court judges|number of district court judges|how many judges in district court',
 ['The total number of District Court judges across India is typically around 17,000.The exact number may vary across different states and regions.District Courts handle the majority of cases filed across the country.']],

# Intermediate Queries

['what is the status of case pendency|explain njdg|case pendency in india|NJDG|njdg', 
 ['The National Judicial Data Grid (NJDG) provides real-time data on the pendency of cases across India.It is an initiative under the eCourts Project, aiming to make judicial data accessible to the public.You can check the status of case pendency on the NJDG portal.']],

['how to pay traffic fines|procedure to pay fines in india|pay fine for traffic violation|traffic fine', 
 ['The DoJ provides a streamlined process for paying traffic fines online.You can pay your fines through the ePay system, available on the eCourts portal.Follow the steps provided on the eCourts website to complete your payment.']],

['can i watch live court cases|is live streaming of court cases available|live court streaming in india|live stream of court', 
 ['Live streaming of court cases is available for select proceedings, especially those of public interest.This initiative is part of the DoJ’s efforts to increase transparency and public access to judicial proceedings.You can access live streams on the official court websites or through designated portals.']],

# Advanced Queries

['how to file a case online|steps for efiling|explain epay system|epay system|epay', 
 ['The DoJ’s eFiling system allows you to file cases online without visiting the court.The ePay system complements this by enabling online payments for court fees and fines.Detailed instructions for eFiling and ePay are available on the eCourts portal.']],

['what are fast track courts|explain fast track courts in india|working of fast track courts|fast track courts', 
 ['Fast Track Courts are special courts established to expedite cases of sensitive nature, such as those under the POCSO Act.These courts aim to reduce the pendency of cases by speeding up the trial process.The DoJ oversees the functioning and expansion of Fast Track Courts across India.']],

['how to download ecourts app|what is ecourts services mobile app|ecourts app download', 
 ['The eCourts Services Mobile App provides easy access to case status, court orders, and other judicial information.You can download the app from the Google Play Store or Apple App Store.The app is designed to help citizens track their cases and access judicial services on the go.']],

['how to use tele law services|what are tele law services|tele law ', 
 ['Tele Law Services provide legal advice to citizens through video conferencing.This initiative, under the DoJ, aims to make legal services more accessible, especially in rural areas.You can avail of Tele Law Services by visiting your nearest Common Service Center (CSC) or through the official website.']],
  # Section Set 1: General Explanations of the Indian Penal Code (IPC)

['section-1|what is section 1 in ipc|explain section 1 ipc|title and extent of operation of the code', 
 ['Section 1 of the IPC provides the title and extent of operation of the Code.It declares the name of the Code as the Indian Penal Code, 1860, and specifies its territorial extent, covering the whole of India except the State of Jammu and Kashmir.This section establishes the geographical reach of the IPC within India.']],

['section-2|what is section 2 in ipc|explain section 2 ipc|punishment of offences committed within india', 
 ['Section 2 of the IPC deals with the punishment of offences committed within India.It states that every person shall be liable to punishment under the IPC for every act or omission contrary to its provisions if the act is committed within India.This section enforces the IPC within Indian territory.']],

['section-3|what is section 3 in ipc|explain section 3 ipc|punishment of offences beyond india', 
 ['Section 3 of the IPC addresses the punishment of offences committed beyond India but which by law may be tried within India.It allows for the prosecution of Indian citizens and others for offences committed outside India if such offences are punishable under Indian law.This section extends the jurisdiction of the IPC to certain extra-territorial offences.']],

['section-4|what is section 4 in ipc|explain section 4 ipc|extension of code to extra-territorial offences', 
 ['Section 4 of the IPC provides for the extension of the Code to extra-territorial offences.It applies the IPC to offences committed by any citizen of India in any place without and beyond India.This section ensures that Indian law applies to Indian citizens even when they are abroad.']],

['section-5|what is section 5 in ipc|explain section 5 ipc|certain laws not affected by this act', 
 ['Section 5 of the IPC clarifies that certain laws are not to be affected by the IPC.It states that the provisions of the IPC shall not affect any special or local law, or any special jurisdiction or power conferred by any other law.This section ensures the IPC does not override specific laws or jurisdictions.']],

['section-6|what is section 6 in ipc|explain section 6 ipc|definitions in the code subject to exceptions', 
 ['Section 6 of the IPC indicates that definitions in the Code should be understood subject to exceptions.It means that definitions provided in the IPC must be interpreted considering any exceptions or limitations specified in the Code or elsewhere.This section ensures accurate interpretation of terms defined within the IPC.']],

['section-7|what is section 7 in ipc|explain section 7 ipc|sense of expression once explained', 
 ['Section 7 of the IPC deals with the sense of expressions once explained.It states that every expression that has been defined in the IPC shall be understood in the sense explained unless there is something repugnant in the subject or context.This section ensures consistency in the interpretation of terms used in the IPC.']],

['section-8|what is section 8 in ipc|explain section 8 ipc|gender', 
 ['Section 8 of the IPC explains the use of gender terms in the Code.It states that the pronoun "he" and its derivatives are used for any person, whether male or female.This section makes clear that gender-specific terms are to be interpreted inclusively.']],

['section-9|what is section 9 in ipc|explain section 9 ipc|number', 
 ['Section 9 of the IPC clarifies the use of number in the Code.',
  'It states that unless there is something repugnant in the subject or context, words importing the singular number include the plural, and words importing the plural number include the singular.This section ensures flexible interpretation of numerical terms in the IPC.']],

['section-10|what is section 10 in ipc|explain section 10 ipc|man and woman', 
 ['Section 10 of the IPC defines the terms "man" and "woman".It states that the word "man" denotes a male human being of any age, and "woman" denotes a female human being of any age.This section provides clarity on gender-specific terms used in the IPC.']],

['section-11|what is section 11 in ipc|explain section 11 ipc|person', 
 ['Section-11 of the IPC defines the term "person".',
  'It states that the word "person" includes any Company or Association or body of persons, whether incorporated or not.',
  'This section broadens the scope of legal accountability to include groups and organizations.']],

['section 12|what is section 12 in ipc|explain section 12 ipc|public', 
 ['Section-12 of the IPC defines the term "public".It states that the word "public" includes any class of the public or any community.This section is used to clarify who can be considered a part of the public in legal terms.']],

['section-13|what is section 13 in ipc|explain section 13 ipc|queen', 
 ['Section 13 of the IPC defines the term "Queen".It states that the word "Queen" refers to the sovereign of the United Kingdom of Great Britain and Ireland.This section was relevant during British rule and may be interpreted in the historical context today.']],

['section-14|what is section 14 in ipc|explain section 14 ipc|servant of government', 
 ['Section 14 of the IPC defines the term "servant of Government".It states that the term "servant of Government" denotes any officer or servant continued, appointed, or employed in India by or under the authority of the Government.This section clarifies who is legally considered a government servant under the IPC.']],
          ['section-15|what is section 15 in ipc|explain section 15 ipc|british india', 
 ['Section 15 of the IPC defines the term "British India"It refers to territories under the control of the British Crown during the colonial period.This section is now of historical interest and was relevant during British rule.']],

['section-16|what is section 16 in ipc|explain section 16 ipc|government of india', 
 ['Section 16 of the IPC defines the term "Government of India".It refers to the central authority governing India during British rule and now applies to the sovereign government post-independence.This section provides a legal definition of the government in the context of the IPC.']],

['section-17|what is section 17 in ipc|explain section 17 ipc|government', 
 ['Section 17 of the IPC defines the term "Government".It includes both the central and state governments within the Republic of India.This section clarifies the scope of governmental authority in legal matters.']],

['section-18|what is section 18 in ipc|explain section 18 ipc|india', 
 ['Section 18 of the IPC defines the term "India".It includes the territory of India excluding the State of Jammu and Kashmir.This section establishes the geographical scope of India as per the IPC.']],

['section-19|what is section 19 in ipc|explain section 19 ipc|judge', 
 ['Section 19 of the IPC defines the term "Judge".It states that the word "Judge" denotes not only every person who is officially designated as a Judge, but also every person who is empowered by law to give, in any legal proceeding, a definitive judgment.This section clarifies who can legally be considered a Judge under the IPC.']],

['section-20|what is section 20 in ipc|explain section 20 ipc|court of justice', 
 ['Section 20 of the IPC defines the term "Court of Justice".It includes all Judges who are legally authorized to administer justice and act as a Court in the exercise of their powers.This section establishes the legal framework for what constitutes a Court of Justice under the IPC.']],
 
 # Section Set 2: General Explanations of the Indian Penal Code (IPC)

['section-21|what is section 21 in ipc|explain section 21 ipc|public servant', 
 ['Section 21 of the IPC defines the term "Public Servant".It includes officers and individuals holding positions of authority in the government or performing public duties.This section broadens the scope of who is legally recognized as a public servant.']],

['section-22|what is section 22 in ipc|explain section 22 ipc|moveable property', 
 ['Section 22 of the IPC defines the term "Moveable Property".It refers to all forms of tangible personal property that can be moved from one place to another.This section distinguishes moveable property from immovable property like land.']],

['section-23|what is section 23 in ipc|explain section 23 ipc|wrongful gain', 
 ['Section 23 of the IPC defines "Wrongful Gain".It refers to the gaining of property through unlawful means or by depriving another of their lawful property.This section addresses illegal acquisition of property under the IPC.']],

['section-24|what is section 24 in ipc|explain section 24 ipc|dishonestly', 
 ['Section 24 of the IPC defines the term "Dishonestly".',
  'It refers to an act done with the intention of causing wrongful gain to one person or wrongful loss to another.',
  'This section is crucial in determining the intent behind unlawful acts.']],

['section-25|what is section 25 in ipc|explain section 25 ipc|fraudulently', 
 ['Section 25 of the IPC defines the term "Fraudulently".It refers to an act done with intent to deceive or to cause loss to another person.This section helps in identifying acts of fraud under the IPC.']],

['section-26|what is section 26 in ipc|explain section 26 ipc|reason to believe', 
 ['Section 26 of the IPC defines the term "Reason to Believe".It means a person has sufficient cause to assume the truth of a fact based on reasonable grounds.This section is used to establish a person’s awareness or belief about certain facts.']],

['section-27|what is section 27 in ipc|explain section 27 ipc|property in possession of wife, clerk or servant', 
 ['Section 27 of the IPC addresses the concept of "Property in Possession of Wife, Clerk or Servant".It states that property in the possession of a person’s wife, clerk, or servant is considered to be in that person’s possession if it has been delivered to them by or on behalf of the person.This section clarifies legal possession in such contexts.']],

['section-28|what is section 28 in ipc|explain section 28 ipc|counterfeit', 
 ['Section 28 of the IPC defines the term "Counterfeit".It refers to making a copy or imitation of something with the intent to deceive or defraud.This section is crucial in legal matters related to forgery and imitation.']],

['section-29|what is section 29 in ipc|explain section 29 ipc|document', 
 ['Section 29 of the IPC defines the term "Document".It includes any matter expressed or described upon any substance by means of letters, figures, or marks intended to be used as evidence of that matter.This section is essential for understanding what constitutes a legal document.']],

['section-29A|what is section 29A in ipc|explain section 29a ipc|electronic record', 
 ['Section 29A of the IPC defines the term "Electronic Record".It includes data, record, or data generated, image or sound stored, received, or sent in an electronic form.This section covers electronic documents under the purview of the IPC.']],

['section-30|what is section 30 in ipc|explain section 30 ipc|valuable security', 
 ['Section 30 of the IPC defines the term "Valuable Security".It refers to any document that is a property in itself, or which provides evidence of a right, duty, or obligation.This section is vital for understanding legal rights associated with documents.']],

['section-31|what is section 31 in ipc|explain section 31 ipc|a will', 
 ['Section 31 of the IPC defines the term "Will".It refers to the legal declaration of a person’s intention regarding the distribution of their property after death.This section clarifies the legal standing of wills.']],

['section-32|what is section 32 in ipc|explain section 32 ipc|words referring to acts include illegal omissions', 
 ['Section 32 of the IPC states that words referring to acts include illegal omissions.It means that any reference to an act in the IPC also includes a reference to an illegal omission of that act.This section is key in cases where negligence or failure to act is in question.']],

['section-33|what is section 33 in ipc|explain section 33 ipc|act omission', 
 ['Section 33 of the IPC defines "Act" and "Omission".It states that the word "Act" denotes as well a series of acts as a single act, and the word "Omission" denotes as well a series of omissions as a single omission.This section is fundamental in understanding the scope of actions and inactions under the IPC.']],

['section-34|what is section 34 in ipc|explain section 34 ipc|acts done by several persons in furtherance of common intention', 
 ['Section 34 of the IPC addresses acts done by several persons in furtherance of common intention.It states that when a criminal act is done by several persons in furtherance of the common intention of all, each of such persons is liable for that act.This section is important in cases involving group offenses or conspiracies.']],

['section-35|what is section 35 in ipc|explain section 35 ipc|when such an act is criminal by reason of its being done with a criminal knowledge or intention', 
 ['Section 35 of the IPC deals with when an act is criminal by reason of its being done with criminal knowledge or intention.It clarifies that if a criminal act requires knowledge or intent, all parties involved must have that knowledge or intent for it to be a criminal offense.This section focuses on the importance of intent in criminal acts.']],

['section-36|what is section 36 in ipc|explain section 36 ipc|effect caused partly by act and partly by omission', 
 ['Section 36 of the IPC covers effects caused partly by act and partly by omission.It states that wherever the causing of a certain effect, or an attempt to cause that effect, by an act or by an omission is an offense, it is to be understood that the causing of that effect partly by an act and partly by an omission is also an offense.This section ensures that both actions and inactions contributing to an offense are recognized.']],

['section-37|what is section 37 in ipc|explain section 37 ipc|co-operation by doing one of several acts constituting an offence', 
 ['Section-37 of the IPC discusses co-operation by doing one of several acts constituting an offence.It states that when an offense requires several acts to be done by different persons, each person who contributes to the offense is liable for the offense.This section addresses the shared responsibility in the commission of an offense.']],

['section-38|what is section 38 in ipc|explain section 38 ipc|persons concerned in criminal act may be guilty of different offences', 
 ['Section 38 of the IPC states that persons concerned in a criminal act may be guilty of different offenses.It means that when multiple persons are involved in a criminal act, each may be liable for a different offense depending on their role.This section allows for differentiated legal responsibility among co-accused.']],

['section-39|what is section 39 in ipc|explain section 39 ipc|voluntarily', 
 ['Section 39 of the IPC defines the term "Voluntarily".It refers to an action that is done with free will and intention, without any external pressure or coercion.This section clarifies the importance of intent in legal responsibility.']],

['section-40b|what is section 40 in ipc|explain section 40 ipc|offence', 
 ['Section 40 of the IPC defines the term "Offence".It refers to any act or omission that is punishable by the IPC or any other law in force at the time being.This section provides a broad definition of what constitutes an offense under the IPC.']],
  # Section Set 3: General Explanations and Punishments of the Indian Penal Code (IPC)

['section-41b|what is section 41 in ipc|explain section 41 ipc|special law', 
 ['Section 41 of the IPC defines the term "Special Law".It refers to any law that is not included in the general laws and is specifically enacted for certain cases or situations.This section distinguishes special laws from other types of legal provisions.']],

['section-42b|what is section 42 in ipc|explain section 42 ipc|local law', 
 ['Section 42 of the IPC defines the term "Local Law".It refers to a law that applies to a particular locality or region rather than the whole country.This section explains how local laws are considered in the legal framework.']],

['section-43|what is section 43 in ipc|explain section 43 ipc|illegal legally bound to do', 
 ['Section 43 of the IPC defines the terms "Illegal" and "Legally Bound to Do".Illegal refers to anything forbidden by law, while legally bound to do means required by law to perform or refrain from performing an act.This section clarifies the scope of legality and obligations under the law.']],
          ['section-44b|what is section 44 in ipc|explain section 44 ipc|injury', 
 ['Section 44 of the IPC defines the term "Injury".It refers to any harm or damage illegally caused to a person’s body, mind, reputation, or property.This section is fundamental in understanding what constitutes an injury under the law.']],

['section-45b|what is section 45 in ipc|explain section 45 ipc|life', 
 ['Section 45 of the IPC defines the term "Life"..It refers to the duration of a person’s existence or survival from birth until death.This section clarifies the legal implications related to life.']],

['section-46b|what is section 46 in ipc|explain section 46 ipc|death', 
 ['Section 46 of the IPC defines the term "Death".It refers to the cessation of life or the end of all biological functions that sustain a living organism.This section is important in legal contexts involving fatal outcomes.']],

['section-47b|what is section 47 in ipc|explain section 47 ipc|animal', 
 ['Section 47 of the IPC defines the term "Animal".It refers to any living creature other than a human being.This section covers the legal considerations related to animals under the IPC.']],

['section-48b|what is section 48 in ipc|explain section 48 ipc|vessel', 
 ['Section 48 of the IPC defines the term "Vessel".It refers to any watercraft, large or small, that is used for transportation on water.This section is significant in legal matters related to maritime activities.']],

['section-49b|what is section 49 in ipc|explain section 49 ipc|year month', 
 ['Section 49 of the IPC defines the terms "Year" and "Month".Year refers to a period of twelve months, and month refers to a calendar month.',
  'This section clarifies time periods in legal terms.']],

['section-50s|what is section 50 in ipc|explain section 50 ipc|section', 
 ['Section 50 of the IPC defines the term "Section".It refers to a distinct and numbered subdivision of a legal statute or document.This section is important for understanding the structure of legal codes.']],

['section-51s|what is section 51 in ipc|explain section 51 ipc|oath', 
 ['Section 51 of the IPC defines the term "Oath".It refers to a solemn promise or declaration, often invoking a divine witness, regarding the truth of a statement or the performance of a duty.This section is crucial in legal proceedings involving sworn statements.']],

['section-52s|what is section 52 in ipc|explain section 52 ipc|good faith', 
 ['Section 52 of the IPC defines the term "Good Faith".It refers to an act done with honest intention, even if it may not have been lawful or correct.This section is key in determining the intention behind actions in legal matters.']],

['section-52As|what is section 52A in ipc|explain section 52a ipc|harbour', 
 ['Section 52A of the IPC defines the term "Harbour".It refers to providing shelter, assistance, or protection to a person who is evading the law.This section covers the legal implications of harboring individuals under the IPC.']],

['section-53s|what is section 53 in ipc|explain section 53 ipc|punishment', 
 ['Section 53 of the IPC outlines various types of punishments under the law.These include death, imprisonment for life, rigorous or simple imprisonment, forfeiture of property, and fines.This section is central to understanding the punitive measures under the IPC.']],

['section-53As|what is section 53A in ipc|explain section 53a ipc|construction of reference to transportation', 
 ['Section 53A of the IPC addresses the "Construction of Reference to Transportation".It provides guidelines on how references to transportation for life or other transportation punishments should be understood in the modern context.This section is important for interpreting older laws that included transportation as a punishment.']],

['section-54s|what is section 54 in ipc|explain section 54 ipc|commutation of sentence of death', 
 ['Section 54 of the IPC provides for the commutation of a death sentence.It allows the appropriate government to commute the death sentence to another form of punishment.This section is critical in the administration of capital punishment.']],

['section-55s|what is section 55 in ipc|explain section 55 ipc|commutation of sentence of imprisonment for life', 
 ['Section 55 of the IPC provides for the commutation of a sentence of imprisonment for life.',
  'It allows the appropriate government to commute the life sentence to imprisonment for a term not exceeding fourteen years.',
  'This section provides a mechanism for reducing life sentences.']],

['section-55As|what is section 55A in ipc|explain section 55a ipc|definition of appropriate government', 
 ['Section 55A of the IPC defines the term "Appropriate Government".It refers to the central or state government that has the authority to commute sentences under the law.This section is important for determining which government body has jurisdiction in commutation cases.']],

['section-56s|what is section 56 in ipc|explain section 56 ipc|sentence of europeans and americans to penal servitude', 
 ['Section 56 of the IPC discusses the sentencing of Europeans and Americans to penal servitude.It refers to the old legal practice of sentencing individuals from these groups to hard labor as punishment.This section is of historical interest, reflecting colonial legal practices.']],

['section-57s|what is section 57 in ipc|explain section 57 ipc|fractions of terms of punishment', 
 ['Section 57 of the IPC deals with "Fractions of Terms of Punishment".It states that in calculating fractions of terms of punishment, imprisonment for life shall be reckoned as equivalent to imprisonment for twenty years.This section is significant for sentencing and calculating terms of imprisonment.']],

['section-58s|what is section 58 in ipc|explain section 58 ipc|offenders sentenced to transportation how dealt with until transported', 
 ['Section 58 of the IPC addresses how offenders sentenced to transportation are to be dealt with until they are actually transported.It provides guidelines for the custody and treatment of such offenders while awaiting transportation.This section is relevant in the context of historical punishments.']],

['section-59s|what is section 59 in ipc|explain section 59 ipc|transportation instead of imprisonment', 
 ['Section 59 of the IPC allows for "Transportation Instead of Imprisonment".It refers to the substitution of transportation for another form of imprisonment, subject to certain legal provisions.This section reflects the penal practices of earlier times.']],

['section-60s|what is section 60 in ipc|explain section 60 ipc|sentence may be in certain cases of imprisonment wholly or partly rigorous or simple', 
 ['Section 60 of the IPC provides that sentences of imprisonment may be wholly or partly rigorous or simple.It allows the court to decide whether a convict should undergo rigorous imprisonment (involving hard labor) or simple imprisonment.This section offers flexibility in sentencing based on the nature of the offense.']],

['section-61s|what is section 61 in ipc|explain section 61 ipc|sentence of forfeiture of property', 
 ['Section 61 of the IPC relates to the "Sentence of Forfeiture of Property".It allows the court to order the forfeiture of a convict’s property as part of the punishment for certain offenses.This section was originally part of the IPC but has been repealed.']],

  
  
  ]
  
    

# Create a Chat object
chatbot= Chat(pairs, reflections)

# Start conversation
time.sleep(2)
print("PLEASE CHECK THE   DATE AND TIME")
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)
time.sleep(1.3)
print("Welcome! Its FALCON CODERS  chatbot... Ask me DOJ--Department of Justice related laws and contents based questions ..... Im here to assist you .")

time.sleep(2.5)
print("  YOU CAN LEARN ABOUT EACH SECTION BY TYPING AS [what is section<section number> in ipc format ].........")

time.sleep(2.9)



print(" HEY ENGINEER WELCOME TO SPARKATHON  2024  ")

# Define the two lines of the welcome message with emojis
line1 = "🎉 WELCOMES YOU 🎉"
line2 = "Welcome to DoJ Chatbot! 👋"

# Print the welcome message
print(line1)
time.sleep(1.5)
print(line2)
while True:
    user_input = input("Spark: ")
    response = chatbot.respond(user_input)
    print("FALCON CODER:", response)
    if user_input.lower() == 'bye':
        break
