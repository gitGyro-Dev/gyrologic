# DifferenceとBoundary

DifferenceとBoundaryは、Gyro Logicにおける派生概念である。これらは不変Coreを置き換えるものではなく、Structure・Slice・Stabilityの間に追加段階として挿入されるものでもない。その役割は、特定のOrientation・Context・Sliceのもとで、非一致がどのように利用可能になり、構造化され、可読化されるかを記述することにある。

## Differenceは距離ではない

多くの数学的・計算的モデルでは、Differenceは数値的距離、偏差、残差、誤差として表現される。このような表現は、距離空間、ノルム、比較尺度、目標値が正当化されている場合には有効である。しかしGyro Logicは、そのような条件が普遍的に利用可能であるとは仮定しない。

Differenceは、非対称、部分的、関係的、カテゴリ的、順序的、分布的、Context依存的、あるいは場に類するものとなり得る。二つの識別可能な対象を比較する場合もあるが、パターン、領域、関係群、期待される継続、local articulationに関わる場合もある。したがってMinimal Formal Modelでは、次の暫定的な部分型付けを用いる。

\[
\Delta_{B,c,\Sigma}:X\rightharpoonup D
\]

ここで、\(X\) は検討対象となる要素、構成、関係、または表出された状況の領域を表し、\(D\) は意図的に異種的なまま残される。領域に応じて、\(D\) はスカラー、ベクトル、順序付きタプル、関係、半順序、分布、記号的分類、場に類する対象となり得る。

部分写像の矢印は重要である。現在のSliceのもとで、すべての入力についてDifferenceが利用可能である必要はない。比較不能、定義不能、不可読な場合があり得る。したがって、この記法は全域的な比較可能性を前提としない。

距離は、追加条件が正当化された特殊例である。

\[
d:X\times X\rightarrow \mathbb{R}_{\geq 0}
\]

この特殊化は、非負性、同一性、対称性、三角不等式などを要求し得る。しかし、これらの性質をGyro Difference一般へ課すことはしない。

したがって、

```text
Difference
≠
Distance
```

である。

## Differenceは誤差ではない

Errorは、偏差を判断するための基準、規範、目標、期待値、受容状態を前提とする。Differenceは、必ずしもそのような評価的意味をもたない。Differenceは、Sliceのもとで利用可能になった構造化された非一致を示すだけの場合がある。

例えば、形態、役割、解釈、関係、継続の変化はDifferenceであり得るが、失敗とは限らない。二つの局所的realizationが大きく異なっていても、可読なTrajectoryに参加し得る。反対に、数値的には小さな偏差でも、現在のOrientationとContextのもとで重要な区別を横切る場合には、運用上決定的となり得る。

したがって、

```text
Difference
≠
Error
```

である。

Error modelは、参照基準が明示的に与えられる特定領域では有効な具体化であるが、Differenceの普遍的意味ではない。

## Slice相対的な構造化された非一致としてのDifference

本論文では、次の作業上の特徴づけを採用する。

> Differenceとは、Slice相対的な、構造化された非一致の関係である。

この特徴づけは、三つのコミットメントを含む。

第一に、DifferenceはSliceに相対的である。Structure内部に潜在的な変動が存在し得るとしても、Sliceが比較、区別、関係を利用可能にする以前から、それが自動的に可読なDifferenceとして成立しているとは限らない。

第二に、Differenceは構造化されている。単に二つが等しくないというだけではない。非一致の関連形式には、方向、順序、局所性、依存、分布、非互換性、役割変更、時間的ずれなどが含まれ得る。

第三に、Differenceは関係的である。一つの数値で表現される場合でも、その数値は、対象、参照、Orientation、Context、Slice、期待される継続の間の関係を表す。

二項形式は、

\[
\Delta_{B,c,\Sigma}(x,y)
\]

と書ける。しかし、より一般的には、

\[
\Delta_{B,c,\Sigma}(X)
\]

も必要である。ここでは、Differenceが二つの独立した対象だけでなく、構成、関係場、Trajectory区間、局所場面に関わることを表す。

## Differenceとlocal articulation

Differenceは、Slice以前から可読な対象として存在している必要はない。Sliceは、local articulation \(a_n\) の中で、一つまたは複数の構造化された非一致を利用可能にし得る。

\[
S_n\xRightarrow{\Sigma_{B_n,c_n}}a_n
\]

表出は、対照、不連続、整合、非互換、関連性の変化などを現し得る。これらは可読なDifferenceの候補となるが、その意義は、現れただけでは確定しない。

Differenceは、現在可読な関係 \(L_n\)、未解決の局所的な未 \(U_n\)、継続条件 \(C_n^{+}\) を通じてStability Sceneへ関与し得る。StabilityはDifferenceの消失を要求しない。Difference pattern自体が、可読かつ継続可能になる場合がある。

したがって、

\[
\Delta_n\neq 0
\]

であってもStability Sceneは成立し得る。また、

\[
\Delta_n=0
\]

であることだけでは、Stability、Identity、Continuity Readabilityを含意しない。

## BoundaryはDifferenceではない

BoundaryはDifferenceと同一ではない。Differenceは構造化された非一致を表し、Boundaryは特定のSliceのもとで可読かつ利用可能になった区別を表す。

作業上の関係は次のとおりである。

```text
Difference
→ 区別として可読化され得る
→ Boundary
```

これは必須の時間順序ではなく、新たなCore段階を追加するものでもない。Difference patternが、局所的に可読な区別となるとき、Boundaryの発生、顕在化、発見、安定化を支え得るという派生関係を表す。

したがって、

```text
Difference
≠
Boundary
```

である。

Differenceは存在していてもBoundaryにならない場合がある。弱すぎる、分散している、現在は無関係である、アクセス不能である、未解決である場合などである。反対に、以前のDifference patternが現在の可読性Contextへ織り込まれているために、元のDifferenceが直接観測されなくてもBoundaryが運用上利用可能であり続ける場合がある。

## Slice相対的な可読区別としてのBoundary

Gyro Logicでは、次の補助的特徴づけを用いる。

> Boundaryとは、Sliceを通じて可読となったSlice相対的な区別である。

したがってBoundaryは、Structure内部に本来的に固定された線として存在すると仮定されない。空間的、論理的、意味的、運用的、社会的、時間的、手続的、またはそれらの複合であり得る。その関連形式は、Orientation・Context・Slice・Incorporated Readabilityに依存する。

暫定的なBoundary述語を、

\[
\operatorname{Bd}_{B,c,\Sigma,\Gamma}(d)
\]

と書く。これは、区別 \(d\) が、Orientation \(B\)、Context \(c\)、Slice \(\Sigma\)、Incorporated Readability Context \(\Gamma\) のもとでBoundaryとして読めることを意味する。

弱い候補条件は、

\[
\operatorname{Bd}_{B,c,\Sigma,\Gamma}(d)
\Rightarrow
\operatorname{Readable}(d;B,c,\Sigma,\Gamma)
\land
\operatorname{UsableDistinction}(d;B,c,\Sigma,\Gamma)
\]

である。

ただし逆は必ずしも成立しない。可読な区別であっても、当該領域でBoundaryとして機能しない場合がある。

## Boundary State

Boundary Stateは、可読なBoundaryに対する対象、事象、表出、realizationの暫定的な関係状態を表す。それは対象の内在的属性ではない。

候補記法は、

\[
\operatorname{BS}(x\mid d,B,c,\Sigma,\Gamma)
\]

である。ここで \(d\) は関連するBoundaryである。結果として、\(x\) はnormal、non-、un-、absence、blank、unknown、Void相対、inside、outside、crossing、deferred、その他の領域固有の関係へ分類され得る。

Boundary Stateは関係的かつ暫定的であるため、Orientation、Context、Slice、Incorporated Readabilityが変化すれば、基礎対象が別の対象へ変わらなくても分類が変わり得る。

## Boundary・Continuity・Trajectory

Boundaryは、ある種類の連続性を中断しながら、別の種類の連続性を保持し得る。型Boundaryの横断によって、ある基準でIdentityが断たれても、物質的、因果的、意味的、機能的なContinuity Readabilityが残り得る。

局所的realization \(g_i\)、\(g_j\) に対して、

\[
\operatorname{BdBreak}_{q}(g_i,g_j)
\]

が成立していても、別の許容可能な関係を通じて、

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma)
\]

が真であり得る。

これは、

```text
Boundary crossing
≠
Trajectory break
```

という区別を支える。

Boundaryは、ある関係を許容、非許容、前景化、DeferすることでContextual Tracingを導き得る。したがってTrajectoryの読解へ関与するが、Boundary自体がTrajectoryなのではない。

## DifferenceとBoundary Readabilityの織り込み

一つの局所的realizationで成立したDifference patternまたはBoundary distinctionは、後続の可読性条件へ織り込まれ得る。暫定的には、

\[
q_n^{\Delta}=\operatorname{Inc}_{\Delta}(g_n)
\]

または、

\[
q_n^{\mathrm{Bd}}=\operatorname{Inc}_{\mathrm{Bd}}(g_n)
\]

と表せる。

これらは、後続Contextを、

\[
\Gamma_{n+1}
=
\operatorname{Update}_{\Gamma}
(\Gamma_n,q_n^{\Delta},q_n^{\mathrm{Bd}},e_n)
\]

のように更新し得る。

ただし織り込みは永久保存を意味しない。以前利用可能であった区別は、修正、重み変更、無効化、抑制、アクセス不能化され得る。

## 形式的コミットメントと非コミットメント

Minimal Formal Modelは、次をコミットする。

1. DifferenceはOrientation・Context・Sliceに相対的である。
2. Differenceは部分的かつ異種的であり得る。
3. Differenceは普遍的に距離的または誤差的ではない。
4. Boundaryは可読な区別から派生し、Differenceと同一ではない。
5. Boundary Stateは関係的かつ暫定的である。
6. DifferenceとBoundaryは、Stability、Continuity Readability、Trajectory、後続のIncorporated Readabilityへ影響し得る。

一方、本モデルは、すべてのDifferenceが測定可能であること、すべてのBoundaryが鋭いこと、すべての区別が二値的であること、すべてのBoundaryが空間的であること、すべてのBoundary横断がContinuityを断つこと、すべての領域が一つの普遍的Difference codomainを共有することを仮定しない。

以上の整理は、統合Minimal Formal Modelへの準備となる。次章では、Structure、Slice、local articulation、Stability Scene、Incorporated Readability、Continuity Readability、Contextual Trajectory、Difference、Boundaryを、不変Coreを維持した一つの簡潔な形式スキーマへ統合する。