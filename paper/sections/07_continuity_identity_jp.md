# Continuity ReadabilityとIdentity

## 局所的成立から関係的連続性へ

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

## 局所的Gyro realization

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

## 関係の存在

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

## Traceability

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

## Admissibility

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

## Continuity Readability

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

## Context相対的なContinuity Readability

Continuity Readabilityは、あらゆる読み方に対して普遍的ではない。同じ二つのrealizationであっても、一つのOrientationでは連続的に読まれ、別のOrientationでは非連続または未確定として読まれ得る。

\[
\operatorname{CR}(g_i,g_j;B_1,c_1,\Sigma_1,\Gamma_1)
\neq
\operatorname{CR}(g_i,g_j;B_2,c_2,\Sigma_2,\Gamma_2)
\]

これは連続性が恣意的であることを意味しない。どの関係が許容可能であり、どのように読めるかが、明示された条件に依存することを意味する。

後続のRe-Sliceによって、以前は不可読だった関係が可視化される場合がある。逆に、以前受け入れられていた関係が棄却されたり、連続性の読みが再構成されたりする場合もある。したがってContinuity Readabilityは、無制約ではないまま修正可能である。

## Identityを別の基準として扱う

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

## Identityを伴わないContinuity

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

## 可読なContinuityを伴わないIdentity

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

## Continuity ReadabilityとDifference

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

## Continuity ReadabilityとIncorporated Readability

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

## 二値形式と段階形式

Minimal Formal Modelでは述語形式が有用であるが、応用によっては段階値が必要になる。

\[
\operatorname{CR}^{*}(g_i,g_j;B,c,\Sigma,\Gamma)
\in \mathcal{C}
\]

ここで \(\mathcal{C}\) は、順序集合、信頼区間、証拠構造、または領域固有の分類であり得る。

本論文は、Continuityが普遍的に二値または数値であることを要求しない。Boolean形式は、統合スキーマに必要な最小限の論理的区別のみを表す。

## 最小限のコミットメント

提案モデルがコミットするのは、次のみである。

1. 局所的Gyro realization間には関係が成立し得る。
2. 関係の存在、Traceability、Admissibility、Readabilityは区別される。
3. Continuity ReadabilityはOrientation・Context・Slice・Incorporated Readabilityに依存する。
4. Identityは別の基準によって扱われる。
5. ContinuityはDifferenceやIdentity変化をまたいで成立し得る。
6. Continuityが不可読または論争的でもIdentityが主張され得る。
7. Continuity readingはRe-SliceとContext更新によって修正され得る。

本モデルは、Continuityが同値関係であること、あらゆる領域で推移的であること、対称的であること、全域的に決定可能であること、一つのIdentity基準が普遍的に適用されることを仮定しない。

## 文脈的Trajectoryへの接続

Continuity Readabilityは、特定の局所的realization同士を接続として読めるかを扱う。Trajectoryには、より広い構成が必要である。複数の局所的realization、保持された関係の場、そして、その中からより大きな関係的経路を可読化するContext相対的なTracing operationが必要になる。

次章では、関係を保持する場とTrajectoryそのものを分離し、Trajectoryを、事前定義された状態列や時系列ログではなく、Contextual Tracingとして構成する。
