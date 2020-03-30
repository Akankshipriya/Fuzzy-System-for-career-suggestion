import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
Physics = ctrl.Antecedent(np.arange(0,101,1),'Physics')
Maths = ctrl.Antecedent(np.arange(0,101,1),'Maths')
Chemistry = ctrl.Antecedent(np.arange(0,101,1),'Chemistry')
Biology = ctrl.Antecedent(np.arange(0,101,1),'Biology')
Business = ctrl.Antecedent(np.arange(0,101,1),'Business')
Accountancy = ctrl.Antecedent(np.arange(0,101,1),'Accountancy')
PE = ctrl.Antecedent(np.arange(0,101,1),'PE')
CS = ctrl.Antecedent(np.arange(0,101,1),'CS')
History = ctrl.Antecedent(np.arange(0,101,1),'History')
Geography = ctrl.Antecedent(np.arange(0,101,1),'Geography')
Politics = ctrl.Antecedent(np.arange(0,101,1),'Politics')
Economy = ctrl.Antecedent(np.arange(0,101,1),'Economy')
Literature = ctrl.Antecedent(np.arange(0,101,1),'Literature')
Language = ctrl.Antecedent(np.arange(0,101,1),'Language')
Art = ctrl.Antecedent(np.arange(0,101,1),'Art')

Engineering = ctrl.Consequent(np.arange(0,1.1,0.1),'Engineering')
Medicine = ctrl.Consequent(np.arange(0,1.1,0.1),'Medicine')
Management = ctrl.Consequent(np.arange(0,1.1,0.1),'Management')
Hospitality = ctrl.Consequent(np.arange(0,1.1,0.1),'Hospitality')
Chief = ctrl.Consequent(np.arange(0,1.1,0.1),'Chief')
Teacher = ctrl.Consequent(np.arange(0,1.1,0.1),'Teacher')
Researcher = ctrl.Consequent(np.arange(0,1.1,0.1),'Researcher')
Architect = ctrl.Consequent(np.arange(0,1.1,0.1),'Architect')
Artist = ctrl.Consequent(np.arange(0,1.1,0.1),'Artist')
Athlete = ctrl.Consequent(np.arange(0,1.1,0.1),'Athlete')
Fitness_trainer = ctrl.Consequent(np.arange(0,1.1,0.1),'Fitness_trainer')
Politician = ctrl.Consequent(np.arange(0,1.1,0.1),'Politician')
Archeologist = ctrl.Consequent(np.arange(0,1.1,0.1),'Archeologist')
Poet = ctrl.Consequent(np.arange(0,1.1,0.1),'Poet')
Writer = ctrl.Consequent(np.arange(0,1.1,0.1),'Writer')
chemist = ctrl.Consequent(np.arange(0,1.1,0.1),'chemist')
work_around = ctrl.Consequent(np.arange(0,1.1,0.1),'work_around')

Physics['Excellent'] = fuzzy.trapmf(Physics.universe,[70,85,100,100])
Physics['Good'] = fuzzy.trapmf(Physics.universe,[55,70,75,75])
Physics['Average'] = fuzzy.trapmf(Physics.universe,[38,55,60,60])
Physics['Poor'] = fuzzy.trapmf(Physics.universe,[25,30,40,40])
Physics['Very_Poor'] = fuzzy.trapmf(Physics.universe,[0,15,25,25])
Maths['Excellent'] = fuzzy.trapmf(Maths.universe,[70,85,100,100])
Maths['Good'] = fuzzy.trapmf(Maths.universe,[55,70,75,75])
Maths['Average'] = fuzzy.trapmf(Maths.universe,[38,55,60,60])
Maths['Poor'] = fuzzy.trapmf(Maths.universe,[25,30,40,40])
Maths['Very_Poor'] = fuzzy.trapmf(Maths.universe,[0,15,25,25])
Chemistry['Excellent'] = fuzzy.trapmf(Chemistry.universe,[70,85,100,100])
Chemistry['Good'] = fuzzy.trapmf(Chemistry.universe,[55,70,75,75])
Chemistry['Average'] = fuzzy.trapmf(Chemistry.universe,[38,55,60,60])
Chemistry['Poor'] = fuzzy.trapmf(Chemistry.universe,[25,30,40,40])
Chemistry['Very_Poor'] = fuzzy.trapmf(Chemistry.universe,[0,15,25,25])
Biology['Excellent'] = fuzzy.trapmf(Biology.universe,[70,85,100,100])
Biology['Good'] = fuzzy.trapmf(Biology.universe,[55,70,75,75])
Biology['Average'] = fuzzy.trapmf(Biology.universe,[38,55,60,60])
Biology['Poor'] = fuzzy.trapmf(Biology.universe,[25,30,40,40])
Biology['Very_Poor'] = fuzzy.trapmf(Biology.universe,[0,15,25,25])
Business['Excellent'] = fuzzy.trapmf(Business.universe,[70,85,100,100])
Business['Good'] = fuzzy.trapmf(Business.universe,[55,70,75,75])
Business['Average'] = fuzzy.trapmf(Business.universe,[38,55,60,60])
Business['Poor'] = fuzzy.trapmf(Business.universe,[25,30,40,40])
Business['Very_Poor'] = fuzzy.trapmf(Business.universe,[0,15,25,25])
Accountancy['Excellent'] = fuzzy.trapmf(Accountancy.universe,[70,85,100,100])
Accountancy['Good'] = fuzzy.trapmf(Accountancy.universe,[55,70,75,75])
Accountancy['Average'] = fuzzy.trapmf(Accountancy.universe,[38,55,60,60])
Accountancy['Poor'] = fuzzy.trapmf(Accountancy.universe,[25,30,40,40])
Accountancy['Very_Poor'] = fuzzy.trapmf(Accountancy.universe,[0,15,25,25])
PE['Excellent'] = fuzzy.trapmf(PE.universe,[70,85,100,100])
PE['Good'] = fuzzy.trapmf(PE.universe,[55,70,75,75])
PE['Average'] = fuzzy.trapmf(PE.universe,[38,55,60,60])
PE['Poor'] = fuzzy.trapmf(PE.universe,[25,30,40,40])
PE['Very_Poor'] = fuzzy.trapmf(PE.universe,[0,15,25,25])
CS['Excellent'] = fuzzy.trapmf(CS.universe,[70,85,100,100])
CS['Good'] = fuzzy.trapmf(CS.universe,[55,70,75,75])
CS['Average'] = fuzzy.trapmf(CS.universe,[38,55,60,60])
CS['Poor'] = fuzzy.trapmf(CS.universe,[25,30,40,40])
CS['Very_Poor'] = fuzzy.trapmf(CS.universe,[0,15,25,25])
History['Excellent'] = fuzzy.trapmf(History.universe,[70,85,100,100])
History['Good'] = fuzzy.trapmf(History.universe,[55,70,75,75])
History['Average'] = fuzzy.trapmf(History.universe,[38,55,60,60])
History['Poor'] = fuzzy.trapmf(History.universe,[25,30,40,40])
History['Very_Poor'] = fuzzy.trapmf(History.universe,[0,15,25,25])
Geography['Excellent'] = fuzzy.trapmf(Geography.universe,[70,85,100,100])
Geography['Good'] = fuzzy.trapmf(Geography.universe,[55,70,75,75])
Geography['Average'] = fuzzy.trapmf(Geography.universe,[38,55,60,60])
Geography['Poor'] = fuzzy.trapmf(Geography.universe,[25,30,40,40])
Geography['Very_Poor'] = fuzzy.trapmf(Geography.universe,[0,15,25,25])
Economy['Excellent'] = fuzzy.trapmf(Economy.universe,[70,85,100,100])
Economy['Good'] = fuzzy.trapmf(Economy.universe,[55,70,75,75])
Economy['Average'] = fuzzy.trapmf(Economy.universe,[38,55,60,60])
Economy['Poor'] = fuzzy.trapmf(Economy.universe,[25,30,40,40])
Economy['Very_Poor'] = fuzzy.trapmf(Economy.universe,[0,15,25,25])
Politics['Excellent'] = fuzzy.trapmf(Politics.universe,[70,85,100,100])
Politics['Good'] = fuzzy.trapmf(Politics.universe,[55,70,75,75])
Politics['Average'] = fuzzy.trapmf(Politics.universe,[38,55,60,60])
Politics['Poor'] = fuzzy.trapmf(Politics.universe,[25,30,40,40])
Politics['Very_Poor'] = fuzzy.trapmf(Politics.universe,[0,15,25,25])
Literature['Excellent'] = fuzzy.trapmf(Literature.universe,[70,85,100,100])
Literature['Good'] = fuzzy.trapmf(Literature.universe,[55,70,75,75])
Literature['Average'] = fuzzy.trapmf(Literature.universe,[38,55,60,60])
Literature['Poor'] = fuzzy.trapmf(Literature.universe,[25,30,40,40])
Literature['Very_Poor'] = fuzzy.trapmf(Literature.universe,[0,15,25,25])
Language['Excellent'] = fuzzy.trapmf(Language.universe,[70,85,100,100])
Language['Good'] = fuzzy.trapmf(Language.universe,[55,70,75,75])
Language['Average'] = fuzzy.trapmf(Language.universe,[38,55,60,60])
Language['Poor'] = fuzzy.trapmf(Language.universe,[25,30,40,40])
Language['Very_Poor'] = fuzzy.trapmf(Language.universe,[0,15,25,25])
Art['Excellent'] = fuzzy.trapmf(Art.universe,[70,85,100,100])
Art['Good'] = fuzzy.trapmf(Art.universe,[55,70,75,75])
Art['Average'] = fuzzy.trapmf(Art.universe,[38,55,60,60])
Art['Poor'] = fuzzy.trapmf(Art.universe,[25,30,40,40])
Art['Very_Poor'] = fuzzy.trapmf(Art.universe,[0,15,25,25])

Engineering.automf(names=['Not_good','Good','Excellent'])
Medicine.automf(names=['Not_good','Good','Excellent'])
Hospitality.automf(names=['Not_good','Good','Excellent'])
Management.automf(names=['Not_good','Good','Excellent'])
Chief.automf(names=['Not_good','Good','Excellent'])
Teacher.automf(names=['Not_good','Good','Excellent'])
Researcher.automf(names=['Not_good','Good','Excellent'])
Architect.automf(names=['Not_good','Good','Excellent'])
Artist.automf(names=['Not_good','Good','Excellent'])
Athlete.automf(names=['Not_good','Good','Excellent'])
Fitness_trainer.automf(names=['Not_good','Good','Excellent'])
Politician.automf(names=['Not_good','Good','Excellent'])
Archeologist.automf(names=['Not_good','Good','Excellent'])
Poet.automf(names=['Not_good','Good','Excellent'])
Writer.automf(names=['Not_good','Good','Excellent'])
chemist.automf(names=['Not_good','Good','Excellent'])
work_around.automf(names=['DUD'])

Physics.view()
Maths.view()
Chemistry.view()
Biology.view()
Business.view()
Accountancy.view()
PE.view()
CS.view()
History.view()
Geography.view()
Politics.view()
Economy.view()
Literature.view()
Language.view()
Art.view()

Engineering.view()
Medicine.view()
Management.view()
Hospitality.view()
Chief.view()
Teacher.view()
Researcher.view()
Architect.view()
Artist.view()
Athlete.view()
Fitness_trainer.view()
Politician.view()
Archeologist.view()
Poet.view()
Writer.view()
chemist.view()
work_around.view()

rule1 = ctrl.Rule(Physics['Excellent'] & Maths['Excellent'] & Chemistry['Excellent'], Engineering['Excellent'])
rule2 = ctrl.Rule(Physics['Excellent'] & Maths['Excellent'] & Chemistry['Good'], Engineering['Excellent'])
rule3 = ctrl.Rule(Physics['Excellent'] & Maths['Excellent'] & Chemistry['Average'], Engineering['Excellent'])
rule4 = ctrl.Rule(Physics['Excellent'] & Maths['Good'] & Chemistry['Excellent'], Engineering['Excellent'])
rule5 = ctrl.Rule(Physics['Excellent'] & Maths['Good'] & Chemistry['Good'], Engineering['Excellent'])
rule6 = ctrl.Rule(Physics['Excellent'] & Maths['Good'] & Chemistry['Average'], Engineering['Excellent'])
rule7 = ctrl.Rule(Physics['Excellent'] & Maths['Average'] & Chemistry['Excellent'], Engineering['Good'])
rule8 = ctrl.Rule(Physics['Excellent'] & Maths['Average'] & Chemistry['Good'], Engineering['Good'])
rule9 = ctrl.Rule(Physics['Excellent'] & Maths['Average'] & Chemistry['Average'], Engineering['Good'])

rule10 = ctrl.Rule(Physics['Good'] & Maths['Excellent'] & Chemistry['Excellent'], Engineering['Excellent'])
rule12 = ctrl.Rule(Physics['Good'] & Maths['Excellent'] & Chemistry['Good'], Engineering['Good'])
rule13 = ctrl.Rule(Physics['Good'] & Maths['Excellent'] & Chemistry['Average'], Engineering['Good'])
rule11 = ctrl.Rule(Physics['Good'] & Maths['Good'] & Chemistry['Excellent'], Engineering['Good'])
rule14 = ctrl.Rule(Physics['Good'] & Maths['Good'] & Chemistry['Good'], Engineering['Good'])
rule15 = ctrl.Rule(Physics['Good'] & Maths['Good'] & Chemistry['Average'], Engineering['Good'])
rule16 = ctrl.Rule(Physics['Good'] & Maths['Average'] & Chemistry['Excellent'], Engineering['Good'])
rule17 = ctrl.Rule(Physics['Good'] & Maths['Average'] & Chemistry['Good'], Engineering['Good'])
rule18 = ctrl.Rule(Physics['Good'] & Maths['Average'] & Chemistry['Average'], Engineering['Good'])

rule19 = ctrl.Rule(Physics['Average'] & Maths['Excellent'] & Chemistry['Excellent'], Engineering['Good'])
rule20 = ctrl.Rule(Physics['Average'] & Maths['Excellent'] & Chemistry['Good'], Engineering['Good'])
rule21 = ctrl.Rule(Physics['Average'] & Maths['Excellent'] & Chemistry['Average'], Engineering['Good'])
rule22 = ctrl.Rule(Physics['Average'] & Maths['Good'] & Chemistry['Excellent'], Engineering['Good'])
rule23 = ctrl.Rule(Physics['Average'] & Maths['Good'] & Chemistry['Good'], Engineering['Good'])
rule24 = ctrl.Rule(Physics['Average'] & Maths['Good'] & Chemistry['Average'], Engineering['Good'])
rule25 = ctrl.Rule(Physics['Average'] & Maths['Average'] & Chemistry['Excellent'], Engineering['Not_good'])
rule26 = ctrl.Rule(Physics['Average'] & Maths['Average'] & Chemistry['Good'], Engineering['Not_good'])
rule27 = ctrl.Rule(Physics['Average'] & Maths['Average'] & Chemistry['Average'], Engineering['Not_good'])

rule28 = ctrl.Rule(Physics['Excellent'] & Biology['Excellent'] & Chemistry['Excellent'], Medicine['Excellent'])
rule29 = ctrl.Rule(Physics['Excellent'] & Biology['Excellent'] & Chemistry['Good'], Medicine['Excellent'])
rule30 = ctrl.Rule(Physics['Excellent'] & Biology['Excellent'] & Chemistry['Average'], Medicine['Excellent'])
rule31 = ctrl.Rule(Physics['Excellent'] & Biology['Good'] & Chemistry['Excellent'], Medicine['Excellent'])
rule32 = ctrl.Rule(Physics['Excellent'] & Biology['Good'] & Chemistry['Good'], Medicine['Excellent'])
rule33 = ctrl.Rule(Physics['Excellent'] & Biology['Good'] & Chemistry['Average'], Medicine['Excellent'])
rule34 = ctrl.Rule(Physics['Excellent'] & Biology['Average'] & Chemistry['Excellent'], Medicine['Good'])
rule35 = ctrl.Rule(Physics['Excellent'] & Biology['Average'] & Chemistry['Good'], Medicine['Good'])
rule36 = ctrl.Rule(Physics['Excellent'] & Biology['Average'] & Chemistry['Average'], Medicine['Good'])

rule37 = ctrl.Rule(Physics['Good'] & Biology['Excellent'] & Chemistry['Excellent'], Medicine['Excellent'])
rule38 = ctrl.Rule(Physics['Good'] & Biology['Excellent'] & Chemistry['Good'], Medicine['Good'])
rule39 = ctrl.Rule(Physics['Good'] & Biology['Excellent'] & Chemistry['Average'], Medicine['Good'])
rule40 = ctrl.Rule(Physics['Good'] & Biology['Good'] & Chemistry['Excellent'], Medicine['Good'])
rule41 = ctrl.Rule(Physics['Good'] & Biology['Good'] & Chemistry['Good'], Medicine['Good'])
rule42 = ctrl.Rule(Physics['Good'] & Biology['Good'] & Chemistry['Average'], Medicine['Good'])
rule43 = ctrl.Rule(Physics['Good'] & Biology['Average'] & Chemistry['Excellent'], Medicine['Good'])
rule44 = ctrl.Rule(Physics['Good'] & Biology['Average'] & Chemistry['Good'], Medicine['Good'])
rule45 = ctrl.Rule(Physics['Average'] & Biology['Average'] & Chemistry['Average'], Medicine['Not_good'])

rule46 = ctrl.Rule(Physics['Good'] & Biology['Average'] & Chemistry['Average'], Medicine['Good'])
rule47 = ctrl.Rule(Physics['Average'] & Biology['Excellent'] & Chemistry['Excellent'], Medicine['Good'])
rule48 = ctrl.Rule(Physics['Average'] & Biology['Excellent'] & Chemistry['Good'], Medicine['Good'])
rule49 = ctrl.Rule(Physics['Average'] & Biology['Excellent'] & Chemistry['Average'], Medicine['Good'])
rule50 = ctrl.Rule(Physics['Average'] & Biology['Good'] & Chemistry['Excellent'], Medicine['Good'])
rule51 = ctrl.Rule(Physics['Average'] & Biology['Good'] & Chemistry['Good'], Medicine['Good'])
rule52 = ctrl.Rule(Physics['Average'] & Biology['Good'] & Chemistry['Average'], Medicine['Good'])
rule53 = ctrl.Rule(Physics['Average'] & Biology['Average'] & Chemistry['Excellent'], Medicine['Not_good'])
rule54 = ctrl.Rule(Physics['Average'] & Biology['Average'] & Chemistry['Good'], Medicine['Not_good'])

rule55 = ctrl.Rule(Accountancy['Excellent'] & Business['Excellent'], Management['Excellent'])
rule56 = ctrl.Rule(Accountancy['Good'] & Business['Excellent'], Management['Excellent'])
rule57 = ctrl.Rule(Accountancy['Average'] & Business['Excellent'], Management['Good'])
rule58 = ctrl.Rule(Accountancy['Excellent'] & Business['Good'], Management['Excellent'])
rule59 = ctrl.Rule(Accountancy['Good'] & Business['Good'], Management['Good'])
rule60 = ctrl.Rule(Accountancy['Average'] & Business['Good'], Management['Not_good'])
rule61 = ctrl.Rule(Accountancy['Excellent'] & Business['Average'], Management['Good'])
rule62 = ctrl.Rule(Accountancy['Good'] & Business['Average'], Management['Good'])
rule63 = ctrl.Rule(Accountancy['Average'] & Business['Average'], Management['Not_good'])

rule64 = ctrl.Rule(Language['Excellent'] & Business['Excellent'], Hospitality['Excellent'])
rule65 = ctrl.Rule(Language['Good'] & Business['Excellent'], Hospitality['Excellent'])
rule66 = ctrl.Rule(Language['Average'] & Business['Excellent'], Hospitality['Good'])
rule67 = ctrl.Rule(Language['Excellent'] & Business['Good'], Hospitality['Excellent'])
rule68 = ctrl.Rule(Language['Good'] & Business['Good'], Hospitality['Good'])
rule69 = ctrl.Rule(Language['Average'] & Business['Good'], Hospitality['Not_good'])
rule70 = ctrl.Rule(Language['Excellent'] & Business['Average'], Hospitality['Good'])
rule71 = ctrl.Rule(Language['Good'] & Business['Average'], Hospitality['Good'])
rule72 = ctrl.Rule(Language['Average'] & Business['Average'], Hospitality['Not_good'])

rule73 = ctrl.Rule(Art['Excellent'] & Language['Excellent'] & History['Excellent'], Chief['Excellent'])
rule74 = ctrl.Rule(Art['Excellent'] & Language['Excellent'] & History['Good'], Chief['Excellent'])
rule75 = ctrl.Rule(Art['Excellent'] & Language['Excellent'] & History['Average'], Chief['Excellent'])
rule76 = ctrl.Rule(Art['Excellent'] & Language['Good'] & History['Excellent'], Chief['Excellent'])
rule77 = ctrl.Rule(Art['Excellent'] & Language['Good'] & History['Good'], Chief['Excellent'])
rule79 = ctrl.Rule(Art['Excellent'] & Language['Good'] & History['Average'], Chief['Excellent'])
rule78 = ctrl.Rule(Art['Average'] & Language['Average'] & History['Average'], Chief['Not_good'])
rule80 = ctrl.Rule(Art['Excellent'] & Language['Average'] & History['Excellent'], Chief['Excellent'])
rule81 = ctrl.Rule(Art['Excellent'] & Language['Average'] & History['Good'], Chief['Good'])

rule82 = ctrl.Rule(Art['Excellent'] & Language['Average'] & History['Average'], Chief['Good'])
rule83 = ctrl.Rule(Art['Good'] & Language['Excellent'] & History['Excellent'], Chief['Excellent'])
rule84 = ctrl.Rule(Art['Good'] & Language['Excellent'] & History['Good'], Chief['Good'])
rule85 = ctrl.Rule(Art['Good'] & Language['Excellent'] & History['Average'], Chief['Good'])
rule86 = ctrl.Rule(Art['Good'] & Language['Good'] & History['Excellent'], Chief['Good'])
rule87 = ctrl.Rule(Art['Good'] & Language['Good'] & History['Good'], Chief['Good'])
rule88 = ctrl.Rule(Art['Good'] & Language['Good'] & History['Average'], Chief['Good'])
rule89 = ctrl.Rule(Art['Good'] & Language['Average'] & History['Excellent'], Chief['Good'])
rule90 = ctrl.Rule(Art['Good'] & Language['Average'] & History['Good'], Chief['Good'])
rule91 = ctrl.Rule(Art['Good'] & Language['Average'] & History['Average'], Chief['Good'])

rule92 = ctrl.Rule(Art['Average'] & Language['Excellent'] & History['Excellent'], Chief['Good'])
rule93 = ctrl.Rule(Art['Average'] & Language['Excellent'] & History['Good'], Chief['Good'])
rule94 = ctrl.Rule(Art['Average'] & Language['Excellent'] & History['Average'], Chief['Good'])
rule95 = ctrl.Rule(Art['Average'] & Language['Good'] & History['Excellent'], Chief['Good'])
rule96 = ctrl.Rule(Art['Average'] & Language['Good'] & History['Good'], Chief['Good'])
rule97 = ctrl.Rule(Art['Average'] & Language['Good'] & History['Average'], Chief['Good'])
rule98 = ctrl.Rule(Art['Average'] & Language['Average'] & History['Excellent'], Chief['Not_good'])
rule99 = ctrl.Rule(Art['Average'] & Language['Average'] & History['Good'], Chief['Not_good'])

rule100 = ctrl.Rule(Physics['Very_Poor'],work_around['DUD'])
rule101 = ctrl.Rule(Maths['Very_Poor'],work_around['DUD'])
rule102 = ctrl.Rule(Chemistry['Very_Poor'],work_around['DUD'])
rule103 = ctrl.Rule(Biology['Very_Poor'],work_around['DUD'])
rule104 = ctrl.Rule(Business['Very_Poor'],work_around['DUD'])
rule105 = ctrl.Rule(Accountancy['Very_Poor'],work_around['DUD'])
rule106 = ctrl.Rule(PE['Very_Poor'],work_around['DUD'])
rule107 = ctrl.Rule(CS['Very_Poor'],work_around['DUD'])
rule108 = ctrl.Rule(History['Very_Poor'],work_around['DUD'])
rule109 = ctrl.Rule(Geography['Very_Poor'],work_around['DUD'])
rule110 = ctrl.Rule(Politics['Very_Poor'],work_around['DUD'])
rule111 = ctrl.Rule(Economy['Very_Poor'],work_around['DUD'])
rule112 = ctrl.Rule(Literature['Very_Poor'],work_around['DUD'])
rule113 = ctrl.Rule(Language['Very_Poor'],work_around['DUD'])
rule114 = ctrl.Rule(Art['Very_Poor'],work_around['DUD'])

rule115 = ctrl.Rule(Physics['Poor'],work_around['DUD'])
rule116 = ctrl.Rule(Maths['Poor'],work_around['DUD'])
rule117 = ctrl.Rule(Chemistry['Poor'],work_around['DUD'])
rule118 = ctrl.Rule(Biology['Poor'],work_around['DUD'])
rule119 = ctrl.Rule(Business['Poor'],work_around['DUD'])
rule120 = ctrl.Rule(Accountancy['Poor'],work_around['DUD'])
rule121 = ctrl.Rule(PE['Poor'],work_around['DUD'])
rule122 = ctrl.Rule(CS['Poor'],work_around['DUD'])
rule123 = ctrl.Rule(History['Poor'],work_around['DUD'])
rule124 = ctrl.Rule(Geography['Poor'],work_around['DUD'])
rule125 = ctrl.Rule(Politics['Poor'],work_around['DUD'])
rule126 = ctrl.Rule(Economy['Poor'],work_around['DUD'])
rule127 = ctrl.Rule(Literature['Poor'],work_around['DUD'])
rule128 = ctrl.Rule(Language['Poor'],work_around['DUD'])
rule129 = ctrl.Rule(Art['Poor'],work_around['DUD'])

rule130 = ctrl.Rule(Language['Excellent'] & (Chemistry['Excellent'] | Physics['Excellent'] | Maths['Excellent'] |  Biology['Excellent'] |  Business['Excellent'] |  Accountancy['Excellent'] |  PE['Excellent'] |  CS['Excellent'] |  History['Excellent'] |  Geography['Excellent'] |  Politics['Excellent'] |  Economy['Excellent'] |  Literature['Excellent'] |  Art['Excellent']), Teacher['Excellent'])
rule131 = ctrl.Rule(Language['Excellent'] & (Chemistry['Good'] | Physics['Good'] | Maths['Good'] |  Biology['Good'] |  Business['Good'] |  Accountancy['Good'] |  PE['Good'] |  CS['Good'] |  History['Good'] |  Geography['Good'] |  Politics['Good'] |  Economy['Good'] |  Literature['Good'] |  Art['Good']), Teacher['Excellent'])
rule132 = ctrl.Rule(Language['Excellent'] & (Chemistry['Average'] | Physics['Average'] | Maths['Average'] |  Biology['Average'] |  Business['Average'] |  Accountancy['Average'] |  PE['Average'] |  CS['Average'] |  History['Average'] |  Geography['Average'] |  Politics['Average'] |  Economy['Average'] |  Literature['Average'] |  Art['Average']), Teacher['Good'])
rule133 = ctrl.Rule(Language['Good'] & (Chemistry['Excellent'] | Physics['Excellent'] | Maths['Excellent'] |  Biology['Excellent'] |  Business['Excellent'] |  Accountancy['Excellent'] |  PE['Excellent'] |  CS['Excellent'] |  History['Excellent'] |  Geography['Excellent'] |  Politics['Excellent'] |  Economy['Excellent'] |  Literature['Excellent'] |  Art['Excellent']), Teacher['Excellent'])
rule134 = ctrl.Rule(Language['Good'] & (Chemistry['Good'] | Physics['Good'] | Maths['Good'] |  Biology['Good'] |  Business['Good'] |  Accountancy['Good'] |  PE['Good'] |  CS['Good'] |  History['Good'] |  Geography['Good'] |  Politics['Good'] |  Economy['Good'] |  Literature['Good'] |  Art['Good']), Teacher['Good'])
rule135 = ctrl.Rule(Language['Good'] & (Chemistry['Average'] | Physics['Average'] | Maths['Average'] |  Biology['Average'] |  Business['Average'] |  Accountancy['Average'] |  PE['Average'] |  CS['Average'] |  History['Average'] |  Geography['Average'] |  Politics['Average'] |  Economy['Average'] |  Literature['Average'] |  Art['Average']), Teacher['Good'])
rule136 = ctrl.Rule(Language['Average'] & (Chemistry['Excellent'] | Physics['Excellent'] | Maths['Excellent'] |  Biology['Excellent'] |  Business['Excellent'] |  Accountancy['Excellent'] |  PE['Excellent'] |  CS['Excellent'] |  History['Excellent'] |  Geography['Excellent'] |  Politics['Excellent'] |  Economy['Excellent'] |  Literature['Excellent'] |  Art['Excellent']), Teacher['Good'])
rule137 = ctrl.Rule(Language['Average'] & (Chemistry['Good'] | Physics['Good'] | Maths['Good'] |  Biology['Good'] |  Business['Good'] |  Accountancy['Good'] |  PE['Good'] |  CS['Good'] |  History['Good'] |  Geography['Good'] |  Politics['Good'] |  Economy['Good'] |  Literature['Good'] |  Art['Good']), Teacher['Not_good'])
rule138 = ctrl.Rule(Language['Average'] & (Chemistry['Average'] | Physics['Average'] | Maths['Average'] |  Biology['Average'] |  Business['Average'] |  Accountancy['Average'] |  PE['Average'] |  CS['Average'] |  History['Average'] |  Geography['Average'] |  Politics['Average'] |  Economy['Average'] |  Literature['Average'] |  Art['Average']), Teacher['Not_good'])

rule139 = ctrl.Rule(Language['Excellent'] & Maths['Excellent'] & (Chemistry['Excellent'] | Physics['Excellent'] | Biology['Excellent'] |  Business['Excellent'] |  Accountancy['Excellent'] |  PE['Excellent'] |  CS['Excellent'] |  History['Excellent'] |  Geography['Excellent'] |  Politics['Excellent'] |  Economy['Excellent'] |  Literature['Excellent'] |  Art['Excellent']), Researcher['Excellent'])
rule140 = ctrl.Rule(Language['Excellent'] & Maths['Excellent'] & (Chemistry['Good'] | Physics['Good'] | Biology['Good'] |  Business['Good'] |  Accountancy['Good'] |  PE['Good'] |  CS['Good'] |  History['Good'] |  Geography['Good'] |  Politics['Good'] |  Economy['Good'] |  Literature['Good'] |  Art['Good']), Researcher['Excellent'])
rule141 = ctrl.Rule(Language['Excellent'] & Maths['Excellent'] & (Chemistry['Average'] | Physics['Average'] | Biology['Average'] |  Business['Average'] |  Accountancy['Average'] |  PE['Average'] |  CS['Average'] |  History['Average'] |  Geography['Average'] |  Politics['Average'] |  Economy['Average'] |  Literature['Average'] |  Art['Average']), Researcher['Good'])
rule142 = ctrl.Rule(Language['Excellent'] & Maths['Good'] & (Chemistry['Excellent'] | Physics['Excellent'] | Biology['Excellent'] |  Business['Excellent'] |  Accountancy['Excellent'] |  PE['Excellent'] |  CS['Excellent'] |  History['Excellent'] |  Geography['Excellent'] |  Politics['Excellent'] |  Economy['Excellent'] |  Literature['Excellent'] |  Art['Excellent']), Researcher['Excellent'])
rule143 = ctrl.Rule(Language['Excellent'] & Maths['Good'] & (Chemistry['Good'] | Physics['Good'] |  Biology['Good'] |  Business['Good'] |  Accountancy['Good'] |  PE['Good'] |  CS['Good'] |  History['Good'] |  Geography['Good'] |  Politics['Good'] |  Economy['Good'] |  Literature['Good'] |  Art['Good']), Researcher['Excellent'])
rule144 = ctrl.Rule(Language['Excellent'] & Maths['Good'] & (Chemistry['Average'] | Physics['Average'] |  Biology['Average'] |  Business['Average'] |  Accountancy['Average'] |  PE['Average'] |  CS['Average'] |  History['Average'] |  Geography['Average'] |  Politics['Average'] |  Economy['Average'] |  Literature['Average'] |  Art['Average']), Researcher['Good'])
rule145 = ctrl.Rule(Language['Excellent'] & Maths['Average'] & (Chemistry['Excellent'] | Physics['Excellent'] | Biology['Excellent'] |  Business['Excellent'] |  Accountancy['Excellent'] |  PE['Excellent'] |  CS['Excellent'] |  History['Excellent'] |  Geography['Excellent'] |  Politics['Excellent'] |  Economy['Excellent'] |  Literature['Excellent'] |  Art['Excellent']), Researcher['Excellent'])
rule146 = ctrl.Rule(Language['Excellent'] & Maths['Average'] & (Chemistry['Good'] | Physics['Good'] |  Biology['Good'] |  Business['Good'] |  Accountancy['Good'] |  PE['Good'] |  CS['Good'] |  History['Good'] |  Geography['Good'] |  Politics['Good'] |  Economy['Good'] |  Literature['Good'] |  Art['Good']), Researcher['Excellent'])
rule147 = ctrl.Rule(Language['Excellent'] & Maths['Average'] & (Chemistry['Average'] | Physics['Average'] |  Biology['Average'] |  Business['Average'] |  Accountancy['Average'] |  PE['Average'] |  CS['Average'] |  History['Average'] |  Geography['Average'] |  Politics['Average'] |  Economy['Average'] |  Literature['Average'] |  Art['Average']), Researcher['Good'])

rule148 = ctrl.Rule(Language['Good'] & Maths['Excellent'] & (Chemistry['Excellent'] | Physics['Excellent'] | Biology['Excellent'] |  Business['Excellent'] |  Accountancy['Excellent'] |  PE['Excellent'] |  CS['Excellent'] |  History['Excellent'] |  Geography['Excellent'] |  Politics['Excellent'] |  Economy['Excellent'] |  Literature['Excellent'] |  Art['Excellent']), Researcher['Excellent'])
rule149 = ctrl.Rule(Language['Good'] & Maths['Excellent'] & (Chemistry['Good'] | Physics['Good'] | Biology['Good'] |  Business['Good'] |  Accountancy['Good'] |  PE['Good'] |  CS['Good'] |  History['Good'] |  Geography['Good'] |  Politics['Good'] |  Economy['Good'] |  Literature['Good'] |  Art['Good']), Researcher['Good'])
rule150 = ctrl.Rule(Language['Good'] & Maths['Excellent'] & (Chemistry['Average'] | Physics['Average'] | Biology['Average'] |  Business['Average'] |  Accountancy['Average'] |  PE['Average'] |  CS['Average'] |  History['Average'] |  Geography['Average'] |  Politics['Average'] |  Economy['Average'] |  Literature['Average'] |  Art['Average']), Researcher['Not_good'])
rule151 = ctrl.Rule(Language['Good'] & Maths['Good'] & (Chemistry['Excellent'] | Physics['Excellent'] | Biology['Excellent'] |  Business['Excellent'] |  Accountancy['Excellent'] |  PE['Excellent'] |  CS['Excellent'] |  History['Excellent'] |  Geography['Excellent'] |  Politics['Excellent'] |  Economy['Excellent'] |  Literature['Excellent'] |  Art['Excellent']), Researcher['Excellent'])
rule152 = ctrl.Rule(Language['Good'] & Maths['Good'] & (Chemistry['Good'] | Physics['Good'] |  Biology['Good'] |  Business['Good'] |  Accountancy['Good'] |  PE['Good'] |  CS['Good'] |  History['Good'] |  Geography['Good'] |  Politics['Good'] |  Economy['Good'] |  Literature['Good'] |  Art['Good']), Researcher['Good'])
rule153 = ctrl.Rule(Language['Good'] & Maths['Good'] & (Chemistry['Average'] | Physics['Average'] |  Biology['Average'] |  Business['Average'] |  Accountancy['Average'] |  PE['Average'] |  CS['Average'] |  History['Average'] |  Geography['Average'] |  Politics['Average'] |  Economy['Average'] |  Literature['Average'] |  Art['Average']), Researcher['Not_good'])
rule154 = ctrl.Rule(Language['Good'] & Maths['Average'] & (Chemistry['Excellent'] | Physics['Excellent'] | Biology['Excellent'] |  Business['Excellent'] |  Accountancy['Excellent'] |  PE['Excellent'] |  CS['Excellent'] |  History['Excellent'] |  Geography['Excellent'] |  Politics['Excellent'] |  Economy['Excellent'] |  Literature['Excellent'] |  Art['Excellent']), Researcher['Excellent'])
rule155 = ctrl.Rule(Language['Good'] & Maths['Average'] & (Chemistry['Good'] | Physics['Good'] |  Biology['Good'] |  Business['Good'] |  Accountancy['Good'] |  PE['Good'] |  CS['Good'] |  History['Good'] |  Geography['Good'] |  Politics['Good'] |  Economy['Good'] |  Literature['Good'] |  Art['Good']), Researcher['Good'])
rule156 = ctrl.Rule(Language['Good'] & Maths['Average'] & (Chemistry['Average'] | Physics['Average'] |  Biology['Average'] |  Business['Average'] |  Accountancy['Average'] |  PE['Average'] |  CS['Average'] |  History['Average'] |  Geography['Average'] |  Politics['Average'] |  Economy['Average'] |  Literature['Average'] |  Art['Average']), Researcher['Not_good'])

rule157 = ctrl.Rule(Language['Average'] & Maths['Excellent'] & (Chemistry['Excellent'] | Physics['Excellent'] | Biology['Excellent'] |  Business['Excellent'] |  Accountancy['Excellent'] |  PE['Excellent'] |  CS['Excellent'] |  History['Excellent'] |  Geography['Excellent'] |  Politics['Excellent'] |  Economy['Excellent'] |  Literature['Excellent'] |  Art['Excellent']), Researcher['Excellent'])
rule158 = ctrl.Rule(Language['Average'] & Maths['Excellent'] & (Chemistry['Good'] | Physics['Good'] | Biology['Good'] |  Business['Good'] |  Accountancy['Good'] |  PE['Good'] |  CS['Good'] |  History['Good'] |  Geography['Good'] |  Politics['Good'] |  Economy['Good'] |  Literature['Good'] |  Art['Good']), Researcher['Not_good'])
rule159 = ctrl.Rule(Language['Average'] & Maths['Excellent'] & (Chemistry['Average'] | Physics['Average'] | Biology['Average'] |  Business['Average'] |  Accountancy['Average'] |  PE['Average'] |  CS['Average'] |  History['Average'] |  Geography['Average'] |  Politics['Average'] |  Economy['Average'] |  Literature['Average'] |  Art['Average']), Researcher['Not_good'])
rule160 = ctrl.Rule(Language['Average'] & Maths['Good'] & (Chemistry['Excellent'] | Physics['Excellent'] | Biology['Excellent'] |  Business['Excellent'] |  Accountancy['Excellent'] |  PE['Excellent'] |  CS['Excellent'] |  History['Excellent'] |  Geography['Excellent'] |  Politics['Excellent'] |  Economy['Excellent'] |  Literature['Excellent'] |  Art['Excellent']), Researcher['Excellent'])
rule161 = ctrl.Rule(Language['Average'] & Maths['Good'] & (Chemistry['Good'] | Physics['Good'] |  Biology['Good'] |  Business['Good'] |  Accountancy['Good'] |  PE['Good'] |  CS['Good'] |  History['Good'] |  Geography['Good'] |  Politics['Good'] |  Economy['Good'] |  Literature['Good'] |  Art['Good']), Researcher['Not_good'])
rule162 = ctrl.Rule(Language['Average'] & Maths['Good'] & (Chemistry['Average'] | Physics['Average'] |  Biology['Average'] |  Business['Average'] |  Accountancy['Average'] |  PE['Average'] |  CS['Average'] |  History['Average'] |  Geography['Average'] |  Politics['Average'] |  Economy['Average'] |  Literature['Average'] |  Art['Average']), Researcher['Not_good'])
rule163 = ctrl.Rule(Language['Average'] & Maths['Average'] & (Chemistry['Excellent'] | Physics['Excellent'] | Biology['Excellent'] |  Business['Excellent'] |  Accountancy['Excellent'] |  PE['Excellent'] |  CS['Excellent'] |  History['Excellent'] |  Geography['Excellent'] |  Politics['Excellent'] |  Economy['Excellent'] |  Literature['Excellent'] |  Art['Excellent']), Researcher['Excellent'])
rule164 = ctrl.Rule(Language['Average'] & Maths['Average'] & (Chemistry['Good'] | Physics['Good'] |  Biology['Good'] |  Business['Good'] |  Accountancy['Good'] |  PE['Good'] |  CS['Good'] |  History['Good'] |  Geography['Good'] |  Politics['Good'] |  Economy['Good'] |  Literature['Good'] |  Art['Good']), Researcher['Not_good'])
rule165 = ctrl.Rule(Language['Average'] & Maths['Average'] & (Chemistry['Average'] | Physics['Average'] |  Biology['Average'] |  Business['Average'] |  Accountancy['Average'] |  PE['Average'] |  CS['Average'] |  History['Average'] |  Geography['Average'] |  Politics['Average'] |  Economy['Average'] |  Literature['Average'] |  Art['Average']), Researcher['Not_good'])

rule166 = ctrl.Rule(Art['Excellent'] & Maths['Excellent'], Architect['Excellent'])
rule167 = ctrl.Rule(Art['Good'] & Maths['Excellent'], Architect['Excellent'])
rule168 = ctrl.Rule(Art['Average'] & Maths['Excellent'], Architect['Good'])
rule169 = ctrl.Rule(Art['Excellent'] & Maths['Good'], Architect['Excellent'])
rule170 = ctrl.Rule(Art['Good'] & Maths['Good'], Architect['Good'])
rule171 = ctrl.Rule(Art['Average'] & Maths['Good'], Architect['Not_good'])
rule172 = ctrl.Rule(Art['Excellent'] & Maths['Average'], Architect['Good'])
rule173 = ctrl.Rule(Art['Good'] & Maths['Average'], Architect['Good'])
rule174 = ctrl.Rule(Art['Average'] & Maths['Average'], Architect['Not_good'])

rule175 = ctrl.Rule(Art['Excellent'] & Literature['Excellent'] & History['Excellent'], Artist['Excellent'])
rule176 = ctrl.Rule(Art['Excellent'] & Literature['Excellent'] & History['Good'], Artist['Excellent'])
rule177 = ctrl.Rule(Art['Excellent'] & Literature['Excellent'] & History['Average'], Artist['Excellent'])
rule178 = ctrl.Rule(Art['Excellent'] & Literature['Good'] & History['Excellent'], Artist['Excellent'])
rule179 = ctrl.Rule(Art['Excellent'] & Literature['Good'] & History['Good'], Artist['Excellent'])
rule180 = ctrl.Rule(Art['Excellent'] & Literature['Good'] & History['Average'], Artist['Excellent'])
rule181 = ctrl.Rule(Art['Excellent'] & Literature['Average'] & History['Excellent'], Artist['Good'])
rule182 = ctrl.Rule(Art['Excellent'] & Literature['Average'] & History['Good'], Artist['Good'])
rule183 = ctrl.Rule(Art['Excellent'] & Literature['Average'] & History['Average'], Artist['Good'])

rule184 = ctrl.Rule(Art['Good'] & Literature['Excellent'] & History['Excellent'], Artist['Excellent'])
rule185 = ctrl.Rule(Art['Good'] & Literature['Excellent'] & History['Good'], Artist['Good'])
rule186 = ctrl.Rule(Art['Good'] & Literature['Excellent'] & History['Average'], Artist['Good'])
rule187 = ctrl.Rule(Art['Good'] & Literature['Good'] & History['Excellent'], Artist['Good'])
rule188 = ctrl.Rule(Art['Good'] & Literature['Good'] & History['Good'], Artist['Good'])
rule189 = ctrl.Rule(Art['Good'] & Literature['Good'] & History['Average'], Artist['Good'])
rule190 = ctrl.Rule(Art['Good'] & Literature['Average'] & History['Excellent'], Artist['Good'])
rule191 = ctrl.Rule(Art['Good'] & Literature['Average'] & History['Good'], Artist['Good'])
rule192 = ctrl.Rule(Art['Good'] & Literature['Average'] & History['Average'], Artist['Good'])

rule193 = ctrl.Rule(Art['Average'] & Literature['Excellent'] & History['Excellent'], Artist['Not_good'])
rule194 = ctrl.Rule(Art['Average'] & Literature['Excellent'] & History['Good'], Artist['Not_good'])
rule195 = ctrl.Rule(Art['Average'] & Literature['Excellent'] & History['Average'], Artist['Not_good'])
rule196 = ctrl.Rule(Art['Average'] & Literature['Good'] & History['Excellent'], Artist['Not_good'])
rule197 = ctrl.Rule(Art['Average'] & Literature['Good'] & History['Good'], Artist['Not_good'])
rule198 = ctrl.Rule(Art['Average'] & Literature['Good'] & History['Average'], Artist['Not_good'])
rule199 = ctrl.Rule(Art['Average'] & Literature['Average'] & History['Excellent'], Artist['Not_good'])
rule200 = ctrl.Rule(Art['Average'] & Literature['Average'] & History['Good'], Artist['Not_good'])
rule201 = ctrl.Rule(Art['Average'] & Literature['Average'] & History['Average'], Artist['Not_good'])

rule202 = ctrl.Rule(PE['Excellent'] & Biology['Excellent'], Athlete['Excellent'])
rule203 = ctrl.Rule(PE['Excellent'] & Biology['Good'], Athlete['Excellent'])
rule204 = ctrl.Rule(PE['Excellent'] & Biology['Average'], Athlete['Excellent'])
rule205 = ctrl.Rule(PE['Average'] & Biology['Excellent'], Athlete['Not_good'])
rule206 = ctrl.Rule(PE['Average'] & Biology['Good'], Athlete['Not_good'])
rule207 = ctrl.Rule(PE['Average'] & Biology['Average'], Athlete['Not_good'])
rule208 = ctrl.Rule(PE['Good'] & Biology['Excellent'], Athlete['Good'])
rule209 = ctrl.Rule(PE['Good'] & Biology['Good'], Athlete['Good'])
rule210 = ctrl.Rule(PE['Good'] & Biology['Average'], Athlete['Good'])

rule211 = ctrl.Rule(PE['Excellent'] & Biology['Excellent'] & Physics['Excellent'], Fitness_trainer['Excellent'])
rule212 = ctrl.Rule(PE['Excellent'] & Biology['Excellent'] & Physics['Good'], Fitness_trainer['Excellent'])
rule213 = ctrl.Rule(PE['Excellent'] & Biology['Excellent'] & Physics['Average'], Fitness_trainer['Excellent'])
rule214 = ctrl.Rule(PE['Excellent'] & Biology['Good'] & Physics['Excellent'], Fitness_trainer['Excellent'])
rule215 = ctrl.Rule(PE['Excellent'] & Biology['Good'] & Physics['Good'], Fitness_trainer['Excellent'])
rule216 = ctrl.Rule(PE['Excellent'] & Biology['Good'] & Physics['Average'], Fitness_trainer['Excellent'])
rule217 = ctrl.Rule(PE['Excellent'] & Biology['Average'] & Physics['Excellent'], Fitness_trainer['Good'])
rule218 = ctrl.Rule(PE['Excellent'] & Biology['Average'] & Physics['Good'], Fitness_trainer['Good'])
rule219 = ctrl.Rule(PE['Excellent'] & Biology['Average'] & Physics['Average'], Fitness_trainer['Good'])

rule220 = ctrl.Rule(PE['Good'] & Biology['Excellent'] & Physics['Excellent'], Fitness_trainer['Excellent'])
rule221 = ctrl.Rule(PE['Good'] & Biology['Excellent'] & Physics['Good'], Fitness_trainer['Excellent'])
rule222 = ctrl.Rule(PE['Good'] & Biology['Excellent'] & Physics['Average'], Fitness_trainer['Excellent'])
rule223 = ctrl.Rule(PE['Good'] & Biology['Good'] & Physics['Excellent'], Fitness_trainer['Excellent'])
rule224 = ctrl.Rule(PE['Good'] & Biology['Good'] & Physics['Good'], Fitness_trainer['Good'])
rule225 = ctrl.Rule(PE['Good'] & Biology['Good'] & Physics['Average'], Fitness_trainer['Good'])
rule226 = ctrl.Rule(PE['Good'] & Biology['Average'] & Physics['Excellent'], Fitness_trainer['Good'])
rule227 = ctrl.Rule(PE['Good'] & Biology['Average'] & Physics['Good'], Fitness_trainer['Good'])
rule228 = ctrl.Rule(PE['Good'] & Biology['Average'] & Physics['Average'], Fitness_trainer['Good'])

rule229 = ctrl.Rule(PE['Average'] & Biology['Excellent'] & Physics['Excellent'], Fitness_trainer['Good'])
rule230 = ctrl.Rule(PE['Average'] & Biology['Excellent'] & Physics['Good'], Fitness_trainer['Good'])
rule231 = ctrl.Rule(PE['Average'] & Biology['Excellent'] & Physics['Average'], Fitness_trainer['Not_good'])
rule232 = ctrl.Rule(PE['Average'] & Biology['Good'] & Physics['Excellent'], Fitness_trainer['Not_good'])
rule233 = ctrl.Rule(PE['Average'] & Biology['Good'] & Physics['Good'], Fitness_trainer['Not_good'])
rule234 = ctrl.Rule(PE['Average'] & Biology['Good'] & Physics['Average'], Fitness_trainer['Not_good'])
rule235 = ctrl.Rule(PE['Average'] & Biology['Average'] & Physics['Excellent'], Fitness_trainer['Not_good'])
rule236 = ctrl.Rule(PE['Average'] & Biology['Average'] & Physics['Good'], Fitness_trainer['Not_good'])
rule237 = ctrl.Rule(PE['Average'] & Biology['Average'] & Physics['Average'], Fitness_trainer['Not_good'])

rule238 = ctrl.Rule(Politics['Excellent'] & Economy['Excellent'], Politician['Excellent'])
rule239 = ctrl.Rule(Politics['Excellent'] & Economy['Good'], Politician['Excellent'])
rule240 = ctrl.Rule(Politics['Excellent'] & Economy['Average'], Politician['Excellent'])
rule241 = ctrl.Rule(Politics['Average'] & Economy['Excellent'], Politician['Not_good'])
rule242 = ctrl.Rule(Politics['Average'] & Economy['Good'], Politician['Not_good'])
rule243 = ctrl.Rule(Politics['Average'] & Economy['Average'], Politician['Not_good'])
rule244 = ctrl.Rule(Politics['Good'] & Economy['Excellent'], Politician['Good'])
rule245 = ctrl.Rule(Politics['Good'] & Economy['Good'], Politician['Good'])
rule246 = ctrl.Rule(Politics['Good'] & Economy['Average'], Politician['Good'])

rule247 = ctrl.Rule(Geography['Excellent'] & History['Excellent'], Archeologist['Excellent'])
rule248 = ctrl.Rule(Geography['Excellent'] & History['Good'], Archeologist['Excellent'])
rule249 = ctrl.Rule(Geography['Excellent'] & History['Average'], Archeologist['Excellent'])
rule250 = ctrl.Rule(Geography['Average'] & History['Excellent'], Archeologist['Not_good'])
rule251 = ctrl.Rule(Geography['Average'] & History['Good'], Archeologist['Not_good'])
rule252 = ctrl.Rule(Geography['Average'] & History['Average'], Archeologist['Not_good'])
rule253 = ctrl.Rule(Geography['Good'] & History['Excellent'], Archeologist['Good'])
rule254 = ctrl.Rule(Geography['Good'] & History['Good'], Archeologist['Good'])
rule255 = ctrl.Rule(Geography['Good'] & History['Average'], Archeologist['Good'])

rule256 = ctrl.Rule(Art['Excellent'] & Language['Excellent'] & Literature['Excellent'], Poet['Excellent'])
rule257 = ctrl.Rule(Art['Excellent'] & Language['Excellent'] & Literature['Good'], Poet['Excellent'])
rule258 = ctrl.Rule(Art['Excellent'] & Language['Excellent'] & Literature['Average'], Poet['Excellent'])
rule259 = ctrl.Rule(Art['Excellent'] & Language['Good'] & Literature['Excellent'], Poet['Excellent'])
rule260 = ctrl.Rule(Art['Excellent'] & Language['Good'] & Literature['Good'], Poet['Excellent'])
rule261 = ctrl.Rule(Art['Excellent'] & Language['Good'] & Literature['Average'], Poet['Excellent'])
rule262 = ctrl.Rule(Art['Excellent'] & Language['Average'] & Literature['Excellent'], Poet['Good'])
rule263 = ctrl.Rule(Art['Excellent'] & Language['Average'] & Literature['Good'], Poet['Good'])
rule264 = ctrl.Rule(Art['Excellent'] & Language['Average'] & Literature['Average'], Poet['Good'])

rule265 = ctrl.Rule(Art['Good'] & Language['Excellent'] & Literature['Excellent'], Poet['Excellent'])
rule266 = ctrl.Rule(Art['Good'] & Language['Excellent'] & Literature['Good'], Poet['Excellent'])
rule267 = ctrl.Rule(Art['Good'] & Language['Excellent'] & Literature['Average'], Poet['Excellent'])
rule268 = ctrl.Rule(Art['Good'] & Language['Good'] & Literature['Excellent'], Poet['Excellent'])
rule269 = ctrl.Rule(Art['Good'] & Language['Good'] & Literature['Good'], Poet['Good'])
rule270 = ctrl.Rule(Art['Good'] & Language['Good'] & Literature['Average'], Poet['Good'])
rule271 = ctrl.Rule(Art['Good'] & Language['Average'] & Literature['Excellent'], Poet['Good'])
rule272 = ctrl.Rule(Art['Good'] & Language['Average'] & Literature['Good'], Poet['Good'])
rule273 = ctrl.Rule(Art['Good'] & Language['Average'] & Literature['Average'], Poet['Good'])

rule274 = ctrl.Rule(Art['Average'] & Language['Excellent'] & Literature['Excellent'], Poet['Good'])
rule275 = ctrl.Rule(Art['Average'] & Language['Excellent'] & Literature['Good'], Poet['Good'])
rule276 = ctrl.Rule(Art['Average'] & Language['Excellent'] & Literature['Average'], Poet['Not_good'])
rule277 = ctrl.Rule(Art['Average'] & Language['Good'] & Literature['Excellent'], Poet['Not_good'])
rule278 = ctrl.Rule(Art['Average'] & Language['Good'] & Literature['Good'], Poet['Not_good'])
rule279 = ctrl.Rule(Art['Average'] & Language['Good'] & Literature['Average'], Poet['Not_good'])
rule280 = ctrl.Rule(Art['Average'] & Language['Average'] & Literature['Excellent'], Poet['Not_good'])
rule281 = ctrl.Rule(Art['Average'] & Language['Average'] & Literature['Good'], Poet['Not_good'])
rule282 = ctrl.Rule(Art['Average'] & Language['Average'] & Literature['Average'], Poet['Not_good'])

rule283 = ctrl.Rule(Language['Excellent'] & Literature['Excellent'], Writer['Excellent'])
rule284 = ctrl.Rule(Language['Excellent'] & Literature['Good'], Writer['Excellent'])
rule285 = ctrl.Rule(Language['Excellent'] & Literature['Average'], Writer['Excellent'])
rule286 = ctrl.Rule(Language['Average'] & Literature['Excellent'], Writer['Not_good'])
rule287 = ctrl.Rule(Language['Average'] & Literature['Good'], Writer['Not_good'])
rule288 = ctrl.Rule(Language['Average'] & Literature['Average'], Writer['Not_good'])
rule289 = ctrl.Rule(Language['Good'] & Literature['Excellent'], Writer['Good'])
rule290 = ctrl.Rule(Language['Good'] & Literature['Good'], Writer['Good'])
rule291 = ctrl.Rule(Language['Good'] & Literature['Average'], Writer['Good'])

rule292 = ctrl.Rule(Chemistry['Excellent'] & Biology['Excellent'], chemist['Excellent'])
rule293 = ctrl.Rule(Chemistry['Excellent'] & Biology['Good'], chemist['Excellent'])
rule294 = ctrl.Rule(Chemistry['Excellent'] & Biology['Average'], chemist['Excellent'])
rule295 = ctrl.Rule(Chemistry['Average'] & Biology['Excellent'], chemist['Not_good'])
rule296 = ctrl.Rule(Chemistry['Average'] & Biology['Good'], chemist['Not_good'])
rule297 = ctrl.Rule(Chemistry['Average'] & Biology['Average'], chemist['Not_good'])
rule298 = ctrl.Rule(Chemistry['Good'] & Biology['Excellent'], chemist['Good'])
rule299 = ctrl.Rule(Chemistry['Good'] & Biology['Good'], chemist['Good'])
rule300 = ctrl.Rule(Chemistry['Good'] & Biology['Average'], chemist['Good'])

rules_Er = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27])

rules_Medi=ctrl.ControlSystem([rule28,rule29,rule30,rule31,rule32,rule33,rule34,rule35,rule36,rule37,rule38,rule39,rule40,rule41,rule42,rule43,rule44,rule45,rule46,rule47,rule48,rule49,rule50,rule51,rule52,rule53,rule54])

rules_Manag=ctrl.ControlSystem([rule55,rule56,rule57,rule58,rule59,rule60,rule61,rule62,rule63])

rules_Hos=ctrl.ControlSystem([rule64,rule65,rule66,rule67,rule68,rule69,rule70,rule71,rule72])

rules_Chief=ctrl.ControlSystem([rule73,rule74,rule75,rule76,rule77,rule78,rule79,rule80,rule81,rule82,rule83,rule84,rule85,rule86,rule87,rule88,rule89,rule90,rule91,rule92,rule93,rule94,rule95,rule96,rule97,rule98,rule99,])

rules_Work_ar=ctrl.ControlSystem([rule100,rule101,rule102,rule103,rule104,rule105,rule106,rule107,rule108,rule109,rule110,rule111,rule112,rule113,rule114,rule115,rule116,rule117,rule118,rule119,rule120,rule121,rule122,rule123,rule124,rule125,rule126,rule127,rule128,rule129])

rules_Tea=ctrl.ControlSystem([rule130,rule131,rule132,rule133,rule134,rule135,rule136,rule137,rule138])

rules_Re=ctrl.ControlSystem([rule139,rule140,rule141,rule142,rule143,rule144,rule145,rule146,rule147,rule148,rule149,rule150,rule151,rule152,rule153,rule154,rule155,rule156,rule157,rule158,rule159,rule160,rule161,rule162,rule163,rule164,rule165])

rules_Arch=ctrl.ControlSystem([rule166,rule167,rule168,rule169,rule170,rule171,rule172,rule173,rule174])

rules_Arti=ctrl.ControlSystem([rule175,rule176,rule177,rule178,rule179,rule180,rule181,rule182,rule183,rule184,rule185,rule186,rule187,rule188,rule189,rule190,rule191,rule192,rule193,rule194,rule195,rule196,rule197,rule198,rule199,rule200,rule201])

rules_Ath=ctrl.ControlSystem([rule202,rule203,rule204,rule205,rule206,rule207,rule208,rule209,rule210])

rules_Fit=ctrl.ControlSystem([rule211,rule212,rule213,rule214,rule215,rule216,rule217,rule218,rule219,rule220,rule221,rule222,rule223,rule224,rule225,rule226,rule227,rule228,rule229,rule230,rule231,rule232,rule233,rule234,rule235,rule236,rule237])

rules_Poli=ctrl.ControlSystem([rule238,rule239,rule240,rule241,rule242,rule243,rule244,rule245,rule246])

rules_Arche=ctrl.ControlSystem([rule247,rule248,rule249,rule250,rule251,rule252,rule253,rule254,rule255])

rules_Poet=ctrl.ControlSystem([rule256,rule257,rule258,rule259,rule260,rule261,rule262,rule263,rule264,rule265,rule266,rule267,rule268,rule269,rule270,rule271,rule272,rule273,rule274,rule275,rule276,rule277,rule278,rule279,rule282,rule281,rule282])

rules_Wri=ctrl.ControlSystem([rule283,rule284,rule285,rule286,rule287,rule288,rule289,rule290,rule291])

rules_Che=ctrl.ControlSystem([rule292,rule293,rule294,rule295,rule296,rule297,rule298,rule299,rule300])

system_Er = ctrl.ControlSystemSimulation(rules_Er)

system_Medi = ctrl.ControlSystemSimulation(rules_Medi)

system_Manag = ctrl.ControlSystemSimulation(rules_Manag)

system_Hos = ctrl.ControlSystemSimulation(rules_Hos)

system_Chief = ctrl.ControlSystemSimulation(rules_Chief)

system_Work_ar = ctrl.ControlSystemSimulation(rules_Work_ar)

system_Tea = ctrl.ControlSystemSimulation(rules_Tea)

system_Re = ctrl.ControlSystemSimulation(rules_Re)

system_Arch = ctrl.ControlSystemSimulation(rules_Arch)

system_Arti = ctrl.ControlSystemSimulation(rules_Arti)

system_Ath = ctrl.ControlSystemSimulation(rules_Ath)

system_Fit = ctrl.ControlSystemSimulation(rules_Fit)

system_Poli = ctrl.ControlSystemSimulation(rules_Poli)

system_Arche = ctrl.ControlSystemSimulation(rules_Arche)

system_Poet = ctrl.ControlSystemSimulation(rules_Poet)

system_Wri = ctrl.ControlSystemSimulation(rules_Wri)

system_Che = ctrl.ControlSystemSimulation(rules_Che)

print("Enter your marks in the following subjects : (enter 0 if not aplicable)\n"),

i = float(input("Physics : \n"))
system_Er.input['Physics']=i
system_Medi.input['Physics']=i
system_Work_ar.input['Physics']=i
system_Tea.input['Physics']=i
system_Re.input['Physics']=i
system_Fit.input['Physics']=i

i = float(input("Maths : \n"))
system_Er.input['Maths']= i
system_Work_ar.input['Maths']= i
system_Tea.input['Maths']= i
system_Re.input['Maths']= i
system_Arch.input['Maths']= i

i = float(input("Chemistry : \n"))
system_Er.input['Chemistry']= i
system_Medi.input['Chemistry']=i
system_Work_ar.input['Chemistry']= i
system_Tea.input['Chemistry']= i
system_Re.input['Chemistry']= i
system_Che.input['Chemistry']= i

i = float(input("Biology : \n"))
system_Medi.input['Biology']= i
system_Work_ar.input['Biology']= i
system_Tea.input['Biology']= i
system_Re.input['Biology']= i
system_Ath.input['Biology']= i
system_Fit.input['Biology']= i
system_Che.input['Biology']= i

i = float(input("Business : \n"))
system_Manag.input['Business']= i
system_Hos.input['Business']= i
system_Work_ar.input['Business']= i
system_Tea.input['Business']= i
system_Re.input['Business']= i

i = float(input("Accountancy : \n"))
system_Manag.input['Accountancy']= i
system_Work_ar.input['Accountancy']= i
system_Tea.input['Accountancy']= i
system_Re.input['Accountancy']= i

i = float(input("PE : \n"))
system_Work_ar.input['PE']= i
system_Tea.input['PE']= i
system_Re.input['PE']= i
system_Ath.input['PE']= i
system_Fit.input['PE']= i

i = float(input("CS : \n"))
system_Work_ar.input['CS']= i
system_Tea.input['CS']= i
system_Re.input['CS']= i

i = float(input("History : \n"))
system_Chief.input['History']= i
system_Work_ar.input['History']= i
system_Tea.input['History']= i
system_Re.input['History']= i
system_Arche.input['History']= i

i = float(input("Geography : \n"))
system_Work_ar.input['Geography']= i
system_Tea.input['Geography']= i
system_Re.input['Geography']= i
system_Arche.input['Geography']= i

i = float(input("Politics : \n"))
system_Work_ar.input['Politics']= i
system_Tea.input['Politics']= i
system_Re.input['Politics']= i
system_Poli.input['Politics']= i

i = float(input("Economy : \n"))
system_Work_ar.input['Economy']= i
system_Tea.input['Economy']= i
system_Re.input['Economy']= i
system_Poli.input['Economy']= i

i = float(input("Literature : \n"))
system_Work_ar.input['Literature']= i
system_Tea.input['Literature']= i
system_Re.input['Literature']= i
system_Arti.input['Literature']= i
system_Poet.input['Literature']= i
system_Wri.input['Literature']= i

i = float(input("Language (Number in any language that you preffer): \n"))
system_Hos.input['Language']= i
system_Chief.input['Language']= i
system_Work_ar.input['Language']= i
system_Tea.input['Language']= i
system_Re.input['Language']= i
system_Poet.input['Language']= i
system_Wri.input['Language']= i

i = float(input("Art : \n"))
system_Chief.input['Art']= i
system_Work_ar.input['Art']= i
system_Tea.input['Art']= i
system_Re.input['Art']= i
system_Arch.input['Art']= i
system_Arti.input['Art']= i
system_Poet.input['Art']= i

system_Er.compute()
print ("Engineering = ",system_Er.output["Engineering"])
Engineering.view(sim=system_Er)

system_Medi.compute()
print ("Medicine = ",system_Medi.output["Medicine"])
Medicine.view(sim=system_Medi)

system_Manag.compute()
print ("Management = ",system_Manag.output["Management"])
Management.view(sim=system_Manag)

system_Hos.compute()
print ("Hospitality = ",system_Hos.output["Hospitality"])
Hospitality.view(sim=system_Hos)

system_Chief.compute()
print ("Chief = ",system_Chief.output["Chief"])
Chief.view(sim=system_Chief)

system_Work_ar.compute()
print ("work_around = ",system_Work_ar.output["work_around"])
work_around.view(sim=system_Work_ar)

system_Tea.compute()
print ("Teacher = ",system_Tea.output["Teacher"])
Teacher.view(sim=system_Tea)

system_Re.compute()
print ("Researcher = ",system_Re.output["Researcher"])
Researcher.view(sim=system_Re)

system_Arch.compute()
print ("Architect = ",system_Arch.output["Architect"])
Architect.view(sim=system_Arch)

system_Arti.compute()
print ("Artist = ",system_Arti.output["Artist"])
Artist.view(sim=system_Arti)

system_Ath.compute()
print ("Athlete = ",system_Ath.output["Athlete"])
Athlete.view(sim=system_Ath)

system_Fit.compute()
print ("Fitness_trainer = ",system_Fit.output["Fitness_trainer"])
Fitness_trainer.view(sim=system_Fit)

system_Poli.compute()
print ("Politician = ",system_Poli.output["Politician"])
Politician.view(sim=system_Poli)

system_Arche.compute()
print ("Archeologist = ",system_Arche.output["Archeologist"])
Archeologist.view(sim=system_Arche)

system_Poet.compute()
print ("Poet = ",system_Poet.output["Poet"])
Poet.view(sim=system_Poet)

system_Wri.compute()
print ("Writer = ",system_Wri.output["Writer"])
Writer.view(sim=system_Wri)

system_Che.compute()
print ("chemist = ",system_Che.output["chemist"])
chemist.view(sim=system_Che)