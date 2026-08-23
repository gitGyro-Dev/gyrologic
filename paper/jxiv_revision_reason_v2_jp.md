# Jxiv 改訂理由 — Minimal Formal Model v2（日本語）

## Jxiv 改訂理由 推奨文

本改訂では、Gyro Logic の不変Core（`Structure → Slice → Stability`）を維持したまま、Minimal Formal Model におけるいくつかの理論上の区別を明確化しました。特に、`slice-done` を underlying event / process 自体の客観的な終了点ではなく、進行中の Slice の一部を一つの局所的成立として扱う local unitization として明確化し、local articulation / local unitization と Stability を区別しました。

また、readability の扱いを見直しました。Stability の canonical wording に含まれる `readable` は維持しますが、`Readable(...)` を普遍的に定義された独立の形式述語としては扱わず、形式的な readability 表記を用いる場合には、専門化された domain model が妥当な semantics を与えない限り、domain-relative な placeholder として扱うことを明示しました。

さらに、局所的な boundary は、現在の Operator の判断、Orientation / Context、継承された protocol や institutional criteria、強い event-side transition などによって供給・制約される可能性があることを整理しました。ただし、すべての boundary が必ず外部要因によって制約されるとは仮定していません。あわせて、boundary 選択後に Orientation / Context や boundary provenance を事後的に導入して正当化することを避けるため、最小限の anti-post-hoc 要件を追加しました。

加えて、retrospective establishment と過去の event 自体を区別しました。現在残っている trace が、過去の event について現在の成立を形成する根拠になり得る一方で、一つの trace だけから過去の event が一意に決定されるとはしないことを明記しました。

最後に、本論文における *minimal* は探索的・運用的な意味で使用しており、unique minimality、cardinal minimality、order-theoretic minimality の形式的証明を主張するものではないことを明確化しました。主要な図、既存数学分野との比較、worked examples、参考文献、および論証の全体構成は維持しています。

Canonical Core およびその順序に変更はありません。

## 短縮版

本改訂では、Gyro Logic のCore（`Structure → Slice → Stability`）を維持したまま、`slice-done` を underlying event の客観的終了ではなく local unitization として明確化し、`Readable(...)` を普遍的な形式述語ではなく domain-relative な placeholder として整理しました。また、局所的 boundary が Operator 判断、Orientation / Context、継承された rule / protocol、institutional criteria、event-side transition などによって供給・制約される可能性と、その provenance に対する anti-post-hoc 要件を明示しました。さらに、過去の event 自体と、trace 等に基づいて現在形成される retrospective establishment を区別しました。*minimal* は厳密な数学的最小性の証明ではなく、探索的・運用的な意味であることも明確化しています。主要な図、事例、数学分野との比較、参考文献、および論証は維持しています。