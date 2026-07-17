# 過程および局所的表出としてのSlice

## Canonical Definition

SliceのCanonical Definitionは変更せず、次のとおり維持する。

> **Sliceとは、Structureの中に、一つの成立へ向かう道筋が開かれる過程である。**

この定義は、形式化に対して二つの直接的な制約を課す。第一に、Sliceは完了した対象ではなく、過程である。第二に、成立へ向かう道筋は、その過程を通じて開かれるのであり、必ずしもSlice以前から完全に個体化された対象として存在し、抽出されるのを待っているとは限らない。

したがって本モデルは、Sliceを、結果空間があらかじめ確定している操作と区別する。ろ過、射影、選択、検索、分割、通常の抽出は、特定領域におけるSliceの実装となり得るが、いずれもSliceの普遍的意味としては採用しない。

## 抽出モデルが不十分である理由

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

## Slice processとlocal articulation

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

## slice-ingとslice-done

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

## OrientationとContextの役割

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

## SliceはStructureを消費しない

Sliceの過程は、Structureが使い尽くされること、消費されること、または前景だけが残って背景が失われるように分割されることを意味しない。高度に確定したarticulationが現れた場合でも、Structureには別の関係、可能なarticulation、未解決条件、代替経路が残り得る。

したがって、

```text
Slice後のStructure
≠
Structureから結果を差し引いたもの
```

である。

Sliceは、特に可読性が後続文脈へ織り込まれる場合、後にStructureへ接近する条件を変化させ得る。しかし、その変化を文字どおりの減算と混同してはならない。また、Structureに生じるすべての変化をSliceへ帰属させてもならない。外部相互作用、環境変化、物質変換、その他の過程も、後続realizationの条件を変化させ得る。

## 局所性と非閉包

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

## Sliceに関する最小限の形式的コミットメント

本論文は、Sliceについて次の点にコミットする。

第一に、Sliceは過程的であり、静的な写像結果だけと同一視できない。

第二に、過程とlocal articulationを区別できる。

第三に、local articulationは、Slice以前から完全に個体化された対象として存在している必要はない。

第四に、OrientationとContextはSliceを条件づけるが、新たなCore段階にはならない。

第五に、local articulationの出現はStabilityを含意しない。

第六に、Sliceは必ずしもStructureを消費または閉包しない。

第七に、抽出、射影、ろ過、分類、選択は領域固有の実装となり得るが、Sliceを普遍的には定義しない。

## 明示的にコミットしないこと

本モデルは、すべてのSliceが一意の結果をもつこと、すべてのSliceが終了すること、Sliceが決定論的であること、articulation空間が事前に固定されること、Orientationが人間の観測者に属すること、Contextが完全に表現可能であること、slice-doneが不可逆であることを主張しない。

また、「道筋が開かれる」という表現が、文字どおりの幾何学的経路を意味するとも主張しない。道筋は、関係的、論理的、手続的、意味的、因果的、物質的、制度的、その他の領域固有の形を取り得る。形式モデルは、path-openingの構造的役割を保持しつつ、その具体化を開いたままにする。

## Stabilityへの接続

local articulation \(a_n\) は、次の形式的区別に必要な結果を与えるが、まだStability Sceneではない。articulationからStabilityへの移行では、そのarticulationが、関連するStructure・Orientation・Contextのもとで、継続可能な成立として読めるかを問う。

暫定的には、

\[
K_n
=
\mathsf{StabScene}(a_n;S_n,B_n,c_n)
\]

と書く。

次章では、この関係を検討し、Stabilityをスカラー、固定点、終端条件ではなく、構造化された局所場面として展開する。
