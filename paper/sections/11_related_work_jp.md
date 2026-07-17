# Related Workと形式的位置づけ

## Gyro Logic基礎論文との関係

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

## 関係構造とグラフモデル

関係構造およびグラフ理論は、異種の局所的realizationと保持された関係を表現するための自然な資源を提供する。標準的なグラフ理論は、頂点、辺、経路、連結性、分岐、グラフ変換を明示的に扱う [@diestel2017graph]。これらは、関係を保持するtrace field

\[
\mathcal{G}_R=(G,E)
\]

の表現に直接利用できる。

ただし、表現済みのグラフは通常、関連するnodeとedgeがすでに個体化されていることを前提とする。したがってGyro Logicにおけるrelation-bearing fieldと可読なTrajectoryの区別は、グラフ表現だけでは尽くされない。グラフは候補関係を保持し、TrajectoryはAdmissibilityとReadabilityの条件下で文脈的Tracingを行った結果として読まれる。

## Event Structureと並行性

Event Structureは、一つのinterleavingされた列へシステムを還元することなく、出来事、因果依存、競合、並行性を表現するために発展してきた。Petri net・Event Structure・domainの古典的な関係は、出来事と因果的組織がconfiguration-based semanticsをどのように支えるかを厳密に示している [@nielsen1981petri]。後続研究では、configuration structure、Event Structure、Petri net間の対応がさらに整理された [@vanglabbeek2009configuration]。

これらは、分岐、合流、競合、半順序、非線形Trajectoryに特に関係する。一方で、形式的に表現されたeventと、enableまたはconflict関係から開始する。Gyro Sliceが扱うのは、それより前または弱いコミットメント、すなわちlocal articulationが利用可能になる過程である。したがってEvent Structureは、実現済みGyro Processの領域固有表現として有力であるが、StructureまたはSliceの普遍的存在論としては採用しない。

## Transition System・Model Checking・Process Algebra

Transition SystemとModel Checkingは、状態、label、transition relationが規定された後の状態発展、分岐挙動、時間的性質、検証に対して精密な技法を提供する [@baier2008principles]。Process Algebraも、相互作用、並行性、同期、継続を合成的に表現する。MilnerのCalculus of Communicating Systemsは、その基礎的な例である [@milner1980ccs; @milner1982combinators]。

これらは、Gyro Process、Gyro Loop、Operator Response、Re-Slice、Defer、Jumpに関係し、GyroOS実装に有用である。ただし、事前定義されたtransitionまたはaction vocabularyを、articulationを可能にするより一般的なStructureと同一視する危険がある。本論文ではProcess AlgebraとTransition Systemを、実装層または領域層の形式化として扱い、不変Coreの置換定義には用いない。

## Dynamical SystemとStability

Dynamical Systemは、trajectory、equilibrium、attractor、oscillation、convergence、bifurcation、perturbationに関する確立されたモデルを提供する [@strogatz2015nonlinear]。状態空間と発展則が正当化される場合、特に測定可能なGyroOSまたはGyroAuthの挙動に有効である。

Gyro Stabilityは、dynamical stabilityより意図的に広い。局所的に可読かつ継続可能な成立に関わり、変化の継続および残存する未と共存し得る。同様に、Gyro Trajectoryを時間添字付き状態解へ普遍的に同一視しない。したがってDynamical Systemは重要な特殊化であるが、equilibrium、convergence、invarianceをStabilityの普遍的定義にはできない。

## Topology・局所性・Sheaf-like Structure

Topologyは、近傍、連続性、閉包、分離、境界を形式化する [@munkres2000topology]。local articulationの周囲における局所的持続と許容変動の表現に有用である。Sheaf theoryは、局所情報、restriction、compatibility、局所データが一つのglobal objectへglueできない可能性を扱う、より豊かな言語を提供する [@maclane1992sheaves]。

これらは、Stability Sceneの局所性、および局所的成立と全体非閉包の区別に対応する。また、重なり合うContext間の可読性を支える可能性がある。ただしTopologyとSheaf theoryは、基礎空間、site、covering、restriction structureが特定されていることを必要とする。本モデルは、それらがすべての領域でSlice以前から利用可能であるとは仮定しない。

## Category Theoryと合成

Category Theoryは、object、morphism、composition、identity、functor、構造保存的translationの一般言語を提供する [@maclane1998categories]。均質な一つの状態型を要求せず、領域固有Gyroモデルを合成し、異なるcontinuity形式を関係づける枠組みとして有望である。

主な注意点は、通常のmorphismが指定済みのdomainとcodomainを持つことである。一般的Slice relationは、local articulationがSlice process以前から完全に個体化されたcodomainとして利用可能であるとは仮定しない。したがってCategory Theoryは、適切な局所objectとmorphismが正当化された後の合成枠組みとなり得るが、StructureまたはSliceの最初からの普遍型としては課さない。

## Belief Revisionと非単調Context更新

AGM belief revisionは、明示的なpostulateによってbelief setの合理的なcontractionとrevisionを形式化する [@alchourron1985logic]。これは、Incorporated Readabilityの非単調的側面、特に後続推論が利用できるものの追加、修正、無効化、重み変更に直接関係する。

ただしIncorporated Readabilityは、belief revisionより広い。readability context \(\Gamma\) はdeductive closureされたbelief setである必要はなく、織り込みは命題的ではなく、物質的、手続的、知覚的、制度的、運用的であり得る。したがってAGM型revisionは論理Contextに対する強い部分モデルであるが、Incorporationの普遍的解釈ではない。

## 確率・統計モデル

確率と統計は、event modelと測定変数が規定された後、不確実性、信頼度、証拠、異種観測を定量化できる。Probabilistic Graphical Modelは、不確実性下の構造化された依存関係と推論に関する成熟した枠組みを提供する [@koller2009probabilistic]。

これらは、段階的Readability、Stability confidence、Difference distribution、競合するTrajectory仮説を具体化し得る。一方、それ自体では、関連する変数、event、distinctionがどのように局所的にarticulableになるかを説明しない。したがってProbabilityは、Gyro Logicの一般意味論ではなく、領域固有の定量層として扱う。

## 本モデルの形式的位置づけ

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