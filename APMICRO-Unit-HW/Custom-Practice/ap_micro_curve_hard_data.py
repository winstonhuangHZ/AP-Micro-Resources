from __future__ import annotations


def q(prompt: str, choices: list[str], answer: str, explanation: str) -> dict:
    return {
        "prompt": prompt,
        "choices": choices,
        "answer": answer,
        "explanation": explanation,
    }


def block(stimulus: str, questions: list[dict]) -> dict:
    return {"stimulus": stimulus, "questions": questions}


BLOCKS = [
    block(
        r"""
        The following questions refer to the graph below, which shows the market for tickets to an annual event with a fixed seating capacity.

        \begin{center}
        \begin{tikzpicture}[x=0.42cm,y=0.42cm]
        \draw[->] (0,0) -- (10,0) node[right] {Quantity of Tickets};
        \draw[->] (0,0) -- (0,10) node[above] {Price};
        \draw[thick] (7.2,0.8) -- (7.2,9.1) node[above] {$S$};
        \draw[thick] (0.8,8.8) -- (9.2,1.0) node[right] {$D_2$};
        \draw[thick] (1.4,7.2) -- (8.2,1.7) node[right] {$D_1$};
        \draw[dashed] (0,4.5) -- (7.2,4.5) node[left] {$P_1$};
        \draw[dashed] (0,5.9) -- (7.2,5.9) node[left] {$P_2$};
        \draw[dashed] (0,3.0) -- (9.0,3.0) node[left] {$P_c$};
        \node[below] at (7.2,0) {$Q_f$};
        \end{tikzpicture}
        \end{center}
        """,
        [
            q(
                r"If demand shifts from $D_1$ to $D_2$ and no price ceiling is imposed, which of the following will occur?",
                [
                    r"Price will remain at $P_1$ and quantity will remain at $Q_f$.",
                    r"Price will rise to $P_2$ and quantity will increase beyond $Q_f$.",
                    r"Price will rise to $P_2$ and quantity will remain at $Q_f$.",
                    r"Price will fall to $P_c$ and quantity will remain at $Q_f$.",
                    r"Price will rise to $P_2$ and quantity will fall below $Q_f$.",
                ],
                "C",
                r"Because supply is perfectly inelastic at $Q_f$, a rightward shift in demand raises price but cannot increase quantity. The new equilibrium is at price $P_2$ and quantity $Q_f$.",
            ),
            q(
                r"Suppose a binding price ceiling is set at $P_c$ after demand has shifted to $D_2$. The market outcome will most likely be",
                [
                    r"quantity exchanged greater than $Q_f$ because the lower price stimulates more demand",
                    r"quantity exchanged equal to $Q_f$ with a shortage because quantity demanded at $P_c$ exceeds quantity supplied",
                    r"quantity exchanged less than $Q_f$ because suppliers reduce output when price falls",
                    r"quantity exchanged equal to the quantity demanded on $D_2$ at $P_c$",
                    r"no shortage because the original supply is vertical",
                ],
                "B",
                r"With fixed seating, quantity supplied remains $Q_f$. At the ceiling price $P_c$, quantity demanded is larger than $Q_f$, so a shortage results even though the number of seats sold stays fixed at $Q_f$.",
            ),
            q(
                r"Relative to the original equilibrium with demand curve $D_1$, the event organizer's total revenue after the shift to $D_2$ and with no price ceiling will",
                [
                    r"increase because the same number of tickets is sold at a higher price",
                    r"decrease because demand becomes less elastic near the top of the graph",
                    r"remain unchanged because quantity is fixed",
                    r"decrease because a vertical supply curve prevents market adjustment",
                    r"be indeterminate because elasticity is not labeled numerically",
                ],
                "A",
                r"Total revenue is price times quantity. Quantity stays fixed at $Q_f$, while price rises from $P_1$ to $P_2$, so revenue increases.",
            ),
            q(
                r"If the binding ceiling at $P_c$ remains in place and resale is possible, which of the following is most accurate?",
                [
                    r"All buyers will necessarily pay exactly $P_c$ because the law fixes the final transaction price.",
                    r"No resale can occur because quantity supplied is perfectly inelastic.",
                    r"Producer surplus must rise because the event remains sold out.",
                    r"Some buyers may end up paying more than $P_c$ in a secondary market.",
                    r"The shortage disappears once buyers understand the supply curve is vertical.",
                ],
                "D",
                r"A binding ceiling below equilibrium encourages nonprice rationing and can create resale or scalping. Some consumers may ultimately pay above the legal ceiling in secondary transactions.",
            ),
        ],
    ),
    block(
        r"""
        The following questions refer to the graph below, which shows a small country that imports a good at world price $P_w$. Afterward, the country imposes a tariff that raises the domestic price to $P_t$.

        \begin{center}
        \begin{tikzpicture}[x=0.42cm,y=0.42cm]
        \draw[->] (0,0) -- (10,0) node[right] {Quantity};
        \draw[->] (0,0) -- (0,10) node[above] {Price};
        \draw[thick] (1.0,8.8) -- (9.0,1.4) node[right] {$D$};
        \draw[thick] (1.1,1.0) -- (8.6,8.5) node[right] {$S$};
        \draw[thick] (0.5,3.0) -- (9.3,3.0) node[right] {$P_w$};
        \draw[thick] (0.5,4.6) -- (9.3,4.6) node[right] {$P_t$};
        \draw[dashed] (2.3,0) -- (2.3,3.0);
        \draw[dashed] (3.5,0) -- (3.5,4.6);
        \draw[dashed] (6.1,0) -- (6.1,4.6);
        \draw[dashed] (7.3,0) -- (7.3,3.0);
        \node[below] at (2.3,0) {$Q_1$};
        \node[below] at (3.5,0) {$Q_2$};
        \node[below] at (6.1,0) {$Q_3$};
        \node[below] at (7.3,0) {$Q_4$};
        \end{tikzpicture}
        \end{center}
        """,
        [
            q(
                r"Before the tariff is imposed, the quantity imported by the country is",
                [
                    r"$Q_2-Q_1$",
                    r"$Q_3-Q_2$",
                    r"$Q_4-Q_3$",
                    r"$Q_4-Q_2$",
                    r"$Q_4-Q_1$",
                ],
                "E",
                r"At the free-trade world price $P_w$, domestic quantity supplied is $Q_1$ and domestic quantity demanded is $Q_4$. Imports therefore equal $Q_4-Q_1$.",
            ),
            q(
                r"After the tariff is imposed and the domestic price rises to $P_t$, the quantity imported becomes",
                [
                    r"$Q_2-Q_1$",
                    r"$Q_3-Q_2$",
                    r"$Q_4-Q_3$",
                    r"$Q_4-Q_1$",
                    r"$Q_3-Q_1$",
                ],
                "B",
                r"At the tariff-inclusive price $P_t$, domestic supply rises to $Q_2$ and domestic demand falls to $Q_3$. Imports shrink to $Q_3-Q_2$.",
            ),
            q(
                r"Which of the following expressions gives the government's tariff revenue?",
                [
                    r"$(P_t-P_w)(Q_4-Q_1)$",
                    r"$(P_t-P_w)(Q_3-Q_2)$",
                    r"$(P_t-P_w)(Q_2-Q_1)$",
                    r"$\tfrac{1}{2}(P_t-P_w)(Q_3-Q_2)$",
                    r"$\tfrac{1}{2}(P_t-P_w)(Q_4-Q_1)$",
                ],
                "B",
                r"Tariff revenue equals the tariff per unit times the number of imported units after the tariff. That is $(P_t-P_w)(Q_3-Q_2)$.",
            ),
            q(
                r"Relative to free trade, which of the following groups are guaranteed to gain from the tariff?",
                [
                    r"Domestic consumers only",
                    r"Domestic producers only",
                    r"Domestic producers and the government",
                    r"Foreign producers and domestic consumers",
                    r"Domestic consumers and the government",
                ],
                "C",
                r"The higher domestic price benefits domestic producers, and the government collects tariff revenue. Domestic consumers are harmed because they pay a higher price and buy less.",
            ),
        ],
    ),
    block(
        r"""
        The following questions refer to the graph below, which shows a competitive market before and after a per-unit excise tax is imposed.

        \begin{center}
        \begin{tikzpicture}[x=0.42cm,y=0.42cm]
        \draw[->] (0,0) -- (10,0) node[right] {Quantity};
        \draw[->] (0,0) -- (0,10) node[above] {Price};
        \draw[thick] (1.0,8.7) -- (8.8,1.3) node[right] {$D$};
        \draw[thick] (1.1,1.2) -- (8.5,8.3) node[right] {$S$};
        \draw[thick] (1.1,2.5) -- (8.5,9.6) node[right] {$S_{\text{tax}}$};
        \draw[dashed] (0,5.2) -- (5.1,5.2) node[left] {$P^{*}$};
        \draw[dashed] (0,6.0) -- (4.2,6.0) node[left] {$P_c$};
        \draw[dashed] (0,4.3) -- (4.2,4.3) node[left] {$P_p$};
        \draw[dashed] (5.1,0) -- (5.1,5.2);
        \draw[dashed] (4.2,0) -- (4.2,6.0);
        \node[below] at (5.1,0) {$Q^{*}$};
        \node[below] at (4.2,0) {$Q_t$};
        \end{tikzpicture}
        \end{center}
        """,
        [
            q(
                r"Based on the graph, the larger share of the tax burden is borne by",
                [
                    r"consumers, because the increase from $P^{*}$ to $P_c$ is larger than the decrease from $P^{*}$ to $P_p$",
                    r"producers, because the tax is legally imposed on sellers",
                    r"consumers and producers equally, because the tax wedge is fixed",
                    r"the government, because quantity falls from $Q^{*}$ to $Q_t$",
                    r"consumers, but only if demand is perfectly inelastic",
                ],
                "A",
                r"The graph shows the consumer-price increase is larger than the producer-price decrease, so consumers bear the larger share. Tax incidence depends on elasticities, not on the legal assignment of the tax.",
            ),
            q(
                r"Which of the following expressions equals total tax revenue after the tax is imposed?",
                [
                    r"$(P_c-P^{*})Q^{*}$",
                    r"$(P^{*}-P_p)Q^{*}$",
                    r"$(P_c-P_p)Q_t$",
                    r"$\tfrac{1}{2}(P_c-P_p)Q_t$",
                    r"$(P_c-P_p)(Q^{*}-Q_t)$",
                ],
                "C",
                r"Tax revenue is the per-unit tax wedge multiplied by the quantity sold after the tax. The vertical wedge is $P_c-P_p$, and the post-tax quantity is $Q_t$.",
            ),
            q(
                r"The deadweight loss created by the tax is measured by",
                [
                    r"$\tfrac{1}{2}(P_c-P_p)(Q^{*}-Q_t)$",
                    r"$(P_c-P_p)Q_t$",
                    r"$\tfrac{1}{2}(P_c-P^{*})Q_t$",
                    r"$(P^{*}-P_p)(Q^{*}-Q_t)$",
                    r"$(P_c-P_p)Q^{*}$",
                ],
                "A",
                r"The tax eliminates mutually beneficial trades from $Q_t$ to $Q^{*}$. The deadweight loss is the triangle with height equal to the tax wedge and base equal to the lost quantity.",
            ),
            q(
                r"If supply became more elastic while demand remained unchanged, which of the following would most likely occur?",
                [
                    r"Consumers would bear a larger share of the tax burden.",
                    r"Producers would bear a larger share of the tax burden.",
                    r"Consumers and producers would still bear equal shares.",
                    r"Tax revenue would necessarily rise.",
                    r"Deadweight loss would necessarily fall to zero.",
                ],
                "A",
                r"When supply is more elastic, producers are more able to reduce quantity supplied in response to the tax. The less elastic side of the market then bears more of the burden, so consumers pay a larger share.",
            ),
        ],
    ),
    block(
        r"""
        The following questions refer to the graph below, which shows a perfectly competitive firm's short-run cost curves and two possible market prices.

        \begin{center}
        \begin{tikzpicture}[x=0.42cm,y=0.42cm]
        \draw[->] (0,0) -- (10,0) node[right] {Output};
        \draw[->] (0,0) -- (0,10) node[above] {Cost, Revenue};
        \draw[thick] plot[smooth] coordinates {(1.0,3.2) (2.5,2.6) (4.5,2.4) (6.5,2.8) (8.4,3.8)} node[right] {$AVC$};
        \draw[thick] plot[smooth] coordinates {(1.0,4.6) (2.7,3.6) (4.9,3.3) (6.8,3.6) (8.6,4.5)} node[right] {$ATC$};
        \draw[thick] plot[smooth] coordinates {(1.5,1.6) (3.0,2.4) (4.6,4.2) (6.0,6.2) (7.2,8.4)} node[right] {$MC$};
        \draw[thick] (0.5,6.3) -- (9.1,6.3) node[right] {$P_1=MR_1$};
        \draw[thick] (0.5,4.4) -- (9.1,4.4) node[right] {$P_2=MR_2$};
        \draw[dashed] (6.1,0) -- (6.1,6.3);
        \draw[dashed] (4.8,0) -- (4.8,4.4);
        \node[below] at (6.1,0) {$Q_1$};
        \node[below] at (4.8,0) {$Q_2$};
        \end{tikzpicture}
        \end{center}
        """,
        [
            q(
                r"At price $P_1$, the firm's profit-maximizing output and profit situation are",
                [
                    r"$Q_1$ and positive economic profit",
                    r"$Q_1$ and negative economic profit",
                    r"$Q_2$ and positive economic profit",
                    r"$Q_2$ and zero economic profit",
                    r"zero output and negative economic profit",
                ],
                "A",
                r"A competitive firm chooses the quantity where price equals marginal cost on the upward-sloping portion of MC. At $P_1$, that output is $Q_1$, and the price line lies above ATC there, so economic profit is positive.",
            ),
            q(
                r"At price $P_2$, the firm should",
                [
                    r"shut down immediately because $P_2$ is below average total cost",
                    r"produce $Q_2$ because $P_2$ is above AVC even though the firm incurs a loss",
                    r"produce $Q_1$ to spread fixed costs over more output",
                    r"shut down because $P_2$ is below marginal cost at every output",
                    r"produce where ATC is minimized rather than where $P_2=MC$",
                ],
                "B",
                r"The shutdown rule compares price with AVC, not ATC. Since $P_2$ lies above AVC and intersects MC at $Q_2$, the firm continues producing $Q_2$ in the short run while taking a loss.",
            ),
            q(
                r"If the firm's fixed cost increases while the market price remains at $P_2$, the firm's short-run profit-maximizing output will",
                [
                    r"rise above $Q_2$",
                    r"fall below $Q_2$",
                    r"remain at $Q_2$",
                    r"fall to zero because ATC shifts up",
                    r"become indeterminate because MC also shifts upward",
                ],
                "C",
                r"A change in fixed cost shifts ATC but does not shift MC or AVC. Because the firm's output rule is $P=MC$ as long as price covers AVC, the output remains $Q_2$.",
            ),
            q(
                r"If many identical firms in the industry are currently earning the same type of profit shown at $P_1$, the most likely long-run market adjustment is that",
                [
                    r"market supply will decrease and the price will rise",
                    r"market supply will increase and the price will fall",
                    r"market demand will decrease and the price will rise",
                    r"firms will exit until price rises above $P_1$",
                    r"the long-run equilibrium price will remain at $P_1$ because firms are price takers",
                ],
                "B",
                r"Positive economic profit attracts entry. Entry shifts market supply right and drives the market price downward until firms earn zero economic profit in the long run.",
            ),
        ],
    ),
    block(
        r"""
        The following questions refer to the graph below, which shows a single-price monopoly.

        \begin{center}
        \begin{tikzpicture}[x=0.42cm,y=0.42cm]
        \draw[->] (0,0) -- (10,0) node[right] {Output};
        \draw[->] (0,0) -- (0,10) node[above] {Price, Cost};
        \draw[thick] (1.0,8.8) -- (8.8,2.0) node[right] {$D$};
        \draw[thick] (1.0,7.2) -- (7.6,0.8) node[right] {$MR$};
        \draw[thick] plot[smooth] coordinates {(1.0,4.8) (3.0,4.0) (5.0,4.3) (7.5,5.5) (8.7,6.6)} node[right] {$ATC$};
        \draw[thick] plot[smooth] coordinates {(1.2,2.4) (3.2,3.0) (4.8,4.0) (6.4,5.3) (8.2,7.4)} node[right] {$MC$};
        \draw[dashed] (4.7,0) -- (4.7,4.0);
        \draw[dashed] (7.0,0) -- (7.0,3.6);
        \draw[dashed] (0,5.6) -- (4.7,5.6) node[left] {$P_m$};
        \draw[dashed] (0,3.6) -- (7.0,3.6) node[left] {$P_c$};
        \node[below] at (4.7,0) {$Q_m$};
        \node[below] at (7.0,0) {$Q_c$};
        \end{tikzpicture}
        \end{center}
        """,
        [
            q(
                r"The monopoly's profit-maximizing output and price are",
                [
                    r"$Q_c$ and $P_c$",
                    r"$Q_m$ and $P_m$",
                    r"$Q_m$ and $P_c$",
                    r"$Q_c$ and $P_m$",
                    r"the quantity where $D$ intersects $ATC$ and the price at $MC$",
                ],
                "B",
                r"A single-price monopolist produces where $MR=MC$, which is $Q_m$, and then charges the price consumers are willing to pay on the demand curve, which is $P_m$.",
            ),
            q(
                r"Relative to the allocatively efficient outcome, the unregulated monopoly",
                [
                    r"produces too much because $P_m$ exceeds $ATC$",
                    r"produces too little because at $Q_m$, price exceeds marginal cost",
                    r"produces the efficient quantity because $MR=MC$",
                    r"produces the efficient quantity because $P_c=MC$",
                    r"must be productively efficient because it is a single seller",
                ],
                "B",
                r"Allocative efficiency requires price to equal marginal cost. At the monopoly quantity $Q_m$, the price on the demand curve is above MC, so the monopoly underproduces relative to the efficient level.",
            ),
            q(
                r"If the monopolist could engage in perfect price discrimination, the quantity produced would most likely",
                [
                    r"remain at $Q_m$ because marginal cost is unchanged",
                    r"fall below $Q_m$ because some consumers would pay more",
                    r"rise to $Q_c$, the same quantity a perfectly competitive market would produce",
                    r"rise above $Q_c$ because all consumer surplus is captured",
                    r"become indeterminate because marginal revenue is no longer defined",
                ],
                "C",
                r"A perfectly price-discriminating monopolist sells every unit for which willingness to pay is at least marginal cost. That expands output to $Q_c$, where demand intersects MC, the same quantity as in perfect competition.",
            ),
            q(
                r"If regulators force this monopoly to charge a price equal to average total cost, the resulting output will most likely be",
                [
                    r"less than $Q_m$",
                    r"equal to $Q_m$",
                    r"between $Q_m$ and $Q_c$",
                    r"equal to $Q_c$",
                    r"greater than $Q_c$",
                ],
                "C",
                r"Average-total-cost pricing increases output relative to an unregulated monopoly because price must fall. But since the regulated price still exceeds MC at the chosen quantity, output remains below the allocatively efficient level $Q_c$.",
            ),
        ],
    ),
    block(
        r"""
        The following questions refer to the graph below, which shows a monopolistically competitive firm in long-run equilibrium.

        \begin{center}
        \begin{tikzpicture}[x=0.42cm,y=0.42cm]
        \draw[->] (0,0) -- (10,0) node[right] {Output};
        \draw[->] (0,0) -- (0,10) node[above] {Price, Cost};
        \draw[thick] plot[smooth] coordinates {(1.2,5.8) (2.5,5.3) (4.7,4.6) (6.4,3.9) (8.3,2.9)} node[right] {$D$};
        \draw[thick] plot[smooth] coordinates {(1.3,4.6) (2.7,3.9) (4.7,3.2) (6.2,2.4) (7.8,1.3)} node[right] {$MR$};
        \draw[thick] plot[smooth] coordinates {(1.2,6.4) (2.7,5.2) (4.7,4.6) (6.8,4.0) (8.2,4.2)} node[right] {$ATC$};
        \draw[thick] plot[smooth] coordinates {(1.4,2.0) (3.0,2.5) (4.7,3.2) (6.8,4.5) (8.4,6.3)} node[right] {$MC$};
        \draw[dashed] (4.7,0) -- (4.7,4.6);
        \draw[dashed] (6.8,0) -- (6.8,4.0);
        \node[below] at (4.7,0) {$Q_m$};
        \node[below] at (6.8,0) {$Q_e$};
        \end{tikzpicture}
        \end{center}
        """,
        [
            q(
                r"The graph implies that the firm is earning",
                [
                    r"positive economic profit because the demand curve lies above marginal revenue",
                    r"zero economic profit because the demand curve is tangent to the ATC curve at the profit-maximizing quantity",
                    r"negative economic profit because the MC curve is rising",
                    r"normal accounting profit only if price equals marginal cost",
                    r"a loss because output is not at the minimum point of ATC",
                ],
                "B",
                r"In long-run monopolistic competition, entry drives economic profit to zero. Graphically, that appears as the demand curve tangent to ATC at the firm's chosen quantity.",
            ),
            q(
                r"The firm has excess capacity because",
                [
                    r"$Q_m$ is greater than the quantity that minimizes ATC",
                    r"$Q_m$ is less than the quantity that minimizes ATC, labeled $Q_e$",
                    r"the marginal revenue curve lies below the demand curve",
                    r"price exceeds marginal cost",
                    r"its demand curve is downward sloping",
                ],
                "B",
                r"Excess capacity means the firm produces less than the output that minimizes average total cost. The graph shows the firm's output $Q_m$ is to the left of $Q_e$, the minimum-ATC quantity.",
            ),
            q(
                r"Which of the following best describes the firm's allocative efficiency?",
                [
                    r"It is allocatively efficient because demand is tangent to ATC.",
                    r"It is allocatively efficient because $MR=MC$ at $Q_m$.",
                    r"It is not allocatively efficient because price exceeds marginal cost at $Q_m$.",
                    r"It is not allocatively efficient because ATC exceeds AVC at all outputs.",
                    r"It is allocatively efficient only if the firm advertises more.",
                ],
                "C",
                r"Allocative efficiency requires $P=MC$. In monopolistic competition, the downward-sloping demand curve implies price exceeds marginal cost at the profit-maximizing output.",
            ),
            q(
                r"If the firm were instead earning positive economic profit in the short run, the long-run adjustment that would move the firm toward the graph shown is",
                [
                    r"entry of new firms that shifts this firm's demand curve leftward",
                    r"exit of firms that shifts this firm's demand curve rightward",
                    r"a decrease in fixed cost that shifts ATC downward",
                    r"a price floor that shifts marginal revenue upward",
                    r"collusion among existing firms that makes demand perfectly elastic",
                ],
                "A",
                r"Positive short-run profits attract entry of close substitutes. That reduces demand for this firm's product and shifts its demand curve left until economic profit is eliminated.",
            ),
        ],
    ),
    block(
        r"""
        The following questions refer to the graph below, which shows a competitive labor market. The original labor demand curve is $D_1$, an increase in worker productivity shifts labor demand to $D_2$, and the government sets a minimum wage of $W_m$.

        \begin{center}
        \begin{tikzpicture}[x=0.42cm,y=0.42cm]
        \draw[->] (0,0) -- (10,0) node[right] {Labor};
        \draw[->] (0,0) -- (0,10) node[above] {Wage};
        \draw[thick] (1.0,1.0) -- (8.7,8.5) node[right] {$S$};
        \draw[thick] (1.0,8.4) -- (8.6,1.7) node[right] {$D_1$};
        \draw[thick] (1.8,9.0) -- (9.2,2.2) node[right] {$D_2$};
        \draw[thick] (0.5,6.4) -- (9.2,6.4) node[right] {$W_m$};
        \draw[dashed] (4.6,0) -- (4.6,4.8);
        \draw[dashed] (3.0,0) -- (3.0,6.4);
        \draw[dashed] (6.1,0) -- (6.1,6.4);
        \draw[dashed] (0,4.8) -- (4.6,4.8) node[left] {$W_1$};
        \node[below] at (4.6,0) {$Q_1$};
        \node[below] at (3.0,0) {$Q_d$};
        \node[below] at (6.1,0) {$Q_s$};
        \end{tikzpicture}
        \end{center}
        """,
        [
            q(
                r"If worker productivity increases so that labor demand shifts from $D_1$ to $D_2$, the competitive equilibrium wage and employment will",
                [
                    r"both decrease",
                    r"both increase",
                    r"wage will increase and employment will decrease",
                    r"wage will decrease and employment will increase",
                    r"remain unchanged because the labor supply curve does not shift",
                ],
                "B",
                r"A rightward shift in labor demand raises the equilibrium wage and the equilibrium quantity of labor employed in a competitive market.",
            ),
            q(
                r"At the binding minimum wage $W_m$, employment and unemployment in this labor market are",
                [
                    r"employment $Q_s$ and unemployment $Q_s-Q_d$",
                    r"employment $Q_d$ and unemployment $Q_s-Q_d$",
                    r"employment $Q_1$ and unemployment $Q_d-Q_1$",
                    r"employment $Q_d$ and unemployment $Q_d-Q_s$",
                    r"employment $Q_s$ and no unemployment because wage is above equilibrium",
                ],
                "B",
                r"With a binding minimum wage, firms hire only the quantity of labor demanded, which is $Q_d$. Workers supply $Q_s$, so unemployment equals $Q_s-Q_d$.",
            ),
            q(
                r"Total earnings received by workers who remain employed at the minimum wage are",
                [
                    r"$W_1 \cdot Q_1$",
                    r"$W_1 \cdot Q_d$",
                    r"$W_m \cdot Q_d$",
                    r"$W_m \cdot Q_s$",
                    r"$W_m(Q_s-Q_d)$",
                ],
                "C",
                r"Total earnings for employed workers equal the wage times the number of workers actually employed. Under the binding minimum wage, that is $W_m$ times $Q_d$.",
            ),
            q(
                r"A minimum wage like $W_m$ is more likely to increase the total earnings of labor when labor demand is",
                [
                    r"relatively elastic",
                    r"relatively inelastic",
                    r"perfectly elastic",
                    r"perfectly inelastic only",
                    r"unit elastic",
                ],
                "B",
                r"If labor demand is relatively inelastic, the wage increase outweighs the reduction in employment, making total earnings more likely to rise.",
            ),
        ],
    ),
    block(
        r"""
        The following questions refer to the graph below, which shows a monopsonistic labor market.

        \begin{center}
        \begin{tikzpicture}[x=0.42cm,y=0.42cm]
        \draw[->] (0,0) -- (10,0) node[right] {Labor};
        \draw[->] (0,0) -- (0,10) node[above] {Wage, Cost, Revenue Product};
        \draw[thick] (1.0,1.1) -- (8.7,8.0) node[right] {$S$};
        \draw[thick] (1.0,2.0) -- (8.7,9.3) node[right] {$MFC$};
        \draw[thick] (1.0,8.7) -- (8.8,1.5) node[right] {$MRP$};
        \draw[dashed] (3.6,0) -- (3.6,4.0);
        \draw[dashed] (5.1,0) -- (5.1,5.3);
        \draw[dashed] (0,4.0) -- (3.6,4.0) node[left] {$W_m$};
        \draw[dashed] (0,5.3) -- (5.1,5.3) node[left] {$W_c$};
        \node[below] at (3.6,0) {$L_m$};
        \node[below] at (5.1,0) {$L_c$};
        \end{tikzpicture}
        \end{center}
        """,
        [
            q(
                r"In the unregulated monopsony, the firm will hire",
                [
                    r"$L_c$ workers and pay wage $W_c$",
                    r"$L_m$ workers and pay wage $W_m$",
                    r"$L_m$ workers and pay wage $W_c$",
                    r"$L_c$ workers and pay wage $W_m$",
                    r"more than $L_c$ workers because $MFC$ exceeds $S$",
                ],
                "B",
                r"A monopsonist hires labor where $MRP=MFC$, which determines $L_m$. It then pays the wage found on the labor supply curve at that employment level, which is $W_m$.",
            ),
            q(
                r"Compared with a competitive labor market, the monopsony outcome results in",
                [
                    r"higher wages and higher employment",
                    r"higher wages and lower employment",
                    r"lower wages and lower employment",
                    r"lower wages and higher employment",
                    r"the same wage but lower employment",
                ],
                "C",
                r"In the competitive benchmark, wage and employment are $W_c$ and $L_c$. The monopsonist instead chooses $W_m$ and $L_m$, both of which are lower.",
            ),
            q(
                r"If the government sets a minimum wage equal to $W_c$, the most likely result is that employment",
                [
                    r"falls below $L_m$",
                    r"remains at $L_m$",
                    r"rises to $L_c$",
                    r"rises above $L_c$",
                    r"becomes zero because the wage is above $W_m$",
                ],
                "C",
                r"A minimum wage set at the competitive wage can flatten the firm's marginal factor cost up to the relevant range. The monopsonist then hires labor where that wage equals MRP, increasing employment to $L_c$.",
            ),
            q(
                r"The reason the $MFC$ curve lies above the labor supply curve is that",
                [
                    r"the firm must pay a lower wage to inframarginal workers when it hires another worker",
                    r"the firm can only hire labor if it also hires more capital",
                    r"hiring an additional worker requires raising the wage paid to all workers",
                    r"the labor supply curve is downward sloping to the firm",
                    r"marginal revenue product rises faster than wage",
                ],
                "C",
                r"In a monopsony, to attract another worker the employer generally must offer a higher wage, and that higher wage applies to all previously hired workers. Therefore the marginal cost of an extra worker exceeds the wage itself.",
            ),
        ],
    ),
    block(
        r"""
        The following questions refer to the graph below, which shows a market generating a negative production externality.

        \begin{center}
        \begin{tikzpicture}[x=0.42cm,y=0.42cm]
        \draw[->] (0,0) -- (10,0) node[right] {Output};
        \draw[->] (0,0) -- (0,10) node[above] {Price, Cost, Benefit};
        \draw[thick] (1.0,8.7) -- (8.8,1.6) node[right] {$MSB=D$};
        \draw[thick] (1.1,2.1) -- (8.7,7.4) node[right] {$MPC$};
        \draw[thick] (1.1,3.6) -- (8.7,8.9) node[right] {$MSC$};
        \draw[dashed] (4.0,0) -- (4.0,5.4);
        \draw[dashed] (5.7,0) -- (5.7,4.9);
        \node[below] at (4.0,0) {$Q_s$};
        \node[below] at (5.7,0) {$Q_m$};
        \end{tikzpicture}
        \end{center}
        """,
        [
            q(
                r"The unregulated market quantity is",
                [
                    r"$Q_s$, because the market accounts for all costs",
                    r"$Q_s$, because $MSB$ intersects $MSC$ there",
                    r"$Q_m$, because private decision makers equate marginal private cost with demand",
                    r"$Q_m$, because marginal social cost is below marginal private cost",
                    r"indeterminate because no prices are labeled",
                ],
                "C",
                r"Private firms ignore external costs and produce where demand intersects MPC, which is the market quantity $Q_m$. The socially efficient quantity is lower, at $Q_s$.",
            ),
            q(
                r"A per-unit Pigouvian tax that corrects the externality should be equal to",
                [
                    r"the vertical distance between $MSB$ and $MPC$ at $Q_m$",
                    r"the vertical distance between $MSC$ and $MPC$ at $Q_s$",
                    r"the horizontal distance between $Q_m$ and $Q_s$",
                    r"the vertical distance between $MSB$ and $MSC$ at $Q_s$",
                    r"the entire deadweight loss triangle",
                ],
                "B",
                r"The corrective tax must internalize the marginal external cost at the socially efficient output. Graphically, that is the vertical gap between $MSC$ and $MPC$ at $Q_s$.",
            ),
            q(
                r"The deadweight loss from the unregulated market is the area",
                [
                    r"between $MSB$ and $MPC$ from 0 to $Q_s$",
                    r"between $MSC$ and $MPC$ from 0 to $Q_s$",
                    r"between $MSC$ and $MSB$ from $Q_s$ to $Q_m$",
                    r"between $MSB$ and $MPC$ from $Q_s$ to $Q_m$",
                    r"between $MSC$ and $MPC$ from $Q_s$ to $Q_m$ plus the rectangle below it",
                ],
                "C",
                r"Overproduction from $Q_s$ to $Q_m$ creates a triangle of lost welfare. On those excess units, marginal social cost exceeds marginal social benefit.",
            ),
            q(
                r"If the government successfully imposes the corrective tax, which of the following will most likely occur?",
                [
                    r"Output will rise from $Q_m$ to $Q_s$ and total surplus will fall.",
                    r"Output will fall from $Q_m$ to $Q_s$ and total surplus will rise.",
                    r"Output will fall below $Q_s$ and total surplus will fall.",
                    r"Output will remain at $Q_m$ and firms will simply earn lower profit.",
                    r"Output will rise above $Q_m$ because tax revenue funds public goods.",
                ],
                "B",
                r"The tax reduces overproduction and moves the market to the socially efficient quantity $Q_s$. Eliminating the deadweight loss increases total surplus.",
            ),
        ],
    ),
    block(
        r"""
        The following questions refer to the Lorenz-curve graph below.

        \begin{center}
        \begin{tikzpicture}[x=0.055cm,y=0.055cm]
        \draw[->] (0,0) -- (105,0) node[right] {\scriptsize Households};
        \draw[->] (0,0) -- (0,105) node[above] {\scriptsize Income};
        \draw[thick] (0,0) -- (100,100) node[above right] {\scriptsize Equality};
        \draw[thick] plot[smooth] coordinates {(0,0) (20,5) (40,15) (60,30) (80,50) (100,100)} node[right] {\scriptsize A};
        \draw[thick] plot[smooth] coordinates {(0,0) (20,10) (40,24) (60,42) (80,65) (100,100)} node[right] {\scriptsize B};
        \draw[dashed] (80,0) -- (80,50);
        \draw[dashed] (0,50) -- (80,50);
        \end{tikzpicture}
        \end{center}
        """,
        [
            q(
                r"Based on the graph, which country has the more equal distribution of income?",
                [
                    r"Country A, because its Lorenz curve lies farther from the line of equality",
                    r"Country A, because its top 20\% receives a smaller share of income",
                    r"Country B, because its Lorenz curve lies closer to the line of equality",
                    r"Country B, because its Lorenz curve is steeper near the origin",
                    r"The two countries are equally distributed because both end at 100\%, 100\%",
                ],
                "C",
                r"A Lorenz curve closer to the 45-degree line indicates a more equal distribution of income. Country B's curve is consistently closer to that line than Country A's.",
            ),
            q(
                r"Which of the following is true about the Gini coefficients of the two countries?",
                [
                    r"Country A has the smaller Gini coefficient.",
                    r"Country B has the smaller Gini coefficient.",
                    r"They must be equal because both countries have a Lorenz curve.",
                    r"Country B's Gini coefficient must exceed 1.",
                    r"The Gini coefficient cannot be related to a Lorenz curve.",
                ],
                "B",
                r"The Gini coefficient rises as the Lorenz curve bows farther away from the line of equality. Since Country A is more bowed out, Country B has the smaller Gini coefficient.",
            ),
            q(
                r"A progressive tax-and-transfer system that reduces inequality would most likely shift a country's Lorenz curve",
                [
                    r"away from the line of equality",
                    r"toward the line of equality",
                    r"downward only at the 100\% endpoint",
                    r"into a perfectly horizontal line",
                    r"into a perfectly vertical line",
                ],
                "B",
                r"Redistribution that makes lower-income households receive a larger share of total income moves the Lorenz curve closer to the line of equality.",
            ),
            q(
                r"In Country A, the graph shows that the bottom 80\% of households receive 50\% of total income. Therefore, the top 20\% of households receive",
                [
                    r"20\% of total income",
                    r"30\% of total income",
                    r"40\% of total income",
                    r"50\% of total income",
                    r"80\% of total income",
                ],
                "D",
                r"If the bottom 80\% receive 50\%, the remaining top 20\% must receive the other 50\% of total income.",
            ),
        ],
    ),
]
