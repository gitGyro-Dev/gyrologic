# 可読かつ継続可能な局所場面としてのStability

## Canonicalな意味

StabilityのCanonical Definitionは変更せず、次のとおり維持する。

> **Stabilityとは、開かれた道筋が、一つの成立として継続可能な状態である。**

この定義は、StabilityをSliceの後に位置づけながらも、Sliceの完了そのものへ還元しない。SliceはStructureの中に道筋を開き、局所的表出を利用可能にする。Stabilityは、その表出が一つの成立として読め、さらに継続可能であるかに関わる。

したがって、次の区別を維持する。

```text
Slice process
≠
local articulation
≠
Stability
```

local articulationが現れても、それが直ちに可読であり、十分にまとまりをもち、継続可能であるとは限らない。Stabilityは、その表出が関連するOrientationとContextのもとで一つの成立として利用可能になった場合に成立する。

## スカラーだけでは十分でない理由

実装を意識した領域では、Stabilityはスコア、閾値、確率、信頼度、または頑健性指標として表現され得る。これらは運用上有用な指標となり得るが、Stabilityの理論的意味を尽くすものではない。

例えば、

\[
\sigma_n \in [0,1]
\]

というスカラー表現は、特定モデルにおけるStabilityの評価度を示し得る。しかし、その値だけでは、どの関係が可読なのか、何が未解決のまま残っているのか、どのような継続が利用可能なのかを表現できない。スカラーはStability Sceneに関する選択された証拠を要約し得るが、その場面自体とは同一ではない。

したがって、

```text
Stability score
≠
Stability
```

である。

同じ制約は閾値判定にも当てはまる。

\[
\sigma_n \geq \theta
\]

という条件は、特定の実装方針のもとであるrealizationをstableと分類する根拠になり得るが、Canonical Conceptを定義するものではない。

## 平衡と固定点は部分モデルである

平衡、収束、不変集合、アトラクタ、固定点は、力学系におけるStabilityの強力なモデルである。関連する状態空間、力学、摂動モデルが正当化される場合、これらは特定のGyro Logic応用を具体化し得る。

しかしGyro Logicは、Stability Sceneが静止していること、全体として収束していること、不変であること、または終端であることを要求しない。局所的に可読な成立は、継続可能なまとまりを保ちながら変化し続け得る。また、長期極限が存在する前にStabilityとして読める場合もある。

したがって、

```text
Gyro Stability
≠
平衡のみ
≠
固定点のみ
≠
全体収束のみ
```

である。

これらの数学構造は、許容可能な特殊化であって普遍的定義ではない。

## 構造化された局所場面としてのStability

本モデルでは、Stability Sceneを暫定的に次のように表す。

\[
K_n
=
\bigl(a_n, L_n, U_n, C_n^{+}\bigr)
\]

ここで、

- \(a_n\) はSliceを通じて利用可能になったlocal articulationである。
- \(L_n\) は、その場面で現在可読な関係、区別、条件の族である。
- \(U_n\) は、未解決または不可読のまま残る局所的な未である。
- \(C_n^{+}\) は、その場面が支える継続条件または利用可能な継続の族である。

このタプルは形式化候補であり、置換定義ではない。その目的は、単一値では表現できない四つの区別を保持することにある。

第一に、表出自体と、それを可読にする関係とは同一ではない。第二に、現在可読なものは、局所的に未解決なものを尽くさない。第三に、現在の可読性と継続可能性は同一ではない。第四に、局所的StabilityはStructure全体の閉包を意味しない。

より明示的な形式化候補として、次を置く。

\[
K_n
=
\operatorname{StabScene}
\bigl(a_n;S_n,B_n,c_n\bigr)
\]

この記法は、Stabilityが表出の現れたStructure・Orientation・Contextに相対的に評価されることを示す。ただし、その評価が決定論的、全域的、または単一の述語へ還元できることを意味しない。

## 可読性と継続可能性

弱い論理的分解として、次を置ける。

\[
\operatorname{Stable}
\bigl(a_n;S_n,B_n,c_n\bigr)
\Rightarrow
\operatorname{Readable}
\bigl(a_n;S_n,B_n,c_n\bigr)
\land
\operatorname{Continuable}
\bigl(a_n;S_n,B_n,c_n\bigr)
\]

この含意は、本モデルにおける必要条件を示す。すなわち、表出が可読でも継続可能でもないなら、それをStabilityとして扱うことはできない。逆向きの含意は普遍的には採用しない。可読性と継続可能性は、領域固有の構造、程度、時間窓、許容条件を必要とする可能性があるためである。

可読性とは、その表出を未形成またはアクセス不能な結果ではなく、一つの成立として扱えることである。継続可能性とは、その成立が変化しないことを要求せず、後続のStructure、Slice、関係、Response、Tracingに参加できることである。

したがって、

```text
継続可能
≠
不変
```

であり、

```text
可読
≠
最終
```

である。

## 残存する未

本モデルの中心的要件は、Stabilityが未解決の局所的な未を含み得ることである。\(U_n\)を導入することにより、同一の場面の中で、

```text
局所的に可読な成立
+
残存する局所的な未
```

を同時に表現できる。

この特徴により、StabilityをStructure全体の閉包として解釈することを避けられる。ある場面は、確認と継続を支えられる程度には落ち着いていながら、なお未表出の区別、不可読な関係、未解決の選択肢、未知の条件、将来のSlice可能性を含み得る。

概略的には、

\[
U_n \neq \varnothing
\quad\text{であっても}\quad
K_n\text{はstableであり得る。}
\]

これは、すべてのStability Sceneが未解決要素を含まなければならないという意味ではない。形式モデルが\(U_n=\varnothing\)を強制してはならない、という意味である。

## 局所性と近傍解釈

Stabilityは、孤立点よりも局所場面または近傍として表す方が適切である。近傍構造が正当化される応用では、次のように書ける。

\[
K_n \subseteq N(a_n)
\]

ここで\(N(a_n)\)は、許容可能な変動範囲のもとで、表出が可読かつ継続可能であり続ける近傍である。

この記法は頑健性分析を支え得るが、Gyro Logicを位相空間へ普遍的に還元するものではない。近傍は、位相的、関係的、意味論的、運用的、確率的、または領域固有の構造であり得る。

本質的なコミットメントは、特定の近傍公理ではなく、可読性と継続可能性の局所的持続である。

## Stabilityは判断しない

Stabilityは評価されるものであり、評価するものではない。Continue、Stop、Jump、Re-Slice、Defer、その他のResponseを選択しない。これらの判断は、Coreの運用的拡張におけるOperator Responseに属する。

したがって、

```text
Stability
≠
Operator Response
```

である。

Stability Sceneは、後続Responseに関係する証拠や条件を提供し得るが、ResponseはStabilityのCanonicalな意味には含まれない。

この区別は、理論Coreとその運用的realizationを分離するために必要である。

```text
Structure
→ Slice
→ Stability
→ Operator Response
```

最後の矢印はGyro Processに属し、不変Core自体には属さない。

## Stabilityと後続Structure

Stability Sceneは、同一の形のまま移送されることなく、後続Structureで利用可能になり得る。その可読な区別、関係、継続条件は、後続Contextで織り込まれ、修正され、重みづけされ、無効化され、またはアクセス不能になり得る。

弱い遷移候補として、次を置く。

\[
K_n
\rightsquigarrow
q_n
\rightsquigarrow
\Gamma_{n+1}
\]

ここで\(q_n\)は局所的realizationから織り込まれるものを表し、\(\Gamma_{n+1}\)は後続の可読性Contextを表す。この遷移は、次章のIncorporated Readabilityで詳しく扱う。

ここで重要なのは、Stabilityが終端でも受動的な保存結果でもないことである。Stabilityは、後に何が可能、関連的、または追跡可能になるかを条件づけ得る、局所的に可読かつ継続可能な場面である。

## 最小限の形式的コミットメント

Stabilityモデルは、次の点にのみコミットする。

1. StabilityはSliceおよびlocal articulationから区別される。
2. Stabilityは局所的可読性と継続支援を必要とする。
3. Stabilityは一つのスカラーでは表現できない内部構造を持ち得る。
4. Stabilityは残存する局所的な未と共存し得る。
5. Stabilityは局所的であり、Structure全体を閉じない。
6. Stabilityは運用上の判断を行わない。
7. Stability SceneはIncorporated Readabilityを通じて後続realizationを条件づけ得る。

本モデルは、Stabilityが常にタプル、スカラー、平衡、固定点、アトラクタ、不変集合、確率、または二値述語であるとは仮定しない。これらはそれぞれ、特定領域で正当化される特殊化となり得る。

## Incorporated Readabilityへの接続

一つの表出がStability Sceneとして可読かつ継続可能になった後、その可読性の一部は後続realizationで利用可能になり得る。持続するものは、出来事、状態、場面の全体とは限らず、不変の記録として保存される必要もない。次章では、この作用を単純な履歴保存ではなく、Context更新としてのIncorporated Readabilityとして検討する。
