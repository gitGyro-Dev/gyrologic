# 文脈的Trajectory

## 局所的連続性からTrajectoryへ

前章では、関係の存在、追跡可能性、Continuity Readability、Identityを区別した。Trajectoryは、これらの区別を複数の局所的接続へ拡張して扱うための概念である。Trajectoryは新たなCore要素として導入されるものではない。特定のOrientation・Context・Slice・Incorporated Readabilityのもとで、複数の局所的Gyro realizationが接続として読めるようになる派生的な関係構成である。

本章の中心的主張は次のとおりである。

```text
Trajectory
≠
状態列
≠
時系列ログ
≠
イベント集合
≠
関係を保持する場そのもの
```

Trajectoryとは、局所的realization間の許容可能な関係を文脈的に辿ることによって読めるようになるものである。

## 局所的Gyro realization

一つの局所的Gyro realizationを、暫定的に次のように表す。

\[
g_i=(S_i,B_i,c_i,\Sigma_i,a_i,K_i).
\]

この表現は、そのrealizationに関わるStructure、Orientation、Context、Slice process、Sliceを通じて利用可能になったlocal articulation、対応するStability Sceneを識別する。各realizationが存在論的に独立しており、他のrealizationから完全に分離されていることを意味しない。添字 \(i\) は、分析上の暫定的参照を与えるだけである。

利用可能な局所的realizationの族を、次のように置く。

\[
G=\{g_i\}_{i\in I}.
\]

この族 \(G\) 自体はTrajectoryではない。Trajectoryとして読める可能性のある局所的realizationの集合にすぎず、一つ以上のTrajectoryを支える場合も、現在は何も支えない場合もある。

## 関係を保持するTrace Field

可能な関係型の族を \(\mathcal{R}\) とする。関係を保持するtrace fieldは、次のように表せる。

\[
E\subseteq G\times\mathcal{R}\times G,
\]

および、

\[
\mathcal{G}_{R}=(G,E).
\]

\((g_i,r,g_j)\in E\) は、二つの局所的realizationの間に、型 \(r\) の関係が利用可能、保持、推定、または表現可能であることを意味する。その関係は、因果的、物質的、機能的、意味的、手続的、制度的、Identityに関するもの、Boundaryに関するもの、Differenceに関するもの、または可読性に関するものとなり得る。本モデルは一つの普遍的な関係型を要求しない。

\(\mathcal{G}_{R}\) は、まだTrajectoryではない。それは可能なtraceを保持または支える場である。そこには、互いに両立しない関係、切断された成分、競合する解釈、潜在的な接続、現在のContextでは利用不能な関係が含まれ得る。したがって、次を区別する。

```text
関係を保持するtrace field
≠
可読なTrajectory
```

## 文脈的Tracing

Tracing operationは、Orientation \(B\)、Context \(c\)、Trajectory指向のSlice \(\Sigma_T\)、Incorporated Readabilityの文脈 \(\Gamma_T\) によって条件づけられる。可読なTrajectoryを、暫定的に次のように表す。

\[
T_{B,c,\Sigma_T,\Gamma_T}
=
\operatorname{Trace}_{B,c,\Sigma_T,\Gamma_T}(G,E).
\]

このTracing operationは、\(G\) の全要素や \(E\) の全関係を単純に列挙するものではない。現在の条件のもとで、許容可能なtraceを選択し、接続し、抑制し、重みづけし、解釈する。同じrelation-bearing fieldからでも、Orientation・Context・Slice・readability contextが異なれば、異なるTrajectoryが読まれ得る。

したがって、基礎となる局所的realizationや保持関係が変化しなくても、

\[
\operatorname{Trace}_{B_1,c_1,\Sigma_1,\Gamma_1}(G,E)
\neq
\operatorname{Trace}_{B_2,c_2,\Sigma_2,\Gamma_2}(G,E)
\]

となり得る。

## Traceの許容可能性

候補となるtraceを、次のように置く。

\[
\pi=(g_{i_0},r_1,g_{i_1},r_2,\ldots,r_m,g_{i_m}).
\]

これが可読なTrajectoryに含まれるためには、形式的に隣接しているだけでは不十分である。弱い許容条件を、次のように表す。

\[
\operatorname{AdmTrace}(\pi;B,c,\Sigma_T,\Gamma_T).
\]

この条件は、例えば次に依存し得る。

- 各関係型の許容可能性
- 連続する関係同士の整合性
- 現在の関連性重み
- 保持されたDifference pattern
- Boundary条件
- 利用可能な連続性基準
- 欠落またはアクセス不能な中間realization
- 解釈に対する文脈制約

許容可能性が、全体で固定され、二値的で、単調で、後続のIncorporated Readabilityから独立しているとは仮定しない。

## Trajectoryは事前定義された状態列ではない

状態Trajectoryは、しばしば次のように表される。

\[
x_0,x_1,x_2,\ldots,x_n.
\]

この表現は、各状態が共通の状態空間に属し、その順序関係がすでに利用可能であることを前提とする。Gyro Trajectoryが要求する前提は、これより弱い。接続されるrealizationは、型、表現、粒度、Identityが異なっていてもよい。連続性は、一つの遷移関数ではなく、異種の関係に依存し得る。

したがって、線形状態列は、前提が正当化される限定領域ではGyro Trajectoryを具体化し得るが、Trajectoryの普遍的形式ではない。

## Trajectoryはログではない

時系列ログは、出来事がある順序で保存されたことを記録する。しかし、それらの出来事の間でどの関係が許容され、追跡でき、連続性として読めるかを、それ自体で確立するわけではない。ログはTrajectory読解を支え得るが、ログそのものがTrajectoryではない。

保存履歴を \(H\) とすると、

\[
H\neq T_{B,c,\Sigma_T,\Gamma_T}.
\]

同じ履歴から複数のTrajectoryが読まれる場合も、何も読めない場合も、記録時点では利用不能だったTrajectoryが後に読める場合もある。

## 分岐・合流・複数Trajectory

relation-bearing fieldは複数の許容可能なTracingを支え得るため、Trajectoryは線形である必要がない。本モデルは次を許容する。

- 一つの局所的realizationから複数の継続が読まれる分岐
- 複数のtraceが一つの後続realizationへ寄与すると読まれる合流
- 異なるTracingが併存する並行Trajectory
- 異なる解釈が相互に両立しない競合Trajectory
- 局所traceがより広いtraceの中で読まれる入れ子Trajectory
- 一部のみが現在可読な部分Trajectory

したがって、特定の実装では、Tracing結果をグラフ、ハイパーグラフ、半順序、圏、イベント構造として表せる可能性がある。しかし本理論は、そのどれか一つを普遍的形式として固定しない。

## 空白と不可読区間

中間realizationの欠落は、Trajectoryの終了を自動的には意味しない。空白を越えて許容可能な関係を辿れるなら、連続性は可読なままであり得る。反対に、記録が密であっても、許容可能な関係が読めなければTrajectoryは成立しない。

したがって、

```text
記録上の空白
≠
Trajectory break
```

であり、

```text
密な履歴
≠
可読な連続性
```

である。空白をどう扱うかは、現在のOrientation・Context・Slice・Incorporated Readabilityに依存する。

## 遡及的TracingとRe-Slice

後続のrealizationによって、以前は利用不能だった可読性が導入されることがある。Re-Sliceを通じて、過去のrealizationと保持された関係は異なる仕方で辿られ得る。Trajectoryは、次のように遡及的に再構成または修正され得る。

\[
T^{(n)}
=
\operatorname{Trace}_{B_n,c_n,\Sigma_n,\Gamma_n}(G,E),
\]

\[
T^{(n+1)}
=
\operatorname{Trace}_{B_{n+1},c_{n+1},\Sigma_{n+1},\Gamma_{n+1}}(G,E).
\]

\(T^{(n)}\) から \(T^{(n+1)}\) への変化は、過去そのものが変更されたことを意味しない。後続条件のもとで、保持されたtraceの可読な組織化が変化したことを意味する。

## Jumpと非連続的再構成

Jumpは、単に大きな数値的不連続として定義されてはならない。本モデルにおけるJumpは、現在の連続性条件では既存のtrace organizationを通じた許容可能な継続を支えられない場合の再構成に関わる。Jumpは、以前のfieldを消去せずに、新たな局所的relation fieldまたは新たなTracing条件を成立させ得る。

したがって、

```text
Jump
≠
大きなDifferenceだけ
```

であり、

```text
Jump
≠
既存Trajectoryの必然的削除
```

である。後続Contextによって、Jumpを越えた関係が可読になる場合も、Jumpが認識された不連続として維持される場合もある。

## Incorporated Readabilityとの関係

Incorporated Readabilityは、どのtraceが許容され、重みづけされ、解釈されるかを条件づける。Tracingに利用されるreadability contextを \(\Gamma_T\) とすると、\(\Gamma_T\) の変化は次を生じさせ得る。

- 以前は不可読だった関係を可読にする
- 以前は許容されていた関係を無効化する
- 競合traceの重みを変更する
- 分離していた局所的realizationを接続する
- 一つの可読Trajectoryを複数へ分割する
- 複数のTrajectoryをより広いTrajectoryへ統合する

したがってTrajectoryは、先行するGyro realizationから独立ではないが、その保存された蓄積へ還元されるものでもない。

## 最小限のコミットメント

文脈的Trajectoryモデルがコミットするのは、次の事項に限られる。

1. 局所的Gyro realizationを暫定的に参照できること
2. それらの間の異種関係を表現できること
3. 関係の存在、追跡可能性、可読性を区別すること
4. Tracing operationがOrientation・Context・Slice・Incorporated Readabilityに条件づけられること
5. Tracing結果が非線形、部分的、修正可能、複数的であり得ること
6. Trajectoryが派生概念であり、不変Coreを置き換えないこと

本モデルは、すべてのTrajectoryが線形、因果的、完全、客観的に一意、連続微分可能、距離空間へ埋め込まれる、または一つの大域時計で添字づけられることを仮定しない。

## DifferenceとBoundaryへの接続

Tracingには、局所的realization間および可能な関係間の区別が必要となる。これらの区別は、状態、形、役割、基準、関連性、連続性の違いを含み得る。しかしDifferenceを距離や誤差と仮定することはできず、BoundaryをDifferenceそのものと同一視することもできない。次章では、DifferenceをSlice・Orientation・Contextに相対的な非一致の構造化された関係として整理し、Boundaryがどのように派生的な可読区別として成立し得るかを検討する。