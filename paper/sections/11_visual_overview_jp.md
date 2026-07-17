# Minimal Formal Modelの図解

## Figure 1：不変Core

![Figure 1. Gyro Logicの不変Core。Operator OrientationとContextはSliceを条件づけるが、追加Core要素にはならない。](../figures/fig1_invariant_core.svg){width=88%}

Figure 1は、本論文全体を拘束する理論条件を示す。不変CoreはStructure → Slice → Stabilityのままである。Operator OrientationとContextはSlice processを条件づけるが、本モデルは、それら、local articulation、Trajectory、Difference、Boundary、Operator Responseを第四のCore要素として挿入しない。

## Figure 2：局所的Gyro realizationとContext更新

![Figure 2. 局所的Gyro realization、Stability Scene、後続readability contextの更新。](../figures/fig2_local_realization.svg){width=96%}

Figure 2は、暫定的な局所realization

\[
g_n=(S_n,B_n,c_n,\Sigma_n,a_n,K_n)
\]

を要約する。図は、Slice processとlocal articulationを分離し、さらにarticulationとStability Sceneを分離する。Stability Sceneは、可読な関係、残存する局所的な未、継続条件を含み得る。Incorporated Readability \(q_n=\operatorname{Inc}(g_n)\) は、後続readability context \(\Gamma_{n+1}\) を更新し、外的変化 \(e_n\) は明示的に別要因として保持される。

## Figure 3：Contextual Trajectory

![Figure 3. relation-bearing fieldから可読なTrajectoryへの文脈的Tracing。](../figures/fig3_contextual_trajectory.svg){width=96%}

Figure 3は、relation-bearing trace field

\[
\mathcal{G}_R=(G,E)
\]

と、可読なTrajectory

\[
T_{B,c,\Sigma_T,\Gamma_T}
=
\operatorname{Trace}_{B,c,\Sigma_T,\Gamma_T}(G,E)
\]

を分離する。relation-bearing fieldは、異種、休眠、競合、または現在不可読な関係を含み得る。Contextual Tracingは、現在条件のもとで関係を許容、抑制、重みづけ、合成、解釈する。結果としてのTrajectoryは、分岐、合流、空白、遡及的修正を含み得る。

## 図解の適用境界

これらの図は説明上の要約であり、置換定義ではない。Structureが箱であること、Sliceが決定論的な矢印であること、Stabilityが常にタプルであること、Trajectoryが常にグラフであることを意味しない。目的は、Minimal Formal Modelが維持する分離を可視化し、後続の数学研究および実装研究のための安定した参照点を提供することである。
