# 既存数学分野との比較

## 比較の目的

Minimal Formal Modelは、既存数学から切り離された独立体系として提案されるものではない。Gyro Logicの各部分については、既存の複数分野が有効な表現手段を提供する。ここで問うべきなのは、Gyro Logicがどの一分野に「属するか」ではなく、各分野がどの前提を導入し、その前提がGyro Logic固有の区別をどこまで保持し、どこから抑圧するかである。

したがって本比較では、各分野を次の二つの観点から評価する。

1. **表現上の有効性**：提案スキーマのどの部分を適切に表現できるか。
2. **還元リスク**：その分野をGyro Logic全体の普遍的形式として採用した場合、どの理論的区別が失われるか。

以下で扱う分野を否定するものではない。各分野は、適用領域と形式化制約を明示したうえで用いられる部分モデルとして位置づけられる。

## 関係構造

関係構造は、提案モデルの基礎候補として最も広い柔軟性をもつ。異種の対象、部分関係、許容条件、Difference pattern、Boundary relation、局所的Gyro realization間の接続を、すべて数値や距離へ還元せずに表現できる。

局所領域は暫定的に次のように書ける。

\[
\mathfrak{R}
=
\langle X,\{R_\alpha\}_{\alpha\in A}\rangle,
\]

ここで関係族 \(\{R_\alpha\}\) は、因果、意味、物質、時間、推論、制度などの関係を含み得る。

この柔軟性は、Continuity ReadabilityやContextual Trajectoryに有効である。一方、通常の関係構造は、対象と関係がすでに利用可能であるように見せやすい。それ自体では、local articulationがSliceを通じてどのように利用可能になるか、不可読な関係がどのように可読になるか、Incorporated Readabilityが後続条件をどう変えるかを説明しない。

## グラフとハイパーグラフ

グラフは、局所的Gyro realizationと痕跡を担う関係の自然な表現を与える。

\[
\mathcal{G}_R=(G,E).
\]

有向グラフは、非対称な継起、依存、Tracingを表現できる。多重グラフは、同じrealization間の複数の関係型を保持できる。ハイパーグラフは、二項辺へ還元できない複数realization間の関係を表現するのに有効である。

分岐、合流、競合するtrace、空白、遡及的再接続の表現に適している。しかしグラフそのものはTrajectoryではない。通常のグラフは、ノードと辺がすでに個体化され、表現可能であることを仮定する。Gyro Logicでは、関係を保持する場と、文脈的Tracingを通じて可読になるTrajectoryとを分離しなければならない。

## 順序理論

順序理論は、先行関係、依存、精緻化、関連性の順位、部分比較可能性を表現できる。Incorporated Readabilityによって区別の影響順位が変化する場合や、Trajectoryが単一時系列ではなく部分順序によって制約される場合に有効である。

例えば、領域相対的な順序を次のように書ける。

\[
x\preceq_{B,c,\Gamma}y.
\]

これは、特定条件のもとで、\(x\) が \(y\) より成立していない、関連性が低い、または先行していることなどを表し得る。

ただし、Differenceは常に順序づけられるとは限らない。比較不能であることは、欠如や失敗を意味しない。したがって順序理論は、DifferenceやStabilityの普遍的値域ではなく、有効な特殊例である。

## 位相と近傍構造

位相は、局所性、近傍、小さな変動に対する持続、Boundaryに類する構成を表現するのに有効である。Stability Sceneをlocal articulationの周囲の近傍として解釈できる。

\[
a_n\in N_n.
\]

この近傍には、全体閉包を要求せず、可読な関係と許容される継続を含められる。これにより、Stabilityを一点ではなく、限定された変動のもとで確認と継続が可能な局所領域として扱える。

ただし、Gyro Stabilityは位相的安定性と同一ではなく、Gyro Boundaryも位相的境界より広い。さらに、Structureの理論的な「未」を位相的開性と同一視してはならない。位相は、対象と近傍が設定された後の局所場面を表現できるが、それらがSliceによってどのように表出するかを単独では説明しない。

## 力学系

力学系は、時間発展、摂動、収束、振動、回復、発散を扱う領域モデルとして強力である。観測可能な状態変数と更新則が定義されているGyroOSやGyroAuthの実装では、とりわけ有効である。

通常の力学モデルは次の形をとる。

\[
x_{t+1}=F(x_t,u_t).
\]

この形式により、Stability score、収束条件、drift detection、response dynamicsを実装できる。しかし力学系のTrajectoryは通常、状態発展そのものである。本モデルにおけるTrajectoryは、局所的realization間の許容可能な関係をTracingすることで読まれる構成である。また、Lyapunov stability、平衡、attractorは特定仮定のもとでのStability実装となり得るが、Stability Sceneの意味全体ではない。

## 遷移系とイベント構造

遷移系は、操作的継起、分岐選択、有効化されたaction、状態依存responseを表現する。イベント構造は、並行性、因果、競合を加え、一つの線形実行順へ還元できない過程を扱える。

これらは、Gyro Process、Operator Response、Re-Slice、Jump、分岐Trajectoryの形式化に関連する。局所的realizationをeventとして、因果関係や有効化関係で接続することもできる。

ただし、状態、event、transitionは通常、実行前に定義されている。Sliceは、local articulationが利用可能になる過程に関わる。したがって遷移系は、実現済みのGyro processを実装できるが、表出以前のStructureを自動的に形式化するわけではない。

## 圏論

圏論は、異種対象、変換、合成、Identity、構造保存写像を扱う強力な言語である。対象型の同一性を要求せずに継続を表現する場合や、異なる領域の局所過程を合成する場合に有効である。

局所的候補として、次のように書くこともできる。

\[
\Sigma:S\to A,
\]

または、traceable relationを射として、その合成を許容可能なpathとして扱える。

しかし通常の射は、定義された始域と終域を前提とする。Gyro Logicでは、local articulation \(a_n\) がSlice以前から完全に定められた終域として存在するとは仮定しない。圏論的モデルは、領域固有のarticulation spaceが正当化された後に適切となる可能性が高い。圏論は有力な統合言語だが、現時点でStructureやSliceの普遍的存在論ではない。

## 論理と証明論

論理と証明論は、Incorporated Readabilityの部分モデルとして非常に強い。証明文脈 \(\Gamma_n\) は、後続推論で利用可能になった定義、仮定、補題、区別、推論規則を表現できる。

\[
\Gamma_n\vdash\varphi.
\]

Context extension、revision、非単調推論、belief revision、defeasible reasoningは、Incorporated Readability更新を形式化する有効な道具を提供する。

ただし、通常の論理体系は、命題、述語、推論規則がすでに個体化された後から始まる。Gyro Sliceは、関連する命題、区別、推論対象そのものが局所的に表出可能になる過程を含み得る。したがって論理的帰結は後続可読性の有力モデルではあるが、Slice全体のモデルではない。

## 制約充足と制約伝播

制約系は、相互作用する条件から局所的configurationが徐々に表出する過程を表現できる。単純なろ過とは異なり、制約伝播は、相互制限と伝播を通じて局所的に整合した形を形成する。この点で、一部のSlice実装候補として有望である。

領域モデルでは、変数 \(V\)、定義域 \(D_V\)、制約 \(C\) を置き、局所的に利用可能なconfigurationが現れるまで伝播を行える。

ただし通常の制約モデルは、変数、定義域、制約が事前に指定されている。Gyro Structureは、その個体化以前の段階を含み得る。したがって制約伝播は、問題表現が成立した後のlocal articulation形成をモデル化できるが、Structure一般の存在論を与えるとは限らない。

## 確率と統計

確率と統計は、readability、Stability、Difference、admissibilityを不確実性のもとで表現する場合に有効である。確率的Stability score、Difference distribution、Continuity Readabilityのconfidence、Incorporated ReadabilityのBayesian revisionを支援できる。

例えば、次のような応用レベルの尺度を導入できる。

\[
P\bigl(\operatorname{Readable}(r)\mid B,c,\Sigma,\Gamma\bigr).
\]

ただし確率は、event space、sigma-algebra、または指定されたuncertainty modelを必要とする。そのようなモデルの存在は普遍的には仮定できない。確率は、表出済みモデル内部の不確実性を定量化するが、その基礎区別がSliceを通じてどのように表出するかを説明しない。

## 層に類する局所・大域構造

Sheaf-like structureは、局所的に可読なdata、重なり合うContext間の整合性、局所readingが一つの大域readingへ結合できない可能性を表現するのに有望である。局所的Stability Scene、Context依存readability、大域的非閉包を扱う形式言語となり得る。

局所sectionが個別には可読でも、全体として整合的にgluingできない場合がある。これは、局所的成立と未解決の大域Structureを分けるGyroの区別と近い。

ただしsheaf theoryは、base space、covering structure、restriction mapを必要とする。これらは特定形式領域では正当化され得るが、Gyro Logicの普遍的なpre-Slice Structureとして仮定してはならない。

## プロセス代数

プロセス代数は、interaction、concurrency、communication、choice、interruption、continuationを表現できる。Operator ResponseがContinue、Stop、Re-Slice、Defer、Jumpを選択するGyro ProcessやGyro Loopに関連する。

その強みは、実行可能かつ合成可能なprocess descriptionにある。一方、process algebraは通常、定義済みのaction vocabularyとprocess syntaxを前提とする。関連するactionとstateが表出された後のGyro Logicの操作的realizationは表現できるが、それらの表出可能性をもつStructureそのものを単独で捉えるわけではない。

## 比較の要約

比較結果は次のように整理できる。

| 数学分野 | 最も強いGyro対応 | 主な還元リスク |
|---|---|---|
| 関係構造 | Difference、Boundary、異種関係、Continuity | 対象と関係が事前に与えられる |
| グラフ／ハイパーグラフ | trace field、分岐、合流、多重関係 | グラフをTrajectoryそのものと誤認する |
| 順序理論 | 依存、関連性、部分的先行 | 比較不能なDifferenceを順序へ強制する |
| 位相 | 局所性、近傍、限定変動、一部Boundary | Stabilityを位相へ、未を開性へ還元する |
| 力学系 | 発展、収束、drift、回復 | Trajectoryを状態列へ、Stabilityを平衡へ還元する |
| 遷移系／イベント構造 | 分岐過程、因果、競合、並行 | 状態とeventを事前個体化する |
| 圏論 | 異種変換と合成 | Slice以前に始域・終域を固定する |
| 論理／証明論 | Incorporated ReadabilityとContext更新 | 命題と規則を事前表出済みとする |
| 制約伝播 | 局所的に整合したarticulation形成 | 変数と制約を事前指定する |
| 確率／統計 | 不確実性とconfidence | event spaceを事前仮定する |
| Sheaf-like structure | 局所・大域整合とgluing failure | base spaceとcoverを事前仮定する |
| プロセス代数 | 操作Loop、interaction、Response | action vocabularyを事前表出済みとする |

## 異種複合モデル

以上の比較から、Minimal Formal Modelは既存数学すべてに対抗する新分野ではなく、複数の部分モデルを調整するスキーマとして理解するのが適切である。領域固有の実装では、例えば次を組み合わせられる。

- 異種trace relationには関係構造またはハイパーグラフ
- 局所Stabilityには近傍構造または位相
- Incorporated Readabilityには論理Contextまたは非単調Context
- 操作的展開にはイベント構造またはプロセス代数
- 測定可能な応用挙動には確率モデルまたは力学モデル
- 特殊化されたモデル間の合成には圏論的道具

この複合モデルが許容される条件は、本論文で確立した区別を保持することである。便利な実装対象を提供するからという理由で、いずれかの部分モデルが不変Coreを再定義してはならない。

## 比較の結論

検討した既存数学分野のいずれも、追加仮定なしにGyro Logic全体の完全な普遍モデルを提供しない。同時に、現段階で完全に独立した新しい数学を要求する必要もない。既存分野は、その適用範囲を明示すれば、強力な部分モデルを提供する。

したがって提案スキーマの主な形式的貢献は、既存数学を置き換えることではない。どの数学モデルが適切であり、何を表現し、何を未解決のまま残すかを判断するために必要な区別を保持し、調整することにある。

次章では、具体例へスキーマを適用し、これらの区別が操作的にも理解可能なまま維持されるかを確認する。