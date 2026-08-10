# External Review Record — Readable Semantics v1 — Gemini Round 2

## Review metadata

- Topic: `Readable(...)` candidate semantics v1
- Source file: `ideas/readable_semantics_v1.md`
- Source commit SHA: `19744a39d20b9c7e24ba6768cbb26fcfc2fde30a`
- Review round: 2
- Review date: 2026-08-10
- Reviewer/service: Gemini
- Model/version if known: not specified
- Review prompt:
  - `reviews/critical_review_prompt.md`
  - v1-specific focus points supplied in chat

## Source status

- [x] Revised exploratory note
- [ ] Paper candidate
- [ ] Pre-submission manuscript

## External review

指定された重度課題（反例の探索、概念の切り分け、非循環な再定義、既存理論との対比）に対し、**あえてv1を解体・再構築する勢いでクリティカルに講評**します。

### 1. PresentTo と LocallyDiscriminable の独立性と十分条件性

#### (1) 独立性の検証と具体例

両者は**論理的に独立**しており、明確に分離可能です。

- **`PresentTo(a; ρ) = true` ∧ `LocallyDiscriminable(a; ρ) = false`**
  - **例：** 高解像度カメラから取り込まれた画像データ全体（Slice済み）において、画面奥の背景ノイズの中に「移動体 `a`」を構成するピクセル群が存在している状態。実現範囲 `ρ` 内に物理的・データ構造的に到達（Present）しているが、S/N比が低すぎて背景と局所的に識別（Discriminable）できない。
- **`PresentTo(a; ρ) = false` ∧ `LocallyDiscriminable(a; ρ) = true`**
  - **例：** 完全に定義された記号的プロトタイプ（例：「赤信号」の識別境界ルール）。ルール自体はシステムにとって極めて明瞭（Discriminable）だが、現在の実行フレーム `ρ` においてセンサーからの入力データが存在しない（Not Present）。

#### (2) 反例：十分条件性の破綻（2条件を満たすが Readable と言えない例）

**反例1：構造的孤立（Structural Isolation / Scope Entrapment）**

- **状況：** ある暗号化モジュール内、またはアクセスメモリの保護領域において、データ `a` が計算され局所的パターンとして確立している（`PresentTo = true` 且つ `LocallyDiscriminable = true`）。しかし、実行コンテキスト `Γ` や境界 `Σ` の制約により、現在の `ρ` を構成する他のいかなる状態変化や評価プロセスからも物理的・論理的に参照アクセス線（Trace Line）が遮断されている。
- **判定：** `a` は `ρ` 内部で「立ち現れており、かつパターンとして独立している」が、システムからは「不可視・アクセス不能（Inaccessible）」であり、Readableとは言えません。

#### (3) 提案：不足している「第3の条件」

上記反例を防ぐため、`SelectivelyAddressable`（離散的アドレス指定）の代わりに、システム論的な `In-Scope / Traceable`（スコープ内到達可能性）を復元・統合する必要があります。

### 2. LocallyDiscriminable の循環性回避と定義候補

`LocallyDiscriminable`（局所的区別可能性）は、そのままでは「読める（Readable）」の類語反復になりがちです。非循環的に定義するには、情報理論や信号検出理論における「エントロピー低下」または「位相的隔離」として定式化するのが最も強固です。

#### 非循環的な定義候補

> **`LocallyDiscriminable(a; ρ)`**
>
> 実現 `ρ` の状態空間において、`a` を支持するサブ空間の相関・確率分布・エネルギー状態が、背景（残余：Undifferentiated Remainder）の分布に対して統計的または位相的に有意な境界（閾値）を形成していること。

「人間や演算器が認知できたか」ではなく、**「状態空間において自立した相を成しているか（Phase Separation）」** という物理的・構造的性質に落とし込むことで、「読める」との視点循環を完全に回避できます。

### 3. 分散表現（Distributed Representation）への適用可能性

**完全に適用可能です。** v1の改訂により、本モデルの汎用性は劇的に向上しました。

- **Deep Learningの Latent Representation / Distributed Activation:**

  1,024次元の潜在空間において、特定の領域（マニホールド）へのプロジェクションとして `a` が存在する場合、単一のノード（アドレス）は存在しません。
- しかし、その活性化パターン全体が他の領域と統計的に分離可能（`LocallyDiscriminable`）であり、現在の推論コンテキストに載っている（`PresentTo`）ならば、**「分散したアーティキュレーション `a` として Readable である」** と矛盾なく判定できます。

### 4. Realization Scope `ρ = (S, B, c, Σ, Γ)` の反証可能性

現状のままでは、「反例が出たら `ρ` のパラメタ（特にContext `c` や `Γ`）を微修正して『別の `ρ` だから成立する』と言い逃れできる」という**不可証性（Unfalsifiability）のリスク**が依然として残ります。

#### `ρ` の同一性維持のための最低限の規律案

1. **パラメータの不変量化（Parameter Invariance Requirement）：**
   検証対象となる文脈において、`S, B, c, Σ, Γ` の各要素は**観測前に静的仕様として固定**されなければならない。
2. **階層的変更の禁止：**
   `a` の Readable 判断が失敗した際、同一の Slice ループ `n` 内で `ρ` を再定義することは不可（`ρ_n → ρ_{n+1}` の遷移には必ず明示的な Re-Slice または Context Update イベントを要求する）。

### 5. Readable ⇏ True / Correct の妥当性

**完全に妥当であり、絶対に変更すべきではありません。**

LLMのハルシネーション（誤った確信）、自律走行車の誤認識（影を障害物と誤認）など、実体システムにおいて「誤ったアーティキュレーションがローカルに成立し、システムに利用可能になる」現象は日常茶飯事です。

- `Readable(a)` ＝ **存在論的・形態的成立（Morphological Establishment）**
- `Epistemic Correctness` ＝ **参照先（Structure / External World）との適合性（Mapping Accuracy）**

この2つを混同すると、Gyro Logicは「正解しか扱えない理想システム論」に退行してしまいます。

### 6. Slice-done / Stability との境界

| Concept | Position | Meaning |
|---|---|---|
| `slice-ing` | process | 切断・局所化の最中（形成過程） |
| `slice-done` | event/state | 局所化が完了し、アーティキュレーションが成立した瞬間 |
| `Readable(a)` | static property/state | `slice-done` によって生じたアーティキュレーションが、局所的に識別・利用可能であること |
| `Stable(a)` | dynamic property/continuity | `Readable(a)` であることに加え、時間的・操作的に「破綻せずに接続（Continuable）」できること |

`slice-done ⇒ Readable(a)` および `Stable(a) ⇒ Readable(a)` の階層構造は論理的に美しく整合しています。中間概念を増やす必要はありません。

### 7. 表現変換 `π(a) = d`（マシン内部表現 `a` と表示 `d`）

`a` と `d` の間で「同じ内容が読まれた」と言えるための保存条件候補：

- **Topology / Homomorphism Preservation（同相・同型保存）：**
  内部状態空間における `a` と他状態の「関係的距離（区分）」が、表示空間 `d` においても同一の位相・順序関係として保たれていること。
- **Information-Theoretic Mutual Information（相互情報量の保持）：**
  `I(a; d) ≈ H(a)` （`a` の持つ情報量が `d` への変換において決定的に欠損していないこと）。

### 8. 既存理論との比較分析

| Theory | Similar concept | Common point | Difference retained by Gyro Logic |
|---|---|---|---|
| Epistemic Logic | `K_i φ` | 明示的な命題の利用可能性 | エージェント（Subject）を要求しない。心理主義・主体依存からの脱却。 |
| Operational Semantics | Evaluation / Value | 状態遷移における値の確定 | 「計算結果」に限定されない。不完全・不確実・中間的な構造の立ち現れを扱える。 |
| Signal Detection Theory | Sensitivity (`d'`) / Criterion | ノイズと信号の区別可能性 | 数値的閾値ではなく、構造的成立（Articulation）を扱う点。 |

### 9. 代替アイデアの提案：さらなる単純化と解体

あえて現在の `v1` を壊し、より明確で不可逆な定義を与える候補を提示します。

#### 新定義案：`Scope-Relative Phase Separation`

```text
Readable(a; ρ)
:=
InScope(a; ρ) ∧ PhaseSeparated(a; ρ)
```

| Item | Content |
|---|---|
| Candidate Definition | `a` が `ρ` の作用範囲内（`InScope`）に存在し、かつその背景状態空間から統計的・位相的に相分離（`PhaseSeparated`）していること。 |
| Assumptions | 状態空間における位相的・情報論的境界の存在。 |
| Counterexample Test | 暗号化された完全なデータ（`PhaseSeparated` だが `InScope`（アクセス可能性）が偽のため Unreadable）。 |
| Advantage | 「認知」「読める」「アドレス指定」といった人間の言語・計算機パラダイム的メタファーを完全排除できる。 |
| Weakness | Gyro Logic が持つ「意味論（Semantics）」的な質感が極限まで薄れ、純粋な物理・情報幾何学の述語に見える。 |

### 総評と次のステップ

`v1` は `v0` の弱点をほぼ克服しており、論文候補（Paper Candidate）に極めて近づいています。

次回の改訂（`v2`）に向けては、**`LocallyDiscriminable` を情報論的・位相的用語（相分離）で非循環的に補強すること** と **`InScope`（アクセス線）の必要性を反例に基づいて検討すること** の2点に絞ってブラッシュアップされることを強く推奨します。

---

## Claim-by-claim assessment

| ID | Review criticism / proposal | Type | Decision | Reason / verification | Required change |
|---|---|---|---|---|---|
| GR2-1 | `PresentTo` and `LocallyDiscriminable` can be separated by examples | definitional | accept-for-investigation | Useful distinction, but the proposed `PresentTo=false ∧ Discriminable=true` example may describe a prototype/rule rather than the same articulation instance | Add stronger worked independence tests before treating logical independence as established |
| GR2-2 | Two-condition sufficiency may fail under structural isolation | counterexample | verify | Strong pressure test, but `InScope` may overlap with what `PresentTo` was intended to encode | Formalize the isolation case and test whether it truly satisfies `PresentTo` as defined in v1 |
| GR2-3 | Add `InScope` / `Traceable` as a third condition | definitional | defer | Potentially useful, but risks reintroducing accessibility/process-topology assumptions removed from v0 | Test as a candidate, not adopt immediately |
| GR2-4 | Define `LocallyDiscriminable` as phase separation / statistical-topological boundary | existing-theory / definitional | partial | Helpful domain instantiation, but too strong as a universal Gyro Logic definition because some domains may lack metric/probability/topology | Keep as specialization candidate; seek weaker structural definition |
| GR2-5 | Distributed representations remain compatible | counterexample/generalization | accept | Consistent with v1's removal of discrete addressability | Retain and strengthen distributed-pattern examples |
| GR2-6 | Strengthen `ρ` falsifiability with pre-fixed parameters and explicit transitions | methodology | partial | Pre-fixing every parameter may be too rigid, but explicit independent change criteria are useful | Add comparison protocol without requiring universal static fixation |
| GR2-7 | Preserve `Readable ⇏ True / Correct` | logical | accept | Strongly supported by current examples and theory boundary | Retain |
| GR2-8 | `slice-done ⇒ Readable` and `Stable ⇒ Readable`; no new intermediate concept needed | cross-document | verify | Plausible and consistent with current Core wording, but must be checked against current Core/Stability docs | Cross-document verification required |
| GR2-9 | `π` should preserve topology/homomorphism or mutual information | representational | defer | These are useful specializations, not obviously universal minimum conditions | Keep as candidate transfer properties only |
| GR2-10 | Replace v1 with `InScope ∧ PhaseSeparated` | alternative definition | reject-as-universal / keep-as-specialization | Introduces stronger state-space/statistical/topological commitments than Gyro Logic currently permits | Preserve as domain-specific candidate for later comparison |

## Counterexamples to carry forward

### C-G2-1 Structural isolation

- Candidate: `PresentTo(a; ρ)=true` and `LocallyDiscriminable(a; ρ)=true`, yet `a` is inaccessible to the rest of the relevant realization.
- Pressure target: sufficiency of the two-condition candidate.
- Key unresolved issue: whether the example really satisfies `PresentTo` under v1's intended meaning, or instead reveals that `PresentTo` was underspecified.
- Status: `VERIFY`

### C-G2-2 Distributed latent representation

- Candidate: no discrete address or token, but a population/manifold-level distinction is discriminable.
- Pressure target: any return to discrete `Addressable` semantics.
- Status: `ACCEPT`

## Existing-theory comparison cautions

Gemini proposes information-theoretic, signal-detection, topological, epistemic-logic, and operational-semantics comparisons. These should be treated as comparison candidates rather than foundations. In particular, `PhaseSeparated` as defined through probability distributions, energy states, entropy, or topology would impose stronger assumptions than the current Gyro Logic formalization permits.

## Fix now / keep provisional

### Can be fixed now

- Add the structural-isolation counterexample explicitly.
- Clarify whether `PresentTo` already includes realization-scope accessibility.
- Strengthen the `ρ` comparison discipline using independently identified changes.
- Preserve distributed representation and truth/correctness separation.

### Should remain provisional

- A universal third condition such as `InScope` or `Traceable`.
- `PhaseSeparated` as a universal definition of `LocallyDiscriminable`.
- Topological / mutual-information preservation as universal requirements for `π`.
- The claim that `PresentTo` and `LocallyDiscriminable` are fully logically independent.

## Revision outcome

- Updated file: pending
- Revision commit SHA: —
- Major changes: —
- Remaining open questions: two-condition sufficiency, scope accessibility, non-circular discriminability, cross-document Stability dependency, representation transfer
- Another external review round required?: yes

## Review gate status

```text
REVISION_REQUIRED
```

Current status: `REVISION_REQUIRED`

## Layer consistency check

- Gyro Logic theory only: yes
- GyroOS requirements imported?: no
- GyroAuth requirements imported?: no
- Core changed?: no
- If Core challenged by reviewer, preserved as review criticism rather than automatically adopted?: yes
