# 最小形式モデル

## 統合スキーマの目的

前章まででは、提案する形式化の主要構成要素を個別に検討した。本章では、それらを一つの最小スキーマへ統合する。目的は、Gyro Logicを完全に公理化することでも、各概念に対して最終的な数学的存在論を一つ決定することでもない。目的は、現在の理論的区別を保持するために必要な、最小限の識別可能な対象と関係を明らかにすることである。

統合モデルは、次の不変Coreを保持しなければならない。

```text
Structure
↓
Slice
↓
Stability
```

同時に、局所的realizationが生じる条件、Sliceを通じて利用可能になる表出、後続の文脈へ織り込まれる可読性、および連続性とTrajectoryが可読になるための関係も表現する必要がある。

## 局所的Gyro realization

局所的Gyro realizationを、暫定的に次で表す。

\[
g_n
=
\bigl(
S_n,
B_n,
c_n,
\Sigma_n,
a_n,
K_n
\bigr).
\]

各要素の役割は次のとおりである。

\[
\begin{aligned}
S_n &:\ \text{局所的realizationに関わるStructure},\\
B_n &:\ \text{Sliceを条件づけるOperator Orientation},\\
c_n &:\ \text{realizationに関係するContext},\\
\Sigma_n &:\ \text{Slice process},\\
a_n &:\ \text{Sliceを通じて利用可能になるlocal articulation},\\
K_n &:\ \text{表出が可読かつ継続可能になるStability Scene}.
\end{aligned}
\]

このタプルは表現上の便宜である。すべての局所的Gyro realizationを存在論的に固定されたタプルとして定義するものではない。また、Orientation、Context、local articulationを不変Coreへ挿入するものでもない。これらは局所的な形式記述を精緻化するが、Coreは次のまま維持される。

\[
S_n
\xRightarrow{\Sigma_{B_n,c_n}}
a_n
\xRightarrow{\operatorname{Stab}}
K_n.
\]

第一の関係は、OrientationとContextのもとで進行するSliceを表す。第二の関係は、局所的に利用可能になった表出からStability Sceneへの移行を表す。いずれの矢印も、決定論的な全域関数とは仮定しない。

## Structure

Structureは識別子 \(S_n\) によって表すが、その数学型は意図的に未確定のまま残す。モデルがコミットするのは、局所的に関係する状態、関係、区別、または表出が、Structureに相対的に利用可能になり得ることのみである。

弱い関係記法として、次を用いる。

\[
x \triangleleft S_n.
\]

これは、\(x\) が \(S_n\) に相対的に局所的に成立可能または利用可能であることを表す。この関係は、集合所属、空間的包含、因果的依存、論理的含意のいずれかに限定されない。特定領域のモデルでは、必要に応じて特殊化できる。

## Sliceとlocal articulation

Sliceは次で表す。

\[
S_n
\xRightarrow{\Sigma_{B_n,c_n}}
a_n.
\]

この表現は、次の区別を保持する。

```text
Slice process
≠
local articulation
```

モデルは、\(a_n\) がSlice以前から完全に個体化された結果として存在し、抽出されるのを待っていたとは仮定しない。また、\(a_n\) がすでにStableであるとも仮定しない。表出は、Sliceによって局所的に利用可能になる「こうなった」である。

## Stability Scene

Stability Sceneは暫定的に次で表す。

\[
K_n
=
\bigl(
a_n,
L_n,
U_n,
C_n^{+}
\bigr),
\]

ここで、

\[
\begin{aligned}
a_n &:\ \text{local articulation},\\
L_n &:\ \text{現在可読な関係と区別},\\
U_n &:\ \text{残存する局所的な未},\\
C_n^{+} &:\ \text{利用可能な継続条件または継続}.
\end{aligned}
\]

この表現では、

\[
U_n \neq \varnothing
\]

であっても、\(K_n\) はStability Sceneとして成立し得る。したがってStabilityは、全体閉包、Differenceの消失、またはより大きなStructureの終了を意味しない。

弱い条件として、次を置く。

\[
\operatorname{StableScene}
\bigl(
a_n;S_n,B_n,c_n
\bigr).
\]

これは、関連条件のもとで、表出が一つの成立として十分に可読であり、かつ十分に継続可能であることを表す。可読性および継続可能性が必ず二値であるとは仮定しない。

## Incorporated Readability

局所的realizationのうち、後続のrealizationで利用可能になる部分を次で表す。

\[
q_n
=
\operatorname{Inc}(g_n).
\]

現在の可読性Contextを \(\Gamma_n\) とし、その更新を次で表す。

\[
\Gamma_{n+1}
=
\operatorname{Update}_{\Gamma}
\bigl(
\Gamma_n,
q_n,
e_n
\bigr),
\]

ここで、\(e_n\) はSliceへ還元できない外的変化、相互作用、環境効果を表す。

この更新は、追記型履歴とは同一ではない。

\[
\Gamma_{n+1}
\neq
\Gamma_n \cup \{q_n\}
\]

が一般に成立し得る。更新は、追加、修正、統合、重み変更、無効化、抑制、またはアクセス不能化を含み得る。

後続Structureは、次の関係で表せる。

\[
\bigl(
S_n,
\Gamma_{n+1},
e_n
\bigr)
\rightsquigarrow
S_{n+1}.
\]

この関係は、すべてのStructure変化が先行するGyro realizationによって生成されると主張するものではない。

## Continuity Readability

\(g_i\) と \(g_j\) を局所的Gyro realizationとする。Continuity Readabilityを次で表す。

\[
\operatorname{CR}
\bigl(
g_i,g_j;
B,c,\Sigma,\Gamma
\bigr).
\]

弱い条件は次である。

\[
\operatorname{CR}
\bigl(
g_i,g_j;
B,c,\Sigma,\Gamma
\bigr)
\iff
\exists r\,
\Bigl(
\operatorname{Adm}(r;B,c,\Sigma,\Gamma)
\land
\operatorname{Traceable}(g_i,g_j;r)
\land
\operatorname{Readable}(r;B,c,\Sigma,\Gamma)
\Bigr).
\]

これは次を分離する。

```text
関係の存在
≠
追跡可能性
≠
Continuity Readability
```

Identityは別の関係として維持する。

\[
\operatorname{Id}_{q}(g_i,g_j).
\]

モデルは、Identityを伴わないContinuity Readabilityと、可読な連続性を伴わないIdentity主張の双方を許容する。

## 関係保持場とTrajectory

局所的Gyro realizationの族を、

\[
G=\{g_i\}_{i\in I}
\]

とする。また、保持された異種関係の族を、

\[
E\subseteq G\times\mathcal{R}\times G
\]

とする。関係を保持するtrace fieldを次で表す。

\[
\mathcal{G}_R=(G,E).
\]

trace field自体はTrajectoryではない。可読なTrajectoryは、文脈的Tracingによって構成される。

\[
T_{B,c,\Sigma_T,\Gamma_T}
=
\operatorname{Trace}_{B,c,\Sigma_T,\Gamma_T}(G,E).
\]

Tracing operationは、Orientation、Context、Trajectory指向のSlice、Incorporated Readabilityに応じて、関係を選択、結合、抑制、再解釈、または未読のまま残し得る。結果として得られるTrajectoryは、分岐、合流、空白、遡及的再解釈、Re-Slice、Jumpを含み得る。一つの時系列状態列へ限定されない。

## Difference

Differenceは、部分的かつ異種的な写像として暫定的に型付けする。

\[
\Delta_{B,c,\Sigma}
:
X
\rightharpoonup
D.
\]

値域 \(D\) は、スカラー、ベクトル、順序構造、関係、分布、記号分類、部分順序、または場に類する対象を取り得る。Differenceが距離的、対称的、全域的、または誤差的であるとは仮定しない。

Differenceは、Stability、Continuity Readability、Trajectory解釈、Boundary形成に寄与し得るが、次の区別を保持する。

```text
Difference
≠
Distance
≠
Error
≠
Boundary
```

可読なBoundaryを次で表す。

\[
\operatorname{Bd}_{B,c,\Sigma,\Gamma}(d).
\]

これは、区別 \(d\) が現在の条件のもとでBoundaryとして読めることを意味する。したがってBoundaryは、可読な区別から派生するものであり、追加のCore段階として導入されない。

## コンパクトな統合形

Minimal Formal Modelは、次の式で要約できる。

\[
g_n
=
(S_n,B_n,c_n,\Sigma_n,a_n,K_n),
\]

\[
S_n
\xRightarrow{\Sigma_{B_n,c_n}}
a_n,
\]

\[
K_n
=
\operatorname{StabScene}
(a_n;S_n,B_n,c_n),
\]

\[
q_n
=
\operatorname{Inc}(g_n),
\]

\[
\Gamma_{n+1}
=
\operatorname{Update}_{\Gamma}
(\Gamma_n,q_n,e_n),
\]

\[
(S_n,\Gamma_{n+1},e_n)
\rightsquigarrow
S_{n+1},
\]

\[
\operatorname{CR}(g_i,g_j)
\iff
\exists r:
\operatorname{Adm}(r)
\land
\operatorname{Traceable}(r)
\land
\operatorname{Readable}(r),
\]

\[
\mathcal{G}_R=(G,E),
\]

\[
T
=
\operatorname{Trace}(G,E),
\]

\[
\Delta_{B,c,\Sigma}:X\rightharpoonup D.
\]

コンパクト表現で省略されたパラメータは、前述の完全形では維持されている。

## 本モデルが保証すること

現在の探索段階において、本モデルが保証するのは概念的・形式的分離である。Structure、Slice process、local articulation、Stability Sceneを区別する。履歴とIncorporated Readability、関係の存在とContinuity Readability、Identityと連続性、trace fieldとTrajectory、Differenceと距離・誤差・Boundaryを分離する。また、不変CoreとGyro Logic・GyroOS・GyroAuthのLayer分離を維持する。

## 本モデルが保証しないこと

本モデルは、完全公理化、普遍意味論、表現の一意性、決定可能性、計算量境界、実証的妥当性、または厳密な数学的意味での最小性の証明を、現時点では提供しない。Structureの最終的数学型、普遍的Stability尺度、普遍的Tracingアルゴリズム、普遍的Difference値域も決定しない。これらは、領域別具体化と後続検証の対象である。

したがって統合スキーマは、形式的な設計境界として機能する。比較、例示、実装研究、後続の精緻化を支える程度に明示的でありながら、保持すべき理論的区別を上書きしない程度に弱い構成である。
