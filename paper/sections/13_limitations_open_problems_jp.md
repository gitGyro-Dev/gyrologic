# 限界と未解決課題

## 本モデルの射程

本論文で提案するMinimal Formal Modelは、意図的に限定されたモデルである。その目的は、Gyro Logic内部で形成されてきた複数の区別を保持し、それらを簡潔で内部整合的な形式スキーマへ整理することにある。完全な公理化、普遍的意味論、または理論の最終的な数学的基礎を提示するものではない。

したがって本モデルは、概念理論と領域固有実装の中間に位置する。明示的な対象、関係、更新則、分離条件を導入する点で単なる比喩より強いが、複数の数学型、許容可能性条件、合成則を意図的に未確定のまま残す点で、完全に規定された形式体系より弱い。

## 数学型の暫定性

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

## 厳密な最小性は証明されていない

本論文における「minimal」は、現在の理論的区別を保持するために必要な以上の形式的コミットメントを導入しないという設計方針を意味する。本論文は、このスキーマが一意に最小であること、要素数の意味で最小であること、または特定の理論順序のもとで最小であることを形式的に証明していない。

より強い最小性を示すには、少なくとも次が必要となる。

1. 許容される形式モデルのクラスの厳密な定義
2. Canonical Conceptを保持するための形式的保存条件
3. 候補モデル間の順序または比較関係
4. いずれかの構成要素を除くと必要な区別の少なくとも一つが失われることの証明

これらは今後の課題である。

## Readabilityの意味論は未完成である

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

## OrientationとContextは十分に規定されていない

Operator OrientationとContextは、Slice、Difference、Continuity Readability、Boundary、Trajectoryを条件づける。本モデルでは形式パラメータとして表すが、その内部構造は十分に規定していない。

主要な未解決課題は次である。

- Orientationは構造化状態、方針、関係、高階制約のどれとして扱うべきか
- Contextは利用可能な条件集合、推論閉包、局所環境、動的更新構造のどれとして扱うべきか
- OrientationとContextはどのように相互作用するか
- 競合する複数のOrientationをどのように表現するか
- ContextをStructureへ還元せず、Slice中のContext変化をどう扱うか

これらは理論モデル、計算モデル、応用モデルで異なる解決を必要とする可能性がある。

## AdmissibilityとTraceabilityには領域基準が必要である

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

## Trajectory再構成はまだアルゴリズム化されていない

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

## Differenceには普遍的な値域がない

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

## Stabilityに普遍的評価規則はない

本モデルはStabilityとStability scoreを区別するが、local articulationが可読かつ継続可能な成立になったかどうかを判断する普遍的手続きを与えない。

領域固有モデルでは、閾値、論理充足、位相的近傍、不変条件、頑健性尺度、信頼区間、多基準判断などを利用し得る。Minimal Formal Modelは、これらのいずれか一つを普遍的規則として選択しない。

このことは理論的一般性を保持する一方で、領域固有の評価関数なしに普遍的Stability判断を生成できないことを意味する。

## Incorporated Readabilityの操作的同定は未完成である

更新

\[
\Gamma_{n+1}
=
\operatorname{Update}_{\Gamma}(\Gamma_n,q_n,e_n)
\]

は、追加、修正、統合、重み変更、無効化、抑制、アクセス不能化を許容する。しかし、\(q_n\)をrealizationからどのように抽出するか、競合するincorporated elementをどう調停するか、またIncorporated Readabilityの効果を通常の記憶やparameter updateから実証的にどう区別するかは未定義である。

今後は、Incorporated Readabilityの観測可能な基準を確立し、複数領域で一貫して操作化できるかを検証する必要がある。

## 実証的検証は限定的である

Illustrative Examplesは概念分離可能性を示すが、実証的妥当性を示すものではない。数学的推論、変形、認証、社会規範、欠測データ、否定検索においてモデルが区別を整理できることは示すが、競合理論より優れた予測、説明、実装を与えることを証明しない。

実証的検証には、少なくとも次が必要である。

- 明示的なデータセットまたはイベントTrace
- 形式用語の操作的定義
- 比較対象となるbaseline model
- 測定可能な成功・失敗基準
- 再現可能な実験またはsimulation

GyroOSまたはGyroAuthによるPoCは一つの検証経路となり得るが、応用上の成功を普遍理論の証明とみなしてはならない。

## 既存数学との関係にはさらに深い検討が必要である

比較章では、関係構造、グラフ理論、位相、力学系、イベント構造、圏論、証明論、制約伝播、確率、sheaf-like structure、process algebraとの部分的対応を示した。しかし、これらの比較はまだ予備的である。

今後、より厳密に検討すべき論点には次がある。

- local articulationをpartial algebraまたはevent semanticsで表せるか
- Stability Sceneが近傍、sheaf、domain theory的表現を許すか
- Incorporated Readabilityを非単調論理またはbelief revisionで表せるか
- contextual tracingがpath category、event structure、provenance modelに対応するか
- 異種Differenceをenriched relation、ordered structure、typed fieldとして扱えるか

目標は強制的還元ではなく、比較と統制された特殊化であるべきである。

## 未解決課題：Formal Securityと敵対的条件

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

## 未解決課題：局所realizationの形式的合成

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

## 未解決課題：モデル改訂基準

本モデルは明示的に暫定的であるため、改訂基準が必要となる。候補構成は、次の場合に修正されるべきである。

- Canonical Definitionと衝突する
- 保持すべき区別を潰す
- 不要な存在論的前提を導入する
- 重要領域で機能しない
- 理論的利益なしに実装を妨げる
- 観測的または推論的証拠へ接続できない

形式モデルは、それが明確化しようとする理論に従属し続けなければならない。

## 限界の要約

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