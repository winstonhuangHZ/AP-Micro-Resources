from __future__ import annotations


def q(prompt: str, choices: list[str], answer: str, explanation: str) -> dict:
    return {
        "prompt": prompt,
        "choices": choices,
        "answer": answer,
        "explanation": explanation,
    }


def block(stimulus: str | None, questions: list[dict]) -> dict:
    return {"stimulus": stimulus, "questions": questions}


UNITS = [
    {
        "unit": 1,
        "title": "Basic Economic Concepts",
        "blocks": [
            block(
                r"""
                The following questions refer to Table 1.

                \begin{center}
                \begin{tabular}{lcc}
                \toprule
                Country & \shortstack{Hours per\\ Charger} & \shortstack{Hours per\\ Bottle} \\
                \midrule
                Alder & 2 & 6 \\
                Briar & 3 & 4 \\
                \bottomrule
                \end{tabular}
                \end{center}

                Assume each country has 240 labor hours available and constant opportunity costs.
                """,
                [
                    q(
                        r"Which of the following statements is correct?",
                        [
                            r"Alder has an absolute advantage in both goods and a comparative advantage in solar chargers.",
                            r"Briar has an absolute advantage in both goods and a comparative advantage in insulated bottles.",
                            r"Alder has an absolute advantage in solar chargers, Briar has an absolute advantage in insulated bottles, and the comparative advantages are the same as the absolute advantages.",
                            r"Briar has an absolute advantage in solar chargers, Alder has an absolute advantage in insulated bottles, and comparative advantage cannot be determined without demand data.",
                            r"Neither country has an absolute advantage, but Alder has a comparative advantage in bottles.",
                        ],
                        "C",
                        r"Alder uses fewer labor hours per charger, while Briar uses fewer labor hours per bottle. Alder gives up only $\tfrac{1}{3}$ of a bottle per charger, compared with Briar's $\tfrac{3}{4}$, so Alder has the comparative advantage in chargers and Briar in bottles.",
                    ),
                    q(
                        r"If both countries specialize according to comparative advantage, the combined output will be",
                        [
                            r"80 chargers and 40 bottles",
                            r"120 chargers and 60 bottles",
                            r"60 chargers and 120 bottles",
                            r"180 chargers and 40 bottles",
                            r"100 chargers and 80 bottles",
                        ],
                        "B",
                        r"Alder specializes in chargers and produces $240/2=120$ chargers. Briar specializes in bottles and produces $240/4=60$ bottles.",
                    ),
                    q(
                        r"Which of the following terms of trade for one solar charger would allow \emph{both} countries to gain from trade?",
                        [
                            r"$\tfrac{1}{5}$ of a bottle",
                            r"$\tfrac{1}{3}$ of a bottle",
                            r"$\tfrac{1}{2}$ of a bottle",
                            r"$\tfrac{4}{5}$ of a bottle",
                            r"1 bottle",
                        ],
                        "C",
                        r"The terms of trade must lie between the two opportunity costs of a charger: greater than Alder's $\tfrac{1}{3}$ bottle and less than Briar's $\tfrac{3}{4}$ bottle. Only $\tfrac{1}{2}$ bottle satisfies that condition.",
                    ),
                    q(
                        r"If the terms of trade are 1 charger for $\tfrac{1}{2}$ of a bottle and Alder exports 30 chargers, Alder will consume",
                        [
                            r"60 chargers and 30 bottles, which is outside Alder's PPC",
                            r"90 chargers and 15 bottles, which is better than Alder could obtain on its own",
                            r"90 chargers and 15 bottles, which is worse than Alder could obtain on its own",
                            r"105 chargers and 10 bottles, which is exactly on Alder's PPC",
                            r"120 chargers and 0 bottles, which means Alder gains nothing from trade",
                        ],
                        "B",
                        r"Alder produces 120 chargers when specializing. Exporting 30 chargers leaves 90 chargers and brings in 15 bottles. Producing 90 chargers domestically would cost Alder 30 labor hours and leave only 10 bottles, so trade lets Alder consume beyond its own PPC.",
                    ),
                    q(
                        r"Suppose Briar adopts a new technology that reduces the labor required per solar charger from 3 hours to 1.5 hours, while bottle technology is unchanged. Which of the following will occur?",
                        [
                            r"Briar gains both the absolute and comparative advantages in solar chargers.",
                            r"Briar gains the absolute advantage in solar chargers, but Alder still has the comparative advantage in solar chargers.",
                            r"Alder loses both the absolute and comparative advantages in solar chargers and bottles.",
                            r"Comparative advantage disappears because Briar can now produce chargers more efficiently in absolute terms.",
                            r"Briar gains the comparative advantage in bottles because its charger technology improved.",
                        ],
                        "B",
                        r"Briar now has the absolute advantage in chargers because 1.5 hours is less than Alder's 2 hours. But Briar's opportunity cost of a charger is $1.5/4=0.375$ bottle, still above Alder's $2/6=\tfrac{1}{3}$, so Alder keeps the comparative advantage in chargers.",
                    ),
                ],
            ),
            block(
                r"""
                The following questions refer to Table 2, which shows the daily production possibilities for drones and emergency medical kits in one economy.

                \begin{center}
                \begin{tabular}{ccc}
                \toprule
                Point & Drones & Medical Kits \\
                \midrule
                A & 0 & 300 \\
                B & 10 & 294 \\
                C & 20 & 282 \\
                D & 30 & 258 \\
                E & 40 & 216 \\
                F & 50 & 150 \\
                \bottomrule
                \end{tabular}
                \end{center}
                """,
                [
                    q(
                        r"The opportunity cost of increasing output from 20 drones to 30 drones is",
                        [
                            r"6 medical kits",
                            r"12 medical kits",
                            r"18 medical kits",
                            r"24 medical kits",
                            r"42 medical kits",
                        ],
                        "D",
                        r"Moving from point C to point D raises drone output by 10 and lowers medical kits from 282 to 258, a sacrifice of 24 kits.",
                    ),
                    q(
                        r"The data in Table 2 best illustrate",
                        [
                            r"constant opportunity costs because each additional drone costs the same number of kits",
                            r"increasing opportunity costs because the number of kits forgone rises as more drones are produced",
                            r"decreasing opportunity costs because drone specialization lowers the cost of each new drone",
                            r"absolute advantage because the economy can produce both goods at the same time",
                            r"comparative advantage because some points favor one good over the other",
                        ],
                        "B",
                        r"The losses in kits for each additional 10 drones are 6, 12, 24, 42, and 66. Because the sacrifice grows as production shifts toward drones, opportunity cost is increasing.",
                    ),
                    q(
                        r"If the economy is currently producing 20 drones and 240 medical kits, which of the following is true?",
                        [
                            r"The economy is on its PPC and productively efficient.",
                            r"The economy is inside its PPC, so it may be experiencing unemployment or inefficient resource use.",
                            r"The economy is outside its PPC, so it must be trading internationally.",
                            r"The economy is inside its PPC because opportunity costs are constant.",
                            r"The economy is on its PPC because 240 kits lies between two listed output combinations.",
                        ],
                        "B",
                        r"At 20 drones, the table shows a maximum of 282 kits. Producing only 240 kits means the economy is inside the frontier.",
                    ),
                    q(
                        r"If a new drone-specific technology raises the maximum number of drones from 50 to 70 while leaving the maximum number of medical kits at 300, the PPC will",
                        [
                            r"shift outward in a parallel way",
                            r"pivot outward on the drone axis only",
                            r"pivot inward on the medical-kit axis only",
                            r"shift inward because resources become more specialized",
                            r"become linear because technology changed only one sector",
                        ],
                        "B",
                        r"A technology improvement that affects only drone production increases the horizontal intercept while leaving the vertical intercept unchanged, so the PPC pivots outward around the medical-kit intercept.",
                    ),
                    q(
                        r"If the economy is currently at point E and policymakers require production of 10 additional drones with no technological change, the output of medical kits must fall by",
                        [
                            r"24 kits",
                            r"30 kits",
                            r"42 kits",
                            r"50 kits",
                            r"66 kits",
                        ],
                        "E",
                        r"Moving from point E to point F raises drones from 40 to 50 and lowers medical kits from 216 to 150, a decrease of 66 kits.",
                    ),
                ],
            ),
            block(
                r"""
                The following questions refer to Lina's utility schedules. Lina buys only study guides and coffee drinks and spends all of her budget on those two goods.

                \begin{center}
                \begin{tabular}{cccc}
                \toprule
                \shortstack{Study\\ Guides} & MU & \shortstack{Coffee\\ Drinks} & MU \\
                \midrule
                1 & 30 & 1 & 18 \\
                2 & 24 & 2 & 15 \\
                3 & 18 & 3 & 12 \\
                4 & 12 & 4 & 9 \\
                5 & 6 & 5 & 6 \\
                6 & 0 & 6 & 3 \\
                \bottomrule
                \end{tabular}
                \end{center}

                Each study guide costs \$6, each coffee drink costs \$3, and Lina's budget is \$24.
                """,
                [
                    q(
                        r"Which of the following bundles maximizes Lina's total utility?",
                        [
                            r"1 study guide and 6 coffee drinks",
                            r"2 study guides and 4 coffee drinks",
                            r"3 study guides and 2 coffee drinks",
                            r"4 study guides and 0 coffee drinks",
                            r"0 study guides and 8 coffee drinks",
                        ],
                        "B",
                        r"Comparing feasible bundles that use the \$24 budget, total utility is 93 for $(1,6)$, 108 for $(2,4)$, 105 for $(3,2)$, and 84 for $(4,0)$. The bundle with 2 guides and 4 coffees yields the highest total utility.",
                    ),
                    q(
                        r"Suppose Lina is currently buying 1 study guide and 6 coffee drinks. To increase total utility while staying within the same budget, she should",
                        [
                            r"buy more of both goods",
                            r"buy fewer of both goods",
                            r"buy more study guides and fewer coffee drinks",
                            r"buy fewer study guides and more coffee drinks",
                            r"keep the same bundle because the budget is fully exhausted",
                        ],
                        "C",
                        r"At that bundle, the next study guide gives 24 utils for \$6, or 4 utils per dollar. The sixth coffee gives 3 utils for \$3, or 1 util per dollar. Reallocating spending toward guides raises utility.",
                    ),
                    q(
                        r"If Lina's budget and both prices double, Lina's utility-maximizing quantities will",
                        [
                            r"double",
                            r"rise, but by less than double",
                            r"fall because the goods become more expensive",
                            r"remain unchanged",
                            r"be impossible to determine without a demand curve",
                        ],
                        "D",
                        r"When income and all prices double by the same proportion, Lina's real purchasing power and relative prices are unchanged. Her optimal quantities stay the same.",
                    ),
                    q(
                        r"If the price of coffee drinks falls from \$3 to \$2 and all marginal utilities stay the same, which of the following is most likely?",
                        [
                            r"Lina will buy fewer coffee drinks because marginal utility diminishes.",
                            r"Lina will buy more coffee drinks because their marginal utility per dollar rises.",
                            r"Lina will buy the same quantities because the utility schedules did not change.",
                            r"Lina will buy fewer study guides and fewer coffee drinks because the budget line rotates inward.",
                            r"Lina will buy more study guides because coffee is now relatively cheaper.",
                        ],
                        "B",
                        r"A lower coffee price raises the marginal utility per dollar of coffee, making coffee relatively more attractive in utility maximization. Lina will generally substitute toward coffee.",
                    ),
                    q(
                        r"The total utility Lina receives from her first 4 coffee drinks is",
                        [
                            r"18 utils",
                            r"27 utils",
                            r"36 utils",
                            r"54 utils",
                            r"60 utils",
                        ],
                        "D",
                        r"Total utility is the sum of marginal utilities: $18+15+12+9=54$ utils.",
                    ),
                ],
            ),
            block(
                None,
                [
                    q(
                        r"Which of the following is most likely to shift an economy's future PPC outward by \emph{more} than an equal increase in current consumption would?",
                        [
                            r"Using more resources today to produce consumer goods rather than capital goods",
                            r"Moving from a point on the PPC to a point inside the PPC",
                            r"Devoting more current resources to capital formation and worker training",
                            r"Imposing a binding price ceiling on capital goods",
                            r"Specializing according to current comparative advantage only",
                        ],
                        "C",
                        r"Investment in capital goods and human capital expands productive capacity in the future, shifting the PPC outward more than current consumption does.",
                    ),
                    q(
                        r"Which of the following is a positive statement rather than a normative statement?",
                        [
                            r"The government should subsidize college because education is valuable.",
                            r"A more equal income distribution is better for society than a less equal distribution.",
                            r"A binding rent ceiling creates a shortage of apartments.",
                            r"The minimum wage ought to be raised to a living wage.",
                            r"Public parks are underprovided, so the government must build more of them.",
                        ],
                        "C",
                        r"A positive statement is testable and descriptive. Whether a binding price ceiling creates a shortage is an empirical claim, not a value judgment.",
                    ),
                    q(
                        r"A government wants to rely mostly on private markets but still correct obvious market failures and provide a social safety net. Which economic system best matches that description?",
                        [
                            r"A pure command economy",
                            r"A mixed market economy",
                            r"A traditional economy",
                            r"A barter economy",
                            r"A pure laissez-faire economy with no public sector",
                        ],
                        "B",
                        r"A mixed market economy uses decentralized markets for most allocation while allowing government intervention for redistribution, externalities, and public goods.",
                    ),
                    q(
                        r"A firm paid \$500{,}000 for a nonrefundable feasibility study. The study now shows that producing the new product would add \$90{,}000 in marginal benefit and \$120{,}000 in marginal cost next year. The firm should",
                        [
                            r"produce the product because the study cost has already been incurred",
                            r"produce the product because total spending on the project exceeds \$500{,}000",
                            r"not produce the product because the additional cost exceeds the additional benefit",
                            r"not produce the product only if average cost exceeds price",
                            r"produce the product if and only if the study cost can be recovered later",
                        ],
                        "C",
                        r"The \$500{,}000 is a sunk cost and should not affect the current choice. Because marginal cost exceeds marginal benefit, the project should be rejected.",
                    ),
                    q(
                        r"""
                        A city is considering additional disaster-response drills. The marginal benefit and marginal cost of each additional drill are shown below.

                        \begin{center}
                        \begin{tabular}{ccc}
                        \toprule
                        Drill Number & Marginal Benefit & Marginal Cost \\
                        \midrule
                        1 & 18 & 5 \\
                        2 & 14 & 7 \\
                        3 & 10 & 9 \\
                        4 & 6 & 11 \\
                        5 & 2 & 13 \\
                        \bottomrule
                        \end{tabular}
                        \end{center}

                        To maximize net social benefit, the city should choose
                        """,
                        [
                            r"1 drill",
                            r"2 drills",
                            r"3 drills",
                            r"4 drills",
                            r"5 drills",
                        ],
                        "C",
                        r"The city should continue as long as marginal benefit is at least marginal cost. That is true through the third drill, but not for the fourth.",
                    ),
                ],
            ),
        ],
    },
    {
        "unit": 2,
        "title": "Supply, Demand, and Market Intervention",
        "blocks": [
            block(
                r"""
                The following questions refer to the market for reusable water bottles.

                \begin{center}
                \begin{tabular}{ccc}
                \toprule
                Price & Quantity Demanded & Quantity Supplied \\
                \midrule
                \$4 & 96 & 24 \\
                \$5 & 84 & 42 \\
                \$6 & 72 & 60 \\
                \$7 & 60 & 78 \\
                \$8 & 48 & 96 \\
                \bottomrule
                \end{tabular}
                \end{center}
                """,
                [
                    q(
                        r"In this market, the equilibrium price and quantity are",
                        [
                            r"\$5 and 42 units",
                            r"\$5 and 84 units",
                            r"\$6 and 60 units",
                            r"\$6 and 72 units",
                            r"\$7 and 78 units",
                        ],
                        "C",
                        r"Equilibrium occurs where quantity demanded equals quantity supplied. That happens at a price of \$6 and a quantity of 60 units.",
                    ),
                    q(
                        r"If the government sets a binding price ceiling of \$5, the number of units exchanged in the market will be",
                        [
                            r"24",
                            r"42",
                            r"60",
                            r"72",
                            r"84",
                        ],
                        "B",
                        r"With a binding ceiling, the quantity exchanged is limited by the short side of the market. At \$5, suppliers offer only 42 units even though consumers want 84.",
                    ),
                    q(
                        r"If the government sets a binding price floor of \$7, the market will experience",
                        [
                            r"a shortage of 18 units",
                            r"a shortage of 60 units",
                            r"a surplus of 18 units",
                            r"a surplus of 24 units",
                            r"no inefficiency because the price floor is above equilibrium",
                        ],
                        "C",
                        r"At \$7, quantity supplied is 78 while quantity demanded is 60. The excess supply is 18 units.",
                    ),
                    q(
                        r"Suppose reusable water bottles are a normal good and consumer incomes rise, while supply remains unchanged. Which of the following will occur?",
                        [
                            r"Equilibrium price will fall and equilibrium quantity will rise.",
                            r"Equilibrium price will rise and equilibrium quantity will rise.",
                            r"Equilibrium price will rise and equilibrium quantity will fall.",
                            r"Equilibrium price will be unchanged and equilibrium quantity will rise.",
                            r"Equilibrium price will be indeterminate and equilibrium quantity will rise.",
                        ],
                        "B",
                        r"A rise in income increases demand for a normal good. With supply fixed, the rightward demand shift raises both equilibrium price and equilibrium quantity.",
                    ),
                    q(
                        r"Suppose production technology improves while, at the same time, consumer income rises and the good is inferior. Which of the following is definitely true?",
                        [
                            r"Equilibrium price will rise.",
                            r"Equilibrium quantity will rise.",
                            r"Equilibrium price will fall, but equilibrium quantity will be indeterminate.",
                            r"Equilibrium quantity will fall, but equilibrium price will be indeterminate.",
                            r"Both equilibrium price and equilibrium quantity will be indeterminate.",
                        ],
                        "C",
                        r"Better technology shifts supply right, and higher income shifts demand left for an inferior good. Both shifts put downward pressure on price, so price falls for sure, but quantity depends on the relative sizes of the shifts.",
                    ),
                ],
            ),
            block(
                r"""
                The following questions refer to a ride-sharing service. At the current price, the price elasticity of demand for rides is 1.5, the cross-price elasticity of demand with bus rides is $+0.8$, and the income elasticity of demand is $+2.0$.
                """,
                [
                    q(
                        r"Based on these elasticity values, ride-sharing is best described as",
                        [
                            r"an inferior good and a complement to bus rides",
                            r"a normal luxury good and a substitute for bus rides",
                            r"a necessity and a complement to bus rides",
                            r"a normal necessity good and an unrelated good with respect to bus rides",
                            r"an inferior good and a substitute for bus rides",
                        ],
                        "B",
                        r"A positive income elasticity means the service is normal, and a value greater than 1 indicates a luxury. A positive cross-price elasticity means bus rides and ride-sharing are substitutes.",
                    ),
                    q(
                        r"If the firm raises the price of rides by 10\%, total revenue from rides will most likely",
                        [
                            r"increase by 15\%",
                            r"increase because demand is elastic",
                            r"decrease because demand is elastic",
                            r"remain unchanged because elasticity is constant",
                            r"decrease only if supply is perfectly elastic",
                        ],
                        "C",
                        r"When demand is elastic, a higher price causes quantity demanded to fall proportionally more than price rises, so total revenue falls.",
                    ),
                    q(
                        r"If bus fares fall by 5\%, the quantity demanded of ride-sharing services will most likely",
                        [
                            r"rise by 4\%",
                            r"fall by 4\%",
                            r"rise by 10\%",
                            r"fall by 10\%",
                            r"remain unchanged because cross elasticity applies only to complements",
                        ],
                        "B",
                        r"A cross-price elasticity of $+0.8$ means the percentage change in ride-sharing demand equals $0.8$ times the percentage change in bus fares. A 5\% fall in bus fares therefore lowers ride-sharing demand by 4\%.",
                    ),
                    q(
                        r"If household income falls by 3\%, the quantity demanded of ride-sharing services will most likely",
                        [
                            r"rise by 6\%",
                            r"fall by 6\%",
                            r"fall by 3\%",
                            r"rise by 3\%",
                            r"remain unchanged because the good is a luxury",
                        ],
                        "B",
                        r"With an income elasticity of $+2.0$, demand changes by twice the percentage change in income in the same direction. A 3\% fall in income lowers quantity demanded by 6\%.",
                    ),
                    q(
                        r"If the demand for a product is less elastic than its supply, a per-unit excise tax on the product will be borne mostly by",
                        [
                            r"consumers, because the side of the market that is less responsive to price bears more of the tax",
                            r"producers, because they remit the tax to the government",
                            r"consumers and producers equally, because tax incidence is legally fixed",
                            r"the government, because quantity traded falls",
                            r"foreign producers, because imports absorb the tax",
                        ],
                        "A",
                        r"Tax incidence depends on relative elasticities, not on statutory assignment. The less elastic side of the market bears the larger share of the tax burden.",
                    ),
                ],
            ),
            block(
                r"""
                The following questions refer to a market with demand curve $P = 30 - 0.5Q$ and supply curve $P = 6 + 0.25Q$, where $P$ is price and $Q$ is quantity.
                """,
                [
                    q(
                        r"In equilibrium, the price and quantity are",
                        [
                            r"\$12 and 24 units",
                            r"\$14 and 32 units",
                            r"\$16 and 28 units",
                            r"\$18 and 24 units",
                            r"\$20 and 20 units",
                        ],
                        "B",
                        r"Set demand equal to supply: $30-0.5Q = 6+0.25Q$. Solving gives $Q=32$ and $P=14$.",
                    ),
                    q(
                        r"At the free-market equilibrium, consumer surplus is",
                        [
                            r"\$128",
                            r"\$192",
                            r"\$224",
                            r"\$256",
                            r"\$288",
                        ],
                        "D",
                        r"The demand intercept is \$30, so consumer surplus is $\tfrac{1}{2}(30-14)(32)=256$.",
                    ),
                    q(
                        r"If the government imposes a \$3 per-unit tax on sellers, the price paid by consumers will become",
                        [
                            r"\$13",
                            r"\$14",
                            r"\$15",
                            r"\$16",
                            r"\$17",
                        ],
                        "D",
                        r"The tax shifts supply up to $P = 9 + 0.25Q$. Setting this equal to demand gives $30 - 0.5Q = 9 + 0.25Q$, so $Q=28$ and the consumer price is \$16.",
                    ),
                    q(
                        r"With the \$3 per-unit tax in place, total tax revenue will be",
                        [
                            r"\$72",
                            r"\$84",
                            r"\$96",
                            r"\$112",
                            r"\$128",
                        ],
                        "B",
                        r"After the tax, 28 units are sold. Tax revenue equals \$3 times 28, which is \$84.",
                    ),
                    q(
                        r"The deadweight loss created by the \$3 per-unit tax is",
                        [
                            r"\$4",
                            r"\$6",
                            r"\$8",
                            r"\$12",
                            r"\$16",
                        ],
                        "B",
                        r"The tax reduces quantity from 32 to 28, so the lost trades equal 4 units. Deadweight loss is $\tfrac{1}{2}(3)(4)=6$.",
                    ),
                ],
            ),
            block(
                r"""
                The following questions refer to a country that can trade coffee beans in the world market. Domestic demand is $Q_d = 120 - 2P$, domestic supply is $Q_s = 20 + 2P$, and the world price is \$15.
                """,
                [
                    q(
                        r"At the world price, the country will",
                        [
                            r"export 20 units",
                            r"export 40 units",
                            r"import 20 units",
                            r"import 40 units",
                            r"neither import nor export",
                        ],
                        "D",
                        r"At \$15, domestic quantity demanded is $120-2(15)=90$ and domestic quantity supplied is $20+2(15)=50$. Imports are therefore 40 units.",
                    ),
                    q(
                        r"Relative to autarky, opening trade at the world price of \$15 will",
                        [
                            r"benefit producers and harm consumers",
                            r"benefit consumers and harm producers",
                            r"benefit both consumers and producers",
                            r"harm both consumers and producers",
                            r"leave domestic welfare unchanged because the market clears either way",
                        ],
                        "B",
                        r"The autarky price is where $120-2P = 20+2P$, which gives \$25. The world price is lower, so consumers gain from cheaper coffee and producers lose from the lower domestic price.",
                    ),
                    q(
                        r"If the government imposes a \$5 tariff on imported coffee beans, the new domestic price will be",
                        [
                            r"\$15",
                            r"\$18",
                            r"\$20",
                            r"\$25",
                            r"\$30",
                        ],
                        "C",
                        r"A small-country tariff raises the domestic price to the world price plus the tariff, so the new domestic price is \$20.",
                    ),
                    q(
                        r"With the \$5 tariff in place, tariff revenue will equal",
                        [
                            r"\$50",
                            r"\$100",
                            r"\$150",
                            r"\$200",
                            r"\$250",
                        ],
                        "B",
                        r"At a domestic price of \$20, quantity demanded is 80 and quantity supplied is 60, so imports are 20 units. Tariff revenue is \$5 times 20, or \$100.",
                    ),
                    q(
                        r"If the government replaced the tariff with an import quota of 20 units and all else remained the same, the domestic price would most likely",
                        [
                            r"remain at \$15 because quotas do not affect price",
                            r"fall below \$15 because imports are restricted",
                            r"rise to \$20 because the quota matches the post-tariff import quantity",
                            r"rise to \$25 because the quota recreates autarky",
                            r"be indeterminate because quotas affect only quantity",
                        ],
                        "C",
                        r"A quota of 20 imports forces the same import quantity as the tariff case. The domestic price must therefore rise to the level at which domestic demand exceeds domestic supply by 20 units, which is \$20.",
                    ),
                ],
            ),
        ],
    },
    {
        "unit": 3,
        "title": "Production, Cost, and Perfect Competition",
        "blocks": [
            block(
                r"""
                The following questions refer to a firm's short-run production data. Labor is the only variable input, each worker is paid \$36 per day, and fixed cost is \$60.

                \begin{center}
                \begin{tabular}{cc}
                \toprule
                Workers & Total Product \\
                \midrule
                0 & 0 \\
                1 & 18 \\
                2 & 34 \\
                3 & 48 \\
                4 & 58 \\
                5 & 64 \\
                6 & 66 \\
                \bottomrule
                \end{tabular}
                \end{center}
                """,
                [
                    q(
                        r"The marginal product of the fourth worker is",
                        [
                            r"6 units",
                            r"10 units",
                            r"12 units",
                            r"14 units",
                            r"18 units",
                        ],
                        "B",
                        r"Marginal product is the change in total product. The fourth worker raises output from 48 to 58, so marginal product is 10 units.",
                    ),
                    q(
                        r"The law of diminishing marginal returns first appears when the firm hires the",
                        [
                            r"second worker",
                            r"third worker",
                            r"fourth worker",
                            r"fifth worker",
                            r"sixth worker",
                        ],
                        "A",
                        r"Marginal product falls from 18 for the first worker to 16 for the second worker, so diminishing marginal returns begin with the second worker.",
                    ),
                    q(
                        r"If the firm hires 5 workers, total variable cost will equal",
                        [
                            r"\$96",
                            r"\$144",
                            r"\$180",
                            r"\$240",
                            r"\$300",
                        ],
                        "C",
                        r"Variable cost is the wage times the number of workers. With 5 workers at \$36 each, total variable cost is \$180.",
                    ),
                    q(
                        r"When output is 48 units, the firm's average fixed cost is",
                        [
                            r"\$0.75",
                            r"\$1.00",
                            r"\$1.25",
                            r"\$1.50",
                            r"\$2.00",
                        ],
                        "C",
                        r"Average fixed cost equals fixed cost divided by output. At 48 units, AFC is \$60/48 = \$1.25.",
                    ),
                    q(
                        r"The marginal cost of increasing output from 48 units to 58 units is",
                        [
                            r"\$2.40 per unit",
                            r"\$3.60 per unit",
                            r"\$6.00 per unit",
                            r"\$10.00 per unit",
                            r"\$36.00 per unit",
                        ],
                        "B",
                        r"To raise output from 48 to 58, the firm must hire the fourth worker for \$36 and gains 10 units of output. Marginal cost is therefore \$36/10 = \$3.60 per unit.",
                    ),
                ],
            ),
            block(
                r"""
                The following questions refer to a perfectly competitive firm with the total cost schedule below.

                \begin{center}
                \begin{tabular}{cc}
                \toprule
                Output & Total Cost \\
                \midrule
                0 & 30 \\
                1 & 42 \\
                2 & 50 \\
                3 & 58 \\
                4 & 70 \\
                5 & 88 \\
                6 & 114 \\
                \bottomrule
                \end{tabular}
                \end{center}

                Assume the market price is initially \$18 per unit.
                """,
                [
                    q(
                        r"The profit-maximizing output for this firm is",
                        [
                            r"3 units",
                            r"4 units",
                            r"5 units",
                            r"6 units",
                            r"the firm should shut down",
                        ],
                        "C",
                        r"The marginal costs are 12, 8, 8, 12, 18, and 26. The firm produces where price equals marginal cost on the upward-sloping portion of MC, which is 5 units when price is \$18.",
                    ),
                    q(
                        r"At the profit-maximizing output, the firm's economic profit is",
                        [
                            r"\$0",
                            r"\$2",
                            r"\$10",
                            r"\$18",
                            r"\$20",
                        ],
                        "B",
                        r"At 5 units, total revenue is \$18 times 5, or \$90. Total cost is \$88, so economic profit is \$2.",
                    ),
                    q(
                        r"The firm's shutdown price is closest to",
                        [
                            r"\$8.00",
                            r"\$9.33",
                            r"\$10.00",
                            r"\$12.00",
                            r"\$14.67",
                        ],
                        "B",
                        r"The shutdown price is the minimum AVC. Variable costs are 12, 20, 28, 40, 58, and 84, so AVC values are 12, 10, 9.33, 10, 11.6, and 14. The minimum is about \$9.33.",
                    ),
                    q(
                        r"If the firm's fixed cost rises from \$30 to \$40, while market price remains \$18, the profit-maximizing output in the short run will",
                        [
                            r"fall to 4 units",
                            r"fall to 3 units",
                            r"remain at 5 units",
                            r"rise to 6 units",
                            r"fall to 0 because economic profit becomes negative",
                        ],
                        "C",
                        r"A change in fixed cost does not change marginal cost, so the MR=MC output rule is unchanged in the short run.",
                    ),
                    q(
                        r"If the market price falls to \$10 per unit, the firm should",
                        [
                            r"shut down immediately because price is below average total cost",
                            r"produce 2 units because price equals average variable cost there",
                            r"produce 3 units because that is the highest output for which price still covers AVC and is near MC",
                            r"produce 4 units because price is below marginal cost there",
                            r"continue to produce 5 units to spread fixed cost over more output",
                        ],
                        "C",
                        r"At a price of \$10, the firm should still produce as long as price covers AVC. The closest MR=MC rule is 3 units: price exceeds the third unit's MC of 8 but is below the fourth unit's MC of 12.",
                    ),
                ],
            ),
            block(
                None,
                [
                    q(
                        r"A constant-cost perfectly competitive industry is in long-run equilibrium. If market demand increases, which of the following will occur in the long run?",
                        [
                            r"Price will remain above the original level and the number of firms will fall.",
                            r"Price will return to the original level and total industry output will increase.",
                            r"Price will remain above the original level and economic profit will remain positive.",
                            r"Each firm's demand curve will shift rightward permanently.",
                            r"The market will fail to return to zero economic profit.",
                        ],
                        "B",
                        r"In a constant-cost industry, entry shifts supply right until price returns to the original minimum-ATC level. Industry output rises, but long-run price returns to where firms earn zero economic profit.",
                    ),
                    q(
                        r"A perfectly competitive firm is allocatively efficient when",
                        [
                            r"average total cost is minimized",
                            r"price is greater than average total cost",
                            r"price equals marginal cost",
                            r"marginal revenue equals average variable cost",
                            r"total revenue equals total cost",
                        ],
                        "C",
                        r"Allocative efficiency occurs where the value to consumers, measured by price, equals the marginal cost of the last unit produced.",
                    ),
                    q(
                        r"A perfectly competitive firm is productively efficient in the long run when",
                        [
                            r"it produces where marginal revenue exceeds marginal cost",
                            r"it produces where average variable cost is maximized",
                            r"it produces where average total cost is minimized",
                            r"it produces where total revenue is maximized",
                            r"it produces where price exceeds marginal cost",
                        ],
                        "C",
                        r"Productive efficiency means producing at the lowest possible average total cost, which is the minimum point of the ATC curve.",
                    ),
                    q(
                        r"If a perfectly competitive market is currently experiencing economic losses for typical firms, the long-run adjustment will most likely involve",
                        [
                            r"entry of new firms and a lower market price",
                            r"exit of firms and a higher market price",
                            r"entry of new firms and a higher market price",
                            r"exit of firms and a lower market price",
                            r"no change, because perfectly competitive firms are price takers",
                        ],
                        "B",
                        r"Losses cause firms to exit. Market supply shifts left, raising price until the remaining firms again earn zero economic profit.",
                    ),
                    q(
                        r"Which of the following is true of the demand curve facing a single perfectly competitive firm?",
                        [
                            r"It slopes downward because the firm must lower price to sell more.",
                            r"It is perfectly inelastic because the firm is small relative to the market.",
                            r"It is perfectly elastic at the market price because the firm is a price taker.",
                            r"It is the same as the market demand curve because the product is homogeneous.",
                            r"It lies below the firm's marginal revenue curve.",
                        ],
                        "C",
                        r"A single competitive firm can sell as much as it wants at the market price, but nothing at a higher price, so its demand curve is horizontal.",
                    ),
                ],
            ),
            block(
                None,
                [
                    q(
                        r"A perfectly competitive firm is earning zero economic profit. If market demand for the product increases unexpectedly, the firm will most likely earn",
                        [
                            r"positive economic profit in the short run and zero economic profit again in the long run",
                            r"positive economic profit in both the short run and the long run",
                            r"zero economic profit in the short run and negative economic profit in the long run",
                            r"negative economic profit in the short run because cost curves do not shift immediately",
                            r"zero economic profit in both the short run and the long run because firms are price takers",
                        ],
                        "A",
                        r"Higher market demand raises price in the short run, giving firms positive profit. Entry then drives price back down until long-run profit returns to zero.",
                    ),
                    q(
                        r"If a competitive industry is an increasing-cost industry, a permanent increase in market demand will most likely cause the long-run equilibrium price to",
                        [
                            r"fall below the original price",
                            r"remain equal to the original price",
                            r"rise above the original price",
                            r"be indeterminate",
                            r"rise in the short run and then return below the original price",
                        ],
                        "C",
                        r"In an increasing-cost industry, expansion raises input prices and shifts firms' cost curves upward, so the new long-run equilibrium price is higher than before.",
                    ),
                    q(
                        r"In the short run, a competitive firm should continue to produce even while earning losses if",
                        [
                            r"price is greater than or equal to average variable cost",
                            r"price is greater than or equal to average total cost",
                            r"marginal revenue is less than marginal cost",
                            r"fixed cost is zero",
                            r"economic profit is positive",
                        ],
                        "A",
                        r"As long as price covers average variable cost, the firm can pay its variable inputs and contribute something toward fixed cost, making continued production better than shutting down.",
                    ),
                    q(
                        r"If worker training raises the marginal product of labor for every worker in a perfectly competitive firm, then all else equal the firm's",
                        [
                            r"marginal cost curve will shift upward",
                            r"marginal cost curve will shift downward",
                            r"demand curve will shift upward",
                            r"average fixed cost will rise",
                            r"shutdown price will necessarily rise",
                        ],
                        "B",
                        r"When labor becomes more productive, each unit of output requires less variable input, so marginal cost falls and the MC curve shifts downward.",
                    ),
                    q(
                        r"A per-unit tax imposed on every firm in a constant-cost perfectly competitive industry will, in the long run, most likely",
                        [
                            r"leave the market price unchanged because firms are price takers",
                            r"raise the market price by less than the tax and leave firms with losses forever",
                            r"raise the market price enough to restore zero economic profit for firms",
                            r"lower market price because industry supply becomes more elastic",
                            r"cause firms to collude to offset the tax",
                        ],
                        "C",
                        r"If all firms face higher per-unit costs, some firms exit until price rises enough for the remaining firms to earn normal profit again. In long-run competitive equilibrium, persistent losses cannot remain.",
                    ),
                ],
            ),
        ],
    },
    {
        "unit": 4,
        "title": "Imperfect Competition",
        "blocks": [
            block(
                r"""
                The following questions refer to a single-price monopolist facing demand curve $P = 50 - Q$, marginal revenue curve $MR = 50 - 2Q$, constant marginal cost $MC = 10$, and constant average total cost $ATC = 18$.
                """,
                [
                    q(
                        r"The monopolist's profit-maximizing quantity is",
                        [
                            r"10 units",
                            r"20 units",
                            r"25 units",
                            r"30 units",
                            r"40 units",
                        ],
                        "B",
                        r"The monopolist chooses output where $MR=MC$. Setting $50-2Q = 10$ gives $Q=20$.",
                    ),
                    q(
                        r"The profit-maximizing price charged by the monopolist is",
                        [
                            r"\$18",
                            r"\$20",
                            r"\$25",
                            r"\$30",
                            r"\$40",
                        ],
                        "D",
                        r"At the profit-maximizing quantity of 20, the demand curve gives the price: $P = 50 - 20 = 30$.",
                    ),
                    q(
                        r"The monopolist's economic profit is",
                        [
                            r"\$120",
                            r"\$200",
                            r"\$240",
                            r"\$360",
                            r"\$400",
                        ],
                        "C",
                        r"Profit equals $(P-ATC)\times Q = (30-18)\times 20 = 240$.",
                    ),
                    q(
                        r"The allocatively efficient quantity in this market is",
                        [
                            r"20 units",
                            r"25 units",
                            r"30 units",
                            r"40 units",
                            r"50 units",
                        ],
                        "D",
                        r"Allocative efficiency occurs where price equals marginal cost. Setting $50-Q = 10$ gives $Q=40$.",
                    ),
                    q(
                        r"If technological improvement lowers marginal cost from 10 to 6, the monopolist will",
                        [
                            r"lower price and lower output",
                            r"raise price and raise output",
                            r"lower price and raise output",
                            r"leave price unchanged and raise output",
                            r"leave output unchanged and lower price",
                        ],
                        "C",
                        r"Lower marginal cost shifts the MC curve down, so the profit-maximizing output rises and the monopoly price falls along the demand curve.",
                    ),
                ],
            ),
            block(
                r"""
                Continue to assume the market demand is $P = 50 - Q$ and marginal cost is constant at \$10.
                """,
                [
                    q(
                        r"If the monopolist can perfectly price discriminate, the profit-maximizing quantity becomes",
                        [
                            r"20 units",
                            r"25 units",
                            r"30 units",
                            r"40 units",
                            r"50 units",
                        ],
                        "D",
                        r"A perfectly price-discriminating monopolist expands output until price equals marginal cost, so it produces the allocatively efficient quantity of 40 units.",
                    ),
                    q(
                        r"Compared with the single-price monopoly outcome, perfect price discrimination will",
                        [
                            r"reduce output and increase deadweight loss",
                            r"increase output and eliminate deadweight loss",
                            r"leave output unchanged and transfer producer surplus to consumers",
                            r"lower output and eliminate consumer surplus",
                            r"raise price for every unit sold",
                        ],
                        "B",
                        r"Perfect price discrimination makes the firm sell every unit for which willingness to pay exceeds marginal cost, so quantity rises from 20 to 40 and deadweight loss disappears.",
                    ),
                    q(
                        r"Under perfect price discrimination in this market, consumer surplus will be",
                        [
                            r"zero because the monopolist captures all willingness to pay above marginal cost",
                            r"positive because quantity rises to the efficient level",
                            r"equal to producer surplus by symmetry",
                            r"larger than under single-price monopoly",
                            r"negative because each consumer pays a different price",
                        ],
                        "A",
                        r"A perfectly discriminating monopolist charges each buyer exactly their willingness to pay, capturing the entire surplus for itself.",
                    ),
                    q(
                        r"A movie theater charges students a lower ticket price than business travelers for the same film. This pricing policy is most likely based on the fact that",
                        [
                            r"students have more inelastic demand than business travelers",
                            r"business travelers have more elastic demand than students",
                            r"students generally have more elastic demand than business travelers",
                            r"marginal cost of serving students is lower",
                            r"students create larger positive externalities",
                        ],
                        "C",
                        r"A seller practicing third-degree price discrimination charges a lower price in the market segment with more elastic demand. Students are typically more price sensitive than business travelers.",
                    ),
                    q(
                        r"Successful price discrimination generally requires all of the following EXCEPT",
                        [
                            r"some degree of market power",
                            r"the ability to sort consumers into groups with different elasticities",
                            r"the ability to prevent or limit resale",
                            r"identical willingness to pay across all consumers",
                            r"knowledge about demand differences across groups",
                        ],
                        "D",
                        r"Price discrimination relies on differences in willingness to pay or elasticity. If all consumers were identical, there would be no gain from charging different prices.",
                    ),
                ],
            ),
            block(
                None,
                [
                    q(
                        r"Monopolistic competition is similar to perfect competition because both market structures have",
                        [
                            r"homogeneous products and significant barriers to entry",
                            r"a downward-sloping demand curve for each firm",
                            r"many firms and relatively free entry",
                            r"mutual interdependence and strategic pricing",
                            r"long-run prices above marginal cost",
                        ],
                        "C",
                        r"Both monopolistic competition and perfect competition feature many firms and low barriers to entry, even though firms in monopolistic competition sell differentiated products.",
                    ),
                    q(
                        r"Monopolistic competition is similar to monopoly because firms in both market structures",
                        [
                            r"face a downward-sloping demand curve for their own product",
                            r"have no close substitutes for their products",
                            r"earn positive economic profit in the long run",
                            r"produce where price equals marginal cost",
                            r"face substantial legal barriers to entry",
                        ],
                        "A",
                        r"Because products are differentiated, a monopolistically competitive firm has some market power and therefore faces a downward-sloping demand curve, like a monopoly.",
                    ),
                    q(
                        r"If a monopolistically competitive firm is earning positive economic profit in the short run, the most likely long-run adjustment is that",
                        [
                            r"its demand curve will shift right as brand loyalty rises",
                            r"new firms will enter and its demand curve will shift left",
                            r"existing firms will collude and reduce output",
                            r"its marginal cost curve will shift upward until profit is zero",
                            r"government will regulate price to average total cost",
                        ],
                        "B",
                        r"Positive profit attracts entry of close substitutes. That reduces demand for the original firm's product and shifts its demand curve left until economic profit is driven to zero.",
                    ),
                    q(
                        r"In long-run equilibrium, a monopolistically competitive firm typically operates",
                        [
                            r"at the minimum point of ATC and is productively efficient",
                            r"where price equals marginal cost and is allocatively efficient",
                            r"with excess capacity and output less than the quantity that minimizes ATC",
                            r"where marginal revenue exceeds marginal cost",
                            r"with a perfectly elastic demand curve",
                        ],
                        "C",
                        r"In long-run monopolistic competition, the demand curve is tangent to ATC at an output smaller than the minimum-ATC quantity. The firm therefore has excess capacity and is not productively efficient.",
                    ),
                    q(
                        r"If advertising makes consumers view a firm's product as more differentiated, the firm's demand for its product will most likely become",
                        [
                            r"more elastic, reducing the firm's pricing power",
                            r"less elastic, increasing the firm's pricing power",
                            r"perfectly elastic, making the market more competitive",
                            r"perfectly inelastic, allowing unlimited price increases",
                            r"horizontal because more consumers know about the product",
                        ],
                        "B",
                        r"Greater differentiation reduces the closeness of substitutes and makes consumers less price responsive, giving the firm more pricing power.",
                    ),
                ],
            ),
            block(
                r"""
                The following questions refer to the payoff matrix below for two firms in an oligopoly, ColaCo and FizzCo. Each firm chooses either a High Price or a Low Price. Payoffs are in millions of dollars.

                \begin{center}
                \begin{tabular}{lcc}
                \toprule
                & FizzCo: High Price & FizzCo: Low Price \\
                \midrule
                ColaCo: High Price & (12,\ 12) & (4,\ 16) \\
                ColaCo: Low Price & (16,\ 4) & (8,\ 8) \\
                \bottomrule
                \end{tabular}
                \end{center}
                """,
                [
                    q(
                        r"ColaCo's dominant strategy is to",
                        [
                            r"choose High Price because 12 is greater than 8",
                            r"choose High Price because collusion is more profitable",
                            r"choose Low Price because it yields a higher payoff regardless of FizzCo's action",
                            r"mix randomly between High Price and Low Price",
                            r"there is no dominant strategy for ColaCo",
                        ],
                        "C",
                        r"If FizzCo chooses High Price, ColaCo earns 16 by choosing Low Price instead of 12. If FizzCo chooses Low Price, ColaCo earns 8 by choosing Low Price instead of 4. So Low Price is dominant.",
                    ),
                    q(
                        r"The one-shot Nash equilibrium of this game is",
                        [
                            r"(High Price, High Price)",
                            r"(High Price, Low Price)",
                            r"(Low Price, High Price)",
                            r"(Low Price, Low Price)",
                            r"there is no Nash equilibrium",
                        ],
                        "D",
                        r"Because Low Price is the dominant strategy for both firms, the Nash equilibrium is for both to choose Low Price and earn 8 each.",
                    ),
                    q(
                        r"If the two firms could successfully collude and enforce the agreement, they would jointly choose",
                        [
                            r"(High Price, High Price) because joint profit is highest there",
                            r"(Low Price, Low Price) because it is the Nash equilibrium",
                            r"(Low Price, High Price) because total profit is 20",
                            r"(High Price, Low Price) because total profit is 20",
                            r"one firm would choose High Price and the other Low Price to maximize industry output",
                        ],
                        "A",
                        r"Collusion seeks to maximize joint profit. Total profit is 24 at (High Price, High Price), which exceeds the 16 total at (Low Price, Low Price).",
                    ),
                    q(
                        r"Why is collusion difficult to maintain in this oligopoly?",
                        [
                            r"Because each firm can raise joint profit by cutting price when the other keeps price high",
                            r"Because the low-price strategy is illegal in oligopoly markets",
                            r"Because firms in oligopoly face perfectly elastic demand curves",
                            r"Because high price is a dominated strategy for both firms",
                            r"Because consumers can force the collusive outcome through arbitrage",
                        ],
                        "A",
                        r"If one firm expects the other to keep a high price, it can increase its own payoff from 12 to 16 by cutting price. That incentive to cheat destabilizes collusion.",
                    ),
                    q(
                        r"If government antitrust enforcement prevents explicit communication between the firms, the most likely outcome is that the market will",
                        [
                            r"move toward the low-price Nash equilibrium",
                            r"guarantee the collusive outcome",
                            r"become perfectly competitive overnight",
                            r"eliminate strategic interdependence",
                            r"force each firm to price at marginal cost",
                        ],
                        "A",
                        r"Without enforceable collusion, each firm has an incentive to follow its dominant strategy. The likely result is the noncooperative low-price equilibrium.",
                    ),
                ],
            ),
        ],
    },
    {
        "unit": 5,
        "title": "Factor Markets",
        "blocks": [
            block(
                r"""
                The following questions refer to a perfectly competitive firm that sells its output for \$12 per unit. The only variable input is labor, and the wage rate is initially \$60 per worker per day.

                \begin{center}
                \begin{tabular}{cc}
                \toprule
                Workers & Total Output \\
                \midrule
                0 & 0 \\
                1 & 10 \\
                2 & 18 \\
                3 & 24 \\
                4 & 28 \\
                5 & 30 \\
                \bottomrule
                \end{tabular}
                \end{center}
                """,
                [
                    q(
                        r"The marginal revenue product of the third worker is",
                        [
                            r"\$48",
                            r"\$60",
                            r"\$72",
                            r"\$84",
                            r"\$96",
                        ],
                        "C",
                        r"The third worker adds 6 units of output, and each unit sells for \$12. The worker's marginal revenue product is therefore \$72.",
                    ),
                    q(
                        r"At the wage of \$60, the profit-maximizing number of workers hired is",
                        [
                            r"1",
                            r"2",
                            r"3",
                            r"4",
                            r"5",
                        ],
                        "C",
                        r"The workers' MRPs are \$120, \$96, \$72, \$48, and \$24. The firm hires labor up to the point where MRP is at least the wage, so it hires 3 workers.",
                    ),
                    q(
                        r"If the market price of output rises from \$12 to \$15, the firm's demand for labor will",
                        [
                            r"shift left because labor is now more expensive",
                            r"shift right because each worker's marginal revenue product rises",
                            r"remain unchanged because the wage did not change",
                            r"become perfectly elastic",
                            r"shift left because diminishing returns set in sooner",
                        ],
                        "B",
                        r"A higher output price raises the marginal revenue product of each worker, shifting the firm's labor demand curve to the right.",
                    ),
                    q(
                        r"If the wage falls from \$60 to \$45 while output price remains \$12, the firm will hire",
                        [
                            r"2 workers",
                            r"3 workers",
                            r"4 workers",
                            r"5 workers",
                            r"the same number of workers because labor demand depends only on product price",
                        ],
                        "C",
                        r"With a wage of \$45, the firm hires labor up to the point where MRP is at least \$45. The fourth worker's MRP is \$48, while the fifth worker's is \$24, so the firm hires 4 workers.",
                    ),
                    q(
                        r"The firm's labor demand curve slopes downward primarily because of",
                        [
                            r"the law of diminishing marginal utility",
                            r"the law of diminishing marginal product",
                            r"the free-rider problem",
                            r"price discrimination",
                            r"economies of scale",
                        ],
                        "B",
                        r"As more workers are hired with other inputs fixed, each additional worker tends to add less output. This causes marginal revenue product to fall and gives labor demand a downward slope.",
                    ),
                ],
            ),
            block(
                r"""
                A bakery uses labor and ovens. At the current combination of inputs, the marginal product of labor is 24 loaves, the marginal product of ovens is 36 loaves, the wage is \$12, and the rental rate of an oven is \$18. The bakery sells bread in a perfectly competitive market for \$4 per loaf.
                """,
                [
                    q(
                        r"At the current combination of inputs, the bakery is",
                        [
                            r"using too much labor and too few ovens",
                            r"using too few labor hours and too many ovens",
                            r"using a cost-minimizing combination of labor and ovens",
                            r"using an allocatively inefficient combination of inputs because output price exceeds wage",
                            r"unable to determine whether the mix is cost-minimizing without total cost data",
                        ],
                        "C",
                        r"Cost minimization requires $MP_L/w = MP_K/r$. Here $24/12 = 2$ and $36/18 = 2$, so the current combination is cost minimizing.",
                    ),
                    q(
                        r"If the wage rises to \$16 while all else remains the same, to restore least-cost production the bakery should",
                        [
                            r"use more labor and fewer ovens",
                            r"use fewer labor hours and more ovens",
                            r"use more of both inputs",
                            r"use less of both inputs",
                            r"make no change because only relative productivity matters",
                        ],
                        "B",
                        r"When the wage rises, $MP_L/w$ falls below $MP_K/r$. The bakery should substitute away from labor and toward ovens.",
                    ),
                    q(
                        r"If the marginal product of ovens rises from 36 to 54 while input prices are unchanged, the bakery should",
                        [
                            r"use more labor and fewer ovens",
                            r"use fewer labor hours and more ovens",
                            r"use less of both inputs",
                            r"make no change because the firm is already cost minimizing",
                            r"raise output price to restore equality between the two ratios",
                        ],
                        "B",
                        r"An increase in $MP_K$ raises $MP_K/r$ above $MP_L/w$, so the bakery can lower cost by using more ovens and less labor until the ratios are equal again.",
                    ),
                    q(
                        r"If the price of bread falls from \$4 to \$3, the bakery's least-cost combination of labor and ovens will",
                        [
                            r"shift toward labor because labor is cheaper than ovens",
                            r"shift toward ovens because marginal revenue product falls",
                            r"remain unchanged because least-cost input choice depends on input prices and physical productivity, not output price",
                            r"be impossible to determine because bread demand also changes",
                            r"require less of both inputs at every output level and therefore change the input ratio",
                        ],
                        "C",
                        r"Cost minimization is governed by $MP_L/w = MP_K/r$. Output price affects profit-maximizing scale, but not the least-cost input ratio for producing a given output.",
                    ),
                    q(
                        r"At the current levels of input use, the marginal revenue product of labor is",
                        [
                            r"\$12, so the bakery is using labor efficiently",
                            r"\$24, so the bakery should reduce labor",
                            r"\$48, so the bakery should hire more labor",
                            r"\$72, so the bakery should hire more labor",
                            r"\$96, so the bakery should reduce labor",
                        ],
                        "E",
                        r"The marginal revenue product of labor is price times marginal product: \$4 times 24 loaves, or \$96. Because this exceeds the \$12 wage, the bakery would want more labor at the margin.",
                    ),
                ],
            ),
            block(
                None,
                [
                    q(
                        r"If the demand for smartphones increases, the demand for assembly-line labor used to produce smartphones will most likely",
                        [
                            r"shift left because labor is a normal good",
                            r"shift right because labor demand is derived from product demand",
                            r"become perfectly elastic",
                            r"remain unchanged unless wages change first",
                            r"shift left because the price of the final product rises",
                        ],
                        "B",
                        r"Labor demand is a derived demand. When demand for the product increases, the demand for the labor used to produce that product also rises.",
                    ),
                    q(
                        r"If workers receive training that makes them more productive, the demand curve for those workers will most likely",
                        [
                            r"shift left because their wage will rise",
                            r"shift right because their marginal revenue product increases",
                            r"become perfectly inelastic",
                            r"shift left because the supply of skilled labor rises",
                            r"remain unchanged because training affects only supply",
                        ],
                        "B",
                        r"Better training raises marginal product, which increases marginal revenue product and shifts labor demand to the right.",
                    ),
                    q(
                        r"In a perfectly competitive labor market, an effective minimum wage above equilibrium will most likely create",
                        [
                            r"no unemployment because firms must hire at the legal wage",
                            r"excess demand for labor",
                            r"excess supply of labor",
                            r"a rightward shift of labor demand",
                            r"a leftward shift of labor supply",
                        ],
                        "C",
                        r"A binding minimum wage raises the wage above equilibrium, causing quantity of labor supplied to exceed quantity of labor demanded.",
                    ),
                    q(
                        r"If a binding minimum wage increases the total earnings of labor, that outcome is most likely because labor demand is",
                        [
                            r"relatively elastic",
                            r"relatively inelastic",
                            r"perfectly elastic",
                            r"unit elastic",
                            r"perfectly inelastic",
                        ],
                        "B",
                        r"When labor demand is relatively inelastic, the wage increase more than offsets the reduction in employment, so total earnings rise.",
                    ),
                    q(
                        r"If labor and capital are substitutes in production, an increase in the rental price of capital will most likely",
                        [
                            r"decrease the demand for labor",
                            r"increase the demand for labor",
                            r"decrease the supply of labor",
                            r"increase the supply of labor",
                            r"have no effect on labor demand",
                        ],
                        "B",
                        r"When capital becomes more expensive and labor can substitute for capital, firms shift toward labor, increasing labor demand.",
                    ),
                ],
            ),
            block(
                r"""
                The following questions refer to a monopsonistic labor market with labor supply curve $w = 10 + 2L$, marginal factor cost $MFC = 10 + 4L$, and marginal revenue product $MRP = 70 - 2L$, where $w$ is the wage and $L$ is the number of workers.
                """,
                [
                    q(
                        r"The monopsonist will hire",
                        [
                            r"10 workers at a wage of \$30",
                            r"10 workers at a wage of \$50",
                            r"15 workers at a wage of \$40",
                            r"15 workers at a wage of \$30",
                            r"20 workers at a wage of \$50",
                        ],
                        "A",
                        r"The monopsonist hires where $MFC = MRP$: $10 + 4L = 70 - 2L$, so $L=10$. The wage is then read from the supply curve: $w = 10 + 2(10) = 30$.",
                    ),
                    q(
                        r"In a competitive labor market with the same supply and demand conditions, employment and the wage would be",
                        [
                            r"10 workers and \$30",
                            r"10 workers and \$40",
                            r"15 workers and \$40",
                            r"15 workers and \$50",
                            r"20 workers and \$40",
                        ],
                        "C",
                        r"Competition sets labor supply equal to labor demand: $10 + 2L = 70 - 2L$, so $L=15$ and $w=40$.",
                    ),
                    q(
                        r"Compared with the competitive outcome, the monopsony results in",
                        [
                            r"higher wages and higher employment",
                            r"higher wages and lower employment",
                            r"lower wages and lower employment",
                            r"lower wages and higher employment",
                            r"the same wage but lower employment",
                        ],
                        "C",
                        r"A monopsonist restricts employment to push wages down. Relative to competition, both wage and employment are lower.",
                    ),
                    q(
                        r"If the government sets a minimum wage of \$40 in this monopsony, employment will most likely",
                        [
                            r"fall to 10 workers",
                            r"rise to 15 workers",
                            r"rise above 15 workers",
                            r"remain unchanged at 10 workers",
                            r"be impossible to determine without the firm's total cost curve",
                        ],
                        "B",
                        r"A minimum wage set at the competitive wage can make the firm's marginal factor cost flat at \$40 up to the relevant quantity. The firm then hires where \$40 equals MRP, which is 15 workers.",
                    ),
                    q(
                        r"The reason the monopsonist's marginal factor cost curve lies above the labor supply curve is that",
                        [
                            r"the firm pays each additional worker a higher wage but leaves existing workers' wages unchanged",
                            r"the firm must raise the wage on all workers when it hires an additional worker",
                            r"the labor supply curve is perfectly elastic",
                            r"marginal revenue product rises with employment",
                            r"fixed costs are increasing",
                        ],
                        "B",
                        r"In a monopsony, attracting an extra worker requires offering a higher wage, and that higher wage must generally be paid to all workers. Thus the marginal cost of one more worker exceeds the wage itself.",
                    ),
                ],
            ),
        ],
    },
    {
        "unit": 6,
        "title": "Market Failure and the Role of Government",
        "blocks": [
            block(
                r"""
                The following questions refer to a competitive market in which demand is $P = 50 - Q$, the marginal private cost is $MPC = 10 + Q$, and the marginal social cost is $MSC = 20 + Q$.
                """,
                [
                    q(
                        r"The quantity produced in the unregulated market equilibrium will be",
                        [
                            r"10 units",
                            r"15 units",
                            r"20 units",
                            r"25 units",
                            r"30 units",
                        ],
                        "C",
                        r"The unregulated market sets demand equal to marginal private cost: $50-Q = 10+Q$. Solving gives $Q=20$.",
                    ),
                    q(
                        r"The socially optimal quantity is",
                        [
                            r"10 units",
                            r"15 units",
                            r"20 units",
                            r"25 units",
                            r"30 units",
                        ],
                        "B",
                        r"Social efficiency requires demand to equal marginal social cost: $50-Q = 20+Q$. Solving gives $Q=15$.",
                    ),
                    q(
                        r"A Pigouvian tax that would lead the market to the socially optimal quantity should be set at",
                        [
                            r"\$5 per unit",
                            r"\$10 per unit",
                            r"\$15 per unit",
                            r"\$20 per unit",
                            r"\$25 per unit",
                        ],
                        "B",
                        r"The tax must make firms face the external cost. Since $MSC - MPC = 10$ at every quantity, the corrective tax is \$10 per unit.",
                    ),
                    q(
                        r"The deadweight loss from the unregulated market is",
                        [
                            r"\$12.50",
                            r"\$25.00",
                            r"\$37.50",
                            r"\$50.00",
                            r"\$75.00",
                        ],
                        "B",
                        r"The market overproduces from 15 to 20 units. The wedge between MSC and demand at 20 units is \$10, so deadweight loss is $\tfrac{1}{2}(5)(10)=25$.",
                    ),
                    q(
                        r"The market described above is inefficient because it",
                        [
                            r"underproduces relative to the socially optimal quantity",
                            r"overproduces because firms ignore external costs",
                            r"underprices output because demand is too elastic",
                            r"fails only because the market is perfectly competitive",
                            r"overproduces because marginal social benefit exceeds demand",
                        ],
                        "B",
                        r"When MSC exceeds MPC, firms base output on private rather than social cost. That causes the market to produce too much output.",
                    ),
                ],
            ),
            block(
                r"""
                The following questions refer to a flood barrier, which is a pure public good. Three residents have marginal benefit schedules given by
                $MB_A = 30 - Q$, $MB_B = 24 - Q$, and $MB_C = 18 - Q$.
                The marginal cost of each unit of the barrier is constant at \$36.
                """,
                [
                    q(
                        r"The marginal social benefit curve for the flood barrier is",
                        [
                            r"$MSB = 30 - Q$",
                            r"$MSB = 72 - Q$",
                            r"$MSB = 72 - 3Q$",
                            r"$MSB = 108 - 3Q$",
                            r"$MSB = 36 - 3Q$",
                        ],
                        "C",
                        r"For a public good, individual marginal benefits are added vertically. Thus $MSB = (30-Q)+(24-Q)+(18-Q) = 72-3Q$.",
                    ),
                    q(
                        r"The efficient quantity of the flood barrier is",
                        [
                            r"8 units",
                            r"10 units",
                            r"12 units",
                            r"18 units",
                            r"36 units",
                        ],
                        "C",
                        r"Set marginal social benefit equal to marginal cost: $72 - 3Q = 36$. Solving yields $Q=12$.",
                    ),
                    q(
                        r"If the flood barrier were left entirely to private voluntary purchase, the most likely outcome would be",
                        [
                            r"overproduction because people double count the benefits",
                            r"underproduction because of the free-rider problem",
                            r"efficient production because price reveals all benefits",
                            r"production at the monopolistic quantity",
                            r"production at the allocatively efficient quantity because the good is nonrival",
                        ],
                        "B",
                        r"Because the barrier is nonexcludable, people can benefit without paying. That weakens private willingness to pay and leads to underprovision.",
                    ),
                    q(
                        r"A pure public good is characterized by",
                        [
                            r"rivalry and excludability",
                            r"rivalry and nonexcludability",
                            r"nonrivalry and excludability",
                            r"nonrivalry and nonexcludability",
                            r"positive externalities and rivalry",
                        ],
                        "D",
                        r"Pure public goods are both nonrival and nonexcludable, which is why competitive markets tend to underprovide them.",
                    ),
                    q(
                        r"Which of the following is the best example of a common resource rather than a public good?",
                        [
                            r"National defense",
                            r"A lighthouse signal",
                            r"A fish population in an open-access lake",
                            r"A citywide tornado siren",
                            r"Broadcast radio",
                        ],
                        "C",
                        r"A common resource is generally nonexcludable but rival. An open-access fishery fits that description, unlike pure public goods such as national defense.",
                    ),
                ],
            ),
            block(
                None,
                [
                    q(
                        r"If a natural monopoly is regulated so that price equals marginal cost, the firm will often need a subsidy because",
                        [
                            r"marginal cost pricing always gives the firm economic profit",
                            r"at the allocatively efficient output, price can lie below average total cost",
                            r"natural monopolies have perfectly elastic demand curves",
                            r"average fixed cost is zero in the long run",
                            r"marginal revenue exceeds price for monopolies",
                        ],
                        "B",
                        r"Natural monopolies have declining ATC over the relevant range, so marginal cost lies below ATC. Pricing at MC can therefore cause losses unless the firm is subsidized.",
                    ),
                    q(
                        r"If a natural monopoly is instead regulated at the price where demand intersects average total cost, the result is that the firm",
                        [
                            r"earns losses and produces the allocatively efficient quantity",
                            r"earns zero economic profit but produces less than the allocatively efficient quantity",
                            r"earns monopoly profit and produces more than the efficient quantity",
                            r"must shut down because marginal cost exceeds price",
                            r"becomes perfectly competitive",
                        ],
                        "B",
                        r"ATC pricing lets the firm cover all costs and earn normal profit, but because price remains above marginal cost, output stays below the allocatively efficient level.",
                    ),
                    q(
                        r"Antitrust policy is primarily intended to",
                        [
                            r"guarantee equal incomes across households",
                            r"eliminate all large firms regardless of efficiency",
                            r"limit anticompetitive practices such as collusion and price fixing",
                            r"force all firms to produce where average total cost is minimized",
                            r"replace markets with government planning",
                        ],
                        "C",
                        r"Antitrust policy aims to preserve competition by discouraging mergers, collusion, and other practices that create or protect excessive market power.",
                    ),
                    q(
                        r"A cap-and-trade program for pollution can reduce total abatement cost relative to a uniform command-and-control rule because it",
                        [
                            r"lets firms with lower abatement costs reduce more pollution and sell permits",
                            r"requires every firm to cut pollution by the same percentage",
                            r"eliminates the need to define property rights",
                            r"guarantees zero pollution in equilibrium",
                            r"works only when demand is perfectly inelastic",
                        ],
                        "A",
                        r"Tradable permits direct pollution reduction toward firms that can reduce emissions most cheaply. That equalizes marginal abatement costs and lowers total cost.",
                    ),
                    q(
                        r"In a monopsonistic labor market, a minimum wage set between the monopsony wage and the competitive wage can",
                        [
                            r"reduce both wages and employment",
                            r"increase wages but always decrease employment",
                            r"increase both wages and employment",
                            r"have no effect because the monopsonist is already efficient",
                            r"eliminate marginal factor cost",
                        ],
                        "C",
                        r"In a monopsony, a moderate minimum wage can flatten marginal factor cost over a range of employment, leading the firm to hire more workers at a higher wage.",
                    ),
                ],
            ),
            block(
                r"""
                The following table shows cumulative shares of national income for two countries.

                \begin{center}
                \begin{tabular}{lcc}
                \toprule
                \shortstack{Cumulative\\ Households} & \shortstack{Country A\\ Income Share} & \shortstack{Country B\\ Income Share} \\
                \midrule
                Bottom 20\% & 4\% & 8\% \\
                Bottom 40\% & 13\% & 23\% \\
                Bottom 60\% & 29\% & 43\% \\
                Bottom 80\% & 53\% & 68\% \\
                Bottom 100\% & 100\% & 100\% \\
                \bottomrule
                \end{tabular}
                \end{center}
                """,
                [
                    q(
                        r"Based on the table, income is more equally distributed in",
                        [
                            r"Country A, because its top quintile receives a smaller share of income",
                            r"Country A, because its bottom quintile receives a smaller share of income",
                            r"Country B, because its Lorenz curve lies closer to the 45-degree line of equality",
                            r"Country B, because its top quintile receives a larger share of income",
                            r"neither country, because both have five quintiles",
                        ],
                        "C",
                        r"Country B gives larger cumulative income shares to the lower quintiles at every point, so its Lorenz curve is closer to the line of equality and its distribution is more equal.",
                    ),
                    q(
                        r"Which of the following is most likely true about the Gini coefficients of the two countries?",
                        [
                            r"Country A has the smaller Gini coefficient.",
                            r"Country B has the smaller Gini coefficient.",
                            r"The two countries must have the same Gini coefficient because total income is 100\% in both.",
                            r"Country B's Gini coefficient must exceed 1.",
                            r"The Gini coefficient cannot be inferred from Lorenz-style information.",
                        ],
                        "B",
                        r"A more equal Lorenz curve implies a smaller area between the curve and the line of equality, so Country B has the lower Gini coefficient.",
                    ),
                    q(
                        r"Which of the following tax policies is most likely to reduce after-tax income inequality?",
                        [
                            r"A regressive sales tax with no transfers",
                            r"A proportional income tax with no transfers",
                            r"A progressive income tax combined with transfer payments to low-income households",
                            r"A lump-sum tax on all households of the same dollar amount",
                            r"An excise tax on necessities purchased mostly by low-income households",
                        ],
                        "C",
                        r"Progressive taxation takes a larger share from higher incomes, and transfers raise lower incomes, both of which compress the after-tax income distribution.",
                    ),
                    q(
                        r"A general sales tax is typically described as regressive because",
                        [
                            r"high-income households spend a larger fraction of income on taxed goods",
                            r"low-income households usually spend a larger fraction of income on consumption",
                            r"the tax rate rises as income rises",
                            r"the tax is levied only on luxury goods",
                            r"the tax reduces consumer surplus for all households equally",
                        ],
                        "B",
                        r"Lower-income households tend to spend a larger share of their income, so a sales tax takes a larger percentage of income from them than from higher-income households.",
                    ),
                    q(
                        r"Which of the following policies is most likely to reduce long-run income inequality by raising workers' human capital?",
                        [
                            r"Eliminating all taxes on inherited wealth",
                            r"Reducing access to primary and secondary education",
                            r"Subsidizing broad access to education and job training",
                            r"Replacing progressive taxation with a flat head tax",
                            r"Imposing a price floor in the market for luxury goods",
                        ],
                        "C",
                        r"Education and training increase skills and productivity, which raise earning potential and can reduce inequality over time through human-capital accumulation.",
                    ),
                ],
            ),
        ],
    },
]
