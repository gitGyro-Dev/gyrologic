---
title: "Gyro Logicの最小形式モデル：局所的表出・Stability Scene・文脈的Tracing"
author: "Shuntaro Kawakami"
affiliation: "Independent Researcher（個人研究者）"
orcid: "0009-0004-0091-1303"
corresponding-author: "Shuntaro Kawakami"
email: "dev.jxiv@gyro-wedge.com"
date: "2026"
status: "Submission Candidate"
paper_type: "Independent formalization paper"
formal_model: "Minimal Formal Model v1"
canonical_core: "unchanged"
bibliography: "references.bib"
link-citations: true
---

**著者:** Shuntaro Kawakami  
**所属:** Independent Researcher（個人研究者）  
**ORCID:** [0009-0004-0091-1303](https://orcid.org/0009-0004-0091-1303)  
**連絡先:** [dev.jxiv@gyro-wedge.com](mailto:dev.jxiv@gyro-wedge.com)

# 要旨

Gyro Logicは、Structure・Slice・Stabilityから成る不変Coreを中心に構成される理論的枠組みである。既存の基礎論文では、このCoreの概念的役割を示し、「Gyro Logicとは何か」という基礎的な問いを扱った。本論文が扱うのは、それとは異なる形式化上の問題である。すなわち、Canonical Definitionを置き換えず、またGyro Logicを既存の単一数学分野へ早期に還元することなく、現在までに形成された概念的区別をどのように最小形式モデルとして整理できるか、という問題である。

提案モデルは、Canonical Coreを維持しながら、Sliceの過程と、その過程を通じて利用可能になるlocal articulationを分離することから始まる。局所的Gyro realizationを暫定的に、

\[
g_n=(S_n,B_n,c_n,\Sigma_n,a_n,K_n)
\]

と表す。ここで、\(S_n\) はStructure、\(B_n\) はOperator Orientation、\(c_n\) はContext、\(\Sigma_n\) はSlice process、\(a_n\) は結果として現れるlocal articulation、\(K_n\) は対応するStability Sceneである。Coreに対応する中心関係は、

\[
S_n\xRightarrow{\Sigma_{B_n,c_n}}a_n\xRightarrow{\operatorname{Stab}}K_n
\]

と表される。

Stabilityは、スカラー値、平衡、固定点、または終端条件へ還元されない。一つの表出が継続可能な成立として読めるようになりながら、なお局所的な未を残し得る構造化された局所場面として扱われる。Incorporated Readabilityは保存履歴から分離され、局所的に成立した区別、関係、基準、関連性条件が後続のrealizationで利用可能になる文脈更新として表現される。Continuity ReadabilityはIdentityから分離され、Trajectoryは状態列および時系列ログの双方から分離される。Trajectoryは、局所的Gyro realization間の許容可能な関係を文脈的にTracingすることで読まれるものとして扱われる。Differenceも、距離、数値誤差、Boundaryから分離され、Slice・Orientation・Contextに相対的で、異種の値域を取り得る構造化された関係として暫定的に型付けされる。

本論文は、提案スキーマを、関係構造、グラフ・ハイパーグラフ、順序理論、位相空間、力学系、遷移系、イベント構造、圏論、論理・証明論、制約伝播、確率・統計、Sheaf-like structure、プロセス代数と比較する。比較の結果、各分野は有効な部分モデルを提供し得る一方、現時点では、より強い前提を導入せずにGyro Logic固有の区別をすべて保持できる単一分野は確認されない。

以上から得られるMinimal Formal Modelは、Canonical Modelではなく探索的モデルである。本論文は、完全公理化、Readabilityの普遍意味論、普遍的Stability尺度、一般的Tracing algorithmを提示するものではない。その貢献は、Structure、Slice、local articulation、Stability、Incorporated Readability、Continuity Readability、Trajectory、Difference、Boundaryの区別を維持するために必要な最小限の形式的コミットメントを明らかにし、今後の検証、比較、実装研究の基盤を提示することにある。

**キーワード:** Gyro Logic、最小形式モデル、Structure、Slice、Stability、local articulation、Incorporated Readability、Continuity Readability、文脈的Trajectory、Difference、Boundary

# 1 Introduction

Gyro Logicは、次の不変Coreを中心に構成される理論的枠組みである。

```text
Structure
↓
Slice
↓
Stability
```

既存のGyro Logic基礎論文は、このCoreの概念的役割を示し、Structure・Slice・Stabilityを通じて一つの成立がどのように利用可能になるかを説明した。そこでは主として、「Gyro Logicとは何か」という問いが扱われた。本論文が扱うのは、それとは異なる問題である。すなわち、Canonical Definitionを置き換えず、またGyro Logicを既存の単一数学分野へ早期に還元することなく、現在までに形成された理論的区別をどのように最小限の形式構成として整理できるか、という問題である。

この問題が生じるのは、既存の数学的形式が、現在のGyro Logicに必要な条件よりも強い前提から出発する場合が多いためである。状態空間モデルは通常、状態とその空間が事前に与えられていることを仮定する。関数は、識別可能な定義域と終域を前提とする。グラフは、ノードと辺がすでに表現可能であることを前提とする。力学系のTrajectoryは、一般に順序づけられた状態列として表される。Stabilityは、平衡、収束、固定点、摂動に対する頑健性、またはスカラー値として表現されることが多い。Differenceも、距離、偏差、または誤差として扱われやすい。これらはいずれも有効な部分モデルとなり得るが、どの区別が保持され、どの区別が失われるかを確認しないまま、Gyro Logic全体の普遍的形式として採用することはできない。

この困難は、とりわけSliceにおいて明確になる。Canonical Definitionでは、Sliceは、Structureの中に一つの成立へ向かう道筋が開かれる過程である。この定義は、Sliceの結果が、あらかじめ完全に個体化された対象として存在し、抽出されるのを待っていることを要求しない。したがってSliceは、ろ過、射影、選択、通常の検索や取り出しから区別されなければならない。本論文では、Sliceの過程と、その過程を通じて利用可能になる局所的表出とを暫定的に分離する。局所的表出は、局所的な「こうなった」を表すが、それ自体はまだStabilityと同一ではない。

第二の困難はStabilityに関するものである。Gyro LogicにおけるStabilityは、評価者でも、意思決定者でも、最終的完了でもない。また、その理論的意味は、数値スコアや固定点だけでは尽くされない。本論文では、Stabilityを、一つの表出が継続可能な成立として読めるようになる構造化された局所場面として検討する。その場面は、確認と継続を支えられる程度に局所的には落ち着いていながら、なお未解決の局所的な未を含み得る。局所的成立と残存する未が共存することは重要である。Stability Sceneは、Structure全体の閉包を意味しない。

第三の困難は、複数の局所的realizationをまたぐ継続に関係する。一つのrealizationで読めるようになったものは、後続のrealizationが生じる条件を変化させ得る。この作用は、過去の出来事を単なる保存履歴や追記型ログとして扱うだけでは十分に表現できない。そこで本論文は、成立した区別、関係、基準、関連性条件が後続の文脈で利用可能になる仕方を表す暫定概念として、Incorporated Readabilityを導入する。同様に、Continuity ReadabilityをIdentityから分離し、Trajectoryを時系列イベント一覧および事前定義された状態列の双方から分離する。Trajectoryは、局所的Gyro realization間の許容可能な関係を文脈的に辿ることで読めるようになるものとして扱われる。

Differenceも関連する形式的問題をもつ。Gyro LogicにおけるDifferenceは、スカラー、距離的、対称的、または誤差的であるとは限らない。Orientation・Context・Sliceに応じて、部分的に定義された関係、順序構造、分布、または場に類する対象となり得る。したがってBoundaryは、Differenceそのものとは同一視されない。Boundaryは、特定のSliceのもとでDifferenceが表出し、安定化されることによって利用可能になる、派生的な可読区別として扱われる。

以上を踏まえ、本論文は最終的な公理化ではなく、探索的なMinimal Formal Modelを提示する。その目的は、Structure、Slice、local articulation、Stability、Incorporated Readability、Continuity Readability、Trajectory、Difference、Boundaryの区別を保持するために必要な、最小限の形式的コミットメントを明らかにすることにある。導入する記法は、Canonical Definitionを支える候補であり、Canonical Definitionそのものではない。本論文は不変Coreを変更せず、Gyro Logicがすでに関係構造、グラフ理論、位相空間、力学系、圏論、証明論、またはその他の一分野へ還元されたとも主張しない。

本論文は、まずContribution StatementとResearch Questionsを示す。続いて、不変Coreが形式化に課す制約を明確にし、Structure・Slice・Stabilityを順に検討する。その後、Incorporated Readability、Continuity Readability、文脈的Trajectory、Difference、Boundaryを扱い、これらを簡潔な形式スキーマへ統合する。さらに関連する数学分野との比較を行い、例示および限界の検討を通じて、本モデルが何を主張し、何を主張しないかを明確にする。

## 1.1 Contribution Statement

本論文は、Gyro Logicの最小形式モデルに向けて、主に八つの貢献を提示する。第一に、不変CoreであるStructure・Slice・Stabilityについて、Canonical Definitionを変更せず、その順序を入れ替えず、新たなCore要素も追加しないまま、暫定的な数学的型付けを与える。本論文で導入する数式表現は、Canonical Definitionを置き換える定義ではなく、それを支える形式化候補として位置づけられる。

第二に、展開中の過程としてのSliceと、その過程を通じて利用可能になる局所的表出とを分離する。この区別により、Sliceを、あらかじめ存在する結果の抽出、ろ過、選択として還元することを避ける。局所的表出は、Sliceに相対的な形で、局所的な「こうなった」が利用可能になるものとして扱われる。

第三に、Stabilityを、スカラー値、平衡点、固定点、または終端条件へ還元せず、一つの表出が継続可能な成立として読めるようになる構造化された局所場面として表現する。この表現により、局所的に読める成立と、その場面内部に残る局所的な未とが、同一のStability Sceneの中に共存できる。

第四に、Incorporated Readabilityを、保存された履歴、イベントログ、または受動的な記憶から分離する。Incorporated Readabilityは、局所的に成立した区別、関係、基準、または関連性条件が、後続のGyro realizationで利用可能になる仕方を表す。その更新は、単純な蓄積だけでなく、追加、修正、統合、重み変更、無効化、またはアクセス不能化を含み得る。

第五に、Continuity ReadabilityをIdentityから分離する。連続性は、特定のOrientation・Context・Sliceのもとで、局所的なGyro realization間の許容可能な関係を辿ることができ、その関係が接続として読める場合に成立するものとして扱う。したがって本モデルは、Identityが断たれていても連続性が読める場合と、Identityが主張されていても連続性が利用不能、不可読、または論争的である場合の双方を許容する。

第六に、Trajectoryを、状態列、時系列ログ、または蓄積された出来事そのものから分離する。Trajectoryは、局所的なGyro realization間の許容可能な関係を文脈的に辿ることで読まれるものであり、関係を保持する場やイベント集合そのものではない。この区別により、Trajectoryを単一の線形経路へ固定することなく、分岐、合流、空白、遡及的再解釈、Re-Slice、Jumpを扱える。

第七に、Differenceを、距離、数値誤差、Boundaryから分離する。Differenceは、Slice・Orientation・Contextに相対的な、非一致の構造化された関係として暫定的に扱われ、その値域は、スカラー、ベクトル、順序構造、関係、分布、部分的に定義された対象、または場に類する対象を取り得る。したがってBoundaryはDifferenceそのものではなく、Differenceが利用可能な区別として読めるようになった派生的構成として位置づけられる。

第八に、提案モデルを、関係構造、グラフ理論・ハイパーグラフ、順序理論、位相空間、力学系、遷移系、イベント構造、圏論、論理・証明論、制約伝播、確率・統計、層に類する構造、プロセス代数と比較する。この比較により、各数学分野が有効な部分モデルを与える範囲と、その前提をそのまま採用した場合にGyro Logicに必要な区別が失われる範囲を明らかにする。

以上の貢献を通じて、本論文は、不変Coreを維持したまま、Gyro Logicの探索的な統合形式スキーマを提示する。

```text
Structure
↓
Slice
↓
Stability
```

本論文は、Gyro Logicを既存の一つの数学分野へ還元できたとは主張しない。また、提案モデルが最終的またはCanonicalであるとも主張しない。本論文の貢献は、現在の理論的区別を保持するために必要な最小限の形式的コミットメントを明らかにし、今後の検証、比較、実装研究の基盤を提示することにある。

## 1.2 Research Questions

本論文の中心的な研究問いは、次のとおりである。すなわち、不変Coreを維持し、Gyro Logicの各概念を既存の数学的対象へ早期に還元することを避けながら、現在の理論を整理できる最小の形式スキーマは何か、という問いである。

**RQ1.** Structure・Slice・Stabilityに対して、Canonicalな意味を再定義せず、その順序を変更せず、新たなCore要素も追加しないまま、どのような暫定的数学型を与えられるか。この問いは、本論文における形式化の境界を定める。目的は理論定義を数式へ置き換えることではなく、三つのCore概念を一貫して区別するために必要な最小限の形式的コミットメントを明らかにすることにある。

**RQ2.** Sliceの結果となる対象や道筋がSlice以前から完全に個体化されて存在すると仮定せずに、局所的表出が利用可能になる過程としてSliceをどのように表現できるか。この問いは、展開中の過程としてのSliceと、局所的な「こうなった」として現れるSlice相対的な表出との区別を扱う。また、抽出、ろ過、射影、通常の全域関数といったモデルが、Gyro Logicに必要な条件よりも強い前提を導入していないかを検討する。

**RQ3.** 同一の場面に未解決の局所的な未を残しながら、局所的に可読かつ継続可能な成立をStabilityとしてどのように表現できるか。この問いは、Stabilityをスカラー値、平衡、固定点、または終端状態へ還元せず、構造化された局所場面として表せるかを検討する。さらに、局所的表出、可読な関係、残存する未、利用可能な継続条件を表現するために必要な最小構成要素を問う。

**RQ4.** 一つの局所的Gyro realizationを通じて獲得された可読性が、保存された履歴、受動的記憶、または単調な蓄積へ還元されることなく、後続のrealizationの条件をどのように変化させ得るか。この問いは、Incorporated Readabilityを、追加、修正、統合、重み変更、無効化、または既存の可読性のアクセス不能化を含み得る文脈更新として形式化する動機を与える。

**RQ5.** 連続性およびTrajectoryを、Identity、あらかじめ定められた状態列、または時系列ログによってではなく、許容可能な関係の文脈的Tracingとしてどのように表現できるか。この問いは、関係の存在、その関係を辿れること、そして特定のOrientation・Context・Sliceのもとで連続性として読めることを分離する。また、Trajectoryを一つの線形経路へ固定せず、分岐、合流、空白、遡及的再解釈、Re-Slice、Jumpを表現可能なまま保持する方法を問う。

**RQ6.** 提案する形式スキーマに対して、どの既存数学分野が有効な部分モデルを与え、どの時点でその前提がGyro Logicにとって過度に制約的となるか。この問いでは、関係構造、グラフ・ハイパーグラフ、順序理論、位相空間、力学系、遷移系、イベント構造、圏論、論理・証明論、制約伝播、確率・統計、層に類する構造、プロセス代数を比較する。目的は最終的な基礎分野を一つ選ぶことではなく、各分野がGyro Logicのどの部分を表現でき、早期の還元によってどの区別が失われるかを明らかにすることにある。

以上の問いは、本論文の範囲を共同で定める。本論文は、Gyro Logicを完全に公理化できるか、または単一の数学分野へ還元できるかを問うものではない。現在の理論で形成された区別を維持し、その後の検証、比較、実装研究を支え得る、最小限で内部整合的かつ明示的に暫定的な形式構成を提示できるかを問うものである。

# 2 不変Coreと形式化制約

## 2.1 不変Core

本論文で構築する形式モデルは、Gyro Logicの次の不変Coreによって制約される。

```text
Structure
↓
Slice
↓
Stability
```

このCoreの順序と構成は、本研究における可変要素ではない。Core要素間に新たな概念を挿入せず、派生概念を第四のCore要素へ昇格させない。Orientation、Context、local articulation、Incorporated Readability、Continuity Readability、Trajectory、Difference、Boundary、Operator Response、Re-Slice、Jumpは、条件、結果、関係、時間、または解釈に関わる概念として扱う。これらは局所的Gyro realizationの形式記述を精緻化し得るが、不変Coreそのものを置き換えたり拡張したりするものではない。

Canonical Definitionは変更せず、次のとおり維持する。

> **Structureとは、何かが成立し得る様式である。**

> **Sliceとは、Structureの中に、一つの成立へ向かう道筋が開かれる過程である。**

> **Stabilityとは、開かれた道筋が、一つの成立として継続可能な状態である。**

これらの定義は、以降で提案するすべての数式表現に優先する。形式化候補がCanonical Definitionと衝突する意味を含意する場合、修正または棄却されるべきなのは形式化候補であり、数学的対象へ合わせてCanonical Definitionを変更してはならない。

## 2.2 Canonical Definitionと形式化候補

本論文は、二種類の記述レベルを区別する。Canonical DefinitionはGyro Logic概念の理論的意味を規定する。形式化候補は、その意味の一部を保持し得る暫定的な数学的構成を示す。両者の関係は同一ではない。

```text
Canonical Definition
≠
形式化候補
```

本論文の数式は、定義を置き換えるものではなく、規律ある表現上の提案として読まれなければならない。例えば、Structureを \(S_n\)、Slice processを \(\Sigma_n\)、Stability Sceneを \(K_n\) と表すことは、モデルに必要な識別子と関係を導入することを意味するにすぎない。Structureが本質的に集合の要素であること、Sliceが通常の全域関数であること、Stabilityがあらゆるrealizationにおいてタプルであることを確定するものではない。

この分離が必要なのは、数学記法が暗黙に存在論的コミットメントを追加し得るためである。関数は固定された定義域と終域を含意し得る。グラフは事前に個体化されたノードと辺を含意し得る。距離は数値比較可能性、対称性、三角不等式を含意し得る。状態Trajectoryは、定義済みの状態空間と時間順序を含意し得る。したがって形式モデルは、各記法が何を前提とし、何を意図的に未確定のまま残すかを明示しなければならない。

## 2.3 最小限の形式的コミットメント

提案モデルは、次の最小限のコミットメントのみを採用する。

第一に、分析のために局所的Gyro realizationを区別できるものとする。これは、現実が本質的に独立した単位へ分割されていることを要求しない。局所的realizationを暫定的に参照し、他のrealizationとの関係を記述できることのみを要求する。

第二に、Sliceと、Sliceを通じて利用可能になるlocal articulationを区別する。展開中の過程と、その過程から局所的に利用可能になった表出とは同一ではない。

第三に、StabilityをSlice processおよびlocal articulationの双方から区別する。Stabilityは表出が現れたこと自体ではなく、その表出が成立として可読かつ継続可能になることに関わる。

第四に、一つの局所的realizationで成立した可読性は、後続のrealizationを条件づけ得るものとする。その条件づけが決定論的、単調、完全、または時間的に直近であることは要求しない。

第五に、局所的realization間に関係が存在していても、すべてのOrientation・Context・Sliceのもとで連続性として読めるとは限らないものとする。したがって、関係の存在、追跡可能性、Continuity Readabilityを区別する。

第六に、Differenceは、普遍的にスカラー、距離的、対称的、全域的、または誤差的であると仮定せずに表現できるものとする。

以上のコミットメントによって、Structureの数学型、関係場、文脈更新、Tracing operationを後続の特殊化へ開いたまま、最小形式スキーマを構築できる。

## 2.4 形式化制約

形式化候補は、少なくとも次の制約を満たす場合にのみ採用可能である。

**Core保存。** Structure・Slice・Stabilityの順序と構成を維持し、代替Coreを導入しない。

**定義保存。** Canonical Conceptを、より狭い数学的特殊例によって再定義しない。

**過程と結果の分離。** 展開中のSlice processと、その過程を通じて利用可能になるlocal articulationを区別する。

**表出とStabilityの分離。** local articulationが現れても、それがすでにStabilityとして可読かつ継続可能であるとは仮定しない。

**全体閉包を伴わない局所性。** 局所的なStability Sceneが成立していても、Structure全体は開かれたままであり、場面内部に未解決の局所的な未を残し得る。

**非還元的な可読性更新。** Incorporated Readabilityを、追記型履歴または不変の保存データへ還元しない。

**Identityと連続性の分離。** Identityを伴わないContinuity Readabilityと、可読な連続性を伴わないIdentity主張の双方を許容する。

**Trajectoryと状態列の分離。** Trajectoryを、時系列ログ、イベント集合、または一つの事前定義された線形状態列と同一視しない。

**Differenceと距離の分離。** Differenceに距離または誤差モデルの条件を必須としない。

**Layer整合性。** 本モデルをGyro Logicの理論モデルとして維持する。GyroOSの実装判断とGyroAuthの応用要件はモデルを具体化し得るが、理論概念を再定義してはならない。

## 2.5 明示的に仮定しないこと

Minimal Formal Modelは、Structureが一つの固定された数学的対象型であること、関連するすべての対象・状態・関係・BoundaryがSlice以前に個体化されていること、Sliceが決定論的または全域的な関数であること、Stabilityがスカラー閾値・平衡・固定点であること、可読性が単調に蓄積すること、ContinuityがIdentityを含意すること、Trajectoryが線形であること、Differenceが距離であること、既存の一つの数学分野がGyro Logicの完全な基礎を与えることを仮定しない。

これらの非仮定は、そのような数学的構成の有用性を否定するものではない。その位置づけを限定するものである。距離、グラフ、力学系、圏、証明文脈、遷移系は、それぞれの前提が正当化される特定領域において具体的モデルとなり得る。しかし本論文は、そのような一つの具体化を理論全体の普遍的形式へ昇格させない。

不変Coreと以上の制約は、後続各章の許容設計空間を定める。次章ではStructureを扱い、それを状態、物体、空間、関係、その他の一つの数学型へ固定する前に、形式的に何をコミットできるかを検討する。

# 3 固定された数学型をもたない成立可能性としてのStructure

## 3.1 Canonicalな意味と形式化上の問題

StructureのCanonical Definitionは、次のとおりである。

> **Structureとは、何かが成立し得る様式である。**

この定義は、Structureを状態、物体、集合、空間、関係、容器、基盤、構成のいずれか一つと同一視しない。これらはいずれも、特定領域では有効な表現となり得るが、本論文ではStructureの普遍的な数学型として採用しない。したがって形式化上の問題は、Structureが既存数学のどの対象で「本当はあるか」を決定することではない。特定の数学型へ特殊化する前に、どのような最小限のコミットメントを置けるかを明らかにすることである。

この区別が重要なのは、通常の数学的モデリングが、対象、状態、変数、関係がすでに個体化された後から開始されることが多いためである。Gyro Logicは、それらがすべて固定される以前にも、Sliceを通じて何かが局所的に表出可能となる形式条件を扱う必要がある。したがってStructureは、成立済みの対象一覧ではなく、成立可能性を担う組織として暫定的に捉える。この表現は作業上の特徴づけであり、Canonical Definitionを置き換えるものではない。

## 3.2 Structureは現在状態ではない

現在状態はStructureの中で表現され得るが、その状態は、状態の成立を可能にするStructureそのものではない。ある記述のもとで現在利用可能な状態を \(x_n\) とする。Minimal Formal Modelは、次を同一視しない。

\[
S_n = x_n.
\]

代わりに、状態がStructureに相対的に成立可能であることだけを要求する。

\[
x_n \triangleleft S_n,
\]

ここで \(\triangleleft\) は、成立利用可能性を表す暫定的な関係である。この記法は、適切な条件のもとで \(x_n\) が \(S_n\) に相対的に成立済み、表出可能、または利用可能として扱えることを意味する。領域固有モデルが明示的に定めない限り、集合への所属、物理的包含、論理的含意、部分全体関係を意味しない。

この区別により、同一のStructureから異なる状態が利用可能となること、現在状態が変化してもStructure全体を完全に独立した対象として置き換える必要がないことを許容できる。逆に、見かけ上同じ状態を示す二つの記述であっても、その状態が成立するStructureは異なり得る。

## 3.3 Structureは担体や対象ではない

局所的realizationが生じる実体、素材、システム、文書、制度、過程を、そのrealizationの担体と呼ぶことができる。しかし担体もStructureと同一ではない。ケーキ、ソフトウェアシステム、法制度、認証セッションは例示における担体となり得るが、それらのStructureは、区別、関係、状態、成立可能性がどのような様式で利用可能になるかに関わる。

これにより、次の存在論的な潰れを避ける。

```text
担体
=
Structure
=
現在状態
```

同一の担体が異なる条件のもとで複数のStructureを支える場合もあり、複数の担体が一つの関係的Structureへ参加する場合もある。同様に、担体が持続しながら現在状態が変化する場合や、担体の物質的または記述的構成が変化してもStructureが継続する場合も排除しない。これらを普遍的に主張するのではなく、モデルが事前に否定しないということである。

## 3.4 全体としての未としてのStructure

Slice以前のStructureは、全体としての未によって特徴づけられる。この未は、不在、無、無知、空の可能性集合を意味しない。特定のSliceを通じて表出される局所的成立が、まだその形では利用可能になっていないことを意味する。したがって全体としての未は、後に読めるものすべてが存在しないということではなく、予定されるSliceに相対的な表出の未成立に関わる。

\(\mathcal{A}^{*}(S_n)\) を、\(S_n\) から利用可能になり得る表出の族を示す暫定記法とする。ただし、それらがすでに完全に個体化された対象であるとは主張しない。アスタリスクは、この非コミットメントを示す。

\[
a \in \mathcal{A}^{*}(S_n)
\]

この記法は、特殊化されたモデルが正当化しない限り、通常の集合所属として読んではならない。表出 \(a\) が、適切なSliceを通じて \(S_n\) と両立し、\(S_n\) によって支えられ、または \(S_n\) から実現可能であることだけを示す。

重要なのは、\(\mathcal{A}^{*}(S_n)\) が、選択されるのを待つ既存回答の一覧ではないことである。これは、Slice以前には未決定のまま残る成立可能性を表すためのplaceholderである。特に、候補表出がすべて列挙可能、相互排他的、同時に利用可能、またはOrientationとContextを越えて不変であることを要求しない。

## 3.5 最小限の関係的特徴づけ

Structureは、暫定的に次の関係スキーマで参照できる。

\[
S_n = \langle \mathsf{Avail}_n,\mathsf{Rel}_n,\mathsf{Cond}_n \rangle^{*},
\]

ここで、

- \(\mathsf{Avail}_n\) は、局所的成立として利用可能になり得るものを表す。
- \(\mathsf{Rel}_n\) は、その成立を支え、制約し、または接続し得る関係を表す。
- \(\mathsf{Cond}_n\) は、利用可能性または関係が関連性をもつ条件を表す。
- 上付きの \(^*\) は、これを普遍的なタプル存在論として採用しないことを示す。

このスキーマは、状態空間、グラフ、制約系、位相空間よりも意図的に弱い。各成分が完全、明示的、相互独立、直接観測可能であることを要求しない。Structureが、Sliceを局所的表出へ向かわせるために十分な利用可能性、関係、条件づけの組合せを支えることだけを述べる。

さらに弱い関係形式として、次を置ける。

\[
\mathsf{Establishable}(a;S_n,B_n,c_n),
\]

これは、表出 \(a\) がOrientation \(B_n\) とContext \(c_n\) に相対的にStructure \(S_n\) から局所的に利用可能になり得ることを意味する。この述語は、\(a\) がSlice以前から与えられていること、必ず現れること、Stabilityへ至ることを述べない。局所的成立の可能性と両立することだけを示す。

## 3.6 OrientationとContextはStructureを構成しない

OrientationとContextは、Structureのどの側面がSliceにとって関連するかを条件づける。しかしStructureを、Operatorが現在見ているものそのものとして定義してはならない。そうするとStructureは視点相対的な表象へ潰れ、その表象を制約し、抵抗し、または超えることができなくなる。

したがって、

\[
S_n \neq S_n(B_n,c_n)
\]

を、StructureとOrientation条件付きの見え方を同一視しないための注意として保持する。特殊化されたモデルは、次のようなアクセス可能な呈示を定義してもよい。

\[
\operatorname{Pres}_{B_n,c_n}(S_n),
\]

ただし、その呈示が \(S_n\) を尽くすとは仮定しない。これにより、別のOrientationやContextでは読めなかった区別がSliceによって顕在化、生成、安定化される場合でも、より広い同一Structureを通じて生じたものとして扱える。

## 3.7 局所的成立はStructureを閉じない

Sliceによってlocal articulationが現れ、それがStableになっても、その局所的成立はStructure全体を閉じない。形式的には、

\[
S_n \xRightarrow{\Sigma_{B_n,c_n}} a_n
\]

が成立し、Stability Scene \(K_n\) が利用可能となっても、次を導かない。

\[
\mathcal{A}^{*}(S_n)=\{a_n\}
\]

または、

\[
S_n \text{ は完了している}.
\]

一つの局所的realizationは一つの表出を落ち着かせ得るが、他の関係、区別、成立可能性を未解決のまま残す。また後続Structureには、そのrealizationを通じて成立した可読性が織り込まれ得るため、継続は同一初期条件の単純な反復ではない。

## 3.8 形式的コミットメントと非コミットメント

Minimal Formal ModelのStructure部分は、次をコミットする。Structureは局所的に参照できる。成立可能性を支える。現在状態および担体から区別される。どの表出が利用可能になるかを制約し得る。そして、いかなる一つの局所的成立を越えても開かれたままである。

一方、本モデルは、Structureが集合、多様体、圏、グラフ、状態空間、確率空間、制約系、論理理論、物理的基盤であるとは確定しない。またStructureが直接観測可能、完全列挙可能、時間的に静的、内部的に均質、または過去のIncorporated Readabilityから独立しているとも仮定しない。これらの強いコミットメントは、正当化される特殊化モデルでのみ採用できる。

この最小限の扱いによって、Coreの次の段階へ進む準備が整う。Structureは何かが成立し得る様式を与えるが、一つのlocal articulationがどのように利用可能になるかを、それ自体では説明しない。その移行はSliceに属する。Sliceは、結果があらかじめ完成した対象として存在すると仮定せず、過程として表現されなければならない。

# 4 過程および局所的表出としてのSlice

## 4.1 Canonical Definition

SliceのCanonical Definitionは変更せず、次のとおり維持する。

> **Sliceとは、Structureの中に、一つの成立へ向かう道筋が開かれる過程である。**

この定義は、形式化に対して二つの直接的な制約を課す。第一に、Sliceは完了した対象ではなく、過程である。第二に、成立へ向かう道筋は、その過程を通じて開かれるのであり、必ずしもSlice以前から完全に個体化された対象として存在し、抽出されるのを待っているとは限らない。

したがって本モデルは、Sliceを、結果空間があらかじめ確定している操作と区別する。ろ過、射影、選択、検索、分割、通常の抽出は、特定領域におけるSliceの実装となり得るが、いずれもSliceの普遍的意味としては採用しない。

## 4.2 抽出モデルが不十分である理由

抽出モデルは、模式的には次のように書ける。

\[
E : S \to X
\]

ここでは、Structure \(S\) から、あらかじめ定義された終域 \(X\) に属する要素または表現が得られる。このモデルは、結果型が事前に分かっている場合には有効である。しかし、現在のGyro Logicが必要とする条件よりも強い前提を導入し得る。例えば、出力がすでに個体化されていること、終域が固定されていること、関連する区別が事前に利用可能であること、あるいは操作が単に既存要素を露出させるだけであることを含意し得る。

Gyro Logicは、一部のSliceが抽出として実装され得ることを否定しない。否定するのは、抽出がSliceの理論的意味を尽くすという主張である。一般的なSliceでは、利用可能になる局所的な形そのものが、過程を通じて構成され得る。問題は、どの既存要素を選ぶかだけではなく、局所的表出がどのように成立候補として利用可能になるかにある。

この区別は、次のように要約できる。

```text
Slice
≠
すでに完成している結果の抽出
```

また、

```text
道筋が開かれること
≠
既存の道筋オブジェクトの取得
```

である。

## 4.3 Slice processとlocal articulation

局所的Structureを \(S_n\)、Operator Orientationを \(B_n\)、Contextを \(c_n\)、Slice processを \(\Sigma_n\) とする。暫定的な形式関係を次のように書く。

\[
S_n
\xRightarrow{\Sigma_{B_n,c_n}}
a_n
\]

ここで \(a_n\) は、Sliceを通じて利用可能になるlocal articulationを表す。

記号 \(\xRightarrow{}\) は、通常の全域関数と意図的に同一視しない。これは、結果が部分的、文脈依存的、非決定論的、遡及的にのみ可読、または別のOrientationでは利用不能となり得る過程関係を表す。したがって、この記法がコミットするのは、次の点に限られる。

1. 局所的Structureが関与すること
2. SliceがOrientationとContextのもとで展開すること
3. その展開を通じてlocal articulationが利用可能になり得ること
4. articulationと、それを利用可能にした過程とを区別できること

\(a_n\) は、局所的な「こうなった」を表す。これは最終完了、全体閉包、またはStabilityそのものを意味しない。後続で可読かつ継続可能な成立として評価され得る、局所的に利用可能な形である。

したがって、

```text
Slice process
≠
local articulation
```

であり、さらに、

```text
local articulation
≠
Stability
```

である。

## 4.4 slice-ingとslice-done

Gyro Logicは、Sliceが展開している時間を含む過程と、その展開から局所的結果が利用可能になった状態を区別する。

```text
slice-ing
=
Sliceが進行している過程
```

```text
slice-done
=
local articulationが利用可能になった時点
```

本モデルにおいて、slice-doneは、articulationがすでに安定していること、完全に検証されていること、Structure全体が閉じていること、または永久に保持されることを意味しない。Sliceが、局所的に表現可能な「こうなった」へ到達したことだけを意味する。Stabilityは、そのarticulationが継続可能な成立として読めるかに関わる。

暫定的な過程表現として、次を置ける。

\[
\alpha_{\Sigma} : I_{\Sigma} \to \mathcal{A}^{*}(S_n)
\]

かつ、

\[
a_n = \alpha_{\Sigma}(\tau^{*})
\]

ここで、\(I_{\Sigma}\) は内部的な過程指標、\(\mathcal{A}^{*}(S_n)\) は可能なlocal articulationの暫定的な空間、\(\tau^{*}\) は一つのarticulationが利用可能になる時点を表す。ただし、この記法は例示的でありCanonicalではない。物理時間、唯一の終端指標、または全領域で共通する固定articulation空間を要求しない。

より一般的な解釈は、関係形式として維持される。

\[
(S_n,B_n,c_n,\Sigma_n) \leadsto a_n
\]

Slice processが分散的、部分的にしか観測できない、非決定論的、または遡及的にのみ区別可能である場合、この形式の方が適している。

## 4.5 OrientationとContextの役割

OrientationとContextはSliceを条件づけるが、新たなCore要素として挿入されるものではない。OrientationはStructureへの方向的な入口を与える。Contextは、どの関係、区別、articulationが利用可能になり得るかに影響する周辺条件を与える。

添字付き記法

\[
\Sigma_{B_n,c_n}
\]

は、この条件づけを表す。ただし、Structure自体がOperatorによって作られることや、Structureのすべての側面が一人の観測者に相対的であることを意味しない。同じStructureが、異なるOrientationとContextのもとで異なるSlice processを許容し、それぞれ異なるlocal articulationを与え得る。

したがって一般に、

\[
\Sigma_{B_1,c_1}(S)
\not\equiv
\Sigma_{B_2,c_2}(S)
\]

である。

この差異は、一方のSliceが必ず真で他方が偽であることを意味しない。成立へ向かう道筋が開かれる条件に応じて、Slice相対的なarticulationが異なり得ることを示す。

## 4.6 SliceはStructureを消費しない

Sliceの過程は、Structureが使い尽くされること、消費されること、または前景だけが残って背景が失われるように分割されることを意味しない。高度に確定したarticulationが現れた場合でも、Structureには別の関係、可能なarticulation、未解決条件、代替経路が残り得る。

したがって、

```text
Slice後のStructure
≠
Structureから結果を差し引いたもの
```

である。

Sliceは、特に可読性が後続文脈へ織り込まれる場合、後にStructureへ接近する条件を変化させ得る。しかし、その変化を文字どおりの減算と混同してはならない。また、Structureに生じるすべての変化をSliceへ帰属させてもならない。外部相互作用、環境変化、物質変換、その他の過程も、後続realizationの条件を変化させ得る。

## 4.7 局所性と非閉包

local articulationは、少なくとも三つの意味で局所的である。第一に、realizationに関与するStructureの範囲に局所的である。第二に、OrientationとContextに局所的である。第三に、特定の成立へ向かって開かれた道筋に局所的である。これらの局所性は、Structureの残余が無関係または不存在になることを意味しない。

したがって本モデルは、

\[
a_n \text{ が利用可能である}
\]

一方で、

\[
S_n \text{ は全体として開かれたままである}
\]

ことを許容する。

これは、後続のRe-Slice、代替articulation、Contextの拡張、Differenceの認識、後のTrajectory tracingに必要である。

## 4.8 Sliceに関する最小限の形式的コミットメント

本論文は、Sliceについて次の点にコミットする。

第一に、Sliceは過程的であり、静的な写像結果だけと同一視できない。

第二に、過程とlocal articulationを区別できる。

第三に、local articulationは、Slice以前から完全に個体化された対象として存在している必要はない。

第四に、OrientationとContextはSliceを条件づけるが、新たなCore段階にはならない。

第五に、local articulationの出現はStabilityを含意しない。

第六に、Sliceは必ずしもStructureを消費または閉包しない。

第七に、抽出、射影、ろ過、分類、選択は領域固有の実装となり得るが、Sliceを普遍的には定義しない。

## 4.9 明示的にコミットしないこと

本モデルは、すべてのSliceが一意の結果をもつこと、すべてのSliceが終了すること、Sliceが決定論的であること、articulation空間が事前に固定されること、Orientationが人間の観測者に属すること、Contextが完全に表現可能であること、slice-doneが不可逆であることを主張しない。

また、「道筋が開かれる」という表現が、文字どおりの幾何学的経路を意味するとも主張しない。道筋は、関係的、論理的、手続的、意味的、因果的、物質的、制度的、その他の領域固有の形を取り得る。形式モデルは、path-openingの構造的役割を保持しつつ、その具体化を開いたままにする。

## 4.10 Stabilityへの接続

local articulation \(a_n\) は、次の形式的区別に必要な結果を与えるが、まだStability Sceneではない。articulationからStabilityへの移行では、そのarticulationが、関連するStructure・Orientation・Contextのもとで、継続可能な成立として読めるかを問う。

暫定的には、

\[
K_n
=
\mathsf{StabScene}(a_n;S_n,B_n,c_n)
\]

と書く。

次章では、この関係を検討し、Stabilityをスカラー、固定点、終端条件ではなく、構造化された局所場面として展開する。

# 5 可読かつ継続可能な局所場面としてのStability

## 5.1 Canonicalな意味

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

## 5.2 スカラーだけでは十分でない理由

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

## 5.3 平衡と固定点は部分モデルである

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

## 5.4 構造化された局所場面としてのStability

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

## 5.5 可読性と継続可能性

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

## 5.6 残存する未

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

## 5.7 局所性と近傍解釈

Stabilityは、孤立点よりも局所場面または近傍として表す方が適切である。近傍構造が正当化される応用では、次のように書ける。

\[
K_n \subseteq N(a_n)
\]

ここで\(N(a_n)\)は、許容可能な変動範囲のもとで、表出が可読かつ継続可能であり続ける近傍である。

この記法は頑健性分析を支え得るが、Gyro Logicを位相空間へ普遍的に還元するものではない。近傍は、位相的、関係的、意味論的、運用的、確率的、または領域固有の構造であり得る。

本質的なコミットメントは、特定の近傍公理ではなく、可読性と継続可能性の局所的持続である。

## 5.8 Stabilityは判断しない

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

## 5.9 Stabilityと後続Structure

Stability Sceneは、同一の形のまま移送されることなく、後続Structureで利用可能になり得る。その可読な区別、関係、継続条件は、後続Contextで織り込まれ、修正され、重みづけされ、無効化され、またはアクセス不能になり得る。

弱い遷移候補として、次を置く。

\[
K_n
\rightsquigarrow
q_n
\rightsquigarrow
\Gamma_{n+1}
\]

ここで\(q_n\)は局所的realizationから織り込まれるものを表し、\(\Gamma_{n+1}\)は後続のreadability contextを表す。この遷移は、次章のIncorporated Readabilityで詳しく扱う。

ここで重要なのは、Stabilityが終端でも受動的な保存結果でもないことである。Stabilityは、後に何が可能、関連的、または追跡可能になるかを条件づけ得る、局所的に可読かつ継続可能な場面である。

## 5.10 最小限の形式的コミットメント

Stabilityモデルは、次の点にのみコミットする。

1. StabilityはSliceおよびlocal articulationから区別される。
2. Stabilityは局所的可読性と継続支援を必要とする。
3. Stabilityは一つのスカラーでは表現できない内部構造を持ち得る。
4. Stabilityは残存する局所的な未と共存し得る。
5. Stabilityは局所的であり、Structure全体を閉じない。
6. Stabilityは運用上の判断を行わない。
7. Stability SceneはIncorporated Readabilityを通じて後続realizationを条件づけ得る。

本モデルは、Stabilityが常にタプル、スカラー、平衡、固定点、アトラクタ、不変集合、確率、または二値述語であるとは仮定しない。これらはそれぞれ、特定領域で正当化される特殊化となり得る。

## 5.11 Incorporated Readabilityへの接続

一つの表出がStability Sceneとして可読かつ継続可能になった後、その可読性の一部は後続realizationで利用可能になり得る。持続するものは、出来事、状態、場面の全体とは限らず、不変の記録として保存される必要もない。次章では、この作用を単純な履歴保存ではなく、Context更新としてのIncorporated Readabilityとして検討する。

# 6 Incorporated ReadabilityとContext更新

## 6.1 局所的Stabilityから後続条件へ

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

## 6.2 Incorporated Readabilityは保存履歴ではない

保存履歴は、何かが起きたことを記録する。Incorporated Readabilityは、何が後続の成立に利用可能になったかに関わる。したがって、次の区別が必要である。

```text
先行realizationの履歴
≠
後続realizationで利用可能な可読性
```

ログは、ある出来事を保存していても、その出来事が後続解釈へ影響しない場合がある。反対に、織り込まれた区別は、元の出来事が明示的な記録として利用できなくなっていても、後続解釈を変化させ得る。したがってIncorporated Readabilityは、追記型保存、受動的記憶、時系列蓄積へ還元できない。

イベント履歴 \(H_n\) とreadability context \(\Gamma_n\) を分けると、この違いは次のように表せる。

\[
H_{n+1}=\operatorname{Append}(H_n,g_n),
\]

一方で、

\[
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n).
\]

前者は出来事の発生を記録する。後者は、後続の読解、比較、Orientation、成立に利用可能な条件を変化させる。どちらか一方が生じても、他方が完全に生じるとは限らない。

## 6.3 利用可能な可読性条件としてのContext

\(\Gamma_n\) は、暫定的なreadability contextを表す。これは、すべての領域で固定された命題集合として理解されるべきではない。realizationに応じて、次のような内容を保持または編成し得る。

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

## 6.4 非単調な更新

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

## 6.5 Weighted Incorporated Readability

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

## 6.6 Structure更新

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

## 6.7 例：数学的推論

数学の問題を解く過程では、最終証明が完成する前に、定義、補題、中間等式、許容可能な変形が一度成立する場合がある。それらは成立後、後続の推論で利用可能になる。これは、ある手順が起きたという履歴が保存されるだけではない。後続の推論が正当に利用できるものを変化させる。

例えば、局所的結果 \(q_n\) が \(\Gamma_n\) のもとで成立したなら、後続推論は次のContextで進み得る。

\[
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n).
\]

後の訂正によって \(q_n\) が修正または無効化されれば、有効なContextも再び変化する。したがって本モデルは、織り込みと撤回の双方を許容する。

## 6.8 最小限のコミットメント

本モデルがコミットするのは、次の点に限られる。

第一に、局所的Gyro realizationは、何らかの可読性を後続realizationで利用可能にし得る。

第二に、織り込まれるものは、先行realization全体と同一ではない。

第三に、Incorporated Readabilityは、保存履歴へ還元されることなく後続条件を変化させ得る。

第四に、その更新は非単調かつContext相対的であり得る。

第五に、外的変化は、局所的Gyro realizationを通じた変化と形式的に区別されなければならない。

本モデルは、\(\Gamma_n\) が常に論理理論、データベース、記憶装置、ベクトル状態、確率分布であるとは仮定しない。それらは、前提が正当化される領域において有効な具体化となり得る。

## 6.9 Continuity Readabilityへの接続

Incorporated Readabilityは、局所的成立がどのように後続条件で利用可能になるかを説明する。しかし、それだけでは二つの局所的realizationが接続していると読めるかは決まらない。そのためには、関係が存在すること、その関係を辿れること、そして連続性として読めることを分離しなければならない。次章では、この区別をContinuity Readabilityとして扱う。

# 7 Continuity ReadabilityとIdentity

## 7.1 局所的成立から関係的連続性へ

前章では、Incorporated Readabilityを、一つの局所的Gyro realizationで成立した区別、関係、基準、関連性条件が、後続のrealizationで利用可能になるためのContext更新として導入した。この更新によって、後続の比較やTracingが可能になる。しかし、それだけで二つのrealizationの間に連続性が成立したとはいえない。関係は存在していても追跡できない場合があり、追跡できる関係であっても、特定のOrientation・Context・Sliceのもとで連続性として読めない場合がある。

したがってGyro Logicでは、少なくとも次の三つを区別する。

```text
関係の存在
≠
追跡可能性
≠
Continuity Readability
```

この区別が必要なのは、連続性を二つのrealizationが自動的に保持する内在的属性として扱わないためである。連続性は、特定の条件のもとで利用可能になる関係的な可読性である。

## 7.2 局所的Gyro realization

局所的なGyro realizationを、暫定的に次のように表す。

\[
g_i=(S_i,B_i,c_i,\Sigma_i,a_i,K_i)
\]

ここで、

- \(S_i\) は当該realizationに関わるStructure、
- \(B_i\) はOperator Orientation、
- \(c_i\) はContext、
- \(\Sigma_i\) はSlice process、
- \(a_i\) はSliceを通じて利用可能になったlocal articulation、
- \(K_i\) は対応するStability Scene

を表す。

このタプルは形式分析のための記述スキーマである。すべてのGyro realizationが本質的に六つの独立対象へ分解されていることを意味しない。

## 7.3 関係の存在

二つの局所的realization \(g_i\) と \(g_j\) の間の関係候補を \(r\) とする。次のように書ける。

\[
r(g_i,g_j)
\]

または、より明示的に、

\[
g_i \xrightarrow{r} g_j
\]

と書く。

関係 \(r\) の型は、領域相対的なものとして意図的に未固定とする。例えば、次のようなものが含まれ得る。

```text
因果的継起
機能的継起
意味的継承
物質的移行
認識されたDifference pattern
Boundary correspondence
ResponseとOrientationの接続
保持された可読性条件
制度的・規則的接続
```

このような関係が存在していても、現在の形式条件のもとで追跡可能であるとは限らない。

## 7.4 Traceability

Traceabilityは、一つのrealizationから別のrealizationへ関係を辿れるかに関わる。暫定的な述語として、次を置く。

\[
\operatorname{Traceable}(g_i,g_j;r)
\]

追跡可能性は、利用可能な証拠、Incorporated Readability、時間的到達可能性、許容された推論規則、アクセス条件などに依存し得る。関係そのものは存在していても、その中間Structureが欠けている、利用不能である、不可読である、またはまだ表出していない場合には、追跡できないことがある。

したがって、

\[
r(g_i,g_j)
\not\Rightarrow
\operatorname{Traceable}(g_i,g_j;r)
\]

である。

Traceabilityは、単なる関係の存在より強いが、Continuity Readabilityよりは弱い。

## 7.5 Admissibility

追跡可能な関係が、すべて連続性に関係するとは限らない。関係は、連続性を読むために用いられるOrientation・Context・Sliceのもとで許容可能でなければならない。

\[
\operatorname{Adm}(r;B,c,\Sigma,\Gamma)
\]

を、関係 \(r\) がOrientation \(B\)、Context \(c\)、連続性を読むためのSlice \(\Sigma\)、およびIncorporated Readability Context \(\Gamma\) に相対的に許容可能であることを表すものとする。

Admissibilityには、例えば次の条件が含まれ得る。

```text
関連性
適用範囲
許容された推論
因果的十分性
意味的両立性
物質的連続性
制度的妥当性
時間的アクセス可能性
信頼・証拠要件
```

Admissibilityは、あらゆる領域で普遍的、静的、または二値的であるとは仮定しない。段階的、反証可能、修正可能、または論争的であり得る。

## 7.6 Continuity Readability

Continuity Readabilityを、Admissibility・Traceability・Readabilityの結合として暫定的に表す。

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma)
\]

候補条件は次である。

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma)
\iff
\exists r\,
\Bigl(
\operatorname{Adm}(r;B,c,\Sigma,\Gamma)
\land
\operatorname{Traceable}(g_i,g_j;r)
\land
\operatorname{Readable}(r;B,c,\Sigma,\Gamma)
\Bigr)
\]

この式は、次の三つの問いを分離する。

```text
許容可能な関係があるか
その関係を辿れるか
その関係を、ここで連続性として読めるか
```

最後の条件が重要である。関係が許容可能かつ追跡可能であっても、必要な区別、基準、Context上の組織化がまだ利用可能でなければ、現在の時点では連続性として読めないことがある。

## 7.7 Context相対的なContinuity Readability

Continuity Readabilityは、あらゆる読み方に対して普遍的ではない。同じ二つのrealizationであっても、一つのOrientationでは連続的に読まれ、別のOrientationでは非連続または未確定として読まれ得る。

\[
\operatorname{CR}(g_i,g_j;B_1,c_1,\Sigma_1,\Gamma_1)
\neq
\operatorname{CR}(g_i,g_j;B_2,c_2,\Sigma_2,\Gamma_2)
\]

これは連続性が恣意的であることを意味しない。どの関係が許容可能であり、どのように読めるかが、明示された条件に依存することを意味する。

後続のRe-Sliceによって、以前は不可読だった関係が可視化される場合がある。逆に、以前受け入れられていた関係が棄却されたり、連続性の読みが再構成されたりする場合もある。したがってContinuity Readabilityは、無制約ではないまま修正可能である。

## 7.8 Identityを別の基準として扱う

Identityは、Continuity Readabilityとは別に表現する。

\[
\operatorname{Id}_{q}(g_i,g_j)
\]

を、Identity基準 \(q\) のもとで、\(g_i\) と \(g_j\) が同じentity、bearer、またはStructureとして扱われることを表すものとする。

基準 \(q\) には、例えば次があり得る。

```text
数的同一性
法的同一性
機能的同一性
物質的持続
意味的同一性
アカウント同一性
生物学的同一性
役割同一性
```

本モデルは、一つの普遍的Identity基準を仮定しない。

中心となる分離は、次である。

\[
\operatorname{CR}(g_i,g_j)
\not\equiv
\operatorname{Id}_{q}(g_i,g_j)
\]

ContinuityとIdentityは異なる問いに答える。Continuityは、realization間の許容可能な関係を辿り、接続として読めるかを問う。Identityは、ある基準のもとで二つのrealizationを同一として扱うかを問う。

## 7.9 Identityを伴わないContinuity

本モデルは、次を許容する。

\[
\operatorname{CR}(g_i,g_j)=\mathrm{true}
\]

かつ、

\[
\operatorname{Id}_{q}(g_i,g_j)=\mathrm{false}
\]

である。

例えば、生地とケーキは、物質変換、因果的継起、製造履歴によって連続的に接続され得るが、型や対象基準のもとで同一とは限らない。同様に、ソフトウェアのrequestと、その結果として生じたdatabase updateは、同じentityではないが、可読な連続関係を形成し得る。

したがって、

```text
Identity break
≠
Trajectory break
```

である。

Identity分類の変化は、必ずしも関係的連続性を破壊しない。

## 7.10 可読なContinuityを伴わないIdentity

逆のケースも許容される。

\[
\operatorname{Id}_{q}(g_i,g_j)=\mathrm{true}
\]

であっても、

\[
\operatorname{CR}(g_i,g_j)=\mathrm{false}
\]

または未確定であり得る。

制度上、二つの記録が同じ法的人物を指すと主張されていても、その間の連続性を現時点で再構成できない場合がある。システムが一つのaccount identifierを維持していても、そのbehavioral trajectoryやoperational trajectoryが不可読になる場合もある。したがってIdentity主張は、断絶、証拠の空白、Tracingの論争があっても存続し得る。

## 7.11 Continuity ReadabilityとDifference

Continuityは、Differenceの不在を要求しない。むしろ、realization間で構造化されたDifference patternを辿れるために、連続性が読める場合がある。

\[
\Delta_{B,c,\Sigma}(g_i,g_j)
\]

を、Slice相対的なDifferenceとする。次の場合でも、Continuityは読める可能性がある。

\[
\Delta_{B,c,\Sigma}(g_i,g_j)\neq 0
\]

ただし、そのDifferenceが連続関係の内部で許容可能であることが必要である。

したがって、

```text
continuity
≠
変化しない同一性
```

である。

Continuity基準は、許容された変換、bounded deviation、役割変化、構造化されたDifferenceを含み得る。

## 7.12 Continuity ReadabilityとIncorporated Readability

Context \(\Gamma\) は、どの関係が許容可能であり、どの関係が可読であるかに影響する。先行するGyro realizationによって、後続のContinuity readingを可能にする基準、カテゴリー、推論経路が成立し得る。

\[
\Gamma_{n+1}
=
\operatorname{Update}_{\Gamma}(\Gamma_n,q_n,e_n)
\]

その結果、

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma_{n+1})
\]

は、\(\Gamma_n\) のもとで利用可能だったContinuity Readabilityと異なり得る。

この依存関係によって、遡及的再解釈が可能になる。以前は不可読だった関係が、追加の区別や証拠が織り込まれた後に追跡可能かつ可読になることがある。逆に、以前受け入れられていたContinuityが、Context修正によって無効化またはアクセス不能になる場合もある。

## 7.13 二値形式と段階形式

Minimal Formal Modelでは述語形式が有用であるが、応用によっては段階値が必要になる。

\[
\operatorname{CR}^{*}(g_i,g_j;B,c,\Sigma,\Gamma)
\in \mathcal{C}
\]

ここで \(\mathcal{C}\) は、順序集合、信頼区間、証拠構造、または領域固有の分類であり得る。

本論文は、Continuityが普遍的に二値または数値であることを要求しない。Boolean形式は、統合スキーマに必要な最小限の論理的区別のみを表す。

## 7.14 最小限のコミットメント

提案モデルがコミットするのは、次のみである。

1. 局所的Gyro realization間には関係が成立し得る。
2. 関係の存在、Traceability、Admissibility、Readabilityは区別される。
3. Continuity ReadabilityはOrientation・Context・Slice・Incorporated Readabilityに依存する。
4. Identityは別の基準によって扱われる。
5. ContinuityはDifferenceやIdentity変化をまたいで成立し得る。
6. Continuityが不可読または論争的でもIdentityが主張され得る。
7. Continuity readingはRe-SliceとContext更新によって修正され得る。

本モデルは、Continuityが同値関係であること、あらゆる領域で推移的であること、対称的であること、全域的に決定可能であること、一つのIdentity基準が普遍的に適用されることを仮定しない。

## 7.15 文脈的Trajectoryへの接続

Continuity Readabilityは、特定の局所的realization同士を接続として読めるかを扱う。Trajectoryには、より広い構成が必要である。複数の局所的realization、保持された関係の場、そして、その中からより大きな関係的経路を可読化するContext相対的なTracing operationが必要になる。

次章では、関係を保持する場とTrajectoryそのものを分離し、Trajectoryを、事前定義された状態列や時系列ログではなく、Contextual Tracingとして構成する。

# 8 文脈的Trajectory

## 8.1 局所的連続性からTrajectoryへ

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

## 8.2 局所的Gyro realization

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

## 8.3 関係を保持するTrace Field

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

## 8.4 文脈的Tracing

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

## 8.5 Traceの許容可能性

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

## 8.6 Trajectoryは事前定義された状態列ではない

状態Trajectoryは、しばしば次のように表される。

\[
x_0,x_1,x_2,\ldots,x_n.
\]

この表現は、各状態が共通の状態空間に属し、その順序関係がすでに利用可能であることを前提とする。Gyro Trajectoryが要求する前提は、これより弱い。接続されるrealizationは、型、表現、粒度、Identityが異なっていてもよい。連続性は、一つの遷移関数ではなく、異種の関係に依存し得る。

したがって、線形状態列は、前提が正当化される限定領域ではGyro Trajectoryを具体化し得るが、Trajectoryの普遍的形式ではない。

## 8.7 Trajectoryはログではない

時系列ログは、出来事がある順序で保存されたことを記録する。しかし、それらの出来事の間でどの関係が許容され、追跡でき、連続性として読めるかを、それ自体で確立するわけではない。ログはTrajectory読解を支え得るが、ログそのものがTrajectoryではない。

保存履歴を \(H\) とすると、

\[
H\neq T_{B,c,\Sigma_T,\Gamma_T}.
\]

同じ履歴から複数のTrajectoryが読まれる場合も、何も読めない場合も、記録時点では利用不能だったTrajectoryが後に読める場合もある。

## 8.8 分岐・合流・複数Trajectory

relation-bearing fieldは複数の許容可能なTracingを支え得るため、Trajectoryは線形である必要がない。本モデルは次を許容する。

- 一つの局所的realizationから複数の継続が読まれる分岐
- 複数のtraceが一つの後続realizationへ寄与すると読まれる合流
- 異なるTracingが併存する並行Trajectory
- 異なる解釈が相互に両立しない競合Trajectory
- 局所traceがより広いtraceの中で読まれる入れ子Trajectory
- 一部のみが現在可読な部分Trajectory

したがって、特定の実装では、Tracing結果をグラフ、ハイパーグラフ、半順序、圏、イベント構造として表せる可能性がある。しかし本理論は、そのどれか一つを普遍的形式として固定しない。

## 8.9 空白と不可読区間

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

## 8.10 遡及的TracingとRe-Slice

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

## 8.11 Jumpと非連続的再構成

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

## 8.12 Incorporated Readabilityとの関係

Incorporated Readabilityは、どのtraceが許容され、重みづけされ、解釈されるかを条件づける。Tracingに利用されるreadability contextを \(\Gamma_T\) とすると、\(\Gamma_T\) の変化は次を生じさせ得る。

- 以前は不可読だった関係を可読にする
- 以前は許容されていた関係を無効化する
- 競合traceの重みを変更する
- 分離していた局所的realizationを接続する
- 一つの可読Trajectoryを複数へ分割する
- 複数のTrajectoryをより広いTrajectoryへ統合する

したがってTrajectoryは、先行するGyro realizationから独立ではないが、その保存された蓄積へ還元されるものでもない。

## 8.13 最小限のコミットメント

文脈的Trajectoryモデルがコミットするのは、次の事項に限られる。

1. 局所的Gyro realizationを暫定的に参照できること
2. それらの間の異種関係を表現できること
3. 関係の存在、追跡可能性、可読性を区別すること
4. Tracing operationがOrientation・Context・Slice・Incorporated Readabilityに条件づけられること
5. Tracing結果が非線形、部分的、修正可能、複数的であり得ること
6. Trajectoryが派生概念であり、不変Coreを置き換えないこと

本モデルは、すべてのTrajectoryが線形、因果的、完全、客観的に一意、連続微分可能、距離空間へ埋め込まれる、または一つの大域時計で添字づけられることを仮定しない。

## 8.14 DifferenceとBoundaryへの接続

Tracingには、局所的realization間および可能な関係間の区別が必要となる。これらの区別は、状態、形、役割、基準、関連性、連続性の違いを含み得る。しかしDifferenceを距離や誤差と仮定することはできず、BoundaryをDifferenceそのものと同一視することもできない。次章では、DifferenceをSlice・Orientation・Contextに相対的な非一致の構造化された関係として整理し、Boundaryがどのように派生的な可読区別として成立し得るかを検討する。

# 9 DifferenceとBoundary

DifferenceとBoundaryは、Gyro Logicにおける派生概念である。これらは不変Coreを置き換えるものではなく、Structure・Slice・Stabilityの間に追加段階として挿入されるものでもない。その役割は、特定のOrientation・Context・Sliceのもとで、非一致がどのように利用可能になり、構造化され、可読化されるかを記述することにある。

## 9.1 Differenceは距離ではない

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

## 9.2 Differenceは誤差ではない

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

## 9.3 Slice相対的な構造化された非一致としてのDifference

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

## 9.4 Differenceとlocal articulation

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

## 9.5 BoundaryはDifferenceではない

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

Differenceは存在していてもBoundaryにならない場合がある。弱すぎる、分散している、現在は無関係である、アクセス不能である、未解決である場合などである。反対に、以前のDifference patternが現在のreadability contextへ織り込まれているために、元のDifferenceが直接観測されなくてもBoundaryが運用上利用可能であり続ける場合がある。

## 9.6 Slice相対的な可読区別としてのBoundary

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

## 9.7 Boundary State

Boundary Stateは、可読なBoundaryに対する対象、事象、表出、realizationの暫定的な関係状態を表す。それは対象の内在的属性ではない。

候補記法は、

\[
\operatorname{BS}(x\mid d,B,c,\Sigma,\Gamma)
\]

である。ここで \(d\) は関連するBoundaryである。結果として、\(x\) はnormal、non-、un-、absence、blank、unknown、Void相対、inside、outside、crossing、deferred、その他の領域固有の関係へ分類され得る。

Boundary Stateは関係的かつ暫定的であるため、Orientation、Context、Slice、Incorporated Readabilityが変化すれば、基礎対象が別の対象へ変わらなくても分類が変わり得る。

## 9.8 Boundary・Continuity・Trajectory

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

## 9.9 DifferenceとBoundary Readabilityの織り込み

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

## 9.10 形式的コミットメントと非コミットメント

Minimal Formal Modelは、次をコミットする。

1. DifferenceはOrientation・Context・Sliceに相対的である。
2. Differenceは部分的かつ異種的であり得る。
3. Differenceは普遍的に距離的または誤差的ではない。
4. Boundaryは可読な区別から派生し、Differenceと同一ではない。
5. Boundary Stateは関係的かつ暫定的である。
6. DifferenceとBoundaryは、Stability、Continuity Readability、Trajectory、後続のIncorporated Readabilityへ影響し得る。

一方、本モデルは、すべてのDifferenceが測定可能であること、すべてのBoundaryが鋭いこと、すべての区別が二値的であること、すべてのBoundaryが空間的であること、すべてのBoundary横断がContinuityを断つこと、すべての領域が一つの普遍的Difference codomainを共有することを仮定しない。

以上の整理は、統合Minimal Formal Modelへの準備となる。次章では、Structure、Slice、local articulation、Stability Scene、Incorporated Readability、Continuity Readability、Contextual Trajectory、Difference、Boundaryを、不変Coreを維持した一つの簡潔な形式スキーマへ統合する。

# 10 最小形式モデル

## 10.1 統合スキーマの目的

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

## 10.2 局所的Gyro realization

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

## 10.3 Structure

Structureは識別子 \(S_n\) によって表すが、その数学型は意図的に未確定のまま残す。モデルがコミットするのは、局所的に関係する状態、関係、区別、または表出が、Structureに相対的に利用可能になり得ることのみである。

弱い関係記法として、次を用いる。

\[
x \triangleleft S_n.
\]

これは、\(x\) が \(S_n\) に相対的に局所的に成立可能または利用可能であることを表す。この関係は、集合所属、空間的包含、因果的依存、論理的含意のいずれかに限定されない。特定領域のモデルでは、必要に応じて特殊化できる。

## 10.4 Sliceとlocal articulation

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

## 10.5 Stability Scene

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
\operatorname{StabScene}
\bigl(
a_n;S_n,B_n,c_n
\bigr).
\]

これは、関連条件のもとで、表出が一つの成立として十分に可読であり、かつ十分に継続可能であることを表す。可読性および継続可能性が必ず二値であるとは仮定しない。

## 10.6 Incorporated Readability

局所的realizationのうち、後続のrealizationで利用可能になる部分を次で表す。

\[
q_n
=
\operatorname{Inc}(g_n).
\]

現在のreadability contextを \(\Gamma_n\) とし、その更新を次で表す。

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

## 10.7 Continuity Readability

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

## 10.8 関係保持場とTrajectory

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

## 10.9 Difference

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

## 10.10 コンパクトな統合形

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

## 10.11 本モデルが保証すること

現在の探索段階において、本モデルが保証するのは概念的・形式的分離である。Structure、Slice process、local articulation、Stability Sceneを区別する。履歴とIncorporated Readability、関係の存在とContinuity Readability、Identityと連続性、trace fieldとTrajectory、Differenceと距離・誤差・Boundaryを分離する。また、不変CoreとGyro Logic・GyroOS・GyroAuthのLayer分離を維持する。

## 10.12 本モデルが保証しないこと

本モデルは、完全公理化、普遍意味論、表現の一意性、決定可能性、計算量境界、実証的妥当性、または厳密な数学的意味での最小性の証明を、現時点では提供しない。Structureの最終的数学型、普遍的Stability尺度、普遍的Tracingアルゴリズム、普遍的Difference値域も決定しない。これらは、領域別具体化と後続検証の対象である。

したがって統合スキーマは、形式的な設計境界として機能する。比較、例示、実装研究、後続の精緻化を支える程度に明示的でありながら、保持すべき理論的区別を上書きしない程度に弱い構成である。

# 11 Minimal Formal Modelの図解

## 11.1 Figure 1：不変Core

![Gyro Logicの不変Core。Operator OrientationとContextはSliceを条件づけるが、追加Core要素にはならない。](figures/fig1_invariant_core.svg){width=94%}

Figure 1は、本論文全体を拘束する理論条件を示す。不変CoreはStructure → Slice → Stabilityのままである。Operator OrientationとContextはSlice processを条件づけるが、本モデルは、それら、local articulation、Trajectory、Difference、Boundary、Operator Responseを第四のCore要素として挿入しない。

## 11.2 Figure 2：局所的Gyro realizationとContext更新

![局所的Gyro realization、Stability Scene、後続readability contextの更新。](figures/fig2_local_realization.svg){width=96%}

Figure 2は、暫定的な局所realization

\[
g_n=(S_n,B_n,c_n,\Sigma_n,a_n,K_n)
\]

を要約する。図は、Slice processとlocal articulationを分離し、さらにarticulationとStability Sceneを分離する。Stability Sceneは、可読な関係、残存する局所的な未、継続条件を含み得る。Incorporated Readability \(q_n=\operatorname{Inc}(g_n)\) は、後続readability context \(\Gamma_{n+1}\) を更新し、外的変化 \(e_n\) は明示的に別要因として保持される。

## 11.3 Figure 3：Contextual Trajectory

![relation-bearing fieldから可読なTrajectoryへの文脈的Tracing。](figures/fig3_contextual_trajectory.svg){width=96%}

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

## 11.4 図解の適用境界

これらの図は説明上の要約であり、置換定義ではない。Structureが箱であること、Sliceが決定論的な矢印であること、Stabilityが常にタプルであること、Trajectoryが常にグラフであることを意味しない。目的は、Minimal Formal Modelが維持する分離を可視化し、後続の数学研究および実装研究のための安定した参照点を提供することである。

# 12 Related Workと形式的位置づけ

## 12.1 Gyro Logic基礎論文との関係

本論文は、Gyro Logic基礎論文を置き換えるものではなく、その形式化を担う補完論文である。先行する基礎論文は、不変Coreを導入し、「Gyro Logicとは何か」という問いを扱った [@kawakami2026gyro_logic_jp]。これに対して本論文が扱うのは、Canonical Definitionを変更せず、Coreの周囲に形成された現在の概念的区別を、どのように暫定的な形式スキーマとして整理できるかという、より限定された方法論的問題である。

両論文の役割は、次のように区別される。

```text
基礎論文
=
概念的導入と理論的方向づけ
```

```text
本論文
=
最小形式組織化と比較境界
```

したがって本モデルは、Gyro Logic全体を一つの閉じた数学体系へ置き換えられるかではなく、既存の区別を維持し、それぞれの仮定を検査可能にできるかによって評価されるべきである。

## 12.2 関係構造とグラフモデル

関係構造およびグラフ理論は、異種の局所的realizationと保持された関係を表現するための自然な資源を提供する。標準的なグラフ理論は、頂点、辺、経路、連結性、分岐、グラフ変換を明示的に扱う [@diestel2017graph]。これらは、関係を保持するtrace field

\[
\mathcal{G}_R=(G,E)
\]

の表現に直接利用できる。

ただし、表現済みのグラフは通常、関連するnodeとedgeがすでに個体化されていることを前提とする。したがってGyro Logicにおけるrelation-bearing fieldと可読なTrajectoryの区別は、グラフ表現だけでは尽くされない。グラフは候補関係を保持し、TrajectoryはAdmissibilityとReadabilityの条件下で文脈的Tracingを行った結果として読まれる。

## 12.3 Event Structureと並行性

Event Structureは、一つのinterleavingされた列へシステムを還元することなく、出来事、因果依存、競合、並行性を表現するために発展してきた。Petri net・Event Structure・domainの古典的な関係は、出来事と因果的組織がconfiguration-based semanticsをどのように支えるかを厳密に示している [@nielsen1981petri]。後続研究では、configuration structure、Event Structure、Petri net間の対応がさらに整理された [@vanglabbeek2009configuration]。

これらは、分岐、合流、競合、半順序、非線形Trajectoryに特に関係する。一方で、形式的に表現されたeventと、enableまたはconflict関係から開始する。Gyro Sliceが扱うのは、それより前または弱いコミットメント、すなわちlocal articulationが利用可能になる過程である。したがってEvent Structureは、実現済みGyro Processの領域固有表現として有力であるが、StructureまたはSliceの普遍的存在論としては採用しない。

## 12.4 Transition System・Model Checking・Process Algebra

Transition SystemとModel Checkingは、状態、label、transition relationが規定された後の状態発展、分岐挙動、時間的性質、検証に対して精密な技法を提供する [@baier2008principles]。Process Algebraも、相互作用、並行性、同期、継続を合成的に表現する。MilnerのCalculus of Communicating Systemsは、その基礎的な例である [@milner1980ccs; @milner1982combinators]。

これらは、Gyro Process、Gyro Loop、Operator Response、Re-Slice、Defer、Jumpに関係し、GyroOS実装に有用である。ただし、事前定義されたtransitionまたはaction vocabularyを、articulationを可能にするより一般的なStructureと同一視する危険がある。本論文ではProcess AlgebraとTransition Systemを、実装層または領域層の形式化として扱い、不変Coreの置換定義には用いない。

## 12.5 Dynamical SystemとStability

Dynamical Systemは、trajectory、equilibrium、attractor、oscillation、convergence、bifurcation、perturbationに関する確立されたモデルを提供する [@strogatz2015nonlinear]。状態空間と発展則が正当化される場合、特に測定可能なGyroOSまたはGyroAuthの挙動に有効である。

Gyro Stabilityは、dynamical stabilityより意図的に広い。局所的に可読かつ継続可能な成立に関わり、変化の継続および残存する未と共存し得る。同様に、Gyro Trajectoryを時間添字付き状態解へ普遍的に同一視しない。したがってDynamical Systemは重要な特殊化であるが、equilibrium、convergence、invarianceをStabilityの普遍的定義にはできない。

## 12.6 Topology・局所性・Sheaf-like Structure

Topologyは、近傍、連続性、閉包、分離、境界を形式化する [@munkres2000topology]。local articulationの周囲における局所的持続と許容変動の表現に有用である。Sheaf theoryは、局所情報、restriction、compatibility、局所データが一つのglobal objectへglueできない可能性を扱う、より豊かな言語を提供する [@maclane1992sheaves]。

これらは、Stability Sceneの局所性、および局所的成立と全体非閉包の区別に対応する。また、重なり合うContext間の可読性を支える可能性がある。ただしTopologyとSheaf theoryは、基礎空間、site、covering、restriction structureが特定されていることを必要とする。本モデルは、それらがすべての領域でSlice以前から利用可能であるとは仮定しない。

## 12.7 Category Theoryと合成

Category Theoryは、object、morphism、composition、identity、functor、構造保存的translationの一般言語を提供する [@maclane1998categories]。均質な一つの状態型を要求せず、領域固有Gyroモデルを合成し、異なるcontinuity形式を関係づける枠組みとして有望である。

主な注意点は、通常のmorphismが指定済みのdomainとcodomainを持つことである。一般的Slice relationは、local articulationがSlice process以前から完全に個体化されたcodomainとして利用可能であるとは仮定しない。したがってCategory Theoryは、適切な局所objectとmorphismが正当化された後の合成枠組みとなり得るが、StructureまたはSliceの最初からの普遍型としては課さない。

## 12.8 Belief Revisionと非単調Context更新

AGM belief revisionは、明示的なpostulateによってbelief setの合理的なcontractionとrevisionを形式化する [@alchourron1985logic]。これは、Incorporated Readabilityの非単調的側面、特に後続推論が利用できるものの追加、修正、無効化、重み変更に直接関係する。

ただしIncorporated Readabilityは、belief revisionより広い。readability context \(\Gamma\) はdeductive closureされたbelief setである必要はなく、織り込みは命題的ではなく、物質的、手続的、知覚的、制度的、運用的であり得る。したがってAGM型revisionは論理Contextに対する強い部分モデルであるが、Incorporationの普遍的解釈ではない。

## 12.9 確率・統計モデル

確率と統計は、event modelと測定変数が規定された後、不確実性、信頼度、証拠、異種観測を定量化できる。Probabilistic Graphical Modelは、不確実性下の構造化された依存関係と推論に関する成熟した枠組みを提供する [@koller2009probabilistic]。

これらは、段階的Readability、Stability confidence、Difference distribution、競合するTrajectory仮説を具体化し得る。一方、それ自体では、関連する変数、event、distinctionがどのように局所的にarticulableになるかを説明しない。したがってProbabilityは、Gyro Logicの一般意味論ではなく、領域固有の定量層として扱う。

## 12.10 本モデルの形式的位置づけ

検討した各分野は重要な形式資源を提供するが、それぞれ、特定のobject、relation、space、event、operationが規定された後に適切となるコミットメントから始まる。Minimal Formal Modelは、それらを調整する役割を担う。すなわち、各数学資源を適用するときに、どの区別を可視のまま維持しなければならないかを明示する。

位置づけは、次のように要約できる。

```text
Gyro Logic Minimal Formal Model
≠
既存数学を置き換える新体系
```

```text
Gyro Logic Minimal Formal Model
=
部分モデルの選択と調整のための形式境界
```

したがって本論文が主張する新規性は、新しいgraph theory、topology、dynamics、probability theory、process algebraではない。領域固有の形式化を比較可能にしつつ、Structure、Slice process、local articulation、Stability Scene、Incorporated Readability、Continuity Readability、contextual Trajectory、Difference、Boundaryを暗黙に潰さないための明示的な組織化にある。

# 13 既存数学分野との比較

## 13.1 比較の目的

Minimal Formal Modelは、既存数学から切り離された独立体系として提案されるものではない。Gyro Logicの各部分については、既存の複数分野が有効な表現手段を提供する。ここで問うべきなのは、Gyro Logicがどの一分野に「属するか」ではなく、各分野がどの前提を導入し、その前提がGyro Logic固有の区別をどこまで保持し、どこから抑圧するかである。

したがって本比較では、各分野を次の二つの観点から評価する。

1. **表現上の有効性**：提案スキーマのどの部分を適切に表現できるか。
2. **還元リスク**：その分野をGyro Logic全体の普遍的形式として採用した場合、どの理論的区別が失われるか。

以下で扱う分野を否定するものではない。各分野は、適用領域と形式化制約を明示したうえで用いられる部分モデルとして位置づけられる。

## 13.2 関係構造

関係構造は、提案モデルの基礎候補として最も広い柔軟性をもつ。異種の対象、部分関係、許容条件、Difference pattern、Boundary relation、局所的Gyro realization間の接続を、すべて数値や距離へ還元せずに表現できる。

局所領域は暫定的に次のように書ける。

\[
\mathfrak{R}
=
\langle X,\{R_\alpha\}_{\alpha\in A}\rangle,
\]

ここで関係族 \(\{R_\alpha\}\) は、因果、意味、物質、時間、推論、制度などの関係を含み得る。

この柔軟性は、Continuity ReadabilityやContextual Trajectoryに有効である。一方、通常の関係構造は、対象と関係がすでに利用可能であるように見せやすい。それ自体では、local articulationがSliceを通じてどのように利用可能になるか、不可読な関係がどのように可読になるか、Incorporated Readabilityが後続条件をどう変えるかを説明しない。

## 13.3 グラフとハイパーグラフ

グラフは、局所的Gyro realizationと痕跡を担う関係の自然な表現を与える。

\[
\mathcal{G}_R=(G,E).
\]

有向グラフは、非対称な継起、依存、Tracingを表現できる。多重グラフは、同じrealization間の複数の関係型を保持できる。ハイパーグラフは、二項辺へ還元できない複数realization間の関係を表現するのに有効である。

分岐、合流、競合するtrace、空白、遡及的再接続の表現に適している。しかしグラフそのものはTrajectoryではない。通常のグラフは、ノードと辺がすでに個体化され、表現可能であることを仮定する。Gyro Logicでは、関係を保持する場と、文脈的Tracingを通じて可読になるTrajectoryとを分離しなければならない。

## 13.4 順序理論

順序理論は、先行関係、依存、精緻化、関連性の順位、部分比較可能性を表現できる。Incorporated Readabilityによって区別の影響順位が変化する場合や、Trajectoryが単一時系列ではなく部分順序によって制約される場合に有効である。

例えば、領域相対的な順序を次のように書ける。

\[
x\preceq_{B,c,\Gamma}y.
\]

これは、特定条件のもとで、\(x\) が \(y\) より成立していない、関連性が低い、または先行していることなどを表し得る。

ただし、Differenceは常に順序づけられるとは限らない。比較不能であることは、欠如や失敗を意味しない。したがって順序理論は、DifferenceやStabilityの普遍的値域ではなく、有効な特殊例である。

## 13.5 位相と近傍構造

位相は、局所性、近傍、小さな変動に対する持続、Boundaryに類する構成を表現するのに有効である。Stability Sceneをlocal articulationの周囲の近傍として解釈できる。

\[
a_n\in N_n.
\]

この近傍には、全体閉包を要求せず、可読な関係と許容される継続を含められる。これにより、Stabilityを一点ではなく、限定された変動のもとで確認と継続が可能な局所領域として扱える。

ただし、Gyro Stabilityは位相的安定性と同一ではなく、Gyro Boundaryも位相的境界より広い。さらに、Structureの理論的な「未」を位相的開性と同一視してはならない。位相は、対象と近傍が設定された後の局所場面を表現できるが、それらがSliceによってどのように表出するかを単独では説明しない。

## 13.6 力学系

力学系は、時間発展、摂動、収束、振動、回復、発散を扱う領域モデルとして強力である。観測可能な状態変数と更新則が定義されているGyroOSやGyroAuthの実装では、とりわけ有効である。

通常の力学モデルは次の形をとる。

\[
x_{t+1}=F(x_t,u_t).
\]

この形式により、Stability score、収束条件、drift detection、response dynamicsを実装できる。しかし力学系のTrajectoryは通常、状態発展そのものである。本モデルにおけるTrajectoryは、局所的realization間の許容可能な関係をTracingすることで読まれる構成である。また、Lyapunov stability、平衡、attractorは特定仮定のもとでのStability実装となり得るが、Stability Sceneの意味全体ではない。

## 13.7 遷移系とイベント構造

遷移系は、操作的継起、分岐選択、有効化されたaction、状態依存responseを表現する。イベント構造は、並行性、因果、競合を加え、一つの線形実行順へ還元できない過程を扱える。

これらは、Gyro Process、Operator Response、Re-Slice、Jump、分岐Trajectoryの形式化に関連する。局所的realizationをeventとして、因果関係や有効化関係で接続することもできる。

ただし、状態、event、transitionは通常、実行前に定義されている。Sliceは、local articulationが利用可能になる過程に関わる。したがって遷移系は、実現済みのGyro processを実装できるが、表出以前のStructureを自動的に形式化するわけではない。

## 13.8 圏論

圏論は、異種対象、変換、合成、Identity、構造保存写像を扱う強力な言語である。対象型の同一性を要求せずに継続を表現する場合や、異なる領域の局所過程を合成する場合に有効である。

局所的候補として、次のように書くこともできる。

\[
\Sigma:S\to A,
\]

または、traceable relationを射として、その合成を許容可能なpathとして扱える。

しかし通常の射は、定義された始域と終域を前提とする。Gyro Logicでは、local articulation \(a_n\) がSlice以前から完全に定められた終域として存在するとは仮定しない。圏論的モデルは、領域固有のarticulation spaceが正当化された後に適切となる可能性が高い。圏論は有力な統合言語だが、現時点でStructureやSliceの普遍的存在論ではない。

## 13.9 論理と証明論

論理と証明論は、Incorporated Readabilityの部分モデルとして非常に強い。証明文脈 \(\Gamma_n\) は、後続推論で利用可能になった定義、仮定、補題、区別、推論規則を表現できる。

\[
\Gamma_n\vdash\varphi.
\]

Context extension、revision、非単調推論、belief revision、defeasible reasoningは、Incorporated Readability更新を形式化する有効な道具を提供する。

ただし、通常の論理体系は、命題、述語、推論規則がすでに個体化された後から始まる。Gyro Sliceは、関連する命題、区別、推論対象そのものが局所的に表出可能になる過程を含み得る。したがって論理的帰結は後続可読性の有力モデルではあるが、Slice全体のモデルではない。

## 13.10 制約充足と制約伝播

制約系は、相互作用する条件から局所的configurationが徐々に表出する過程を表現できる。単純なろ過とは異なり、制約伝播は、相互制限と伝播を通じて局所的に整合した形を形成する。この点で、一部のSlice実装候補として有望である。

領域モデルでは、変数 \(V\)、定義域 \(D_V\)、制約 \(C\) を置き、局所的に利用可能なconfigurationが現れるまで伝播を行える。

ただし通常の制約モデルは、変数、定義域、制約が事前に指定されている。Gyro Structureは、その個体化以前の段階を含み得る。したがって制約伝播は、問題表現が成立した後のlocal articulation形成をモデル化できるが、Structure一般の存在論を与えるとは限らない。

## 13.11 確率と統計

確率と統計は、readability、Stability、Difference、admissibilityを不確実性のもとで表現する場合に有効である。確率的Stability score、Difference distribution、Continuity Readabilityのconfidence、Incorporated ReadabilityのBayesian revisionを支援できる。

例えば、次のような応用レベルの尺度を導入できる。

\[
P\bigl(\operatorname{Readable}(r)\mid B,c,\Sigma,\Gamma\bigr).
\]

ただし確率は、event space、sigma-algebra、または指定されたuncertainty modelを必要とする。そのようなモデルの存在は普遍的には仮定できない。確率は、表出済みモデル内部の不確実性を定量化するが、その基礎区別がSliceを通じてどのように表出するかを説明しない。

## 13.12 層に類する局所・大域構造

Sheaf-like structureは、局所的に可読なdata、重なり合うContext間の整合性、局所readingが一つの大域readingへ結合できない可能性を表現するのに有望である。局所的Stability Scene、Context依存readability、大域的非閉包を扱う形式言語となり得る。

局所sectionが個別には可読でも、全体として整合的にgluingできない場合がある。これは、局所的成立と未解決の大域Structureを分けるGyroの区別と近い。

ただしsheaf theoryは、base space、covering structure、restriction mapを必要とする。これらは特定形式領域では正当化され得るが、Gyro Logicの普遍的なpre-Slice Structureとして仮定してはならない。

## 13.13 プロセス代数

プロセス代数は、interaction、concurrency、communication、choice、interruption、continuationを表現できる。Operator ResponseがContinue、Stop、Re-Slice、Defer、Jumpを選択するGyro ProcessやGyro Loopに関連する。

その強みは、実行可能かつ合成可能なprocess descriptionにある。一方、process algebraは通常、定義済みのaction vocabularyとprocess syntaxを前提とする。関連するactionとstateが表出された後のGyro Logicの操作的realizationは表現できるが、それらの表出可能性をもつStructureそのものを単独で捉えるわけではない。

## 13.14 比較の要約

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

## 13.15 異種複合モデル

以上の比較から、Minimal Formal Modelは既存数学すべてに対抗する新分野ではなく、複数の部分モデルを調整するスキーマとして理解するのが適切である。領域固有の実装では、例えば次を組み合わせられる。

- 異種trace relationには関係構造またはハイパーグラフ
- 局所Stabilityには近傍構造または位相
- Incorporated Readabilityには論理Contextまたは非単調Context
- 操作的展開にはイベント構造またはプロセス代数
- 測定可能な応用挙動には確率モデルまたは力学モデル
- 特殊化されたモデル間の合成には圏論的道具

この複合モデルが許容される条件は、本論文で確立した区別を保持することである。便利な実装対象を提供するからという理由で、いずれかの部分モデルが不変Coreを再定義してはならない。

## 13.16 比較の結論

検討した既存数学分野のいずれも、追加仮定なしにGyro Logic全体の完全な普遍モデルを提供しない。同時に、現段階で完全に独立した新しい数学を要求する必要もない。既存分野は、その適用範囲を明示すれば、強力な部分モデルを提供する。

したがって提案スキーマの主な形式的貢献は、既存数学を置き換えることではない。どの数学モデルが適切であり、何を表現し、何を未解決のまま残すかを判断するために必要な区別を保持し、調整することにある。

次章では、具体例へスキーマを適用し、これらの区別が操作的にも理解可能なまま維持されるかを確認する。

# 14 例示による確認

本章では、提案した区別が具体的状況へ適用されたときにも理解可能なまま維持されるかを、少数の例によって確認する。目的は、実証的妥当性を示すことでも、Minimal Formal Modelの一意性を証明することでもない。各例は概念的ストレステストとして機能する。すなわち、Structure、Slice process、local articulation、Stability、Incorporated Readability、Continuity Readability、Trajectory、Difference、Boundaryを、矛盾なく分離できるかを確認する。

## 14.1 例1：数学問題を解く過程

最終結果へ到達する前に、中間的な定義を導入する数学的証明を考える。ある段階における問題全体、既存の仮定、利用可能な補題、記法、未解決の証明義務は、Structure \(S_n\) を形成する。このStructureは、書かれた紙面や現在の命題そのものではない。証明上の一手が成立し得る組織化された様式である。

Slice process \(\Sigma_{B_n,c_n}\) は、Orientation \(B_n\) とContext \(c_n\) のもとで進行する。Orientationは、補題を証明すること、不変量を切り出すこと、あるいは目標を再定式化することへ向けられ得る。このSliceは、すでに完全に個体化された結果を単に取り出すものではない。例えば、次のようなlocal articulation \(a_n\) が利用可能になる。

```text
変換のもとで保存される量を q_n と定義する。
```

この表出は最終定理ではない。また、自動的にStableでもない。定義が可読で、利用可能で、後続推論を支える程度に整合するとき、初めてStability Sceneの一部となる。

\[
K_n=(a_n,L_n,U_n,C_n^{+}).
\]

ここで、\(L_n\) は新しい定義を理解可能にする関係、\(U_n\) は未解決の証明義務、\(C_n^{+}\) はその定義によって可能になる後続推論を含む。

この段階で獲得された可読性は、後続の証明文脈へ織り込まれ得る。

\[
q_n=\operatorname{Inc}(g_n),
\qquad
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n).
\]

この更新は、定義文をログへ保存することとは同じではない。新しい定義は、どの変換が関連するか、どの部分目標が見えるか、どの後続命題を帰結として読めるかを変化させ得る。この例は、Incorporated Readabilityが受動的な履歴保存よりもContext拡張に近いことを示す。

## 14.2 例2：生地がケーキになる過程

生地をオーブンへ入れ、ケーキへ変化させる過程を考える。この物質過程は多数の物理状態変数によって表現できるが、Gyro Logic上の論点は、Sliceのもとで何が可読になるかにある。

生地と加熱条件はStructure \(S_i\) を形成する。Sliceは、料理としての完成度、化学変化、物質的連続性、製品Identityなどへ向けられ得る。あるOrientationのもとでは、次のlocal articulationが現れ得る。

```text
混合物がケーキとしての形に固まった。
```

別のOrientationでは、水分分布、内部温度、化学反応が表出し得る。これらは、Slice以前から完全に個体化された対象として待機していたと仮定されない。Sliceを通じて利用可能になる。

生地からケーキへの変化は、IdentityとContinuity Readabilityの分離も示す。厳格なIdentity基準 \(q\) は、生地とケーキを異なる対象として分類し得る。

\[
\operatorname{Id}_{q}(g_i,g_j)=\mathrm{false}.
\]

その一方で、物質的、因果的、工程的関係は追跡可能かつ可読なままであり得る。

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma)=\mathrm{true}.
\]

したがって、次の区別が成り立つ。

```text
Identity break
≠
Continuity break
```

また、Differenceが大きいことは、必ずしもTrajectory breakを意味しない。食感、形状、温度、化学的組織が大きく変化しても、その変化全体は一つの継続過程として読める場合がある。

## 14.3 例3：条件変化を含む認証

端末、行動、ネットワーク、時間、動作に関する観測を用いる認証過程を考える。一般的なモデルでは、現在の測定値を保存済みプロファイルと比較し、誤差スコアを算出することがある。Minimal Formal Modelは、より広い解釈を許す。

現在の認証状況はStructure \(S_n\) を形成する。Slice process \(\Sigma_{B_n,c_n}\) は認証へ向けられ、Contextには端末履歴、最近のネットワーク変化、過去の成功セッション、既知のリスク条件などが含まれ得る。local articulation \(a_n\) は、例えば次のように表される。

```text
現在のセッションは、これまで可読であったユーザーTrajectoryと暫定的に継続可能な程度に整合している。
```

Stabilityは数値的な認証スコアと同一ではない。スコアは \(L_n\) の一つの証拠となり得るが、Stability Sceneには未解決条件 \(U_n\) と継続条件 \(C_n^{+}\) も含まれる。例えば、新しいネットワーク位置が未解決のままでも、セッション全体は局所的に可読であり得る。

Differenceは単一スカラーではなく、異種要素からなる対象として表せる。

\[
\Delta_{B,c,\Sigma}(x)
=
(
\Delta_{\mathrm{device}},
\Delta_{\mathrm{behavior}},
\Delta_{\mathrm{network}},
\Delta_{\mathrm{time}},
\Delta_{\mathrm{motion}}
).
\]

これらの成分は、同じ単位や距離条件を共有する必要がない。Differenceのパターンが、通常のdriftから疑わしい挙動への区別として扱われるとき、Boundaryが可読になる。したがってBoundaryはDifference tupleそのものではない。

この例は、Incorporated Readabilityが後続認証の条件を変えることも示す。以前に受理された端末、確認済みの移動パターン、回復過程などは、その後のreadability contextを変化させ得る。これは過去観測の保存以上のものであり、後続のDifferenceの解釈を変える。

## 14.4 例4：社会規範の成立

男女平等という社会的認識を考える。その規範が成立する以前から、社会には制度、実践、対立、言語、認識可能な複数の形が存在する。これらは、多様な成立が可能なStructureとして扱える。

Sliceは、法改正、公共的議論、社会運動、教育、制度解釈などを通じて生じ得る。一つのSliceが、すでに完成済みの規範を抽出すると仮定する必要はない。例えば、次のようなlocal articulationが現れる。

```text
この領域では、平等な取扱いが正当な基準として認識される。
```

この表出が、行為、解釈、制度運用を導ける程度に可読になると、局所的Stability Sceneが成立する。しかし、執行、文化的実践、例外、競合制度には未解決の局所的な未が残り得る。したがってStabilityは、Structure全体の閉包やDifferenceの消失を意味しない。

平等の可読性が織り込まれると、後続の法律、紛争、解釈は、平等がすでに利用可能な基準となったContextから始まる。この例は、Incorporated Readabilityが後続の成立条件を変えることを示す。

また、この例におけるTrajectoryは、単なる出来事の時系列一覧ではない。社会運動、法律、判決、制度、実践の間のどの関係を、現在のContextで許容可能かつ追跡可能とみなすかによって、歴史的Trajectoryは異なる形で読まれる。法的連続性、概念的継承、政治的闘争、制度実装など、複数のTrajectory readingが成立し得る。

## 14.5 例5：欠測データとTrajectoryの空白

センサーシステムに、測定が記録されなかった区間がある場合を考える。時系列ログには空白が存在する。しかし、その空白だけではTrajectory breakは成立しない。

欠測区間の前後の局所的realizationを \(g_i\)、\(g_j\) とする。モデル制約、物質的連続性、冗長センサー、後続証拠などを通じて許容可能な関係を辿れるなら、Continuity Readabilityは維持され得る。

\[
\exists r:
\operatorname{Adm}(r)
\land
\operatorname{Traceable}(g_i,g_j;r)
\land
\operatorname{Readable}(r).
\]

逆に、完全かつ高密度なログが存在しても、可読なTrajectoryが保証されるわけではない。記録された出来事に許容可能な関係が存在しない場合、Contextが互換でない場合、またはRe-Sliceを経なければ連続性が理解できない場合がある。

この例は、次の区別を維持する。

```text
record continuity
≠
Trajectory continuity
```

さらに、関係保持場 \(\mathcal{G}_R=(G,E)\) がTrajectoryそのものではない理由も示す。同一のイベント場から異なる文脈的Tracingが成立し得て、現在のSliceでは不可読な関係も残り得る。

## 14.6 例6：「九州以外の都道府県」の検索

「日本の都道府県のうち、九州以外」を検索する場合を考える。データベース実装では、全都道府県集合を取得し、九州に属する集合を特定し、集合差を計算できる。この実装は、対象、所属関係、地域分類がすでに利用可能な領域では妥当である。

しかしGyro Logic上の重要点は、単なる集合差ではない。この問い合わせは、すでに成立している分類に相対的な否定条件が可読になるSliceを開く。結果は絶対的な非存在ではなく、次の関係的表出である。

```text
現在の九州所属条件を満たさない都道府県
```

Differenceは距離ではなく、カテゴリー的な非一致となり得る。Boundaryは現在のSliceのもとで可読な地域区別である。「九州ではない」「何もない」「不明」「空欄」「Void」を一つの状態へ潰してはならない。この例は、否定、欠如、非所属、不可読性を別々に扱う必要があることを示す。

## 14.7 例を横断した観察

以上の例には、共通する区別が現れる。

第一に、Structureは現在の観測へ還元できない。局所的成立が利用可能になるための組織化された条件を含む。

第二に、Sliceは事前存在する結果の取得だけでは十分に表せない。OrientationとContextに相対的なlocal articulationが現れる。

第三に、local articulationが利用可能になっても、直ちにStableとは限らない。Stabilityは単なる出現ではなく、可読性と継続可能性に関わる。

第四に、Stabilityは完全解決を要求しない。残存する局所的な未を含み得る。

第五に、一度可読になったものは、保存履歴と同一でない仕方で後続条件を変え得る。

第六に、Identity、関係の存在、Traceability、Continuity Readability、Trajectoryは区別されなければならない。

第七に、Differenceは異種的かつ非距離的であり得て、Boundaryは派生的な可読区別である。

これらの例は形式モデルを証明するものではない。しかし、論理的、物質的、計算的、社会的、観測的な複数領域において、一つの普遍的数学実装を要求せずに本モデルの区別を使用できることを示す。次章ではモデルの限界を検討し、未解決の主張を明確にする。

# 15 限界と未解決課題

## 15.1 本モデルの射程

本論文で提案するMinimal Formal Modelは、意図的に限定されたモデルである。その目的は、Gyro Logic内部で形成されてきた複数の区別を保持し、それらを簡潔で内部整合的な形式スキーマへ整理することにある。完全な公理化、普遍的意味論、または理論の最終的な数学的基礎を提示するものではない。

したがって本モデルは、概念理論と領域固有実装の中間に位置する。明示的な対象、関係、更新則、分離条件を導入する点で単なる比喩より強いが、複数の数学型、許容可能性条件、合成則を意図的に未確定のまま残す点で、完全に規定された形式体系より弱い。

## 15.2 数学型の暫定性

本モデルは、Structureに対して一つの普遍的数学型を確定しない。Structureは、対象領域に応じて、状態的、関係的、空間的、論理的、組織的、または過程的に表現され得る。しかし、これらのいずれもGyro Logicの普遍的存在論へ昇格させない。

同じ制約は、Slice、Stability、Context、Difference、Trajectoryにも当てはまる。記法

\[
S_n \xRightarrow{\Sigma_{B_n,c_n}} a_n
\]

は、Slice processとlocal articulationを分離するが、\(\Sigma\)を最終的に関係、部分写像、遷移、process object、event、morphism、その他の数学的構成のどれとして扱うべきかまでは定めない。同様に、

\[
K_n=(a_n,L_n,U_n,C_n^{+})
\]

はStability Sceneの構造化表現であり、あらゆるStability Sceneが本質的に四成分タプルであるという主張ではない。

## 15.3 厳密な最小性は証明されていない

本論文における「minimal」は、現在の理論的区別を保持するために必要な以上の形式的コミットメントを導入しないという設計方針を意味する。本論文は、このスキーマが一意に最小であること、要素数の意味で最小であること、または特定の理論順序のもとで最小であることを形式的に証明していない。

より強い最小性を示すには、少なくとも次が必要となる。

1. 許容される形式モデルのクラスの厳密な定義
2. Canonical Conceptを保持するための形式的保存条件
3. 候補モデル間の順序または比較関係
4. いずれかの構成要素を除くと必要な区別の少なくとも一つが失われることの証明

これらは今後の課題である。

## 15.4 Readabilityの意味論は未完成である

Readabilityは、Stability、Incorporated Readability、Continuity Readability、Boundary、Trajectoryの中心にある。しかし、本モデルはReadabilityの完全な意味論をまだ与えていない。

Readabilityを次のいずれとして扱うべきかは未解決である。

- 二値述語
- 段階量
- 文脈的判断
- 推論上の利用可能性関係
- アクセス可能性構造
- 観測者相対的条件
- 領域固有の異種関係族

本モデルはこれらを許容するが、普遍的解釈を一つ選択しない。これは意図的な開放性である一方、理論の予測精度と計算精度を制限する。

## 15.5 OrientationとContextは十分に規定されていない

Operator OrientationとContextは、Slice、Difference、Continuity Readability、Boundary、Trajectoryを条件づける。本モデルでは形式パラメータとして表すが、その内部構造は十分に規定していない。

主要な未解決課題は次である。

- Orientationは構造化状態、方針、関係、高階制約のどれとして扱うべきか
- Contextは利用可能な条件集合、推論閉包、局所環境、動的更新構造のどれとして扱うべきか
- OrientationとContextはどのように相互作用するか
- 競合する複数のOrientationをどのように表現するか
- ContextをStructureへ還元せず、Slice中のContext変化をどう扱うか

これらは理論モデル、計算モデル、応用モデルで異なる解決を必要とする可能性がある。

## 15.6 AdmissibilityとTraceabilityには領域基準が必要である

Continuity Readabilityは、暫定的に次のように表される。

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma)
\iff
\exists r\,
\bigl(
\operatorname{Adm}(r)
\land
\operatorname{Traceable}(r)
\land
\operatorname{Readable}(r)
\bigr).
\]

この式はAdmissibility、Traceability、Readabilityを分離するが、普遍的なAdmissibility基準を定義しない。実際には、因果的、論理的、物質的、意味的、制度的、時間的、セキュリティ的制約に依存し得る。

したがって領域モデルは、少なくとも次を規定しなければならない。

- 許容される関係型
- 関係を支持する証拠
- 競合関係の扱い
- Traceが断たれたと判断する条件
- Tracingの不確実性の表現

このような基準がない限り、contextual tracingは実行手法ではなく形式スキーマにとどまる。

## 15.7 Trajectory再構成はまだアルゴリズム化されていない

本モデルは、関係を保持するtrace field

\[
\mathcal{G}_R=(G,E)
\]

と、可読なTrajectory

\[
T_{B,c,\Sigma_T,\Gamma_T}
=
\operatorname{Trace}_{B,c,\Sigma_T,\Gamma_T}(G,E)
\]

を分離する。しかしTracing operatorは、まだアルゴリズムとして定義されていない。

本論文は次を規定しない。

- 探索順序
- 停止条件
- 競合解消
- 分岐選択
- 空白処理
- 不確実性伝播
- 遡及的修正のコスト
- 計算量

今後は、contextual tracingをグラフ探索、イベント構造解析、制約伝播、確率推論、圏論的合成、またはそれらのハイブリッドとして実装すべきかを検討する必要がある。

## 15.8 Differenceには普遍的な値域がない

本モデルは、意図的に

\[
\Delta_{B,c,\Sigma}:X\rightharpoonup D
\]

という異種値域 \(D\) を許容する。これによりDifferenceをスカラー距離や誤差へ還元することを避けるが、異なるDifference型をどのように比較、合成、集約、伝播するかは未解決となる。

今後の課題には次が含まれる。

- 異種Difference値間の適合性定義
- 二つのDifference記述が同値となる条件
- 局所Differenceと累積Differenceの区別
- DifferenceをゼロにすることなくStability evidenceへ関連づける方法
- DifferenceがBoundaryとして可読化される過程の形式化

## 15.9 Stabilityに普遍的評価規則はない

本モデルはStabilityとStability scoreを区別するが、local articulationが可読かつ継続可能な成立になったかどうかを判断する普遍的手続きを与えない。

領域固有モデルでは、閾値、論理充足、位相的近傍、不変条件、頑健性尺度、信頼区間、多基準判断などを利用し得る。Minimal Formal Modelは、これらのいずれか一つを普遍的規則として選択しない。

このことは理論的一般性を保持する一方で、領域固有の評価関数なしに普遍的Stability判断を生成できないことを意味する。

## 15.10 Incorporated Readabilityの操作的同定は未完成である

更新

\[
\Gamma_{n+1}
=
\operatorname{Update}_{\Gamma}(\Gamma_n,q_n,e_n)
\]

は、追加、修正、統合、重み変更、無効化、抑制、アクセス不能化を許容する。しかし、\(q_n\)をrealizationからどのように抽出するか、競合するincorporated elementをどう調停するか、またIncorporated Readabilityの効果を通常の記憶やparameter updateから実証的にどう区別するかは未定義である。

今後は、Incorporated Readabilityの観測可能な基準を確立し、複数領域で一貫して操作化できるかを検証する必要がある。

## 15.11 実証的検証は限定的である

Illustrative Examplesは概念分離可能性を示すが、実証的妥当性を示すものではない。数学的推論、変形、認証、社会規範、欠測データ、否定検索においてモデルが区別を整理できることは示すが、競合理論より優れた予測、説明、実装を与えることを証明しない。

実証的検証には、少なくとも次が必要である。

- 明示的なデータセットまたはイベントTrace
- 形式用語の操作的定義
- 比較対象となるbaseline model
- 測定可能な成功・失敗基準
- 再現可能な実験またはsimulation

GyroOSまたはGyroAuthによるPoCは一つの検証経路となり得るが、応用上の成功を普遍理論の証明とみなしてはならない。

## 15.12 既存数学との関係にはさらに深い検討が必要である

比較章では、関係構造、グラフ理論、位相、力学系、イベント構造、圏論、証明論、制約伝播、確率、sheaf-like structure、process algebraとの部分的対応を示した。しかし、これらの比較はまだ予備的である。

今後、より厳密に検討すべき論点には次がある。

- local articulationをpartial algebraまたはevent semanticsで表せるか
- Stability Sceneが近傍、sheaf、domain theory的表現を許すか
- Incorporated Readabilityを非単調論理またはbelief revisionで表せるか
- contextual tracingがpath category、event structure、provenance modelに対応するか
- 異種Differenceをenriched relation、ordered structure、typed fieldとして扱えるか

目標は強制的還元ではなく、比較と統制された特殊化であるべきである。

## 15.13 未解決課題：Formal Securityと敵対的条件

認証または脆弱性対応へ適用する場合、敵対的操作が中心課題となる。攻撃者はcriterionをpoisoningし、Contextを改変し、偽のcontinuityを構成し、Differenceを抑制し、誤ったStabilityを誘発する可能性がある。

Formal Security拡張では、少なくとも次を定義する必要がある。

- 信頼済み証拠と未信頼証拠
- \(\Gamma\)に対する敵対的更新
- criterion poisoning
- false continuity construction
- Boundary manipulation
- rollback、freeze、defer、review、isolationの意味論
- 明示的な保証事項と非保証事項

これらはモデルのセキュリティ特殊化に属し、普遍Coreへ暗黙に持ち込んではならない。

## 15.14 未解決課題：局所realizationの形式的合成

本モデルは局所realizationを

\[
g_n=(S_n,B_n,c_n,\Sigma_n,a_n,K_n)
\]

とするが、普遍的合成演算

\[
g_i \circ g_j
\]

を定義していない。

合成は時間的、因果的、論理的、意味的、物質的、文脈的であり得る。異なる関係型には異なる合成則が必要となる可能性がある。今後は、局所realizationがいつ合成可能か、合成が結合的か、部分的か、Re-SliceとJumpが合成へどう影響するかを検討する必要がある。

## 15.15 未解決課題：モデル改訂基準

本モデルは明示的に暫定的であるため、改訂基準が必要となる。候補構成は、次の場合に修正されるべきである。

- Canonical Definitionと衝突する
- 保持すべき区別を潰す
- 不要な存在論的前提を導入する
- 重要領域で機能しない
- 理論的利益なしに実装を妨げる
- 観測的または推論的証拠へ接続できない

形式モデルは、それが明確化しようとする理論に従属し続けなければならない。

## 15.16 限界の要約

本モデルは、次をまだ提供しない。

- Structureの最終存在論
- Sliceの普遍数学型
- Readabilityの完全意味論
- 普遍的Stability metric
- 普遍的Difference codomain
- 実行可能なTracing algorithm
- 厳密な最小性証明
- 完全なFormal Security Model
- 複数領域にわたる実証的妥当性

本モデルが提供するのは、規律ある形式的境界である。どの区別を保持すべきか、どの還元が現時点で正当化されないか、どの構成要素にさらなる数学的・計算的・実証的研究が必要かを明示する。

したがって最終章では、本論文の中心的主張へ戻る。Minimal Formal Modelの価値は、Gyro Logicを一つの完成済み数学体系へ閉じることではなく、比較、検証、改訂、実装を体系的に進められる程度まで、現在のコミットメントを明示することにある。

# 16 結論

本論文は、Gyro Logicの不変Coreを維持したまま、探索的なMinimal Formal Modelを提示した。

```text
Structure
↓
Slice
↓
Stability
```

本研究の目的は、Canonical Definitionを数式へ置き換えることでも、Gyro Logicを既存の一つの数学分野へ還元することでもなかった。中心的な問いは、現在の理論が必要とする条件よりも強い前提を導入することなく、形成されてきた概念上の区別を、最小限で内部整合的な形式スキーマとして整理できるか、というものであった。

提案モデルは、この問いに対して暫定的に肯定的な回答を与える。Structureは、一つの普遍的数学対象型へ固定せずに扱われる。Sliceは、Slice processと、その過程を通じて利用可能になるlocal articulationとに分離される。Stabilityは、一つの表出が継続可能な成立として読めるようになる構造化された局所場面として表され、その内部には残存する局所的な未が残り得る。Incorporated Readabilityは保存履歴から分離され、後続の可読性条件を変化させる非単調な更新として扱われる。Continuity ReadabilityはIdentityから分離され、Trajectoryは状態列、ログ、出来事の累積から分離され、局所的Gyro realization間の許容可能な関係を文脈的に辿ることで読まれる構成として扱われる。Differenceは距離、数値誤差、Boundaryから分離され、Boundaryは派生的な可読区別として位置づけられる。

局所的Gyro realizationは、暫定的に次のように表される。

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
\bigr)
\]

Coreに対応する関係は、次のとおりである。

\[
S_n
\xRightarrow{\Sigma_{B_n,c_n}}
a_n
\xRightarrow{\operatorname{Stab}}
K_n.
\]

一つのrealizationから織り込まれる可読性は、次のように表される。

\[
q_n=\operatorname{Inc}(g_n),
\]

\[
\Gamma_{n+1}
=
\operatorname{Update}_{\Gamma}
(\Gamma_n,q_n,e_n),
\]

また、後続Structureの条件は、次の関係を通じて生じ得る。

\[
(S_n,\Gamma_{n+1},e_n)
\rightsquigarrow
S_{n+1}.
\]

Continuity Readabilityは、許容可能で、追跡可能で、かつ可読な関係の存在によって特徴づけられる。Trajectoryは、関係を保持する場に対する文脈的Tracing operationとして表される。Differenceは、部分的かつ異種的な写像として、弱く次のように型付けされる。

\[
\Delta_{B,c,\Sigma}:X\rightharpoonup D.
\]

これらの表現は、最終的な公理化を構成するものではない。その意義は、次の区別を維持することにある。

```text
Slice process
≠
local articulation
≠
Stability
```

```text
stored history
≠
Incorporated Readability
```

```text
Identity
≠
Continuity Readability
```

```text
relation field
≠
Trajectory
```

```text
Difference
≠
Distance
≠
Error
≠
Boundary
```

既存数学分野との比較からは、関係構造、グラフ、位相、力学系、遷移系、圏論、証明論、制約伝播、プロセス代数、および関連する枠組みが、それぞれ有効な部分モデルを与え得ることが確認された。一方で、現時点では、単一の数学分野だけでGyro Logic全体を表現しようとすると、上記の区別の一部を失わせる前提が導入される。したがって、現段階で適切なのは、既存数学から孤立した独自体系を直ちに主張することでも、一分野へ早期に還元することでもない。明示された前提のもとで、領域ごとの数学モデルが理論の異なる部分を具体化できる、異種的な形式構成として扱うことである。

本論文は、既存のGyro Logic基礎論文に対する形式化上の補完論文として位置づけられる。基礎論文が「Gyro Logicとは何か」を扱うのに対し、本論文は、現在の概念的区別を、数学的比較、検証、後続実装へ向けてどのように最小限に整理できるかを扱う。したがって、両論文は重複するものではなく、異なる役割を持ちながら相互補完的である。

今後は、本モデルをより厳密に検証する必要がある。主要な課題には、Readability、Admissibility、Traceabilityの領域別意味論、局所的realization間の合成、実行可能モデルまたはSimulationの構築、非単調なIncorporated Readabilityの評価、敵対的更新およびcriterion poisoningの形式化、Minimal Formal Model v1.1または後続の公理モデルが必要かどうかの判断が含まれる。

本研究の到達点は、意図的に限定されている。提案スキーマが一意に最小であること、複数領域において実証的に妥当であること、計算的に決定可能であること、または完全であることは証明していない。本論文が示したのは、より限定的であるが必要な基盤である。すなわち、Gyro Logicは、不変Coreを変更せず、その中心的区別を既存の狭い数学形式へ潰すことなく、規律ある形式構成として整理可能である。

# 利益相反・研究資金・データ／コードの利用可能性

## 利益相反

著者は、本研究に関連して申告すべき利益相反がないことを表明する。

## 研究資金

本研究は外部資金の提供を受けていない。

## データの利用可能性

本研究は理論研究であり、新たな実証データセットの生成または解析は行っていない。

## AI支援ツールの使用

本稿の作成にあたり、構成整理、草稿作成補助、表現調整、整合性確認のためにAI支援ツールを使用した。本文の内容、主張、参考文献、最終原稿については著者が確認・編集し、全責任を負う。

## コードおよび関連資料の利用可能性

論文原稿、図、統合スクリプト、PDF生成Workflow、および検証スクリプトは、Gyro Logicリポジトリで公開している：[https://github.com/gitGyro-Dev/gyrologic](https://github.com/gitGyro-Dev/gyrologic)。

# 参考文献
