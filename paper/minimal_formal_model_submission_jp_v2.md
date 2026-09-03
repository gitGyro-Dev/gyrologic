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
formal_model: "Minimal Formal Model v2"
canonical_core: "unchanged"
bibliography: "references.bib"
link-citations: true
source: "paper/minimal_formal_model_full_en.md"
---

**著者:** Shuntaro Kawakami  
**所属:** Independent Researcher（個人研究者）  
**ORCID:** [0009-0004-0091-1303](https://orcid.org/0009-0004-0091-1303)  
**連絡先:** [dev.jxiv@gyro-wedge.com](mailto:dev.jxiv@gyro-wedge.com)

# 要旨

Gyro Logicは、Structure、Slice、Stabilityから成る不変Coreを中心に構成される理論的枠組みである。既存の基礎論文では、このCoreの概念的役割を示し、「Gyro Logicとは何か」という基礎的な問いを扱った。本論文が扱うのは、それとは異なる形式化上の問題である。すなわち、Canonical Definitionを置き換えず、またGyro Logicを既存の単一数学分野へ早期に還元することなく、現在までに形成された概念的区別をどのように探索的な最小形式モデルとして整理できるか、という問題である。

提案モデルは、Canonical Coreを維持しながら、Sliceの過程と、その過程を通じて利用可能になるlocal articulationを分離することから始まる。局所的Gyro realizationを暫定的に

\[
g_n=(S_n,B_n,c_n,\Sigma_n,a_n,K_n)
\]

と表す。ここで、\(S_n\) はStructure、\(B_n\) はOperator Orientation、\(c_n\) はContext、\(\Sigma_n\) はSlice process、\(a_n\) は結果として現れるlocal articulation、\(K_n\) は対応するStability Sceneである。Coreに対応する中心関係は

\[
S_n\xRightarrow{\Sigma_{B_n,c_n}}a_n\xRightarrow{\operatorname{Stab}}K_n
\]

と表される。

改訂版では、`slice-done`をunderlying eventの客観的終端として読まないことを明確化する。`slice-done`は、展開中のSliceのある範囲を、一つのlocal establishmentとして扱うlocal unitizationを表す。その局所的単位化は、現在のOperator判断、OrientationとContext、継承されたprotocolやrule、institutional criteria、あるいは強いevent-side transitionなどによって供給または制約される可能性があるが、必ずそうなることを意味しない。underlying eventやprocessはその後も継続し得る。また、`slice-done`はStability、不可逆的完了、global closureを意味しない。

Stabilityは、scalar、equilibrium、fixed point、terminal conditionへ還元されない。本論文では、一つのarticulationが継続可能なestablishmentとして扱える一方で、residual local not-yetを残し得る構造化された局所場面としてStabilityを扱う。Canonical Definitionにおける`readable`という語は維持するが、`Readable(...)`を普遍的に定義された独立predicateとはみなさない。形式的なreadability表記が必要な場合には、domain-specific modelが正当化されたsemanticsを与えない限り、domain-relative placeholderとして扱う。

Incorporated Readabilityはstored historyから分離され、局所的に成立したdistinction、relation、criterion、relevance conditionが後続のrealizationで利用可能になるcontext updateとして表現される。Continuity ReadabilityはIdentityから分離され、Trajectoryはstate sequenceおよびchronological logの双方から分離される。Trajectoryは、局所的Gyro realization間のadmissible relationをcontextual tracingすることで成立するものとして扱われる。Differenceもmetric distance、numerical error、Boundaryから分離され、Slice・Orientation・Contextに相対的で、異種のcodomainを取り得るstructured relationとして暫定的に型付けされる。

本論文は、提案schemaをrelational structures、graphs / hypergraphs、order theory、topology、dynamical systems、transition systems、event structures、category theory、logic / proof theory、constraint propagation、probability / statistics、sheaf-like structures、process algebraと比較する。これらはそれぞれ有効なpartial modelを提供し得るが、現時点では、より強い前提を導入せずにGyro Logic固有の区別をすべて保持できる単一分野は確認されない。

本論文でいう*minimal*は、theoremとして証明されたstrict minimalityではなく、現在の理論的区別を保つために必要と判断されるformal commitmentをできるだけ増やさない、operational / exploratoryな意味で用いる。unique minimality、cardinal minimality、order-theoretic minimalityのproofは主張しない。本モデルはexploratoryであり、complete axiomatization、universal semantics of readability、universal Stability metric、universal boundary-admissibility rule、general tracing algorithmを提供するものではない。その貢献は、現在のformal commitmentを十分明示し、今後のvalidation、comparison、revision、implementation studyを可能にする点にある。

**キーワード:** Gyro Logic、最小形式モデル、Structure、Slice、Stability、local articulation、Incorporated Readability、Continuity Readability、contextual Trajectory、Difference、Boundary

# 1 Introduction

Gyro Logicは、次の不変Coreを中心に構成される理論的枠組みである。

```text
Structure
↓
Slice
↓
Stability
```

既存のGyro Logic基礎論文は、このCoreの概念的役割を示し、Structure・Slice・Stabilityを通じて一つのestablishmentがどのように利用可能になるかを説明した。そこでは主として「Gyro Logicとは何か」という問いが扱われた。本論文が扱うのは、それとは異なる問題である。すなわち、Canonical Definitionを置き換えず、またGyro Logicを既存の単一数学分野へ早期に還元することなく、現在までに形成された理論的区別をどのように最小限のformal organizationとして整理できるか、という問題である。

ここでいう*minimal*は意図的に限定された意味を持つ。本論文は、提案schemaがuniquely minimal、cardinally minimal、あるいはformal orderingの下でminimalであることを証明しない。むしろ、現在の理論的区別を維持するために十分だと判断されるminimum formal commitmentsを探索的に提示する。より厳密なminimality resultには、admissible model class、preservation criterion、candidate model間のcomparison relation、ならびにあるcomponentを除去すると必要な区別の少なくとも一つが失われることのproofが必要となる。

この問題が生じるのは、既存の数学的形式が、現在のGyro Logicに必要な条件よりも強い前提から出発する場合が多いためである。state-space modelは通常、stateとそのspaceが事前に与えられていることを仮定する。functionは、識別可能なdomainとcodomainを前提とする。graphは、nodeとedgeがすでに表現可能であることを前提とする。dynamical trajectoryは、一般にordered state sequenceとして表される。Stabilityは、equilibrium、convergence、fixed point、robustness under perturbation、scalar scoreなどとして表現されることが多い。Differenceも、distance、deviation、errorとして扱われやすい。これらはいずれも有効なpartial modelとなり得るが、どの区別が保持され、どの区別が失われるかを確認しないまま、Gyro Logic全体のuniversal formとして採用することはできない。

この困難は、とりわけSliceにおいて明確になる。Canonical Definitionでは、Sliceは、Structureを通して一つのestablishmentへ向かうpathを開くprocessである。この定義は、Sliceの結果が、あらかじめ完全にindividuatedされた対象として存在し、抽出されるのを待っていることを要求しない。したがってSliceは、filtering、projection、selection、ordinary retrievalから区別されなければならない。本論文では、Slice processと、そのprocessを通じて利用可能になるlocal articulationとを暫定的に分離する。local articulationは、局所的な「こうなった」を表すが、それ自体はまだStabilityと同一ではない。

改訂版では、`slice-done`のlocalityも明確化する。unfolding event、process、relationは、Operatorがその一部を一つのlocal establishmentとして扱ったからといって停止する必要はない。したがって`slice-done`はunderlying eventのintrinsic terminal stateではない。現在のOrientationとContext、またはinherited protocol、rule、institutionなどのframeの下で、Sliceのあるrangeを一つのarticulated resultとして扱う局所的statusである。event-side transitionがboundaryを強く制約する場合もあるが、それは普遍的必須条件ではなく、より広いprocessは継続し得る。

第二の困難はStabilityに関するものである。Gyro LogicにおけるStabilityは、evaluatorでもdecision-makerでもfinal completionでもない。また、その理論的意味はnumerical scoreやfixed pointだけでは尽くされない。本論文では、Stabilityを、一つのarticulationが継続可能なestablishmentとして扱える構造化されたlocal sceneとして検討する。そのsceneは、confirmationとcontinuationを支えられる程度に局所的には落ち着いていながら、なおunresolved local not-yetを含み得る。local establishmentとresidual not-yetが共存することは重要であり、Stability SceneはStructure全体のclosureを意味しない。

Canonical Definition of Stabilityは`readable`という語を用いる。今回のrevisionはそのwordingを維持する一方で、そのformal commitmentを弱める。universalでindependently validatedな`Readable(...)`のoperational semanticsは仮定しない。本論文では、domain-specific modelがより強いsemanticsを与えない限り、readabilityを、そのarticulationやrelationがrelevant frameの下でestablishedとして扱える条件を説明するprovisional explanatory / relational languageとして扱う。

第三の困難は、複数のlocal realizationをまたぐcontinuationに関係する。一つのrealizationでestablishedとなったものは、後続realizationが生じる条件を変化させ得る。この作用は、過去のeventを単なるstored historyやappend-only logとして扱うだけでは十分に表現できない。そこで本論文は、established distinction、relation、criterion、relevance conditionが後続contextで利用可能になる仕方を表す暫定概念としてIncorporated Readabilityを導入する。同様に、Continuity ReadabilityをIdentityから分離し、Trajectoryをchronological event listおよびpredefined state sequenceの双方から分離する。Trajectoryは、local Gyro realization間のadmissible relationをcontextual tracingすることで成立するものとして扱われる。

Differenceも関連するformal problemをもつ。Gyro LogicにおけるDifferenceは、scalar、metric、symmetric、error-likeであるとは限らない。Orientation・Context・Sliceに応じて、partially defined、relational、ordered、distributive、field-likeな対象となり得る。したがってBoundaryはDifferenceそのものとは同一視されない。Boundaryは、特定のSliceとframeの下でDifferenceがarticulatedかつstabilizedされることによりlocally usableとなるderivative distinctionとして扱われる。

以上を踏まえ、本論文はfinal axiomatizationではなくexploratory Minimal Formal Modelを提示する。その目的は、Structure、Slice、local articulation、Stability、Incorporated Readability、Continuity Readability、Trajectory、Difference、Boundaryの区別を保持するために必要なcompact formal commitmentsを明らかにすることにある。導入するnotationはsupporting candidateであり、Canonical Definitionそのものではない。本論文は不変Coreを変更せず、Gyro Logicがすでにrelational structures、graph theory、topology、dynamical systems、category theory、proof theory、あるいはその他の単一分野へ還元されたとも主張しない。

本論文は、まずContribution StatementとResearch Questionsを示す。続いて、不変Coreがformalizationに課すconstraintsを明確にし、Structure・Slice・Stabilityを順に検討する。その後、Incorporated Readability、Continuity Readability、contextual Trajectory、Difference、Boundaryを扱い、これらをcompact formal schemaへ統合する。さらに関連数学分野との比較を行い、illustrative examplesとlimitationsを通じて、本モデルが何を主張し、何を主張しないかを明確にする。

## 1.1 Contribution Statement

本論文は、Gyro LogicのMinimal Formal Modelに向けて主に八つの貢献を提示する。

第一に、不変CoreであるStructure・Slice・Stabilityについて、Canonical Definitionを変更せず、その順序を入れ替えず、新たなCore要素も追加しないまま、provisional mathematical typingを与える。本論文で導入するformal expressionは、Canonical Definitionを置き換えるdefinitionではなく、それを支えるformal candidateとして位置づけられる。

第二に、unfolding processとしてのSliceと、そのprocessを通じて利用可能になるlocal articulationとを分離する。さらに、`slice-done`をunderlying eventのobjective terminal stateではなくlocal unitizationとして明確化する。この区別により、Sliceをpre-existing resultのextraction、filtering、selectionへ還元すること、また一つのuniversal stopping pointを仮定することを避ける。

第三に、Stabilityをscalar value、equilibrium、fixed point、terminal conditionへ還元せず、articulationが継続可能なestablishmentとして扱えるstructured local sceneとして表現する。このrepresentationにより、local establishmentとresidual local not-yetが同一Stability Scene内で共存でき、かつStabilityを`slice-done`から分離できる。

第四に、Incorporated Readabilityをstored history、event log、passive memoryから区別する。Incorporated Readabilityは、locally established distinction、relation、criterion、relevance conditionが後続Gyro realizationで利用可能になる仕方を表す。そのupdateは、単純なaccumulationではなく、addition、revision、integration、reweighting、invalidation、loss of accessibilityを含み得る。

第五に、Continuity ReadabilityをIdentityから分離する。Continuityは、admissible relationがtrace可能であり、given Orientation、Context、Slice、incorporated contextの下でcontinuityとして扱えるときに成立する。したがって、Identity breakをまたいでcontinuityが維持される場合と、Identityがassertedされていてもcontinuityがunavailable / disputedである場合の双方を許容する。

第六に、Trajectoryをstate sequence、chronological log、accumulated eventから分離する。Trajectoryは、relation-bearing fieldやevent collectionそのものではなく、local Gyro realization間のadmissible relationをcontextual tracingした結果として扱う。この区別により、branching、merging、gap、retrospective reinterpretation、Re-Slice、Jumpを、Trajectoryを単一linear pathへ押し込めずに表現できる。

第七に、Differenceをmetric distance、numerical error、Boundaryから分離する。Differenceは、Slice・Orientation・Contextに相対的なstructured relation of non-coincidenceとして暫定的に扱い、そのcodomainはscalar、vectorial、ordered、relational、distributive、partially defined、field-likeであり得る。Boundaryはそれにより、Differenceそのものではなく、derivative locally usable distinctionとして扱われる。

第八に、提案modelをrelational structures、graphs / hypergraphs、order theory、topology、dynamical systems、transition systems、event structures、category theory、logic / proof theory、constraint propagation、probability / statistics、sheaf-like structures、process algebraと比較する。これにより、各分野がどこで有効なpartial modelを提供し、どこからそのassumptionがGyro Logicに必要な区別を過度に狭めるかを明示する。

これらを合わせることで、不変Core

```text
Structure
↓
Slice
↓
Stability
```

を維持したまま、exploratory integrated schemaを提示する。本論文はGyro Logicが単一既存数学分野へ還元されたとは主張せず、modelがfinal、canonical、proven uniquely minimalとも主張しない。貢献は、現在のtheoretical distinctionを維持するために必要なminimum formal commitmentsを明示し、今後のvalidation、comparison、revision、implementation studyの基盤を提供する点にある。

## 1.2 Research Questions

本論文の中心Research Questionは、Gyro Logicの不変Coreを維持し、既存数学object typeへのpremature reductionを避けながら、現在の概念を整理できるcompact formal schemaは何か、である。

**RQ1.** Structure、Slice、StabilityのCanonical meaningを再定義せず、順序も変更せず、新たなCore要素も導入しないまま、どのようにprovisional mathematical typeを与えられるか。

**RQ2.** Sliceを、resultやpathが事前にfully individuatedされていると仮定せず、また`slice-done`をunderlying eventのobjective endとみなさずに、local articulationが利用可能になるunfolding processとしてどのように表現できるか。

**RQ3.** Stabilityを、`slice-done`に伴うlocal unitizationから分離しつつ、residual local not-yetを保持できるlocally established and continuable sceneとしてどのように表現できるか。

**RQ4.** 一つのlocal Gyro realizationを通じてestablishedとなったものが、stored history、passive memory、monotonic accumulationへ還元されることなく、後続realizationの条件をどのように変え得るか。

**RQ5.** ContinuityとTrajectoryを、Identity、predefined state sequence、chronological log、あるいはuniversal `Readable(...)` predicateへ還元することなく、admissible relationのcontextual tracingとしてどのように表現できるか。

**RQ6.** 既存のどの数学分野が提案schemaのpartial modelとして有効であり、どの時点でそのassumptionがGyro Logicにとってrestrictiveすぎるものになるか。

これらの問いは、本論文のscopeを共同で定義する。本論文は、Gyro Logicを完全にaxiomatizeできるか、あるいは単一数学disciplineへreduceできるかを問うものではない。現在のtheoryで形成された区別を維持しつつ、未解決のsemanticsやadmissibility conditionsを明示できるinternally consistentかつexplicitly provisionalなformal organizationを構築できるかを問う。

# 2 The Invariant Core and Formalization Constraints

## 2.1 不変Core

本論文で展開するformal modelは、Gyro Logicの不変Core

```text
Structure
↓
Slice
↓
Stability
```

によって制約される。このCoreのorderとcompositionは本研究のvariableではない。追加conceptをCore間へ挿入せず、derivative conceptを第四のCore要素へ昇格させない。Orientation、Context、local articulation、Incorporated Readability、Continuity Readability、Trajectory、Difference、Boundary、Operator Response、Re-Slice、Jumpはconditioning、resulting、relational、temporal、interpretive conceptとして扱う。それらはlocal Gyro realizationのformal descriptionを精密化し得るが、不変Coreそのものを置き換えたり拡張したりしない。

Canonical Definitionsは変更せず維持する。

> **Structure is the mode in which something can be established.**

> **Slice is the process by which a path is opened through a Structure toward an establishment.**

> **Stability is the state in which an opened path becomes readable as an establishment that can continue.**

以下で提案する全mathematical expressionより、これらCanonical Definitionが優先される。formal candidateがCanonical Definitionと矛盾する意味を含む場合、修正または棄却されるべきなのはformal candidateであり、数学objectに合わせてCanonical Definitionを変更してはならない。

Stability Definitionに含まれる`readable`という語はcanonical wordingとして維持する。しかし、このwordingからuniversal formal predicate `Readable(...)`が存在すると推論しない。以下でformal readability notationを用いる場合も、specialized modelがより強いsemanticsを与えない限り、provisional domain-relative placeholderとして扱う。

## 2.2 Canonical DefinitionとFormal Candidate

本論文はstatementを二つのlevelに分ける。Canonical DefinitionはGyro Logic conceptのtheoretical meaningを定める。Formal Candidateは、そのmeaningの一部を保持し得るprovisional mathematical organizationを示す。したがって両者は同一ではない。

```text
canonical definition
≠
formal candidate
```

本論文のformulaは、replacement definitionではなくdisciplined representational proposalとして読むべきである。Structureを\(S_n\)、Slice processを\(\Sigma_n\)、Stability Sceneを\(K_n\)と表しても、Structureが本質的にset elementである、Sliceがordinary total functionである、Stabilityが常にtupleであることを意味しない。

数学notationはしばしばsilent ontological commitmentを導入する。functionはfixed domain / codomainを、graphはpre-individuated node / edgeを、metricはnumerical comparabilityやsymmetry、triangle inequalityを、state trajectoryはalready defined state spaceやtemporal orderingを暗黙に含み得る。したがってformal modelは、各notationが何をcommitし、何をopenに残すかを明示しなければならない。

## 2.3 Minimal Formal Commitments

本モデルは、次のminimum commitmentsのみを採用する。

第一に、analysisのためlocal Gyro realizationを区別できる。これはreality自体がintrinsically independent unitsに分割されていることを要求しない。local realizationを暫定的にreferenceし、他realizationとrelationづけられることだけを要求する。

第二に、Sliceは、Sliceを通じて利用可能になるlocal articulationから区別される。processとlocally available articulationは同一ではない。

第三に、StabilityはSlice processおよびlocal articulationの双方から区別される。Stabilityは単なるappearanceではなく、articulationをestablishmentとして扱いcontinuationできることに関係する。

第四に、一つのlocal realizationでestablishedとなったreadabilityは、後続realizationをconditionし得る。そのconditioningはdeterministic、monotonic、complete、immediately adjacent in timeである必要はない。

第五に、local realization間のrelationは、すべてのOrientation、Context、Sliceの下でcontinuityとして扱えるとは限らない。したがってrelation existence、traceability、admissibility、continuity judgmentは分離される。

第六に、Differenceはuniversally scalar、metric、symmetric、total、error-likeと仮定せずに表現できる。

これらのcommitmentはminimal schemaの構築には十分である一方、Structure、relation field、context update、tracing operationのmathematical typeはlater specializationへopenに残す。

## 2.4 Formalization Constraints

candidate modelは、少なくとも次のconstraintsを満たす場合にのみacceptableである。

**Core preservation.** Structure、Slice、Stabilityのorderとcompositionを維持し、replacement Coreを導入しない。

**Definition preservation.** Canonical conceptをnarrow mathematical special caseで再定義しない。

**Process–result separation.** Sliceをunfolding processとして、そこから利用可能になるlocal articulationと分離する。

**Articulation–Stability separation.** local articulationが出現しても、すでにestablished and continuableなStabilityであると仮定しない。

**Locality without global closure.** locally established Stability Sceneと、globally openなStructure、residual local not-yetの共存を許す。

**Non-reductive readability update.** Incorporated Readabilityをappend-only historyやimmutable stored dataへ還元しない。

**Identity–continuity separation.** continuity without identityとidentity claim without available continuityの双方を許す。

**Trajectory–sequence separation.** Trajectoryをchronological log、event set、predefined linear state sequenceと同一視しない。

**Difference–metric separation.** Differenceにmetric / error-model assumptionsを必須化しない。

**Layer consistency.** Gyro Logic theory modelとして維持し、GyroOS implementation decisionやGyroAuth application requirementがtheory conceptを再定義しない。

## 2.5 Explicit Non-Assumptions

Minimal Formal Modelは、Structureが一つのfixed mathematical object typeであること、すべてのrelevant object / state / relation / boundaryがSlice以前にindividuatedされていること、Sliceがdeterministic / total functionであること、Stabilityがscalar threshold / equilibrium / fixed pointであること、readabilityがmonotonically accumulatesすること、continuityがidentityを含意すること、Trajectoryがlinearであること、Differenceがdistanceであること、単一既存数学分野がGyro Logicのcomplete foundationを提供することを仮定しない。

これらはその数学constructionの有用性を否定するものではない。そのstatusを限定するためのnon-assumptionである。metric、graph、dynamical system、category、proof context、transition systemは、assumptionが正当化されるdomainではvalid instantiationになり得る。本論文はそのいずれもtheoryのuniversal formへ昇格させない。

# 3 Structure as Establishability Without Fixed Mathematical Type

## 3.1 Canonical Meaning and Formal Problem

StructureのCanonical Definitionは次である。

> **Structure is the mode in which something can be established.**

このdefinitionはStructureをstate、object、set、space、relation、container、substrate、configurationと同一視しない。これらはいずれもparticular domainではvalid representationとなり得るが、universal mathematical typeとしては採用しない。formal problemは、Structureが「本当は何か」を既存object typeから選ぶことではなく、そのspecializationを正当化する前に、最低限何をcommitできるかを明らかにすることにある。

通常のmathematical modelingは、object、state、variable、relationがすでにindividuatedされた後から始まることが多い。Gyro Logicは、relevant object / relationがすべてfixedされていると仮定せず、何かがSliceを通じてlocally articulableになり得るprior formal conditionも扱う必要がある。そのためStructureは、completed inventory of established entitiesではなく、establishability-bearing organizationとして扱う。この表現はworking characterizationでありreplacement definitionではない。

## 3.2 Structure Is Not the Current State

current stateはStructure内で表現され得るが、そのstateはestablishmentを可能にするStructureそのものではない。current stateを\(x_n\)とすると、minimal modelは

\[
S_n=x_n
\]

を採用しない。必要なのは、stateがStructureにrelativeにestablishableであり得ることだけである。

\[
x_n\triangleleft S_n
\]

ここで\(\triangleleft\)はprovisional establishment-availability relationである。これは、appropriate conditionsの下で\(x_n\)をestablished / articulable / availableとして扱えることを意味し、domain-specific modelが明示しない限り、set membership、physical containment、logical entailment、part–whole inclusionを意味しない。

この区別により、同じStructureから異なるstateがavailableになり得る。またcurrent stateが変化しても、Structureを完全に独立した別objectへ交換する必要はない。逆に、同じapparent stateが異なるStructureを通して成立している場合も排除しない。

## 3.3 Structure Is Not the Bearer or Object

local realizationが起きるentity、material、system、text、institution、processはbearerと呼び得る。しかしbearerもStructureと同一ではない。cake、software system、legal institution、authentication sessionはexample上のbearerとなり得るが、そのStructureはdistinction、relation、state、possible establishmentがavailableになり得るmodeに関係する。

```text
bearer
=
Structure
=
current state
```

というcollapseを避ける。同じbearerがdifferent conditionsの下でmultiple Structuresをsupportすることも、multiple bearersがone relational Structureへparticipateすることも排除しない。またbearerがpersistしながらcurrent stateが変化する場合、Structureがbearerのmaterial / descriptive organizationの変化をまたいでcontinueする場合も、modelはあらかじめ否定しない。

## 3.4 Structure as Globally Not-Yet

Slice以前のStructureはglobal not-yetによってcharacterizeされる。これはabsence、nothingness、ignorance、empty possibility setを意味しない。prospective Sliceを通じてarticulateされるparticular local establishmentが、まだそのformでavailableになっていないことを意味する。

\(\mathcal{A}^{*}(S_n)\)を、Structureからavailableになり得るarticulation familyのprovisional placeholderとする。asteriskは、それらがすでにfully individuated objectであるとcommitしないことを示す。

\[
a\in\mathcal{A}^{*}(S_n)
\]

もordinary set membershipとして読まない。appropriate Sliceを通じて\(a\)が\(S_n\)とcompatible / supportable / realizableであることのみを示す。

重要なのは、\(\mathcal{A}^{*}(S_n)\)がpre-existing answer catalogueではないことである。Slice以前のestablishabilityをunder-determinedなまま保持するplaceholderであり、all candidate articulationがenumerable、mutually exclusive、simultaneously available、Orientation / Contextに対してinvariantであることを要求しない。

## 3.5 Minimal Relational Characterization

Structureは暫定的に

\[
S_n=\langle\mathsf{Avail}_n,\mathsf{Rel}_n,\mathsf{Cond}_n\rangle^{*}
\]

とreferenceできる。

- \(\mathsf{Avail}_n\)：local establishmentとしてavailableになり得るもの
- \(\mathsf{Rel}_n\)：そのestablishmentをsupport / constrain / connectし得るrelation
- \(\mathsf{Cond}_n\)：availability / relationがrelevantになるcondition
- \(^*\)：universal tuple ontologyとして採用しないこと

このschemaはstate space、graph、constraint system、topological spaceより弱い。componentがcomplete、explicit、independent、directly observableであることを要求せず、Sliceがlocal articulationへ向かって進むために必要なavailability / relation / conditioningの組合せをStructureがsupportすることのみを示す。

さらに弱いrelationとして

\[
\mathsf{Establishable}(a;S_n,B_n,c_n)
\]

を置ける。これはarticulation \(a\)がStructure \(S_n\)、Orientation \(B_n\)、Context \(c_n\)にrelativeにlocally availableになり得ることを示す。\(a\)がSlice以前にalready givenである、必ずappearanceする、必ずStableになることは意味しない。

## 3.6 Orientation and Context Do Not Constitute Structure

OrientationとContextは、StructureのどのaspectがSliceにrelevantになるかをconditionするが、StructureをOperatorが現在見ているものへ還元しない。そうするとStructureがperspective-relative representationへcollapseし、そのrepresentationをconstrain / resist / exceedできなくなるためである。

したがって

\[
S_n\neq S_n(B_n,c_n)
\]

を、StructureとOrientation-conditioned viewを同一視しないwarningとして保持する。specialized modelは

\[
\operatorname{Pres}_{B_n,c_n}(S_n)
\]

というaccessible presentationを定義してもよいが、それが\(S_n\)全体をexhaustするとは仮定しない。

## 3.7 Local Establishment Does Not Close Structure

Sliceがlocal articulationをyieldし、それがStableになっても、resulting local establishmentはStructureをglobally closeしない。

\[
S_n\xRightarrow{\Sigma_{B_n,c_n}}a_n
\]

かつStability Scene \(K_n\)がavailableになっても、

\[
\mathcal{A}^{*}(S_n)=\{a_n\}
\]

や

\[
S_n\text{ is complete}
\]

は導かれない。一つのlocal realizationは一つのarticulationをsettleし得るが、他のrelation、distinction、possibilityはunresolvedのまま残り得る。

## 3.8 Formal Commitments and Non-Commitments

Structure componentは、Structureをlocally referenceできること、establishment possibilityをsupportすること、current stateとbearerから区別されること、どのarticulationがavailableになり得るかをconstrainし得ること、one local establishmentを超えてopenであり続けることへcommitする。

一方、Structureがset、manifold、category、graph、state space、probability space、constraint system、logical theory、physical substrateであるとはcommitしない。またdirectly observable、fully enumerable、temporally static、internally homogeneous、prior incorporated readabilityからindependentとも仮定しない。

# 4 Slice as Process and Local Articulation

## 4.1 Canonical Meaning

SliceのCanonical Definitionは次である。

> **Slice is the process by which a path is opened through a Structure toward an establishment.**

このdefinitionは二つのconstraintsを課す。第一に、Sliceはcompleted objectではなくprocessである。第二に、establishmentへ向かうpathはprocessを通じてopenされるのであり、事前にfully individuatedされたentityとして存在することを必須としない。

したがって本モデルはSliceを、fixed result spaceを前提とするoperationから区別する。filtering、projection、selection、retrieval、partitioning、ordinary extractionはrestricted domainでSlice processをinstantiateし得るが、Sliceのuniversal meaningにはしない。

## 4.2 Why Extraction Models Are Insufficient

extraction modelはschematically

\[
E:S\to X
\]

と書ける。このmodelはresult typeがalready knownなdomainでは有用だが、Gyro Logicが一般に必要とするより強いassumptionを導入する。outputがalready individuated、codomainがfixed、relevant distinctionが事前にavailable、operationがpre-existing componentをrevealするだけ、といった含意を持ち得るためである。

Gyro Logicは、some Slice processesがextractionとしてimplementedされることを否定しない。否定するのは、extractionがSliceのtheoretical meaning全体を尽くすことである。general Sliceでは、locally available formそのものがprocessを通じてconstitutedされ得る。

```text
Slice
≠
extraction of an already completed result
```

```text
path-opening
≠
retrieval of a pre-existing path object
```

## 4.3 Process and Local Articulation

local Structureを\(S_n\)、Operator Orientationを\(B_n\)、Contextを\(c_n\)、Slice processを\(\Sigma_n\)とし、provisional relationを

\[
S_n\xRightarrow{\Sigma_{B_n,c_n}}a_n
\]

と書く。\(a_n\)はSliceを通じてavailableになるlocal articulationである。

\(\xRightarrow{}\)はordinary total functionと同一視しない。resultがpartial、context-dependent、non-deterministic、retrospectively readable、another Orientationではunavailableであり得るprocess relationを示す。

1. local Structureが関与する
2. SliceがOrientationとContextの下でunfoldする
3. local articulationがそのunfoldingを通じてavailableになり得る
4. articulationとprocessは区別される

\(a_n\)は局所的な「こうなった」を表す。final completion、global closure、Stabilityそのものではない。後続でestablished / continuableかをevaluateできるlocally available formである。

```text
Slice process
≠
local articulation
```

```text
local articulation
≠
Stability
```

## 4.4 Slice-ing and Slice-done

Gyro Logicは、Sliceのtime-including unfoldingと、そのunfoldingを局所的に一つのresultとしてunitizeしたものを区別する。

```text
slice-ing
=
the process while Slice is unfolding
```

```text
slice-done
=
a local unitization in which some range of the unfolding Slice
is treated as one local establishment
```

このlocal unitizationは、current Operator judgment、Orientation and Context、inherited protocol / rule、institutional criteria、strong event-side transitionsなどによって供給または制約される可能性がある。ただし、それらのいずれかが必ず影響することを意味しない。また、underlying event自体がそのpointでobjectively / absolutely endすることも意味しない。

```text
slice-done
≠
end of the underlying event
```

```text
slice-done
≠
Stability
```

provisional process representationは

\[
\alpha_{\Sigma}:I_{\Sigma}\to\mathcal{A}^{*}(S_n)
\]

および

\[
a_n=\alpha_{\Sigma}(\tau^{*})
\]

とできる。\(I_{\Sigma}\)はinternal process index、\(\mathcal{A}^{*}(S_n)\)はpossible local articulationのprovisional space、\(\tau^{*}\)はselected frameの下でのlocal analytical point of unitizationを示す。このnotationはillustrativeでありcanonicalではない。physical time、unique terminal index、fixed articulation spaceをuniversally要求しない。

よりgeneralには

\[
(S_n,B_n,c_n,\Sigma_n;F_n)\leadsto a_n
\]

と書き、\(F_n\)を、domain modelで有用な場合のlocal / inherited frameとする。\(F_n\)はadditional Core elementではない。

## 4.5 The Role of Orientation, Context, and Inherited Frames

OrientationとContextはSliceをconditionするが、additional Core elementではない。OrientationはStructureへのdirectional entranceを、Contextはどのrelation、distinction、articulationがavailableになり得るかに関わるsurrounding conditionを与える。

local boundaryは、current Operatorが毎回freshly chooseするとは限らない。protocol termination rule、legal / institutional criterion、medical procedure、pre-existing computational contractなどからinheritされる場合がある。event-side transitionがavailable boundaryをstrongly constrainする場合も、inherited criterionがselected frame内でboundaryをlocally fixする場合もある。ただし、これらはpossible source / constraintであり、すべてのboundaryが必ずその影響を受けるというuniversal claimではない。

\[
\Sigma_{B_n,c_n}
\]

というindexed notationは、このconditioningを表す。StructureそのものがOperatorによって作られる、あるいはStructure全体がsingle observerにrelativeであることを意味しない。

## 4.6 Minimal Anti-Post-Hoc Constraint

Operator-relativityやinherited-frame languageを、after-the-fact rescue mechanismとして無制限に使用してはならない。

> boundary judgmentを正当化するために持ち出すOrientation、Context、inherited rule、institutional criterion、boundary provenanceは、そのboundary judgment自体とは独立したsupportを持つべきである。boundaryを選択した後にframeを導入・再記述するだけでは、そのboundaryの正当化にはならない。

Temporal priorityだけでも不十分である。prior statementがall plausible candidate boundariesをopenのまま残すなら、ほとんどconstraintにならない。同様に、after the factに「inherited」とlabelするだけでもnon-post-hocにはならず、claimed provenance自体がindependently supportableでなければならない。

本モデルは、frameがどの程度specific / discriminating / evidentially sufficientであるべきかを決めるdomain-neutral metricをまだ提供しない。またnever-live alternativeを形式上excludeしただけではsubstantive constraintにならない場合もある。full admissibility semanticsはfuture workである。

## 4.7 Slice Does Not Consume Structure

Slice processは、Structureがexhausted / consumedされる、またはforegroundとbackgroundへ分割され一方が消えることを意味しない。highly determinate articulationが生じても、Structureは他のrelation、possible articulation、unresolved condition、alternative pathを保持し得る。

```text
Structure after Slice
≠
Structure minus extracted result
```

Sliceがlater approach conditionを変える場合はあり得るが、literal subtractionと混同してはならない。またall Structure changeをSliceへ帰属させない。external interaction、environmental change、material transformationなどもlater realizationのconditionを変え得る。

## 4.8 Locality and Non-Closure

local articulationは少なくとも、関与したStructure section、Orientation / Contextまたはinherited frame、particular establishmentへのpathという意味でlocalである。いずれもStructureのremainderがirrelevant / nonexistentになることを意味しない。

\[
a_n\text{ is available}
\]

でありながら

\[
S_n\text{ remains globally open}
\]

であり得る。これはRe-Slice、alternative articulation、Context expansion、Difference recognition、later Trajectory tracingのために必要である。

## 4.9 Minimal Formal Commitments for Slice

本論文はSliceについて次へcommitする。

1. Sliceはprocessualであり、static mapping resultだけとは同一視できない。
2. processとlocal articulationは区別される。
3. `slice-done`はlocal unitizationでありuniversal event terminationではない。
4. local articulationは事前にfully individuated objectとして存在する必要がない。
5. Orientation、Context、inherited frameはSliceをconstrainし得るがCore stageにはならない。
6. local articulationのappearance / unitizationはStabilityを含意しない。
7. SliceはStructureを必ずconsume / closeしない。
8. extraction、projection、filtering、classification、selectionはdomain-specific implementationとなり得るが、Sliceのuniversal definitionではない。

## 4.10 Explicit Non-Commitments

本モデルは、every Sliceにunique resultがある、every Sliceがterminatesする、Sliceがdeterministic、articulation spaceがfixed、Orientationがhuman observerに属する、Contextがfully representable、every local boundaryがcurrent Operatorにfreely chosenされる、`slice-done`がirreversibleである、とは主張しない。

また「a path is opened」をliteral geometric pathとはしない。pathはrelational、logical、procedural、semantic、causal、material、institutionalなどdomain-specificであり得る。

## 4.11 Transition to Stability

local articulation \(a_n\)はnext formal distinctionのresultを提供するが、まだStability Sceneではない。articulationからStabilityへのtransitionは、そのarticulationがrelevant Structure、Orientation、Context、および必要に応じlocal / inherited frameの下で、継続可能なestablishmentとして扱えるかを問う。

\[
K_n=\mathsf{StabScene}(a_n;S_n,B_n,c_n,F_n)
\]

optional \(F_n\)はdomain-model parameterでありCore elementではない。

# 5 Stability as a Readable and Continuable Scene

## 5.1 Canonical Meaning

StabilityのCanonical Definitionは次である。

> **Stability is the state in which an opened path becomes readable as an establishment that can continue.**

このdefinitionはStabilityをSliceの後に置く一方、Slice completionへ還元することを防ぐ。Sliceはpathをopenし、`slice-done`としてlocal unitizationされ得る。Stabilityは、そのarticulationが継続可能なestablishmentとして扱えるかに関係する。

```text
Slice process
≠
local articulation / local unitization
≠
Stability
```

local articulationはappearance / unitizationしていても、domain-relevant continuation conditionsを満たしていない場合がある。Stabilityは、relevant frameの下でarticulationをestablishmentとして扱いcontinuationできるときに成立する。

## 5.2 Why a Scalar Is Not Sufficient

implementation-oriented settingではStabilityをscore、threshold、probability、confidence value、robustness measureで表す場合がある。これらはoperational indicatorとして有用だが、theoretical Stability全体ではない。

\[
\sigma_n\in[0,1]
\]

のようなscalarは、specific modelでdegree of assessed stabilityを示せるが、which relations are available for establishment、which unresolved conditions remain、which continuations are availableを単独では表現しない。

```text
Stability score
≠
Stability
```

\[
\sigma_n\geq\theta
\]

のようなthresholdも、particular implementation policyのlabelingには使えてもCanonical conceptを定義しない。

## 5.3 Why Equilibrium and Fixed Points Are Partial Models

Equilibrium、convergence、invariant set、attractor、fixed pointはdynamical systemsにおけるpowerful stability modelsであり、relevant state space、dynamics、perturbation modelが正当化されるapplicationではGyro Logicをinstantiateし得る。

しかしGyro Stabilityはmotionless、globally converged、invariant、terminalであることを要求しない。locally established sceneはchangeし続けてもcontinuationのため十分coherentであり得る。またlong-run limit以前にestablishmentがavailableになることもある。

```text
Gyro Stability
≠
equilibrium only
≠
fixed point only
≠
global convergence only
```

## 5.4 Stability as a Structured Local Scene

Stability Sceneをprovisionally

\[
K_n=(a_n,L_n,U_n,C_n^{+})
\]

と表す。

- \(a_n\)：Sliceを通じてavailableになったlocal articulation
- \(L_n\)：scene内でarticulationをestablishedとして扱うことを支えるcurrent relation / distinction / condition
- \(U_n\)：unresolved / unavailableなresidual local not-yet
- \(C_n^{+}\)：sceneがsupportするcontinuation condition / available continuation

このtupleはformal candidateでありreplacement definitionではない。単一valueでは表せない区別を保持するためのrepresentationである。

\[
K_n=\operatorname{StabScene}(a_n;S_n,B_n,c_n)
\]

と書くことで、StabilityがStructure、Orientation、Contextにrelativeにevaluatedされることを示す。ただしdeterministic、total、single predicate reducibleとはしない。

## 5.5 Readability and Continuability

Canonical Definitionは`readable`を含むが、本論文はこのwordへ一つのuniversal necessary-and-sufficient predicate semanticsを与えない。

weak domain-relative formulationとして

\[
\operatorname{Stable}(a_n;S_n,B_n,c_n)
\Rightarrow
\operatorname{EstablishedFor}_{D}(a_n;S_n,B_n,c_n)
\land
\operatorname{Continuable}_{D}(a_n;S_n,B_n,c_n)
\]

を用いる。subscript \(D\)はdomain-specific interpretationを表す。specialized modelはestablishment conditionを\(\operatorname{Readable}_{D}\)と名付けてもよいが、それはdomain modelが供給するplaceholderであり、本論文がestablishしたuniversal Gyro predicateではない。

このimplicationは、articulationをestablishedとして扱えず、continuationもsupportできない状況でStabilityをclaimできないことのみを示す。converseはuniversally採用しない。

```text
continuable
≠
unchanging
```

```text
readable / established-for
≠
final
```

## 5.6 Residual Not-Yet

Stabilityはunresolved local not-yetを含み得る。\(U_n\)により

```text
local establishment
+
residual local not-yet
```

が同一scene内で共存できる。これはStabilityをStructure全体のclosureとして解釈することを防ぐ。

\[
U_n\neq\varnothing
\quad\text{is compatible with}\quad
K_n\text{ being stable}
\]

は、every Stability Sceneがunresolved elementsを必ず含むことを要求するのではなく、formal modelが\(U_n=\varnothing\)を強制しないことを示す。

## 5.7 Locality and Neighborhood Interpretation

Stabilityはisolated pointよりlocal scene / neighborhoodとして表す方が適切である。neighborhood structureが正当化されるapplicationでは

\[
K_n\subseteq N(a_n)
\]

と書ける。\(N(a_n)\)はadmissible range of variationの下でarticulationがestablished / continuableであり続けるneighborhoodである。

ただしtopologyをuniversal foundationとはしない。neighborhoodはtopological、relational、semantic、operational、probabilistic、domain-specificであり得る。

## 5.8 Stability Does Not Decide

Stabilityはevaluatedされるのであってevaluateしない。Continue、Stop、Jump、Re-Slice、Deferなどのresponseをselectしない。それはCoreのoperational extensionであるOperator Responseに属する。

```text
Stability
≠
Operator Response
```

```text
Structure
→ Slice
→ Stability
→ Operator Response
```

最後のarrowはGyro Processに属し、不変Coreそのものには属さない。

## 5.9 Stability and Later Structure

Stability Sceneはlater Structureへavailableになり得るが、そのままunchanged transferされる必要はない。established distinction、relation、continuation conditionは、later contextでincorporated、revised、weighted、invalidated、inaccessibleになる場合がある。

\[
K_n\rightsquigarrow q_n\rightsquigarrow\Gamma_{n+1}
\]

と表し、\(q_n\)はlocal realizationからincorporatedされるもの、\(\Gamma_{n+1}\)はlater readability contextを示す。

## 5.10 Minimum Formal Commitments

Stability modelは次へcommitする。

1. StabilityはSliceとlocal articulationから区別される。
2. Stabilityはlocal establishmentとcontinuation supportを必要とする。
3. Stabilityはsingle scalarでは表せないinternal structureを持ち得る。
4. Stabilityはresidual local not-yetと共存し得る。
5. StabilityはlocalでありStructureをglobally closeしない。
6. Stabilityはoperational decisionを行わない。
7. Stability SceneはIncorporated Readabilityを通じてlater realizationをconditionし得る。

## 5.11 Transition to Incorporated Readability

articulationがStability Sceneとしてestablished / continuableになった後、そのreadabilityの一部がlater realizationへavailableになる場合がある。persistするものはentire event / state / sceneとは限らず、immutable recordとしてstoredされる必要もない。次節ではIncorporated Readabilityをsimple history preservationではなくcontext updateとして扱う。

# 6 Incorporated Readability and Context Update

## 6.1 From Local Stability to Later Conditions

local Gyro realizationはisolated Stability Sceneで必ず終わるわけではない。articulationが継続可能なestablishmentとして扱えるようになると、そのreadabilityの一部がlater realizationへavailableになる場合がある。これをIncorporated Readabilityと呼ぶ。

Incorporated Readabilityはpreceding event、Slice process、articulation、Stability Sceneそのものではない。local realizationから何がlater condition形成にusableになるかに関係する。established distinction、relation、criterion、relevance ordering、Boundary、Difference pattern、continuity condition、later Orientationに影響するtendencyなどを含み得る。

\[
g_n=(S_n,B_n,c_n,\Sigma_n,a_n,K_n)
\]

とし、incorporated readabilityを

\[
q_n=\operatorname{Inc}(g_n)
\]

と書く。\(\operatorname{Inc}\)はcomplete and lossless summaryをdeterministically extractするoperatorではなく、\(g_n\)を通じてavailableになったreadabilityの一部がlater conditionsへavailableになることを示すprovisional relationである。

## 6.2 Incorporated Readability Is Not Stored History

stored historyはsomething occurredをrecordする。Incorporated Readabilityは、subsequent establishmentのため何がavailableになったかに関係する。

```text
history of prior realization
≠
readability available to later realization
```

logにeventが残っていてもlater interpretationへ影響しない場合がある。逆にoriginal eventがexplicit recordとして残っていなくても、incorporated distinctionがlater interpretationを変える場合がある。

archive \(H_n\)とreadability context \(\Gamma_n\)を分けると

\[
H_{n+1}=\operatorname{Append}(H_n,g_n)
\]

に対し

\[
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n)
\]

となる。前者はoccurrenceをrecordし、後者はlater reading、comparison、orientation、establishmentのconditionsを変える。

## 6.3 Context as an Available Readability Condition

\(\Gamma_n\)はprovisional readability contextであり、every domainでfixed proposition setを意味しない。例えば次をcontain / organizeし得る。

- now available distinctions
- now followable relations
- now applicable criteria
- prior Difference patterns affecting comparison
- usable Boundaries
- relevance weights / priority orderings
- exclusions / invalidations / unresolved conflicts
- conditions under which later Slice may proceed

weak characterizationとして

\[
\Gamma_n=\langle\mathsf{Avail}_n,\mathsf{Weight}_n,\mathsf{Constraint}_n,\mathsf{Access}_n\rangle^{*}
\]

と書ける。\(^*\)はcanonical definitionではなくformal candidateであることを示す。

## 6.4 Non-Monotonic Update

Incorporated Readabilityはmonotonically growすると仮定しない。later updateはaddition、revision、integration、reweighting、invalidation、suppression、loss of accessibilityを含み得る。

\[
\Gamma_n\nsubseteq\Gamma_{n+1}
\]

も

\[
\Gamma_{n+1}=\Gamma_n\cup\{q_n\}
\]

も一般には要求しない。代わりに

\[
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n,e_n)
\]

とし、\(e_n\)はlocal Gyro realizationへ還元できないenvironmental / institutional / interpersonal / material changeなどを表す。

```text
Structure change
≠
Slice
```

を保持し、all later conditionsがpreceding Sliceだけからproducedされるというclaimを避ける。

## 6.5 Weighted Incorporated Readability

すべてのincorporated readabilityが同じinfluenceを持つとは限らない。あるdistinctionはavailableのままperipheralになり、別のdistinctionはlater Contextでdecisiveになり得る。

\[
w_n(q;c,B)\in W
\]

とし、\(W\)はnumericである必要はなく、ordering、priority class、partial orderなどでよい。

\[
\operatorname{Effective}(q_n;B_m,c_m,\Sigma_m)
\]

はone later realizationでholdしてもanotherではfailし得る。Incorporated Readabilityはpermanent universal ruleではなく、context-relative influenceを持ってlater Structure conditionsへwovenされたreadabilityである。

## 6.6 Structure Update

later Structureはcompletely independent objectとは扱わないが、Incorporated Readabilityだけからderivedされるとも扱わない。

\[
(S_n,\Gamma_{n+1},e_n)\rightsquigarrow S_{n+1}
\]

とする。このrelationはupdateがpartial、distributed、non-deterministic、only retrospectively readableであり得ることを許す。

```text
Structure
≠
readability context
```

を保持しつつ、incorporated readabilityがlater Structure conditionsを変える可能性を認める。

## 6.7 Example: Mathematical Reasoning

mathematical problemを解く途中で、definition、lemma、intermediate equality、admissible transformationがfinal proofより先にestablishedすることがある。一度establishedすればlater stepで使用できる。それは単に「そのstepが起きた」というhistoryではなく、later reasoningで何をlegitimately useできるかを変える。

\[
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n)
\]

later correctionが\(q_n\)をrevise / invalidateすればeffective contextも変わるため、modelはincorporationとretractionの双方をsupportする。

## 6.8 Minimal Commitments

1. local Gyro realizationはsome readabilityをlater realizationへavailableにし得る。
2. incorporatedされるものはcomplete prior realizationと同一ではない。
3. incorporated readabilityはstored historyへ還元されずlater conditionsを変え得る。
4. updateはnon-monotonicかつcontext-relativeであり得る。
5. external changeはlocal Gyro realization由来changeからformalに区別される必要がある。

\(\Gamma_n\)を常にlogical theory、database、memory store、vector state、probability distributionと仮定しない。

## 6.9 Transition to Continuity Readability

Incorporated Readabilityはlocal establishmentがlater conditionsへavailableになる仕方を説明するが、two local realizationsがconnectedとして扱えるかはまだ決めない。そのためrelation existence、traceability、admissibility、current continuity judgmentをさらに区別する必要がある。

# 7 Continuity Readability and Identity

## 7.1 From Local Establishment to Relational Continuity

preceding sectionのcontext updateはlater comparison / tracingを可能にするが、それだけでtwo realizationsがcontinuousとはならない。relationは存在してもuntraceableであり得るし、traceableでもgiven Orientation、Context、Slice、incorporated contextでcontinuityとしてcountしない場合がある。

```text
relation existence
≠
traceability
≠
admissibility
≠
continuity judgment
```

Continuityはtwo realizationsがintrinsically持つpropertyではなく、specific conditionsの下でavailableになるrelational judgmentとして扱う。

## 7.2 Local Gyro Realizations

\[
g_i=(S_i,B_i,c_i,\Sigma_i,a_i,K_i)
\]

とし、各componentはStructure、Operator Orientation、Context、Slice process、local articulation、Stability Sceneを表す。このtupleはbookkeeping schemaであり、every realizationがontologically six independent objectsへ分解されることを意味しない。

## 7.3 Relation Existence

candidate relation \(r\)を

\[
r(g_i,g_j)
\]

または

\[
g_i\xrightarrow{r}g_j
\]

と書く。\(r\)はdomain-relativeであり、causal succession、functional succession、semantic inheritance、material transfer、recognized Difference pattern、Boundary correspondence、response-to-orientation linkage、retained readability condition、institutional / rule-based connectionなどを表し得る。

## 7.4 Traceability

\[
\operatorname{Traceable}(g_i,g_j;r)
\]

はrelationをone realizationからanotherへfollowできるかを表す。available evidence、incorporated readability、temporal reach、admissible inference rule、access conditionなどへ依存し得る。

\[
r(g_i,g_j)\not\Rightarrow\operatorname{Traceable}(g_i,g_j;r)
\]

relation existenceはtraceabilityを保証しない。

## 7.5 Admissibility

traceable relationがすべてrelevant continuity relationになるわけではない。

\[
\operatorname{Adm}(r;B,c,\Sigma,\Gamma)
\]

を、Orientation、Context、continuity-oriented Slice、incorporated readability contextの下で\(r\)がadmissibleであることを表すpredicateとする。

admissibilityはrelevance、scope、permitted inference、causal sufficiency、semantic compatibility、material continuity、institutional validity、temporal accessibility、trust / evidence requirementなどをencodeし得る。universal、static、binaryとは仮定しない。

## 7.6 Continuity Readability

Continuity ReadabilityというGyro termは維持するが、universal independent `Readable(...)` predicateで定義しない。

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma)
\iff
\exists r\bigl(
\operatorname{Adm}(r;B,c,\Sigma,\Gamma)
\land
\operatorname{Traceable}(g_i,g_j;r)
\land
\operatorname{CountsAsContinuity}_{D}(r;B,c,\Sigma,\Gamma)
\bigr)
\]

とする。\(\operatorname{CountsAsContinuity}_{D}\)はexplicitly domain-relative placeholderである。specialized modelはjustified \(\operatorname{Readable}_{D}\)、graded evidence structure、logical rule、causal criterion、institutional ruleなどを用いてよい。

```text
Is there an admissible relation?
Can it be traced?
Does the domain model currently count it as continuity?
```

という三つのoperational questionを分離する。

## 7.7 Continuity Readability Is Context-Relative

same pair of realizationsでも

\[
\operatorname{CR}(g_i,g_j;B_1,c_1,\Sigma_1,\Gamma_1)
\neq
\operatorname{CR}(g_i,g_j;B_2,c_2,\Sigma_2,\Gamma_2)
\]

となり得る。これはcontinuityがarbitraryという意味ではなく、admissibilityとdomain-relative continuity conditionがexplicit conditionsへdependすることを意味する。

## 7.8 Identity as a Separate Criterion

\[
\operatorname{Id}_{q}(g_i,g_j)
\]

を、identity criterion \(q\)の下で\(g_i, g_j\)をsame entity / bearer / Structureとして扱うこととする。\(q\)はnumerical、legal、functional、material persistence、semantic、account、biological、role identityなどであり得る。

\[
\operatorname{CR}(g_i,g_j)\not\equiv\operatorname{Id}_{q}(g_i,g_j)
\]

Continuityはadmissible relationをtraceしcontinuityとしてcountできるか、Identityはcriterionの下でsameと扱うか、というdifferent questionsである。

## 7.9 Continuity Without Identity

\[
\operatorname{CR}(g_i,g_j)=\mathrm{true}
\]

かつ

\[
\operatorname{Id}_{q}(g_i,g_j)=\mathrm{false}
\]

を許す。batterとcakeはtype / object criterionではdifferentでも、material transformation、causal succession、production historyを通じてcontinuityが成立し得る。

```text
Identity break
≠
Trajectory break
```

## 7.10 Identity Without Readable Continuity

逆に

\[
\operatorname{Id}_{q}(g_i,g_j)=\mathrm{true}
\]

でありながら

\[
\operatorname{CR}(g_i,g_j)=\mathrm{false}
\]

またはindeterminateである場合も許す。institutionがsame legal personをassertしていてもcontinuity reconstructionが現在できない場合、systemがsame account identifierを保持していてもbehavioral / operational trajectoryがunavailableな場合などである。

## 7.11 Continuity Readability and Difference

ContinuityはDifference absenceを要求しない。むしろstructured Difference patternをtraceできるためcontinuityがavailableな場合もある。

\[
\Delta_{B,c,\Sigma}(g_i,g_j)\neq0
\]

でも、そのDifferenceがcontinuity relation内でadmissibleならcontinuityは成立し得る。

```text
continuity
≠
unchanged sameness
```

## 7.12 Continuity Readability and Incorporated Readability

\(\Gamma\)はどのrelationがadmissibleか、どのcontinuity ruleをapplyできるかに影響する。

\[
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n,e_n)
\]

の後、

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma_{n+1})
\]

が\(\Gamma_n\)の下のjudgmentと異なる場合がある。previously unavailable relationがlater evidenceによってtraceable / continuity-countingになる場合も、previously accepted continuityがinvalidatedされる場合もある。

## 7.13 Binary and Graded Forms

\[
\operatorname{CR}^{*}(g_i,g_j;B,c,\Sigma,\Gamma)\in\mathcal{C}
\]

とし、\(\mathcal{C}\)をordered set、confidence interval、evidence structure、domain-specific classificationとしてもよい。Continuityをuniversally binary / numericalとはしない。

## 7.14 Minimal Commitments

1. Local Gyro realizationはrelationを持ち得る。
2. Relation existence、traceability、admissibility、continuity judgmentは区別される。
3. Continuity ReadabilityはOrientation、Context、Slice、incorporated readabilityにdependする。
4. Identityはseparate criterionである。
5. ContinuityはDifferenceやidentity changeをまたいでpersistし得る。
6. Identityはcontinuity unavailable / disputedでもassertされ得る。
7. Continuity readingはRe-Slice / context updateによりreviseされ得る。

Continuityをequivalence relation、always transitive、symmetric、globally decidableとは仮定しない。

## 7.15 Transition to Contextual Trajectory

particular local realizationsがconnectedとして扱えることと、broader Trajectoryは別である。Trajectoryにはfamily of local realizations、retained relation field、contextual tracing operationが必要となる。

# 8 Contextual Trajectory

## 8.1 From Local Continuity to Trajectory

Trajectoryはadditional Core elementではなく、multiple local Gyro realizationをgiven Orientation、Context、Slice、incorporated readability conditionの下でconnectedとして扱うderivative relational constructionである。

```text
Trajectory
≠
state sequence
≠
chronological log
≠
event collection
≠
relation-bearing field itself
```

## 8.2 Local Gyro Realizations

\[
g_i=(S_i,B_i,c_i,\Sigma_i,a_i,K_i)
\]

のfamilyを

\[
G=\{g_i\}_{i\in I}
\]

とする。\(G\)自体はTrajectoryではなく、one or more trajectoriesをsupportし得るlocal realizationsのcollectionである。

## 8.3 The Relation-Bearing Trace Field

possible relation type familyを\(\mathcal{R}\)とし、

\[
E\subseteq G\times\mathcal{R}\times G
\]

\[
\mathcal{G}_R=(G,E)
\]

をrelation-bearing trace fieldとする。\((g_i,r,g_j)\in E\)は、type \(r\)のrelationがavailable / retained / inferred / representableであることを示す。causal、material、functional、semantic、procedural、institutional、identity-related、Boundary-related、Difference-relatedなどを含み得る。

```text
relation-bearing trace field
≠
Trajectory
```

## 8.4 Contextual Tracing

Trajectoryを

\[
T_{B,c,\Sigma_T,\Gamma_T}
=\operatorname{Trace}_{B,c,\Sigma_T,\Gamma_T}(G,E)
\]

とprovisionally表す。tracing operationは\(G\)や\(E\)を単純enumerateするのではなく、current conditionsの下でadmissible tracesをselect、compose、suppress、weight、interpretする。

same relation-bearing fieldでもdifferent Orientation / Context / Slice / readability contextによってdifferent Trajectoryが成立し得る。

## 8.5 Admissibility of a Trace

candidate trace

\[
\pi=(g_{i_0},r_1,g_{i_1},r_2,\ldots,r_m,g_{i_m})
\]

のTrajectory inclusionにはformal adjacency以上が必要である。

\[
\operatorname{AdmTrace}(\pi;B,c,\Sigma_T,\Gamma_T)
\]

はrelation type admissibility、successive relation compatibility、relevance weight、retained Difference pattern、Boundary condition、continuity criteria、missing intermediate realizations、contextual interpretation constraintsなどへdependし得る。

## 8.6 Trajectory Is Not a Predefined State Sequence

ordinary state trajectory

\[
x_0,x_1,x_2,\ldots,x_n
\]

はcommon state spaceとordering relationをpresupposeする。Gyro Trajectoryはweaker assumptionsでよく、connected realizationsはtype、representation、granularity、identityが異なり得る。heterogeneous relationsを通じてcontinuityが成立してよい。

## 8.7 Trajectory Is Not a Log

chronological logはeventがorderを伴ってstoredされたことをrecordするが、どのrelationがadmissible / traceable / continuityとしてcountするかを自動的に決めない。

\[
H\neq T_{B,c,\Sigma_T,\Gamma_T}
\]

same historyがmultiple trajectories、no current trajectory、later trajectoryをsupportし得る。

## 8.8 Branching, Merging, and Multiple Trajectories

Trajectoryはlinearである必要がない。branching、merging、parallel trajectories、competing trajectories、nested trajectories、partial trajectoriesを許す。implementationはgraph-like、hypergraph-like、partially ordered、category-like、event-structuralであり得るが、universal formを一つに固定しない。

## 8.9 Gaps and Unavailable Intervals

missing intermediate realizationは自動的にTrajectory breakを意味しない。gapをまたいでadmissible relationをtraceできればcontinuityはavailableであり得る。一方dense recordがあってもadmissible continuity relationがなければTrajectoryにならない。

```text
record gap
≠
Trajectory break
```

```text
dense history
≠
continuity
```

## 8.10 Retrospective Tracing and Re-Slice

later realizationがpreviously unavailableだったrelation / evidenceを導入すると、Re-Sliceによりearlier realizationsやretained relationsをdifferent wayでtraceできる。

\[
T^{(n)}=\operatorname{Trace}_{B_n,c_n,\Sigma_n,\Gamma_n}(G,E)
\]

\[
T^{(n+1)}=\operatorname{Trace}_{B_{n+1},c_{n+1},\Sigma_{n+1},\Gamma_{n+1}}(G,E)
\]

changeはpastがalteredされたことを意味せず、retained tracesのpresent organizationがlater conditionsの下で変化したことを意味する。

related but distinct problemとしてretrospective establishmentがある。later Operatorは、availableなtrace、relation、consequence、later establishmentからearlier eventについてpresent local establishmentを形成し得る。

```text
past event itself
≠
present establishment about the past event
```

またone remaining traceがpast eventをuniquely determineするとは主張しない。

## 8.11 Jump and Non-Continuous Reconstruction

Jumpはlarge numerical discontinuityだけではない。current continuity conditionsがexisting trace organizationを通じたadmissible continuationをsupportできない場合のreconstructionに関係する。

```text
Jump
≠
large Difference only
```

```text
Jump
≠
necessary deletion of prior Trajectory
```

## 8.12 Relation to Incorporated Readability

\(\Gamma_T\)のchangeはpreviously unavailable relationをexpose、accepted relationをinvalidate、competing tracesのweightをchange、separated realizationsをconnect、one Trajectoryをsplit、multiple trajectoriesをmergeし得る。

Trajectoryはprior Gyro realizationからindependentではないが、stored accumulationへreducibleでもない。

## 8.13 Minimal Commitments

1. local Gyro realizationをprovisionally referenceできる。
2. heterogeneous relationsをrepresentできる。
3. relation existence、traceability、admissibility、continuity judgmentを区別する。
4. tracing operationはOrientation、Context、Slice、Incorporated Readabilityにconditionされる。
5. tracing resultはnon-linear、partial、revisable、pluralであり得る。
6. TrajectoryはderivativeでありCoreを置き換えない。

## 8.14 Transition to Difference and Boundary

Tracingにはlocal realization間やpossible relation間のdistinctionが必要である。Differenceをmetric distance / errorと仮定せず、BoundaryをDifferenceそのものと同一視しない。

# 9 Difference and Boundary

DifferenceとBoundaryはderivative conceptsであり、不変Coreをreplaceせず、Structure・Slice・Stability間のadditional stageにもならない。Orientation、Context、Sliceの下でnon-coincidenceがどのようにavailable / organized / usableになるかを記述する。

## 9.1 Difference Is Not Distance

Differenceは必ずしもnumerical distance、deviation、residual、errorではない。metric space、norm、comparison scale、target valueが正当化されるdomainではそれらが有用だが、universally仮定しない。

\[
\Delta_{B,c,\Sigma}:X\rightharpoonup D
\]

とし、\(D\)はscalar、vector、ordered tuple、relation、partial order、distribution、symbolic classification、field-like objectなどであり得る。partial arrowはevery inputでDifferenceがavailableとは限らないことを示す。

metric

\[
d:X\times X\to\mathbb{R}_{\geq0}
\]

はadditional commitmentsが正当化されるspecial caseである。

```text
Difference
≠
Distance
```

## 9.2 Difference Is Not Error

Errorはreference、norm、target、expected value、accepted stateをpresupposeする。Differenceはそのevaluative meaningを必ずしも持たない。

```text
Difference
≠
Error
```

change in form / role / interpretation / relation / continuationはfailureでなくてもDifferenceであり得る。

## 9.3 Difference as Slice-Relative Structured Non-Coincidence

working characterizationは次である。

> Difference is a Slice-relative structured relation of non-coincidence.

DifferenceはSlice-relative、structured、relationalである。pairwiseには

\[
\Delta_{B,c,\Sigma}(x,y)
\]

generalには

\[
\Delta_{B,c,\Sigma}(X)
\]

と書ける。

## 9.4 Difference and Local Articulation

DifferenceはSlice以前にalready usable objectとして存在する必要はない。Sliceを通じてlocal articulation \(a_n\)内でstructured non-coincidenceがavailableになり得る。

\[
S_n\xRightarrow{\Sigma_{B_n,c_n}}a_n
\]

Difference patternはStability Sceneの\(L_n\)、\(U_n\)、\(C_n^{+}\)へcontributeし得る。StabilityはDifferenceがzeroであることを要求しない。

\[
\Delta_n\neq0
\]

でもStabilityとcompatibleであり、\(\Delta_n=0\)だけでStability / Identity / Continuity Readabilityを保証しない。

## 9.5 Boundary Is Not Difference

BoundaryはDifferenceと同一ではない。Differenceはstructured non-coincidence、Boundaryはparticular Sliceの下でlocally usableになったdistinctionである。

```text
Difference
→ may become locally usable as a distinction
→ Boundary
```

これはmandatory temporal sequenceではなくderivative relationを表す。

```text
Difference
≠
Boundary
```

## 9.6 Boundary as a Slice-Relative Distinction

supporting characterizationは次である。

> Boundary is a Slice-relative distinction that has become readable through Slice.

ここで`readable`はcanonical explanatory roleを維持し、universal independent predicateを意味しない。Boundaryはfixed line intrinsically contained in Structureとは仮定しない。spatial、logical、semantic、operational、social、temporal、procedural、hybridであり得る。

\[
\operatorname{Bd}_{B,c,\Sigma,\Gamma}(d)
\]

を、distinction \(d\)がstated conditionsの下でBoundaryとしてfunctionすることとする。

## 9.7 Boundary State

\[
\operatorname{BS}(x\mid d,B,c,\Sigma,\Gamma)
\]

は、object / event / articulation / realizationがBoundary \(d\)にrelativeにどのstateにあるかを表す。normal、non-、un-、absent、blank、unknown、void-relative、inside、outside、crossing、deferredなどdomain-specific classificationを取り得る。

## 9.8 Boundary, Continuity, and Trajectory

Boundaryはone kind of continuityをinterruptしつつanotherをpreserveし得る。type Boundary crossingがIdentity criterionをbreakしても、material / causal / semantic / functional continuityがavailableな場合がある。

```text
Boundary crossing
≠
Trajectory break
```

## 9.9 Incorporation of Difference and Boundary Readability

\[
q_n^{\Delta}=\operatorname{Inc}_{\Delta}(g_n)
\]

\[
q_n^{\mathrm{Bd}}=\operatorname{Inc}_{\mathrm{Bd}}(g_n)
\]

としてlater contextをupdateし得る。

\[
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n^{\Delta},q_n^{\mathrm{Bd}},e_n)
\]

inclusionはpermanent preservationを意味せず、revision、reweighting、invalidation、suppression、loss of accessibilityを許す。

## 9.10 Formal Commitments and Non-Commitments

1. DifferenceはOrientation、Context、Sliceにrelative。
2. Differenceはpartial / heterogeneousであり得る。
3. Differenceはuniversally metric / error-likeではない。
4. Boundaryはlocally usable distinctionからderivativeでありDifferenceそのものではない。
5. Boundary Stateはrelational / provisional。
6. DifferenceとBoundaryはStability、Continuity Readability、Trajectory、later incorporated readabilityに影響し得る。

# 10 Minimal Formal Model

## 10.1 Purpose of the Integrated Schema

preceding sectionsのcomponentsを一つのminimal schemaへintegrateする。complete axiomatizationやfinal mathematical ontologyを与えるのではなく、current theoretical distinctionsを維持するために必要なsmallest set of distinguishable objects / relationsを示す。

不変Core

```text
Structure
↓
Slice
↓
Stability
```

を維持しつつ、local realization conditions、Sliceからavailableになるarticulation、later contextへincorporatedされるreadability、continuity / Trajectoryに関わるrelationsをrepresentする。

## 10.2 Local Gyro Realization

\[
g_n=(S_n,B_n,c_n,\Sigma_n,a_n,K_n)
\]

各componentはStructure、Operator Orientation、Context、Slice process、local articulation、Stability Sceneである。このtupleはrepresentational convenienceであり、Orientation、Context、local articulationをCoreへ挿入しない。

\[
S_n\xRightarrow{\Sigma_{B_n,c_n}}a_n\xRightarrow{\operatorname{Stab}}K_n
\]

first relationはOrientation / Contextの下のSlice process、second relationはlocal articulationからStability Sceneへのtransitionを表す。いずれもdeterministic total functionとはしない。

## 10.3 Structure

Structureは\(S_n\)とreferenceするがmathematical typeはopenに保つ。

\[
x\triangleleft S_n
\]

を、\(x\)が\(S_n\)にrelativeにlocally establishable / availableであるweak relationとする。

## 10.4 Slice and Local Articulation

\[
S_n\xRightarrow{\Sigma_{B_n,c_n}}a_n
\]

は

```text
Slice process
≠
local articulation
```

を保つ。\(a_n\)がSlice以前にfully individuated resultとして存在することも、すでにStableであることも仮定しない。

## 10.5 Stability Scene

\[
K_n=(a_n,L_n,U_n,C_n^{+})
\]

とprovisionally表し、\(U_n\neq\varnothing\)でもStability Sceneであり得る。

\[
\operatorname{StabScene}(a_n;S_n,B_n,c_n)
\]

はarticulationをrelevant conditions下でestablished / continuableとして扱えることを示すweak conditionである。

## 10.6 Incorporated Readability

\[
q_n=\operatorname{Inc}(g_n)
\]

\[
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n,e_n)
\]

とし、append-only historyと同一視しない。

\[
(S_n,\Gamma_{n+1},e_n)\rightsquigarrow S_{n+1}
\]

はall Structure changeがpreceding Gyro realizationからgeneratedされるとは主張しない。

## 10.7 Continuity Readability

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma)
\iff
\exists r\bigl(
\operatorname{Adm}(r)
\land
\operatorname{Traceable}(r)
\land
\operatorname{CountsAsContinuity}_{D}(r)
\bigr)
\]

とweakly表す。

```text
relation existence
≠
traceability
≠
admissibility
≠
continuity judgment
```

Identityは\(\operatorname{Id}_{q}(g_i,g_j)\)としてseparate relationである。

## 10.8 Relation-Bearing Trace Field and Trajectory

\[
G=\{g_i\}_{i\in I}
\]

\[
E\subseteq G\times\mathcal{R}\times G
\]

\[
\mathcal{G}_R=(G,E)
\]

とする。trace fieldはTrajectoryそのものではない。

\[
T_{B,c,\Sigma_T,\Gamma_T}=\operatorname{Trace}_{B,c,\Sigma_T,\Gamma_T}(G,E)
\]

Trajectoryはcontextual tracingのresultであり、branching、merging、gap、retrospective reinterpretation、Re-Slice、Jumpを含み得る。

## 10.9 Difference

\[
\Delta_{B,c,\Sigma}:X\rightharpoonup D
\]

とし、\(D\)をheterogeneousに保つ。

```text
Difference
≠
Distance
≠
Error
≠
Boundary
```

## 10.10 Compact Integrated Form

\[
g_n=(S_n,B_n,c_n,\Sigma_n,a_n,K_n)
\]

\[
S_n\xRightarrow{\Sigma_{B_n,c_n}}a_n
\]

\[
K_n=\operatorname{StabScene}(a_n;S_n,B_n,c_n)
\]

\[
q_n=\operatorname{Inc}(g_n)
\]

\[
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n,e_n)
\]

\[
(S_n,\Gamma_{n+1},e_n)\rightsquigarrow S_{n+1}
\]

\[
\operatorname{CR}(g_i,g_j)\iff\exists r:\operatorname{Adm}(r)\land\operatorname{Traceable}(r)\land\operatorname{CountsAsContinuity}_{D}(r)
\]

\[
\mathcal{G}_R=(G,E)
\]

\[
T=\operatorname{Trace}(G,E)
\]

\[
\Delta_{B,c,\Sigma}:X\rightharpoonup D
\]

## 10.11 What the Model Guarantees

current exploratory levelでmodelがguaranteeするのはconceptual / formal separationである。Structure、Slice process、local articulation、Stability Scene、historyとIncorporated Readability、relation existenceとContinuity Readability、Identityとcontinuity、trace fieldとTrajectory、Differenceとmetric / error / Boundaryを分ける。またGyro Logic / GyroOS / GyroAuth layer separationも維持する。

## 10.12 What the Model Does Not Guarantee

complete axiomatization、universal semantics、uniqueness of representation、decidability、complexity bound、empirical validation、strict mathematical minimality proofは提供しない。Structureのfinal type、universal Stability measure、universal tracing algorithm、universal Difference codomainも確定しない。

# 11 Visual Overview of the Minimal Formal Model

## 11.1 Figure 1: Invariant Core

![Gyro Logicの不変Core。Operator OrientationとContextはSliceをconditionするが、additional Core elementではない。](figures/fig1_invariant_core.svg){width=94%}

Figure 1は、本論文全体を支配するtheoretical constraintを示す。不変CoreはStructure → Slice → Stabilityのままである。Operator Orientation、Context、local articulation、Trajectory、Difference、Boundary、Operator Responseを第四のCore要素として挿入しない。

## 11.2 Figure 2: Local Gyro Realization and Context Update

![local Gyro realization、Stability Scene、later readability conditionsのupdate。](figures/fig2_local_realization.svg){width=96%}

Figure 2は

\[
g_n=(S_n,B_n,c_n,\Sigma_n,a_n,K_n)
\]

を要約する。Slice processとlocal articulation、articulationとStability Sceneを分離し、Incorporated Readability \(q_n=\operatorname{Inc}(g_n)\)がlater readability context \(\Gamma_{n+1}\)をupdateする一方で、external change \(e_n\)も明示的に残す。

## 11.3 Figure 3: Contextual Trajectory

![relation-bearing fieldからTrajectoryへのcontextual tracing。](figures/fig3_contextual_trajectory.svg){width=96%}

\[
\mathcal{G}_R=(G,E)
\]

と

\[
T_{B,c,\Sigma_T,\Gamma_T}=\operatorname{Trace}_{B,c,\Sigma_T,\Gamma_T}(G,E)
\]

を分ける。relation-bearing fieldはheterogeneous / dormant / conflicting / unavailable relationsを含み得る。contextual tracingはrelationをadmit、suppress、weight、compose、interpretし、resulting Trajectoryはbranch、merge、gap、retrospective revisionを持ち得る。

## 11.4 Figure Interpretation Boundary

figuresはexplanatory summaryでありreplacement definitionではない。Structureがbox、Sliceがdeterministic arrow、Stabilityが常にtuple、Trajectoryが常にgraphであることを意味しない。

# 12 Related Work and Formal Positioning

## 12.1 Relation to the Foundational Gyro Logic Paper

本論文はfoundational Gyro Logic paperをreplaceするものではなくformalization companionである。earlier paperは不変Coreを導入し、「Gyro Logicとは何か」を扱った [@kawakami2026gyro_logic_en]。本論文は、そのCore周辺で形成された区別をCanonical Definitionを変更せずprovisional formal schemaへ整理する、よりnarrow methodological questionを扱う。

```text
foundational paper
=
conceptual introduction and theoretical orientation
```

```text
present paper
=
minimal formal organization and comparison boundary
```

## 12.2 Relational and Graph-Based Models

relational structures / graph theoryはheterogeneous local realizationsとretained relationsを表すため有用である。graphはvertex、edge、path、connectedness、branching、transformationを扱える [@diestel2017graph]。ただしgraphはrelevant node / edgeがalready individuatedされていることを通常前提とする。Gyro Logicではrelation-bearing fieldとTrajectoryを分け、Trajectoryをadmissibilityとdomain-relative continuity conditionsの下のcontextual tracing resultとする。

## 12.3 Event Structures and Concurrency

event structuresはoccurrence、causal dependency、conflict、concurrencyを一つのinterleaved sequenceへ還元せず扱う [@nielsen1981petri; @vanglabbeek2009configuration]。branching / merging / conflict / partial order / non-linear Trajectoryに関係するが、formally represented eventsとenabling / conflict relationsから始まる点で、local articulationがavailableになるSliceより強いcommitmentを持つ。

## 12.4 Transition Systems, Model Checking, and Process Algebra

transition systems / model checkingはstates、labels、transition relationsが定義された後のstate evolution、branching、temporal property、verificationに強い [@baier2008principles]。process algebraもinteraction、concurrency、synchronization、continuationをcompositionalに扱う [@milner1980ccs; @milner1982combinators]。Gyro Process / Loop / Operator Response / Re-Slice / Defer / Jumpのimplementationには有用だが、不変Coreのreplacement definitionにはしない。

## 12.5 Dynamical Systems and Stability

dynamical systemsはtrajectory、equilibrium、attractor、oscillation、convergence、bifurcation、perturbationを扱う [@strogatz2015nonlinear]。Gyro Stabilityはよりbroaderであり、ongoing change / residual not-yetと共存し得る。Gyro Trajectoryもtime-indexed state solutionとはuniversally同一視しない。

## 12.6 Topology, Locality, and Sheaf-Like Structures

topologyはneighborhood、continuity、closure、separation、boundaryを形式化する [@munkres2000topology]。sheaf theoryはlocal information、restriction、compatibility、local-to-global failureを扱う [@maclane1992sheaves]。Stability Sceneのlocalityやglobal non-closureとの対応はあるが、specified underlying space / site / coveringをuniversally仮定しない。

## 12.7 Category Theory and Composition

category theoryはobject、morphism、composition、identity、functorを通じてheterogeneous transformationを扱う [@maclane1998categories]。ただしordinary morphismはdomain / codomainをpresupposeするため、local articulationがSlice以前にfully determined codomainとして存在しない一般ケースにはそのまま適用しない。

## 12.8 Belief Revision and Non-Monotonic Context Update

AGM belief revisionはbelief setのcontraction / revisionをpostulatesで形式化する [@alchourron1985logic]。Incorporated Readabilityのnon-monotonic updateには関連するが、\(\Gamma\)はdeductively closed belief setである必要はなく、material / procedural / perceptual / institutional / operationalなincorporationもあり得る。

## 12.9 Probabilistic and Statistical Models

probability / statisticsはuncertainty、confidence、evidence、heterogeneous observationをquantifyでき、probabilistic graphical modelはstructured dependency / inferenceの成熟したframeworkである [@koller2009probabilistic]。graded domain-specific establishment/readability、Stability confidence、Difference distribution、competing Trajectory hypothesisをinstantiateし得るが、relevant variable / event / distinctionがどうarticulableになるかまでは説明しない。

## 12.10 Position of the Present Model

reviewed fieldsはいずれも有力なformal resourcesを提供するが、particular objects / relations / spaces / events / operationsがspecifiedされた後に適切となるcommitmentを持つ。Minimal Formal Modelはそれらをreplaceするのではなく、どのdistinctionを保持すべきかを示すcoordination roleを持つ。

```text
Gyro Logic Minimal Formal Model
≠
a replacement for established mathematics
```

```text
Gyro Logic Minimal Formal Model
=
a formal boundary for selecting and coordinating partial models
```

# 13 Comparison with Existing Mathematical Fields

## 13.1 Purpose of the Comparison

比較は、どの単一分野へGyro Logicが「属するか」を決めるためではなく、各fieldがどのrepresentationを得意とし、どのassumptionによってGyro-specific distinctionを失うかを見るために行う。

1. **Representational usefulness**：schemaのどの部分をeffectiveにmodelできるか
2. **Reduction risk**：fieldをuniversal formにしたとき何を失うか

## 13.2 Relational Structures

heterogeneous objects、partial relations、admissibility conditions、Difference patterns、Boundary relations、local realization connectionsをnumeric / metric assumptionsなしに表せる。ただしobject / relationがalready availableに見えるため、Sliceを通じてlocal articulationがavailableになる過程は単独では説明しない。

## 13.3 Graphs and Hypergraphs

\[
\mathcal{G}_R=(G,E)
\]

としてtrace-bearing relationsを表すのに自然であり、directed graph、multigraph、hypergraphはbranching / merging / competing traces / gaps / retrospective reconnectionに有用。ただしgraphそのものをTrajectoryとはしない。

## 13.4 Order Theory

precedence、dependency、refinement、relevance ordering、partial comparabilityを表せる。

\[
x\preceq_{B,c,\Gamma}y
\]

のようなrelationをdomain-relativeに使えるが、Differenceがalways orderableとは限らない。

## 13.5 Topology and Neighborhood Structures

Stability Sceneを

\[
a_n\in N_n
\]

のようなneighborhood interpretationで表す場合に有用。しかしGyro Stabilityをtopological stabilityへ、Boundaryをtopological set boundaryへ、not-yetをtopological opennessへ還元しない。

## 13.6 Dynamical Systems

\[
x_{t+1}=F(x_t,u_t)
\]

のようなmodelはGyroOS / GyroAuthでmeasurable state variableが定義された場合に強い。Stability score、convergence、drift、recoveryを扱えるが、Trajectoryをstate evolutionそのもの、StabilityをLyapunov / equilibriumだけへ還元しない。

## 13.7 Transition Systems and Event Structures

operational succession、branching choices、enabled actions、causality、conflict、concurrencyを扱える。Gyro Process / Operator Response / Re-Slice / Jumpに有用だが、states / events / transitionsをexecution以前にspecifiedするため、pre-individuated Structure全体のmodelにはならない。

## 13.8 Category Theory

heterogeneous object、transformation、composition、identityを扱うintegration languageとして有力。ただしordinary morphismはdomain / codomainをfixedするため、Slice以前のarticulation未確定性をそのままuniversalizeしない。

## 13.9 Logic and Proof Theory

\[
\Gamma_n\vdash\varphi
\]

のようなproof contextはIncorporated Readabilityのpartial modelとして強い。context extension、revision、non-monotonic inference、belief revisionを扱えるが、proposition / predicate / inference ruleがalready articulatedであることを前提とする。

## 13.10 Constraint Satisfaction and Constraint Propagation

variables、domains、constraintsからlocally coherent configurationを作る点でSlice implementation候補になる。ただしvariables / domains / constraintsがpre-specifiedされるため、Structure全体のuniversal modelではない。

## 13.11 Probability and Statistics

uncertainty、confidence、evidenceをquantifyできるが、event space / measurable variableがalready articulatedであることを必要とする。

## 13.12 Sheaf-Like and Local-to-Global Structures

local data、overlap compatibility、failure of global gluingを扱い、local Stabilityとglobal non-closureに対応し得る。ただしbase space、covering、restriction mapsをuniversally仮定しない。

## 13.13 Process Algebra

interaction、concurrency、communication、choice、interruption、continuationをexecutably / compositionally扱える。Gyro Process / Loopに有用だが、action vocabulary / process syntaxがalready articulatedである。

## 13.14 Comparative Summary

| Mathematical field | Strongest Gyro correspondence | Main reduction risk |
|---|---|---|
| Relational structures | Difference, Boundary, heterogeneous relations, continuity | Objects and relations appear pre-given |
| Graphs / hypergraphs | Trace fields, branching, merging, multi-relational connection | Graph mistaken for Trajectory |
| Order theory | Dependency, relevance, partial precedence | Incomparable Difference forced into order |
| Topology | Locality, neighborhoods, bounded variation, some Boundary models | Stability reduced to topology; not-yet reduced to openness |
| Dynamical systems | Evolution, convergence, drift, recovery | Trajectory reduced to state sequence; Stability reduced to equilibrium |
| Transition / event structures | Branching process, causality, conflict, concurrency | States and events assumed pre-individuated |
| Category theory | Heterogeneous transformation and composition | Domain and codomain fixed before Slice |
| Logic / proof theory | Incorporated Readability and context update | Propositions and rules assumed already articulated |
| Constraint propagation | Emergence of locally coherent articulation | Variables and constraints assumed pre-specified |
| Probability / statistics | Uncertainty and confidence models | Event space assumed in advance |
| Sheaf-like structures | Local-to-global compatibility and failure of gluing | Base space and coverings assumed |
| Process algebra | Operational loops, interaction, response | Action vocabulary assumed articulated |

## 13.15 A Heterogeneous Composite Model

Minimal Formal Modelはexisting disciplinesのcompetitorではなく、multiple partial modelsをcoordinateするschemaとして理解するのが適切である。domain-specific implementationは、relational / hypergraph structures、neighborhood / topology、logical / non-monotonic context、event structure / process algebra、probabilistic / dynamical model、category-theoretic compositionなどを組み合わせ得る。ただしどのcomponentもconvenient implementation objectであることを理由に不変Coreを再定義してはならない。

## 13.16 Result of the Comparison

examined fieldのどれもadditional assumptionsなしにGyro Logic全体のcomplete universal modelを提供しない。一方、現段階でwholly independent mathematicsも必要ではない。existing fieldsはscopeを明示すればstrong partial modelsを提供する。

# 14 Illustrative Examples

本節のexampleはempirical validationやuniqueness proofではなくconceptual stress testである。

## 14.1 Example 1: Mathematical Problem Solving

proof途中のproblem、prior assumptions、available lemmas、notation、unresolved obligationsをStructure \(S_n\)とみなす。Orientationはsub-lemma proof、invariant isolation、goal reformulationなどへ向けられ得る。Sliceを通じて

```text
Let q_n denote the quantity preserved under the transformation.
```

のようなlocal articulationがavailableになる。

Stability Sceneは

\[
K_n=(a_n,L_n,U_n,C_n^{+})
\]

として、definitionをintelligibleにするrelations、remaining proof obligations、enabled deductionsを区別する。incorporationは

\[
q_n=\operatorname{Inc}(g_n),\qquad
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n)
\]

と表され、単なるlog保存ではなくlater proof conditionを変える。

## 14.2 Example 2: Batter Becoming Cake

batterとcooking conditionsをStructureとし、Sliceはculinary readiness、chemical transformation、material continuity、product identityなど異なるOrientationの下で進み得る。

```text
The mixture has set into a cake-like form.
```

のようなarticulationはpre-existing answer extractionではなくSliceを通じてavailableになる。

\[
\operatorname{Id}_{q}(g_i,g_j)=\mathrm{false}
\]

でも

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma)=\mathrm{true}
\]

となり得る。

```text
identity break
≠
continuity break
```

## 14.3 Example 3: Authentication Across Changing Conditions

current authentication situationをStructureとし、device、behavior、network、time、motionなどのobservationsを扱う。local articulationは例えば

```text
The current session is consistent enough with the previously available user trajectory to continue provisionally.
```

Stabilityはnumerical authentication scoreそのものではなく、scoreは\(L_n\)のevidential componentの一つにすぎない。

Differenceは

\[
\Delta_{B,c,\Sigma}(x)=
(\Delta_{\mathrm{device}},\Delta_{\mathrm{behavior}},\Delta_{\mathrm{network}},\Delta_{\mathrm{time}},\Delta_{\mathrm{motion}})
\]

のようなheterogeneous objectであり得る。BoundaryはDifference tupleそのものではなく、ordinary driftとsuspicious behaviorを区切るlocally usable distinctionとして成立し得る。

## 14.4 Example 4: Historical Norm Formation

gender equalityのsocial recognitionを例に、society内のinstitutions、practices、conflicts、language、possible recognition formsをStructureとみなす。legal reform、public debate、social movement、education、institutional reinterpretationなどを通じてlocal articulationsが成立し得る。

```text
Equal treatment is recognized as a legitimate standard in this domain.
```

local Stability Sceneが成立しても、enforcement、cultural practice、exceptions、conflicting institutionsにlocal not-yetが残り得る。once incorporatedされるとequalityがlater law / dispute / interpretationのconditionを変える。

Trajectoryはchronological event listそのものではなく、movements、laws、decisions、institutions、practices間のrelationをどのContextの下でadmissible / traceableとするかにより変わる。

## 14.5 Example 5: Missing Data and Trajectory Gaps

sensor systemでmeasurement gapがあってもTrajectory breakとは限らない。before / after realizations間でadmissible relationをmodel constraints、material continuity、redundant sensors、later evidenceなどからtraceできる場合がある。

```text
record continuity
≠
Trajectory continuity
```

same event fieldでもdifferent contextual tracingsをsupportし得る。

## 14.6 Example 6: Search for “All Prefectures Except Kyushu”

「九州以外の都道府県」というqueryはdatabase上ではset differenceで実装できるが、Gyro Logicではnegative conditionがalready established classificationにrelativeにavailableになるSliceとして見る。

```text
prefectures that do not satisfy the current Kyushu-membership condition
```

Differenceはcategoricalであり得る。Boundaryはcurrent Sliceの下でusableなregional distinctionである。「Not Kyushu」「nothing」「unknown」「blank」「Void」を同一状態へcollapseしない。

## 14.7 Cross-Example Observations

examples全体を通して、Structureはcurrent observationへ還元されず、Sliceはpre-existing result retrievalへ還元されず、local articulationとStabilityは分離され、Stabilityはresidual not-yetを許し、Incorporated Readabilityはstored historyと区別され、Identity / relation existence / traceability / Continuity Readability / Trajectoryは分離され、Differenceはnon-metricでBoundaryと区別される。

# 15 Limitations and Open Problems

## 15.1 Scope of the Present Model

本モデルはintentionally limitedであり、complete axiomatization、universal semantics、final mathematical foundationを主張しない。conceptual theoryとdomain-specific implementationの中間に位置する。

## 15.2 Provisional Status of Mathematical Types

Structure、Slice、Stability、Context、Difference、Trajectoryについて一つのuniversal mathematical typeを決めない。

\[
S_n\xRightarrow{\Sigma_{B_n,c_n}}a_n
\]

も\(\Sigma\)をrelation / partial map / transition / process object / event / morphismのどれかへ最終確定しない。

\[
K_n=(a_n,L_n,U_n,C_n^{+})
\]

もevery Stability Sceneがintrinsically four-component tupleであるというclaimではない。

## 15.3 No Proof of Strict Minimality

本論文でいうminimalは、current theoretical distinctionsを維持するためにcurrently judged necessaryなformal commitmentsを増やしすぎないという意味であり、unique / cardinal / order-theoretic minimalityをproofしない。

より強いresultには、admissible formal model class、canonical concept preservation criterion、candidate models間のordering / comparison relation、component removalによるdistinction lossのproofが必要である。

## 15.4 Incomplete Semantics of Readability

ReadabilityはStability DefinitionやIncorporated Readability / Continuity Readabilityの名称においてimportant canonical / explanatory languageであるが、本モデルはcomplete universal semanticsを提供せず、`Readable(...)`をindependently validated universal predicateとはしない。

domain-specific readabilityがbinary predicate、graded quantity、contextual judgment、inferential availability relation、accessibility structure、observer-relative condition、heterogeneous family of domain-specific relationsのいずれであるべきかは未解決である。

formal conditionが必要な箇所では\(\operatorname{EstablishedFor}_{D}\)、\(\operatorname{CountsAsContinuity}_{D}\)のようなdomain-relative placeholderを用いる。

## 15.5 Orientation and Context Are Underspecified

Orientation / Contextのinternal structureはfully specifiedされていない。structured state / policy / relation / higher-order constraintなのか、Contextをavailable conditions / inferential closure / local environment / dynamic structureのどれとして扱うか、mutual interaction、conflicting Orientations、Slice中のContext changeなどはfuture workである。

## 15.6 Boundary Admissibility and Anti-Post-Hoc Limits

`slice-done`はlocal unitizationであり、local boundaryはcurrent Operator judgment、Orientation / Context、inherited protocol、institutional criteria、strong event-side transitionなどによって供給または制約される可能性がある。ただし、すべてのboundaryが必ずこれらの影響を受けるとは主張しない。

このflexibilityはadmissibility problemを生む。Operator-relativityは、boundary選択後にOrientation / Contextを都合よく再記述するだけでboundaryを正当化することを許してはならない。同様に、inherited boundaryもafter the factにprotocol / rule / institution由来だとassertするだけでは不十分で、claimed provenance自体にindependent supportが必要である。

Temporal priorityも単独では不十分であり、all plausible live alternativesをopenにするprior frameはほとんどconstraintにならない。present paperはmethodological anti-post-hoc constraintのみを採用し、universal theorem of boundary admissibility、universal specificity metric、domain-neutral procedure for live candidate boundariesをまだ提供しない。

## 15.7 Admissibility and Traceability Require Domain Criteria

\[
\operatorname{CR}(g_i,g_j;B,c,\Sigma,\Gamma)
\iff
\exists r\bigl(
\operatorname{Adm}(r)
\land
\operatorname{Traceable}(r)
\land
\operatorname{CountsAsContinuity}_{D}(r)
\bigr)
\]

はadmissibility、traceability、continuity judgmentを分離するが、それぞれのuniversal criteriaは定義しない。domain modelがpermitted relation type、evidence、conflicting relation handling、trace break、what counts as continuity、uncertainty representationをspecifyする必要がある。

## 15.8 Retrospective Establishment and Reliability

later Operatorは、availableなrelation、trace、consequence、record、later establishmentからearlier eventについてpresent establishmentを形成し得る。

```text
past event itself
≠
present establishment about that past event
```

Direct contemporaneous observationはevery retrospective establishmentに必須ではない。しかし

```text
a remaining trace may support retrospective establishment
≠
a single trace is sufficient to uniquely determine the past event
```

である。scorch markはlightning、arson、electrical fault、other heat sourceなどmultiple causesとcompatibleであり得る。

well-supported retrospective establishmentとmerely plausible storyを区別するuniversal reliability criterionはまだない。Trajectory、Re-Slice、Incorporated Readability、abduction / IBE、historical geology、forensic reasoning、historiographical methodとの関係はopenである。

## 15.9 Trajectory Reconstruction Is Not Yet Algorithmic

\[
\mathcal{G}_R=(G,E)
\]

と

\[
T_{B,c,\Sigma_T,\Gamma_T}=\operatorname{Trace}_{B,c,\Sigma_T,\Gamma_T}(G,E)
\]

を分離するが、tracing operatorのsearch order、stopping condition、conflict resolution、branch selection、gap handling、uncertainty propagation、retrospective revision cost、complexityは未定義である。

## 15.10 Difference Lacks a Universal Codomain

\[
\Delta_{B,c,\Sigma}:X\rightharpoonup D
\]

でheterogeneous codomainを許すため、different Difference typesのcomparison、composition、aggregation、propagationはopenである。

## 15.11 Stability Has No Universal Evaluation Rule

Stabilityをscoreから区別する一方、local articulationをestablishment that can continueと判断するuniversal procedureは提供しない。threshold、logical satisfaction、topological neighborhood、invariance、robustness、confidence interval、multi-criteria judgmentなどdomain-specific modelを許す。

## 15.12 Incorporated Readability Is Not Yet Operationally Identified

\[
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n,e_n)
\]

において、\(q_n\)をrealizationからどうextractするか、competing incorporated elementsをどうreconcileするか、ordinary memory / parameter updateとempiricallyどう区別するかは未解決である。

## 15.13 Empirical Validation Remains Limited

illustrative examplesはconceptual separabilityを示すがempirical validityは証明しない。explicit dataset / event trace、operational definition、baseline model、measurable success / failure criteria、reproducible experiment / simulationが必要である。GyroOS / GyroAuth PoC successもuniversal theory proofとはしない。

## 15.14 Relationship to Existing Mathematics Requires Deeper Study

local articulationとpartial algebra / event semantics、Stability Sceneとneighborhood / sheaf / domain theory、Incorporated Readabilityとnon-monotonic logic / belief revision、contextual tracingとpath category / event structure / provenance model、heterogeneous Differenceとenriched relations / order / typed field、continuing-event / local-unitization distinctionとevent boundedness / telicity / aspect / process theoryの関係をよりrigorousに比較する必要がある。

## 15.15 Open Problem: Formal Security and Adversarial Conditions

authentication / vulnerability responseへapplyする場合、attackerによるcriterion poisoning、Context alteration、fabricated continuity、Difference suppression、false Stabilityなどを扱うsecurity specializationが必要である。trusted / untrusted evidence、adversarial \(\Gamma\) update、Boundary manipulation、rollback / freeze / defer / review / isolation semanticsなどを定義する必要がある。

## 15.16 Open Problem: Formal Composition of Local Realizations

\[
g_n=(S_n,B_n,c_n,\Sigma_n,a_n,K_n)
\]

間のuniversal composition operator

\[
g_i\circ g_j
\]

は未定義である。compositionはtemporal、causal、logical、semantic、material、contextualであり得る。

## 15.17 Open Problem: Criteria for Model Revision

formal modelはprovisionalであるため、canonical definitionとconflictする、必要なdistinctionをcollapseする、unnecessary ontological assumptionsを導入する、important domainsでfailする、theoretical benefitなくimplementationを妨げる、observable / inferential evidenceへ接続できない場合にrevisionが必要となる。

## 15.18 Summary of Limitations

present modelは以下を提供しない。

- final ontology of Structure
- universal mathematical type for Slice
- complete universal semantics of readability
- universal Stability metric
- universal boundary-admissibility rule
- universal Difference codomain
- executable tracing algorithm
- general reliability criterion for retrospective establishment
- proof of strict minimality
- complete security model
- empirical validation across domains

提供するのは、どのdistinctionを維持し、どのreductionがcurrently unjustifiedで、どのcomponentにfuture developmentが必要かを示すdisciplined formal boundaryである。

# 16 Conclusion

本論文は、不変Core

```text
Structure
↓
Slice
↓
Stability
```

を維持したまま、Gyro Logicのexploratory Minimal Formal Modelを提示した。目的はCanonical Definitionをequationで置き換えることでも、Gyro Logicを単一既存数学分野へ還元することでもない。現在のtheoretical distinctionsを、theoryが要求するより強いcommitmentを導入せずcompact / internally consistentなformal schemaへ整理できるかを問うた。*minimal*はexploratory operational senseであり、strict mathematical minimalityは証明していない。

Structureはone universal mathematical object typeへ固定しない。SliceはSlice processとlocal articulationから分離され、`slice-done`はunderlying eventのobjective endではなくlocal unitizationとして明確化された。Stabilityはそのunitizationとは別であり、articulationを継続可能なestablishmentとして扱えるstructured local sceneとして表現され、residual local not-yetを許す。

Canonical term `readable`は維持するが、universal independent `Readable(...)` predicateは仮定しない。domain-specific formal modelが、operational precisionを必要とする箇所でestablishment、continuity、admissibility、tracingのjustified conditionsを与える必要がある。

Incorporated Readabilityはstored historyから分離され、later conditionsのpotentially non-monotonic updateとして扱われる。Continuity ReadabilityはIdentityと別であり、Trajectoryはstate sequence、log、event accumulationから分離され、local Gyro realizations間のadmissible relationsをcontextual tracingしたものとして扱う。Differenceはdistance、numerical error、Boundaryから分離され、Boundaryはderivative locally usable distinctionとして扱う。

integrated local realizationは

\[
g_n=(S_n,B_n,c_n,\Sigma_n,a_n,K_n)
\]

と表し、Core-relative relationは

\[
S_n\xRightarrow{\Sigma_{B_n,c_n}}a_n\xRightarrow{\operatorname{Stab}}K_n
\]

である。

incorporated contributionは

\[
q_n=\operatorname{Inc}(g_n)
\]

\[
\Gamma_{n+1}=\operatorname{Update}_{\Gamma}(\Gamma_n,q_n,e_n)
\]

とし、later Structure conditionsは

\[
(S_n,\Gamma_{n+1},e_n)\rightsquigarrow S_{n+1}
\]

と関係づけられる。

Continuity Readabilityは、admissible / traceable relationがdomain-relative continuity conditionを満たすこととしてcharacterizeされる。Trajectoryはrelation-bearing field上のcontextual tracing operation、Differenceはweakly typed partial heterogeneous mappingとして表現される。

本モデルが保持する主要区別は次である。

```text
Slice process
≠
local articulation / local unitization
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

existing mathematical fieldsとの比較から、relational structures、graphs、topology、dynamical systems、transition systems、category theory、proof theory、constraint propagation、process algebraなどはいずれもuseful partial modelとなる一方、単一分野がGyro Logic全体をadditional assumptionsなしにcaptureするとは現時点では言えない。したがって現在の適切なpositionは、mathematical isolationでもpremature reductionでもなく、domain-specific mathematical modelsをexplicit assumptionsの下で組み合わせるheterogeneous formal organizationである。

本論文はintroductory Gyro Logic paperのformalization companionとして読むべきである。introductory workは「Gyro Logicとは何か」を扱い、本論文はcurrent conceptual distinctionsをmathematical comparison、validation、later implementationのためにどのようにminimally organizeできるかを扱う。

future researchでは、domain-specific semantics of establishment/readability、admissibility、traceability、boundary provenance / admissibility、local-unitizationとevent/process theoriesの比較、retrospective establishmentとevidentiary / abductive methodologiesの比較、local realization composition、executable / simulation-based instantiation、non-monotonic Incorporated Readability、adversarial update / criterion poisoningなどを検討する必要がある。

present resultはdeliberately limitedであり、proposed schemaがuniquely minimal、empirically valid across domains、computationally decidable、complete、universal boundary / retrospective-reliability criteriaを持つとは証明しない。よりmodestなfoundationとして、Gyro Logicが不変Coreを変更せず、そのcentral distinctionsをnarrow pre-existing mathematical formsへcollapseさせることなくdisciplined formal organizationを持ち得ることを示す。

# Declarations

## Conflict of Interest

著者は、本研究に関連する利益相反がないことを宣言する。

## Funding

本研究は外部資金の提供を受けていない。

## Data Availability

本理論研究では、新たなempirical datasetの生成・分析は行っていない。

## Use of Generative AI and AI-Assisted Tools

本稿のstructure organization、drafting assistance、language refinement、consistency checkingに、generative AIおよびその他のAI-assisted toolsを使用した。著者はmanuscript content、theoretical claims、citations、references、final textをreview、verify、editし、本稿のすべての内容について最終的な責任を負う。

## Code and Materials Availability

manuscript sources、figures、assembly scripts、PDF-generation workflow、validation scriptsはGyro Logic repositoryで公開している: [https://github.com/gitGyro-Dev/gyrologic](https://github.com/gitGyro-Dev/gyrologic)。

# References
