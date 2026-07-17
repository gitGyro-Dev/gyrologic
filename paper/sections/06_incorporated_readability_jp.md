# Incorporated ReadabilityとContext更新

## 局所的Stabilityから後続条件へ

局所的なGyro realizationは、孤立したStability Sceneで終わるとは限らない。local articulationが、継続可能な成立として読めるようになったとき、その可読性の一部は、後続のrealizationで利用可能になり得る。本論文では、この後続利用可能性を **Incorporated Readability** と呼ぶ。

Incorporated Readabilityは、先行する出来事、Slice process、local articulation、またはStability Sceneそのものと同一ではない。局所的realizationのうち、何が後続条件の形成に利用可能になるかに関わる。そこには、成立した区別、関係、基準、関連性の順序、Boundary、Difference pattern、連続性条件、後続のOrientationへ影響する傾向などが含まれ得る。

局所的Gyro realizationを、暫定的に次のように表す。

\[
g_n = (S_n,B_n,c_n,\Sigma_n,a_n,K_n).
\]

このrealizationから織り込まれる可読性を、次のように書く。

\[
q_n = \operatorname{Inc}(g_n).
\]

この記法は、決定論的な抽出器が \(g_n\) から完全かつ損失なく要約を取り出すことを意味しない。\(\operatorname{Inc}\) は、\(g_n\) を通じて利用可能になった何らかの可読性が、後続条件でも利用可能になることを示す暫定的な関係である。

## Incorporated Readabilityは保存履歴ではない

保存履歴は、何かが起きたことを記録する。Incorporated Readabilityは、何が後続の成立に利用可能になったかに関わる。したがって、次の区別が必要である。

```text
先行realizationの履歴
≠
後続realizationで利用可能な可読性
```

ログは、ある出来事を保存していても、その出来事が後続解釈へ影響しない場合がある。反対に、織り込まれた区別は、元の出来事が明示的な記録として利用できなくなっていても、後続解釈を変化させ得る。したがってIncorporated Readabilityは、追記型保存、受動的記憶、時系列蓄積へ還元できない。

イベント履歴 \(H_n\) と可読性Context \(\Gamma_n\) を分けると、この違いは次のように表せる。

\[
H_{n+1}=\operatorname{Append}(H_n,g_n),
\]

一方で、

\[
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n).
\]

前者は出来事の発生を記録する。後者は、後続の読解、比較、Orientation、成立に利用可能な条件を変化させる。どちらか一方が生じても、他方が完全に生じるとは限らない。

## 利用可能な可読性条件としてのContext

\(\Gamma_n\) は、暫定的な可読性Contextを表す。これは、すべての領域で固定された命題集合として理解されるべきではない。realizationに応じて、次のような内容を保持または編成し得る。

- 新たに可能になった区別
- 新たに辿れるようになった関係
- 新たに適用可能になった基準
- 比較へ影響する既知のDifference pattern
- 利用可能になったBoundary
- 関連性の重みまたは優先順位
- 除外、無効化、未解決の競合
- 後続Sliceが進行するための条件

したがって、\(\Gamma_n\) は単なる項目の集合ではない。後続の可読性を条件づける構成である。

弱い特徴づけとして、次を置く。

\[
\Gamma_n
=
\langle
\mathsf{Avail}_n,
\mathsf{Weight}_n,
\mathsf{Constraint}_n,
\mathsf{Access}_n
\rangle^{*}.
\]

上付きの \(^*\) は、これがCanonical Definitionではなく形式化候補であることを示す。各要素は、何が利用可能か、どの程度影響するか、どの条件が利用を制約するか、そして現在アクセス可能かを区別する。

## 非単調な更新

Incorporated Readabilityは、単調に増加するとは仮定しない。後続更新は、追加、修正、統合、重み変更、無効化、抑制、アクセス不能化を含み得る。したがって、

\[
\Gamma_n \subseteq \Gamma_{n+1}
\]

が常に成り立つとは限らず、

\[
\Gamma_{n+1}=\Gamma_n\cup\{q_n\}
\]

とも限らない。

更新関係は、より一般に次のように書ける。

\[
\Gamma_{n+1}
=
\operatorname{Update}_{\Gamma}
(\Gamma_n,q_n,e_n),
\]

ここで \(e_n\) は、局所的Gyro realizationそのものへ還元できない環境的、制度的、対人的、物質的、その他の変化を表す。

この形式は、次の区別を維持する。

```text
Structure change
≠
Slice
```

また、後続条件のすべてが、直前のSliceだけによって生じるという誤った主張を避ける。

## Weighted Incorporated Readability

織り込まれた可読性が、すべて同じ影響力をもつとは限らない。ある区別は利用可能なまま周辺化され、別の区別は後続Contextにおいて決定的になる場合がある。そこで、Context相対的な重み関係を次のように置く。

\[
w_n(q;c,B) \in W,
\]

ここで \(W\) は数値である必要はない。順序、優先クラス、半順序、その他の影響構造であり得る。

したがって、織り込まれた可読性の作用は条件依存である。

\[
\operatorname{Effective}(q_n;B_m,c_m,\Sigma_m)
\]

は、ある後続realizationでは成立し、別のrealizationでは成立しない場合がある。Incorporated Readabilityは、永続的かつ普遍的な規則ではない。後続のStructure条件へ織り込まれ、Context相対的な影響をもつ可読性である。

## Structure更新

後続のStructureは、完全に独立した対象としては扱わない。同時に、Incorporated Readabilityだけから導出されるとも扱わない。弱い関係形式として、次を置く。

\[
(S_n,\Gamma_{n+1},e_n)\rightsquigarrow S_{n+1}.
\]

この表現は、更新が部分的、分散的、非決定論的、または遡及的にのみ読める場合を許容する。また、Structureと \(\Gamma_n\) を同一視しない。Structureは、何かが成立し得る様式であり続ける。\(\Gamma_n\) は、その様式の中で何が読めるようになるかへ影響する一つの条件である。

したがって、次の区別を維持する。

```text
Structure
≠
readability context
```

ただし、Incorporated Readabilityは後続のStructure条件を変化させ得る。

## 例：数学的推論

数学の問題を解く過程では、最終証明が完成する前に、定義、補題、中間等式、許容可能な変形が一度成立する場合がある。それらは成立後、後続の推論で利用可能になる。これは、ある手順が起きたという履歴が保存されるだけではない。後続の推論が正当に利用できるものを変化させる。

例えば、局所的結果 \(q_n\) が \(\Gamma_n\) のもとで成立したなら、後続推論は次のContextで進み得る。

\[
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n).
\]

後の訂正によって \(q_n\) が修正または無効化されれば、有効なContextも再び変化する。したがって本モデルは、織り込みと撤回の双方を許容する。

## 最小限のコミットメント

本モデルがコミットするのは、次の点に限られる。

第一に、局所的Gyro realizationは、何らかの可読性を後続realizationで利用可能にし得る。

第二に、織り込まれるものは、先行realization全体と同一ではない。

第三に、Incorporated Readabilityは、保存履歴へ還元されることなく後続条件を変化させ得る。

第四に、その更新は非単調かつContext相対的であり得る。

第五に、外的変化は、局所的Gyro realizationを通じた変化と形式的に区別されなければならない。

本モデルは、\(\Gamma_n\) が常に論理理論、データベース、記憶装置、ベクトル状態、確率分布であるとは仮定しない。それらは、前提が正当化される領域において有効な具体化となり得る。

## Continuity Readabilityへの接続

Incorporated Readabilityは、局所的成立がどのように後続条件で利用可能になるかを説明する。しかし、それだけでは二つの局所的realizationが接続していると読めるかは決まらない。そのためには、関係が存在すること、その関係を辿れること、そして連続性として読めることを分離しなければならない。次章では、この区別をContinuity Readabilityとして扱う。